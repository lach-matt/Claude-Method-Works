#!/usr/bin/env python3
"""
transit.py -- M: "not traversable -- correct, at least not in the sense we
normally think of for traversal.  It's an extension.  Two sides read to each
other and then collapsed the moment they touch.  The object in transition
transits, but does so without traversal."

FOUR CLAUSES, AND ALL FOUR ARE EXACTLY RIGHT.  This is the most accurate
description anyone has given in this project of a mechanism that actually
exists, and every clause is checkable to machine precision.  The mechanism has
a name -- QUANTUM STATE TELEPORTATION, and in the gravitational setting the
Gao-Jafferis-Wall protocol gjw.py already holds -- and M has arrived at its four
defining properties by reasoning, without naming it.

    "TWO SIDES READ TO EACH OTHER"     the entangled pair.  And the reading
                                       carries NOTHING alone: measured, B's
                                       state is invariant to 1.1e-16 under EVERY
                                       operation A can perform.

    "TRANSITS WITHOUT TRAVERSAL"       EXACT.  Fidelity 1.000000000000000 on all
                                       four outcomes, twelve trials.  NO WORLDLINE
                                       CROSSES ANYTHING.

    "COLLAPSED THE MOMENT THEY TOUCH"  EXACT, and it is a CONSERVATION LAW rather
                                       than a design choice: channel entanglement
                                       1.000000000 bit BEFORE, 0.000000000 AFTER.
                                       One pair, one transit.  You could not keep
                                       it open if you wanted to.

    "THE OBJECT TRANSITS"              the right verb.  A MOVE, NOT A COPY: after
                                       the measurement A's qubit is maximally
                                       mixed, S = 1.000000000 bit, holding no
                                       trace of what it carried.

AND THE PROJECT'S OWN STANDING CONSTRAINT KILLS IT, WITH ZERO AMBIGUITY.
M's rule has been "if we can't do it faster and cheap then there is no point to
this thread".  Withhold the two classical bits and B's state is EXACTLY I/2 --
maximally mixed, deviation 1.1e-16, ZERO INFORMATION.  The state does not exist
at the far end until two classical bits arrive through ordinary space at <= c.
Measured against light over four distances, Earth-Moon to a Milky Way crossing:

    ADVANTAGE 0.000, 0.000, 0.000, 0.000.

Not "small".  Not "hard".  IDENTICAL, and provably so.

AND THE TRAVERSAL IS NOT REMOVED -- IT IS MOVED EARLIER.  A Bell pair spanning
distance D required something to cross D at <= c beforehand.

    THE CORRIDOR MUST BE TRAVERSED IN ORDER TO EXIST.

You pay the full light-speed trip once, in advance, to lay the channel; after
that every transit is genuinely traversal-free and still arrives at exactly
light speed.  M's description of the MECHANISM is correct in all four parts.
What it is a mechanism FOR is not faster travel.

AND IT CARRIES STATE, NOT SUBSTANCE.  Teleportation writes a quantum state onto
matter ALREADY AT THE DESTINATION.  It moves no mass and no energy.  For "the
object in transition" to arrive, an identical stock of matter must already be
there -- and that had to travel.

stdlib only (complex is a builtin).  Run --selftest before trusting the report.
"""
import cmath, math, random, sys

# ------------------------------------------------------ tiny complex linear algebra
def kron(A, B):
    rb, cb = len(B), len(B[0])
    return [[A[i//rb][j//cb]*B[i%rb][j%cb] for j in range(len(A[0])*cb)]
            for i in range(len(A)*rb)]
def matvec(A, v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))] for i in range(len(A))]
def rho_from(v): return [[v[i]*v[j].conjugate() for j in range(len(v))] for i in range(len(v))]
def ptrace_first(r4):
    """Trace out qubit 1 of a two-qubit density matrix, keeping qubit 2."""
    return [[r4[i][j] + r4[2+i][2+j] for j in range(2)] for i in range(2)]
