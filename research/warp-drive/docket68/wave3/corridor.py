#!/usr/bin/env python3
"""
corridor.py -- DOCKET 68 wave 3, W3A: the corridor as the A-B coupling (M-RULINGS items 21-22).

Not seated.  stdlib + numpy.  It reads nothing from the board but M's words (the rulings file); every outside result is
READ at source with the route recorded.

    python3 corridor.py              report
    python3 corridor.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 corridor.py --json       the numbers as JSON

M'S WORDS (M-RULINGS-2026-10-03.md, verbatim)
  item 21: "The two positions technically exist as one. So the corridor allows for the the entanglement of two positions
           at once. The object in transit requires no speed. It is either at the beginning or end position, never in
           between them".
  item 22: the corridor carried as the A-B coupling, a two-position system |A>, |B> rotated by a coupling term -- M:
           "Yes. Exactly." and "yes please".

THE MODEL.  One excitation (the object's state) on two positions, H = J (|A><B| + |B><A|) (hbar = 1).  This is
Christandl, Datta, Ekert & Landahl's N = 2 chain (quant-ph/0309131v2 p.2, READ via alphaXiv: 'F(t) = -i sin(t)').

WHAT IT COMPUTES
  (1) NEVER IN BETWEEN -- IN THE TWO-SITE MODEL (H-DIRECT-COUPLING).  The position observable X = x_A |A><A| +
      x_B |B><B| has exactly two eigenvalues, so every measurement finds the object at A or at B (true by construction
      of a two-site model: printed STRUCTURAL).  On any RELAYED chain this fails: at half the transfer time the object is
      found on interior sites with probability 0.50 (engineered N = 3), 0.75 (N = 4), 0.98 (N = 8) (computed).  P_B(t) = sin^2(J t); the transfer is complete at t* = pi / (2J)
      (reproducing Christandl's F(pi/2) = -i).  NUANCE, computed: the MEAN <X>(t) passes through every value between
      x_A and x_B -- no single outcome is in between, the average is.
  (2) THE ENTANGLEMENT OF TWO POSITIONS AT ONCE.  At t*/2 the state is (|A> - i|B>)/sqrt2.  Read as two modes (occupied
      / empty at A, at B), its concurrence is 2 |c_A c_B| = 1: maximal mode entanglement between the two positions
      (H-MODE-ENTANGLEMENT: reading a single excitation as entanglement between modes is a contested reading).  Under
      it, M's item-21 phrase is the mid-transfer state.
  (3) A COUPLING IS A CHANNEL.  With J > 0, B's local occupation at time t depends on whether A was prepared excited or
      empty (on/off keying: a classical bit gets through; the empty start is the zero-excitation sector, which the
      hopping term does not move -- Christandl p.2, carried).  MATCHED CONTROL: the same protocol with J = 0 gives no
      deviation.  Second CONTROL: entanglement alone (a Bell pair, J = 0) does not signal.  The transfer of the STATE
      itself rests on F(t*) = -i, a fixed phase (Christandl eqs. 3, 5): no classical bits are needed (contrast
      transit.py's 2 bits per qubit).
  (4) WHERE DISTANCE ENTERS.  The two-site model has no distance in it: t* does not depend on how far apart A and B are
      (STRUCTURAL).  Physics puts distance back through how the coupling is MEDIATED:
        (a) uniform nearest-neighbour chain of N sites, coupling J: the excitation's first arrival at the far end grows
            linearly with N (a finite group speed), and perfect transfer happens only for N = 2, 3 (Christandl p.2);
        (b) Christandl's engineered chain, J_n = (lambda/2) sqrt(n (N - n)): perfect transfer at the fixed time pi/lambda
            (p.3, eq. 15) -- but its largest coupling grows with N, so with the coupling strength bounded by J_max the
            time is pi max_n sqrt(n(N-n)) / (2 J_max), which grows linearly with N;
        (c) the light cone: on the uniform chain the amplitude at distance d at HALF the time d/(2J) falls by about 90x
            per 10 sites (asymptotic rate acosh 2 - sqrt3/2 per site; computed); near the cone the decay is weak.  This
            is what Nachtergaele & Sims's Lieb-Robinson bound requires for short-range interactions (arXiv:1004.2086v1,
            Thm 2.3, eqs. 2.11, 2.15-2.16, READ via alphaXiv; eq. 2.15 needs an exponentially decaying interaction,
            p.5): 'Lieb-Robinson bounds imply that non-relativistic quantum dynamics has, at least approximately, the
            same kind of locality structure provided in a field theory by the finiteness of the speed of light' (p.1).
        (d) LONG-RANGE relays (H-LONG-RANGE): with pairwise strength bounded by 1/r^alpha, Eldredge et al.,
            arXiv:1612.02442v2 (READ via alphaXiv, abstract p.1): 'If alpha < d, the state transfer time is
            asymptotically independent of L; if alpha = d, the time scales logarithmically with the distance L';
            L^(alpha-d) for d < alpha < d + 1; L for alpha >= d + 1.  Caveat (p.6 fn. 45): for alpha <= d a volume
            prefactor 1/L^(d-alpha) is needed for a thermodynamic limit, whose inverse multiplies the transfer time.
            Realised in polar molecules, Rydberg atoms, trapped ions (p.1) -- as quasi-static (non-retarded)
            interactions (H-QUASI-STATIC).
        (e) UNBOUNDED relays: dropping H-BOUNDED-J, Christandl's engineered chain is speed-free too (pi/lambda for every
            N, 4b).
      So 'no speed' holds iff H-DIRECT-COUPLING, or H-LONG-RANGE with alpha < d, or not H-BOUNDED-J.  Each of these
      clashes with relativistic microcausality at the fundamental level (H-LOCALITY): a quasi-static long-range
      interaction is the non-retarded limit of a field that propagates at c, and an effective direct A-B term from a
      mediator integrated out (a cavity or bus mode spanning A to B; H-EFFECTIVE-COUPLING) needs that mediator in
      place first, itself causal at c.
  (5) BEFORE LIGHT (the board's DEF-BITS, combine.py: 'O-BITS removed iff a channel carries >= 2 bits per teleported
      qubit before light').  A coupling beats light across L iff its transfer time pi/2J < L/c, i.e. J > pi c/(2L): at
      the Proxima span, hbar J > 7.7e-24 eV per qubit in parallel; sent serially down one coupling, the whole object
      needs hbar J > hbar I pi c/(2L) (computed per count).  Moving the qubit itself counts as delivering a teleported
      qubit's 2 bits only under H-STATE-AS-BITS (a named mapping onto DEF-BITS).
  GRADE (proposed, for verification; not seated): O-BITS REMOVED-IF {one of H-DIRECT-COUPLING / H-LONG-RANGE
  (alpha < d) / not H-BOUNDED-J; J > pi c/(2L) (computed); H-STATE-AS-BITS}, and each speed-free option clashes with
  H-LOCALITY (relativistic microcausality).  It moves state, not substance: O-SEAT is untouched (H-INFO-SHAPE).
  O-LOOP: carried as an identification of the kind corridors.py grades (H-CORRIDOR-AS-IDENTIFICATION, a named
  mapping): it closes no causal loop only if every such coupling is keyed to one frame (corridors.py's H-FRAME) --
  recorded, not re-derived here.

HISTORY (first said, corrected after the W3A verifier, 2026-10-05): 'never in between' stated without its two-site
condition, and its eigenvalue check counted (it cannot fail); the O-BITS grade without DEF-BITS's 'before light'
condition; 'no speed iff DIRECT' omitting long-range (alpha < d) and unbounded relays; 'exponentially small before the
time d/(2J)' (computed only at half that time); the Nachtergaele-Sims quote without its 'at least approximately';
the signalling control in a different protocol (and signalling_coupled(J=0) divided by zero).

NAMED HYPOTHESES
  H-DIRECT-COUPLING  (M's reading of items 21-22) a single coupling term joins the degrees of freedom at A and at B with
                     no intermediate system.
  H-LOCALITY         physical interactions are local (field theory's finite speed; Lieb-Robinson for lattices): any
                     coupling between A and B is mediated.  The board's physics; it clashes with H-DIRECT-COUPLING.
  H-ONE-EXCITATION   the object's state is carried as one excitation (Christandl's single-spin-up subspace, p.2); a
                     many-body state is not modelled.
  H-BOUNDED-J        the local coupling strength is bounded by J_max (for 4b).
  H-LONG-RANGE       pairwise couplings 1/r^alpha with alpha < d (Eldredge et al., READ; fn. 45 caveat).
  H-QUASI-STATIC     a long-range interaction treated as instantaneous (its non-retarded limit).
  H-EFFECTIVE-COUPLING a direct A-B term obtained by integrating out a mediator that already spans A to B.
  H-MODE-ENTANGLEMENT a single excitation over two sites read as entanglement between the two modes.
  H-STATE-AS-BITS    moving a qubit counts, for DEF-BITS, as delivering a teleported qubit's 2 classical bits.
  H-CORRIDOR-AS-IDENTIFICATION a direct coupling between separated positions is graded as corridors.py's identification.
  H-INFO-SHAPE       (M, rulings items 1, 5) teleportation carries the shape; the substance comes from the seat.
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.abspath(os.path.join(HERE, ".."))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
M_WORDS_21 = ("The two positions technically exist as one. So the corridor allows for the the entanglement of two "
              "positions at once. The object in transit requires no speed. It is either at the beginning or end "
              "position, never in between them")
READ = [
    {"source": "quant-ph/0309131v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-4",
     "used": "N=2: F(t) = -i sin(t); uniform chain PST only for N = 2, 3 (p.2); engineered J_n = (lambda/2) sqrt(n(N-n)),"
             " F(t) = [-i sin(lambda t/2)]^(N-1), PST at t = pi/lambda (p.3, eq. 15)"},
    {"source": "arXiv:1004.2086v1", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-5",
     "used": "Thm 2.3 eq. 2.11; exponential form eq. 2.15; velocity bound eq. 2.16; p.1 'the same kind of locality "
             "structure provided in a field theory by the finiteness of the speed of light'"},
]


def evolve(H, psi0, t):
    w, V = np.linalg.eigh(H)
    return V @ (np.exp(-1j * w * t) * (V.conj().T @ psi0))


def chain(N, J=1.0, couplings=None):
    H = np.zeros((N, N))
    for n in range(N - 1):
        c = J if couplings is None else couplings[n]
        H[n, n + 1] = H[n + 1, n] = c
    return H


def basis(N, k):
    v = np.zeros(N, dtype=complex)
    v[k] = 1.0
    return v


# ============================================================================ (1) never in between
def two_site(J=1.0, xA=0.0, xB=1.0, n=401):
    H = chain(2, J)
    X = np.diag([xA, xB])
    tstar = math.pi / (2 * J)
    ts = np.linspace(0, tstar, n)
    pB = [abs(evolve(H, basis(2, 0), t)[1]) ** 2 for t in ts]
    meanX = [float(np.real(np.vdot(evolve(H, basis(2, 0), t), X @ evolve(H, basis(2, 0), t)))) for t in ts]
    amp = evolve(H, basis(2, 0), tstar)[1]
    return {"X_eigenvalues": sorted(np.linalg.eigvalsh(X).tolist()), "t_star": tstar, "P_B_at_t_star": pB[-1],
            "F_at_t_star": complex(amp), "sin2_max_err": max(abs(p - math.sin(J * t) ** 2) for p, t in zip(pB, ts)),
            "meanX_takes_values_strictly_between": sum(1 for m in meanX if xA + 1e-6 < m < xB - 1e-6)}


# ============================================================================ (2) entanglement of two positions
def mid_transfer_concurrence(J=1.0):
    psi = evolve(chain(2, J), basis(2, 0), math.pi / (4 * J))
    return 2.0 * abs(psi[0] * psi[1]), psi


# ============================================================================ (3) a coupling is a channel
def signalling_coupled(J=1.0, t=math.pi / 4):
    """B's occupation at time t when A starts excited vs empty.  The empty start is the zero-excitation sector, which the
    hopping term conserves (Christandl p.2): B's occupation from it is 0 at every t (carried, not computed)."""
    excited = abs(evolve(chain(2, J), basis(2, 0), t)[1]) ** 2
    empty = 0.0
    return abs(excited - empty)


