"""D67 audit 1802.08257-pms-luminosity: what is checkable about
'late M dwarfs have long PMS phases during which the stellar luminosity can
change significantly' (MacGregor et al. 2018 sec 1), as formation.py uses it
(a present-luminosity snow-line radius is REFUSED).

The source sentence is qualitative background (cited 'e.g.' to Hawley 1997,
Shkolnik 2014, France 2016); MacGregor et al. compute nothing about it.  What
is checkable here is the Proxima-specific magnitude, from numbers READ at
source in two later papers:
  Ribas et al. 2016 (1608.06813) Table 1: M=0.123, R=0.141 Rsun, L=0.00155 Lsun,
    Teff=3050 K, a_b=0.0485 au, S_p=0.65 S_earth; sec 4.4: b entered the HZ at
    ~90 Myr (inner edge 1.5 S_earth) or ~200 Myr (0.9 S_earth), Baraffe 2015 tracks.
  Barnes et al. 2016/2018 (1608.06919) sec 3.1/4.3: pre-MS ~1 Gyr, HZ reached
    b after 169 +- 13 Myr; star 'contracts at roughly constant temperature'.
  Hayashi 1981 snow line a_ice = 2.7 (L/Lsun)^(1/2) au, as restated in
    Johnston et al. 2025 (2508.20291) sec 1 -- NAMED-NOT-READ at Hayashi.
Nothing here is a disc model; the snow-line numbers illustrate the scale of
the error a present-L radius would carry, they are not a formation radius.
"""
import sympy as sp

Tsun = 5772.0
# (1) Stefan-Boltzmann consistency of the READ present-day parameters
R, Teff, L = 0.141, 3050.0, 0.00155
L_sb = R**2 * (Teff/Tsun)**4
print(f"(1) L from R,Teff = {L_sb:.5f} Lsun vs READ {L}  ratio {L_sb/L:.4f}")
assert abs(L_sb/L - 1) < 0.02

# (2) instellation of b now: S = L / a^2 (Lsun, au -> S_earth)
a = 0.0485
S_now = L / a**2
print(f"(2) S_now = {S_now:.3f} S_earth vs READ 0.65")
assert abs(S_now - 0.65) < 0.02

# (3) HZ entry times READ imply L(t) at those epochs (orbit fixed, as Ribas assume)
for S_edge, t in ((1.5, "~90 Myr"), (0.9, "~200 Myr")):
    ratio = S_edge / S_now
    print(f"(3) inner edge {S_edge} S_earth reached at {t}: L(t)/L_now = {ratio:.3f}")
    assert ratio > 1.3
# so at >= 90 Myr -- long after disc dispersal (3-10 Myr, Ribas sec 5.1) --
# Proxima was still >= 2.3x today's luminosity; at disc epochs it was higher still.

# (4) symbolic: fully convective contraction at ~constant Teff  => L ∝ R^2;
#     irradiation-only snow line a_ice ∝ L^(1/2) ∝ R
Rs, R0, Lr = sp.symbols('R R0 L_ratio', positive=True)
Lratio = (Rs/R0)**2
a_ratio = sp.sqrt(Lratio)
assert sp.simplify(a_ratio - Rs/R0) == 0
print("(4) at fixed Teff: L_ratio = (R/R0)^2, a_ice ratio = R/R0 (sympy-verified)")

# (5) scale of the error, bracketed (radius at disc epoch is NOT read as a number;
#     Barnes 2018 Fig 1 radius axis spans 0.2-1.2 Rsun -- figure-read only).
a_now = 2.7 * L**0.5
print(f"(5) Hayashi a_ice at present L = {a_now:.3f} au")
for Rdisc in (0.3, 0.5, 0.8, 1.0, 1.2):
    lr = (Rdisc/R)**2
    print(f"    R_disc={Rdisc:.1f} Rsun: L/L_now={lr:6.1f}, a_ice={2.7*(L*lr)**0.5:.3f} au "
          f"(x{(lr)**0.5:.1f})")
# lower bound from READ numbers alone (step 3): L >= 2.31 L_now at 90 Myr
lb = 1.5/S_now
print(f"    lower bound from READ HZ timing: a_ice(disc) >= {a_now*lb**0.5:.3f} au "
      f"(x{lb**0.5:.2f}) -- even this floor exceeds the present-L radius")
assert a_now*lb**0.5 > 1.5*a_now

print("OUTCOME: luminosity change during PMS for Proxima is a factor >= 2.28 even at "
      "90 Myr from READ numbers; a present-L radius would underestimate an "
      "irradiation snow line by >= 1.5x (and by ~3-8x at disc epochs if R ~0.5-1.2 Rsun). "
      "The source's qualitative claim, applied to Proxima, is borne out.")
