#!/usr/bin/env python3
"""sooterm.py -- RULING 1: THE TWO-BODY SPIN-ORBIT TERM. STEP ONE, AND IT IS THE STEP THAT CAN BE PROVED.

  M's ruling of 6 September 2026, on FINDING-R4-21's question: "1 - build it."  The named candidate for the
  d-row half of the spin-orbit residual is the two-body spin-other-orbit interaction, which no form in this
  corpus contains -- `RESULT-S94-ITEM3-JSEL.md` says so in its own words: "First-order zeta on an SR orbital; no
  self-consistent Dirac field; no occupancy-dependent splitting; NO BREIT."

  THE OPERATOR (Breit-Pauli, atomic units, alpha = 1/c; the Breit part as Hoshino 2023 arXiv:2311.05294 Eqs. 6-7
  states it, and Bethe-Salpeter 1977 / Itoh Rev. Mod. Phys. 37 (1965) 159 behind that):

      H = (alpha^2/2) SUM_i (Z/r_i^3) l_i.s_i
        - (alpha^2/2) SUM_{i!=j} [ (r_i - r_j) x p_i ] . ( s_i + 2 s_j ) / r_ij^3

  The s_i piece is the two-body spin-OWN-orbit (the screening of the nuclear term); the 2 s_j piece is the
  spin-OTHER-orbit.  The relative weight is 1 : 2 and it is not adjustable.

  WHAT IS DERIVED HERE BEFORE ANY CODE, and it decides the shape of the whole build:

  (1) FOR A CLOSED CORE THE SPIN-OTHER-ORBIT HAS NO DIRECT PART.  Its Hartree average needs either SUM_j <s_j>
      over the core, which is zero for a closed shell, or the core's net orbital current, which is also zero.
      **So the entire spin-other-orbit effect is an EXCHANGE effect.**  That is exactly why no local potential
      can carry it, and it is why so94.py's own declaration -- "the nonlocal HF exchange has no dV/dr; zeta is
      taken on the LOCAL potential" -- names a real absence rather than a convenience.

  (2) THE DIRECT PART OF THE SPIN-OWN-ORBIT IS THE SCREENING ALREADY IN so94, AND IT EQUALS ONE MARVIN INTEGRAL.
      For a spherical core shell b holding N_b electrons, with P_b normalised to 1,

          V_b(r) = N_b [ (1/r) INT_0^r P_b^2 dr2 + INT_r^inf P_b^2 / r2 dr2 ]
          =>  dV_b/dr = -N_b (1/r^2) INT_0^r P_b^2 dr2
          =>  (1/r) dV_b/dr = -N_b (1/r^3) INT_0^r P_b^2(r2) dr2

      so  (alpha^2/2) <a| (1/r) dV_b/dr |a>  =  -(alpha^2/2) N_b M^0(ab)  EXACTLY, where

          M^k(ab) = INT dr1 P_a^2(r1) r1^-(k+3) INT_0^{r1} dr2 P_b^2(r2) r2^k          [Marvin]

      **This fixes the Marvin convention with no appeal to memory, and it is a gate**: the radial machinery below
      must reproduce so94's screening from the M^0 side.  MEASURED, it does, to 1.5e-5 relative at all six
      anchored openings -- and getting there found a real thing.  A plain cumulative sum for the inner integral
      is off by a CONSTANT 0.3 % on every row; the chain's own Yk (t7b_hf.py:30) quadratures it as
      `np.cumsum(w) - 0.5*w`, and matching that convention -- read from its source, not guessed -- closes the
      gap by a factor of 250.  It is the strongest check available for the direct channel and it is --verify.

  A DISCREPANCY BETWEEN TWO STATEMENTS OF THE MEAN-FIELD EQUATION, CAUGHT BY A CONSISTENCY TEST AND RESOLVED.
  arXiv:2404.04716 Eq. (15) as extracted reads

      F^{BP,xi}_pq = h^xi_pq + SUM_rs P_rs [ g^xi_pqrs - (3/2) g^xi_sqpr + (3/2) g^xi_spqr ]

  with the two exchange terms at OPPOSITE signs.  Read literally with that paper's own index convention
  (g_pqrs = <phi_p(1) phi_r(2)| g |phi_q(1) phi_s(2)>, its Eq. 17), those two terms become IDENTICAL when p = q
  -- and p = q is exactly the diagonal element that carries zeta, since F^z_{a m, a m} = zeta_a m by
  Wigner-Eckart.  So the exchange contribution to zeta would cancel identically, which cannot be right: it is
  the whole of what Blume-Watson exists to compute.  **The form was refused on that test, not adopted.**

  The ORCA 6.1 manual states the same object independently, and it does not cancel:

      h^SOC_pq = (p| h^1e |q) + SUM_rs P_rs [ (pq| g |rs) - (3/2)(pr| g |sq) - (3/2)(sq| g |pr) ]

  BOTH exchange terms at -3/2, and their index patterns are genuinely different -- electron 1 carries the
  a -> b transition in one and electron 2 in the other, and the operator acts on electron 1 only, so the two
  are not the same integral.  At p = q they do not coincide and the diagonal survives.  ORCA's own sentence
  for what they are: "The exchange term has contributions from both the spin-own-orbit and spin-other-orbit
  interaction."  **This is the form carried here**, and the discrepancy with the extracted equation is
  recorded rather than smoothed: it is either a sign convention this reconstruction does not share or an
  extraction fault, and nothing here depends on deciding which.

  THE COEFFICIENT ITSELF IS CROSS-CHECKED THREE WAYS: it is 3/2 in both statements above, and 3/2 = 1 + 2 x (1/2)
  is exactly the spin-own-orbit-to-spin-other-orbit weight the Breit-Pauli operator at the top of this docstring
  fixes independently.  Two literature statements and one derivation agree on it.

  The operator definitions are Kotaru, Pokhilko and Sokolov's (their Eqs. 16-20)

      h^xi(i)      = SUM_A Z_A [ r_iA x p(i) ]_xi / r_iA^3                 the nuclear term
      g^xi,sso(i,j) = - [ r_ji x p(i) ]_xi / r_ij^3                        the two-electron spin-SAME-orbit
      h^xi_pq      = -i <phi_p(1)| h^xi(1) |phi_q(1)>
      g^xi_pqrs    = -i <phi_p(1) phi_r(2)| g^xi,sso(1,2) |phi_q(1) phi_s(2)>
      H_SO         = i (alpha^2/4) SUM_xi SUM_pq F^xi_pq D^xi_pq

  and their own sentence for why the exchange coefficient is 3/2 and not 1: **"The two-electron term of F^{BP,xi}_pq
  in Eq. (15) also contains contributions from the spin-other orbit operator, which matrix elements can be fully
  expressed in terms of g^xi_pqrs."**  The 3/2 is 1 + 2 x (1/2): the spin-own-orbit at weight 1 and the
  spin-other-orbit at weight 2, exactly the ratio the Breit-Pauli operator at the top of this docstring fixes.

  So the COULOMB coefficient is +1 -- and that is the term §(2) above proves equals -N_b M^0(ab), which is the
  anchor the exchange channel is built against.

  WHAT REMAINS IS THE ANGULAR REDUCTION, AND ITS FIRST STEP IS TAKEN AND SELF-CONSISTENT.  Write the two-electron
  operator with F = 1/r_12 and split the gradient into its radial and angular parts, using r-hat x grad =
  (i/r) L-hat:

      g^xi(1,2) = -[ grad_1 F x p_1 ]_xi
                = i [ (dF/dr_1) (i/r_1) L_1  +  (1/r_1) ( grad_Omega1 F  x  grad_1 ) ]_xi

  TWO THINGS FOLLOW, AND THE FIRST IS A CLOSED LOOP ON WHAT IS ALREADY PROVED:

    (i) In the DIRECT term, F's angular dependence averages over the closed shell and the second piece vanishes,
        leaving (dV/dr)(1/r) L -- which is exactly the screening §(2) derives and --verify measures to 1.5e-5.
        **The decomposition reproduces the proved anchor**, so it is the right decomposition.

   (ii) In the EXCHANGE term the first piece carries <l_b m_b| L_xi |l_a m_a>, which VANISHES UNLESS l_b = l_a.
        So for a core shell of different l, only the angular-gradient piece contributes; for a core shell of the
        SAME l as the entrant -- 2p under Al's 3p, 3d and 4d under La's 5d -- both do.  That is a structural
        prediction of the reduction, and it is testable before any number is read.

  What is still owed is the angular-gradient piece's reduction into 3j weights on N^k(ab).  The operator and its
  coefficients are no longer the open piece; this one step is.  §THE EXCHANGE CHANNEL below states it with its
  gates.

  usage:  python3 sooterm.py --verify     the direct-channel identity at every core shell of the six openings
          python3 sooterm.py --selftest
          python3 sooterm.py             the report

  numpy; the chain is loaded by path exactly as fieldentry.py loads it.
"""
import argparse, importlib.util, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RECOVERED = os.path.join(ROOT, "recovered")
OUT_JSON = os.path.join(HERE, "sooterm.json")
HA_CM = 219474.6313705


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# ================================================================== the Marvin radial integrals
def _cumin(np, f, dr):
    """Cumulative INT_0^{r_j} f dr IN THE CHAIN'S OWN CONVENTION, read from t7b_hf.Yk (line 30):

        A = np.cumsum(w * r**k) - 0.5 * w * r**k          with w = Pa*Pb*dr

    i.e. a cumulative sum carrying a half-weight correction at the current node.  This is not a detail.  The
    identity in the docstring must hold against the potential the chain ITSELF builds with Yk, so the inner
    integral has to be quadratured the way Yk quadratures it; a plain cumsum differs by 0.5 f_j dr_j and shows
    up as a CONSTANT 0.3 % on every row -- measured, before this was matched."""
    w = f * dr
    return np.cumsum(w) - 0.5 * w


