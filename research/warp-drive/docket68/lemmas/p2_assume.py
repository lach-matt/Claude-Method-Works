#!/usr/bin/env python3
"""p2_assume.py -- item 323: "Assumptions to overrule if you disagree - prove the assumptions".  Item 322's answer
(p2_offset V6: 139 (1)'s plane's offset 2.625e-10 J/m^3, half ours) was reported as resting on three assumptions: the
board's one-way reading (a) of 276, with the side total the C4 verifier noted at 310; the flat static background of 139
(1); and, by implication, that the summed reading does not hold.  M orders them proved.  Each is proved here from M's
rulings and general relativity's junction of one surface between two bulks, and the one step of p2_offset V5 that
leaned on a board's reading (139 (2)'s "positive" against a negative-mass bulk) is closed on a ruling and a proof
instead.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; deduced where marked;
not verified by a separate session; not seated); 2026-10-12.

  Q0 (read) The words this rests on, verbatim in the rulings file: M's item 323; 276, "The passage is one-way in all
     aspects", and the error 276 recorded, g_coincide's "coincident sheets as one geometry acting both ways"; 275,
     "Coincident everywhere"; 201, M's "σ and its dark-energy offset", carried as "the offset carries the dark energy"
     and "k_R = k_L/2"; 202, "the same definitions as we do"; 226, "its plane's tension and offset among them"; 120 and
     137, "matter is neither created nor destroyed"; 141, "I suggest the planes are static"; and the C4 verifier's at
     310 (not M's), "the junction fixes position 2's side total S1 + 2 S2, not tau".
  Q1 (computed, exact; READ) One surface between two bulks.  With each side's carried stress Sigma^-+ (its extrinsic
     curvature in stress units), Israel's condition is Sigma^- + Sigma^+ = 2 S, S = S1 + S2 the surface's whole stress
     (b5a_residue A1), and each side obeys its own Gauss equation with the one H: H^2 = c Sigma^-+^2 - k^-+^2 + C^-+/a^4,
     c = (kappa^2/6)^2.  Together they fix the split: Sigma^-+ = S +- (k1^2 - k2^2 - (C1 - C2)/a^4)/(4 c S), and H^2 =
     c S^2 - (k1^2 + k2^2)/2 + (C1 + C2)/(2 a^4) + (k1^2 - k2^2 - (C1 - C2)/a^4)^2/(16 c S^2) (computed).  At equal
     curvatures this is Ida's brane-world Friedmann equation for two sides of different mass (gr-qc/9912002 eq. (24),
     READ: "a new term arises if the assumption Z2-symmetry is dropped"), term by term (computed).  So the split is not
     a free reading: general relativity fixes it from the stress and the two bulks.
  Q2 (deduced from 276; computed) Assumption 1 proved: our side carries ours alone, Sigma^- = S1.  "One-way in all
     aspects": nothing of position 2's -- its stress, its bulk, its presence -- acts on ours, so every quantity on our
     side is a function of ours alone (S1, our bulk's k1 and C1), the same function whether position 2 is there or not.
     Take the universe in which it is not -- our plane alone as the record defines it, the one-plane configuration whose
     relation 201's B6' is (sigma = 3 c^4/(4 pi G ell^2) holds for a plane with its bulk on both sides), not a free
     choice of far side: Israel's condition with the mirror gives Sigma^- = Sigma^+ = S1 (computed), and our Gauss
     equation gives H^2 = c S1^2 - k1^2 + C1/a^4.  Our side's Sigma^- is fixed by H and our bulk alone -- Sigma^- =
     (6/kappa^2) sqrt(H^2 + k1^2 - C1/a^4), the positive root, ours being positive (computed) -- and both are ours, so in
     the actual configuration Sigma^- = S1 (computed).  Israel then gives Sigma^+ = S1 + 2 S2, the side total the C4
     verifier noted (310).  Against Q1, our side carries S1 if and only if 4 c (S1 + S2) S2 = k2^2 - k1^2 + (C1 - C2)/a^4
     (computed): 276 does not add an assumption to general relativity, it fixes position 2's content -- the relation
     p2_offset V5 solves.
  Q3 (deduced; computed; READ) Assumption 2 proved: the flat static background, k1 = kappa^2 sigma/6 and k2 = kappa^2
     sigma/12.
     - k1.  201 defines our universe by its tension and "its dark-energy offset": the offset carries the dark energy, so
       with no offset and no matter our plane is flat, H = 0, and Q2's Gauss equation gives c sigma^2 = k1^2, k1 =
       kappa^2 sigma/6 (computed).  Ida (READ, eq. (30)): the induced cosmological constant kappa^4 sigma^2/12 - 3 l^2
       vanishes exactly there (computed).  And 201's B6' -- sigma = 3 c^4/(4 pi G ell^2) as a definition, with G =
       kappa^4 sigma/(48 pi) (Ida (29), READ; SMS) and ell = 1/k1 -- gives the same k1 (computed): two record routes, one
       value.
     - k2.  202 gives position 2 "the same definitions as we do", 226 its tension and offset: its offset carries its
       dark energy, so with no offsets and no matter its side is flat too, c Sigma^+(0)^2 = k2^2, and Sigma^+(0) = sigma
       - 2 sigma/4 = sigma/2 (Q2, 139 (1)), so k2 = kappa^2 sigma/12 = k1/2 (computed) -- the ratio 201 already carries,
       "k_R = k_L/2".
     - Static.  With these curvatures and the tensions alone, Q1's general relativity returns H = 0, our side carrying
       exactly sigma and position 2's exactly sigma/2 (computed): the background is a solution, flat, its planes at
       rest relative to each other (141) and coincident (275).
  Q4 (computed; READ in the rulings) Assumption 3: the summed reading excluded.  If our side carried the summed stress,
     Sigma^- = S1 + S2, our expansion would turn on position 2's offset (d H^2/d delta sigma_2 = 2 c (S1 + S2), not 0)
     and our Newton constant on its tension (kappa^4 (3 sigma/4)/(48 pi), not kappa^4 sigma/(48 pi)) (computed) --
     position 2 acting on ours, against 276.  276 recorded exactly that as the board's error: g_coincide treated "the
     two coincident sheets as one geometry acting both ways".  And by Q1 a symmetric split needs k1^2 - k2^2 = (C1 -
     C2)/a^4 at every a, so k1 = k2 -- not Q3's (computed).
  Q5 (computed; deduced) p2_offset V5's closure, without the board's reading.  V5 needs the constant part B of the Gauss
     pair to vanish.  A vacuum energy carries no flux (Sigma + Pi = 0 in the Codazzi identity, b5a_residue A3); our
     matter is conserved -- 120's and 137's "matter is neither created nor destroyed", and 276 -- so C1 is constant. A
     constant B != 0 then needs C2 = C1 + c a^4 B, and C2 changes only through position 2's sheet (Codazzi at the sheet,
     A3).  A sheet riding outward in Vaidya-AdS5 has w = dv/dtau (or du/dtau, the outgoing dust) proportional to 1/a
     (computed), so the flux Codazzi demands is a source on position 2's matter proportional to H: d rho2/d ln a + 3 (1 +
     w2) rho2 = -K, K = 6 c w0 B/kappa^2 (computed), whose late solution is rho2 = -K/(3 (1 + w2)), a constant
     (computed).  Either that density is negative -- against pointwise P4, matter's rho >= 0 proved -- or it is held
     constant while the plane expands, its amount growing as a^3 without end: matter created, against 120 and 137.  A
     steady state that folds rho2's constant into B changes nothing: with B = 0 there is no flux, rho2 dilutes, and its
     constant is 0.  So B = 0 (deduced), on a ruling and a proof; p2_offset V5's appeal to 139 (2) and to Q > 0 stays as
     corroboration.  A field carrier is no way round: a constant part of its stress at the sheet is bulk vacuum, inside
     Q3's k2, and its flux sources position 2's matter through the same Codazzi identity (A3) (deduced).
     [Item 339 (the B5a verifier's note outside B5a): "our matter is conserved -- so C1 is constant" omits the bulk's
     normal stress at our sheet. The verifier derived Cdot1 = -(2 kappa^2/3) a^4 H T_nn - (kappa^4/18) a^4 eps J (its
     derivation, not re-derived by the board): with no flux C1 is constant only if our bulk's T_nn vanishes at our
     sheet, which 320 makes a limit, so the step is incomplete. It found no effect on x+, B being a property of the
     offsets alone (the verifier's reading, recorded).]
  Q6 (deduced) The three are derived, not assumed: 1 from 276 with Israel's condition; 2 from 201, 202 and 226 with
     Israel and Gauss (and 201's B6' agreeing); 3 excluded by 276.  Item 322's answer stands on M's rulings and general
     relativity: 139 (1)'s plane's offset is 2.625e-10 J/m^3.
  Q7 (the cypher NOT-RUN, stated) Each assumption is a derivation from rulings, not a choice among configurations; an
     index of (reading, one-way, flat, static) rows would carry the answer as its own column, a key (211), as
     tau_share T6, pointwise P9 and p2_offset V8 found.  Not run, and said.

What this does not prove.
  - General relativity in the bulk (Einstein's equations, Israel's condition, Gauss and Codazzi): the framework of the
    whole record, taken as given.
    [Item 324: M ordered it proved; it is, in relativity.py U1-U6 -- everything that can exist couples to one metric,
    whose law is Einstein's in four dimensions and Einstein's with one constant more in five (U4), that constant
    computed through to item 322's offset.]  [Item 325: that constant evaluated, alpha = 0 exactly in both bulks
    (gb_alpha.py B2-B3, on 201's B6'): the law in five dimensions is Einstein's.]  [Item 326: and from U6 alone,
    gravity keeping the light cone (gb_cone.py C7).]
  - That "all aspects" admits no other reading: Q2 reads it as including position 2's presence, since a presence that
    changed ours would be position 2 acting on ours.
  - Anything before late times: Q5's limit is the expanding universe of two positive offsets, a growing without end.

Imports p2_offset.py by path.  Stdlib + sympy.  python3 p2_assume.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("Assumptions to overrule if you disagree - prove the assumptions", "The passage is one-way in all aspects",
         "coincident sheets as one geometry acting both ways", "Coincident everywhere", "σ and its dark-energy offset",
         "the offset carries the dark energy", "k_R = k_L/2", "the same definitions as we do",
         "its plane's tension and offset among them", "matter is neither created nor destroyed",
         "I suggest the planes are static", "the junction fixes position 2's side total S1 + 2 S2, not tau")
IDA = ("a new term arises if the assumption Z2-symmetry is dropped", "8 pi G_N = kappa^4 sigma/6",
       "Lambda = kappa^4 sigma^2/12 - 3 l^2")          # gr-qc/9912002, abstract and eqs. (29), (30), READ
kap, sig, a, H = sp.symbols("kappa sigma a H", positive=True)
S1, S2, k1, k2, C1, C2 = sp.symbols("S1 S2 k1 k2 C1 C2", real=True)
c = (kap ** 2 / 6) ** 2


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def junction():
    """Q1: Israel's sum and the two Gauss equations fix the split; Ida's eq. (24) at equal curvature"""
    S = sp.Symbol("S", positive=True)
    Sm = sp.Symbol("Sigma_m", real=True)
    Sp = 2 * S - Sm
    sol = sp.solve(sp.Eq(c * Sm ** 2 - k1 ** 2 + C1 / a ** 4, c * Sp ** 2 - k2 ** 2 + C2 / a ** 4), Sm)[0]
    split = sp.simplify(sol - (S + (k1 ** 2 - k2 ** 2 - (C1 - C2) / a ** 4) / (4 * c * S))) == 0
    H2 = sp.expand(c * sol ** 2 - k1 ** 2 + C1 / a ** 4)
    H2_form = sp.simplify(H2 - (c * S ** 2 - (k1 ** 2 + k2 ** 2) / 2 + (C1 + C2) / (2 * a ** 4)
                                + (k1 ** 2 - k2 ** 2 - (C1 - C2) / a ** 4) ** 2 / (16 * c * S ** 2))) == 0
    l, aR, aL = sp.symbols("l alpha_R alpha_L", positive=True)
    s = 1 if not MUT.get("ida_sign") else -1               # the mutant: the asymmetric term with the other sign
    ida = kap ** 4 * S ** 2 / 36 - l ** 2 + (aR + aL) / (2 * a ** 4) + s * 9 * (aR - aL) ** 2 / (4 * kap ** 4 * S ** 2
                                                                                                  * a ** 8)
    ours = H2.subs({k1: l, k2: l, C1: aL, C2: aR})          # Ida's k = 0 slice, our sides L = ours, R = position 2's
    reduces = sp.simplify(ours - ida) == 0
    return dict(sol=sol, split=split, H2_form=H2_form, reduces=reduces)


def oneway(jn):
    """Q2: the mirror universe gives Sigma = S1; Gauss on our side gives Sigma^- = S1; the condition on position 2"""
    Sm, Sp = sp.symbols("Sigma_m Sigma_p", real=True)
    half = sp.Rational(1, 2) if MUT.get("z2_half") else 1  # the mutant: the mirror read as halving our stress
    mirror = sp.solve([sp.Eq(Sm, Sp), sp.Eq(Sm + Sp, 2 * S1 * half)], [Sm, Sp], dict=True)[0]
    s1 = sp.Symbol("s1", positive=True)                     # S1 > 0: sigma > 0, offset and matter >= 0
    H2_ours = c * mirror[Sm] ** 2 - k1 ** 2 + C1 / a ** 4
    Sigma_m = (6 / kap ** 2) * sp.sqrt(H2_ours + k1 ** 2 - C1 / a ** 4)
    carries = sp.simplify(Sigma_m.subs(S1, s1) - s1) == 0
    side = sp.simplify(2 * (S1 + S2) - S1 - (S1 + 2 * S2)) == 0
    cond = sp.factor(sp.expand((jn["sol"].subs(sp.Symbol("S", positive=True), S1 + S2) - S1) * 4 * c * (S1 + S2)))
    cond_ok = sp.simplify(cond - (4 * c * (S1 + S2) * S2 + k1 ** 2 - k2 ** 2 - (C1 - C2) / a ** 4)) == 0
    return dict(mirror=mirror[Sm], carries=carries, side=side, cond=cond_ok)


def background():
    """Q3: k1 from 201's flatness, Ida (30) and B6'; k2 from 202/226; the static solution"""
    k1v = sp.solve(sp.Eq(c * sig ** 2 - k1 ** 2, 0), k1)
    k1v = [v for v in k1v if v.is_positive][0]
    if MUT.get("k1_double"):
        k1v = 2 * k1v                                       # the mutant: our bulk twice as curved
    ida30 = sp.simplify((kap ** 4 * sig ** 2 / 12 - 3 * k1v ** 2)) == 0
    G = kap ** 4 * sig / (48 * sp.pi)
    ell = 1 / k1v
    b6 = sp.simplify(sig - 3 / (4 * sp.pi * G * ell ** 2)) == 0       # B6' with c = 1
    Sp0 = sig - 2 * sig / 4
    if MUT.get("k2_from_total"):
        Sp0 = sig - sig / 4                                 # the mutant: position 2's side from the summed tension
    k2v = [v for v in sp.solve(sp.Eq(c * Sp0 ** 2 - k2 ** 2, 0), k2) if v.is_positive][0]
    jn = junction()
    S0 = sig - sig / 4
    Sm0 = sp.simplify(jn["sol"].subs({sp.Symbol("S", positive=True): S0, k1: k1v, k2: k2v, C1: 0, C2: 0}))
    H0 = sp.simplify(c * Sm0 ** 2 - k1v ** 2)
    return dict(k1=k1v, k2=k2v, ratio=sp.simplify(k2v / k1v), ida30=ida30, b6=b6, Sm0=Sm0, Sp0=sp.simplify(2 * S0 - Sm0),
                H0=H0)


def summed(bg):
    """Q4: the summed reading puts position 2's offset and tension in our expansion and our G"""
    d2 = sp.Symbol("delta_sigma_2", real=True)
    S1v, S2v = sig + sp.Symbol("d1", real=True), -sig / 4 + d2
    H2_sum = c * (S1v + S2v) ** 2 - bg["k1"] ** 2
    dep = sp.simplify(sp.diff(H2_sum, d2))
    G_sum, G_ours = kap ** 4 * (sig - sig / 4) / (48 * sp.pi), kap ** 4 * sig / (48 * sp.pi)
    allowed = bool(MUT.get("summed_ok"))                    # the mutant: the summed reading let stand
    symmetric_needs_equal = sp.simplify(bg["k1"] - bg["k2"]) != 0     # Q1: Sigma^- = S at C1 = C2 only if k1 = k2
    return dict(dep=dep, acts=(dep != 0 or sp.simplify(G_sum - G_ours) != 0) and not allowed,
                symmetric_excluded=symmetric_needs_equal and not allowed)


