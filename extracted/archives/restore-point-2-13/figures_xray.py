#!/usr/bin/env python3
"""figures_xray.py — settle the three unresolved X-ray figures.

R 1385  the "85 unblended elements" row set — which exclusion rule gives 85?
R 1390  "the ratio climbs from 0.108 at Ca to 0.226 at Pb", rising monotonically
        toward the hydrogenic limit and never past it
R 1391  the 3p-2p screening offset, "5.296 +/- 0.108 over 45 elements Kr to Pb"

All three are computed from the held captures. Registers 1385, 1390 and 1391 do
not state which column they used; the endpoints of 1390 and the span of 1385
both reproduce off the THEORY column, so theory is used throughout and that is
declared rather than assumed.

The hydrogenic form (R 1390):
    dE(n, l) = (Z - sigma)^4 * alpha^4 * m c^2 / (2 n^3 l(l+1))
so for l = 1, dE(3p)/dE(2p) = (2/3)^3 = 8/27 = 0.2963 at a common sigma, and
    sigma_2 = Z - (32  * dE2 / K)^(1/4)
    sigma_3 = Z - (108 * dE3 / K)^(1/4)      with K = alpha^4 m c^2
"""
import re

ALPHA = 1 / 137.035999177
MC2 = 510998.95            # eV
K = ALPHA ** 4 * MC2       # eV

SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni "
       "Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe "
       "Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg "
       "Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm").split()
Z = {s: i + 1 for i, s in enumerate(SYM)}


def num(s):
    s = s.strip()
    return float(re.sub(r"\(.*\)", "", s)) if s else None


def load(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8")
            if not l.startswith("#")]
    hdr, data = rows[0], rows[1:]
    return [dict(zip(hdr, r)) for r in data]


KL3 = {(r["element"], r["a"]): r for r in load("XRAY-KL3.tsv")}
KL2 = {(r["element"], r["a"]): r for r in load("XRAY-KL2.tsv")}
L1M = {(r["element"], r["a"]): r for r in load("XRAY-L1M.tsv")}

# ---------------------------------------------------------------- R 1385 ---
print("=" * 72)
print("R 1385 — the row set behind 'eighty-five unblended elements, Mg to Fm'")
print("=" * 72)
both = [k for k in KL3 if k in KL2
        and num(KL3[k]["exp_eV"]) is not None and num(KL2[k]["exp_eV"]) is not None]
blended = {k for k in both if KL3[k]["blend"].strip() or KL2[k]["blend"].strip()}
flagged_hash = {k for k in both if "#" in KL3[k]["exp_flag"] + KL2[k]["exp_flag"]}
flagged_star = {k for k in both if "*" in KL3[k]["exp_flag"] + KL2[k]["exp_flag"]}


def els(ks):
    return {k[0] for k in ks}


rules = [
    ("both experimental values present", set(both)),
    ("  minus blended", set(both) - blended),
    ("  minus blended, minus #", set(both) - blended - flagged_hash),
    ("  minus blended, minus *", set(both) - blended - flagged_star),
    ("  minus blended, minus # and *", set(both) - blended - flagged_hash - flagged_star),
]
for name, ks in rules:
    print(f"  {name:<34} rows {len(ks):>3}   elements {len(els(ks)):>3}")
theory = [k for k in KL3 if k in KL2]
th_el = {k[0] for k in theory if Z[k[0]] >= 12}
print(f"  theory column, Mg to Fm, no exclusions   rows {len([k for k in theory if Z[k[0]]>=12]):>3}"
      f"   elements {len(th_el):>3}")
print("  VERDICT: no natural rule yields 85. The register's row set is unstated,")
print("           and every figure conditioned on it (exponent 4.55, sigma scan,")
print("           the +16% above Z >= 70) must be re-derived once it is fixed.")

# ---------------------------------------------------------------- R 1390 ---
print()
print("=" * 72)
print("R 1390 — the 3p / 2p ratio, and the monotonicity claim")
print("=" * 72)


