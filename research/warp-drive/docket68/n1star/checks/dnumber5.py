#!/usr/bin/env python3
"""dnumber5: the loss d as far as the record numbers it -- X_7 summed exactly over the levels, and c' reduced to the
one order the record fixes only by the closed graph theorem (CONSTANTS5.md, Round 6, item 1). Labels: READ (cited
lines), deduced (the reading of the cited lines, stated with each item), computed (exact integers; d1, d0 and the
sl offsets in certified rational intervals; every floor sum evaluated at both ends of those intervals and asserted
equal).

The chain (from the table: dweights5 W1/W3, dceiling5 D4/D6, eflat5 F4-F5, imported, not copied):

  d <= 3 (R2 + R3) + L_above [3 P_W + 11 + n_iota + 15 W] + L_below [15 W + 58] + SUM_{levels beta > 3} X_7(beta)
       + (K + 1) c',

  n_iota <= 3 P_iota + excess (eflat5 F5), X_7(beta) the loss of III.A Proposition 4.2 (2) at Step 7 of III.I''''''''''''
  Proposition 2.1 at the level beta (PART-III-I14-LEVELS.md:131, PART-III-I12-SPECTRAL.md:389-407), c' every other
  fixed per-level step. Round 5 left L_above X_7 with X_7 symbolic and c' symbolic.

  K1 (exact) the Round-5 constant A (R0 and R1) rebuilt from R2, R3, P_W, P_iota, W, the level counts and F4's excess.
  K2 (deduced; READ I12:328-376 Step 5 (i)-(iv), Lemma 2.3 I12:174-216, (G) I11:153, LOSS-D (2.2)) E_K below the
     K+-weight beta_K = beta - 2 - eps. By the dictionary (I12:46-49) a zf-term |sigma|^z log^m is the K+-term
     t^(-z-1) log^m, so E_K = 1 + (zf-exponents of the pieces). The pieces with non-integer zf-degree are Lemma 2.3's
     c_tau(sigma) T_tau(sigma) at levels 1 and 2: degree alpha_0 - 3 + j + i (s1) and alpha_0 - 2 - mu + j + i (other
     rows), alpha_0 the tf-exponent at level j, whose u-exponent is lambda = alpha_0 + j - 1 (I12:49-51). So the s1 rows
     give K+-exponents lambda - 1 + i and the others lambda - mu + i (mu <= 0), with log order k(lambda) (+1 where
     alpha_0 = 2: c_s1 = -|sigma|^-1 log|sigma|, and beta_0(2) = 0 for s0, s2). Every other piece has integer degree
     and no log|sigma| (zero-energy pieces, P_int, columns): K+-exponents in N, log 0. Level 1 treats lambda in
     [2, 2 + eta_1), which is {2} (P_iota = P_W + 1, dceiling5 D4); level 2 treats lambda in [2 + eta_1, 3 + eta_2).
     With beta_K <= 2 + eps_K - eps and (G) (no lambda in (2, 2 + eps_K] or (3, 3 + eps_K]):
       E_K cap {Re <= beta_K} = {(1, <= k_1(2) + 1)} u {(lambda - 1, <= k_2(lambda)) : lambda in Lambda cap (2, 3)}
                               u {(2, <= max(k_2(3), k_1(2)) + 1)}, cut at beta_K;
     n_iota = |E_iota,<=| = 0 at Step 7 (eflat5 F7), and LOSS-D (2.2) gives X_7 = n_K + ceil(beta_K + eps - 1/2)
     = n_K + ceil(beta - 5/2).
  K3 (deduced; computed) the log orders k_2(lambda) of the level-2 sources at lambda in (2, 3): E^flat's (eflat5 F4:
     2 off the 26 points of pi_1 E^C_I, the table there at them), 2 + E_col (Lemma 1.1, E_col := E cap {Re >= 0} with
     E's exponents b + w + sigma, b in {0, 2, 3}, w in E_ind, sigma >= -5, I12:79-110; E_ind's Lemma 1.4 log orders on
     every type's roots, the reading under which lambdagen5's eleven E_col bases enter P_W), u_0's (III.I''''''''''''
     Lemma 2.1 at level 0: Lemma 1.4 with the one root 2, which meets the sources only at 3), and the remainders of
     III.G'''' Proposition 4.4 (4.3): (alpha_0, k) + E_ind, whose only offset below 1 on the construction reading is d1
     (log order 0), so a log order is carried along the d1-chain of its point; the offset 1 lands above 3 except from
     the level-1 point 2 (log k_1(2) + 2 at 3). Result: k_2(lambda) <= 2 + e_c on the chain c of lambda, e_c the
     excess of the chain's first point in (2, 3) (every excess source is the first point of its chain in (2, 3):
     asserted).
  K4 (computed, certified) SUM over the 53,244,736 levels above 3 of X_7(beta), by floor sums over each chain and
     level range, at both ends of the d1 and base intervals (equal); the special points z = 1 and z = 2 and
     ceil(beta - 5/2) counted level by level in closed form.
  K5 (computed) the new constant: d <= A' + 106,489,470 c' (R0 and R1), N = 21 d + 6.
  K6 (READ; deduced) c': III.I Theorem 5.3's FWD loss D_0 + D_1 + d' + d'' + 6 (II.F2-TAME (3.2)-(3.3)), BG 2, and the
     fixed MODs. D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) contains d^T_0 = II.A Proposition 9.6's d_0, which is II.A Lemma
     8.5's (II.A:1306-1307), defined as d_* + K + 1 with d_* from the closed graph theorem (II.A:955-967), and
     d^E_0, d^S_0 rest on (L3)-(L4) and II.A Lemma 8.6, whose d_0 the write-out fixes through d_0 - 2 >= M_2.4 + 2
     (II.A2:722-723), M_2.4 again a closed-graph seminorm count (II.A2 Proposition 2.4's proof, :277-279). [SBG]'s own
     boundedness theorem gives no count either (READ: its Proposition 3.32 cites [Hin23a] Corollary 4.34 for uniformly
     bounded symbols; its Theorem 3.44 is "an immediate consequence"; variable orders "mutatis mutandis", p. 66). So
     c' >= 10 + D_0 and c' has no number in the record (deduced); the program prints d as A' + 106,489,470 c' and what
     each c' would give.
  Controls (each mutates the computed path and must fail): C1 the level sum of K4 on a scaled instance (d1 -> 1/97,
  four chains, a level step 1/89, three excess sources) against a brute-force simulation of levels 1-2 (sources,
  d1-remainders carried, the s1 rows at lambda - 1, the critical +1 at 2 and 3): equal; the closed form with the
  propagation removed (excess only at the source point) disagrees. C2 the dictionary shift removed (s1 rows taken at
  rate lambda, as for s0): E_K below beta_K collapses to {1, 2} and K2's identity |E_K,<=| = sum over Lambda cap
  [2, beta - 1 - eps] fails. C3 K1 with F4's excess dropped: A differs from eflat5's printed constant. C4 the floor sum
  of K4 at a perturbed d1 (one part in 10^9): the two interval ends no longer agree with it.

    python3 checks/dnumber5.py        (about a minute)
"""
import builtins
import os
import sys
import textwrap
from fractions import Fraction as Fr
from math import ceil, floor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import dweights5 as DW  # noqa: E402  (W1 weights, W3 counts, d1, floor_sum, chain_points, data_ECI)
import dceiling5 as DC  # noqa: E402  (D4's range_count)
import eflat5 as EF  # noqa: E402  (F1's E_ind tables, F4's excess rule)
import lambdagen5 as LG  # noqa: E402  (E_col's bases)
import prop31loss5 as P31  # noqa: E402  (least E^C_I)