def marvin_M(np, P_a, P_b, r, dr, k):
    """M^k(ab) = INT dr1 P_a^2(r1) r1^-(k+3) INT_0^{r1} dr2 P_b^2(r2) r2^k.

    The inner integral is the cumulative one, taken on the same mesh and with the same weights the chain uses,
    so no interpolation enters.  Both P are normalised to INT P^2 dr = 1 by the caller."""
    inner = _cumin(np, P_b ** 2 * r ** k, dr)               # INT_0^{r1} P_b^2 r2^k dr2
    return float(np.sum(P_a ** 2 * r ** (-(k + 3)) * inner * dr))


def marvin_N(np, P_a, P_b, r, dr, k):
    """N^k(ab), the exchange-shaped partner: the same kernel over the OVERLAP density P_a P_b on both sides.
    Built here because it is the radial object the exchange channel needs; it is NOT used in any figure until
    that channel has its coefficients."""
    inner = _cumin(np, P_a * P_b * r ** k, dr)
    return float(np.sum(P_a * P_b * r ** (-(k + 3)) * inner * dr))


# ================================================================== --verify: the direct-channel identity
def cmd_verify(log=sys.stderr):
    """so94's screening, taken two ways: from the local potential's gradient (what fieldresidue does) and from
    the Marvin M^0 integrals shell by shell (the identity derived in the docstring).  They must agree."""
    import numpy as np
    fe = _load("fieldentry", os.path.join(HERE, "fieldentry.py"))
    fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
    ch = fe.Chain(log=log)
    rows = []
    try:
        H, T, C0 = ch.hfc2, ch.t5_scf, ch.C0
        H.CORR = False
        for lab in ("3p", "4p", "5p", "6p", "4d", "5d"):
            m = fr.MEAS[lab]; Z, n, l = m["Z"], m["n"], m["l"]
            occ = T.ground_occ(Z)
            print(f"  {lab} {m['el']} Z={Z} ...", file=log, flush=True)
            h = H.HFC(Z, occ, c=C0); h.run2()
            r, dr, P = h.r, h.dr, h.P
            a = (n, l)
            u = P[a] / np.sqrt(float(np.sum(P[a] ** 2 * dr)))
            keys = [(x, y) for x, y, q in occ]; Q = {(x, y): q for x, y, q in occ}
            # --- route 1: the electronic part of so94's Vloc, gradient taken as so94 takes it
            Y0 = {k2: h.Yk(P[k2], P[k2], 0) for k2 in keys}
            Vel = sum((Q[b] if b != a else Q[a] - 1.0) * Y0[b] / r for b in keys)
            z_grad = float(np.sum(u * u * np.gradient(Vel, r) / r * dr) / (2 * C0 * C0))
            # --- route 2: the Marvin M^0 sum, shell by shell, from the identity
            z_marv = 0.0; per = {}
            for b in keys:
                Nb = Q[b] if b != a else Q[a] - 1.0
                if abs(Nb) < 1e-14: continue
                Pb = P[b] / np.sqrt(float(np.sum(P[b] ** 2 * dr)))
                M0 = marvin_M(np, u, Pb, r, dr, 0)
                per[f"{b[0]}{'spdfg'[b[1]]}"] = -Nb * M0 / (2 * C0 * C0)
                z_marv += -Nb * M0
            z_marv /= (2 * C0 * C0)
            rel = abs(z_marv - z_grad) / abs(z_grad)
            rows.append(dict(lab=lab, el=m["el"], Z=Z, z_grad=z_grad, z_marv=z_marv, rel=rel, per=per))
            print(f"    gradient {z_grad*HA_CM:12.4f}   Marvin M^0 {z_marv*HA_CM:12.4f}   rel {rel:.2e}",
                  file=log, flush=True)
        json.dump(dict(rows=rows), open(OUT_JSON, "w"), indent=1)
        print(f"wrote {OUT_JSON}", file=log)
    finally:
        ch.close()
    return rows