def interior_occupation():
    """Probability on interior sites at half the perfect-transfer time: engineered chains (J_max = 1) and uniform N = 3."""
    out = {}
    for N in (3, 4, 8, 16):
        e = engineered_time(N)
        peak = max(math.sqrt(n * (N - n)) for n in range(1, N))
        lam = 2.0 / peak
        cpl = [lam / 2.0 * math.sqrt(n * (N - n)) for n in range(1, N)]
        psi = evolve(chain(N, couplings=cpl), basis(N, 0), e["t_pst"] / 2.0)
        out["engineered N=%d" % N] = float(1 - abs(psi[0]) ** 2 - abs(psi[-1]) ** 2)
    psi = evolve(chain(3), basis(3, 0), math.pi / (2 * math.sqrt(2)))
    out["uniform N=3"] = float(1 - abs(psi[0]) ** 2 - abs(psi[-1]) ** 2)
    return out


def before_light():
    """J > pi c/(2L) per qubit; serially for the whole object, J > I pi c/(2L).  hbar J in eV, at the Proxima span."""
    import contextlib
    import io
    for _p in (D68, os.path.join(D68, "..")):
        if _p not in sys.path:
            sys.path.insert(0, _p)
    with contextlib.redirect_stdout(io.StringIO()):
        import seat
        import measure
    hbar = 1.054571817e-34
    ev = 1.602176634e-19
    L, c = seat.D_PROXIMA, seat.C
    per = hbar * math.pi * c / (2 * L) / ev
    rows, _, _, _ = measure.price_table()
    return {"L_m": L, "hbarJ_min_eV_per_qubit": per,
            "serial_hbarJ_min_eV": {r["count"]: per * r["bits"] for r in rows}}