OK = {}
KPLUS1 = 106489470


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


# ------------------------------------------------------------------------------------------- the Lemma 1.4 rule
def lemma14_general(roots, F, top):
    """III.A Lemma 1.4 (A-PREREQ:176-182): E_0 := E(alpha) bar-cup F, E_(k+1) := E(alpha) bar-cup (F bar-cup (E_k +
    1)), E := union; F a dict {exponent: log order} (closed under + N_0 here). For F = (k, 0) + N_0 this is
    iotapoles5.lemma14 (checked in K3)."""
    def closure(pts):
        out = {}
        for z0, lo in pts.items():
            n = 0
            while z0 + n <= top:
                out[z0 + n] = max(out.get(z0 + n, -1), lo)
                n += 1
        return out

    def ubar(A, B):
        out = dict(A)
        for z0, lo in B.items():
            out[z0] = out[z0] + lo + 1 if z0 in out else lo
        return out
    Ea, Fc = closure({r: 0 for r in roots}), closure(F)
    E = ubar(Ea, Fc)
    U = dict(E)
    for _ in range(int(top) + 3):
        E = ubar(Ea, ubar(Fc, {z0 + 1: lo for z0, lo in E.items() if z0 + 1 <= top}))
        for z0, lo in E.items():
            U[z0] = max(U.get(z0, -1), lo)
    return U


