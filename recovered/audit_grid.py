print("1. Grid arithmetic of the E(X)=5 audit")
grid = {
 ("stated","t1"):1,("stated","t2"):1,("stated","t3"):1,
 ("derived","t1"):1,("derived","t2"):1,("derived","t3"):1,
 ("computable","t1"):1,("computable","t2"):1,("computable","t3"):1,
 ("conf_failure","t1"):1,("conf_failure","t2"):0,("conf_failure","t3"):0,
 ("second_species","t1"):0,("second_species","t2"):0,("second_species","t3"):0,
 ("bounds_coverage","t1"):1,("bounds_coverage","t2"):1,("bounds_coverage","t3"):1,
}
occ=sum(grid.values()); adm=len(grid)
print(f"   admitted {adm}, occupied {occ}, E = {adm-occ}   (stated: 18, 13, 5)  "
      f"{'OK' if (adm,occ,adm-occ)==(18,13,5) else 'MISMATCH'}")

print("\n2. Budget accounting across the two turns (13.6: E(X) = prediction budget)")
preds=[("Be II fails at l=3->4","REFUTED — zero violations; refutation corrected the framework"),
       ("r_l eventually bites","CONFIRMED — first exit, 6f-6g and 7f-7g"),
       ("Be I / Ne I fail","OPEN — reframed: +>- falls now admissible under corrected test"),
       ("coverage drops on raw levels","OPEN — 497 floor, recompute owed"),
       ("Al I labelling generalises","OPEN")]
resolved=sum(1 for _,v in preds if not v.startswith("OPEN"))
print(f"   predictions made: {len(preds)} = E before.  resolved by the Be II fetch: {resolved}.")
print(f"   E after (stated in the Be II turn): 3.  5 - {resolved} = {5-resolved}  "
      f"{'— the budget spent equals the cells closed, exactly' if 5-resolved==3 else 'MISMATCH'}")
for p,v in preds: print(f"     - {p}: {v}")

print("\n3. Post-collapse grid (test 1 deleted, subsumed by test 2)")
print("   12 cells. He I 1 (12/12, all delta-rises) reclassifies as test 2's confirming failure;")
print("   Be II supplies test 2's second species (18 comparisons, 0 violations) and")
print("   test 3's confirming failure (the exit). Empty: test 3 second species,")
print("   plus the two coverage bounds pending the corrected-test recompute -> E = 3 coherent.")