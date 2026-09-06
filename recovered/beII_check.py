R=109737.31568  # cm^-1
Z=2             # Be II: outer electron sees net charge +2, T = Z^2 R/(n-d)^2

print("1. r_l arithmetic  (r = DT/sigma)")
for pair,DT,sg,claim,verdict in [("5f-5g",1.610,0.14,11.5,"admissible"),
                                 ("6f-6g",0.960,0.20,4.80,"EXITS"),
                                 ("7f-7g",0.800,0.20,4.01,"EXITS")]:
    r=DT/sg
    print(f"   {pair}: {DT}/{sg} = {r:.2f}   claimed {claim}  "
          f"{'OK' if abs(r-claim)<0.02 else 'MISMATCH'}   {verdict} (threshold 5): "
          f"{'exits' if r<5 else 'admissible'}")

print("\n2. Ddelta <-> DT consistency:  dT/ddelta = 2 Z^2 R/(n-d)^3")
dd = 0.000148-(-0.000081)   # stated 5f -> 5g defect step
for n,DTstated in [(5,1.610),(6,0.960),(7,0.800)]:
    slope = 2*Z*Z*R/n**3
    DTpred = slope*dd
    print(f"   n={n}: slope={slope:8.1f}/unit-delta  DT(pred, Ddelta={dd:.6f}) = {DTpred:.3f}"
          f"   stated {DTstated:.3f}   implied Ddelta = {DTstated/slope:.6f}")

print("\n3. nu^-3 scaling of r_l (sigma held at stated values)")
r5=1.610/0.14
print(f"   r(6) from r(5): {r5*(125/216)*(0.14/0.20):.2f}   stated 4.80")
print(f"   r(7) from r(5): {r5*(125/343)*(0.14/0.20):.2f}   stated 4.01")

print("\n4. Direction claim, analytically. T = Z^2 R/(n-delta)^2 is INCREASING in delta.")
print("   So T order in l preserved  <=>  delta non-increasing l -> l+1.")
for name,d1,d2 in [("He I singlet p->d",-0.0095,+0.0016),("Be II f->g",+0.000148,-0.000081)]:
    rises = d2>d1
    print(f"   {name}: {d1:+.6f} -> {d2:+.6f}   delta {'RISES -> T order inverted' if rises else 'FALLS -> order preserved'}")
print("   => sign change is not the failure condition; a rise is. +>- falls are harmless,")
print("      ->+ rises invert. Test 1 (sign constancy) is strictly subsumed by test 2.")