"""Where is the multiplicative triangle inequality TIGHT?

The Mathematical Compendium proves d(x,z) <= d(x,y)*d(y,z) coordinatewise, with
d(x,y) = prod_i (|x_i - y_i| + 1), and then glosses the equality case:

    "Equality holds on an axis iff st = 0, i.e. y lies between x and z there, so
     global equality iff y in [x /\ z, x \/ z] -- y on a geodesic;
     4,000 of 4,000 sampled triples satisfy the inequality."

with s = |a-b| and t = |b-c| on the axis.  THE TWO HALVES OF THAT "i.e." ARE NOT THE
SAME CONDITION.  st = 0 says b coincides with a or with c.  Betweenness allows both s
and t positive.  So the first clause is right, the gloss is strictly weaker, and the
conclusion drawn from the gloss -- the equality set is the ORDER INTERVAL -- is wrong:
the equality set is the VERTEX SET of the interval.

This program measures the gap.  It does not repair the text.

WHAT IT DOES
  1. Proves the per-axis equality case from the arithmetic the Compendium itself gives:
     the right side is st+s+t+1, the left |a-c|+1, and equality forces st = 0.
  2. Exhibits the counterexample the gloss admits and the arithmetic forbids:
     a = 0, b = 1, c = 2 -- b between a and c, st = 1, 3 against 4.
  3. Counts, for every ordered pair of DISTINCT points of an axis range, the points
     that are between against the points that give equality.
  4. Over the seated Lambda_8, takes every unordered pair of cells and compares the
     order interval's size prod(Delta_i + 1) against the equality set's size 2^k,
     k the number of axes on which the pair differs.  Reports the largest ratio and
     where it falls.
  5. Repeats (4) inside Lambda_8 -- how many cells OF THE LATTICE lie in the interval
     and how many give equality -- because the interval is a box in Z^8 and Lambda_8
     is a proper subset of its box, so the ambient figure is an upper bound on what a
     reader of the book could actually exhibit.

INPUT
  method/members/tower-2.py -- the seated member, imported by path, never copied.

REFUSALS
  It offers no verdict on the sampling sentence.  "4,000 of 4,000 sampled triples
  satisfy the inequality" is true and was never in question: the inequality is proved.
  A sample of the inequality cannot see a fault in the equality case, and this program
  does not read the sentence as if it had claimed to.

  It does not say the Compendium's global-equality conclusion is unreachable.  Where
  x and z differ on every axis by exactly 1, interval and vertex set coincide, and the
  gloss and the arithmetic agree.  The claim is about the general case, and the ratio
  reported below is where they part.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, itertools, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")

# The Compendium's own quoted gloss, so the object under test is on the page.
GLOSS = ("Equality holds on an axis iff st = 0, i.e. y lies between x and z there, "
         "so global equality iff y ∈ [x∧z, x∨z] — y on a geodesic")


def load_tower(members):
    path = os.path.join(members, "tower-2.py")
    spec = importlib.util.spec_from_file_location("tower2", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def d(x, y):
    """The Compendium's distance: prod over axes of (|Delta| + 1)."""
    p = 1
    for a, b in zip(x, y):
        p *= abs(a - b) + 1
    return p


def between(a, b, c):
    return min(a, c) <= b <= max(a, c)


def axis_equal(a, b, c):
    """Does the per-axis inequality (|a-c|+1) <= (|a-b|+1)(|b-c|+1) hold with equality?"""
    return abs(a - c) + 1 == (abs(a - b) + 1) * (abs(b - c) + 1)


def axis_census(lo, hi):
    """Over every (a, b, c) in [lo, hi]^3 with a != c: between vs equality."""
    btw = eq = both = 0
    for a in range(lo, hi + 1):
        for c in range(lo, hi + 1):
            if a == c:
                continue
            for b in range(lo, hi + 1):
                B = between(a, b, c)
                E = axis_equal(a, b, c)
                btw += B
                eq += E
                both += (B and E)
    return btw, eq, both


