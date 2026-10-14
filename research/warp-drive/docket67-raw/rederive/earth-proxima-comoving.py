#!/usr/bin/env python3
"""DOCKET 67, pass S, 36/36 -- earth-proxima-comoving.

The tree (research/warp-drive/ledger.py:2033-2035, W8):
  "Earth and Proxima are comoving to about one part in 1e4, so a receiver at
   rest in Proxima's atoms automatically shares Earth's B whatever B is"

Checks, in order:
  A. NUMERIC.  Proxima's heliocentric space velocity from its astrometry
     (parallax, proper motion, radial velocity), then Earth-Proxima relative
     speed swept over Earth's orbit (circular 29.78 km/s and the eccentric
     extremes 29.29 / 30.29 km/s), plus Earth rotation and, separately, a
     receiver on Proxima b (orbital speed from a, P; orientation unknown ->
     worst-case bound).  Output: beta_rel = v_rel / c, min / max.
  B. SYMPY.  "shares Earth's B whatever B is" -- what is exactly true:
     (i)  the Doppler factor of a FIXED null direction seen from two frames
          with relative speed b differs by a factor in [e^-eta, e^+eta],
          eta = artanh(b), INDEPENDENT of the common boost B (proved);
     (ii) collinear composition B' - B = b (1 - B^2)/(1 + B b): the
          ABSOLUTE difference in B shrinks as B -> 1, but RELATIVE to B it is
          ~ b/B, i.e. NOT small when B is comparable to b (shown at the CMB
          dipole speed the tree itself names in branelink.py:74).
  C. The priced escape (branelink.b_for_saving: save = T d ((1+B)/(1-B))^2):
     fractional spread of the saving between Earth's and Proxima's B at the
     measured beta_rel, at the tree's own B values.

INPUT PROVENANCE (named, never flattened):
  parallax 768.0665 +- 0.0499 mas; pm_ra* -3781.741, pm_dec 769.465 mas/yr
    (Gaia DR3 values)            -- READ-VIA-RESTATEMENT (search-engine
                                    restatement of the Wikipedia/Gaia entry;
                                    arXiv/Gaia archive unreachable here)
  RV -22.204 +- 0.032 km/s (Kervella, Thevenin & Lovis 2017, A&A 598, L7,
    arXiv:1611.03495, HARPS absolute RV)
                                 -- READ-VIA-RESTATEMENT (same route); the
                                    tree's oneway.py:64 has 22.2 km/s RECALLED
  RA 217.42894 deg, Dec -62.67949 deg (J2000)  -- RECALLED (direction only;
    a 1-arcmin error moves nothing at the printed precision)
  Earth orbital speed 29.78 km/s mean, e = 0.0167    -- RECALLED (textbook)
  Proxima b: a = 0.0485 AU, P = 11.186 d             -- RECALLED
"""
import math
import itertools

C_KMS = 299792.458
K = 4.740470446          # km/s per (AU/yr): v_t = K * mu[arcsec/yr] / plx[arcsec]
AU_KM = 149597870.7
DAY = 86400.0

PLX_MAS = 768.0665
PMRA_MAS = -3781.741
PMDE_MAS = 769.465
RV_KMS = -22.204
RA_DEG, DE_DEG = 217.42894, -62.67949
EPS_DEG = 23.4392911     # J2000 obliquity

V_EARTH_MEAN = 29.78
E_EARTH = 0.0167
V_ROT_EQ = 0.465

A_B_AU, P_B_D = 0.0485, 11.186

def proxima_velocity_icrs(plx=PLX_MAS, pmra=PMRA_MAS, pmde=PMDE_MAS, rv=RV_KMS):
    a, d = math.radians(RA_DEG), math.radians(DE_DEG)
    vra = K * pmra / plx
    vde = K * pmde / plx
    r = (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))
    ea = (-math.sin(a), math.cos(a), 0.0)
    ed = (-math.sin(d) * math.cos(a), -math.sin(d) * math.sin(a), math.cos(d))
    return tuple(rv * r[i] + vra * ea[i] + vde * ed[i] for i in range(3))

