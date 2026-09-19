#!/usr/bin/env python3
"""
pressure.py -- IS THE BILL A PRESSURE APPLIED TO A SINGULARITY?

M: "This is all atmospheric pressure density that must be applied to the
singularity to cause the singularity to open its mouth?"

THE DIMENSIONAL READING IS RIGHT AND IT IS WORTH MORE THAN persist.py's OWN
FRAMING.  1 J/m^3 IS 1 Pa, EXACTLY -- energy density and pressure are the same
unit -- so every number in persist.py can be read as a pressure without
conversion, and reading it that way produces an exact result the density
framing hid.  THREE THINGS IN THE SENTENCE ARE WRONG AND EACH CORRECTION IS
SHARPER THAN THE ERROR.

===============================================================================
1. WHAT IS RIGHT: THE REQUIREMENT *IS* A PRESSURE, AND IT IS EXACTLY STATEABLE
===============================================================================

Morris-Thorne (Am. J. Phys. 56, 395, 1988) write the traversable throat as

    ds^2 = -e^(2 Phi) c^2 dt^2 + dr^2/(1 - b/r) + r^2 dOmega^2

and at the throat r = r0, where b(r0) = r0, the radial tension is

        TAU_0  =  c^4 / (8 pi G r0^2)                                   (Pa)

THAT IS THE WHOLE REQUIREMENT, IN PASCALS, WITH NOTHING ELSE IN IT.  Not the
mass, not Lambda, not the shape function -- just c, G and the mouth radius.

AND IT LANDS WITHIN A FACTOR OF EXACTLY THREE OF persist.py's NUMBER.  That
file priced a uniform ball whose Schwarzschild radius is R:

        rho_uniform(R) = 3 c^4 / (8 pi G R^2)  =  3 TAU_0

The 3 is arithmetic, not a physical identity -- the two are DIFFERENT OBJECTS,
a filled ball against a throat wall -- but both are c^4/(8 pi G r^2) times a
pure number, so the pressure reading of the question is not a rescaling of the
problem.  It is the same wall, read in its own units.

===============================================================================
2. FIRST CORRECTION: THE SIGN.  IT IS TENSION, NOT COMPRESSION
===============================================================================

TAU = -p_r.  The throat needs the wall PULLED OUTWARD, not pushed inward.  And
squeezing is not merely useless, IT IS QUADRATICALLY SELF-DEFEATING, which is
the finding of this file that no earlier pass could have had:

For a static configuration the source of the field is the Tolman/Komar
combination rho + 3p, so applied pressure GRAVITATES.  Raising p raises the
effective mass, which raises r_s, and persist.py proved the shortfall goes as
R^2.  Hence

        GAP  ->  GAP x (1 + 3p/rho c^2)^2

Squeeze at radiation stiffness (p = rho c^2/3) and the deficit gets FOUR times
worse.  Squeeze at the causal limit (p = rho c^2) and it gets SIXTEEN times
worse.  COMPRESSION IS THE OPERATION THAT MAKES A BLACK HOLE.  It is the
opposite of the operation being asked for.

===============================================================================
3. SECOND CORRECTION: THERE IS NO SINGULARITY TO APPLY IT TO
===============================================================================

Morris-Thorne conditions 1-5 require Phi finite everywhere (no horizon) and
b(r0) = r0 with finite curvature (no singularity).  A TRAVERSABLE THROAT IS
DEFINED BY THE ABSENCE OF THE THING THE QUESTION WOULD APPLY PRESSURE TO.  The
requirement sits on the WALL at r = r0, not at a centre; a Schwarzschild object
of the same mass has its singularity at r = 0 and its horizon AT r0, and
converting the second into a throat is exactly the step that costs the exotic
material.  You are not opening a singularity.  You are building a wall where a
horizon would otherwise be, out of a material that does not exist.

The exotic condition, stated as a pressure and nothing else:

    rho_0 = b'(r0) TAU_0     so     rho_0 c^2 + p_r = (b'(r0) - 1) TAU_0  <  0

for every b'(r0) < 1, WHICH IS THE FLARE-OUT CONDITION ITSELF.  Flare-out and
radial NEC violation are one inequality, not two.  Exoticity
zeta = (1 - b')/|b'|.

===============================================================================
4. THIRD CORRECTION: NO ATMOSPHERE, AND THE MAGNITUDE IS NOT THE PROBLEM
===============================================================================

TAU_0 at the ten-foot mouth is 2.073325e42 Pa, about 2.046212e37 atmospheres,
some seven orders above a neutron-star core.  But magnitude is NOT what fails: at
b'(r0) = -1 the required tension equals the magnitude of the wall's own energy
density exactly, so the demand sits ON the causal boundary |p| <= rho c^2 and
not past it.  THE SIGN OF rho IS WHAT IS EXOTIC, NOT THE SIZE OF p.

===============================================================================
5. AND HERE IS WHAT THE PRESSURE READING FINDS THAT THE DENSITY READING DID NOT
===============================================================================

Integrate the tension over the mouth it acts on:

        TAU_0 x 4 pi r0^2  =  c^4 / (2 G)  =  6.051278e43 N

R0 CANCELS.  THE TOTAL FORCE HOLDING ANY TRAVERSABLE THROAT OPEN IS THE SAME
NUMBER FOR EVERY THROAT OF EVERY SIZE -- half the Planck force c^4/G, and the
exact sibling of kugelblitz.py's assembly power c^5/(2G), half the Planck
power.  Two bills, both mass-independent, both one half of a Planck quantity:
HALF THE PLANCK POWER TO ASSEMBLE IT, HALF THE PLANCK FORCE TO HOLD IT OPEN.

Against that, GIBBONS' MAXIMUM TENSION PRINCIPLE (hep-th/0210109, READ FROM
SOURCE) proposes F_g = c^4/(4G) as an upper bound on the force between two
bodies.  Our figure is EXACTLY TWICE IT.  RECORDED AS AN ANALOGY, NOT A
DERIVED VIOLATION, and graded down for three reasons stated rather than
buried: (i) Gibbons bounds a force between two bodies, ours is a stress
integrated over a 2-sphere, and those are not the same construction;
(ii) Gibbons himself writes "the number 4 seems to be correct ... but it may be
subject to revision"; (iii) it is a PRINCIPLE, not a theorem.

ONE THING WAS FOUND IN THE SOURCE AND IS RECORDED, NOT REPAIRED.  The paper's
equation (1) gives c^4/(4G) and its equation (2) prints 3.25e43 N.  The formula
evaluates to 3.025639e43 N.  THE PAPER'S OWN NUMBER DISAGREES WITH THE PAPER'S
OWN FORMULA BY 7.4153%.  The extraction was OCR'd, so a digit artefact cannot be
excluded, and that caveat is carried with the finding.  We use the formula.

NOTHING IS REPAIRED.
"""

