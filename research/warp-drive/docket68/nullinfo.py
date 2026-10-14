# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  M: "Null (NEC) is a containment. This is where information
# lives, and is quantifiable."  Two results the board audited (D67) tie null surfaces to information:
#   (1) Bousso's covariant entropy bound, hep-th/9905177 p.9-10 (READ; D67 NARROWED): entropy on a light-sheet L of a
#       surface B (a NULL hypersurface with non-positive expansion) obeys S <= A(B)/4 (hbar = c = G = k = 1).
#   (2) The QNEC, Bousso-Fisher-Leichenauer-Wall 1509.02542 (READ; D67 NARROWED): <T_kk(p)> >= (hbar/2pi) S''_out/A,
#       proven for free / superrenormalizable bosonic fields, on STATIONARY null surfaces of FIXED backgrounds with no
#       dynamical gravity, where the expansion and shear vanish at p.
import sympy as sp, math
G, hbar, c, r0, bp = sp.symbols('G hbar c r_0 bprime', positive=True)
lP2 = hbar*G/c**3
# (1) the cap, in bits, on a light-sheet of area A
A = sp.symbols('A', positive=True)
bits_per_area = 1/(4*lP2*sp.log(2))
lP = 1.616255e-35
print(f"(1) light-sheet cap: A/(4 l_P^2 ln 2) = {1/(4*lP**2*math.log(2)):.4e} bits per square metre")
# (2) Morris-Thorne throat, Phi = 0 (Lobo 0710.4474 eqs 26-28; D67 STANDS): rho + p_r at r0 = (b'(r0) - 1)/(8 pi r0^2)
#     in geometric units; restore SI energy density by c^4/G.  QNEC then requires S''_out/A <= (2 pi/(hbar c)) T_kk.
Tkk_SI = (bp - 1)/(8*sp.pi*r0**2) * c**4/G
req = sp.simplify(2*sp.pi/(hbar*c) * Tkk_SI)
print("(2) QNEC at a Morris-Thorne throat requires  S''_out/A  <=", req, " nats per m^4")
print("    = -(1 - b'(r0)) / r0^2  x  (1/(4 l_P^2)):", sp.simplify(req - (-(1 - bp)/r0**2 * 1/(4*lP2))) == 0)
print(f"    numerically, b'(r0) = 0, r0 = 1 m: S''_out/A <= {-(1/(4*lP**2))/math.log(2):.4e} bits per m^2 per m^2")
