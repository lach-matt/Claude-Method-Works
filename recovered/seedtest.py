"""seedtest.py -- s61, Rung 3/4 SEED-INDEPENDENCE. Prediction sha 192d08537bf28e9e.
The ruling path is untouched: NG.run_guarded -> HFC.run2, CORR=False, c=C0, chained cfg.
The ONLY variable is HF.seed (t7b_hf.py:33), run2's line 40, the sole entry of TFD /
Latter / alpha=2/3 into the walk.
  A  baseline, qtail=1        B  same generator, qtail=6      C  bare Coulomb -Z/r, no TFD
usage: python3 pack61/seedtest.py A            can-fail the switch (no SCF)
       python3 pack61/seedtest.py E Z          fixed-config converged energy, 3 seeds
       python3 pack61/seedtest.py O Z seed     one chain step under one seed
"""
import sys, os, json, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import t7b_hf
from hfs import numerov_wf
import nlchain as NC
import nlguard as NG
import hfc2 as H
from t7c_kernel import C0
H.CORR = False

BASE = t7b_hf.HF.seed          # the sealed seed, captured unbound before any patch


def seed_A(self, qtail=1):
    return BASE(self, 1)


def seed_B(self, qtail=1):
    return BASE(self, 6)       # same generator, different Latter tail


def seed_C(self, qtail=1):
    """bare Coulomb start: V = -Z/r. No TFD, no Latter clamp, no exchange, no screening,
    no chosen constant. s53's 'different potential' in its strongest available form."""
    Z = self.Z
    Vf = lambda rr: -Z / np.asarray(rr, float)
    P = {}; eps = {}
    for n, l, q in self.occ:
        rr, drr, u, E, nd = numerov_wf(Vf, l, n, 1.0, Z)
        if nd != n - l - 1:
            raise RuntimeError(f"seed_C Z={Z} {n},{l} nodes {nd}")
        ui = np.interp(self.r, rr, u, left=0.0, right=0.0)
        ui /= np.sqrt(np.sum(ui * ui * self.dr))
        P[(n, l)] = ui; eps[(n, l)] = E
    return P, eps


SEEDS = {"A": seed_A, "B": seed_B, "C": seed_C}


def install(tag):
    t7b_hf.HF.seed = SEEDS[tag]


def chain_cfg(Z):
    rows = NC.load()
    return NC.cfg_from_chain(Z - 1, rows), rows


def phase_A():
    """CAN-FAIL: prove each variant actually changes the starting point. VOID if not."""
    print("PHASE A -- can-fail the seed switch (no SCF, Z=19)")
    cfg, rows = chain_cfg(19)
    out = {}
    for tag in "ABC":
        install(tag)
        h = H.HFC(19, [tuple(x) for x in cfg], c=C0)
        P, eps = h.seed(1)
        out[tag] = {f"{n}{'spdfg'[l]}": float(e) for (n, l), e in eps.items()}
        print(f"  seed {tag}: " + "  ".join(f"{k}={v:+.5f}" for k, v in out[tag].items()))
    verdict = "PASS"
    for tag in "BC":
        d = {k: out[tag][k] - out["A"][k] for k in out["A"]}
        mx = max(abs(v) for v in d.values())
        val = max(out["A"], key=lambda k: (int(k[0]), "spdfg".index(k[1])))
        print(f"  A->{tag}: max|d_eps| = {mx:.6f} Ha   valence {val} d = {d[val]:+.5f} Ha")
        if mx <= 1e-6:
            print(f"  *** VOID: seed {tag} REPRODUCES seed A. The control is vacuous (F59.3).")
            verdict = "VOID"
        if tag == "C" and abs(d[val]) <= 0.05:
            print(f"  *** VOID: seed C valence differs by only {abs(d[val]):.5f} < 0.05 Ha.")
            verdict = "VOID"
    print(f"PHASE A: {verdict}   (P1 {'holds' if verdict=='PASS' else 'FAILS -> test is VOID'})")
    json.dump(out, open("../pack61/seedA.json", "w"), indent=1)


def phase_E(Z):
    """fixed configuration, three seeds, converged total energy. P2 and P4."""
    cfg, rows = chain_cfg(Z)
    cfg = [tuple(x) for x in cfg]
    print(f"PHASE E -- Z={Z} fixed cfg {''.join(f'{n}{chr(0)}' for n,l,k in [])}"
          f"{''.join(f'{n}{"spdfg"[l]}{k:g}' for n,l,k in cfg)}")
    res = {}
    for tag in "ABC":
        install(tag)
        t0 = time.time()
        try:
            E, Ec, it, eps = H.HFC(Z, cfg, c=C0).run2()
            res[tag] = dict(E=float(E), it=it, sec=int(time.time() - t0))
            print(f"  seed {tag}: E = {E:.9f} Ha  it={it}  {res[tag]['sec']}s")
        except Exception as e:
            res[tag] = dict(E=None, err=type(e).__name__ + ": " + str(e)[:100])
            print(f"  seed {tag}: NO-DATA {res[tag]['err']}")
    if res["A"]["E"] is not None:
        for tag in "BC":
            if res[tag]["E"] is not None:
                d = res[tag]["E"] - res["A"]["E"]
                print(f"  dE(A->{tag}) = {d:+.9f} Ha = {d*1000:+.6f} mHa"
                      f"   {'<1mHa OK' if abs(d)<1e-3 else 'EXCEEDS 1 mHa'}")
    json.dump(res, open(f"../pack61/seedE{Z}.json", "w"), indent=1)


def phase_O(Z, tag):
    """one chain step under one seed. P3: entrant and full order vs the sealed row."""
    install(tag)
    cfg, rows = chain_cfg(Z)
    print(f"PHASE O -- Z={Z} seed {tag}  ref cfg {''.join(f'{n}{chr(115)}' for n,l,k in [])}")
    t0 = time.time()
    o = NC.step(Z, cfg, rows, f"seed{tag}")
    o = {k: o[k] for k in ("Z", "mode", "ent", "ent_nl", "D_ent", "margin", "order", "nfail")}
    sealed = rows[Z]
    o["sealed_ent"] = sealed["ent"]; o["sealed_margin"] = sealed["margin"]
    o["ENT_MATCH"] = (o["ent"] == sealed["ent"])
    o["ORDER_MATCH"] = ([k for k, _ in o["order"]] == [k for k, _ in sealed["order"]])
    o["dmargin"] = (None if o["margin"] is None or sealed["margin"] is None
                    else round(o["margin"] - sealed["margin"], 6))
    o["sec"] = int(time.time() - t0)
    print(f"  entrant {o['ent']} (sealed {sealed['ent']})  ENT_MATCH={o['ENT_MATCH']}"
          f"  ORDER_MATCH={o['ORDER_MATCH']}  dmargin={o['dmargin']} Ha  {o['sec']}s")
    with open(f"../pack61/seedO.jsonl", "a") as f:
        f.write(json.dumps(o) + "\n")


if __name__ == "__main__":
    a = sys.argv[1]
    if a == "A": phase_A()
    elif a == "E": phase_E(int(sys.argv[2]))
    elif a == "O": phase_O(int(sys.argv[2]), sys.argv[3])
