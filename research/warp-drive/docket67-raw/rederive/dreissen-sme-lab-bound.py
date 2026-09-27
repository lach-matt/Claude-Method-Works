"""DOCKET 67 -- audit of dreissen-sme-lab-bound (branelink.py:149, 97-98, 308).

What is checkable here WITHOUT the source (Dreissen et al. arXiv:2206.00570 and
Kabat & Nomura arXiv:2309.05759 could not be opened in this stage):
  (a) the tree's own arithmetic: |c| at r = 38.6 um, beta = 1 and log10(1e-21/|c|) = 42;
  (b) SENSITIVITY: how far the bound value would have to move before "does not bite"
      at (r = 38.6 um, beta = 1) changes -- i.e. whether the datum can move the conclusion;
  (c) the r- and beta-dependence the tree's statement fixes: where (r, beta) the SAME
      formula and the SAME 1e-21 WOULD bite -- the scope of "does not bite";
  (d) the mu*r -> 0 caveat: m_e * r / (hbar c) at r = 38.6 um (identity of mu NOT read).
Constants are taken from the tree's modules (read-only import), not retyped.
"""
import math, sys
from fractions import Fraction
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import branelink as B
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

# (a) tree arithmetic, recomputed with an exact zeta(3) instead of the tree's partial sum
r, beta, M, hc = sp.symbols('r beta Mbar hbarc', positive=True)
c_sym = (1/(16*sp.pi**2)) / (sp.pi*(r/hc)*M)**2 * sp.Rational(3,4) * beta**2 * sp.zeta(3)/4
c_tree = B.sme_coefficient()
c_exact = float(c_sym.subs({r: B.R_EOTWASH, hc: B.HBARC_GEV_M, M: B.MBAR4_GEV, beta: 1}).evalf(30))
print("  |c| tree  =", c_tree)
print("  |c| sympy =", c_exact, " (exact zeta(3))")
chk("(a1) tree |c| = sympy |c| to 1e-9 rel", abs(c_tree/c_exact - 1) < 1e-9)
chk("(a2) |c| = 6.37e-64 to 1e-3 rel (branelink selftest pin)", abs(c_exact/6.37e-64 - 1) < 1e-3)
orders = math.log10(B.SME_LAB_BOUND / c_exact)
print("  log10(1e-21/|c|) =", orders)
chk("(a3) rounds to 42 (SME_ORDERS_SHORT)", round(orders) == 42 and abs(B.SME_ORDERS_SHORT - orders) < 1e-9)
chk("(a4) scaling |c| ~ beta^2 / r^2 exactly", sp.simplify(sp.diff(sp.log(c_sym), r)*r + 2) == 0
    and sp.simplify(sp.diff(sp.log(c_sym), beta)*beta - 2) == 0)

# (b) sensitivity of the conclusion to the bound's VALUE
#   "does not bite" at (38.6 um, 1)  <=>  bound > |c|.  Margin in orders:
for trial in (1e-19, 1e-20, 1e-21, 1e-22, 1e-23):
    print("  bound %.0e -> %.2f orders short" % (trial, math.log10(trial/c_exact)))
chk("(b1) any bound in [1e-23, 1e-19] leaves >= 40 orders short at (38.6 um, beta=1)",
    all(math.log10(t/c_exact) >= 40 for t in (1e-19, 1e-23)))
chk("(b2) the bound would have to improve by > 1e42 to bite at (38.6 um, beta=1)",
    B.SME_LAB_BOUND / c_exact > 1e42)

# (c) scope: where would the SAME formula and the SAME bound bite?
#   |c|(r, beta) = |c|0 * beta^2 * (r0/r)^2 ; bites when >= 1e-21
r0 = B.R_EOTWASH
r_bite_b1 = r0 * math.sqrt(c_exact / B.SME_LAB_BOUND)
E_bite_b1 = B.HBARC_GEV_M / r_bite_b1
print("  beta = 1: bites for r <= %.3e m  (hbar c / r = %.3e GeV)" % (r_bite_b1, E_bite_b1))
beta_gw = B.BETA_MAX
r_bite_gw = r0 * beta_gw * math.sqrt(c_exact / B.SME_LAB_BOUND)
L_PL = math.sqrt(B.HBAR * B.G / B.C**3)
print("  beta = %.4e (tree's GW170817 bound): bites for r <= %.3e m = %.1f l_Planck"
      % (beta_gw, r_bite_gw, r_bite_gw / L_PL))
chk("(c1) at beta = 1 the bound DOES bite below r ~ 3e-26 m (so 'does not bite' is a statement AT r = 38.6 um, not over all r)",
    2e-26 < r_bite_b1 < 4e-26)
chk("(c2) at the tree's beta_max the bite threshold r is within 1e3 Planck lengths (EFT validity there is not established)",
    r_bite_gw / L_PL < 1e3)
# at beta = beta_max, r = 38.6 um:
c_gw = c_exact * beta_gw**2
print("  at beta_max, r = 38.6 um: |c| = %.3e, %.1f orders short" % (c_gw, math.log10(1e-21/c_gw)))

# (d) mu r -> 0 caveat, IF mu were the electron mass (identity of mu NOT read here)
ME_GEV = 0.51099895069e-3        # PDG 2024 electron mass, GeV (context only)
x = ME_GEV * r0 / B.HBARC_GEV_M
print("  m_e r / (hbar c) at r = 38.6 um = %.3e" % x)
chk("(d1) m_e r >> 1 at r = 38.6 um: IF mu = m_e the mu r -> 0 limit is not the regime evaluated (OPEN: mu not read)", x > 1e7)

# (e) sign/direction: component projection. IF KN's c_{mu nu} is built on a preferred
#     4-velocity u (c ~ |c| (u_mu u_nu + eta_{mu nu}/4)), a lab moving at speed v relative to
#     that frame sees anisotropic spatial parts c_JK ~ gamma^2 v^2 |c| <= |c| for v<=~1:
v = sp.symbols('v', positive=True)
g2 = 1/(1-v**2)
cjk_over_c = sp.simplify(g2*v**2)       # u_J u_K amplitude in the lab frame
print("  c_JK/|c| (hypothetical preferred-frame structure) =", cjk_over_c,
      "; at v = 1.23e-3 (CMB dipole):", float(cjk_over_c.subs(v, B.V_CMB/B.C)))
chk("(e1) under that HYPOTHETICAL structure the Sun-frame spatial coefficient is suppressed by v^2 ~ 1.5e-6 at the CMB speed (drift runs AGAINST biting)",
    float(cjk_over_c.subs(v, B.V_CMB/B.C)) < 2e-6)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
