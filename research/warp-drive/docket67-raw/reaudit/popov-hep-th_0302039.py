"""DOCKET 67 RE-AUDIT: Popov hep-th/0302039v2 (READ this run via alphaXiv, pp.1-2, 4-5, 8-12, 14-16)
and the AHS content it restates.  Shared by the four re-audit JSONs
  hep-th_0302039.json, hep-th_0302039_domain.json, hep-th_0302039_seciv.json, ahs-1995-prd51-4337.json

P1  Popov's PRINTED (B1)-(B3) at xi = 1/6, m = 0 -- transcribed HERE, independently, from the alphaXiv
    text layer of v2 pp.14-16 (the (xi-1/6), (xi-1/6)^2 and m brackets dropped) -- equals the tree's
    transcription hpscentre.build()['popov'] term by term (imported read-only).
P2  M1/M3 AS PRINTED: B1 log carries -116 f'^2 f'' r^8 f; B3's -21 r^8 f'^4 sits inside the
    (xi-1/6)^2 bracket (printed next to +7020 r^8 f'^4 in the same bracket).  Printed B3 is NOT
    conserved; with -21 r^8 f'^4 moved into the xi-free log bracket it IS, identically in f, r.
P3  Popov (M3 restored), log sign flipped per u0 = w0 sqrt(r^2/f) (eq. 20/68), equals HPS (5)-(7) at the
    conserved reading (116, 21, r^2) exactly: the tree's mapping and its three disagreements.
P4  The scale (log) part is separately conserved and traceless.
P5  Popov eqs (62)-(64) [(T)^(0), high-frequency] + (75)-(76) at m = 0 [low-frequency, AF, Boulware]
    cancel identically with Omega_0 = w0/sqrt(f); (65)-(67) vanish at xi = 1/6, m = 0.  So in AF/Boulware
    <T>_ren -> (T)^(4) = AHS analytic, which is Popov's p.12 statement; and (T)^(0) is by itself
    conserved and traceless, i.e. the high-frequency part is (T)^(0)+(T)^(2)+(T)^(4)+..., of which the
    AHS expression is the fourth WKB order only.
"""
import sys, os, importlib.util
sys.dont_write_bytecode = True
import sympy as sp

TREE = '/home/user/Claude-Method-Works/research/warp-drive'
sys.path.insert(0, TREE)
spec = importlib.util.spec_from_file_location('hpscentre', os.path.join(TREE, 'hpscentre.py'))
hpc = importlib.util.module_from_spec(spec); spec.loader.exec_module(hpc)

res = []
def chk(name, ok):
    res.append((name, bool(ok))); print(('PASS ' if ok else 'FAIL ') + name)

S = hpc.build(sp)
l = S['l']; f, f1, f2, f3, f4 = S['F']; r, r1, r2, r3, r4 = S['R']
Q = r**2
q1, q2, q3, q4 = [sp.diff(Q, l, k) for k in range(1, 5)]
d = r**8*f**4

# ---------------- P1: my transcription of Popov v2 App. B, printed, xi = 1/6, m = 0 ----------------
# (B1) T^t_t : non-log part (after the m^4, m^2 terms), then the xi-free part of the log bracket
B1n = (32*r**4*f**4 - 32*q4*r**6*f**4 - 12*f2**2*r**8*f**2 + 56*q2**2*r**4*f**4 + 16*f4*r**8*f**3
       + 7*f1**4*r**8 - 32*f2*q2*r**6*f**3 - 16*f1*q1**3*r**2*f**3 + 40*f1**2*q2*r**6*f**2
       - 16*f1*f3*r**8*f**2 + 16*f2*q1**2*r**4*f**3 + 4*f1**2*f2*r**8*f - 12*f1**3*q1*r**6*f
       - 14*f1**2*q1**2*r**4*f**2 - 48*f1*q3*r**6*f**3 + 48*q1*q3*r**4*f**4
       - 112*q1**2*q2*r**2*f**4 + 32*f1*q2*q1*r**4*f**3 + 40*q1**4*f**4 + 32*q1*f3*r**6*f**3)