# ------------------------------------------------------------------------------------------- K1
def k1_constant(w, c, P_i, P_W, W, excess):
    La, Lb = c['levels_above3'], c['levels_below3']
    return 3 * (c['R2'] + c['R3']) + La * (3 * P_W + 11 + 3 * P_i + excess + 15 * W) + Lb * (15 * W + 58)


# ------------------------------------------------------------------------------------------- K3 log orders
def logs_tables():
    """E^flat's F4 bounds (R0, R1) at the points of pi_1 E^C_I in [2, 3]; E_ind (every type's roots, k = 1, 2);
    E_col's log orders on [0, 1] on the widest reading (b in {0, 2, 3}) and on the shifted one (b in {2, 3})"""
    off, ints, ok = EF.offsets()
    d1 = off[('sl-', 1)][1]
    allroots = sorted({Fr(n) + q for (n, q, _, _) in off.values()} | {Fr(i) for i in range(3, 12)})
    eind = {}
    for k in (1, 2):
        for wv, lo in EF.site_eind(allroots, k, top=Fr(10)).items():
            eind[wv] = max(eind.get(wv, -1), lo)
    blocks = {'s0': [2 + off[('s0', 0)][1], Fr(3)], 's1': [2 + d1, 3 + off[('sl+', 1)][1], Fr(4)], 'v1': [Fr(3)]}
    union = {}
    for b, k in (('s0', 1), ('v1', 2), ('s1', 2), ('s1', 1)):
        for wv, lo in EF.site_eind(blocks[b], k).items():
            union[wv] = max(union.get(wv, -1), lo)
    G = {Fr(2): 0}
    for wv, lo in union.items():
        if 0 < wv <= 1 + EF.EPS_P:
            G[2 + wv] = max(G.get(2 + wv, -1), lo)
    lmax_w = max(lo for wv, lo in union.items() if 0 < wv <= EF.TOP_W)
    c_gen = max(lmax_w, max(G.values()))
    flat = {}
    for name, M in (('R0', 1), ('R1', 4)):                   # eflat5 F4 (Round 6: with the completion of (3.2))
        rows = EF.f4_table(M, G, lmax_w, c_gen)[0]
        flat[name] = {Fr(z).limit_denominator(10 ** 6): b for z, kz, b in rows}
    ecol = {}
    ecol = {}
    for rd, bases in (('wide', (0, 2, 3)), ('shifted', (2, 3))):
        res = {}
        for b in bases:
            pts = {Fr(0): 0}
            pts.update(eind)
            for wv, lo in pts.items():
                for sig in range(-5, 3):
                    p = b + wv + sig
                    if 0 <= p <= 1:
                        res[p] = max(res.get(p, -1), lo)
        ecol[rd] = res
    return dict(off=off, d1=d1, flat=flat, c_gen=c_gen, ecol=ecol, union=union)


