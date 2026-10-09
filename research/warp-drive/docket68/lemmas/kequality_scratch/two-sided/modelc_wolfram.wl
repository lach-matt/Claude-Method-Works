(* modelc_wolfram.wl -- independent cross-checks of modelc.py in Wolfram Language (run through the connector). ell_s = 1. *)
quad = (2 mu - u)^2 (1 + u/L^2) - (u^2 (1 + u) - mu u);   (* squared balance, k = 1, outer pure AdS(L) *)
w1 = Reduce[u > 0 && mu > 0 && L >= 1 && u > 2 mu && quad == 0, {u, mu, L}, Reals];        (* P2 static with L >= 1: expect False *)
w1b = Reduce[u > 0 && mu > 0 && L > 0 && u > 2 mu && quad == 0 && L == 1/2 && u == 3, {u, mu, L}, Reals]; (* control: exists at L = 1/2 *)
w2 = Reduce[u > 0 && mu > 0 && L > 0 && u < 2 mu && quad == 0 && (2 mu/u)^2 (1 + u/L^2)/u <= (1 + 1/L)^2, {u, mu, L}, Reals]; (* ours at or below critical: expect False *)
w2b = Reduce[u > 0 && mu > 0 && L > 0 && u < 2 mu && quad == 0 && (2 mu/u)^2 (1 + u/L^2)/u <= (1 + 1/L + 1/10)^2 && L == 2, {u, mu, L}, Reals]; (* control: a slightly larger cap admits solutions *)
f0[r_] := r^2 - mu/r^2;
w3 = FullSimplify[2 (2 f0[R] - R f0'[R])/(2 Sqrt[f0[R]]), R > 0 && mu > 0 && R^4 > mu];   (* flat mirrored B *)
uc = L^2/(L^2 - 1);
w4 = FullSimplify[{(2 uc/uc - 1)^2 (1 + uc/L^2) - (1 + uc - uc/uc), (2 uc/uc^(3/2)) Sqrt[1 + uc/L^2]}, L > 1]; (* RS at ell_s: expect {0, 2} *)
m2 = 4/3; lam2 = -1/2;
w5 = Select[u /. NSolve[4 m2^2 (u + u^2 - m2) == lam2^2 u^2 (u - 2 m2)^2, u, Reals, WorkingPrecision -> 40], # > 2 m2 &];
w5L = Sqrt[#/((Abs[lam2] #^(3/2)/(2 m2))^2 - 1)] & /@ w5;
fs = -1 + u + 1/(4 u); fo = -1 + u/Lo^2;
w6 = FullSimplify[{(-1 + 1/(2 u))/Sqrt[fs] + 1/Sqrt[fo], (-1/(2 u)) Sqrt[fo]/Sqrt[u]} /. u -> Lo^2/(1 - Lo^2), 1/Sqrt[3] < Lo < 1];
{w1, w1b, w2, w2b, w3, w4, N[w5, 20], N[w5L, 20], w6}
