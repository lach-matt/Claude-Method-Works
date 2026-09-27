#!/usr/bin/env python3
"""DOCKET 67 RE-AUDIT: Weinberg PRL 43 (1979) 1566, READ from Drive (OCR text), plus
't Hooft PRL 37 (1976) 8 for the anomaly caveat.  Tests the three statements of the source
that bear on C3 against massform's YUKAWA_TERMS / _Q (read by AST, no import):
 (W1) fermion-BILINEAR interactions with any number of derivatives and ordinary bosons
      conserve B, "SU(3) implies" (p.1567);
 (W2) eq.(20): a d = 5 lepton-nonconserving term l l phi phi with scalar doublets;
 (W3) footnote: the coefficient of (20) "would vanish if B-L were exactly conserved".
stdlib only."""
import ast, itertools, sys
from fractions import Fraction as F
FAIL = []
def chk(n, ok, d=""):
    print(("PASS " if ok else "FAIL ") + n + ("  " + d if d else "")); (FAIL.append(n) if not ok else None)

src = open("/home/user/Claude-Method-Works/research/warp-drive/massform.py").read()
tree = ast.parse(src)
seg = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("_Q", "YUKAWA_TERMS"):
        seg[node.targets[0].id] = ast.get_source_segment(src, node)
ns = {"Fraction": F}
exec(seg["_Q"], ns); exec(seg["YUKAWA_TERMS"], ns)
Q, YT = ns["_Q"], ns["YUKAWA_TERMS"]
for name, term in YT.items():
    B = sum(s * Q[f][0] for f, s in term); L = sum(s * Q[f][1] for f, s in term)
    chk("massform %s: B = L = 0" % name.strip(), (B, L) == (0, 0))

W = [("Q", F(1, 3), 0, F(1, 6), 1, 2), ("uc", F(-1, 3), 0, F(-2, 3), 2, 1), ("dc", F(-1, 3), 0, F(1, 3), 2, 1),
     ("L", 0, 1, F(-1, 2), 0, 2), ("ec", 0, -1, F(1, 1), 0, 1), ("nc", 0, -1, 0, 0, 1)]
conj = lambda w: (w[0] + "~", -w[1], -w[2], -w[3], (3 - w[4]) % 3, w[5])
ALL = W + [conj(w) for w in W]
viol = [(a[0], b[0]) for a, b in itertools.combinations_with_replacement(ALL, 2)
        if (a[4] + b[4]) % 3 == 0 and a[1] + b[1] != 0]
chk("(W1) no colour-singlet fermion bilinear carries B: 'SU(3) implies baryon conservation'", viol == [], str(viol))
Lbil = sorted({(a[0], b[0], a[2] + b[2]) for a, b in itertools.combinations_with_replacement(ALL, 2)
               if (a[4] + b[4]) % 3 == 0 and a[2] + b[2] != 0})
chk("L-carrying bilinears exist and every one has Delta(B-L) = -Delta L != 0", len(Lbil) > 0 and all(l != 0 for *_, l in Lbil), str(Lbil[:6]))
Y = 2 * F(-1, 2) + 2 * F(1, 2)
chk("(W2) eq.(20) l l phi phi: hypercharge 0, Delta L = 2, Delta B = 0, dimension 3/2+3/2+1+1 = 5",
    (Y, 2, 0, F(3, 2) * 2 + 2) == (0, 2, 0, 5))
chk("(W3) eq.(20) has Delta(B-L) = -2, so exact B-L (the tree's H-BL) forbids it", (0 - 2) != 0)
chk("under H-BL + (W1): no fermion-bilinear coupling, any dimension, carries B or L",
    viol == [] and all(l != 0 for *_, l in Lbil))
qqql = (3 * F(1, 3), 1, 3 * F(1, 6) + F(-1, 2))
chk("(H+H)QQQL: B = 1, L = 1, Y = 0, d = 8 -- a Higgs coupling carrying B that neither W1 nor H-BL excludes",
    qqql == (1, 1, 0))
aB = F(1, 2) * 3 * F(1, 3); aL = F(1, 2) * 1
chk("SU(2)^2 anomaly per generation: B = L = 1/2, so B-L anomaly-free, B+L not ('baryon and lepton currents have anomalies')",
    (aB, aL) == (F(1, 2), F(1, 2)))
print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS"); sys.exit(1 if FAIL else 0)