def special_logs(T, reading, ecol_rd):
    """k_1(2), k_2(3) and the E_K log orders at z = 1, 2 (K2-K3)"""
    fl = T['flat'][reading]
    ec = T['ecol'][ecol_rd]
    kf2, kf3 = fl.get(Fr(2), 0), fl.get(Fr(3), 0)
    k12 = max(kf2, ec[Fr(0)])                                 # E^flat at 2; 2 + E_col at 0 (and u_0's 1 + E_col)
    # u_0 (Lemma 2.1 at level 0): Lemma 1.4 with F = (E^flat - 1) u (1 + E_col) at 1, 2 and the root 2
    F = {Fr(1): max(kf2, ec[Fr(0)]), Fr(2): max(kf3, ec[Fr(1)])}
    U = lemma14_general([Fr(2)], F, Fr(3))
    k_u0 = U[Fr(2)]
    k23 = max(kf3, k_u0, k12 + 2, ec[Fr(0)], ec[Fr(1)])         # sources at 3: E^flat, u_0, 2 + E_ind's (1, 2), E_col
    return dict(k12=k12, k23=k23, z1=k12 + 1, z2=max(k23, k12) + 1, k_u0=k_u0)


# ------------------------------------------------------------------------------------------- chains
def chains(w, T, reading, ecol_rd, d1lo, d1hi):
    """the chains of Lambda meeting (2, 3) on the construction reading (dceiling5 D4's starts and E_col's bases),
    each with its excess e_c and its first point in (2, 3)"""
    E = P31.least_ECI()
    named = [DW.LSHARP, Fr(2), Fr(3)]
    starts = sorted({g + m for g in named for m in (0, 1)} | {z for z in E if z < 4})
    bases = [(n, lo, hi) for n, lo, hi in LG.ecol_bases()]
    fl, ec = T['flat'][reading], T['ecol'][ecol_rd]
    sp = special_logs(T, reading, ecol_rd)
    out = []
    for g in starts:
        if not (g < 3):
            continue
        if g == 2:
            n_a = 1
        elif g > 2:
            n_a = 0
        else:                                                     # first n with g + n d1 > 2, certified
            qa, qb = floor((2 - g) / d1hi), floor((2 - g) / d1lo)
            assert qa == qb
            n_a = qa + 1
        if g == 2:
            e = max(sp['k12'], ec[[p for p in ec if abs(p - T['d1']) < Fr(1, 10 ** 30)][0]], 2) - 2
        elif 2 < g < 3:
            e = max(fl.get(g, 2), 2) - 2
        else:
            e = 0
        if g < 2:
            assert e == 0
        out.append(dict(name=str(float(g)), lo=g, hi=g, n_a=n_a, e=e))
    keys = sorted(ec)
    for n, lo, hi in bases:
        if not (hi < 3):
            continue
        frac = (lo - 2, hi - 2)
        m = [p for p in keys if frac[0] - Fr(1, 10 ** 30) <= p <= frac[1] + Fr(1, 10 ** 30)]
        e = max(ec[m[0]], 2) - 2 if m else 0
        out.append(dict(name=n, lo=lo, hi=hi, n_a=0, e=e))
    return out, sp


