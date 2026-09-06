"""rg.py -- s73. Scores PREDICTION-RG111 (sha256 20ffe3c7...d23c1a), filed before this file
existed. E(d10 s1) vs E(d9 s2) down group 11, each state on its OWN average-of-configuration
scalar-relativistic HF field plus its OWN determinantal Hund-term correction -- the sealed
pb4_terms convention. Machinery: t7c_hfsr (sealed), hfterm.radial/E_open/E_avg/hund_det
(sealed). The ONLY number entered anywhere is c.

d10 s1 : the only open shell is s1. A single electron forms no pair, so E_open - E_avg = 0
         identically. Asserted here as algebra, not measured.
d9  s2 : open shell d9, Hund term 2D. Term correction nonzero.

Z=111 IS BEYOND THE SEAL. OUTPUT ONLY. NO SCORE. NO DENOMINATOR.
"""
import sys, json, time, numpy as np
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ
from hfterm import radial, E_open, E_avg, hund_det

ROW = {29:('Cu',3,4), 47:('Ag',4,5), 79:('Au',5,6), 111:('Rg',6,7)}

def cfg(Z, nd, ns, kind):
    """Closed core from the generator, then d10 s1 or d9 s2 explicitly."""
    base = {(n,l):q for n,l,q in ground_occ(Z)}
    for k in [(nd,2),(ns,0)]: base.pop(k, None)
    base = {k:v for k,v in base.items() if v == 2*(2*k[1]+1)}      # closed shells only
    base[(nd,2)] = 10 if kind=='A' else 9
    base[(ns,0)] = 1  if kind=='A' else 2
    return sorted([(n,l,q) for (n,l),q in base.items() if q>0])

def energy(Z, nd, ns, kind, c):
    occ = cfg(Z, nd, ns, kind)
    h = HFSR(Z, occ, c=c); _, E, it, _ = h.run('hf', qtail=1)
    openk = [(n,l) for n,l,q in occ if 0 < q < 2*(2*l+1)]
    shells = [(l, int(round(q))) for n,l,q in occ if 0 < q < 2*(2*l+1)]
    dE = 0.0
    if shells and sum(N for _,N in shells) > 1:
        Fk, Gk = radial(h, openk)
        dE = E_open(shells, hund_det(shells), Fk, Gk) - E_avg(shells, Fk, Gk)
    return float(E) + dE, float(E), dE, it, occ

def row(Z, c):
    el, nd, ns = ROW[Z]
    EA, EAh, dA, itA, oA = energy(Z, nd, ns, 'A', c)
    EB, EBh, dB, itB, oB = energy(Z, nd, ns, 'B', c)
    return dict(Z=Z, el=el, c=c, EA=EA, EB=EB, EA_hf=EAh, EB_hf=EBh, dA=dA, dB=dB,
                gap_mHa=(EB-EA)*1e3, lower=('d10s1' if EA < EB else 'd9s2'),
                it=[itA,itB])

if __name__ == "__main__":
    CNR = 1e6
    out = []
    print("=== RG-1 CALIBRATION: the instrument on the three rows whose answer is known ===")
    print("    observed ground state at Cu, Ag, Au is d10 s1. Instrument must agree, or")
    print("    RG-3 and RG-4 are UNINTERPRETABLE and will not be scored.\n")
    ok = True
    for Z in (29, 47, 79):
        r = row(Z, C0); out.append(r)
        good = r['lower'] == 'd10s1'; ok &= good
        print(f"  {r['el']:>3} Z={Z:<4} E(d10s1)-E(d9s2) = {-r['gap_mHa']:10.2f} mHa   "
              f"lower = {r['lower']:<6}  {'AGREES' if good else '*** DISAGREES ***'}", flush=True)
    print(f"\n  RG-1: {'PASS -- instrument calibrated on all three' if ok else 'FAIL'}\n")

    print("=== Z=111 Rg -- BEYOND THE SEAL, OUTPUT ONLY, NO SCORE ===")
    rr = row(111, C0); out.append(rr)
    print(f"  scalar-relativistic c=137.035999 : E(d10s1)-E(d9s2) = {-rr['gap_mHa']:10.2f} mHa"
          f"   lower = {rr['lower']}", flush=True)
    rn = row(111, CNR); out.append(rn)
    print(f"  non-relativistic    c=1e6        : E(d10s1)-E(d9s2) = {-rn['gap_mHa']:10.2f} mHa"
          f"   lower = {rn['lower']}", flush=True)

    shift = abs(rr['gap_mHa'] - rn['gap_mHa'])
    print(f"\n=== RG-2 LEVER (F54.2 law): c moved the Z=111 gap by {shift:.2f} mHa ===")
    if shift <= 1.0:
        print("  RG-2 FAIL -- LEVER DEAD. RUN VOID."); sys.exit(4)
    print("  RG-2 PASS -- c demonstrably moves the output.")
    json.dump(out, open('rg111.json','w'), indent=1)
    print("\nwrote rg111.json")
