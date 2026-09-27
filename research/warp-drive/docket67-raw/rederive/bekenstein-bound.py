#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'bekenstein-bound'.
Reads research/warp-drive READ-ONLY (sys.dont_write_bytecode, no writes).
Checks:
 A  Schwarzschild D=4 saturates S <= 2 pi R E/(hbar c) exactly (R = r_s, E = Mc^2)   [sympy]
 B  D-dim Schwarzschild: S_BH / bound = 2/(D-2)  (Bousso hep-th/0203101 p.9)        [sympy]
 C  Reissner-Nordstrom (spherical, R unambiguous): S/bound = r+/(2M) < 1 for Q != 0  [sympy]
 D  Kerr: S/bound depends on which 'R' (r+, areal, equatorial circumferential)       [sympy]
 E  the tree's numerics: 1.8038e45 bits, 1.58e45 (R=0.875), ratio 7478, 0.134 mm     [numeric]
 F  hypotheses on the tree's instance: weak gravity, spherical bound weaker            [numeric]
 G  data moves: CODATA 2018 vs 2022 constants, T_CMB 2.7255 vs 2.72548 (Fixsen 2009)  [numeric]
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

ok_all = True
def chk(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- A
G, c, hbar, M, pi = sp.symbols('G c hbar M pi_', positive=True)
R = 2*G*M/c**2
E = M*c**2
bound = 2*sp.pi*R*E/(hbar*c)
A = 4*sp.pi*R**2
S_BH = A*c**3/(4*G*hbar)
chk("A: Schwarzschild D=4: 2 pi r_s Mc^2/(hbar c) == A c^3/(4 G hbar)  [both = 4 pi G M^2/(hbar c)]",
    sp.simplify(bound - S_BH) == 0)
print("     common value:", sp.simplify(S_BH))

# ---------------- B  (geometrised G=hbar=c=1), D dims
D, b = sp.symbols('D b', positive=True)
AD2 = 2*sp.pi**((D-1)/2)/sp.gamma((D-1)/2)
MD = (D-2)*AD2*b**(D-3)/(16*sp.pi)          # Bousso RMP eq. 2.12
SD = AD2*b**(D-2)/4
ratioD = sp.simplify(SD/(2*sp.pi*MD*b))
chk("B: D-dim Schwarzschild S_BH/(2 pi M b) == 2/(D-2)", sp.simplify(ratioD - 2/(D-2)) == 0)
for d in (4, 5, 6, 10, 11):
    print("     D=%d: ratio %s" % (d, ratioD.subs(D, d)))
chk("B: equals 1 only at D=4", sp.solve(sp.Eq(2/(D-2), 1), D) == [4])

# ---------------- C  Reissner-Nordstrom, G=c=hbar=1
Mm, Q, a = sp.symbols('M Q a', nonnegative=True)
rp_RN = Mm + sp.sqrt(Mm**2 - Q**2)
ratio_RN = sp.simplify(sp.pi*rp_RN**2/(2*sp.pi*Mm*rp_RN))
chk("C: RN S/bound == r+/(2M)", sp.simplify(ratio_RN - rp_RN/(2*Mm)) == 0)
vals = [(q, float(ratio_RN.subs({Mm: 1, Q: q}))) for q in (0, 0.5, 0.9, 1.0)]
print("     RN ratio at M=1, Q in (0,.5,.9,1):", ["%.4f" % v for _, v in vals])
chk("C: RN saturates only at Q=0; extremal Q=M gives 1/2",
    abs(vals[0][1]-1) < 1e-15 and all(v < 1 for q, v in vals[1:]) and abs(vals[-1][1]-0.5) < 1e-15)

# ---------------- D  Kerr, G=c=hbar=1 ; S = pi (r+^2 + a^2)
rp_K = Mm + sp.sqrt(Mm**2 - a**2)
S_K = sp.pi*(rp_K**2 + a**2)
convs = {
    "R = r+ (Boyer-Lindquist)": rp_K,
    "R = areal sqrt(A/4pi)": sp.sqrt(rp_K**2 + a**2),
    "R = equatorial circumferential (r+^2+a^2)/r+": (rp_K**2 + a**2)/rp_K,
}
kerr = {}
for k, Rk in convs.items():
    rr = [float((S_K/(2*sp.pi*Mm*Rk)).subs({Mm: 1, a: av})) for av in (0, 0.5, 0.9, 1.0)]
    kerr[k] = rr
    print("     Kerr %-46s ratio at a/M=(0,.5,.9,1): %s" % (k, ["%.4f" % x for x in rr]))
chk("D: Kerr with R = r+ saturates for all a (identity r+^2+a^2 = 2 M r+)",
    all(abs(x-1) < 1e-12 for x in kerr["R = r+ (Boyer-Lindquist)"]))
chk("D: Kerr with areal or circumscribing R saturates only at a = 0",
    all(x < 1-1e-9 for k in list(convs)[1:] for x in kerr[k][1:]))
chk("D: extremal Kerr, circumscribing R: ratio = 1/2; areal R: 1/sqrt(2)",
    abs(kerr[list(convs)[2]][3]-0.5) < 1e-12 and abs(kerr[list(convs)[1]][3]-1/math.sqrt(2)) < 1e-12)

# ---------------- E  the tree's numerics, from the tree's own constants
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import nopath
Gn, Cn, HB, KB = nopath.G, nopath.C, nopath.HBAR, nopath.KB
M_KG = 70.0     # massform.py:5152 pin label "Bekenstein 70 kg"
T = 2.7255
def bek_bits(Rm, Ej): return 2*math.pi*Rm*Ej/(HB*Cn*math.log(2))
Ej = M_KG*Cn**2
b1 = bek_bits(1.0, Ej); b875 = bek_bits(0.875, Ej)
land = Ej/(KB*T*math.log(2))
ratio = b1/land
Rbe = HB*Cn/(2*math.pi*KB*T)
print("     Bekenstein 70 kg R=1 m   : %.6e bits" % b1)
print("     Bekenstein 70 kg R=0.875 : %.6e bits" % b875)
print("     ratio Bek/Landauer        : %.4f" % ratio)
print("     break-even radius          : %.6e m" % Rbe)
chk("E: 1.8038e45 bits (massform.py:461)", abs(b1/1.8038e45 - 1) < 5e-5)
chk("E: nopath.bekenstein_bits agrees", abs(nopath.bekenstein_bits(1.0, Ej)/b1 - 1) < 1e-14)
chk("E: 1.58e45 at R = 0.875 m", abs(b875/1.58e45 - 1) < 3e-3)
chk("E: ratio 7478 (massform.py:472)", round(ratio) == 7478)
chk("E: break-even 0.134 mm (massform.py:474)", abs(Rbe*1e3 - 0.134) < 5e-4)
# routes_agree: the Schwarzschild saturation as the tree codes it, at its own mass
chk("E: nopath.routes_agree() (Bekenstein at r_s == A/4 l_P^2)", nopath.routes_agree())

# ---------------- F  hypotheses on the tree's instance
compact = 2*Gn*M_KG/(Cn**2*1.0)
print("     2GM/(c^2 R) for 70 kg, 1 m: %.3e" % compact)
chk("F: weakly self-gravitating (2GM/c^2R << 1)", compact < 1e-20)
holo_bits = nopath.holographic_bits(1.0)
chk("F: Bekenstein figure < spherical/holographic bound at R = 1 m (Bousso eq 2.25 direction)", b1 < holo_bits)
print("     holographic bits R=1 m: %.4e ; Bek/holo = %.3e" % (holo_bits, b1/holo_bits))
# E includes rest mass (complete-system hypothesis, Bekenstein quant-ph/0404042 Sec. II)
chk("F: E = M c^2 (rest energy included, as Bekenstein 2004 Sec. II requires)", Ej == M_KG*Cn**2)

# ---------------- G  data moves
# hbar, c, k_B exact in SI since 2019 (CODATA 2018 = 2022 for these); G CODATA 2018 6.67430e-11, CODATA 2022 6.67430e-11
chk("G: tree constants == SI-exact hbar(1.054571817e-34 is the rounded exact h/2pi), c, k_B",
    Cn == 299792458.0 and KB == 1.380649e-23 and abs(HB/(6.62607015e-34/(2*math.pi)) - 1) < 1e-9)
T2 = 2.72548
r2 = 2*math.pi*1.0*KB*T2/(HB*Cn)
print("     ratio with T = 2.72548 K: %.4f (vs %.4f); relative move %.2e" % (r2, ratio, r2/ratio-1))
chk("G: T_CMB 2.7255 -> 2.72548 does not move '7478'", round(r2) == 7478)
print("     G enters only the saturation check (cancels: both sides = 4 pi G M^2/hbar c); not the bound")

print("\nALL PASS" if ok_all else "\nSOME FAIL")
sys.exit(0 if ok_all else 1)