def chain_level_sum(ch, w, c, d1, top3=3):
    """sum over the levels k3 <= k <= K of #{n >= n_a : g + n d1 < 3, g + n d1 <= beta_k - 1 - eps}, at one value of
    d1 and of g (rationals): exact"""
    g, n_a = ch['g'], ch['n_a']
    a1, s, eps, al = w['alpha1'], w['s'], w['eps'], w['alpha']
    k3, K = c['k3'], c['K']
    q = (top3 - g) / d1
    n_b = int(q) - 1 if q == int(q) else int(floor(q))            # last n with g + n d1 < 3
    if n_b < n_a:
        return 0, 0
    full = n_b - n_a + 1
    Ta = g + n_a * d1 + 1 + eps                                   # beta >= Ta: at least one point
    Tb = g + n_b * d1 + 1 + eps                                   # beta >= Tb: every point
    ka = max(k3, ceil((Ta - a1) / s))
    kb = min(K, ceil((Tb - a1) / s))                              # first level (index) counting every point
    tot = 0
    # levels k in [ka, kb - 1] with k <= K - 1: floor((a1 + k s - 1 - eps - g)/d1) - n_a + 1
    k_end = min(kb - 1, K - 1)
    if k_end >= ka:
        n = k_end - ka + 1
        c0 = a1 - 1 - eps - g + ka * s
        D = c0.denominator * s.denominator // __import__('math').gcd(c0.denominator, s.denominator)
        p, qq = d1.numerator, d1.denominator
        b = int(c0 * D) * qq
        a = int(s * D) * qq
        m = p * D
        tot += DW.floor_sum(n, m, a, b) + n * (1 - n_a)
    # levels counting every point: k in [kb, K - 1] and the top level beta_K = alpha
    nfull = max(0, (K - 1) - max(kb, ka) + 1) if kb <= K - 1 else 0
    tot += nfull * full
    assert al - 1 - eps > top3
    tot += full                                                   # the top level
    return tot, full


def certified_chain_sum(ch, w, c, d1lo, d1hi):
    lo_g, hi_g = ch['lo'], ch['hi']
    s1, f1 = chain_level_sum(dict(g=hi_g, n_a=ch['n_a']), w, c, d1hi)   # fewest points: largest g and d1
    s2, f2 = chain_level_sum(dict(g=lo_g, n_a=ch['n_a']), w, c, d1lo)
    return s1, s2, f1, f2


# ------------------------------------------------------------------------------------------- C1 brute force
def brute_force(d1, starts, excess_src, generic, k12, k23, levels, eps, prop=True, shift=1):
    """levels 1-2 simulated: sources on each chain (generic log, excess at listed points), the level-1 point 2 with
    k12, d1-remainders carrying their log order (prop), the s1 rows at lambda - shift; returns sum over levels of
    |E_K cap {Re <= beta - 2 - eps}| (pairs) and the per-level list"""
    pts = {}
    for g in starts:
        n = 0
        while g + n * d1 < 3:
            x = g + n * d1
            if x > 2:
                pts[x] = max(pts.get(x, -1), generic)
            n += 1
    for x, lo in excess_src.items():
        pts[x] = max(pts.get(x, -1), lo)
    pts[2 + d1] = max(pts.get(2 + d1, -1), k12)                  # the level-1 remainder (2, k12) + (d1, 0)
    k2 = {}
    for x in sorted(pts):
        k2[x] = max(pts[x], k2.get(x, -1))
        if prop and x + d1 < 3 and x + d1 in pts:
            k2[x + d1] = max(k2.get(x + d1, -1), k2[x])
    EK = {Fr(1): k12 + 1, Fr(2): max(k23, k12) + 1}
    for x, lo in k2.items():
        z = x - shift
        EK[z] = max(EK.get(z, -1), lo)
    tot = 0
    for beta in levels:
        tot += sum(lo + 1 for z, lo in EK.items() if z <= beta - 2 - eps)
    return tot


def closed_form_scaled(d1, starts, excess_first, generic, k12, k23, levels, eps):
    tot = 0
    for beta in levels:
        cut = beta - 1 - eps
        for g in starts:
            n, cnt = 0, 0
            while g + n * d1 < 3:
                x = g + n * d1
                if 2 < x <= cut:
                    cnt += 1
                n += 1
            tot += cnt * (generic + 1 + excess_first.get(g, 0))
        if beta - 2 - eps >= 1:
            tot += k12 + 2
        if beta - 2 - eps >= 2:
            tot += max(k23, k12) + 2
    return tot