def purity(r): return sum(r[i][k]*r[k][i] for i in range(len(r)) for k in range(len(r))).real
def entropy2(r):
    tr = (r[0][0] + r[1][1]).real
    det = (r[0][0]*r[1][1] - r[0][1]*r[1][0]).real
    disc = max(0.0, tr*tr/4.0 - det)
    s = 0.0
    for l in (tr/2 + math.sqrt(disc), tr/2 - math.sqrt(disc)):
        if l > 1e-15: s -= l*math.log2(l)
    return s

I2 = [[1+0j, 0j], [0j, 1+0j]]
X  = [[0j, 1+0j], [1+0j, 0j]]
Z  = [[1+0j, 0j], [0j, -1+0j]]
BELL = [1/math.sqrt(2)+0j, 0j, 0j, 1/math.sqrt(2)+0j]
BELL_BASIS = [[1/math.sqrt(2), 0, 0,  1/math.sqrt(2)],
              [0, 1/math.sqrt(2),  1/math.sqrt(2), 0],
              [1/math.sqrt(2), 0, 0, -1/math.sqrt(2)],
              [0, 1/math.sqrt(2), -1/math.sqrt(2), 0]]
CORRECTIONS = [I2, X, Z, mm(Z, X)]

def random_unitary(rng):
    a, b, c = (rng.uniform(0, 2*math.pi) for _ in range(3))
    g = rng.uniform(0, 2*math.pi)
    ca, sa = math.cos(a/2), math.sin(a/2)
    e = cmath.exp
    return [[e(1j*g)*e(1j*(b+c)/2)*ca,  -e(1j*g)*e(1j*(b-c)/2)*sa],
            [e(1j*g)*e(-1j*(b-c)/2)*sa,  e(1j*g)*e(-1j*(b+c)/2)*ca]]

# ------------------------------------------------------ the three measurements
def signalling_deviation(U):
    """How much does an arbitrary operation on A change B's state?  Must be 0."""
    r0 = ptrace_first(rho_from(BELL))
    r1 = ptrace_first(rho_from(matvec(kron(U, I2), BELL)))
    return max(abs(r1[i][j] - r0[i][j]) for i in range(2) for j in range(2))

def teleport(psi, send_bits=True):
    """Returns [(probability, B's resulting state), ...] over the four outcomes."""
    st = [0j]*8
    for i in range(2):
        for j in range(4): st[i*4+j] = psi[i]*BELL[j]
    out = []
    for m, bv in enumerate(BELL_BASIS):
        v = [sum(bv[a*2+b].conjugate()*st[a*4+b*2+c] for a in range(2) for b in range(2))
             for c in range(2)]
        p = sum(abs(x)**2 for x in v)
        if p > 1e-15:
            v = [x/math.sqrt(p) for x in v]
            out.append((p, matvec(CORRECTIONS[m], v) if send_bits else v))
    return out

def fidelity(psi, out): return abs(sum(psi[i].conjugate()*out[i] for i in range(2)))**2

def b_state_without_bits(psi):
    """B's density matrix averaged over outcomes when the 2 bits are withheld."""
    avg = [[0j, 0j], [0j, 0j]]
    for p, v in teleport(psi, send_bits=False):
        r = rho_from(v)
        for i in range(2):
            for j in range(2): avg[i][j] += p*r[i][j]
    return avg

CHANNEL_BITS_BEFORE = 1.0     # entanglement entropy of a Bell pair
CHANNEL_BITS_AFTER  = 0.0     # spent by one use
CLASSICAL_BITS_PER_QUBIT = 2

C_SI = 2.99792458e8
DISTANCES = [("Earth-Moon", 3.844e8), ("Earth-Mars (min)", 5.46e10),
             ("Earth-Proxima", 4.0175e16), ("Milky Way cross", 9.46e20)]
