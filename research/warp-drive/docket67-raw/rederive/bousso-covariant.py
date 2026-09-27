#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation / machine check for 'bousso-covariant'
(Bousso covariant entropy bound, hep-th/9905177; review hep-th/0203101;
FMW proofs hep-th/9908070).

READ-ONLY with respect to research/warp-drive: bounds.py is imported with
sys.dont_write_bytecode = True, and every counterfactual re-coding below is
made on an in-memory copy and restored.  Nothing is repaired.

Sections
  A  sympy: the A/4G coefficient from Hawking T and the first law; G enters
     the RHS (dS/dG != 0 at fixed A; bound -> trivial as G -> 0); Bekenstein
     2 pi R E / hbar c has no G; Schwarzschild saturates Bekenstein exactly.
  B  numeric: Bousso's printed '1.4 x 10^69 bits per square meter' from
     CODATA 2022 (and 1998) constants.
  C  numeric: FMW first theorem, per generator: |s| <= (lam_inf - lam) f / 8
     => int s A dlam <= (1 - A_end)/4.  Random adversarial profiles + a
     non-vacuity guard (hypothesis violated x3 -> violations must appear).
  D  sympy + numeric: FMW second theorem constants (pi a1)^(1/4)+(a2/pi)^(1/2)=1
     for a1 = 1/(16 pi), a2 = pi/4; per-generator check of
     I <= (1/4) (1 - A_end)^(1/2) under s^2 <= b1 f, |s'| <= b2 f.
  E  the tree's coding (bounds.py:50, 195, 316, 457-459) against the source:
     G, Z, K, B slots, with the exact cost of each counterfactual re-coding.