def no_signalling_bell(trials=50, seed=7):
    """J = 0, shared Bell pair: B's reduced state after any local unitary at A (largest change, trace distance)."""
    rng = np.random.default_rng(seed)
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)

    def rhoB(psi):
        m = psi.reshape(2, 2)
        return m.T @ m.conj()

    base = rhoB(bell)
    worst = 0.0
    for _ in range(trials):
        q, _ = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))
        psi = np.kron(q, np.eye(2)) @ bell
        d = 0.5 * np.abs(np.linalg.eigvalsh(rhoB(psi) - base)).sum()
        worst = max(worst, d)
    return worst


# ============================================================================ (4) where distance enters
def uniform_arrival(N, J=1.0, thr=0.05, tmax_factor=3.0, steps=6000):
    H = chain(N, J)
    ts = np.linspace(0, tmax_factor * N / (2 * J) + 2, steps)
    w, V = np.linalg.eigh(H)
    c0 = V.conj().T @ basis(N, 0)
    first, best = None, 0.0
    for t in ts:
        a = abs((V @ (np.exp(-1j * w * t) * c0))[N - 1]) ** 2
        best = max(best, a)
        if first is None and a >= thr:
            first = t
    return {"N": N, "first_arrival_t": first, "max_fidelity_in_window": best}


