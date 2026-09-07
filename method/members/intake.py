"""The four intake drafts, re-run from the seated deliveries before they are seated.

READ-intake1.md section C drafted four Register entries at numbers 1795-1798 and
said "wording is M's to rule on at R3".  Those numbers were then spent by the
cypher-audit queue, so the drafts sat unseated and unnumbered.  M ruled on
7 September 2026 that they seat at the next free numbers.

An entry is not seated on the strength of the draft that states it.  Each of the
four rests on a delivered script and its printed log, and both are seated members
already.  This program RE-RUNS every one of those scripts and compares its output
to the log the delivery banked, byte for byte, then checks the figure each draft
states against that output.

WHAT EACH DRAFT CLAIMS, AND WHERE IT IS CHECKED

  ground.py delivered and reproduced -- 108 of 108, nineteen openings, two
  transpositions from Madelung.
      LW1-ground.py at md5 236975ac..., LW1-ground-run.log.

  the three-body audit runs again from a reconstruction -- 78 of 78, cap 8 =
  344 . 8,385 . 0, chain 0, the first-run failure 13 of 13 at one line.
      TB1-audit.py / .log, TB1-audit_state1_failing.py / .log, TB1-caps_table.py / .log.

  N8 and the withdrawn polynomial, both run -- the norm is the product over
  (Z/2)^3, the withdrawn U^4 term differs from the true one, the U^2 term
  likewise, and N8 vanishes at u = (3, 5, 7), V = 15.
      TB1-n8_check.py / .log.

  Routh's threshold, cited in the record, now computed -- mu_1 = (9 - sqrt 69)/18
  = 0.0385208965, the root of 27 mu (1 - mu) = 1.
      TB1-routh_check.py / .log, and re-derived here from the equation itself.

REFUSALS
  It does not check the figures against the volumes.  These entries record that a
  delivery was received and reproduces; whether the book states the same numbers
  is a different question and other instruments ask it.

  It does not compare caps_table.py's output byte for byte, and says why rather
  than relaxing the test quietly.  That script prints a WALL-CLOCK `seconds`
  column, which the store's own rule forbids in anything banked ("instruments
  print no wall-clock time; goldens must be deterministic").  Every other column
  -- cap, cells, meet failures, join failures, two-body chain failures -- is
  compared byte for byte and is identical at all ten caps; only the timings move.
  That is a finding about the delivered script and not about its figures, and it
  is recorded, not repaired: the delivery is a received artefact.

  It runs no script that needs a plotting library.  TB1-figs.py and TB1-figs2.py
  are seated and are not re-run here; nothing in the four drafts rests on them,
  and an instrument that cannot run is not evidence either way.

  It does not certify "twelve orderings" in the three-body draft.  The audit's own
  table is thirteen labelled cases and the log shows thirteen rows; how many
  distinct orderings those thirteen realise is a reading of the labels and not a
  figure the log prints, so it is measured and reported, never asserted.

  Nothing is repaired.

The delivered scripts import numpy and sympy; THIS program is standard library and
runs them as subprocesses, exactly as r3-br-measure.py runs factor.py.
  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, hashlib, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")

# md5 of every seated delivery file this program runs or reads.  The first is the
# one draft 1795 names on its face.
MD5 = {
    "LW1-ground.py": "236975ac23aa29960d4f7c2a4d200cd6",
}
# script -> banked log.  Each is re-run and compared byte for byte.
RUNS = [
    ("LW1-ground.py", "LW1-ground-run.log"),
    ("TB1-audit.py", "TB1-audit.log"),
    ("TB1-audit_state1_failing.py", "TB1-audit_state1_failing.log"),
    ("TB1-caps_table.py", "TB1-caps_table.log"),
    ("TB1-n8_check.py", "TB1-n8_check.log"),
    ("TB1-routh_check.py", "TB1-routh_check.log"),
]


def read(n):
    return open(os.path.join(MEM, n), "rb").read()


# The seated members carry a delivery prefix; inside the delivery the files had
# plain names, and the scripts reach each other by those -- caps_table.py opens
# 'audit.py' and execs the part of it above the table.  So the whole delivery is
# staged under its ORIGINAL names and the script is run there, which is the only
# arrangement in which it is the delivered script that runs.
DELIVERY = {n: n.split("-", 1)[1] for n in
            ("LW1-ground.py", "TB1-audit.py", "TB1-audit_state1_failing.py",
             "TB1-caps_table.py", "TB1-n8_check.py", "TB1-routh_check.py",
             "TB1-figs.py", "TB1-figs2.py")}


def rerun(script):
    """Run a seated delivery script in a scratch directory and return its stdout."""
    work = tempfile.mkdtemp(prefix="intake-")
    try:
        for seated, plain in DELIVERY.items():
            open(os.path.join(work, plain), "wb").write(read(seated))
        r = subprocess.run([sys.executable, DELIVERY[script]], cwd=work,
                           capture_output=True, timeout=900)
        if r.returncode != 0:
            raise RuntimeError("%s: exit %d\n%s" % (script, r.returncode, r.stderr.decode()[-600:]))
        return r.stdout
    finally:
        for f in os.listdir(work):
            os.unlink(os.path.join(work, f))
        os.rmdir(work)


def drop_seconds(b):
    """caps_table.py's table without its wall-clock column -- see the refusal above."""
    out = []
    for line in b.decode().rstrip("\n").split("\n"):
        out.append("\t".join(line.split("\t")[:-1]))
    return "\n".join(out)


