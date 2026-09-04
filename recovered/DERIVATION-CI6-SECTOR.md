# DERIVATION — WHICH DETERMINANTS CI-6 MUST USE. Session 73, R 1968.
# FILED BEFORE ci2.py EXISTS AND BEFORE ANY NUMBER BEARING ON CI-6 IS READ.
# Reached by READING hfterm.hund_det and the two configurations. Nothing computed.

## 1 · THE LITERAL READING OF R-C(a) IS A GUARANTEED ZERO, FOR A NON-PHYSICAL REASON
R-C(a) says: V between "the two highest-weight determinants hfterm.hund_det already builds".
hund_det builds MAX-S-THEN-MAX-L. At both named rows those two determinants sit in
DIFFERENT M_S sectors:

    Cr 24   A = 3d5 4s1   hund_det -> six parallel spins, M_S = 3
            B = 3d4 4s2   hund_det -> M_S = 2
    Cu 29   A = 3d10 4s1  M_S = 1/2, M_L = 0
            B = 3d9  4s2  hund_det -> M_S = 1/2, M_L = 2

H commutes with S_z and L_z. A matrix element between different M_S (Cr) or different M_L
(Cu) is zero IDENTICALLY, and says nothing whatever about configuration mixing.
**Running R-C(a) literally would return V = 0 at both rows and would score CI-6 FAILED.
That would be a FALSE NULL of exactly the F72.1 / F72.2 shape: a negative produced by the
instrument's own framing rather than by the physics.** It is refused here, before it is run.

## 2 · THE CORRECT DETERMINANT-LEVEL OBJECT — STILL (a), NO RECOUPLING
Take the MAXIMAL COMMON (M_L, M_S) sector. At both rows the pair is forced and unique:

    common set C = the 10 (Cu) / 5 (Cr) spin-orbitals shared
    A = C + 3d(m=0, spin down)
    B = C + 4s(m=0, spin down)

    Cr   C = { 3d(2,u), 3d(1,u), 3d(0,u), 3d(-1,u), 4s(0,u) }      M_L = 2, M_S = 2
    Cu   C = { 3d9 with the hole at (m=0, down) , 4s(0,u) }        M_L = 0, M_S = 1/2

Both rows reduce to the SAME replacement: 3d(m=0, down) -> 4s(m=0, down). Same spin, same
M_L, same M_S, differing by exactly one spin-orbital. Slater-Condon single replacement
applies, S = I stands, and NO CG recoupling is used. This is (a), not (b).

## 3 · TWO EXACT SYMMETRY STATEMENTS, DERIVED, TO BE TESTED AGAINST THE INSTRUMENT
**(3a) Cu is an EXACT ZERO.** A = closed 3d10 + 4s(up) is PURE 2S. B at M_L=0 is a d9 hole
at m=0 with 4s2, and d9 carries only 2D, so B is PURE 2D. H is a scalar: <2S|H|2D> = 0
exactly. **The instrument MUST return zero at Cu. If it returns nonzero, the instrument is
wrong, not the physics.** This is a control with a known answer and is used as such.

**(3b) Cr's GROUND TERMS DO NOT MIX EITHER.** Cr's actual ground term is 3d5 4s1 7S; the
Madelung configuration's ground term is 3d4 4s2 5D. Different L AND different S: exactly
zero. The nonzero Cr element measured in §2 connects B's 5D to an EXCITED 5D of 3d5 4s1,
NOT to Cr's 7S ground state.

## 4 · WHAT THIS MEANS FOR WHAT CI-6 CAN DECIDE — STATED BEFORE THE NUMBER
A nonzero V at Cr lowers a root of the 5D pair. It CANNOT lower Cr's 7S ground state,
because 7S has no partner in the other configuration. **Therefore the 2x2, at the ground
terms, cannot move the Cr row in favour of the observed configuration by construction.**
Whether it moves the row at all is what the number decides. Both directions remain open and
neither is asserted here.

## 5 · TIMING
No radial integral has been evaluated. ci2.py does not exist. pack71/ci2a.json holds
ZERO/NONZERO flags only and carries no magnitude. Nothing above was reached from a number.