def icrs_to_ecl(v):
    e = math.radians(EPS_DEG)
    x, y, z = v
    return (x, math.cos(e) * y + math.sin(e) * z, -math.sin(e) * y + math.cos(e) * z)

def norm(v):
    return math.sqrt(sum(t * t for t in v))

def part_A():
    vp = proxima_velocity_icrs()
    vt = K * math.hypot(PMRA_MAS, PMDE_MAS) / PLX_MAS
    vsun = norm(vp)
    print("A. Proxima heliocentric: v_t = %.3f km/s, v_r = %.3f km/s, |v| = %.3f km/s,"
          " beta = %.4e" % (vt, RV_KMS, vsun, vsun / C_KMS))
    ve = icrs_to_ecl(vp)
    lat = math.degrees(math.asin(ve[2] / vsun))
    print("   Proxima velocity ecliptic latitude %.2f deg (in-plane part %.3f km/s)"
          % (lat, math.hypot(ve[0], ve[1])))
    res = {}
    for label, speeds in (("circular", (V_EARTH_MEAN,)),
                          ("eccentric extremes", (V_EARTH_MEAN * (1 - E_EARTH), V_EARTH_MEAN * (1 + E_EARTH)))):
        lo, hi = 1e9, -1.0
        for s in speeds:
            for k in range(36000):
                th = 2 * math.pi * k / 36000
                vE = (s * math.cos(th), s * math.sin(th), 0.0)
                rel = norm(tuple(ve[i] - vE[i] for i in range(3)))
                lo, hi = min(lo, rel), max(hi, rel)
        # Earth rotation: worst case +-0.465 km/s
        lo_r, hi_r = max(lo - V_ROT_EQ, 0.0), hi + V_ROT_EQ
        res[label] = (lo_r, hi_r)
        print("   Earth-Proxima (%s, incl. rotation): %.3f .. %.3f km/s -> beta_rel %.3e .. %.3e"
              % (label, lo_r, hi_r, lo_r / C_KMS, hi_r / C_KMS))
    vb = 2 * math.pi * A_B_AU * AU_KM / (P_B_D * DAY)
    lo, hi = res["eccentric extremes"]
    print("   receiver on Proxima b: orbital speed %.2f km/s; worst-case bound"
          " beta_rel <= %.3e (orientation unknown)" % (vb, (hi + vb) / C_KMS))
    # sensitivity: RV and parallax moved by 100 sigma, and RV -> -21.7 (older values)
    for rv in (-21.7, -22.204 - 3.2, -22.204 + 3.2):
        print("   sensitivity RV=%.3f: |v_sun| = %.3f km/s" % (rv, norm(proxima_velocity_icrs(rv=rv))))
    return vsun, lo, hi, vb

