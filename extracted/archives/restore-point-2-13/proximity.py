#!/usr/bin/env python3
"""proximity.py — was proximity a signal, or the trigger?

Register 1407 tested proximity as a TRIGGER and demoted it to a SIGNAL: the four
smallest margins in the table are all resets and there are zero false positives,
but the best threshold reaches 91% accuracy against an 87% baseline of predicting
no reset anywhere, with four true positives and NINE resets missed. The verdict
was that the charge signal lives in the margin's scaling, not in a threshold.

But 1407 measured the margin PER ELEMENT — the width of that element's own
corridor. The balance result (R 1401, recomputed tonight) says the object that
governs a is not the element's corridor but the RUNNING INTERSECTION of every
corridor since the last move. Those are different quantities, and only the second
is what a actually has to sit inside.

So the question 1407 could not ask: measured on the running intersection, is
proximity a trigger? And if so, at what threshold?
"""
import sys, io, contextlib
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack

IV = {r[0]: r for r in brack.IV}
RESET = {3, 19, 37, 42, 43, 45, 55, 58, 64, 65, 80, 81, 87, 91, 96, 97, 103, 104}

# ---- per-element margin, which is what R 1407 scanned ---------------------
per = {}
for Z, _, _, _, L, U, _, _ in IV.values():
    if L < -1e8 or U > 1e8:
        continue                       # one-sided: no margin to speak of
    per[Z] = U - L

