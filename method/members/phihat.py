#!/usr/bin/env python3
"""tools/phihat.py -- phi-hat at arbitrary caps, and which form of it is right.

r2lib.py L391-392 records what is missing:

    "Its companion phi_at is NOT lifted: it depends on TERMS, which is still
     owed."

This supplies both. TERMS is section 12.11.1's microstate enumeration, run
rather than described; phi_at is phi-hat at any caps, computed rather than
hardcoded at the three values tower-2.py carries.

THE TOOL TAKES NO POSITION ON WHICH FORM IS RIGHT. Section 12.11.1 gives
phi-hat's genus and one value set -- "the monotone envelope of k -> max 2J over
the parent shells admitted by the caps, so phi-hat = {1: 3, 2: 4, 3: 5} at
7.4's" -- and never says over what the envelope is taken. Members print it two
ways. So the candidate forms are DATA, exactly as cypher.py's language rosters
are data, and the tool MEASURES each against the numbers the corpus records
rather than asserting one. The comparison decides.

    python3 tools/phihat.py --candidates          # the forms, as data
    python3 tools/phihat.py --compare             # every form against the record
    python3 tools/phihat.py --phi --caps 3,3,1,3,1
    python3 tools/phihat.py --tower --caps 4,4,2,6,2 --form running-max
    python3 tools/phihat.py --max2j --l 3
    python3 tools/phihat.py --selftest

Stdlib only, Python 3.9+.

WITNESS STATUS, AND IT IS CARRIED. Every count this tool prints is
THEORETICAL: proven by construction on the lattice, never verified by
spectroscopic measurement. M's ruling: such a figure is publishable as
theoretically proven but not yet witnessed, and the label travels with it. A
tower count is not a measurement and this tool never prints one as though it
were.

Three things it refuses to do:

  1. It never asserts a form. --compare reports what each candidate reproduces
     and what it fails; if several are indistinguishable on the record it says
     so, because that is the finding.

  2. It never prints a count without its witness status. THEORETICAL is not a
     hedge, it is the class the figure belongs to.

  3. It never edits a seated member. phi_at is owed to r2lib; lifting it there
     is a close action under close.py --append, not this tool's to take.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import os
import sys

def _repo_root(start=None):
    """The repository root, found by walking up for method/verify.py.

    An instrument travels as a bundle member (chat 68's standing half), so the
    same file runs from tools/ and from method/members/ and must locate the
    store from either. Walking up for a landmark does that; a fixed number of
    dirname() calls does not."""
    d = os.path.dirname(os.path.abspath(start or __file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "method", "verify.py")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return os.path.dirname(os.path.dirname(os.path.abspath(start or __file__)))


REPO = _repo_root()

THEORETICAL = "THEORETICAL"      # proven by construction, never witnessed
CAPS_74 = (3, 3, 1, 3, 1)        # section 7.4's standing caps (n, e, l, k, f)

_TERMS = {}


def terms(l, k):
    """The multiset of LS terms (2S, L) of l^k, by microstate enumeration.

    Section 12.11.1, executed: "list every way of placing k electrons in the
    2(2l+1) spin-orbitals, accumulate (2M_L, 2M_S), and strip complete (2S, 2L)
    blocks from the largest M_L down until the list is empty."

    This is TERMS, which r2lib records as owed."""
    key = (l, k)
    if key in _TERMS:
        return _TERMS[key]
    if k < 0 or k > 2 * (2 * l + 1):
        _TERMS[key] = []
        return []
    orb = [(ml, ms2) for ml in range(l, -l - 1, -1) for ms2 in (1, -1)]
    cnt = collections.Counter()
    for c in itertools.combinations(orb, k):
        cnt[(sum(o[0] for o in c), sum(o[1] for o in c))] += 1
    out = []
    while cnt:
        ML = max(m for (m, _s) in cnt)
        MS2 = max(s for (m, s) in cnt if m == ML)
        out.append((MS2, ML))
        for ml in range(-ML, ML + 1):
            for ms2 in range(-MS2, MS2 + 1, 2):
                cnt[(ml, ms2)] -= 1
                if cnt[(ml, ms2)] <= 0:
                    del cnt[(ml, ms2)]
    out.sort()
    _TERMS[key] = out
    return out


def max2J(l, k):
    """max 2J over the terms of l^k. Main L3368: "max2J(l,k), unimodal with its
    peak at half filling, 25 at f7, zero at closure, for the core's J." The
    corpus names this separately from phi-hat, and that separation is the whole
    question this tool exists to settle."""
    return max((2 * L + s2 for s2, L in terms(l, k)), default=0)


def shells(caps):
    """The parent shells admitted by the caps: l from 0 to l_max."""
    return range(0, caps[2] + 1)


def half_filling(l):
    return 2 * l + 1


# ---------------------------------------------------------------------------
# The candidate forms. DATA, not a decision.
# ---------------------------------------------------------------------------

def _pointwise(k, caps):
    return max((max2J(l, k) for l in shells(caps) if k <= 2 * (2 * l + 1)),
               default=0)


def _running_max(k, caps):
    return max((_pointwise(j, caps) for j in range(1, k + 1)), default=0)


def _fold(k, caps):
    best = 0
    for l in shells(caps):
        cap = 2 * (2 * l + 1)
        if k > cap:
            continue
        best = max(best, max2J(l, k), max2J(l, cap - k))
    return best


def _clamp_half(k, caps):
    best = 0
    for l in shells(caps):
        if k > 2 * (2 * l + 1):
            continue
        best = max(best, max2J(l, min(k, half_filling(l))))
    return best


def _global_max(k, caps):
    return max((_pointwise(j, caps) for j in range(1, caps[3] + 1)), default=0)


CANDIDATES = {
    "pointwise": (_pointwise,
                  "max 2J over terms of l^k at occupancy exactly k. The form "
                  "printed at MC L1686 and Transitions A15 L1819, both without "
                  "an envelope operation."),
    "running-max": (_running_max,
                    "max over k' <= k of the pointwise value: the monotone "
                    "majorant. Section 12.11.2, main L3383: 'Each admissible "
                    "extension is the monotone envelope of its physics.'"),
    "fold": (_fold,
             "max over the particle-hole conjugate pair, k and 4l+2-k. Uses "
             "section 8.4's conjugation directly."),
    "clamp-half": (_clamp_half,
                   "the pointwise value at min(k, half filling) per shell. "
                   "Saturates at the unimodal peak rather than majorising."),
    "global-max": (_global_max,
                   "constant at the largest pointwise value under the caps. "
                   "The crudest monotone envelope there is."),
}


def phi_at(caps, form="running-max"):
    """phi-hat at arbitrary caps -- the function r2lib records as owed.

    Returns {k: phi-hat(k)} for k = 1 .. k_max. tower-2.py hardcodes
    {1:3, 2:4, 3:5}; this computes it, at any caps, under any candidate form."""
    fn = CANDIDATES[form][0]
    return {k: fn(k, caps) for k in range(1, caps[3] + 1)}


# ---------------------------------------------------------------------------
# The tower, counted rather than enumerated
# ---------------------------------------------------------------------------

def tower_counts(caps, form="running-max"):
    """|Lambda_8| .. |Lambda_13| at the given caps under the given form.

    Counted combinatorially: Lambda_13 at (5,5,2,6,2) holds 77 million cells
    and enumerating them to count them is a waste of a machine."""
    nmax, emax, lmax, kmax, fmax = caps
    phi = phi_at(caps, form)
    c8 = c9 = c10 = c11 = c12 = c13 = 0
    for n in range(1, nmax + 1):
        for l in range(0, min(lmax, n - 1) + 1):
            for k in range(1, min(kmax, 4 * l + 2) + 1):
                ph = phi[k]
                # 2J_c in [0, ph]; 2K in [0, 2J_c + 2 f_max]; 2J in [|2K-1|, 2K+1]
                n_jc = ph + 1
                n_jc_k = sum(jc + 2 * fmax + 1 for jc in range(0, ph + 1))
                n_jc_k_j = sum(len(range(max(0, K2 - 1), K2 + 2))
                               for jc in range(0, ph + 1)
                               for K2 in range(0, jc + 2 * fmax + 1))
                for q in range(0, k + 1):
                    for e in range(1, emax + 1):
                        for f in range(0, min(fmax, e - 1) + 1):
                            for g in range(0, min(4 * f + 2, q) + 1):
                                n_s = k + 1                    # 2S in [0, k]
                                n_sp = g + 1                   # 2S' in [0, g]
                                # v in [2S', g] summed over 2S'
                                n_v = sum(g - sp + 1 for sp in range(0, g + 1))
                                c8 += n_s
                                c9 += n_s * n_sp
                                c10 += n_s * n_v
                                c11 += n_s * n_v * n_jc
                                c12 += n_s * n_v * n_jc_k
                                c13 += n_s * n_v * n_jc_k_j
    return {8: c8, 9: c9, 10: c10, 11: c11, 12: c12, 13: c13}


def pauli_consistent(caps):
    """Can the largest admitted shell actually hold k_max electrons?

    Section 7.1's k <= 2(2l+1) is Pauli exclusion. A cap setting with
    k_max > 2(2 l_max + 1) asks for an occupancy no admitted shell can carry,
    and the seven constraints already forbid it. It matters here because two
    candidate forms of phi-hat differ ONLY on such settings."""
    return caps[3] <= 2 * (2 * caps[2] + 1)


def divergence(form_a, form_b, sweep=None):
    """Where two candidate forms part, and whether they part anywhere the
    caps are Pauli-consistent."""
    sweep = sweep or [(n, e, l, k, f)
                      for n in (3, 4, 5) for e in (3, 4, 5)
                      for l in (0, 1, 2, 3) for k in range(1, 15)
                      for f in (0, 1, 2)]
    all_diff, phys_diff, phys = [], [], 0
    for caps in sweep:
        same = phi_at(caps, form_a) == phi_at(caps, form_b)
        if not same:
            all_diff.append(caps)
        if pauli_consistent(caps):
            phys += 1
            if not same:
                phys_diff.append(caps)
    return {"swept": len(sweep), "differ": len(all_diff),
            "pauli_consistent": phys, "differ_when_pauli_consistent":
            len(phys_diff), "examples": all_diff[:5]}


def monotone(phi):
    ks = sorted(phi)
    return all(phi[a] <= phi[b] for a, b in zip(ks, ks[1:]))


# ---------------------------------------------------------------------------
# The record. Every fixture is a number the corpus states about itself.
# ---------------------------------------------------------------------------

FOUR_CAPS = [(3, 3, 1, 3, 1), (4, 4, 2, 4, 1),
             (4, 4, 2, 6, 2), (5, 5, 2, 6, 2)]

RECORD = {
    # main L3072, MC L1686, tower-2.py's PHI
    "phi at 7.4's caps = {1:3, 2:4, 3:5}":
        lambda f: phi_at(CAPS_74, f) == {1: 3, 2: 4, 3: 5},
    # section 12.11.0.10's table, every stage
    "|L8..L13| at 7.4's caps = 976/1654/2535/13585/70905/199130":
        lambda f: tower_counts(CAPS_74, f) == {8: 976, 9: 1654, 10: 2535,
                                               11: 13585, 12: 70905,
                                               13: 199130},
    # main L3124-3125, the four-cap sweep
    "|L13| at the four caps = 199130/4731790/40310170/77083771":
        lambda f: [tower_counts(c, f)[13] for c in FOUR_CAPS] ==
                  [199130, 4731790, 40310170, 77083771],
    # main L3122: "phi-hat stays monotone" across those same four
    "phi-hat monotone at all four caps":
        lambda f: all(monotone(phi_at(c, f)) for c in FOUR_CAPS),
    # r2lib L390-391: L8_at's own documented returns
    "|L8| = 976 / 1636 / 2394 at (3,3,1,3,1) / (3,3,1,4,1) / (4,3,1,4,1)":
        lambda f: [tower_counts(c, f)[8] for c in
                   ((3, 3, 1, 3, 1), (3, 3, 1, 4, 1), (4, 3, 1, 4, 1))] ==
                  [976, 1636, 2394],
}


def compare(forms=None):
    forms = forms or list(CANDIDATES)
    rows = {}
    for f in forms:
        rows[f] = {}
        for name, test in RECORD.items():
            try:
                rows[f][name] = bool(test(f))
            except Exception as exc:                       # noqa: BLE001
                rows[f][name] = "ERROR: %s" % exc
    return rows


def report_compare(rows):
    names = list(RECORD)
    print("Every candidate form of phi-hat, against the numbers the corpus")
    print("records about itself. The tool asserts nothing; the record decides.")
    print()
    width = max(len(f) for f in rows)
    for i, name in enumerate(names, 1):
        print("  [%d] %s" % (i, name))
    print()
    print("  %-*s  %s" % (width, "form", "  ".join("[%d]" % i
                                                   for i in range(1, len(names) + 1))))
    for f, res in rows.items():
        marks = []
        for name in names:
            v = res[name]
            marks.append(" ok" if v is True else ("  x" if v is False else "err"))
        print("  %-*s  %s" % (width, f, "  ".join(marks)))
    print()
    survivors = [f for f, res in rows.items()
                 if all(res[n] is True for n in names)]
    refuted = [f for f in rows if f not in survivors]
    if refuted:
        print("  REFUTED by the record: %s" % ", ".join(refuted))
    if not survivors:
        print("  NO candidate reproduces the whole record.")
    elif len(survivors) == 1:
        print("  ONE candidate reproduces the whole record: %s" % survivors[0])
        print("  %s" % CANDIDATES[survivors[0]][1])
    else:
        print("  %d candidates reproduce the whole record: %s"
              % (len(survivors), ", ".join(survivors)))
        print()
        # Survivors may be one function under two spellings. Measure it rather
        # than leaving "indistinguishable on the record" as the last word.
        for a, b in itertools.combinations(survivors, 2):
            d = divergence(a, b)
            if d["differ"] == 0:
                print("  %s and %s agree at every one of the %d cap settings"
                      % (a, b, d["swept"]))
                print("  swept: they are one function under two spellings.")
            elif d["differ_when_pauli_consistent"] == 0:
                print("  %s and %s differ at %d of %d cap settings swept, and"
                      % (a, b, d["differ"], d["swept"]))
                print("  at NONE of the %d that are Pauli-consistent. They part"
                      % d["pauli_consistent"])
                print("  only where k_max exceeds the largest admitted shell's")
                print("  capacity -- which section 7.1's k <= 2(2l+1) forbids.")
                print("  On the admissible domain the record IS decisive.")
            else:
                print("  %s and %s differ at %d Pauli-consistent cap settings,"
                      % (a, b, d["differ_when_pauli_consistent"]))
                print("  e.g. %s. The record does not decide between them, and"
                      % (d["examples"][0],))
                print("  that is a question for a ruling, not for this tool.")
    print()
    print("  Every count above is %s: proven by construction on the lattice,"
          % THEORETICAL)
    print("  never verified by spectroscopic measurement.")
    return survivors


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def selftest():
    fails, checked = [], 0

    def check(cond, msg):
        nonlocal checked
        checked += 1
        if not cond:
            fails.append(msg)

    # TERMS against textbook values, which is what makes the rest trustworthy.
    for l, k, want in ((1, 2, {(0, 0), (0, 2), (2, 1)}),
                       (1, 3, {(1, 1), (1, 2), (3, 0)}),
                       (2, 2, {(0, 0), (0, 2), (0, 4), (2, 1), (2, 3)}),
                       (0, 2, {(0, 0)}), (1, 6, {(0, 0)})):
        check(set(terms(l, k)) == want,
              "terms(%d,%d) = %s, expected %s"
              % (l, k, sorted(set(terms(l, k))), sorted(want)))

    # max2J's four recorded properties -- main L3366-3369, banked at
    # WORKING-REGISTER L4817 against r2-ch12y.out (42a33746).
    check(max2J(3, 7) == 25, "max2J(f^7) = %d, the record says 25" % max2J(3, 7))
    for l in (1, 2, 3):
        cap = 2 * (2 * l + 1)
        row = [max2J(l, k) for k in range(0, cap + 1)]
        check(row.index(max(row)) == half_filling(l),
              "max2J peaks at k=%d on l=%d, half filling is %d"
              % (row.index(max(row)), l, half_filling(l)))
        check(row[-1] == 0, "max2J is not zero at closure on l=%d" % l)
        check(all(max2J(l, k) == max2J(l, cap - k) for k in range(cap + 1)),
              "max2J is not fold-symmetric on l=%d" % l)
        check(not all(a <= b for a, b in zip(row[1:], row[2:])),
              "max2J is monotone on l=%d; the record says unimodal" % l)
    # section 8.4's conjugation, stated as terms not as max2J
    for l in (1, 2):
        cap = 2 * (2 * l + 1)
        check(all(terms(l, k) == terms(l, cap - k) for k in range(cap + 1)),
              "terms(l,k) != terms(l,4l+2-k) on l=%d (section 8.4)" % l)

    # phi_at must reproduce tower-2.py's hardcoded PHI under at least one form.
    got = [f for f in CANDIDATES if phi_at(CAPS_74, f) == {1: 3, 2: 4, 3: 5}]
    check(bool(got), "no candidate reproduces tower-2.py's PHI at 7.4's caps")

    # The comparison must be decisive, and it must be decisive the same way
    # every time. If this fixture ever fails, the record has changed or a
    # candidate has -- either is a finding, not a thing to tune.
    rows = compare()
    survivors = [f for f, r in rows.items() if all(v is True for v in r.values())]
    check(sorted(survivors) == ["clamp-half", "running-max"],
          "the record leaves %s standing; expected clamp-half and running-max"
          % (sorted(survivors) or "nothing"))
    for f in ("pointwise", "fold", "global-max"):
        check(f not in survivors, "%s survives the record; it should not" % f)
    # The printed form must be refuted, and refuted BY the four-cap counts --
    # the only fixture that separates it, since it agrees at 7.4's caps.
    four = "|L13| at the four caps = 199130/4731790/40310170/77083771"
    check(rows["pointwise"][four] is False,
          "the pointwise form is not refuted by the four-cap counts")
    check(rows["pointwise"]["phi at 7.4's caps = {1:3, 2:4, 3:5}"] is True,
          "the pointwise form fails already at 7.4's caps; then the ambiguity "
          "would never have been invisible, and it was")

    # The two survivors are one function on the admissible domain. If this
    # ever fails, the record genuinely does not decide and a ruling is owed.
    d = divergence("running-max", "clamp-half")
    check(d["differ"] > 0,
          "running-max and clamp-half never differ; they are the same "
          "expression and one of them should be dropped")
    check(d["differ_when_pauli_consistent"] == 0,
          "running-max and clamp-half differ at %d Pauli-consistent cap "
          "settings; the record does not decide and a ruling is owed"
          % d["differ_when_pauli_consistent"])
    check(d["pauli_consistent"] > 500,
          "only %d Pauli-consistent settings were swept" % d["pauli_consistent"])

    # the tower at 7.4's caps, against section 12.11.0.10's whole table
    tc = tower_counts(CAPS_74, "running-max")
    for d, want in ((8, 976), (9, 1654), (10, 2535), (11, 13585),
                    (12, 70905), (13, 199130)):
        check(tc[d] == want, "|L%d| = %d at 7.4's caps, the table says %d"
              % (d, tc[d], want))

    print("fixtures checked: %d  failed: %d" % (checked, len(fails)))
    for f in fails:
        print("  FAIL " + f)
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED")
    return 0 if not fails else 1


def parse_caps(s):
    parts = [int(x) for x in s.split(",")]
    if len(parts) != 5:
        raise ValueError("caps are (n_max, e_max, l_max, k_max, f_max)")
    return tuple(parts)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="phi-hat at arbitrary caps, and which form of it is right.")
    ap.add_argument("--caps", default="3,3,1,3,1",
                    help="n_max,e_max,l_max,k_max,f_max (default 7.4's)")
    ap.add_argument("--form", default="running-max", choices=sorted(CANDIDATES))
    ap.add_argument("--candidates", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--phi", action="store_true")
    ap.add_argument("--tower", action="store_true")
    ap.add_argument("--max2j", action="store_true")
    ap.add_argument("--l", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.candidates:
        print("The candidate forms of phi-hat. Data, not a decision.")
        print()
        for name, (_fn, note) in CANDIDATES.items():
            print("  %-13s %s" % (name, note))
        return 0
    if args.compare:
        rows = compare()
        if args.json:
            json.dump(rows, sys.stdout, indent=2)
            print()
            return 0
        report_compare(rows)
        return 0

    caps = parse_caps(args.caps)
    if args.max2j:
        ls = [args.l] if args.l is not None else list(shells(caps))
        for l in ls:
            cap = 2 * (2 * l + 1)
            print("  l=%d  max2J(k=0..%d) = %s   peak k=%d, half filling %d"
                  % (l, cap, [max2J(l, k) for k in range(cap + 1)],
                     [max2J(l, k) for k in range(cap + 1)].index(
                         max(max2J(l, k) for k in range(cap + 1))),
                     half_filling(l)))
        return 0
    if args.phi:
        phi = phi_at(caps, args.form)
        print("  caps %s   form %s" % (caps, args.form))
        print("  phi-hat = %s   monotone: %s" % (phi, monotone(phi)))
        print("  [%s]" % THEORETICAL)
        return 0
    if args.tower:
        tc = tower_counts(caps, args.form)
        print("  caps %s   form %s" % (caps, args.form))
        for d in sorted(tc):
            print("    |Lambda_%-2d| = %-12d [%s]" % (d, tc[d], THEORETICAL))
        return 0
    ap.error("name a mode: --candidates, --compare, --phi, --tower, --max2j "
             "or --selftest")


if __name__ == "__main__":
    sys.exit(main())