def part_B():
    import sympy as sp
    b = sp.symbols('b', positive=True)
    B, mu, eta = sp.symbols('B mu eta', real=True)
    # (i) ratio of Doppler factors for fixed null k between frames u1, u2 with
    # relative speed b, in u1's rest frame: u2 = gamma_b (1, b n), k ~ (1, m),
    # mu = n.m in [-1,1]:  ratio = gamma_b (1 - b mu).  Common boost B absent.
    gam = 1 / sp.sqrt(1 - b**2)
    ratio = gam * (1 - b * mu)
    lo = sp.simplify((ratio.subs(mu, 1)**2 - sp.exp(-2*sp.atanh(b)).rewrite(sp.log)))
    hi = sp.simplify((ratio.subs(mu, -1)**2 - sp.exp(2*sp.atanh(b)).rewrite(sp.log)))
    lo_n = [float((ratio.subs(mu, 1) - sp.exp(-sp.atanh(b))).subs(b, x)) for x in (1e-4, 0.3, 0.9)]
    hi_n = [float((ratio.subs(mu, -1) - sp.exp(sp.atanh(b))).subs(b, x)) for x in (1e-4, 0.3, 0.9)]
    print("B(i) Doppler-factor ratio extremes squared minus e^{-+2eta}: symbolic %s, %s; numeric %s %s"
          % (lo, hi, lo_n, hi_n))
    # generic-frame check: explicit 4-vectors, u1 = boost(B) along x, u2 = u1 composed
    # with b in arbitrary direction, k arbitrary null.  Brute numeric over many B.
    import random
    random.seed(67)
    def boost_mat(beta_vec):
        bx, by, bz = beta_vec
        b2 = bx*bx+by*by+bz*bz
        g = 1/math.sqrt(1-b2)
        L = [[g, g*bx, g*by, g*bz]]
        for i, bi in enumerate((bx, by, bz)):
            row = [g*bi]
            for j, bj in enumerate((bx, by, bz)):
                row.append((1 if i == j else 0) + (g-1)*bi*bj/b2)
            L.append(row)
        return L
    def mv(L, v):
        return [sum(L[i][j]*v[j] for j in range(4)) for i in range(4)]
    def dot(u, k):
        return u[0]*k[0]-u[1]*k[1]-u[2]*k[2]-u[3]*k[3]
    worst = 0.0
    bmag = 1.2e-4
    for Bv in (1.23e-3, 0.5, 0.999387630, 0.99999993):
        for _ in range(2000):
            n = [random.gauss(0, 1) for _ in range(3)]; nn = norm(n); n = [t/nn for t in n]
            m = [random.gauss(0, 1) for _ in range(3)]; mm = norm(m); m = [t/mm for t in m]
            u1 = mv(boost_mat((Bv, 0, 0)), [1, 0, 0, 0])
            u2 = mv(boost_mat((Bv, 0, 0)), mv(boost_mat(tuple(bmag*t for t in n)), [1, 0, 0, 0]))
            k = [1] + m
            r = dot(u2, k) / dot(u1, k)
            worst = max(worst, abs(math.log(r)) / math.atanh(bmag))
    print("B(i) generic frames, B in {1.23e-3, 0.5, 0.999387630, 0.99999993}: max |ln ratio|/eta = %.6f (<= 1 required)" % worst)
    # (ii) collinear composition
    Bp = (B + b) / (1 + B * b)
    dB = sp.simplify(Bp - B)
    print("B(ii) collinear composition: B' - B = %s" % sp.factor(dB))
    for Bv in (1.2336e-3, 0.999387630, 0.99999993):
        d = float(dB.subs({B: Bv, b: 1.0e-4}))
        print("      B = %.10g, b = 1e-4: B'-B = %.3e, relative %.3e" % (Bv, d, d / Bv))
    return worst

def part_C(beta_rel_max):
    eta = math.atanh(beta_rel_max)
    # save ~ D^4 with D = sqrt((1+B)/(1-B)): multiplicative spread <= e^{4 eta}
    print("C. priced escape save = T d ((1+B)/(1-B))^2 = T d D^4: spread between"
          " endpoints <= e^{4 eta} - 1 = %.3e at beta_rel = %.3e (any B)"
          % (math.expm1(4 * eta), beta_rel_max))

if __name__ == "__main__":
    vsun, lo, hi, vb = part_A()
    worst = part_B()
    part_C(hi / C_KMS)
    ok = (1e-5 < lo / C_KMS) and (hi / C_KMS < 3e-4) and worst <= 1.0 + 1e-9
    print("VERDICT: beta_rel in [%.2e, %.2e] (star), <= %.2e (Proxima b); order 1e-4: %s"
          % (lo / C_KMS, hi / C_KMS, (hi + vb) / C_KMS, "YES" if ok else "NO"))