# ================================================================== report
def report():
    print("=" * 108)
    print("sooterm.py -- RULING 1: THE TWO-BODY SPIN-ORBIT TERM, STEP ONE")
    print("=" * 108)
    print("""
  M: "1 - build it."  The object is the two-body spin-other-orbit interaction, which no form in this corpus
  contains and whose absence the record states outright (RESULT-S94-ITEM3-JSEL: "no Breit").

  TWO THINGS ARE DERIVED BEFORE ANY CODE, AND THEY DECIDE THE BUILD:

  (1) FOR A CLOSED CORE THE SPIN-OTHER-ORBIT HAS NO DIRECT PART.  Its Hartree average needs either the core's
      total spin, zero for a closed shell, or the core's net orbital current, also zero.  THE WHOLE EFFECT IS
      EXCHANGE.  That is why no local potential carries it, and it vindicates so94's own declaration that "the
      nonlocal HF exchange has no dV/dr".

  (2) THE DIRECT SPIN-OWN-ORBIT IS EXACTLY ONE MARVIN INTEGRAL PER CORE SHELL:

          (alpha^2/2) <a| (1/r) dV_b/dr |a>  =  -(alpha^2/2) N_b M^0(ab)

      derived from V_b's own form, with M^k(ab) = INT dr1 P_a^2 r1^-(k+3) INT_0^r1 dr2 P_b^2 r2^k.  This fixes
      the Marvin convention WITHOUT appealing to a remembered formula, and it is the gate below.
""")
    if os.path.exists(OUT_JSON):
        R = json.load(open(OUT_JSON))["rows"]
        print("  THE DIRECT CHANNEL, VERIFIED TWO WAYS (zeta from the core screening alone, cm-1)\n")
        print(f"  {'row':6} {'el':3} {'from dV/dr':>14} {'from Marvin M^0':>17} {'relative':>11}")
        for x in R:
            print(f"  {x['lab']:6} {x['el']:3} {x['z_grad']*HA_CM:14.4f} {x['z_marv']*HA_CM:17.4f} {x['rel']:11.2e}")
        print("\n  The two routes share no code: one differentiates the potential the SCF built, the other")
        print("  integrates each shell's density against the Marvin kernel.  Agreement is the proof that the")
        print("  radial machinery and the convention are right, and it is what the exchange channel will stand on.")
    else:
        print("  (run --verify for the direct-channel identity)")
    print("""
  THE EXCHANGE CHANNEL IS BUILT, GATED -- AND IT DOES NOT CLOSE THE SIX ROWS

  The angular reduction was derived rather than looked up: the multipole expansion of 1/r12, the gradient split
  of the docstring, and the three resulting angular integrals by Gauss-Legendre quadrature in cos(theta).  No
  remembered angular formula enters anywhere.

  WHAT IS PROVED ABOUT THE MACHINERY, and it is not the same as proving the answer:
    - Unsold's theorem holds to 3e-14, so a closed shell's k > 0 multipoles vanish as they must.  Getting there
      caught a real fault: converting a positive-order Legendre function to negative order BY HAND while also
      normalising with |m| double-applies the factor, and Unsold came out 0.6347 where it must be 0.8463.
    - THE COULOMB CHANNEL OF THE GENERAL REDUCTION REPRODUCES THE MARVIN M^0 SUM TO 5e-15 -- exact, at every
      core shell of every opening, s p and d alike.  That is an independent derivation meeting a numerical one.
    - zeta comes out INDEPENDENT OF m_a to 5e-15, which is what Wigner-Eckart requires and what a broken
      angular reduction would not give.

  AND WHAT IS NOT: the Coulomb anchor exercises only the k = 0, q = 0 path, so of the three angular terms it
  tests one.  rad2, rad3 and A3r are reached only by the exchange itself and by the m_a test.  **Stated because
  it bears on how much weight the result below can carry.**

  THE RESULT, measured (zeta in cm-1; "was" is nuclear + direct alone, which is what fieldresidue uses):

      row  el      nuc      dir   exchange     total   measured    ratio     was
      3p   Al     82.0    -14.1       -6.1      61.9       74.7    0.829    0.910
      4p   Ga    549.0    -45.6      -15.8     487.6      550.8    0.885    0.914
      5p   In   1484.8    -76.3      -26.0    1382.5     1475.1    0.937    0.955
      6p   Tl   5748.5   -165.7      -58.1    5524.7     5195.1    1.063    1.075
      4d   Y     366.8   -104.3      -18.2     244.2      212.1    1.151    1.237
      5d   La    713.7   -140.9      -22.9     550.0      421.3    1.306    1.360

  **GATE (d) FAILS.**  The two-electron term is negative on every row: it improves both d rows (1.237 -> 1.151,
  1.360 -> 1.306) and worsens all four p rows, leaving the spread where it was -- 0.83 to 1.31 against 0.91 to
  1.36.  It does not collapse the 1.5x spread, which is what the gate asked of it.

  THIS IS RECORDED, NOT TUNED.  Nothing here is adjusted to make the gate pass, and the two exchange terms are
  printed separately (they come out equal, which the sum over m_b makes expected rather than suspicious) so the
  next reader can see the parts.  The finding is consistent with FINDING-R4-21's: the residual is at least TWO
  faults of opposite sign, and this term addresses only the one that is negative at d.  What the p rows want is
  positive, and the two-electron spin-orbit does not supply it.

  Nothing is repaired in any volume.  Every figure is MEASURED by this instrument or RECORD-CARRIED with its
  quote.""")
    print("=" * 108)