def closure():
    """Q5: w = dv/dtau ~ 1/a for a sheet riding outward in Vaidya-AdS5; Codazzi's source; rho2's late value"""
    R, Hh, k, C, r0 = sp.symbols("R H_h k C r0", positive=True)
    f = k ** 2 * R ** 2 - C / R ** 2
    Rdot = Hh * R
    vdot = (Rdot + sp.sqrt(Rdot ** 2 + f)) / f              # from -1 = -f vdot^2 + 2 vdot Rdot, the future root
    udot = (-Rdot + sp.sqrt(Rdot ** 2 + f)) / f             # outgoing: -1 = -f udot^2 - 2 udot Rdot
    norm = sp.simplify(-f * vdot ** 2 + 2 * vdot * Rdot + 1) == 0 and \
        sp.simplify(-f * udot ** 2 - 2 * udot * Rdot + 1) == 0
    w_scaled = sp.limit(vdot * R, R, sp.oo)                 # finite and positive: w ~ w0/a
    u_scaled = sp.limit(udot * R, R, sp.oo)
    u_pos = sp.simplify(1 / u_scaled - (Hh + sp.sqrt(Hh ** 2 + k ** 2))) == 0     # 1/(H + sqrt(H^2 + k^2)) > 0
    both = bool(w_scaled.is_positive) and u_pos
    if MUT.get("w_const"):
        w_power = 0                                         # the mutant: w read as a constant
    else:
        w_power = -1 if (both and sp.limit(vdot * R ** 2, R, sp.oo) == sp.oo) else 0
    N = sp.Symbol("N", real=True)                           # N = ln a
    w2, K, B, w0 = sp.symbols("w2 K B w0", real=True)
    rho = sp.Function("rho2")
    # Codazzi on position 2's side: 2 (rho' + 3 (1 + w2) rho) H = -(3/(kappa^2 a^3)) w dC2/dtau, dC2/dtau = 4 c B a^4 H
    src = -(3 / (kap ** 2 * sp.exp(3 * N))) * w0 * sp.exp(w_power * N) * 4 * c * B * sp.exp(4 * N) / 2
    ode = sp.Eq(rho(N).diff(N) + 3 * (1 + w2) * rho(N), src)
    gen = sp.dsolve(ode, rho(N)).rhs
    w2v = sp.Rational(0)                                    # dust; any w2 > -1 alike
    late = sp.limit(gen.subs(w2, w2v), N, sp.oo)
    late_val = sp.simplify(late) if late.is_finite else None
    expect = sp.simplify(-(6 * c * w0 * B / kap ** 2) / 3)
    return dict(norm=norm, w_scaled=w_scaled, u_scaled=u_scaled, w_power=w_power, late=late_val,
                late_ok=late_val is not None and sp.simplify(late_val - expect) == 0,
                vanishes_iff_B0=late_val is not None and sp.simplify(late_val.subs(B, 0)) == 0)


