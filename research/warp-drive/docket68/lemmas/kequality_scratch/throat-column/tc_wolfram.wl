(* tc_wolfram.wl -- the Wolfram cross-check of model B's column equations, as run through the Wolfram connector
   (Wolfram 15.0.1, 2026-10-09).  Independent of sympy and of sim2_facing.py.  Result recorded in tc_wolfram.out. *)
coords = {y, t, x, th, ph};
g = DiagonalMatrix[{1, -al[y]^2 x/2, al[y]^2/x^2, 4 be[y]^2, 4 be[y]^2 Sin[th]^2}];
gi = Inverse[g];
Gam = Table[(1/2) Sum[gi[[a, d]] (D[g[[d, b]], coords[[c]]] + D[g[[d, c]], coords[[b]]] - D[g[[b, c]], coords[[d]]]), {d, 5}], {a, 5}, {b, 5}, {c, 5}];
Ric = Table[Sum[D[Gam[[a, b, c]], coords[[a]]] - D[Gam[[a, b, a]], coords[[c]]] + Sum[Gam[[a, a, d]] Gam[[d, b, c]] - Gam[[a, c, d]] Gam[[d, b, a]], {d, 5}], {a, 5}], {b, 5}, {c, 5}];
mixed = Simplify[gi . Ric];
eqs = Simplify[Diagonal[mixed] + 4 e^2];
offdiag = Simplify[mixed - DiagonalMatrix[Diagonal[mixed]]];
sol = Solve[{eqs[[2]] == 0, eqs[[4]] == 0}, {al''[y], be''[y]}][[1]];
rules = {al'[y] -> p al[y], be'[y] -> q be[y]};
P = Simplify[(al''[y]/al[y] /. sol /. rules) - p^2];
Q = Simplify[(be''[y]/be[y] /. sol /. rules) - q^2];
cons = Simplify[(eqs[[1]] /. sol /. rules)];
DD = Simplify[Q - P - (-4 ((p + q)/2) (q - p) + 1/(4 al[y]^2) + 1/(4 be[y]^2))];
lemTnum = Simplify[(P + Q)/2 - (e^2 - ((p + q)/2)^2 - (q - p)^2/4)];
{offdiagZero -> (offdiag === ConstantArray[0, {5, 5}]), Pform -> P, Qform -> Q, constraint -> Expand[cons],
 Dident -> DD, xEqMinusTEq -> Simplify[eqs[[3]] - eqs[[2]]], LemmaTresidualOverConstraint -> Simplify[lemTnum/cons],
 constraintAtPlane -> Simplify[cons /. {p -> -e, q -> -e, al[y] -> 1, be[y] -> 1}]}
(* Output (2026-10-09):
   offdiagZero -> True
   Pform -> 4 e^2 - 2 p (p + q) - 1/(4 al^2)          (= sim2_facing.throat_rhs P)
   Qform -> 4 e^2 - 2 q (p + q) + 1/(4 be^2)          (= throat_rhs Q)
   constraint -> -12 e^2 + 2 p^2 + 8 p q + 2 q^2 + 1/(2 al^2) - 1/(2 be^2)   (= 2 x SIM2's coded constraint)
   Dident -> 0   (D' = -4 a D + 1/(4 al^2) + 1/(4 be^2))
   xEqMinusTEq -> 0
   Lemma T residual = (24 e^2 - 4 p^2 - 16 p q - 4 q^2 - 1/al^2 + 1/be^2)/8 = -constraint/4: zero on the constraint
   constraintAtPlane -> 0 (for every e) *)
