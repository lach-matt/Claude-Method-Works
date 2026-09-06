from itertools import product
def build(CN,CE,CL,CF,CK,CG):
    cells=[]
    for n in range(1,CN+1):
        for l in range(0,min(n-1,CL)+1):
            for k in range(0,min(2*(2*l+1),CK)+1):
                for S2 in range(0,k+1):
                    for q in range(0,k+1):
                        for e in range(1,CE+1):
                            for f in range(0,min(e-1,CF)+1):
                                for g in range(0,min(q,2*(2*f+1),CG)+1):
                                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
def box(L):
    b=1
    for i in range(8): b*=(max(c[i] for c in L)-min(c[i] for c in L)+1)
    return b
hits=[]
for CN in (3,4):
 for CE in (3,4):
  for CL in (1,2,3):
   for CF in (1,2,3):
    for CK in (2,3,4):
     for CG in (2,3,4,6):
      L=build(CN,CE,CL,CF,CK,CG)
      if len(L)==976:
          hits.append((CN,CE,CL,CF,CK,CG,box(L),sum((-1)**sum(c) for c in L)))
print("caps (n,e,l,f,k,g) giving |L|=976:")
for h in hits: print(f"  n<={h[0]} e<={h[1]} l<={h[2]} f<={h[3]} k<={h[4]} g<={h[5]}   box={h[6]}  F(-1)={h[7]}")
print("\nof those, matching book box 6912 AND F(-1)=2:")
for h in hits:
    if h[6]==6912 and h[7]==2: print(f"  *** n<={h[0]} e<={h[1]} l<={h[2]} f<={h[3]} k<={h[4]} g<={h[5]}")