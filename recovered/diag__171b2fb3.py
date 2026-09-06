import sys; sys.path.insert(0,"/home/claude/work")
exec(open("p1d.py").read().split("# ---- TEST THE CLAIM")[0])
L="spdfg"
F=[("v0-2v2+v4",(0,2,4)),("2v0-3v2+v6",(0,2,6)),("v1-2v4+v6",(1,4,6)),("v1-2v3+v5",(1,3,5)),("v3-2v5+v7",(3,5,7))]
print("facet            step  entrant   chord points (n,l,p)   n+l of the three")
for name,(p1,pg,p2) in F:
    for Z,gn,gl,cand in STEPS:
        # find candidates at p1,pg,p2 with min n
        byp={}
        for n,l in cand:
            pp=n-l-1
            if pp not in byp or n<byp[pp][0]: byp[pp]=(n,l)
        if (gn-gl-1)!=pg or p1 not in byp or p2 not in byp: continue
        c1,c2=byp[p1],byp[p2]
        # is this chord the generating one? check by coefficient match
        cvec=[0]*8; cvec[pg]+=c2[0]-c1[0]; cvec[p1]+=gn-c2[0]; cvec[p2]-=gn-c1[0]
        g=math.gcd(*[abs(x) for x in cvec if x]); key=tuple(round(x/g,12) for x in cvec)
        if key in uniq and any(z==Z for z,*_ in uniq[key]):
            trip=[(c1[0],L[c1[1]],p1),(gn,L[gl],pg),(c2[0],L[c2[1]],p2)]
            ms=[c1[0]+c1[1], gn+gl, c2[0]+c2[1]]
            print(f"{name:<14} Z={Z:>3} {G.GROUND[Z][0]:<3} {gn}{L[gl]}   {trip}   {ms}")