# ================================================================== selftest
def selftest():
    ok = bad = 0
    def check(name, cond, extra=""):
        nonlocal ok, bad
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   [{extra}]" if extra else ""))
        ok, bad = ok + bool(cond), bad + (not cond)
    if importlib.util.find_spec("numpy") is None:
        print("  SKIP (numpy needed)"); return True
    import numpy as np
    # --- the Marvin integrals against a case with a closed form.  Take P_a^2 and P_b^2 both concentrated so that
    #     P_b lies entirely inside P_a: then M^0(ab) -> <a|1/r^3|a> exactly, because the inner integral is 1.
    r = np.exp(np.linspace(math.log(1e-6), math.log(60.0), 20000)); dr = np.gradient(r)
    Pb = np.exp(-((r - 0.02) / 0.004) ** 2); Pb /= math.sqrt(float(np.sum(Pb ** 2 * dr)))
    Pa = np.exp(-((r - 3.0) / 0.5) ** 2); Pa /= math.sqrt(float(np.sum(Pa ** 2 * dr)))
    M0 = marvin_M(np, Pa, Pb, r, dr, 0)
    r3 = float(np.sum(Pa ** 2 / r ** 3 * dr))
    check("M^0(ab) -> <a|1/r^3|a> when b lies entirely inside a (the inner integral saturates at 1)",
          abs(M0 / r3 - 1) < 1e-6, f"{M0:.8f} vs {r3:.8f}")
    # --- and the converse: b entirely OUTSIDE a gives zero
    Pc = np.exp(-((r - 40.0) / 2.0) ** 2); Pc /= math.sqrt(float(np.sum(Pc ** 2 * dr)))
    M0o = marvin_M(np, Pa, Pc, r, dr, 0)
    check("M^0(ab) -> 0 when b lies entirely outside a (no screening from outside)",
          abs(M0o) < 1e-9 * r3, f"{M0o:.3e} against <1/r^3> {r3:.4f}")
    check("N^k is symmetric in the overlap density it integrates",
          abs(marvin_N(np, Pa, Pb, r, dr, 0) - marvin_N(np, Pb, Pa, r, dr, 0)) < 1e-12)
    if not os.path.exists(OUT_JSON):
        print("  SKIP the direct-channel identity (run --verify)")
    else:
        R = json.load(open(OUT_JSON))["rows"]
        check("the direct-channel identity was verified at all six anchored openings", len(R) == 6, f"{len(R)} rows")
        worst = max(x["rel"] for x in R)
        check("so94's screening from dV/dr equals the Marvin M^0 sum at every one, to 1e-4 relative",
              worst < 1e-4, f"worst {worst:.2e}")
    # --- the angular machinery: Unsold's theorem, which a wrong negative-m normalisation breaks
    x, w = _gauss(np)
    worstU = 0.0
    for l in (1, 2, 3):
        for k in (0, 2, 4):
            tot = 0.0
            for mm in range(-l, l + 1):
                Pl, _ = _plm(np, l, mm, x); Pk, _ = _plm(np, k, 0, x)
                tot += _norm(l, mm) ** 2 * _norm(k, 0) * 2 * math.pi * float(np.sum(w * Pl * Pk * Pl))
            exp = (2 * l + 1) / math.sqrt(4 * math.pi) if k == 0 else 0.0
            worstU = max(worstU, abs(tot - exp))
    check("Unsold: sum_m |Y_lm|^2 is spherical, so the k > 0 multipoles of a closed shell vanish",
          worstU < 1e-12, f"worst {worstU:.1e}")
    ex = os.path.join(HERE, "sooterm-exchange.json")
    if not os.path.exists(ex):
        print("  SKIP the SOMF gates (run --exchange)")
    else:
        E = json.load(open(ex))["rows"]
        check("the SOMF run covers all six anchored openings", len(E) == 6, f"{len(E)} rows")
        w2 = max(x["m_indep"] for x in E)
        check("zeta is independent of m_a, as Wigner-Eckart requires (the angular reduction's own test)",
              w2 < 1e-12, f"worst {w2:.1e}")
        if os.path.exists(OUT_JSON):
            byl = {x["lab"]: x for x in json.load(open(OUT_JSON))["rows"]}
            worstD = 0.0
            for x in E:
                o = byl.get(x["lab"])
                if o: worstD = max(worstD, abs(x["z_dir"] / o["z_marv"] - 1))
            check("THE ANCHOR THROUGH THE GENERAL MACHINERY: the Coulomb channel of the two-electron reduction"
                  " equals the Marvin M^0 sum", worstD < 1e-6, f"worst {worstD:.1e}")
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--exchange", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if a.verify: cmd_verify(); return
    if a.exchange: cmd_exchange(); return
    report()