def interval_size(x, z):
    p = 1
    for a, b in zip(x, z):
        p *= abs(a - b) + 1
    return p


def vertex_count(x, z):
    return 2 ** sum(1 for a, b in zip(x, z) if a != b)


def ambient_census(cells):
    """Over every unordered pair of distinct cells: interval size against vertex count."""
    best = (0, None, 0, 0)
    pairs = 0
    for x, z in itertools.combinations(cells, 2):
        pairs += 1
        iv = interval_size(x, z)
        vt = vertex_count(x, z)
        r = iv // vt
        if r > best[0]:
            best = (r, (x, z), iv, vt)
    return pairs, best


def lattice_census(cells, sample):
    """Inside Lambda_8: cells of the lattice in the interval, against cells giving equality.

    Equality for the triple (x, y, z) is d(x,z) == d(x,y)*d(y,z), tested directly.
    Restricted to a sample of pairs because the full sweep is 976 * 475,800."""
    S = cells
    worst = (0, None, 0, 0)
    tot_iv = tot_eq = 0
    for x, z in sample:
        iv = eq = 0
        for y in S:
            if all(min(a, b) <= v <= max(a, b) for a, b, v in zip(x, z, y)):
                iv += 1
                if d(x, z) == d(x, y) * d(y, z):
                    eq += 1
        tot_iv += iv
        tot_eq += eq
        if eq and iv // eq > worst[0]:
            worst = (iv // eq, (x, z), iv, eq)
    return tot_iv, tot_eq, worst


def report(cells):
    print("THE GLOSS UNDER TEST (Mathematical Compendium, the metric entry)")
    print("  " + GLOSS)
    print()

    print("1. THE PER-AXIS ARITHMETIC, FROM THE COMPENDIUM'S OWN TERMS")
    print("   right side (|a-b|+1)(|b-c|+1) = st + s + t + 1 ; left side |a-c|+1 <= s + t + 1")
    print("   so equality forces st = 0, i.e. b = a or b = c.  Betweenness does not force it.")
    bad = [(a, b, c) for a in range(4) for b in range(4) for c in range(4)
           if between(a, b, c) and not axis_equal(a, b, c)]
    print("   triples in [0,3] that are BETWEEN and not EQUAL: %d" % len(bad))
    a, b, c = 0, 1, 2
    print("   the smallest: a=%d b=%d c=%d -- st=%d, b is between, |a-c|+1 = %d against (%d)(%d) = %d"
          % (a, b, c, abs(a - b) * abs(b - c), abs(a - c) + 1,
             abs(a - b) + 1, abs(b - c) + 1, (abs(a - b) + 1) * (abs(b - c) + 1)))
    print()

    print("2. BETWEEN AGAINST EQUAL, COUNTED ON ONE AXIS")
    for hi in (3, 5, 9):
        btw, eq, both = axis_census(0, hi)
        print("   range [0,%d]: between %5d   equality %5d   equality is a subset of between: %s"
              % (hi, btw, eq, both == eq))
    print()

    print("3. THE SETS THE TWO READINGS NAME, OVER LAMBDA_8")
    print("   %d cells; the interval [x/\\z, x\\/z] has prod(Delta_i + 1) points," % len(cells))
    print("   the equality set has 2^k, k the number of axes on which x and z differ.")
    pairs, (r, xz, iv, vt) = ambient_census(cells)
    print("   over all %s unordered pairs of cells:" % format(pairs, ","))
    print("     largest interval-to-vertex ratio : %d" % r)
    print("     at interval %s against %s vertices" % (format(iv, ","), format(vt, ",")))
    print("     x = %s" % (xz[0],))
    print("     z = %s" % (xz[1],))
    print()

    print("4. AND INSIDE LAMBDA_8, WHICH IS WHAT A READER COULD EXHIBIT")
    print("   the interval is a box in Z^8 and Lambda_8 is a proper subset of its box,")
    print("   so the ambient ratio above is an upper bound on the ratio among real cells.")
    sample = list(itertools.combinations(cells[:: len(cells) // 12], 2))
    tot_iv, tot_eq, worst = lattice_census(cells, sample)
    print("   over %d pairs sampled evenly across the cell list:" % len(sample))
    print("     cells of Lambda_8 in the intervals   : %s" % format(tot_iv, ","))
    print("     cells of Lambda_8 giving equality    : %s" % format(tot_eq, ","))
    if worst[1]:
        print("     largest ratio on a single pair       : %d (%d in the interval, %d equal)"
              % (worst[0], worst[2], worst[3]))
    print()

    print("5. WHERE THE TWO READINGS AGREE")
    agree = sum(1 for x, z in itertools.combinations(cells, 2)
                if interval_size(x, z) == vertex_count(x, z))
    print("   pairs whose interval IS its vertex set (every Delta_i is 0 or 1): %s of %s"
          % (format(agree, ","), format(pairs, ",")))
    print("   For those the gloss and the arithmetic name the same set, which is why a")
    print("   reader checking small examples would not meet the fault.")
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest(cells):
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    # The object identifies itself: the seated lattice's own printed size.
    chk("Lambda_8 cells", len(cells), 976)
    chk("unordered pairs of cells", len(cells) * (len(cells) - 1) // 2, 475800)

    # The counterexample, which is the whole finding.
    chk("d((0,),(2,)) -- the left side", d((0,), (2,)), 3)
    chk("d((0,),(1,)) * d((1,),(2,)) -- the right", d((0,), (1,)) * d((1,), (2,)), 4)
    chk("b=1 is between a=0 and c=2", between(0, 1, 2), True)
    chk("st = 0 at that triple", abs(0 - 1) * abs(1 - 2) == 0, False)
    chk("so the axis is BETWEEN and NOT EQUAL", (between(0, 1, 2), axis_equal(0, 1, 2)), (True, False))

    # Equality is exactly st = 0, over a range wide enough to be more than the counterexample.
    chk("equality iff st = 0 on [0,9]^3",
        all(axis_equal(a, b, c) == (abs(a - b) * abs(b - c) == 0)
            for a in range(10) for b in range(10) for c in range(10)),
        True)
    # And equality is a proper subset of betweenness, not equal to it.
    btw, eq, both = axis_census(0, 3)
    chk("[0,3]: equality is contained in betweenness", both == eq, True)
    chk("[0,3]: and properly -- between exceeds equal", btw > eq, True)

    # The inequality itself, which was never in question and is asserted here so the
    # finding cannot be read as doubting it.
    chk("the multiplicative inequality holds on 4,000 triples of Lambda_8",
        all(d(x, z) <= d(x, y) * d(y, z)
            for x, y, z in (
                (cells[(7 * i) % 976], cells[(29 * i + 3) % 976], cells[(61 * i + 11) % 976])
                for i in range(4000))),
        True)

    # The magnitude.  A second session reported "up to 6,561x on Lambda's eight axes";
    # 6,561 is 3^8, an estimate of the box, not a ratio.  Measured, the answer is 27.
    pairs, (r, xz, iv, vt) = ambient_census(cells)
    chk("pairs censused", pairs, 475800)
    chk("largest interval-to-vertex ratio", r, 27)
    chk("the interval it falls at", iv, 6912)
    chk("the vertex set it falls at", vt, 256)
    box = 1
    for i in range(8):
        box *= max(c[i] for c in cells) - min(c[i] for c in cells) + 1
    chk("and that interval is Lambda_8's own box, prod(span_i + 1)", box, iv)
    chk("3^8 is not reachable: not every axis of Lambda_8 spans Delta = 2",
        sorted({max(c[i] for c in cells) - min(c[i] for c in cells) for i in range(8)}),
        [1, 2, 3])

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    cells = load_tower(MEMBERS).L8()
    if a.selftest:
        selftest(cells)
    else:
        report(cells)