def engineered_time(N, J_max=1.0):
    peak = max(math.sqrt(n * (N - n)) for n in range(1, N))
    lam = 2.0 * J_max / peak
    t = math.pi / lam
    couplings = [lam / 2.0 * math.sqrt(n * (N - n)) for n in range(1, N)]
    F = evolve(chain(N, couplings=couplings), basis(N, 0), t)[N - 1]
    return {"N": N, "t_pst": t, "fidelity": abs(F) ** 2, "max_coupling": max(couplings)}


LC_RATE_PER_SITE = math.acosh(2.0) - math.sqrt(3.0) / 2.0      # asymptotic |J_d(d/2)| decay rate per site


def light_cone(d, J=1.0, frac=0.5):
    """Amplitude at distance d at time frac x d/(2J), on a uniform chain long enough to have no reflection."""
    N = 2 * d + 41
    t = frac * d / (2.0 * J)
    return abs(evolve(chain(N, J), basis(N, 20), t)[20 + d])


def collect():
    two = two_site()
    c, _ = mid_transfer_concurrence()
    return {"two_site": two, "mid_concurrence": c, "signalling_coupled": signalling_coupled(),
            "no_signalling_bell_worst": no_signalling_bell(),
            "uniform": [uniform_arrival(N) for N in (4, 8, 16, 32, 48)],
            "engineered": [engineered_time(N) for N in (2, 4, 8, 16, 32)],
            "light_cone": {d: light_cone(d) for d in (5, 10, 20, 30)}, "interior": interior_occupation(),
            "before_light": before_light(), "READ": READ}