# ================================================================== the angular reduction, done numerically
# Everything below implements the reduction derived in the docstring, with NO remembered angular formula: the
# multipole expansion of 1/r12, the gradient split into radial and angular parts, and the three resulting
# angular integrals evaluated by Gauss-Legendre quadrature in cos(theta) -- exact for these integrands, which
# are polynomials in cos(theta) times powers of sin(theta).  The phi integral is done analytically by the
# selection it imposes, q = m_B - m_A = m_C - m_D.
#
#   T^z(A,B;C,D) = - SUM_k SUM_q (4pi/(2k+1)) G2 [ G1 (rad1 m_B + rad2 q) + rad3 A3r ]
#
#   G1  = INT Y*_A Y*_kq Y_B dOmega
#   G2  = INT Y*_C Y_kq  Y_D dOmega
#   A3r = -INT_-1^1 P_A x [ m_B P'_kq P_B + q P_kq P'_B ] dx   (times the same normalisations and 2 pi)
#   rad1 = INT P_A P_B R'_k / r dr,  rad2 = INT P_A R_k (P_B/r)' dr,  rad3 = INT P_A P_B R_k / r^2 dr
#
# with R_k(r) = INT P_C P_D f_k dr2 and R'_k analytic (the surface terms cancel identically):
#   R_k  = A_k/r^(k+1) + B_k r^k,   R'_k = -(k+1) A_k/r^(k+2) + k B_k r^(k-1)
# A_k = INT_0^r P_C P_D r2^k dr2 and B_k = INT_r^inf P_C P_D r2^-(k+1) dr2, both in the chain's own convention.

