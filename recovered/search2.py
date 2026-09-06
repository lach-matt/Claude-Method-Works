def build(CN,CE,CL,CF,CK,CG,coupling=True):
    cells=[]
    for n in range(1,CN+1):
        for l in range(0,min(n-1,CL)+1):
            for k in range(0,min(2*(2*l+1),CK)+1):
                for S2 in range(0,k+1):
                    for q in range(0,k+1):
                        for e in range(1,CE+1):
                            for f in range(0,min(e-1,CF)+1):
                                gmax=min(q,CG)
                                if coupling: gmax=min(gmax,2*(2*f+1))
                                for g in range(0,gmax+1):
                                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
found=[]
for CN in range(2,6):
 for CE in range(2,6):
  for CL in range(1,4):
   for CF in range(1,4):
    for CK in range(2,7):
     for CG in range(2,7):
      L=build(CN,CE,CL,CF,CK,CG,True)
      if len(L)!=976: continue
      L0=build(CN,CE,CL,CF,CK,CG,False)
      b=1
      for i in range(8): b*=(max(c[i] for c in L)-min(c[i] for c in L)+1)
      diff=set(L0)-set(L)
      found.append(dict(caps=(CN,CE,CL,CF,CK,CG),nocoup=len(L0),box=b,
                        Fm1=sum((-1)**sum(c) for c in L),
                        excl=len(diff), allf0g3=all(c[5]==0 and c[6]==3 for c in diff)))
print(f"{len(found)} cap settings give |Lambda| = 976\n")
for h in found:
    star = "***" if h['nocoup']==1000 and h['box']==6912 and h['Fm1']==2 and h['excl']==24 and h['allf0g3'] else "   "
    print(f"{star} caps n<={h['caps'][0]} e<={h['caps'][1]} l<={h['caps'][2]} f<={h['caps'][3]} "
          f"k<={h['caps'][4]} g<={h['caps'][5]} | no-coupling {h['nocoup']} | box {h['box']} | "
          f"F(-1) {h['Fm1']} | excluded {h['excl']} all(f=0,g=3) {h['allf0g3']}")