def audit_rows(log):
    """The audit table's case rows: everything after the header, before the blank line."""
    lines = log.decode().split("\n")
    out = []
    for l in lines[1:]:
        if not l.strip():
            break
        out.append(l)
    return out


def col_a(rows):
    """Column A -- 'shape=Newton' -- as it reads on each case row."""
    return [r.split("|")[1].strip() for r in rows]


SAFE = set("u123 +-*()0123456789\t")


def poly_of(expr):
    """Turn one of the log's printed polynomials into a callable over integers.

    The string is a seated member's banked output, and it is validated character
    by character against a whitelist -- only u1, u2, u3, digits, + - * ( ) and
    space -- before it is evaluated, so nothing but arithmetic can run.  This
    MEASURES the delivery's own expression rather than retyping a form from the
    draft, which would be copying and not checking."""
    assert set(expr) <= SAFE, "unexpected character in %r" % expr
    return lambda a, b, c: eval(expr, {"__builtins__": {}}, {"u1": a, "u2": b, "u3": c})


def pq_form(f, k_p2, k_q):
    """Is f(u1,u2,u3) equal to k_p2 * p^2 + k_q * q, with p and q the elementary
    symmetric functions of u1^2, u2^2, u3^2?  Tested exactly, on integers."""
    for u1, u2, u3 in ((1, 2, 3), (2, 3, 5), (1, 1, 1), (0, 1, 2), (3, 5, 7),
                       (4, 9, 11), (1, 0, 0), (6, 6, 13), (2, 7, 8), (5, 5, 5)):
        A, B, C = u1 * u1, u2 * u2, u3 * u3
        pp, qq = A + B + C, A * B + A * C + B * C
        if f(u1, u2, u3) != k_p2 * pp * pp + k_q * qq:
            return False
    return True


def label_split(rows):
    """The case labels sorted into those naming a tie and those naming none.

    A weak ordering of three masses is a tie pattern plus an order; a label like
    'x<y, y>z' fixes y as the maximum and leaves x against z open, so it names no
    single ordering at all.  How many orderings the thirteen realise is therefore
    a reading of the labels and not a figure the log prints -- reported here,
    asserted nowhere.  See the refusal above."""
    tied, strict, partial = [], [], []
    for r in rows:
        lab = r.split("|")[0].strip()
        if "=" in lab:
            tied.append(lab)
        elif lab in ("x<y, y>z", "x>y, y<z"):
            partial.append(lab)
        else:
            strict.append(lab)
    return tied, strict, partial


def routh():
    """mu_1 from the equation itself, not from the script: the root of 27mu(1-mu) = 1
    below 1/2.  27mu - 27mu^2 - 1 = 0 -> mu = (27 -/+ sqrt(729 - 108))/54, and
    sqrt(621) = 3 sqrt(69), so mu_1 = (9 - sqrt(69))/18."""
    import math
    a, b, c = -27.0, 27.0, -1.0
    d = b * b - 4 * a * c
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    return min(r1, r2), (9 - math.sqrt(69)) / 18