def report():
    d = collect()
    t = d["two_site"]
    print("W3A -- the corridor as the A-B coupling (M-RULINGS items 21-22)")
    print('  M: "%s"' % M_WORDS_21)
    print("\n(1) never in between, in the two-site model (H-DIRECT-COUPLING): X's eigenvalues %s; P_B(t*) = %.12f at "
          "t* = pi/2J = %.4f; F(t*) = %s" % (t["X_eigenvalues"], t["P_B_at_t_star"], t["t_star"], t["F_at_t_star"]))
    print("    on relayed chains, probability between A and B at half the transfer time: %s"
          % {k: round(v, 4) for k, v in d["interior"].items()})
    print("    nuance: the mean <X> takes %d of 401 sampled values strictly between x_A and x_B (no outcome does)"
          % t["meanX_takes_values_strictly_between"])
    print("(2) the entanglement of two positions at once: mid-transfer mode concurrence %.12f (maximal = 1)"
          % d["mid_concurrence"])
    print("(3) a coupling is a channel: on/off deviation %.4f with J > 0; matched CONTROL J = 0: %.4f; Bell pair: %.2e"
          % (d["signalling_coupled"], signalling_coupled(J=0.0), d["no_signalling_bell_worst"]))
    print("(4) where distance enters (the two-site t* has no distance in it):")
    for u in d["uniform"]:
        print("    uniform chain N = %2d: first arrival (P >= 0.05) at t = %.3f; best fidelity in window %.4f"
              % (u["N"], u["first_arrival_t"], u["max_fidelity_in_window"]))
    for e in d["engineered"]:
        print("    engineered chain N = %2d, J_max = 1: perfect transfer at t = %.4f (fidelity %.12f)"
              % (e["N"], e["t_pst"], e["fidelity"]))
    for k, v in d["light_cone"].items():
        print("    light cone: amplitude at distance %2d at half the time d/2J: %.3e" % (k, v))
    print("    asymptotic decay at half the cone time: x %.4f per 10 sites" % math.exp(-10 * LC_RATE_PER_SITE))
    b = d["before_light"]
    print("(5) before light at the Proxima span: hbar J > %.3g eV per qubit in parallel; serially, the whole object:"
          % b["hbarJ_min_eV_per_qubit"])
    for k, v in b["serial_hbarJ_min_eV"].items():
        print("    %-42s hbar J > %.3g eV" % (k, v))
    print("\n  'No speed' iff H-DIRECT-COUPLING, H-LONG-RANGE (alpha < d), or unbounded J; each clashes with H-LOCALITY.")


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("corridor.py selftest")
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    chk("M's item-21 words found verbatim in the rulings file", M_WORDS_21 in txt, True)
    t = two_site()
    io_ = interior_occupation()
    chk("on a relayed chain the object IS found between A and B at half the transfer time (engineered N = 8 > 0.9)",
        io_["engineered N=8"] > 0.9, True)
    chk("P_B(t) = sin^2(J t) throughout (to 1e-12), complete at t* = pi/2J",
        (t["sin2_max_err"] < 1e-12, abs(t["P_B_at_t_star"] - 1) < 1e-12), (True, True))
    chk("Christandl N = 2: F(pi/2) = -i (to 1e-12)", abs(t["F_at_t_star"] - (-1j)) < 1e-12, True)
    chk("the MEAN position passes between A and B (nuance: no outcome does, the average does)",
        t["meanX_takes_values_strictly_between"] > 0, True)
    c, _ = mid_transfer_concurrence()
    chk("mid-transfer mode concurrence is 1 (maximal entanglement of the two positions)", abs(c - 1) < 1e-12, True)
    chk("a coupling signals: B's occupation depends on A's preparation (deviation 0.5 at t*/2)",
        abs(signalling_coupled() - 0.5) < 1e-12, True)
    chk("CONTROL (matched): the same on/off protocol with J = 0 gives no deviation", signalling_coupled(J=0.0), 0.0,
        ctl=True)
    chk("CONTROL: entanglement alone (J = 0, Bell pair) does not signal (worst change < 1e-12)",
        no_signalling_bell() < 1e-12, True, ctl=True)
    u = [uniform_arrival(N) for N in (8, 16, 32, 48)]
    slopes = [(u[i + 1]["first_arrival_t"] - u[i]["first_arrival_t"]) / (u[i + 1]["N"] - u[i]["N"])
              for i in range(len(u) - 1)]
    chk("uniform chain: first arrival grows linearly with N (successive slopes agree within 10%%; %s)"
        % ["%.3f" % s for s in slopes], max(slopes) / min(slopes) < 1.1, True)
    chk("uniform chain: no perfect transfer at N = 8 (Christandl: PST only for N = 2, 3)",
        uniform_arrival(8)["max_fidelity_in_window"] < 0.999, True)
    chk("CONTROL: the uniform N = 3 chain does transfer perfectly at t = pi/sqrt2 (Christandl p.2)",
        abs(abs(evolve(chain(3), basis(3, 0), math.pi / math.sqrt(2))[2]) ** 2 - 1) < 1e-12, True, ctl=True)
    e = [engineered_time(N) for N in (4, 8, 16, 32)]
    chk("engineered chain: perfect transfer at t = pi/lambda for every N (fidelity 1 to 1e-10)",
        all(abs(x["fidelity"] - 1) < 1e-10 for x in e), True)
    chk("engineered chain with J_max bounded: the transfer time grows with N (doubling N roughly doubles it)",
        all(1.8 < e[i + 1]["t_pst"] / e[i]["t_pst"] < 2.2 for i in range(len(e) - 1)), True)
    lc = [light_cone(dd) for dd in (10, 20, 30)]
    chk("light cone: at half the time d/2J the amplitude at distance d falls by > 50x per 10 sites (asymptotic x %.4f)"
        % math.exp(-10 * LC_RATE_PER_SITE), all(lc[i + 1] < 2e-2 * lc[i] for i in range(len(lc) - 1)), True)
    chk("CONTROL: near the cone (0.95 d/2J) the decay is weak -- d = 40 keeps more than 1% of d = 20's amplitude",
        light_cone(40, frac=0.95) > 0.01 * light_cone(20, frac=0.95), True, ctl=True)
    bl = before_light()
    chk("before light: hbar J per qubit = hbar pi c/(2L) at the Proxima span is 7.7e-24 eV (to 2%)",
        abs(bl["hbarJ_min_eV_per_qubit"] / 7.7e-24 - 1) < 0.02, True)
    structural.append("the two-site transfer time pi/2J contains no distance: built so (the model has no distance in "
                      "it); what is computed is where distance re-enters (4a-4e)")
    structural.append("the position observable of a two-site model has exactly two eigenvalues %s: true by construction"
                      % t["X_eigenvalues"])
    structural.append("a two-site chain has no interior sites, so nothing is found between A and B there: true by "
                      "construction (normalisation); relayed chains are the computed case above")
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