def compute():
    jn = junction()
    bg = background()
    return dict(jn=jn, ow=oneway(jn), bg=bg, sm=summed(bg), cl=closure())


def report(o):
    jn, ow, bg, sm, cl = o["jn"], o["ow"], o["bg"], o["sm"], o["cl"]
    print("p2_assume.py -- the assumptions of item 322 proved (item 323)\n")
    print("Q1 split Sigma^-+ = S +- (k1^2 - k2^2 - dC/a^4)/(4 c S): %s; H^2 form: %s; Ida (24) at equal curvature: %s"
          % (jn["split"], jn["H2_form"], jn["reduces"]))
    print("Q2 mirror gives Sigma = %s; our side carries S1: %s; Sigma^+ = S1 + 2 S2: %s; the condition on position 2: "
          "%s" % (ow["mirror"], ow["carries"], ow["side"], ow["cond"]))
    print("Q3 k1 = %s, k2 = %s, k2/k1 = %s; Ida (30) vanishes: %s; B6' agrees: %s; tensions alone: Sigma^- = %s, "
          "Sigma^+ = %s, H^2 = %s" % (bg["k1"], bg["k2"], bg["ratio"], bg["ida30"], bg["b6"], bg["Sm0"], bg["Sp0"],
                                      bg["H0"]))
    print("Q4 summed reading: d H^2/d delta sigma_2 = %s; position 2 acts on ours: %s; a symmetric split needs k1 = k2: "
          "%s" % (sm["dep"], sm["acts"], sm["symmetric_excluded"]))
    print("Q5 sheet in Vaidya-AdS5: normalised %s, lim w R = %s, outgoing %s (w ~ a^%s); rho2's late value %s; zero "
          "iff B = 0: %s" % (cl["norm"], cl["w_scaled"], cl["u_scaled"], cl["w_power"], cl["late"],
                             cl["vanishes_iff_B0"]))


