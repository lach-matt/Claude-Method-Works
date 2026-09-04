# gate96.py -- scores PREDICTION-Z57C.md (sha cbcc3d249ab02f34, filed 15:19:53Z). F56.3 remedy.
import json,sys
L="spdfghi"; nl=lambda c:int(c[0])+L.index(c[1])
CF=int(sys.argv[sys.argv.index("--canfail")+1]) if "--canfail" in sys.argv else 0
c=[json.loads(l) for l in open("/tmp/c3z57.jsonl")][0]
s={x["Z"]:x for x in (json.loads(l) for l in open("nlchain.jsonl"))}[57]
if CF==1: c["ent"]="4f"
if CF==2: c["order"]=[[k,v*0.5] for k,v in c["order"]]
S={k:v for k,v in s["order"]}; C={k:v for k,v in c["order"]}
print(f"  self-check: {c.get('selfcheck', c.get('dE80','(field absent)'))}")
print(f"  {'chan':>6}{'n+l':>5}{'sealed':>11}{'c=1e6':>11}{'deepens by':>12}")
for k in ("4f","5d","6p","7s"):
    if k in S and k in C: print(f"  {k:>6}{nl(k):>5}{S[k]:>11.5f}{C[k]:>11.5f}{S[k]-C[k]:>12.5f}")
ru=[ (k,v) for k,v in c["order"] if k!=c["ent"] ][0]
d4=S["4f"]-C["4f"]; d5=S["5d"]-C["5d"]; diff=d4-d5
sh_c=C["4f"]-C["5d"]
V=[("ZC-1 self-check present and lever alive", "1206.45" in str(c), str(c).count("1206.45")>0),
   ("ZC-2 ent(57,c=1e6) = 5d  -- 4f STILL LOSES", c["ent"]=="5d", f"ent={c['ent']}, runner-up={ru[0]}(n+l={nl(ru[0])})"),
   ("ZC-3 4f deepens MORE than 5d", diff>0, f"4f {d4:+.5f} vs 5d {d5:+.5f}, differential {diff:+.5f}"),
   ("ZC-4 differential < 0.183 Ha (the Z=90 value)", diff<0.183, f"{diff:.5f} vs 0.183"),
   ("ZC-5 shortfall(57,c=1e6) positive and < 0.10029", 0<sh_c<0.10029, f"{sh_c:.5f} vs sealed 0.10029"),
   ("ZC-6 4f and 5d both n+l=7 at c=1e6", nl("4f")==7 and nl("5d")==7, "7 and 7 -- tie-break only")]
V=[(a,b,d) for a,b,d in [(x[0],x[1],x[2]) for x in V]]
np=sum(1 for _,o,_ in V if o)
print(f"\nGATE 96 -- PREDICTION-Z57C  {np}/{len(V)}"+(f"   [CANFAIL {CF}]" if CF else ""))
for n_,o,note in V: print(f"   {'PASS' if o else 'FAIL'}  {n_:<44} {note}")
print(f"\n  4f/5d differential at Z=57 : {diff:.5f} Ha")
print(f"  5f/6d differential at Z=90 : 0.18300 Ha (s55 §4)")
print(f"  ratio {diff/0.183:.3f}   against the filed (57/90)^2 = 0.401 scaling argument")