_GL = {}


def _gauss(np, n=200):
    if n not in _GL: _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]


def _plm(np, l, m, x):
    """P_l^m(x) with the Condon-Shortley phase, and its x-derivative, for SIGNED m -- scipy's lpmv takes a
    signed order directly, and the derivative recurrence (x^2-1) dP/dx = l x P_l^m - (l+m) P_{l-1}^m holds for
    signed m too.  Converting a positive-order P to negative order BY HAND while also normalising with |m| in
    _norm double-applies the factor: measured, that breaks Unsold's theorem (sum_m |Y_lm|^2 came out 0.6347
    where (2l+1)/sqrt(4pi) is 0.8463, and the k > 0 sums that must vanish did not)."""
    from scipy.special import lpmv
    if abs(m) > l: return np.zeros_like(x), np.zeros_like(x)
    P = lpmv(m, l, x)
    Pm1 = lpmv(m, l - 1, x) if l - 1 >= abs(m) else np.zeros_like(x)
    dP = (l * x * P - (l + m) * Pm1) / (x * x - 1.0)
    return P, dP


def _norm(l, m):
    """The spherical-harmonic normalisation for SIGNED m, matching _plm's signed order."""
    return math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - m) / math.factorial(l + m))


def _ang(np, lA, mA, k, q, lB, mB, n=200):
    """(G1, A3r) for one (k, q), by quadrature.  Returns 0 when the phi selection fails."""
    if mB - mA != q: return 0.0, 0.0
    if abs(q) > k: return 0.0, 0.0
    x, w = _gauss(np, n)
    PA, _ = _plm(np, lA, mA, x)
    PB, dPB = _plm(np, lB, mB, x)
    PK, dPK = _plm(np, k, q, x)
    N = _norm(lA, mA) * _norm(k, q) * _norm(lB, mB) * 2 * math.pi
    G1 = N * float(np.sum(w * PA * PK * PB))
    A3r = -N * float(np.sum(w * PA * x * (mB * dPK * PB + q * PK * dPB)))
    return G1, A3r