def checks(o):
    jn, ow, bg, sm, cl = o["jn"], o["ow"], o["bg"], o["sm"], o["cl"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Q0 item 323, 276 and its recorded error, 275, 201, 202, 226, 120/137, 141 and 310's note verbatim",
        all(w in rul for w in WORDS))
    add("Q1 general relativity fixes the split from the stress and the two bulks; Ida's eq. (24) at equal curvature",
        jn["split"] and jn["H2_form"] and jn["reduces"])
    add("Q2 the mirror gives Sigma = S1; our side, fixed by H and our bulk, carries S1; Sigma^+ = S1 + 2 S2; GR's split "
        "equals S1 exactly under the relation on position 2", ow["mirror"] == S1 and ow["carries"] and ow["side"]
        and ow["cond"])
    add("Q3 k1 = kappa^2 sigma/6 (201's flatness, Ida (30), B6'), k2 = k1/2 (202, 226), the tensions alone static",
        bg["k1"] == kap ** 2 * sig / 6 and bg["ratio"] == sp.Rational(1, 2) and bg["ida30"] and bg["b6"]
        and bg["Sm0"] == sig and bg["Sp0"] == sig / 2 and bg["H0"] == 0)
    add("Q4 the summed reading puts position 2 in our expansion and our G, against 276; a symmetric split needs k1 = k2",
        sm["acts"] and sm["symmetric_excluded"])
    add("Q5 w ~ 1/a; the Codazzi source holds rho2 at a nonzero constant unless B = 0", cl["norm"]
        and cl["w_power"] == -1 and cl["late_ok"] and cl["vanishes_iff_B0"])
    return res


MUTANTS = {"ida_sign": "the asymmetric term of the junction with the other sign (Q1)",
           "z2_half": "the mirror read as halving our stress (Q2)",
           "k1_double": "our bulk twice as curved (Q3)",
           "k2_from_total": "position 2's side flat on the summed tension (Q3)",
           "summed_ok": "the summed reading let stand (Q4)",
           "w_const": "the sheet's dv/dtau read as a constant (Q5)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
