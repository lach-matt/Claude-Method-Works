"""pb4_terms.py -- s48: scores PREDICTION-PB4-TEST (PT-1..PT-5).
Compares TWO NEUTRAL CONFIGURATIONS of the same Z on the ruling field (hfc2, SR HF, CORR=False),
each with frozen average-of-configuration orbitals from its OWN SCF, plus the Slater term
correction dE = E_open(hund_det) - E_avg from that state's own radials (same construction as
nlterm.state, reused unchanged -- no new machinery, no new constant).
    dAVG  = E_A - E_B                  (avg-of-config only)
    dTOT  = (E_A+dE_A) - (E_B+dE_B)    (with lowest terms)
    dTERM = dTOT - dAVG                (the exchange contribution, isolated)
A = the 5d-holding configuration (the walk's), B = the record's alternative.
Negative = A lower. usage: python3 pb4_terms.py 59 64   ->  appends pb4_terms.jsonl, resumable.
"""
import sys, os, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H; H.CORR = False
from t7c_kernel import C0
import ground as G
from hfterm import radial, E_open, E_avg, hund_det
from nlterm import opens, diag_sum_terms, term_label

OUT = "pb4_terms.jsonl"
XE = G.expand(54)

# A = walk's (holds 5d1), B = record's (RECALLED-NOT-ENTERED, comparison target only)
CASES = {
    59: dict(el='Pr', A=[(4, 3, 2), (5, 2, 1), (6, 0, 2)], B=[(4, 3, 3), (6, 0, 2)],
             Alab='4f2 5d1 6s2', Blab='4f3 6s2'),
    64: dict(el='Gd', A=[(4, 3, 7), (5, 2, 1), (6, 0, 2)], B=[(4, 3, 8), (6, 0, 2)],
             Alab='4f7 5d1 6s2', Blab='4f8 6s2'),
}


def state(Z, tail):
    occ = XE + list(tail)
    assert sum(q for _, _, q in occ) == Z, f"electron count {sum(q for _,_,q in occ)} != {Z}"
    h = H.HFC(Z, occ, c=C0); E, _, it, eps = h.run2()
    op = opens(occ)
    openk = [(n, l) for n, l, q in op]
    shells = [(l, int(round(q))) for n, l, q in op]
    if not shells:
        return dict(E=float(E), it=it, dE=0.0, lowest=None, hund=None)
    Fk, Gk = radial(h, openk)
    dE = E_open(shells, hund_det(shells), Fk, Gk) - E_avg(shells, Fk, Gk)
    low = None
    big = [(i, (l, N)) for i, (l, N) in enumerate(shells) if 1 < N < 2 * (2 * l + 1) - 1]
    if len(big) == 1:
        i, (l, N) = big[0]
        low = [term_label(m, L) for m, L, _ in diag_sum_terms(l, N, Fk[(i, i)])[:3]]
    return dict(E=float(E), it=it, dE=float(dE), lowest=low,
                hund=term_label(int(2 * sum(min(N, 2 * l + 1) - max(N - (2 * l + 1), 0)
                                            for l, N in shells) / 2.0) + 1,
                                int(sum(sum(list(range(l, -l - 1, -1))[:min(N, 2 * l + 1)])
                                        for l, N in shells))))


if __name__ == "__main__":
    done = {d['Z'] for d in map(json.loads, open(OUT))} if os.path.exists(OUT) else set()
    for Z in map(int, sys.argv[1:]):
        if Z in done: print("SKIP", Z); continue
        c = CASES[Z]; t0 = time.time()
        A = state(Z, c['A']); B = state(Z, c['B'])
        dAVG = A['E'] - B['E']
        dTOT = (A['E'] + A['dE']) - (B['E'] + B['dE'])
        o = dict(Z=Z, el=c['el'], Acfg=c['Alab'], Bcfg=c['Blab'],
                 E_A=round(A['E'], 6), E_B=round(B['E'], 6),
                 dE_A=round(A['dE'], 6), dE_B=round(B['dE'], 6),
                 dAVG=round(dAVG, 6), dTOT=round(dTOT, 6), dTERM=round(dTOT - dAVG, 6),
                 low_A=A['lowest'], low_B=B['lowest'], hund_A=A['hund'], hund_B=B['hund'],
                 it=[A['it'], B['it']], sec=int(time.time() - t0))
        open(OUT, "a").write(json.dumps(o) + "\n"); print(json.dumps(o), flush=True)
