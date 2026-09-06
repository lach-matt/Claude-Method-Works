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

  THE MEAN-FIELD COEFFICIENTS, FOUND AND RECORD-CARRIED WITH THEIR QUOTE.  Blume & Watson's own papers are
  paywalled, but the working equation they stand behind is stated in the open literature, and M's direction was
  to look for who cites them rather than stop at them.  Kotaru, Pokhilko, Sokolov, arXiv:2404.04716 Eq. (15),
  in the spin-orbit mean-field (SOMF) approximation:

      F^{BP,xi}_pq = h^xi_pq + SUM_rs P_rs [ g^xi_pqrs - (3/2) g^xi_sqpr + (3/2) g^xi_spqr ]

  with P_rs the spin-free one-particle density matrix, and (their Eqs. 16-20)

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

  WHAT REMAINS, AND IT IS ONE STEP: the ANGULAR reduction of the two exchange terms over a spherical closed
  shell, which turns them into sums over k of the exchange-shaped radial integrals N^k(ab) with 3j weights.  The
  operator and its coefficients are no longer the open piece; the reduction is.  §THE EXCHANGE CHANNEL below
  states it with its gates.

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
  THE EXCHANGE CHANNEL: ONE STEP OPEN, AND IT IS NO LONGER THE COEFFICIENTS

  The mean-field working equation is now record-carried with its quote (see the docstring): Coulomb at +1, the
  two exchange terms at -3/2 and +3/2, the 3/2 being the spin-own-orbit at weight 1 plus the spin-other-orbit at
  weight 2.  M's direction found it -- "search for others who have referenced these papers" -- where stopping at
  Blume & Watson themselves had not: arXiv:2404.04716 Eq. (15) states it in the open, and cites them for it.

  What is still owed is the ANGULAR reduction of those two exchange terms over a spherical closed shell: the
  weights on the exchange-shaped radial integrals N^k(ab) as functions of (l_a, l_b, k).  It is a derivation, not
  a lookup, and it has an anchor no reading could give it:

    the object      d_zeta_a = SUM_b [ -N_b M^0(ab)  +  SUM_k c_k(l_a,l_b) N^k(ab) ]
    the Coulomb half PROVED here: -N_b M^0(ab), the two routes agreeing to 1.5e-5 at all six openings
    the radial half  BUILT AND GATED here: marvin_M and marvin_N, in the chain's own quadrature convention
    the angular half c_k, the one open piece
    its gates       (a) the Coulomb half unchanged, which --verify already asserts and which any correct
                    reduction must reproduce THROUGH THE SAME MACHINERY; (b) lever-dead as c -> inf;
                    (c) identically zero for l_a = 0; (d) THE SIX MEASURED INTERVALS, which span 0.910 to 1.360
                    today -- a wrong reduction does not collapse a 1.5x spread across p and d and across Z from
                    13 to 81, so this is a test and not a fit

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
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if a.verify: cmd_verify(); return
    report()


if __name__ == "__main__":
    main()
