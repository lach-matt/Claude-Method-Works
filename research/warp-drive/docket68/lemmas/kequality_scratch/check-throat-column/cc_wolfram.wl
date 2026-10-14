(* Evaluated through the Wolfram connector (Wolfram 15.0.1), 2026-10-09.  Output recorded in cc_wolfram.out. *)
coords = {t, r, y, th, ph};
g = DiagonalMatrix[{-a[y]^2 (1 + r^2/4), a[y]^2/(1 + r^2/4), 1, 4 b[y]^2, 4 b[y]^2 Sin[th]^2}];
gi = Inverse[g];
Gam = Table[Simplify[Sum[gi[[i, l]] (D[g[[l, j]], coords[[k]]] + D[g[[l, k]], coords[[j]]] - D[g[[j, k]], coords[[l]]]), {l, 5}]/2], {i, 5}, {j, 5}, {k, 5}];
Ric = Table[Simplify[Sum[D[Gam[[i, j, k]], coords[[i]]] - D[Gam[[i, j, i]], coords[[k]]] + Sum[Gam[[i, i, l]] Gam[[l, j, k]] - Gam[[i, k, l]] Gam[[l, j, i]], {l, 5}], {i, 5}]], {j, 5}, {k, 5}];
Rmix = Simplify[gi . Ric];
rules = {a''[y] -> (pp + p^2) A, b''[y] -> (qp + q^2) B, a'[y] -> p A, b'[y] -> q B, a[y] -> A, b[y] -> B};
eqs = {(Rmix[[1, 1]] /. rules) == -4 e^2, (Rmix[[4, 4]] /. rules) == -4 e^2};
sol = Solve[eqs, {pp, qp}][[1]];
ppE = Simplify[pp /. sol]; qpE = Simplify[qp /. sol];
Rs = Simplify[Tr[Rmix]];
Gyy = Simplify[(Rmix[[3, 3]] - Rs/2 - 6 e^2) /. rules];
{Simplify[ppE - (4 e^2 - 2 p (p + q) - 1/(4 A^2))], Simplify[qpE - (4 e^2 - 2 q (p + q) + 1/(4 B^2))],
 Simplify[Gyy /. {pp -> ppE, qp -> qpE}], Simplify[(Gyy /. {pp -> ppE, qp -> qpE})/(p^2 + q^2 + 4 p q - 6 e^2 - (-1/(2 A^2) + 1/(2 B^2))/2)],
 Simplify[(qpE - ppE) - (-2 (p + q) (q - p) + 1/(4 A^2) + 1/(4 B^2))],
 Solve[(-(x - Sqrt[x^2 - 35/36])/2) == -1/6 && x >= 1, x],
 Solve[(-(x - Sqrt[x^2 - 7/16])/2) == -1/4 && x >= 1, x],
 Solve[(k)^2 == e^2 + (-3/8)/12 && k == -e/2 && e > 0, {e, k}]}