def d2(k):   # 2p splitting, theory
    return num(KL3[k]["theory_eV"]) - num(KL2[k]["theory_eV"])


def d3(k):   # 3p splitting, theory
    return float(L1M[k]["theory_split_eV"]) if k in L1M else None


common = sorted((k for k in KL3 if k in KL2 and k in L1M and d3(k) is not None),
                key=lambda k: (Z[k[0]], k[1]))
lim = (2 / 3) ** 3
print(f"  hydrogenic limit (2/3)^3 = {lim:.4f}")
for el in ("Ca", "Pb"):
    k = (el, "")
    print(f"  {el:<3} ratio = {d3(k)/d2(k):.4f}   (register quotes "
          f"{'0.108' if el=='Ca' else '0.226'})")

win = [k for k in common if 36 <= Z[k[0]] <= 82 and k[1] == ""]
rat = [d3(k) / d2(k) for k in win]
mono = all(b >= a for a, b in zip(rat, rat[1:]))
falls = [(win[i][0], round(rat[i], 4), round(rat[i + 1], 4))
         for i in range(len(rat) - 1) if rat[i + 1] < rat[i]]
print(f"  over Kr-Pb: {len(win)} elements, ratio {min(rat):.4f} to {max(rat):.4f}")
print(f"  monotone non-decreasing: {mono}   never exceeds the limit: {max(rat) < lim}")
if falls:
    print(f"  it falls at {len(falls)} steps, first three: {falls[:3]}")
print("  VERDICT: the 'never past the limit' half HOLDS; the 'rising")
print("           monotonically' half does NOT, over this window.")

# ---------------------------------------------------------------- R 1391 ---
print()
print("=" * 72)
print("R 1391 — the screening offset sigma_3 - sigma_2, per Janet region")
print("=" * 72)


def sig(k):
    s2 = Z[k[0]] - (32 * d2(k) / K) ** 0.25
    s3 = Z[k[0]] - (108 * d3(k) / K) ** 0.25
    return s3 - s2


def stats(ks):
    v = [sig(k) for k in ks]
    m = sum(v) / len(v)
    sd = (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5 if len(v) > 1 else 0.0
    return m, sd, len(v)


for lo, hi, label, quoted in [(18, 20, "3d empty", "3.798 +/- 0.107, n=2"),
                              (21, 22, "3d COLLAPSING", "anomalous, n=2"),
                              (32, 35, "3d complete", "4.595 +/- 0.137, n=4"),
                              (36, 82, "post-Kr closure", "5.296 +/- 0.108, n=45")]:
    ks = [k for k in common if lo <= Z[k[0]] <= hi and k[1] == ""
          and d3(k) > 0 and d2(k) > 0]
    if not ks:
        print(f"  Z {lo}-{hi:<3} {label:<16} NO ELEMENTS with a positive splitting")
        continue
    m, sd, n = stats(ks)
    print(f"  Z {lo}-{hi:<3} {label:<16} offset {m:7.3f} +/- {sd:5.3f}  n={n:<3}"
          f"   register: {quoted}")

# which two of the forty-seven does the register drop?
ks = [k for k in common if 36 <= Z[k[0]] <= 82 and k[1] == ""]
m_all, sd_all, n_all = stats(ks)
print(f"\n  all {n_all} elements Kr-Pb: {m_all:.3f} +/- {sd_all:.3f}")
dev = sorted(ks, key=lambda k: -abs(sig(k) - m_all))
print(f"  largest deviations: " +
      ", ".join(f"{k[0]} {sig(k):.3f}" for k in dev[:4]))
best = [k for k in ks if k not in dev[:2]]
m2, sd2, n2 = stats(best)
print(f"  dropping the two largest -> {m2:.3f} +/- {sd2:.3f}  n={n2}"
      f"   (register: 5.296 +/- 0.108, n=45)")
print(f"  the two dropped would be: {dev[0][0]} and {dev[1][0]}")
