"""Re-audit: material-strength-t1000-becu.  Maker sheets (Toray T1000G; Materion Alloy 25/C17200) NOT read:
WebFetch to www.toraycma.com, www.cf-composites.toray, materion.com, www.materion.com -> EGRESS_BLOCKED (not routed around).
No arXiv source restating the data-sheet figures was found.  What WAS read (alphaXiv, verbatim tables):
  2202.09783 Table I (citing Bolund et al. 2007): 'Carbon T1000 1520 [kg/m3] 1950 [MPa]'  (a rotor-composite row)
  2005.04976 Table 2 (measured, Cu-2wt%Be): CG '325 C for 10 hours 1170 [s0.2] 1280 [UTS]'; 'HPT 275 C 10 hours 1300 1375'
             and text citing ASM (Davis 2001): 'hardness up to 400 HV, which corresponds to a 1100 MPa yield stress'
  2410.14855 Table 2: 'BeCu 129 [E, GPa] 1000 [yield, MPa]'  (no source, no density)
None states a BeCu density.  The ring factor v_tip/sqrt(sigma/rho) is recomputed on these."""
import math, sys
sys.path.insert(0,'/home/user/Claude-Method-Works/research/warp-drive')
import warpfolder as W
P=[];F=[]
def chk(n,ok): (P if ok else F).append(n); print(("PASS " if ok else "FAIL ")+n)
v=W.tip_speed_m_s(); print("   tip speed %.2f m/s"%v)
chk("tip speed 8011 m/s (pi*1.8*85000/60)", abs(v-8011.06)<0.05)
fac=lambda s,r: v/math.sqrt(s/r)
tree=[fac(s,r) for _,s,r in W.MATERIALS]; print("   tree factors", ["%.4f"%x for x in tree])
chk("tree ring factors round to [4.2, 19.4]", [round(x,1) for x in tree]==[4.2,19.4])
cases={
 "T1000 composite row (2202.09783 Tab.I via Bolund 2007): 1950 MPa, 1520 kg/m3": fac(1950e6,1520),
 "T1000G sheet value per WebSearch summary only (NOT READ): 6370 MPa, 1800": fac(6370e6,1800),
 "Cu-2Be CG peak-aged UTS 1280 MPa (2005.04976 Tab.2), tree rho 8250": fac(1280e6,8250),
 "Cu-2Be HPT+aged UTS 1375 MPa (2005.04976 Tab.2), tree rho 8250": fac(1375e6,8250),
 "BeCu yield 1000 MPa (2410.14855 Tab.2), tree rho 8250": fac(1000e6,8250),
}
for k,x in cases.items(): print("   %-80s ring factor %.2f  disc(nu=.3) %.2f"%(k,x,x/math.sqrt(8/3.3)))
chk("every read value leaves the rotor over its limit as a ring and as a uniform disc", all(x/math.sqrt(8/3.3)>1 for x in cases.values()))
chk("the composite row makes T1000 WORSE (ring x7.07 vs tree x4.25): the tree's fibre figure favours the rotor", cases[list(cases)[0]]>tree[0])
chk("measured peak-aged BeCu UTS (1280-1375 MPa) gives 19.6-20.3x, 1-5% above the tree 19.4x (lower strength only raises the factor)", all(abs(cases[k]/tree[1]-1)<0.05 for k in list(cases)[2:4]))
print("\n%d PASS, %d FAIL"%(len(P),len(F))); raise SystemExit(1 if F else 0)