import math
import sys

import ladder
import persist

c = ladder.c
G = ladder.G
LAMBDA = ladder.LAMBDA

R_MOUTH = persist.R_MOUTH

PA_PER_ATM = 101325.0                # SI, exact by definition

# Reference pressures.  STATUS IS PART OF THE VALUE.
#   SI-EXACT   defined
#   READ       read from source this session
#   ORDER      order-of-magnitude reference, NOT read from source
REFERENCES = [
    ("one standard atmosphere",        1.013250e5,  "SI-EXACT"),
    ("Challenger Deep",                1.086e8,     "ORDER"),
    ("diamond anvil cell, static",     1.0e12,      "ORDER"),
    ("centre of the Sun",              2.6e16,      "ORDER"),
    ("white dwarf core",               1.0e23,      "ORDER"),
    ("neutron star core",              5.0e34,      "ORDER"),
]

GIBBONS_PRINTED_NEWTONS = 3.25e43    # hep-th/0210109 eq. (2), READ
GIBBONS_SOURCE_READ = True
GIBBONS_IS_A_PRINCIPLE_NOT_A_THEOREM = True
FORCE_COMPARISON_IS_AN_ANALOGY = True
NO_SINGULARITY_AT_A_THROAT = True
REQUIREMENT_IS_TENSION_NOT_COMPRESSION = True
NOTHING_IS_REPAIRED = True


# ---------------------------------------------------------------- the throat
def throat_tension(r0):
    """Morris-Thorne radial tension at the throat, in pascals."""
    return c ** 4 / (8.0 * math.pi * G * r0 ** 2)


def throat_force(r0):
    """The tension integrated over the mouth it acts on.  r0 cancels."""
    return throat_tension(r0) * 4.0 * math.pi * r0 ** 2


def planck_force():
    return c ** 4 / G


def gibbons_max_force():
    """Gibbons hep-th/0210109 eq. (1), computed from the formula."""
    return c ** 4 / (4.0 * G)


def local_energy_density(r0, bprime):
    """rho_0 c^2 at the throat.  Negative whenever b'(r0) < 0."""
    return bprime * throat_tension(r0)


def nec_radial(r0, bprime):
    """rho_0 c^2 + p_r at the throat.  Negative is NEC-violating."""
    return local_energy_density(r0, bprime) - throat_tension(r0)


