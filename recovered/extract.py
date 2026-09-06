import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
print("  THE GEOMETRIC SHAPE -> THE ALGEBRA.  the ceiling is")
print("      U = (n_r - n_g) / (sqrt(rad_r) - sqrt(rad_g)),   rad = p + occ/2(2l+1)")
print("  the rival's OCCUPANCY enters through rad_r. Expand it.\n")
print("  d(U)/d(occ_r) — how much does one electron in the RIVAL move the ceiling?\n")
def U(dn, pg, pr, occr, lr):
    return dn/(math.sqrt(pr+occr/cap(lr)) - math.sqrt(pg))
print(f"  {'case':<22}{'occ 0':>10}{'occ 1':>10}{'occ 2':>10}{'Δ per e-':>11}")
CASES=[("s rival, p_r=4, Δn=1",1,1,4,0),("s rival, p_r=3, Δn=1",1,1,3,0),
       ("p rival, p_r=3, Δn=1",1,1,3,1),("d rival, p_r=2, Δn=1",1,1,2,2),
       ("d rival, p_r=1, Δn=0",1,1,1,2)]
for lab,dn,pg,pr,lr in CASES:
    vs=[U(dn,pg,pr,o,lr) for o in (0,1,2)]
    print(f"  {lab:<22}{vs[0]:>10.4f}{vs[1]:>10.4f}{vs[2]:>10.4f}{(vs[2]-vs[0])/2:>11.4f}")
print("\n  THE ALGEBRA: U falls as occ_r rises, because sqrt(p_r + occ/cap) grows")
print("  and the DENOMINATOR grows. The rate is  -dn/(2*cap*sqrt(rad_r)*(sqrt(rad_r)-sqrt(rad_g))^2)")
print("  so the pull is largest when (a) cap is SMALL and (b) the two radicands")
print("  are CLOSE. cap = 2 for s, 6 for p, 10 for d, 14 for f.\n")
def dUdocc(dn,pg,pr,occr,lr):
    rr=pr+occr/cap(lr); d=math.sqrt(rr)-math.sqrt(pg)
    return -dn/(2*cap(lr)*math.sqrt(rr)*d*d)
print(f"  {'rival':>7}{'cap':>5}{'p_r':>5}{'p_g':>5}{'dU/d(occ)':>12}")
for lab,lr,pr,pg in (("s",0,4,1),("s",0,3,1),("p",1,3,1),("d",2,2,1),("f",3,0,1)):
    if pr<=pg and lr==3: continue
    print(f"  {lab:>7}{cap(lr):>5}{pr:>5}{pg:>5}{dUdocc(1,pg,pr,1,lr):>12.4f}")
print("\n  -> the s rival has cap 2, the SMALLEST, so one electron in an s rival")
print("     moves the ceiling MOST. that is the algebra of 'the charge of two'.")
print("\n  CHECK against the measured medians (margin by rival occupancy):")
print("      s occ 0 -> +1.7379   s occ 1 -> +0.2529   ratio "
      f"{1.7379/0.2529:.2f}")
print("      p occ 0 -> +0.8369   p occ 1 -> -0.1356")
print("      d occ 0 -> +0.5071   d occ 1 -> +0.1520   d occ 2 -> -0.0984")
print("      the ordering is monotone in occupancy WITHIN each l, and the")
print("      s drop is the largest — as 1/cap predicts.")