B1l = (-16*r**4*f**4 - 20*q1**4*f**4 + 56*q1**2*q2*r**2*f**4 + 8*f1*q2*q1*r**4*f**3
       - 28*q2**2*r**4*f**4 - 16*f4*r**8*f**3 + 52*f1*f2*q1*r**6*f**2 + 16*q4*r**6*f**4
       + 36*f2**2*r**8*f**2 + 49*f1**4*r**8 - 4*f1*q1**3*r**2*f**3 - 4*f1**2*q2*r**6*f**2
       + 48*f1*f3*r**8*f**2 + 4*f2*q1**2*r**4*f**3 - 116*f1**2*f2*r**8*f - 22*f1**3*q1*r**6*f
       - 3*f1**2*q1**2*r**4*f**2 + 8*f1*q3*r**6*f**3 - 32*q1*f3*r**6*f**3
       - 24*q1*q3*r**4*f**4 - 8*f2*q2*r**6*f**3)
# (B2) T^rho_rho
B2n = (f1**4*r**8 + 32*f1*q2*q1*r**4*f**3 - 4*f1**2*f2*r**8*f - 24*f2*q1**2*r**4*f**3
       - 16*f1*q3*r**6*f**3 - 16*q1*f3*r**6*f**3 - 8*f1*q1**3*r**2*f**3 - 24*f1**2*q2*r**6*f**2
       + 12*f1**2*q1**2*r**4*f**2 + 8*f1*f3*r**8*f**2 - 4*f2**2*r**8*f**2 + 16*f2*q2*r**6*f**3
       - 8*f1**3*q1*r**6*f + 32*f1*f2*q1*r**6*f**2)
B2l = (12*f2*q1**2*r**4*f**3 - 16*r**4*f**4 - 4*q1**4*f**4 + 8*f1**2*q2*r**6*f**2
       + 12*f1**2*f2*r**8*f + 8*q1*f3*r**6*f**3 - 8*f1*f3*r**8*f**2 + 8*f1*q3*r**6*f**3
       - 24*f1*f2*q1*r**6*f**2 - 3*f1**2*q1**2*r**4*f**2 + 4*f1*q1**3*r**2*f**3
       - 16*f1*q2*q1*r**4*f**3 + 8*q1**2*q2*r**2*f**4 - 8*q1*q3*r**4*f**4
       + 10*f1**3*q1*r**6*f - 7*f1**4*r**8 - 8*f2*q2*r**6*f**3 + 4*f2**2*r**8*f**2
       + 4*q2**2*r**4*f**4)
# (B3) T^theta_theta
B3n = (-8*r**4*f**3*f1*q2*q1 + 16*r**6*f**2*f1*f2*q1 + 17*r**8*f1**4 - 16*r**8*f**3*f4
       - 8*r**6*f*f1**3*q1 + 16*r**6*f**3*f1*q3 + 16*r**4*f**3*f2*q1**2 - 52*r**8*f*f1**2*f2
       + 24*r**8*f**2*f1*f3 - 4*r**4*f**2*f1**2*q1**2 + 8*r**6*f**2*f1**2*q2 + 28*r**8*f**2*f2**2
       - 24*r**6*f**3*q1*f3 - 16*r**6*f**3*f2*q2)
B3l = (16*r**4*f**4 - 20*r**8*f**2*f1*f3 + 12*f**4*q1**4 - 14*r**6*f**2*f1*f2*q1
       + 12*r**6*f**3*q1*f3 + 8*r**6*f**3*f2*q2 + 6*r**6*f*f1**3*q1 - 2*r**6*f**2*f1**2*q2
       - 8*r**6*f**3*f1*q3 + 12*r**4*f**4*q2**2 - 20*r**8*f**2*f2**2 + 4*r**4*f**3*f1*q2*q1
       - 8*r**4*f**3*f2*q1**2 + 3*r**4*f**2*f1**2*q1**2 + 16*r**4*f**4*q1*q3
       + 52*r**8*f*f1**2*f2 + 8*r**8*f**3*f4 - 8*r**6*f**4*q4 - 32*r**2*f**4*q1**2*q2)
M3_TERM = -21*r**8*f1**4        # printed as the 2nd term INSIDE B3's (xi-1/6)^2 log bracket

mine = ((B1n/d, B1l/d), (B2n/d, B2l/d), (B3n/d, B3l/d))
for (a, b), (c, e), lab in zip(mine, S['popov'], ('B1', 'B2', 'B3')):
    chk('P1 %s non-log: this transcription == tree hpscentre.build popov' % lab, sp.expand(a - c) == 0)
    chk('P1 %s log    : this transcription == tree hpscentre.build popov' % lab, sp.expand(b - e) == 0)