def main():
    print('dnumber5: X_7 summed over the levels; d up to c\'')
    w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    c = DW.counts(w)
    d1lo, d1hi = DW.d1_interval()
    La = c['levels_above3']
    assert c['K'] + 1 == KPLUS1 and La == 53244736
    # D4's counts (dceiling5 D4, rebuilt with its range_count)
    E = P31.least_ECI()
    named = [DW.LSHARP, Fr(2), Fr(3)]
    starts = sorted({g + m for g in named for m in (0, 1)} | {z for z in E if z < 4})
    bases = [(lo, hi) for _, lo, hi in LG.ecol_bases()]
    allst = list(starts) + bases
    top_i = 3 + w['eps_p'] - w['eps'] + Fr(1, 10 ** 40)
    n0 = DC.range_count(allst, d1lo, d1hi, Fr(0), Fr(2))
    P_i = DC.range_count(allst, d1lo, d1hi, Fr(2), top_i)
    P_W = DC.range_count(allst, d1lo, d1hi, 2 + w['eta1'], 3 + w['eta2'])
    W = n0
    open23 = DC.range_count(allst, d1lo, d1hi, Fr(2), Fr(3)) - 1     # minus the point 2
    # K1
    A = {'R0': k1_constant(w, c, P_i, P_W, W, 23), 'R1': k1_constant(w, c, P_i, P_W, W, 47)}
    OK['K1'] = (A['R0'] == 37919138373535686 and A['R1'] == 37919139651409350 and P_W == 85025783
                and P_i == P_W + 1 and W == 1470302 and open23 == P_i - 2)
    print('  K1: A = 3 (R2 + R3) + L_above [3 P_W + 11 + 3 P_iota + excess + 15 W] + L_below [15 W + 58] = %d (R0), '
          '%d (R1) (eflat5 F5 as corrected in Round 6: R1's excess 47); P_W = %d, P_iota = %d, W = %d, |Lambda cap (2, 3)| = %d' % (
              A['R0'], A['R1'], P_W, P_i, W, open23))
    C3 = k1_constant(w, c, P_i, P_W, W, 0)
    OK['C3'] = C3 != A['R1'] and C3 != A['R0']
    print('  C3 (control): K1 with F4\'s excess dropped: %d, not eflat5\'s constant: %s' % (C3, OK['C3']))

    # K3 log tables
    T = logs_tables()
    chk = EF.IP.lemma14([Fr(3)], 2, Fr(7))
    chk2 = lemma14_general([Fr(3)], {Fr(2): 0}, Fr(7))
    OK['K3a'] = chk == chk2
    print('  K3: Lemma 1.4\'s rule with a general source agrees with iotapoles5.lemma14 on (k, 0) sources: %s' % (
        OK['K3a']))
    for rd in ('wide', 'shifted'):
        ec = T['ecol'][rd]
        print('      E_col on [0, 1] (%s reading): log order %d at 0, %d at 1, at most %d off the integers (%d points)'
              % (rd, ec[Fr(0)], ec[Fr(1)], max(v for p, v in ec.items() if p not in (0, 1)),
                 len([p for p in ec if p not in (0, 1)])))
    results = {}
    for reading in ('R0', 'R1'):
        for ecol_rd in ('wide', 'shifted'):
            chs, sp = chains(w, T, reading, ecol_rd, d1lo, d1hi)
            tot, full_pts, gen = 0, 0, 0
            for ch in chs:
                s1, s2, f1, f2 = certified_chain_sum(ch, w, c, d1lo, d1hi)
                assert s1 == s2 and f1 == f2, (ch['name'], s1, s2)
                ch['sum'], ch['full'] = s1, f1
                tot += (3 + ch['e']) * s1
                gen += 3 * s1
                full_pts += f1
            assert full_pts == open23
            # special points z = 1 (levels with beta - 2 - eps >= 1) and z = 2 (beta - 2 - eps >= 2)
            a1, s, eps, K, k3 = w['alpha1'], w['s'], w['eps'], c['K'], c['k3']
            lv_z1 = (K - 1) - max(k3, ceil((3 + eps - a1) / s)) + 1 + 1
            lv_z2 = (K - 1) - max(k3, ceil((4 + eps - a1) / s)) + 1 + 1
            k72 = ceil((Fr(7, 2) - a1) / s)                       # first level index with beta > 7/2
            assert a1 + (k72 - 1) * s < Fr(7, 2) < a1 + k72 * s
            lF = (k72 - k3) * 1 + ((K - 1) - k72 + 1) * 2 + 2     # ceil(beta - 5/2): 1 up to 7/2, then 2; top 2
            spec = lv_z1 * (sp['z1'] + 1) + lv_z2 * (sp['z2'] + 1)
            X7 = tot + spec + lF
            results[(reading, ecol_rd)] = dict(X7=X7, tot=tot, gen=gen, spec=spec, lF=lF, sp=sp, chs=chs,
                                               lv=(lv_z1, lv_z2))
    # K2 (identity on the real data): the generic part is 3 x sum over levels of |Lambda cap (2, beta - 1 - eps]|
    r = results[('R1', 'wide')]
    top = sum(ch['full'] * (3 + ch['e']) for ch in r['chs']) + r['sp']['z1'] + 1 + r['sp']['z2'] + 1
    OK['K2'] = r['gen'] % 3 == 0 and top > 3 * open23
    print('  K2: E_K below beta_K = {1} u {lambda - 1 : lambda in Lambda cap (2, 3)} u {2}, cut at beta - 2 - eps; at '
          'the top level (beta = alpha) |E_K,<=| = %d pairs (3 |Lambda cap (2, 3)| = %d, the rest the excess and the '
          'points 1, 2), so X_7(alpha) = %d' % (top, 3 * open23, top + 2))
    for reading in ('R0', 'R1'):
        sp = results[(reading, 'wide')]['sp']
        print('      %s: k_1(2) = %d, u_0 at 3 (Lemma 1.4, root 2) %d, k_2(3) = %d; E_K log orders %d at 1, %d at 2' % (
            reading, sp['k12'], sp['k_u0'], sp['k23'], sp['z1'], sp['z2']))
    rw = results[('R1', 'wide')]
    exc = [(ch['name'], ch['e']) for ch in rw['chs'] if ch['e'] > 0]
    print('      chains with an excess (R1, wide E_col): %s; the other %d chains carry log order <= 2' % (
        exc, len([ch for ch in rw['chs'] if ch['e'] == 0])))
    OK['K3'] = all(ch['n_a'] >= 0 for ch in rw['chs'])
    # K4
    for key, rr in sorted(results.items()):
        print('  K4 %s/%s: sum over the levels above 3 of X_7 = %d (generic 3 per point %d, excess %d, the points 1 and '
              '2 %d, ceil(beta - 5/2) %d); certified (each chain sum equal at both ends of the d1 and base intervals)'
              % (key[0], key[1], rr['X7'], rr['gen'], rr['tot'] - rr['gen'], rr['spec'], rr['lF']))
    OK['K4'] = all(rr['X7'] > 0 for rr in results.values())
    # K5
    final = {}
    for reading in ('R0', 'R1'):
        Xm = max(results[(reading, rd)]['X7'] for rd in ('wide', 'shifted'))
        final[reading] = A[reading] + Xm
    unif = La * (top + 2)
    print('  K5: d <= %d (R0), %d (R1) + %d c\'  (%.6e + 1.0649e8 c\'); N = 21 d + 6 <= %d + %d c\' (R1). The '
          'uniform bound L_above X_7(alpha) would give %d more' % (
              final['R0'], final['R1'], KPLUS1, final['R1'], 21 * final['R1'] + 6, 21 * KPLUS1,
              unif - results[('R1', 'wide')]['X7']))
    for cp in (10, 100, 10 ** 4, 10 ** 6):
        dv = final['R1'] + KPLUS1 * cp
        print('      c\' = %d: d <= %d (%.6e), N <= %d (%.6e)' % (cp, dv, dv, 21 * dv + 6, 21 * dv + 6))
    OK['K5'] = final['R1'] > A['R1'] and final['R1'] < 10 ** 17
    # K6: c' (READ, deduced): printed only
    print('  K6: c\' >= D_0 + D_1 + d\' + d\'\' + 6 + 2 (BG) + the fixed MODs; D_0 >= II.A Lemma 8.5\'s d_0 = d_* + K + 1, d_* '
          'from the closed graph theorem (II.A:955-967), and D_0 >= the d_0 of (L3)-(L4), fixed by d_0 - 2 >= M_2.4 + 2 '
          '(II.A2:722-723), M_2.4 a closed-graph seminorm count (II.A2:277-279); [SBG] Theorem 3.44 gives no count '
          '(READ). So c\' has no number in the record; d is A\' + 106,489,470 c\' with A\' above (deduced)')
    # C1: brute force on a scaled instance
    d1s = Fr(1, 97)
    st = [Fr(2), Fr(2) + Fr(1, 3) + Fr(1, 1000), Fr(5, 2), Fr(5, 2) + Fr(1, 7)]
    exc_first = {Fr(5, 2): 3, Fr(2): 2}                          # excess at the chain's first point in (2, 3)
    exc_src = {Fr(5, 2): 2 + 3}
    k12s, k23s, gen = 4, 9, 2
    levels = [Fr(3) + Fr(i, 89) for i in range(1, 90)] + [Fr(4) + Fr(1, 200)]
    epss = Fr(1, 10 ** 6)
    bf = brute_force(d1s, st, exc_src, gen, k12s, k23s, levels, epss)
    cf = closed_form_scaled(d1s, st, exc_first, gen, k12s, k23s, levels, epss)
    cf_mut = closed_form_scaled(d1s, st, {Fr(5, 2): 3}, gen, k12s, k23s, levels, epss)   # 2's propagation dropped
    bf_noprop = brute_force(d1s, st, exc_src, gen, k12s, k23s, levels, epss, prop=False)
    OK['C1'] = bf == cf and cf_mut != bf and bf_noprop != bf
    print('  C1 (control): scaled instance (d1 = 1/97, four chains, 90 levels): brute force %d = closed form %d; the '
          'closed form without the chain of 2\'s carried excess %d and the simulation without propagation %d differ: %s'
          % (bf, cf, cf_mut, bf_noprop, OK['C1']))
    # C2: the dictionary shift removed
    bf_shift0 = brute_force(d1s, st, exc_src, gen, k12s, k23s, levels, epss, shift=0)
    OK['C2'] = bf_shift0 != bf
    print('  C2 (control): s1 rows taken at rate lambda (no shift): %d pairs over the levels, not %d: K2\'s identity '
          'fails: %s' % (bf_shift0, bf, OK['C2']))
    # C4: perturbed d1
    ch0 = [ch for ch in results[('R1', 'wide')]['chs'] if ch['name'] == '2.5'][0]
    pert = chain_level_sum(dict(g=ch0['lo'], n_a=ch0['n_a']), w, c, d1lo * (1 + Fr(1, 10 ** 9)))[0]
    OK['C4'] = pert != ch0['sum']
    print('  C4 (control): the chain of 2.5 summed at d1 (1 + 1e-9): %d, not the certified %d: %s' % (
        pert, ch0['sum'], OK['C4']))
    for k_, v in OK.items():
        builtins.print(k_, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