def _radials(np, PA, PB, PC, PD, r, dr, k):
    """rad1, rad2, rad3 and the R_k they use, in the chain's own quadrature convention."""
    wCD = PC * PD * dr
    Ak = np.cumsum(wCD * r ** k) - 0.5 * wCD * r ** k                  # INT_0^r P_C P_D r2^k
    Bk = np.cumsum((wCD / r ** (k + 1))[::-1])[::-1] - 0.5 * wCD / r ** (k + 1)
    Rk = Ak / r ** (k + 1) + Bk * r ** k
    dRk = -(k + 1) * Ak / r ** (k + 2) + k * Bk * r ** (k - 1)          # surface terms cancel
    rad1 = float(np.sum(PA * PB * dRk / r * dr))
    dPB_over_r = np.gradient(PB / r, r)
    rad2 = float(np.sum(PA * Rk * dPB_over_r * dr))
    rad3 = float(np.sum(PA * PB * Rk / r ** 2 * dr))
    return rad1, rad2, rad3


def T_z(np, A, B, C, D, P, r, dr, kmax=8):
    """T^z(A,B;C,D) = <phi_A(1) phi_C(2)| g^z(1,2) |phi_B(1) phi_D(2)>, in the units this module fixes by its
    own Coulomb anchor.  Each of A..D is (l, m, key) with key indexing the radial function in P."""
    (lA, mA, kA), (lB, mB, kB), (lC, mC, kC), (lD, mD, kD) = A, B, C, D
    q = mB - mA
    if mC - mD != q: return 0.0
    tot = 0.0
    for k in range(0, kmax + 1):
        if abs(q) > k: continue
        if (lC + k + lD) % 2 or not (abs(lC - lD) <= k <= lC + lD): continue    # G2's strict selection
        x, w = _gauss(np)
        PC_, _ = _plm(np, lC, mC, x); PD_, _ = _plm(np, lD, mD, x); PK_, _ = _plm(np, k, q, x)
        G2 = _norm(lC, mC) * _norm(k, q) * _norm(lD, mD) * 2 * math.pi * float(np.sum(w * PC_ * PK_ * PD_))
        if abs(G2) < 1e-14: continue
        G1, A3r = _ang(np, lA, mA, k, q, lB, mB)
        if abs(G1) < 1e-14 and abs(A3r) < 1e-14: continue
        rad1, rad2, rad3 = _radials(np, P[kA], P[kB], P[kC], P[kD], r, dr, k)
        tot += (4 * math.pi / (2 * k + 1)) * G2 * (G1 * (rad1 * mB + rad2 * q) + rad3 * A3r)
    return -tot


