import itertools,collections
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
P={'none found':0,'found':1}
def cell(s): a,b,c=[x.strip() for x in s.split('·')]; return (S[a],V[b],P[c])
E65="""definition·order|a closed index §14.1|proved·exhaustive·found
definition·combinatorics|E(X) §6.1|proved·exhaustive·none found
mechanism·order|ℛ §14.2|proved·exhaustive·none found
formula·combinatorics|F(z) §11|proved·exhaustive·found
formula·combinatorics|rank polynomial §11.8|verified·exhaustive·found
formula·analysis|λ²=(2/3)T|proved·exhaustive·found
formula·analysis|V=4ν/3|measured·exhaustive·none found
formula·analysis|bracket width|verified·exhaustive·none found
formula·physics|Rydberg term|verified·exhaustive·found
theorem·order|A.1|proved·exhaustive·none found
theorem·order|A.2|proved·exhaustive·found
theorem·order|A.3|proved·exhaustive·none found
theorem·order|A.6|proved·exhaustive·none found
theorem·order|A.7|proved·exhaustive·none found
theorem·combinatorics|A.8|proved·exhaustive·found
theorem·combinatorics|A.9|proved·exhaustive·found
theorem·combinatorics|A.10|proved·exhaustive·none found
theorem·analysis|A.12|proved·exhaustive·none found
theorem·analysis|A.13|proved·exhaustive·none found
law·complexity|reorderability law|proved·exhaustive·none found
method·order|order recovery|verified·exhaustive·none found
method·combinatorics|collection procedure|verified·sampled·none found
method·analysis|the bracket|verified·exhaustive·none found
measurement·combinatorics|976|measured·exhaustive·none found
measurement·combinatorics|maximal chains|measured·exhaustive·none found
measurement·physics|1442 bracket test|measured·exhaustive·none found
measurement·algebraic geometry|540 KS|measured·sampled·found
theorem·order|A.4|proved·exhaustive·none found
theorem·order|A.5|proved·sampled·none found
theorem·order|A.11|proved·exhaustive·none found
theorem·order|Thm 18.1|proved·exhaustive·none found
theorem·order|Thm 18.2|proved·exhaustive·none found
theorem·order|A.18|proved·exhaustive·none found
theorem·order|ℛ closure op|proved·exhaustive·found
theorem·combinatorics|A.19.0|proved·exhaustive·found
formula·combinatorics|976 words|proved·exhaustive·found
theorem·order|cap-arity|proved·exhaustive·none found
theorem·order|slack=kernel|conjectured·sampled·none found
measurement·combinatorics|3749 covers|measured·exhaustive·none found
theorem·combinatorics|17=17|proved·exhaustive·none found
theorem·order|occupancy clock|proved·exhaustive·found
theorem·order|one arrow|proved·exhaustive·found
measurement·combinatorics|second bridge|measured·exhaustive·none found
theorem·order|separation hyp|proved·sampled·none found
theorem·order|decay theorem|proved·sampled·found
measurement·combinatorics|two indices|measured·exhaustive·none found
theorem·order|step law|proved·exhaustive·found
theorem·order|meet-closure|proved·exhaustive·found
mechanism·physics|LS.ent|verified·exhaustive·none found
law·physics|LS.law|proved·exhaustive·none found
mechanism·physics|LS.coll|verified·exhaustive·found
theorem·physics|LS.pin|measured·exhaustive·none found
theorem·analysis|LS.asym|proved·exhaustive·found
theorem·analysis|LS.quart|proved·exhaustive·none found
theorem·analysis|LS.chord|proved·exhaustive·found
measurement·physics|LS.twin|measured·exhaustive·none found
definition·analysis|3B.shape|proved·exhaustive·found
formula·analysis|3B.metric|proved·exhaustive·found
formula·analysis|3B.JM|proved·exhaustive·found
formula·analysis|3B.pot|proved·exhaustive·found
theorem·algebraic geometry|3B.norm|proved·exhaustive·found
theorem·analysis|3B.five|proved·exhaustive·found
measurement·combinatorics|3B.tri|measured·exhaustive·none found
theorem·complexity|3B.def|proved·exhaustive·found
theorem·order|3B.index|proved·exhaustive·found"""
NEW="""theorem·analysis|the corridor, 106 consistent inequalities|verified·exhaustive·found
measurement·analysis|the nineteen surds|measured·exhaustive·none found
formula·analysis|a_cross = (√(n−1)+√(n−4))/3|proved·exhaustive·none found
formula·order|the staircase algebra|verified·exhaustive·found
mechanism·physics|the sequence-index fix|verified·exhaustive·found
measurement·analysis|the selection-rule falsification|measured·sampled·none found
theorem·physics|the necessity of state|verified·exhaustive·none found
law·physics|the observability boundary|conjectured·sampled·none found
definition·order|the singleton-output rule|proved·exhaustive·none found
law·physics|the domain prohibition|verified·exhaustive·none found
measurement·combinatorics|the limit, E = 11 all named|measured·exhaustive·none found
law·physics|rival = donor iff not full|verified·exhaustive·none found"""
def parse(s): return [(l.split('|')[0],l.split('|')[1],cell(l.split('|')[2])) for l in s.splitlines()]
def R(X):
    X=set(X); A=[sorted({x[i] for x in X}) for i in range(3)]
    def phi(i,j,v): return max(x[i] for x in X if x[j]<=v)
    out=set()
    for x in itertools.product(*A):
        ok=all(x[i]<=phi(i,j,x[j]) for i in range(3) for j in range(3) if i!=j)
        if x[1]==0 and x[2]!=1: ok=False          # cited ⟹ found
        if x[0]>=2 and x[1]<1: ok=False           # ≥measured ⟹ ≥sampled
        if ok: out.add(x)
    return out
def run(els):
    fib=collections.defaultdict(list)
    for f,n,c in els: fib[f].append(c)
    tot=0
    for f,cs in fib.items():
        e=len(R(cs))-len(set(cs)); tot+=e
        if e: print("  ",f,"E =",e,"admitted, absent:",sorted(R(cs)-set(cs)))
    return len(fib),tot
base=parse(E65); print(len(base),"elements; fibres, E:",run(base))
new=parse(NEW); allx=base+new; print(len(allx),"elements; fibres, E:",run(allx))