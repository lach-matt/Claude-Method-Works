# gate94.py -- scores PREDICTION-FIRSTPROTON.md (sha ecd3cc64479abfc5, filed 15:15:35Z).
# Reads sealed nlchain.jsonl only. CAN-FAIL: pass --canfail N to corrupt clause N's input.
import json,sys
L="spdfghi"; nl=lambda c:int(c[0])+L.index(c[1])
CF=int(sys.argv[sys.argv.index("--canfail")+1]) if "--canfail" in sys.argv else 0
rows={x["Z"]:x for x in (json.loads(l) for l in open("nlchain.jsonl"))}
D={}
for Z in (57,89):
    r=rows[Z]; S=nl(r["ent"]); od=list(r["order"])
    if CF==1 and Z==57: od=od+[["6s",-0.9]]            # inject a lower-n+l channel
    shell=[(k,v) for k,v in od if nl(k)==S]
    if CF==2 and Z==89: shell=[shell[0],shell[3],shell[1],shell[2]]  # move 5f off last
    f=[x for x in shell if x[0][1]=="f"][0]; d=[x for x in shell if x[0][1]=="d"][0]
    D[Z]=dict(S=S,ent=r["ent"],shell=shell,f=f,d=d,
              rank_f=[k for k,_ in shell].index(f[0])+1,n=len(shell),
              lower=[k for k,_ in od if nl(k)<S], short=d[1]-f[1])
if CF==3: D[89]["short"]=0.99                          # break the reproduction
V=[]
def C(name,ok,note): V.append((name,ok,note)); 
C("FP-1 no lower n+l admissible at 57",  D[57]["lower"]==[], f"lower={D[57]['lower']}")
C("FP-1 no lower n+l admissible at 89",  D[89]["lower"]==[], f"lower={D[89]['lower']}")
C("FP-1 entrant shares n+l with the f it beat",
  nl(D[57]["ent"])==nl(D[57]["f"][0]) and nl(D[89]["ent"])==nl(D[89]["f"][0]),
  f"57:{D[57]['ent']}={nl(D[57]['ent'])} vs 4f=7 | 89:{D[89]['ent']}={nl(D[89]['ent'])} vs 5f=8")
C("FP-2a 5f LAST in its shell at 89", D[89]["rank_f"]==D[89]["n"],
  f"rank {D[89]['rank_f']} of {D[89]['n']}")
C("FP-2b 4f SECOND in its shell at 57", D[57]["rank_f"]==2,
  f"rank {D[57]['rank_f']} of {D[57]['n']}  -- PREDICTED 2")
C("FP-3a shortfall_f(89)=0.12616+/-2e-5", abs(D[89]["short"]-0.12616)<=2e-5,
  f"{D[89]['short']:.5f}")
C("FP-3b shortfall_f(57) < shortfall_f(89)", D[57]["short"]<D[89]["short"],
  f"{D[57]['short']:.5f} < {D[89]['short']:.5f}")
C("FP-3c shortfall_f(57) < 0.05", D[57]["short"]<0.05, f"{D[57]['short']:.5f}")
C("FP-4 f behind the d of its own shell at BOTH", D[57]["short"]>0 and D[89]["short"]>0,
  f"{D[57]['short']:.5f}, {D[89]['short']:.5f}")
C("FP-5 no atom where f is deeper than d and still loses",
  D[57]["short"]>0 and D[89]["short"]>0, "route alive")
np=sum(1 for _,o,_ in V if o)
print(f"GATE 94 -- PREDICTION-FIRSTPROTON  {np}/{len(V)}"+(f"   [CANFAIL {CF}]" if CF else ""))
for n_,o,note in V: print(f"   {'PASS' if o else 'FAIL'}  {n_:<46} {note}")
print("VERDICT: two clauses FALSIFIED as filed." if np<len(V) else "VERDICT: all held.")
sys.exit(0 if not CF else (0 if np<len(V) else 9))