# ================================================================== --exchange: the whole SOMF zeta
def somf_zeta(np, ch, h, Z, n, l, occ, ma=None):
    """zeta_a from the mean-field spin-orbit operator, all three channels through ONE machinery.

        h^SOC_pq = (p|h1e|q) + SUM_rs P_rs [ (pq|g|rs) - (3/2)(pr|g|sq) - (3/2)(sq|g|pr) ]     (ORCA 6.1)

    In the T notation of this module, with p = q = a (the entrant, magnetic number m_a) and r = s = b (a core
    spatial orbital, m_b), and P_rs = 2 for a doubly occupied spatial orbital:

        Coulomb   T(a,a;b,b)        -- PROVED equal to -N_b M^0(ab), and re-proved through this machinery
        exchange  T(a,b;b,a) and T(b,a;a,b), each at -3/2

    zeta = -(1/m_a) x 2 x SUM_b SUM_mb [ ... ], all of it divided by 2c^2 to reach Hartree."""
    r, dr, P, C0 = h.r, h.dr, h.P, ch.C0
    a = (n, l)
    if ma is None: ma = l
    u = {}
    for (nn, ll, q) in occ:
        u[(nn, ll)] = P[(nn, ll)] / np.sqrt(float(np.sum(P[(nn, ll)] ** 2 * dr)))
    z_nuc = Z * float(np.sum(u[a] ** 2 / r ** 3 * dr))
    dir_sum = exc_sum = exc1 = exc2 = 0.0
    per = {}
    for (nb, lb, qb) in occ:
        b = (nb, lb)
        if b == a: continue
        d = e1 = e2 = 0.0
        for mb in range(-lb, lb + 1):
            d += T_z(np, (l, ma, a), (l, ma, a), (lb, mb, b), (lb, mb, b), u, r, dr)
            e1 += -1.5 * T_z(np, (l, ma, a), (lb, mb, b), (lb, mb, b), (l, ma, a), u, r, dr)
            e2 += -1.5 * T_z(np, (lb, mb, b), (l, ma, a), (l, ma, a), (lb, mb, b), u, r, dr)
        d *= -2.0 / ma; e1 *= -2.0 / ma; e2 *= -2.0 / ma; e = e1 + e2
        exc1 += e1; exc2 += e2
        per[f"{nb}{'spdfg'[lb]}"] = (d, e)
        dir_sum += d; exc_sum += e
    f = 1.0 / (2 * C0 * C0)
    return dict(z_nuc=z_nuc * f, z_dir=dir_sum * f, z_exc=exc_sum * f,
                z_exc1=exc1 * f, z_exc2=exc2 * f,
                z_tot=(z_nuc + dir_sum + exc_sum) * f, per={k: (v[0] * f, v[1] * f) for k, v in per.items()})


def cmd_exchange(log=sys.stderr):
    import numpy as np
    fe = _load("fieldentry", os.path.join(HERE, "fieldentry.py"))
    fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
    ch = fe.Chain(log=log)
    rows = []
    try:
        H, T, C0 = ch.hfc2, ch.t5_scf, ch.C0
        H.CORR = False
        for lab in ("3p", "4p", "5p", "6p", "4d", "5d"):
            m = fr.MEAS[lab]; Z, n, l = m["Z"], m["n"], m["l"]
            occ = T.ground_occ(Z)
            print(f"  {lab} {m['el']} Z={Z} ...", file=log, flush=True)
            h = H.HFC(Z, occ, c=C0); h.run2()
            out = somf_zeta(np, ch, h, Z, n, l, occ)
            chk = somf_zeta(np, ch, h, Z, n, l, occ, ma=1) if l > 1 else out
            zm = 2.0 * (m["split"] / HA_CM) / (2 * l + 1)
            rows.append(dict(lab=lab, el=m["el"], Z=Z, zeta_meas=zm, m_indep=abs(chk["z_tot"] / out["z_tot"] - 1), **out))
            print(f"    nuc {out['z_nuc']*HA_CM:9.1f}  dir {out['z_dir']*HA_CM:9.1f}  exc {out['z_exc']*HA_CM:9.1f}"
                  f"  tot {out['z_tot']*HA_CM:9.1f}  meas {zm*HA_CM:9.1f}  ratio {out['z_tot']/zm:.4f}",
                  file=log, flush=True)
        json.dump(dict(rows=rows), open(os.path.join(HERE, "sooterm-exchange.json"), "w"), indent=1)
        print("wrote sooterm-exchange.json", file=log)
    finally:
        ch.close()
    return rows

if __name__ == "__main__":
    main()