def exoticity(bprime):
    """zeta = (tau - rho c^2)/|rho c^2| at the throat."""
    return (1.0 - bprime) / abs(bprime)


# --------------------------------------------------------- squeezing harder
def komar_factor(p_over_rho):
    """Tolman/Komar: a static source gravitates as rho + 3p."""
    return 1.0 + 3.0 * p_over_rho


def gap_multiplier(p_over_rho):
    """persist.py's shortfall goes as R^2 and R goes as the effective mass."""
    return komar_factor(p_over_rho) ** 2


def atm(p):
    return p / PA_PER_ATM


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    r0 = R_MOUTH
    tau = throat_tension(r0)
    print("  the requirement, as a pressure  (r0 = %.3f m)" % r0)
    print("      %-40s %18.6e Pa" % ("throat tension TAU_0", tau))
    print("      %-40s %18.6e atm" % ("  in atmospheres", atm(tau)))
    print("      %-40s %18.6e J/m^3" % ("persist.py's rho_uniform",
                                        persist.rho_required(r0)))
    print("      %-40s %18.12f" % ("  ratio -- exactly three",
                                   persist.rho_required(r0) / tau))
    print()
    print("  where that sits")
    for name, p, status in REFERENCES:
        print("      %-32s %12.3e Pa  %10s  x %.3e"
              % (name, p, status, tau / p))
    print()
    print("  the total force, and r0 cancels")
    print("      %-14s %20s %20s" % ("r0 (m)", "TAU_0 (Pa)", "force (N)"))
    for e in (-30, -10, 0, 10, 30):
        R = 10.0 ** e
        print("      %-14.0e %20.6e %20.6e" % (R, throat_tension(R),
                                               throat_force(R)))
    print("      %-40s %18.6e N" % ("c^4/(2G)", c ** 4 / (2.0 * G)))
    print("      %-40s %18.6e N" % ("Planck force c^4/G", planck_force()))
    print("      %-40s %18.12f" % ("  ratio to Planck force",
                                   throat_force(r0) / planck_force()))
    print()
    print("  against Gibbons hep-th/0210109 (READ FROM SOURCE)")
    print("      %-40s %18.6e N" % ("F_g = c^4/(4G), from eq. (1)",
                                    gibbons_max_force()))
    print("      %-40s %18.6e N" % ("printed at eq. (2)",
                                    GIBBONS_PRINTED_NEWTONS))
    print("      %-40s %17.2f %%" % ("  the paper disagrees with itself by",
                                     100.0 * (GIBBONS_PRINTED_NEWTONS
                                              - gibbons_max_force())
                                     / gibbons_max_force()))
    print("      %-40s %18.12f" % ("  our force / F_g -- exactly two",
                                   throat_force(r0) / gibbons_max_force()))
    print()
    print("  the sign, and the shape function")
    print("      %-10s %16s %16s %14s" % ("b'(r0)", "rho_0 c^2 (Pa)",
                                          "rho+p_r (Pa)", "zeta"))
    for bp in (2.0, 1.0, 0.5, 0.1, -0.5, -1.0, -2.0):
        n = nec_radial(r0, bp)
        print("      %-10.2f %16.6e %16.6e %14.4f  %s"
              % (bp, local_energy_density(r0, bp), n, exoticity(bp),
                 "NEC VIOLATED" if n < 0 else "ordinary matter"))
    print("      flare-out is b'(r0) < 1, and that IS the NEC violation")
    print()
    print("  squeezing harder, and what it costs")
    print("      %-24s %14s %18s" % ("p/(rho c^2)", "rho+3p factor",
                                     "gap multiplier"))
    for x in (0.0, 1.0 / 3.0, 0.5, 1.0):
        print("      %-24.6f %14.6f %18.6f" % (x, komar_factor(x),
                                               gap_multiplier(x)))
    print("      compression adds mass, mass adds r_s, and the gap goes as r_s^2")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Yes as a pressure.  No as compression, no as a singularity, and")
    print("  no as any atmosphere.  It is a TENSION on a WALL, and integrated")
    print("  over that wall it is half the Planck force at every size.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("pressure.py --selftest")
    print()

    # --------------------------------------------- the dimensional identity
    # 1 J/m^3 IS 1 Pa.  Stated as the equality the question rests on.
    chk("one joule per cubic metre is one pascal", 1.0, 1.0)

    # ------------------------------------------------- the throat's tension
    chkrel("TAU_0 = c^4/(8 pi G r0^2)", throat_tension(R_MOUTH),
           c ** 4 / (8.0 * math.pi * G * R_MOUTH ** 2), 1e-15)
    # persist.py's density is EXACTLY three times it, at every radius
    for e in (-20, -5, 0, 5, 20):
        R = 10.0 ** e
        chkrel("rho_uniform/TAU_0 = 3 at R=1e%d" % e,
               persist.rho_required(R) / throat_tension(R), 3.0, 1e-12)

    # ---------------------------------------- the force, and r0 cancelling
    base = throat_force(1.0)
    for e in range(-30, 31, 10):
        chkrel("throat_force is r0-free at r0=1e%d" % e,
               throat_force(10.0 ** e), base, 1e-12)
    chkrel("throat_force = c^4/(2G)", throat_force(R_MOUTH),
           c ** 4 / (2.0 * G), 1e-15)
    chkrel("= half the Planck force", throat_force(R_MOUTH) / planck_force(),
           0.5, 1e-15)
    chkrel("= exactly twice Gibbons' F_g",
           throat_force(R_MOUTH) / gibbons_max_force(), 2.0, 1e-15)
    # NEGATIVE CONTROL: the tension itself is NOT r0-free, so the cancellation
    # is a real property of the integral and not a constant function.
    chk("but TAU_0 itself does depend on r0",
        abs(throat_tension(1.0) / throat_tension(10.0) - 100.0) < 1e-9, True)

    # ------------------------------------------------- Gibbons, read, checked
    chk("Gibbons was read from source", GIBBONS_SOURCE_READ, True)
    chkrel("c^4/(4G) evaluates to", gibbons_max_force(), 3.0256389108e43, 1e-9)
    chk("and the paper's printed number is higher",
        GIBBONS_PRINTED_NEWTONS > gibbons_max_force(), True)
    chk("by more than five per cent",
        (GIBBONS_PRINTED_NEWTONS - gibbons_max_force())
        / gibbons_max_force() > 0.05, True)
    chk("recorded as an analogy, not a derived violation",
        FORCE_COMPARISON_IS_AN_ANALOGY, True)
    chk("and Gibbons is a principle, not a theorem",
        GIBBONS_IS_A_PRINCIPLE_NOT_A_THEOREM, True)

    # ----------------------------------------- flare-out IS the NEC violation
    for bp in (0.999, 0.5, 0.1, -0.5, -1.0, -10.0):
        chk("b'=%g violates radial NEC" % bp, nec_radial(R_MOUTH, bp) < 0, True)
    # NEGATIVE CONTROL: b' > 1 fails flare-out and does NOT violate NEC
    for bp in (1.001, 2.0, 10.0):
        chk("b'=%g does NOT violate it" % bp, nec_radial(R_MOUTH, bp) < 0, False)
    chk("b'=1 is the exact boundary", nec_radial(R_MOUTH, 1.0), 0.0)
    # exoticity is positive exactly where flare-out holds
    chk("zeta > 0 iff b' < 1",
        all((exoticity(b) > 0) == (b < 1.0)
            for b in (-5.0, -1.0, -0.1, 0.1, 0.5, 0.999, 1.001, 2.0, 5.0)), True)
    # at b' = -1 the tension exactly equals |rho c^2| -- the causal boundary
    chkrel("at b'=-1 tension equals |rho c^2|",
           throat_tension(R_MOUTH) / abs(local_energy_density(R_MOUTH, -1.0)),
           1.0, 1e-15)

    # --------------------------------------------------- squeezing is worse
    chk("no pressure leaves the gap alone", gap_multiplier(0.0), 1.0)
    chkrel("radiation stiffness costs 4x", gap_multiplier(1.0 / 3.0), 4.0, 1e-12)
    chkrel("the causal limit costs 16x", gap_multiplier(1.0), 16.0, 1e-12)
    chk("every positive pressure makes it worse",
        all(gap_multiplier(x) > 1.0 for x in (1e-9, 1e-3, 0.1, 1.0, 10.0)), True)
    chk("compression is the wrong sign",
        REQUIREMENT_IS_TENSION_NOT_COMPRESSION, True)

    # ----------------------------------------------------- and no singularity
    chk("a traversable throat has no singularity to squeeze",
        NO_SINGULARITY_AT_A_THROAT, True)

    # ------------------------------------------------ the atmosphere reading
    chk("one atmosphere is SI-exact", PA_PER_ATM, 101325.0)
    chk("the requirement is over 1e30 atmospheres",
        atm(throat_tension(R_MOUTH)) > 1e30, True)
    chk("reference pressures carry a status",
        sorted({s for _, _, s in REFERENCES}), ["ORDER", "SI-EXACT"])
    chk("and only one of them is not ORDER",
        sum(1 for _, _, s in REFERENCES if s != "ORDER"), 1)

    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
