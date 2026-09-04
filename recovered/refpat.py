import numpy as np
print("="*88)
print("  THE CONTRADICTION, AND WHY IT WAS ONE")
print("="*88)
print("""
  I wrote: 'the index sees the sign change and cannot tell you which it
  is.'  **An index does not see A sign change. It sees a FAMILY.** Section
  10.7.1 already established that the discriminating question is asked of
  the whole structure, not of one cell — that is how a defect of the index
  is told from a feature of the world.

  **Apply the same move: look at the PATTERN of refusals across the
  family, not at one refusal.**
""")
def refusal_pattern(y,k=1):
    """where does the (k+1)th difference change sign?"""
    d=np.array(y,dtype=float)
    for _ in range(k+1): d=np.diff(d)
    s=np.sign(d)
    return s, [i for i in range(1,len(s)) if s[i]!=s[i-1] and s[i]!=0 and s[i-1]!=0]
x=np.linspace(0,6*np.pi,60)
OSC=np.cos(x)
a=np.linspace(-1,1,60)
BIF=np.where(a<0,0.0,np.sqrt(np.maximum(a,0)))
MONO=1.0/(np.linspace(3,20,60)**2)
LIN=2.0*np.linspace(1,60,60)
print("  %-22s%10s%14s%28s"%("family","refusals","spacing","verdict"))
print("  "+"-"*76)
for nm,y in [("cos — oscillation",OSC),("pitchfork — bifurcation",BIF),
             ("1/nu^2 — monotone",MONO),("linear",LIN)]:
    s,ch=refusal_pattern(y)
    if len(ch)>=2:
        gaps=np.diff(ch); sp="%.1f ± %.1f"%(gaps.mean(),gaps.std())
    elif len(ch)==1: sp="single"
    else: sp="none"
    if len(ch)>=3 and np.std(np.diff(ch))<0.25*np.mean(np.diff(ch)):
        v="PERIODIC — an oscillation"
    elif len(ch)==1: v="ONE — a bifurcation"
    elif len(ch)==0: v="NONE — smooth or exact"
    else: v="irregular"
    print("  %-22s%10d%14s%28s"%(nm,len(ch),sp,v))
print("""
  **THE INDEX DOES TELL THEM APART, AND BY A SINGLE TEST:**

     refusals REGULARLY SPACED   -> an oscillation. The family returns.
     refusals ONE                -> a bifurcation. The family changes
                                    character once and does not return.
     refusals NONE               -> smooth, or exact.

  **CORRECTION 115.** 'The index sees the sign change and cannot tell you
  which it is' is false. It cannot tell from ONE cell. **An index is never
  one cell**, and Section 10.7.1 makes exactly that argument about a
  different pair.
""")
print("="*88)
print("  AND THE FIRST POINT IS ALSO RIGHT — PHYSICS IS IN THE INDEX")
print("="*88)
print("""
  I drew a line between 'a question about physics' and 'a question about
  the index'. **The book's own results deny that line:**
""")
EV=[("the Pauli bound g <= 2(2f+1)","Section 6.5","the ONE constraint that is physics, and it is a coordinate bound"),
    ("the magic numbers 2,8,20,28,50,82","Section 22.6.2","fall out of the nuclear index as cumulative capacities"),
    ("the resonance order cut at 7/8","Section 10.7.1","recovered from occupancy alone; e^order never supplied"),
    ("delta falls with l","Chapter 16","an ordering of channels, and it is penetration"),
    ("the pole at p = 1","Section 22.6.1","exact linearity — and L4, L5 are exact solutions")]
print("  %-34s%-16s%s"%("physical fact","where","how it enters"))
print("  "+"-"*86)
for a2,b2,c2 in EV: print("  %-34s%-16s%s"%(a2,b2,c2[:36]))
print("""
  **EVERY ONE OF THESE IS PHYSICS EXPRESSED AS AN ORDER PROPERTY.** The
  index does not sit beside the physics; **where the coordinates are
  physical, the physics IS the index.**

  **So the correct statement is not 'that is a question about physics, not
  about the index'. It is:**

     a question is answerable by the index **exactly when the physics has
     been put into the coordinates**

     and when it has not, the right response is to PUT IT THERE — which
     is what Section 22.6.2 did for the nucleus and Section 10.7.1 did for
     the resonances

  **CORRECTION 116.** The line I drew is the one Section 11's E2 forbids:
  it treats a physical fact as external when it is a candidate coordinate.
""")
print("="*88)
print("  SO THE CONJECTURE'S PART 2 IS BACK IN PLAY")
print("="*88)
print("""
  'linear and oscillating are the two stable regimes' — I called this
  half-testable because the index could not distinguish oscillation from
  bifurcation. **It can.**

     LINEAR      V = infinite, no refusals, exact
     OSCILLATING refusals REGULARLY SPACED, family returns
     BIFURCATING refusals ONCE, family does not return

  **Three regimes, all three visible to the index, all three distinguished
  by the refusal pattern alone** -- no fit, no equations of motion.

  **And 'stable' now has an index-side meaning:** a family is stable when
  its refusal pattern is either empty or periodic. **A single refusal is
  the unstable case**, because it marks a change of character with no
  return.
""")