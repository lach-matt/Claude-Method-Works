#!/usr/bin/env python3
"""palindromic.py — §11.7 and §11.8's biconditional, and the six in Chapters 8-11. Phase 1, item
I-021 (mathematical overstatements: iff / equivalence / exactly claims that hold one way).

THE CENSUS. Chapters 8 to 11 carry six biconditional claims. Five are definitions, metric axioms or
characterisations the volume proves. ONE is false in one direction, and it is stated twice:

  §11.7 (Figure 11.2's caption) and §11.8, in the same words:
  "A RANK POLYNOMIAL IS PALINDROMIC IF AND ONLY IF THE POSET IS SELF-DUAL."

Self-dual implies palindromic: TRUE, and it is immediate -- an anti-automorphism sends rank r to
rank M - r, so the level sizes read the same both ways. Palindromic implies self-dual: FALSE.

A COUNTEREXAMPLE, found by exhaustive search over strictly graded posets and printed in full so the
claim can be checked by hand. Six elements; minimal {0, 4, 5}, maximal {1, 2, 3}; the relations are
0 < 1, 0 < 2, 0 < 3, 4 < 1, 5 < 2. Every maximal chain has length one, so it is graded in the strict
sense. Rank sizes are (3, 3) -- PALINDROMIC. It is NOT self-dual: element 0 has three elements above
it and no element of the poset has three below it, so no anti-automorphism exists.

AND THE BOOK'S ARGUMENT IS SOUND, WHICH IS WHY THIS IS A WORDING DEFECT AND NOT A RESULT DEFECT.
§11.8 uses the claim in one direction only: the rank sequence is asymmetric -- 1, 5, 15, 34, 59, 87
forwards against 1, 4, 10, 21, 37, 57 backwards -- therefore the poset is not self-dual, which is the
CONTRAPOSITIVE of the direction that holds. The conclusion stands. What does not stand is "if and
only if", and with it §11.8's "they are the SAME statement": an asymmetric rank sequence IMPLIES
non-self-duality and is not equivalent to it.

stdlib only.  --selftest verifies the counterexample from first principles and the census.
"""
import argparse, itertools, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")
CLAIM = "A rank polynomial is palindromic if and only if the poset is self-dual"
FORWARDS = [1, 5, 15, 34, 59, 87]
BACKWARDS = [1, 4, 10, 21, 37, 57]
N = 6
RELS = [(0, 1), (0, 2), (0, 3), (4, 1), (5, 2)]


def closure(n, rel):
    R = [[False] * n for _ in range(n)]
    for a, b in rel:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][k] and R[k][j]:
                    R[i][j] = True
    return R


def ranks(n, R):
    rk = [0] * n
    for _ in range(n):
        for i in range(n):
            rk[i] = max([rk[k] + 1 for k in range(n) if R[k][i]] or [0])
    return rk


def strictly_graded(n, R, rk):
    top = max(rk)
    for i in range(n):
        below = [k for k in range(n) if R[k][i]]
        above = [k for k in range(n) if R[i][k]]
        if not below and rk[i] != 0:
            return False
        if not above and rk[i] != top:
            return False
    for i in range(n):
        for j in range(n):
            if R[i][j] and not any(R[i][k] and R[k][j] for k in range(n)):
                if rk[j] - rk[i] != 1:
                    return False
    return True


def self_dual(n, R):
    return any(all(R[i][j] == R[p[j]][p[i]] for i in range(n) for j in range(n))
               for p in itertools.permutations(range(n)))


def census():
    L = open(MAIN, encoding="utf-8").read().split("\n")
    hd = [(i, re.match(r"^#{2,6}\s+(\S+)", l).group(1))
          for i, l in enumerate(L) if re.match(r"^#{2,6}\s+\S+", l)]
    def sec(line):
        cur = "?"
        for i, n in hd:
            if i < line: cur = n
            else: break
        return cur
    pat = re.compile(r"\biff\b|if and only if|exactly when|equivalent to|precisely when", re.I)
    return [(sec(i - 1), i, re.sub(r"\s+", " ", l).strip())
            for i, l in enumerate(L, 1)
            if re.match(r"^(8|9|10|11)(\.|$)", sec(i - 1)) and pat.search(l)]


def report():
    R = closure(N, RELS); rk = ranks(N, R)
    sizes = [rk.count(r) for r in range(max(rk) + 1)]
    print("§11.7 and §11.8's biconditional, and the six in Chapters 8–11\n")
    print(f"  the claim, stated twice: \"{CLAIM}\"\n")
    print("  self-dual ⟹ palindromic:  TRUE — an anti-automorphism sends rank r to rank M − r.")
    print("  palindromic ⟹ self-dual:  FALSE, and here is a six-element counterexample:\n")
    print(f"    elements 0–5; relations {', '.join(f'{a} < {b}' for a, b in RELS)}")
    print(f"    ranks {rk}, level sizes {sizes} — palindromic")
    print(f"    strictly graded: {strictly_graded(N, R, rk)}   self-dual: {self_dual(N, R)}")
    print("    element 0 has three above it and nothing in the poset has three below it,")
    print("    so no anti-automorphism exists.\n")
    print("  AND THE BOOK'S ARGUMENT IS SOUND. §11.8 uses it one way only:")
    print(f"    forwards  {FORWARDS}")
    print(f"    backwards {BACKWARDS}   — asymmetric, therefore not self-dual,")
    print("    which is the CONTRAPOSITIVE of the direction that holds.")
    print("\n  What does not stand is 'if and only if', and with it §11.8's 'they are the SAME")
    print("  statement': an asymmetric rank sequence IMPLIES non-self-duality, and is not")
    print("  equivalent to it. A wording defect, not a result defect.\n")
    c = census()
    print(f"  the biconditional census of Chapters 8–11: {len(c)} claims, of which this is the one")
    for s, i, t in c:
        mark = "  <-- FALSE ONE WAY" if CLAIM.lower() in t.lower() else ""
        print(f"    §{s:<9} L{i:<6} {t[:110]}{mark}")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    R = closure(N, RELS); rk = ranks(N, R)
    sizes = [rk.count(r) for r in range(max(rk) + 1)]
    eq("the counterexample is a poset", all(not R[i][i] for i in range(N)), True)
    eq("strictly graded", strictly_graded(N, R, rk), True)
    eq("its level sizes", sizes, [3, 3])
    eq("which are palindromic", sizes == sizes[::-1], True)
    eq("and it is NOT self-dual", self_dual(N, R), False)
    eq("so palindromic does not imply self-dual", sizes == sizes[::-1] and not self_dual(N, R), True)
    t = open(MAIN, encoding="utf-8").read()
    eq("the claim is stated twice in the volume", t.count(CLAIM), 2)
    eq("§11.8's forwards sequence is asymmetric", FORWARDS == BACKWARDS, False)
    eq("so the book's own inference uses the direction that holds",
       FORWARDS != BACKWARDS, True)
    c = census()
    eq("biconditionals in Chapters 8–11", len(c), 6)
    eq("and this claim is two of the six",
       sum(1 for _, _, x in c if CLAIM.lower() in x.lower()), 2)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
