(* Wolfram 15.0.1 (connector) cross-check, reading ell_ref = ell_1, ours at RS(ell_1), units ell_s = 1.
   Run 1: FindRoot on the 4 unsquared equations (L1, mu, u1, u2) for (c=4/3, ratio -1/8) and (c=1, ratio -1/4).
   Run 2: NSolve over Reals of the polynomialised system in (x, y, v=1/L1), v>1, x>0, 0<y<1, then admissibility
          (u1,u2,mu>0, f_s>0) and unsquared residuals.  See chk_wolfram.out for the returned values. *)
fs[u_, m_] := 1 + u - m/u; fo[u_, L_] := 1 + u/L^2;
res[c_, r_, L_, mm_, uu1_, uu2_] := {(2/L) Sqrt[uu1] - (Sqrt[fs[uu1, mm]] + Sqrt[fo[uu1, L]]),
   (1 - 2 mm/uu1)/Sqrt[fs[uu1, mm]] + 1/Sqrt[fo[uu1, L]],
   (r 2/L) Sqrt[uu2] - (Sqrt[fs[uu2, mm]] - Sqrt[fo[uu2, c L]]),
   (1 - 2 mm/uu2)/Sqrt[fs[uu2, mm]] - 1/Sqrt[fo[uu2, c L]]};
poly[c_, r_] := Module[{v2 = v/c, lam1 = 2 v, u1x, u2y},
   u1x = (1 + x)^2/(lam1^2 - (1 + x)^2 v^2);
   u2y = (2 y + 1) (y - 1)/(2 (1 - y^2 v2^2));
   {v^2 x^2 + (2 - 2 lam1^2) x + 2 - v^2 + lam1^2 == 0,
    (1 - y) (v2^2 (1 + y) - 2) == (r lam1)^2 (2 y + 1),
    Numerator[Together[u1x (1 + x)/2 - u2y (1 - y)/2]] == 0}];
check[c_, r_] := Module[{sol, rows},
   sol = NSolve[Join[poly[c, r], {v > 1, x > 0, 0 < y < 1}], {x, y, v}, Reals, WorkingPrecision -> 30];
   rows = Map[Module[{vv = v /. #, xx = x /. #, yy = y /. #, L, uu1, mm, uu2, rr},
       L = 1/vv; uu1 = (1 + xx)^2/((2 vv)^2 - (1 + xx)^2 vv^2); mm = uu1 (1 + xx)/2;
       uu2 = (2 yy + 1) (yy - 1)/(2 (1 - yy^2 (vv/c)^2));
       rr = If[uu1 > 0 && uu2 > 0 && mm > 0 && fs[uu1, mm] > 0 && fs[uu2, mm] > 0, Max[Abs[N[res[c, r, L, mm, uu1, uu2], 20]]], "inadmissible"];
       {N[L, 12], N[mm, 12], rr}] &, sol];
   {c, r, Length[sol], rows}];
Table[check[c, r], {c, {1, 4/3, 3, 6}}, {r, {-1/4, -1/8}}]