# ---------------- P2: conservation of Popov as printed vs M3 restored ----------------
lnf = sp.log(f); c0 = sp.Symbol('c0')          # Popov's log = ln|4 w0^2/(m_DS^2 f)| = c0 - ln f
def T_of(logs):
    return tuple(n + (c0 - lnf)*g for (n, _), g in zip(mine, logs))
printed = T_of((B1l/d, B2l/d, B3l/d))
restored = T_of((B1l/d, B2l/d, (B3l + M3_TERM)/d))
chk('P2 Popov AS PRINTED (M3 inside the (xi-1/6)^2 bracket) is NOT conserved',
    hpc.divergence(sp, S, printed) != 0)
chk('P2 Popov with -21 r^8 f\'^4 moved into the xi-free log bracket IS conserved identically',
    hpc.divergence(sp, S, restored) == 0)
chk('P2 M1 as printed in Popov (B1): coefficient of ln-bracket f\'^2 f\'\' r^8 f is -116',
    sp.Poly(sp.expand(B1l), f1, f2).coeff_monomial(f1**2*f2) == -116*r**8*f)

# ---------------- P3: against HPS at the conserved reading ----------------
Ssub = {sp.Symbol('alpha_tt'): 116, sp.Symbol('alpha_th'): 21, sp.Symbol('ll_pow'): 2}
ok = True
for (hn, hl), (pn, pl), extra in zip(S['hps'], mine, (0, 0, M3_TERM/d)):
    ok &= sp.expand(hn - pn) == 0
    ok &= sp.expand(hl.subs(Ssub) + (pl + extra)) == 0       # HPS ln f coefficient = MINUS Popov's
chk('P3 HPS (5)-(7) at (116, 21, r^2) == Popov (B1)-(B3) with M3 restored, log sign flipped', ok)
u0, w0, mDS = sp.symbols('u0 w0 m_DS', positive=True)
fp, rp = sp.symbols('fp rp', positive=True)
chk('P3 ln|4u0^2/(m_DS^2 r^2)| with u0 = w0 sqrt(r^2/f) (Popov (20),(68)) = ln(4 w0^2/(m_DS^2 f))',
    sp.simplify(sp.expand_log(sp.log(4*(w0*sp.sqrt(rp**2/fp))**2/(mDS**2*rp**2)) - sp.log(4*w0**2/(mDS**2*fp)), force=True)) == 0)

# ---------------- P4: scale part ----------------
scale = tuple(g for g in (B1l/d, B2l/d, (B3l + M3_TERM)/d))
chk('P4 scale (log-constant) part separately conserved', hpc.divergence(sp, S, scale) == 0)
chk('P4 scale part traceless', sp.expand(scale[0] + scale[1] + 2*scale[2]) == 0)

# ---------------- P5: (T)^(0) + LFC ----------------
Om0 = w0/sp.sqrt(f); U0 = w0*sp.sqrt(r**2/f)
T0 = (U0**4/(16*sp.pi**2*r**4), -U0**4/(48*sp.pi**2*r**4), -U0**4/(48*sp.pi**2*r**4))   # (62)-(64)
LFC = (-Om0**4/(16*sp.pi**2), Om0**4/(48*sp.pi**2), Om0**4/(48*sp.pi**2))              # (75),(76) m=0
chk('P5 (T)^(0) [(62)-(64)] + LFC [(75)-(76), m=0, Omega0 = w0/sqrt f] = 0 componentwise',
    all(sp.simplify(a + b) == 0 for a, b in zip(T0, LFC)))
chk('P5 (T)^(0) alone is conserved', sp.simplify(hpc.divergence(sp, S, T0)) == 0)
chk('P5 (T)^(0) alone is traceless', sp.simplify(T0[0] + T0[1] + 2*T0[2]) == 0)
xi, m = sp.symbols('xi m')
T2tt = U0**2/(4*sp.pi**2*r**2)*((xi - sp.Rational(1, 6))*(1/(2*r**2) + 5*f1**2/(4*f**2) - f1*q1/(f*r**2)
       + q1**2/(8*r**4) - f2/f - q2/(2*r**2)) + m**2/4)                          # (65)
chk('P5 (T)^(2) [(65)] vanishes at xi = 1/6, m = 0', sp.simplify(T2tt.subs({xi: sp.Rational(1, 6), m: 0})) == 0)

print('\n%d checks, %d FAIL' % (len(res), sum(1 for _, ok in res if not ok)))
sys.exit(0 if all(ok for _, ok in res) else 1)
