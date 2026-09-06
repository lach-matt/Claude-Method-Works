# r2-ch12u.py — Phase R2, main §12.11.1.2 (L3205–3232), chat 77.
# L3212–3220: "Build Λ₉ at a caps tuple, keep the cells whose target is a legal source, and count those with g = q" — the four
# printed rows (caps, |Λ₉|, composable, conservative, share) re-measured on every Λ₉ cell at each cap by r2lib.analyse
# (build9/src/tgt lifted from r2-ch12f, chat 73) and by a direct count here; the same rows read against §12.11.0.1's table
# (L2593–2597: |Λ₉|, objects, edges, conservative over every cell); L3206–3208 the two denominators at the book's caps;
# L3222–3230 the movement of both shares. tower-2.py by path via r2lib (Λ₉ control at the book's caps). Deterministic.
import importlib.util, os
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

ROWS = [((3, 3, 1, 3, 1), 1654, 1169, 739, 63.2), ((4, 4, 1, 6, 1), 19433, 16150, 5986, 37.1), ((4, 4, 2, 6, 2), 44153, 37430, 14114, 37.7), ((5, 5, 2, 6, 2), 83543, 71087, 26921, 37.9)]
SEC0 = {(3, 3, 1, 3, 1): (33, 739, 904, 54.7), (4, 4, 1, 6, 1): (101, 5986, 6693, 34.4), (4, 4, 2, 6, 2): (155, 14114, 15509, 35.1), (5, 5, 2, 6, 2): (214, 26921, 29489, 35.3)}   # §12.11.0.1 L2594–2597: objects, edges, conservative (all cells), %

L9 = T.L9(); c9 = r2lib.build9((3, 3, 1, 3, 1))
print(f'== control (3,3,1,3,1): tower Λ9 {len(L9):,} = build9 {len(c9):,} {len(L9)==len(c9)}, same cell set {set(L9)==set(c9)}')
def direct(caps):
    cells = r2lib.build9(caps); O = {r2lib.src(c) for c in cells}
    comp = [c for c in cells if r2lib.tgt(c) in O]
    cons_comp = sum(1 for c in comp if c[6] == c[3]); cons_all = sum(1 for c in cells if c[6] == c[3])
    edges = len({(r2lib.src(c), r2lib.tgt(c)) for c in comp})
    return len(cells), len(O), len(comp), cons_comp, cons_all, edges
print('== L3216–3220 caps | |Λ9| | composable (target ∈ objects) | conservative (g = q) among composable | share | printed | and §12.11.0.1\'s row (objects, edges, conservative over every cell)')
for caps, p9, pcomp, pcons, pshare in ROWS:
    n9, nobj, ncomp, cc, ca, ne = direct(caps); share = 100 * cc / ncomp
    ok = lambda a, b: 'OK' if a == b else f'MISMATCH (printed {b:,})'
    print(f'   {caps}: |Λ9| {n9:,} {ok(n9, p9)} | composable {ncomp:,} {ok(ncomp, pcomp)} | conservative among composable {cc:,} {ok(cc, pcons)} | share {share:.1f} (printed {pshare}: {"OK" if round(share,1)==pshare else "MISMATCH"}) | printed conservative {pcons:,} / composable = {100*pcons/ncomp:.1f}')
    o0, e0, c0, s0 = SEC0[caps]
    print(f'      §12.11.0.1: objects {nobj} (printed {o0}) | edges {ne:,} (printed {e0:,}) | conservative over every cell {ca:,} = {100*ca/n9:.1f}% (printed {c0:,}, {s0}%) | the printed conservative-among-composable {pcons:,} equals the edge count {pcons == ne}, equals the measured count {pcons == cc}')
print('== r2lib.analyse at the four caps (the lifted instrument\'s own lines):')
for caps, *_ in ROWS: r2lib.analyse(caps)
# L3222–3230 the movement of both shares
D = {caps: direct(caps) for caps, *_ in ROWS}
sh = [100 * D[c][3] / D[c][2] for c, *_ in ROWS]; al = [100 * D[c][4] / D[c][0] for c, *_ in ROWS]
print(f'== L3222–3230 the composable share by caps {[round(x, 1) for x in sh]} (printed 63.2 / 37.1 / 37.7 / 37.9) | the all-cells share {[round(x, 1) for x in al]} (L3223–3224: 54.7 then 34–35) | "nearly halves" composable {sh[1]/sh[0]:.2f}, all cells {al[1]/al[0]:.2f} | "moves by less than a point" over rows 2–4: composable {max(sh[1:])-min(sh[1:]):.1f} points, all cells {max(al[1:])-min(al[1:]):.1f} | "fiftyfold growth in cells" Λ9 {D[ROWS[3][0]][0]/D[ROWS[0][0]][0]:.1f}×, composable {D[ROWS[3][0]][2]/D[ROWS[0][0]][2]:.1f}× | "three cells in eight" = 37.5 | "overstate it by two thirds" 63.2/37.9 = {63.2/37.9:.2f}, 63.2/37.5 = {63.2/37.5:.2f}')
print(f'   row 2 (4,4,1,6,1) has ℓ_max = 1 — no d shell (L3226 "Once the d shell is open the share sits at 37–38%"); the d shell enters at row 3')
