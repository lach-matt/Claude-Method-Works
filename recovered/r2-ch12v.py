# r2-ch12v.py — Phase R2, main §12.11.1.3 (L3233–3268), chat 77.
# L3239–3244 the five-row table: Λ₈ 0 of 976 (four source coordinates against three target, L3261), Λ₉ 1,169 of 1,654 = 0.707,
# the violation index 2,370 / 1,410 = 0.595 (record-carried from the companion's threshold table — Transitions.md L554–559 and
# IoI L110–117 — with Register 620's differencing re-done as arithmetic); L3261–3264 the jump 0 → 70.7 against the heading
# "The twenty-point jump" and the withdrawn 50.3 % (Register 625: the three-against-three convenience signature).
# build9/src/tgt from r2lib (r2-ch12f, chat 73); tower-2.py by path via r2lib. Deterministic.
import importlib.util, os
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

L8, L9 = T.L8(), T.L9()
# Λ₈ on the book's own signatures: source (n, ℓ, k, 2S) — four coordinates — against target (e, f, g) — three
src8 = {(c[0], c[1], c[2], c[7]) for c in L8}; tgt8 = [(c[4], c[5], c[6]) for c in L8]
comp8 = sum(1 for t in tgt8 if t in src8)
print(f'== L3240/L3261 Λ₈: cells {len(L8):,} | composable under source (n,ℓ,k,2S) against target (e,f,g) — four against three — {comp8} of {len(L8):,} = {comp8/len(L8):.3f} (printed 0, 0.000)')
# the withdrawn convenience signature (Register 625: three against three)
src3 = {(c[0], c[1], c[2]) for c in L8}
comp3 = sum(1 for c in L8 if (c[4], c[5], c[6]) in src3)
print(f'   the three-against-three convenience signature (n,ℓ,k) against (e,f,g): {comp3:,} of {len(L8):,} = {100*comp3/len(L8):.1f}% — the withdrawn 50.3 % (L3264, Register 625) {"reproduces" if round(100*comp3/len(L8),1)==50.3 else "does NOT reproduce"}')
# Λ₉
srcs = {r2lib.src(c) for c in L9}; comp9 = sum(1 for c in L9 if r2lib.tgt(c) in srcs)
print(f'== L3241/L3262 Λ₉: cells {len(L9):,} | composable {comp9:,} | fraction {comp9/len(L9):.4f} → prints 0.707 {round(comp9/len(L9),3)==0.707} and 70.7% {round(100*comp9/len(L9),1)==70.7}')
# the violation index row — record-carried from the companion's threshold table (Transitions.md L554–559; IoI L110–117)
TT = [('classical black hole', 'none', 2370, 1410), ('Hawking-evaporating', 'NEC>=1', 2196, 1410), ('Planck-scale wormhole', 'NEC>=2', 1764, 1134), ('macroscopic wormhole', 'NEC>=3', 1146, 738), ('universal horizon', 'X>=2', 1374, 840), ('time machine', 'X=3', 558, 360)]
c0, r0 = TT[0][2], TT[0][3]
print(f'== L3242 the violation index (record-carried): {c0:,} cells, {r0:,} reachable, fraction {r0/c0:.4f} → prints 0.595 {round(r0/c0,3)==0.595}')
d = [(TT[i][2]-TT[i+1][2], TT[i][3]-TT[i+1][3]) for i in range(3)]
print(f'   Register 620 differencing: NEC=0 {d[0][0]} cells, reachable drop {d[0][1]} (all unreachable {d[0][1]==0}) | NEC=1 {d[1][0]}, drop {d[1][1]} = {100*d[1][1]/d[1][0]:.1f}% reachable | NEC=2 {d[2][0]}, drop {d[2][1]} = {100*d[2][1]/d[2][0]:.1f}% | NEC>=3 {TT[3][2]:,} | sum {d[0][0]+d[1][0]+d[2][0]+TT[3][2]:,} = 2,370 {d[0][0]+d[1][0]+d[2][0]+TT[3][2]==2370}')
# L3261 the heading against its own paragraph
print(f'== L3261 "The twenty-point jump": 0 → 70.7 is {comp9/len(L9)*100:.1f} points ("the whole distance from nothing to seven-tenths", L3263–3264); 50.3 → 70.7 is {100*comp9/len(L9)-50.3:.1f} points — the twenty is the withdrawn computation\'s jump, not the printed one')