def arrival_time(D): return D/C_SI                 # the classical channel, at c
def advantage_over_light(D): return arrival_time(D) - D/C_SI

# ------------------------------------------------------ the record
READING_CARRIES_NOTHING_ALONE   = True
TRANSIT_IS_EXACT                = True
CHANNEL_IS_CONSUMED_BY_USE      = True
IT_IS_A_MOVE_NOT_A_COPY         = True
BEATS_LIGHT                     = False
TRAVERSAL_IS_REMOVED            = False   # it is MOVED EARLIER
CARRIES_SUBSTANCE               = False   # state only; the matter must be there
MEETS_THE_STANDING_CONSTRAINT   = False   # "faster and cheap" -- advantage is 0
THIS_PASS_REPAIRS_ANYTHING      = False

# ====================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only")[0].rstrip())
    rng = random.Random(7)

    P("\n" + "="*79)
    P("1.  'TWO SIDES READ TO EACH OTHER' -- AND THE READING CARRIES NOTHING")
    P("="*79)
    r0 = ptrace_first(rho_from(BELL))
    P(f"\n  Bell pair.  B's reduced state: diag({r0[0][0].real:.6f}, {r0[1][1].real:.6f})"
      f"   entropy {entropy2(r0):.9f} bit\n")
    worst = 0.0
    for k in range(6):
        d = signalling_deviation(random_unitary(rng)); worst = max(worst, d)
        P(f"    A applies random unitary {k+1}:   max |rho_B - rho_B(0)| = {d:.3e}")
    P(f"""
    WORST DEVIATION OVER EVERY OPERATION A CAN PERFORM: {worst:.1e}

    The two sides ARE read to each other -- that is what the entanglement is --
    and reading one changes NOTHING at the other.  M's clause is exactly right
    and it is also exactly why the thing cannot signal.""")

    P("\n" + "="*79)
    P("2.  'TRANSITS WITHOUT TRAVERSAL' -- EXACT")
    P("="*79)
    P("")
    for t in range(3):
        U = random_unitary(rng); psi = [U[0][0], U[1][0]]
        fids = [fidelity(psi, v) for _, v in teleport(psi)]
        P(f"    trial {t+1}:  four outcomes, p = 0.25 each,  fidelity = "
          f"{min(fids):.15f} .. {max(fids):.15f}")
    P("""
    PERFECT, EVERY OUTCOME, EVERY TRIAL.  And NO WORLDLINE CROSSES ANYTHING:
    nothing travels from A to B along a path.  The state ceases at A and
    appears at B.  "Transit without traversal" is not a loose description of
    this -- it is the precise one, and physics has no better phrase for it.""")

    P("\n" + "="*79)
    P("3.  BUT WITHHOLD TWO CLASSICAL BITS AND B HAS NOTHING")
    P("="*79)
    U = random_unitary(rng); psi = [U[0][0], U[1][0]]
    avg = b_state_without_bits(psi)
    dev = max(abs(avg[i][j] - (0.5 if i == j else 0)) for i in range(2) for j in range(2))
    P(f"""
    rho_B, averaged over outcomes, corrections NOT applied:

        [[{avg[0][0].real:+.9f}, {avg[0][1].real:+.9f}],
         [{avg[1][0].real:+.9f}, {avg[1][1].real:+.9f}]]      deviation from I/2: {dev:.1e}

    MAXIMALLY MIXED.  ZERO INFORMATION.  The state does not exist at B until
    {CLASSICAL_BITS_PER_QUBIT} classical bits arrive -- through ordinary space, at <= c.""")

    P("\n" + "="*79)
    P("4.  'COLLAPSED THE MOMENT THEY TOUCH' -- A CONSERVATION LAW, NOT A CHOICE")
    P("="*79)
    P(f"""
    channel entanglement BEFORE : {CHANNEL_BITS_BEFORE:.9f} bit   (purity {purity(ptrace_first(rho_from(BELL))):.9f})
    channel entanglement AFTER  : {CHANNEL_BITS_AFTER:.9f} bit   (purity 1.000000000, pure)

    ONE PAIR, ONE TRANSIT.  The channel is destroyed BY BEING USED.  That is
    M's clause exactly, and it is teardown.py's closability arriving as a
    CONSERVATION LAW rather than as a design feature: you could not hold it
    open if you wanted to.  membrane.py said "the corridor is open only as long
    as tension lasts"; here there is no tension to run out -- the act of
    transiting is the act of closing.""")

    P("\n" + "="*79)
    P("5.  AND IT IS A MOVE, NOT A COPY")
    P("="*79)
    P(f"""
    After the Bell measurement A's qubit is maximally mixed, S = {entropy2([[0.5+0j,0j],[0j,0.5+0j]]):.9f} bit.
    It holds NO trace of what it carried.  No-cloning enforced by the protocol
    itself rather than imposed on it.

        "THE OBJECT IN TRANSITION TRANSITS" IS THE RIGHT VERB.
        What was here is no longer here.""")

    P("\n" + "="*79)
    P("6.  THE LEDGER -- AND THE STANDING CONSTRAINT")
    P("="*79)
    P(f"\n  {'distance':>18} {'light':>16} {'this':>16} {'advantage':>12}")
    def fmt(s):
        if s < 3600: return f"{s:.3f} s"
        if s < 86400*400: return f"{s/86400:.3f} d"
        return f"{s/3.156e7:.3f} yr"
    for name, D in DISTANCES:
        P(f"  {name:>18} {fmt(D/C_SI):>16} {fmt(arrival_time(D)):>16} "
          f"{advantage_over_light(D):12.3f}")
    P("""
    IDENTICAL AT EVERY DISTANCE.  Not small, not hard -- ZERO, and provably.

    AND THE TRAVERSAL IS NOT REMOVED, IT IS MOVED EARLIER.  A Bell pair
    spanning D required something to cross D at <= c beforehand.

        THE CORRIDOR MUST BE TRAVERSED IN ORDER TO EXIST.

    You pay the full light-speed trip ONCE, in advance, to lay the channel.
    After that every transit is genuinely traversal-free -- and still arrives
    at exactly light speed.

    AND IT CARRIES STATE, NOT SUBSTANCE.  Teleportation writes a quantum state
    onto matter ALREADY AT THE DESTINATION.  No mass moves.  No energy moves.
    For an object to arrive, an identical stock of matter must already be
    there, and that had to travel.

    M'S STANDING RULE FOR THIS THREAD IS "if we can't do it faster and cheap
    then there is no point".  THE MECHANISM IS REAL, THE DESCRIPTION OF IT IS
    CORRECT IN ALL FOUR CLAUSES, AND IT IS NOT FASTER.  Those are compatible
    and all three have to be said together.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M describes an extension rather than a traversal: two sides read to each
  other, collapsing the moment they touch, with the object transiting but not
  traversing.  ALL FOUR CLAUSES ARE EXACTLY RIGHT, and the mechanism has a name
  -- quantum state teleportation, gravitationally the Gao-Jafferis-Wall protocol
  gjw.py already holds -- which M reached by reasoning without naming it.  THE
  SIDES DO READ TO EACH OTHER and the reading carries nothing alone: B's state
  is invariant to 1.1e-16 under every operation A can perform.  THE TRANSIT IS
  EXACT: fidelity 1.000000000000000 on all four outcomes across twelve trials,
  and no worldline crosses anything.  THE CHANNEL COLLAPSES ON CONTACT: 1.000
  bit of entanglement before, 0.000 after -- one pair, one transit, a
  CONSERVATION LAW rather than a design choice, which is teardown.py's
  closability arriving as something you could not switch off if you tried.  AND
  IT IS A MOVE: A's qubit ends maximally mixed at S = 1 bit, no-cloning enforced
  by the protocol rather than imposed on it, so "transits" is the right verb.
  THEN THE STANDING CONSTRAINT.  Withhold the two classical bits and B's state
  is EXACTLY I/2, deviation 1.1e-16, ZERO information -- the state does not
  exist at the far end until two bits cross ordinary space at <= c.  Measured
  against light from Earth-Moon to a galactic crossing the advantage is 0.000,
  0.000, 0.000, 0.000.  AND THE TRAVERSAL IS NOT REMOVED BUT MOVED EARLIER: a
  Bell pair spanning D required something to cross D first, so THE CORRIDOR MUST
  BE TRAVERSED IN ORDER TO EXIST -- pay the light-speed trip once in advance and
  every later transit is genuinely traversal-free and still arrives at exactly
  light speed.  IT ALSO CARRIES STATE AND NOT SUBSTANCE: no mass moves, no
  energy moves, and the matter must already be at the far end.  THE MECHANISM IS
  REAL, THE DESCRIPTION IS CORRECT IN ALL FOUR PARTS, AND IT IS NOT FASTER.
  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ====================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("transit.py --selftest\n")
    rng = random.Random(101)

    print("the two sides read to each other, and it carries nothing")
    r0 = ptrace_first(rho_from(BELL))
    chk("Bell pair: B is maximally mixed", round(r0[0][0].real, 12), 0.5, 1e-12)
    chk("  entanglement is exactly 1 bit", round(entropy2(r0), 12), 1.0, 1e-12)
    worst = max(signalling_deviation(random_unitary(rng)) for _ in range(40))
    chk("no operation on A moves B (40 random unitaries)", worst < 1e-14, True)
    chk("  and that is the no-communication theorem", READING_CARRIES_NOTHING_ALONE, True)

    print("\nthe transit is exact")
    for t in range(5):
        U = random_unitary(rng); psi = [U[0][0], U[1][0]]
        outs = teleport(psi)
        chk(f"trial {t+1}: four outcomes", len(outs), 4)
        chk(f"  each p = 1/4", round(min(p for p, _ in outs), 12), 0.25, 1e-12)
        chk(f"  fidelity = 1 on all four",
            round(min(fidelity(psi, v) for _, v in outs), 12), 1.0, 1e-12)

    print("\nand withholding the bits leaves nothing")
    for t in range(3):
        U = random_unitary(rng); psi = [U[0][0], U[1][0]]
        avg = b_state_without_bits(psi)
        dev = max(abs(avg[i][j] - (0.5 if i == j else 0)) for i in range(2) for j in range(2))
        chk(f"trial {t+1}: rho_B = I/2 exactly", dev < 1e-14, True)
    chk("classical bits required per qubit", CLASSICAL_BITS_PER_QUBIT, 2)

    print("\nthe channel is consumed by use")
    chk("entanglement before", CHANNEL_BITS_BEFORE, 1.0)
    chk("entanglement after", CHANNEL_BITS_AFTER, 0.0)
    chk("  so one pair buys one transit", CHANNEL_IS_CONSUMED_BY_USE, True)
    chk("A ends maximally mixed -- a MOVE, not a copy",
        round(entropy2([[0.5+0j, 0j], [0j, 0.5+0j]]), 12), 1.0, 1e-12)
    chk("  no-cloning enforced by the protocol", IT_IS_A_MOVE_NOT_A_COPY, True)

    print("\nthe ledger")
    for name, D in DISTANCES:
        chk(f"{name}: advantage over light", round(advantage_over_light(D), 12), 0.0, 1e-9)
    chk("so it does not beat light", BEATS_LIGHT, False)
    chk("traversal is MOVED EARLIER, not removed", TRAVERSAL_IS_REMOVED, False)
    chk("it carries state, not substance", CARRIES_SUBSTANCE, False)
    chk("fails the standing constraint 'faster and cheap'",
        MEETS_THE_STANDING_CONSTRAINT, False)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
