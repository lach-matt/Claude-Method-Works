# On a D-O diagonal (fixed M): p = 2n-M-1 steps by 2, n by 1.  nu = n - a*v(p).
# Member k precedes k+1 iff a*(v_{k+1}-v_k) > 1  ->  corridor of member k = (1/D_k , 1/D_{k-1}),  D_k = v_{k+1}-v_k.
# Concave v => D_k decreasing => corridors are consecutive, disjoint, and partition (0,inf).
cores = {
 'Xe core, Cs I  (M=7)': [('4f',0.033),('5d',2.466),('6p',3.593),('7s',4.051)],
 'Xe core, Ba II (M=7)': [('4f',0.756),('5d',2.415),('6p',3.241),('7s',3.598)],
 'Rn core, Fr I  (M=8)': [('5f',None),('6d',3.42371),('7p',4.59521),('8s',5.07221)],
 'Kr core, Rb I  (M=6)': [('4d',1.331),('5p',2.657),('6s',3.136)],
}
for name,mem in cores.items():
    print(name)
    lo=0.0
    for k,(lab,v) in enumerate(mem):
        nxt = mem[k+1][1] if k+1<len(mem) else None
        if v is None: print(f"  {lab}: (0, ?)  -- v unmeasured (facet-4 null)"); lo=None; continue
        hi = 1/(nxt-v) if nxt is not None else float('inf')
        los = '?' if lo is None else f"{lo:.3f}"
        print(f"  {lab}: ({los}, {hi:.3f})")
        lo=hi