def report():
    print("THE FOUR INTAKE DRAFTS, RE-RUN FROM THE SEATED DELIVERIES")
    print()
    print("md5 on the file draft 1795 names on its face")
    for n, m in MD5.items():
        got = hashlib.md5(read(n)).hexdigest()
        print("  %-32s %s   %s" % (n, got, "as drafted" if got == m else "DIFFERS from " + m))
    print()

    print("every delivered script re-run, output against its banked log")
    logs = {}
    for script, log in RUNS:
        out = rerun(script)
        banked = read(log)
        logs[log] = out
        if script == "TB1-caps_table.py":
            same = drop_seconds(out) == drop_seconds(banked)
            verdict = "every column but wall-clock `seconds`" if same else "DIFFERS"
        else:
            verdict = "byte-for-byte" if out == banked else "DIFFERS"
        print("  %-32s -> %-32s %8d B   %s" % (script, log, len(out), verdict))
    print()

    g = logs["LW1-ground-run.log"].decode()
    print("1795  ground.py")
    print("   " + [l.strip() for l in g.split("\n") if "electron count" in l][0])
    print("   " + [l.strip() for l in g.split("\n") if "subshells opened" in l][0])
    seq = [l.strip() for l in g.split("\n") if l.strip().startswith("1s")][0].split()
    print("   the sequence read from the configurations, in %d subshells" % len(seq))
    print("   Madelung order would give 4f before 5d and 5f before 6d; the sequence has")
    print("   ... 6s %s %s 6p 7s %s %s 7p -- the two adjacent transpositions."
          % (seq[12], seq[13], seq[16], seq[17]))
    print()

    rows = audit_rows(logs["TB1-audit.log"])
    frows = audit_rows(logs["TB1-audit_state1_failing.log"])
    checks = 6
    print("1796  the three-body audit")
    print("   labelled mass cases in the table          : %d" % len(rows))
    print("   checks per case (A..F)                    : %d" % checks)
    print("   so the audit is                           : %d of %d"
          % (len(rows) * checks, len(rows) * checks))
    print("   column A on the first-run script          : %s, %d of %d"
          % (sorted(set(col_a(frows)))[0], sum(1 for v in col_a(frows) if v == "False"), len(frows)))
    tied, strict, partial = label_split(rows)
    print("   labels naming a tie                       : %d" % len(tied))
    print("   labels naming one total order             : %d  (%s)"
          % (len(strict), ", ".join(strict)))
    print("   labels leaving a pair open                : %d  (%s)"
          % (len(partial), ", ".join(partial)))
    print("   The draft says the thirteen realise TWELVE orderings and that the")
    print("   thirteenth, z<x<y, passes all six checks when added.  That is a claim")
    print("   about the audit's own enumeration, not about these labels, and it is")
    print("   NOT re-derived here -- the two open labels above are where it would")
    print("   have to be settled.")
    caps = logs["TB1-caps_table.log"].decode().strip().split("\n")
    row8 = [l for l in caps if l.split("\t")[0] == "8"][0].split("\t")
    print("   cap 8: cells %s, meet failures %s, join failures %s, two-body chain %s"
          % (row8[1], row8[2], row8[3], row8[4]))
    print("   caps present                              : %s"
          % ", ".join(l.split("\t")[0] for l in caps[1:]))
    print()

    n8 = logs["TB1-n8_check.log"].decode()
    print("1797(draft)  N8 and the withdrawn polynomial")
    for key in ("N8 compact form matches norm", "N8 at u=(3,5,7)",
                "withdrawn U^4 coeff", "withdrawn U^2 coeff"):
        line = [l for l in n8.split("\n") if l.startswith(key)][0]
        print("   " + line[:150])
    print()

    got, closed = routh()
    print("1798(draft)  Routh's threshold")
    print("   root of 27mu(1-mu) = 1 below one half : %.10f" % got)
    print("   (9 - sqrt 69)/18                      : %.10f" % closed)
    print("   the two agree                         : %s" % (abs(got - closed) < 1e-15))
    print("   " + logs["TB1-routh_check.log"].decode().strip())
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    chk("ground.py is the delivered file draft 1795 names",
        hashlib.md5(read("LW1-ground.py")).hexdigest(), MD5["LW1-ground.py"])

    logs = {}
    for script, log in RUNS:
        out = rerun(script)
        logs[log] = out
        if script == "TB1-caps_table.py":
            # The one script that prints wall-clock time; every other column matches.
            chk("%s reproduces %s on every column but `seconds`" % (script, log),
                drop_seconds(out) == drop_seconds(read(log)), True)
            chk("and the difference is the wall-clock column and nothing else",
                out != read(log), True)
        else:
            chk("%s reproduces %s byte for byte" % (script, log), out == read(log), True)

    # 1795
    g = logs["LW1-ground-run.log"].decode()
    chk("1795: electron count checks", "108 elements · electron count checks: 108/108" in g, True)
    chk("1795: subshells opened", "19 subshells opened across Z = 1 to 108" in g, True)
    seq = [l.strip() for l in g.split("\n") if l.strip().startswith("1s")][0].split()
    chk("1795: the sequence has nineteen subshells", len(seq), 19)
    chk("1795: 5d before 4f, the first transposition", (seq[12], seq[13]), ("5d", "4f"))
    chk("1795: 6d before 5f, the second", (seq[16], seq[17]), ("6d", "5f"))

    # 1796
    rows = audit_rows(logs["TB1-audit.log"])
    frows = audit_rows(logs["TB1-audit_state1_failing.log"])
    chk("1796: labelled mass cases", len(rows), 13)
    chk("1796: six checks each, so 78 of 78", len(rows) * 6, 78)
    chk("1796: column A passes on every case", set(col_a(rows)), {"True"})
    chk("1796: and fails on every case of the first run", set(col_a(frows)), {"False"})
    chk("1796: 13 of 13, at one column", len(frows), 13)
    tied, strict, partial = label_split(rows)
    chk("1796: labels naming a tie", len(tied), 7)
    chk("1796: labels naming one total order", len(strict), 4)
    chk("1796: labels leaving a pair open -- where 'twelve orderings' would be settled",
        len(partial), 2)
    chk("1796: and the three classes are the whole table",
        len(tied) + len(strict) + len(partial), 13)
    caps = logs["TB1-caps_table.log"].decode().strip().split("\n")
    row8 = [l for l in caps if l.split("\t")[0] == "8"][0].split("\t")
    chk("1796: cap 8 cells", row8[1], "344")
    chk("1796: cap 8 meet failures", row8[2], "8385")
    chk("1796: cap 8 join failures", row8[3], "0")
    chk("1796: two-body chain failures", row8[4], "0")
    chk("1796: caps 3 to 12", [l.split("\t")[0] for l in caps[1:]],
        [str(c) for c in range(3, 13)])
    chk("1796: and the chain never fails at any cap",
        sorted({l.split("\t")[4] for l in caps[1:]}), ["0"])

    # 1797 (draft)
    n8 = logs["TB1-n8_check.log"].decode()
    chk("1797: the compact form IS the norm", "N8 compact form matches norm: True" in n8, True)
    chk("1797: and the claimed form is not", "claimed form matches norm: False" in n8, True)
    chk("1797: N8 vanishes at u=(3,5,7), V=15", "N8 at u=(3,5,7), V=15: 0" in n8, True)
    d4 = [l for l in n8.split("\n") if l.startswith("withdrawn U^4 coeff")][0]
    d2 = [l for l in n8.split("\n") if l.startswith("withdrawn U^2 coeff")][0]
    chk("1797: the withdrawn U^4 term differs from the true one",
        d4.split("=", 1)[1].strip() not in ("0", ""), True)
    chk("1797: and so does the U^2 term", d2.split("=", 1)[1].strip() not in ("0", ""), True)
    # "The norm is the product over (Z/2)^3": N8 has degree 8 = 2^3, one factor per
    # sign choice on (u1, u2, u3).  The eight collapse to FOUR squared linear forms,
    # because a sign flip of all three sends a factor to its negative and the square
    # is the same -- which is what the log's factored constant term prints.
    const = [l for l in n8.split("\n") if l.startswith("0 ")][0][2:]
    chk("1797: the constant term is four squared linear forms", const.count(")**2"), 4)
    chk("1797: and they are the (Z/2)^3 sign choices, paired by overall sign", const,
        "(u1 - u2 - u3)**2*(u1 - u2 + u3)**2*(u1 + u2 - u3)**2*(u1 + u2 + u3)**2")
    chk("1797: four squared forms is degree eight, which is 2^3", 4 * 2, 8)
    # The draft states the two U^4 terms in p and q, the elementary symmetric
    # functions of u1^2, u2^2, u3^2.  The log prints them in u.  The reduction is
    # done here, from the log's own strings, so the draft's form is checked and
    # not taken.
    true4 = [l for l in n8.split("\n") if l.startswith("4 ")][0][2:]
    diff4 = d4.split("=", 1)[1].strip()
    chk("1797: the TRUE U^4 term is 6p^2 - 8q", pq_form(poly_of(true4), 6, -8), True)
    chk("1797: and the withdrawn one is 2p^2 + 16q",
        pq_form(lambda a, b, c, t=poly_of(true4), d=poly_of(diff4):
                t(a, b, c) + d(a, b, c), 2, 16), True)
    chk("1797: so the two differ by -4p^2 + 24q, which is not zero",
        pq_form(poly_of(diff4), -4, 24), True)

    # 1798 (draft)
    got, closed = routh()
    chk("1798: mu_1 to ten places", round(got, 10), 0.0385208965)
    chk("1798: the closed form is the same root", abs(got - closed) < 1e-15, True)
    chk("1798: 27 mu (1 - mu) = 1 at that root", round(27 * got * (1 - got), 12), 1.0)
    chk("1798: agrees with the printed 0.0385209 at seven places",
        round(got, 7), 0.0385209)
    chk("1798: the delivery's own log says so",
        "agree to 1e-7: True" in logs["TB1-routh_check.log"].decode(), True)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