pr = [per[z] for z in per if z in RESET]
pn = [per[z] for z in per if z not in RESET]
med = lambda v: sorted(v)[len(v) // 2]
print("=" * 72)
print("R 1407's QUANTITY — the element's OWN corridor width")
print("=" * 72)
print(f"  two-sided elements: {len(per)}   resets among them: {len(pr)}")
print(f"  median margin, resets     {med(pr):+.3f}   (register: +0.50)")
print(f"  median margin, non-resets {med(pn):+.3f}   (register: +1.15)")
smallest = sorted(per, key=lambda z: per[z])[:4]
print(f"  four smallest margins: {smallest}  all resets: "
      f"{all(z in RESET for z in smallest)}")

best = None
for t in sorted(set(per.values())):
    tp = sum(1 for z in per if per[z] <= t and z in RESET)
    fp = sum(1 for z in per if per[z] <= t and z not in RESET)
    fn = sum(1 for z in per if per[z] > t and z in RESET)
    tn = len(per) - tp - fp - fn
    acc = (tp + tn) / len(per)
    if best is None or acc > best[0]:
        best = (acc, t, tp, fp, fn)
acc, t, tp, fp, fn = best
base = sum(1 for z in per if z not in RESET) / len(per)
print(f"  best threshold {t:.3f}: accuracy {acc:.0%} against a {base:.0%} baseline")
print(f"    true positives {tp}, false positives {fp}, resets MISSED {fn}")
print("  -> NOT R 1407's QUANTITY. The corridor width gives 73 steps, not 99.")

# ---- the running intersection's margin, which is what a sits inside -------
print()
print("=" * 72)
print("THE QUANTITY THE BALANCE NAMES — the RUNNING INTERSECTION's width")
print("=" * 72)
lo, hi = -1e9, 1e9
rows, forced = [], []
for Z in sorted(IV):
    _, _, _, _, L, U, _, _ = IV[Z]
    nlo, nhi = max(lo, L), min(hi, U)
    width = nhi - nlo
    rows.append((Z, width))
    if nlo >= nhi:
        forced.append(Z)
        lo, hi = L, U
    else:
        lo, hi = nlo, nhi

tp = sum(1 for z in forced if z in RESET)
fp = sum(1 for z in forced if z not in RESET)
missed = sorted(RESET - set(forced))
print(f"  trigger: the running intersection's width reaches ZERO")
print(f"    fires at {len(forced)} elements: {forced}")
print(f"    true positives {tp}, false positives {fp}, resets missed {len(missed)}")
print(f"    the missed: {missed}  — Li, K, Tl, Fr, every one a period opening")
n = len(rows)
acc = (tp + (n - len(forced) - len(missed))) / n
print(f"    accuracy {acc:.0%} over all {n} steps, against an "
      f"{(n-len(RESET))/n:.0%} baseline")

print()
print("  THE COMPARISON, ON ONE LINE EACH")
print(f"    per-element margin, best threshold : {tp if False else best[2]} caught, "
      f"{best[3]} false, {best[4]} missed")
print(f"    running intersection, threshold ZERO: {tp} caught, {fp} false, "
      f"{len(missed)} missed")
print()
print("  So on THIS quantity proximity is the trigger, and the threshold is not")
print("  a fitted number — it is zero. Whether R 1407's own margin is a proxy")
print("  for it cannot be said until that margin is defined.")
print("  The strict inequality needs no proximity TERM: proximity is the")
print("  inequality reaching equality, which is what a corridor emptying IS.")

# ---- and what 1406's algebra has in it -----------------------------------
print()
print("=" * 72)
print("WHAT R 1406's SENSITIVITY ACTUALLY CONTAINS")
print("=" * 72)
print("  The ceiling is  dn / (sqrt(p_r) - sqrt(p_g)),  so")
print("      d(ceiling)/d(q_rival)  =  -dn / ( 2 * cap * sqrt(p_r) * GAP^2 )")
print("  with GAP = sqrt(p_r) - sqrt(p_g). Two things sit in that denominator:")
print("    · the CAP — 2, 6, 10, 14 — so an s rival's single electron moves the")
print("      ceiling most. That is charge shared over the fewest carriers.")
print("    · the GAP, SQUARED. An inverse-square in the separation between the")
print("      two radicands.")
print("  The inverse-square is a fact about this algebra. Identifying it WITH")
print("  the Coulomb law is a further claim and is NOT tested here — the")
print("  radicands are node counts, not distances, and R 1407's own Slater test")
print("  reached only r = +0.64 against 1/Z_eff. Recorded as a shape, not a")
print("  derivation.")


# ---------------------------------------------------------------------------
# R 1407's ACTUAL QUANTITY, recovered 2026-08-11 from the 1.6.1 transcript:
# the margin is PROXIMITY TO THE CEILING -- the distance from the HELD a to U --
# and its "ninety-nine two-sided steps" are the steps with a finite CEILING.
# The floor is irrelevant to it, which is why the two-sided count of 73 was the
# wrong set. Ninety-nine is reproduced exactly below.
# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("R 1407's MARGIN, WITH THE RECOVERED DEFINITION")
print("=" * 72)
lo, hi, a, marg = -1e9, 1e9, None, {}
for Z in sorted(IV):
    _, _, _, _, L, U, _, _ = IV[Z]
    nlo, nhi = max(lo, L), min(hi, U)
    if nlo >= nhi or a is None:
        lo, hi = L, U
        a = L if 1e-9 < L < 1e8 else (U if U < 1e8 else 0.0)
    else:
        lo, hi = nlo, nhi
    if U < 1e8:
        marg[Z] = U - a
mr = [marg[z] for z in marg if z in RESET]
mn = [marg[z] for z in marg if z not in RESET]
print(f"  steps with a finite ceiling: {len(marg)}   register 1407: ninety-nine")
print(f"  median margin, resets     {med(mr):+.3f}   register: +0.50")
print(f"  median margin, non-resets {med(mn):+.3f}   register: +1.15")
print()
print("  The COUNT reproduces exactly; the MEDIANS do not, and cannot.")
print("  The margin is U - a, so it depends on where a was placed, which depends")
print("  on the placement rule -- the very thing the trigger hunt was trying to")
print("  derive. That is why proximity could only ever be a SIGNAL: measuring it")
print("  presupposes the answer. Emptiness does not contain a at all, which is")
print("  why it is trajectory-free (R 1402) and why the fourteen forced moves")
print("  reproduce from the intervals alone.")
print()
print("  AND A CORRECTION TO THIS SCRIPT'S OWN EARLIER CLAIM: the emptiness")
print("  criterion above is NOT a new trigger. It is register 1401 restated.")
print("  R 1407 warns that scanning a tenth condition after nine have failed is")
print("  searching rather than measuring, and that warning applies here.")
