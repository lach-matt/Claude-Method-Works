#!/usr/bin/env python3
"""DOCKET 67 re-derivation for 1809.06923 (Markkanen, Rajantie, Stopyra 2018).

What is finite / closed-form here:
  (1) the flat-space thin-wall bubble: after nucleation at Coleman's radius
      R0 = 3 sigma/eps the wall follows x^2 - t^2 = R0^2, its speed -> c, and
      ALL released vacuum energy sits in the wall (the source's 'expand at near
      the speed of light, releasing energy into the bubble wall').
      Hypotheses: H-FLAT (no gravity), H-THIN (thin wall), H-NOFRIC (no plasma
      friction), H-SUPER (bubble nucleated at/above R0).
  (2) 'different masses inside': m_f = y_f h / sqrt2, so any interior Higgs
      value h_in != v rescales every Yukawa mass by h_in/v.
  (3) z3: the tree's INFERENCE 'masses differ AND destroys what it meets ->
      forms no atomic mass at the seat' is NOT a propositional entailment; it
      needs a bridging hypothesis (named here H-BRIDGE).  And the tree's C4
      combination is independent of the metastable/stable case (top mass).
  (4) the tree's own booleans, recomputed from its held transcription
      (massform.SOURCES['MRS-bubble']); this checks the tree against its
      transcription, NOT against the source (not re-readable this session).
"""
import sys, math, json
import sympy as sp
import z3

out = {}

# ---------------------------------------------------------------- (1)
t, R0, sig, eps, R = sp.symbols('t R0 sigma epsilon R', positive=True)
Rt = sp.sqrt(R0**2 + t**2)
v = sp.diff(Rt, t)
gamma = 1/sp.sqrt(1 - v**2)
# static energy of a bubble at rest: surface minus volume term
E_static = 4*sp.pi*R**2*sig - sp.Rational(4, 3)*sp.pi*eps*R**3
Rc = 3*sig/eps
out['E_static(3sigma/eps)=0'] = sp.simplify(E_static.subs(R, Rc)) == 0
# energy conservation with E_total = 0: wall energy 4 pi R^2 sigma gamma = (4/3) pi eps R^3
gam_needed = sp.simplify((sp.Rational(4, 3)*sp.pi*eps*R**3)/(4*sp.pi*R**2*sig))  # = R/R0
out['gamma_needed == R/Rc'] = sp.simplify(gam_needed - R/Rc) == 0
out['hyperbola gamma == R(t)/R0'] = sp.simplify(gamma - Rt/R0) == 0
out['lim_{t->oo} v'] = str(sp.limit(v, t, sp.oo))
# fraction of released vacuum energy carried by the wall along the trajectory (R0 = 3 sigma/eps)
frac = sp.simplify((4*sp.pi*Rt**2*sig*gamma) / (sp.Rational(4, 3)*sp.pi*eps*Rt**3)).subs(R0, Rc)
out['wall energy / released vacuum energy'] = str(sp.simplify(frac))
# numeric illustration: R0 ~ 1/(1e11 GeV) (the tree's Degrassi instability scale, order only)
hbarc_GeV_m = 1.973269804e-16
R0_m = hbarc_GeV_m/1e11
for Rm in (1e-10, 1.0, 6.371e6):
    g = Rm/R0_m
    out[f'R={Rm:g} m: gamma, 1-v'] = (f'{g:.3e}', f'{1/(2*g*g):.3e}')

# ---------------------------------------------------------------- (2)
v_EW = 246.21965          # GeV, (sqrt2 G_F)^(-1/2), G_F = 1.1663788e-5 GeV^-2 (PDG)
me = 0.51099895e-3        # GeV
scal = {}
for label, hin in (('h_in = 1e10 GeV', 1e10), ('h_in = 1e12 GeV', 1e12),
                   ('h_in = M_Pl = 1.22e19 GeV', 1.22e19)):
    r = hin/v_EW
    scal[label] = {'mass ratio h_in/v': f'{r:.3e}', 'm_e inside [GeV]': f'{me*r:.3e}'}
out['Yukawa rescaling (illustrative interior values, not READ)'] = scal

# ---------------------------------------------------------------- (3)
A, B, F, BR = z3.Bools('masses_differ destroys_what_it_meets atomic_mass_forms H_BRIDGE')
s = z3.Solver(); s.add(A, B, F)
out['A & B & F satisfiable (inference not an entailment)'] = str(s.check())
s2 = z3.Solver(); s2.add(z3.Implies(z3.And(A, B), z3.Not(F)), A, B, F)
out['with H-BRIDGE (A&B -> not F): A&B&F'] = str(s2.check())
rel, dec, meta = z3.Bools('rel dec meta')
fs = lambda m: z3.Or(rel, z3.And(m, dec))
c4 = z3.Or(fs(True), fs(False))
p = z3.Solver(); p.add(z3.Not(c4 == z3.Or(rel, dec)))
out['c4_combined == rel | dec (valid)'] = str(p.check()) == 'unsat'
p2 = z3.Solver(); p2.add(z3.Not(z3.Implies(z3.And(z3.Not(rel), z3.Not(dec)), z3.Not(c4))))
out['not rel & not dec -> not C4 (valid)'] = str(p2.check()) == 'unsat'

# ---------------------------------------------------------------- (4)
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import massform as mf
    out['tree: DECAY_CHANGES_PARTICLE_MASSES'] = mf.DECAY_CHANGES_PARTICLE_MASSES
    out['tree: DECAY_DESTROYS_WHAT_IT_MEETS'] = mf.DECAY_DESTROYS_WHAT_IT_MEETS
    out['tree: VACUUM_DECAY_FORMS_ATOMIC_MASS_AT_THE_SEAT'] = mf.VACUUM_DECAY_FORMS_ATOMIC_MASS_AT_THE_SEAT
    out['tree: HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY'] = mf.HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY
    held = mf.SOURCES['MRS-bubble'][2]
    out['tree held text mentions gravitational collapse'] = 'gravitational collapse' in held
    out['tree held text: "near the speed of light" and "at the speed of light"'] = (
        'near the speed of light' in held, 'expands at the speed of light' in held)
except Exception as e:  # pragma: no cover
    out['tree import'] = f'FAILED: {e!r}'

print(json.dumps(out, indent=1, default=str))
ok = (out['E_static(3sigma/eps)=0'] and out['gamma_needed == R/Rc'] and out['hyperbola gamma == R(t)/R0']
      and out['lim_{t->oo} v'] == '1' and out['wall energy / released vacuum energy'] == '1'
      and out['A & B & F satisfiable (inference not an entailment)'] == 'sat'
      and out['with H-BRIDGE (A&B -> not F): A&B&F'] == 'unsat'
      and out['c4_combined == rel | dec (valid)'] and out['not rel & not dec -> not C4 (valid)'])
print('ALL CHECKS AGREE' if ok else 'A CHECK DISAGREES')
sys.exit(0 if ok else 1)