"""
import sys, math, random, json
sys.dont_write_bytecode = True
import sympy as sp

OUT = {}
ok_all = True
def rec(name, ok, detail):
    global ok_all
    ok_all &= bool(ok)
    OUT[name] = {"ok": bool(ok), "detail": detail}
    print("  [%s] %-62s %s" % ("ok" if ok else "XX", name, detail))

print("A. Bekenstein-Hawking coefficient and the G slot (sympy)")
M, G, hb, c, k, A, R, E = sp.symbols('M G hbar c k A R E', positive=True)
T_H = hb*c**3/(8*sp.pi*G*M*k)
S_bh = sp.integrate(c**2/T_H, (M, 0, M))           # dS = dE/T, E = M c^2
A_s = 16*sp.pi*G**2*M**2/c**4                        # Schwarzschild horizon area
ratio = sp.simplify(S_bh / (k*A_s*c**3/(4*G*hb)))
rec("S_BH = k A c^3/(4 G hbar) from T_H and first law", ratio == 1, "ratio=%s" % ratio)
bousso_rhs = k*A*c**3/(4*G*hb)
dG = sp.diff(bousso_rhs, G)
rec("Bousso RHS depends on G at fixed A (G slot = 1)", sp.simplify(dG) != 0, "d/dG = %s" % dG)
rec("Bousso RHS -> oo as G -> 0 (bound trivial without gravity)",
    sp.limit(bousso_rhs, G, 0, '+') == sp.oo, "lim = oo")
bek = 2*sp.pi*k*R*E/(hb*c)
rec("Bekenstein RHS has no G (tree's DOCKET 4 contrast)", sp.diff(bek, G) == 0, "d/dG = 0")
sat = sp.simplify(bek.subs({R: 2*G*M/c**2, E: M*c**2}) - S_bh)
rec("Schwarzschild saturates Bekenstein exactly (tree's K=0 standard)", sat == 0, "diff=%s" % sat)

print("B. '1.4 x 10^69 bits per square meter' (hep-th/0203101 abstract)")
c_ = 299792458.0
hbar22 = 1.054571817e-34
for label, Gv, hb_ in (("CODATA 2022", 6.67430e-11, hbar22),
                       ("CODATA 1998", 6.673e-11, 1.054571596e-34)):
    bits = c_**3/(4*Gv*hb_*math.log(2))
    OUT.setdefault("bits_per_m2", {})[label] = bits
    print("     %s: c^3/(4 G hbar ln2) = %.4e bits/m^2   (l_P = %.5e m)"
          % (label, bits, math.sqrt(Gv*hb_/c_**3)))
b22 = OUT["bits_per_m2"]["CODATA 2022"]; b98 = OUT["bits_per_m2"]["CODATA 1998"]
rec("printed 1.4e69 reproduced to 2 s.f. (CODATA 2022)", abs(b22/1.4e69 - 1) < 0.04, "%.4e" % b22)
rec("move 1998 -> 2022 in G is < 0.1 % of the density", abs(b22/b98 - 1) < 1e-3,
    "rel shift %.2e" % (b22/b98 - 1))

# ---------------------------------------------------------------------------
def integrate_generator(fprof, theta0, n=4000):
    """G = sqrt(A): G'' = -f G / 2, G(0)=1, G'(0)=theta0/2.  RK4 on [0,1];
    stop at a caustic (G -> 0).  Returns (lams, Gs, lam_end)."""
    h = 1.0/n
    lam, g, gp = 0.0, 1.0, theta0/2.0
    L, Gs = [0.0], [1.0]
    def acc(l, gg): return -0.5*fprof(l)*gg
    for i in range(n):
        k1g, k1p = gp, acc(lam, g)
        k2g, k2p = gp+0.5*h*k1p, acc(lam+0.5*h, g+0.5*h*k1g)
        k3g, k3p = gp+0.5*h*k2p, acc(lam+0.5*h, g+0.5*h*k2g)
        k4g, k4p = gp+h*k3p, acc(lam+h, g+h*k3g)
        gn = g + h*(k1g+2*k2g+2*k3g+k4g)/6
        gpn = gp + h*(k1p+2*k2p+2*k3p+k4p)/6
        if gn <= 0.0:                          # caustic inside this step
            lam_c = lam + h*g/(g-gn)
            L.append(lam_c); Gs.append(0.0)
            return L, Gs, lam_c
        lam, g, gp = lam+h, gn, gpn
        L.append(lam); Gs.append(g)
    return L, Gs, 1.0

def rand_f(rng):
    bumps = [(rng.uniform(0, 1), rng.uniform(0.01, 0.3), rng.uniform(0, 1)**3*rng.choice([0.1, 1, 10, 50]))
             for _ in range(rng.randint(1, 4))]
    base = rng.uniform(0, 1)*rng.choice([0, 0.1, 1, 5])
    return lambda l: base + sum(a*math.exp(-((l-m)/w)**2) for m, w, a in bumps)

def trap(xs, ys):
    return sum(0.5*(xs[i+1]-xs[i])*(ys[i+1]+ys[i]) for i in range(len(xs)-1))

print("C. FMW first theorem (hep-th/9908070 Sec. II.C), per generator, G=1 units")
rng = random.Random(67)
worst = 0.0; nviol = 0; N = 400
for t in range(N):
    f = rand_f(rng); th0 = -rng.uniform(0, 3)*rng.choice([0, 1])
    L, Gs, le = integrate_generator(f, th0)
    s = [(le - l)*f(l)/8.0 for l in L]                  # hypothesis (1.9) saturated
    I = trap(L, [si*g*g for si, g in zip(s, Gs)])
    bound = (1.0 - Gs[-1]**2)/4.0
    r = I/bound if bound > 0 else 0.0
    worst = max(worst, r); nviol += (I > bound*(1+1e-6))
rec("I <= (1 - A_end)/4 on %d random generators" % N, nviol == 0, "max I/bound = %.4f" % worst)
OUT["fmw1_max_ratio"] = worst
nv = 0
for t in range(N):
    f = rand_f(rng); th0 = -rng.uniform(0, 3)*rng.choice([0, 1])
    L, Gs, le = integrate_generator(f, th0)
    s = [3.0*(le - l)*f(l)/8.0 for l in L]              # hypothesis violated x3
    I = trap(L, [si*g*g for si, g in zip(s, Gs)])
    nv += I > (1.0 - Gs[-1]**2)/4.0*(1+1e-6)
rec("non-vacuity guard: s at 3x the hypothesis violates somewhere", nv > 0, "%d/%d violate" % (nv, N))

print("D. FMW second theorem (Sec. II.D)")
a1, a2 = sp.Rational(1, 16)/sp.pi, sp.pi/4
cond = sp.simplify((sp.pi*a1)**sp.Rational(1, 4) + (a2/sp.pi)**sp.Rational(1, 2))
rec("(pi a1)^(1/4) + (a2/pi)^(1/2) = 1 for a1=1/(16pi), a2=pi/4", cond == 1, "= %s" % cond)
b1 = float(a1/(8*sp.pi)); b2 = float(a2/(8*sp.pi))        # f >= 8 pi T_kk
worst2 = 0.0; nviol2 = 0
for t in range(N):
    amp = rng.uniform(0, 1)*rng.choice([0.01, 0.1, 1, 10])
    m, w = rng.uniform(0, 1), rng.uniform(0.05, 0.5)
    sfun = lambda l, amp=amp, m=m, w=w: amp*math.exp(-((l-m)/w)**2)
    spf = lambda l, amp=amp, m=m, w=w: amp*math.exp(-((l-m)/w)**2)*(-2*(l-m)/w**2)
    extra = rng.uniform(0, 1)*rng.choice([0, 1])
    f = lambda l: max(sfun(l)**2/b1, abs(spf(l))/b2) + extra
    th0 = -rng.uniform(0, 2)*rng.choice([0, 1])
    L, Gs, le = integrate_generator(f, th0)
    I = trap(L, [sfun(l)*g*g for l, g in zip(L, Gs)])
    bound = 0.25*math.sqrt(max(0.0, 1.0 - Gs[-1]**2))
    r = I/bound if bound > 0 else 0.0
    worst2 = max(worst2, r); nviol2 += I > bound*(1+1e-6)
rec("I <= (1/4)(1 - A_end)^(1/2) <= 1/4 on %d random generators" % N, nviol2 == 0,
    "max I/bound = %.4f" % worst2)
OUT["fmw2_max_ratio"] = worst2

print("E. the tree's coding of Bousso against the source (bounds.py, read-only import)")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import bounds
row = [r for r in bounds.BOUNDS if r[0] == "Bousso covariant"][0]
OUT["tree_row"] = list(row)
print("     tree row:", row)
rec("G = 1 and it is the only G = 1 row (bounds.py:459)",
    row[4] == 1 and bounds.gravitational() == ["Bousso covariant"], str(bounds.gravitational()))
# Source: L is a NULL hypersurface (hep-th/9905177 Sec. 2: 'we must use null
# hypersurfaces bounded by B'; hep-th/0203101 Sec. V: 'L is a null hypersurface,
# unlike V which is spacelike').  Slot Z: 1 = timelike or null, 2 = spacelike/region.
rec("DISCREPANCY RECORDED: Z coded 2 (spacelike/region); source is null (Z=1 cell)",
    row[6] == 2, "Z=%d" % row[6])
orig = list(bounds.BOUNDS)
def measure():
    X = bounds.cells()
    z2 = [r[0] for r in bounds.BOUNDS if r[6] == 2]
    return {"cells": len(X), "collisions": bounds.collisions(),
            "saturated": len(bounds.saturated()),
            "Z2": z2, "Z2_with_G": [r[0] for r in bounds.BOUNDS if r[6] == 2 and r[4] == 1],
            "every_Z2_has_entropy_LHS": all(r[1] == 2 for r in bounds.BOUNDS if r[6] == 2),
            "all_energy_LHS_have_Z01": all(r[6] in (0, 1) for r in bounds.BOUNDS if r[1] in (0, 1))}
try:
    base = measure()
    i = [j for j, r in enumerate(bounds.BOUNDS) if r[0] == "Bousso covariant"][0]
    r = list(bounds.BOUNDS[i]); r[6] = 1; bounds.BOUNDS[i] = tuple(r)
    cfZ = measure()
    bounds.BOUNDS[:] = orig
    r = list(bounds.BOUNDS[i]); r[5] = 0; bounds.BOUNDS[i] = tuple(r)
    cfK = measure()
finally:
    bounds.BOUNDS[:] = orig
OUT["coding_as_seated"] = base
OUT["counterfactual_Z_2_to_1"] = cfZ
OUT["counterfactual_K_1_to_0"] = cfK
print("     as seated     :", json.dumps(base))
print("     Z 2->1 (null) :", json.dumps(cfZ))
print("     K 1->0        :", json.dumps(cfK))
rec("Z 2->1 keeps 'every Z=2 bound has an entropy LHS' True", cfZ["every_Z2_has_entropy_LHS"], "")
rec("Z 2->1 empties 'region bounds with gravity' (tree:197 says two... of three)",
    cfZ["Z2_with_G"] == [], "as seated %s -> %s" % (base["Z2_with_G"], cfZ["Z2_with_G"]))
rec("restored in memory; no file written", bounds.BOUNDS == orig, "")

print()
print("ALL CHECKS", "PASS" if ok_all else "FAIL")
json.dump(OUT, open("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/bousso-covariant.out.json", "w"), indent=1, default=str)
sys.exit(0 if ok_all else 1)
