import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])
rng=np.random.default_rng(99)
def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def Sig(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    return 2*np.nanmean([V(y[i%2==0]),V(y[i%2==1])])/V(y)

print("=== robustness of the two load-bearing conclusions to their weakest assumption ===")
mp=np.array([134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0])
print("alkane melting points: sigma is ASSUMED (0.3 K), and handbook values differ between sources.")
print(f"{'assumed sigma':>15}{'Sigma obs':>11}{'null 99%':>10}{'margin':>9}")
for sig in [0.1,0.3,0.5,1.0,2.0,3.0,5.0]:
    S=[]
    x=np.arange(11.); base=np.polyval(np.polyfit(x[::2],mp[::2],3),x)
    step=np.median(np.abs(np.diff(mp[::2])))/2
    for _ in range(3000):
        z=base+rng.normal(0,sig,11)
        if np.all(np.diff(z)>0): S.append(Sig(z))
    nl=np.percentile(S,99) if S else np.nan
    # also perturb the DATA itself by sigma, to see if the observed Sigma is stable
    obs=[Sig(mp+rng.normal(0,sig,11)) for _ in range(2000)]
    print(f"{sig:>15.1f}{np.median(obs):>11.2f}{nl:>10.2f}{np.median(obs)/nl:>8.1f}x")

print("\n=== OH kinetics V: 90% interval at the evaluation's own stated uncertainty ===")
K=np.array([.00640,.248,1.09,2.36,3.80,5.20,6.76,8.11,9.70,11.0,12.3,13.2,15.1]); U=np.full(13,.10); U[[4,12]]=.125
w=[];e=[]
for i in range(1,12):
    w.append(abs(K[i+1]-K[i-1])/K[i]); e.append(abs(np.interp(0,[-1,1],[K[i-1],K[i+1]])-K[i])/K[i])
bs=[]
for _ in range(4000):
    Kp=K*(1+rng.normal(0,U,13))
    ww=np.abs(Kp[2:]-Kp[:-2]); ee=np.abs(Kp[2:]-2*Kp[1:-1]+Kp[:-2])/2
    bs.append(ww.sum()/ee.sum())
print(f"  V = {V(K):.1f}, 90% CI [{np.percentile(bs,5):.1f}, {np.percentile(bs,95):.1f}]")

print("\n=== nuclear: how well does V = 2*Sbar/Delta actually predict V? ===")
pr=[];ob=[]
for el,(Z,rows) in CH.items():
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows]); d=np.diff(B)
    S=d.mean(); D=abs(d[0::2].mean()-d[1::2].mean())/2
    pr.append(2*S/D); ob.append(V(B))
pr=np.array(pr);ob=np.array(ob); rel=(pr-ob)/ob
print(f"  predicted/observed ratio: mean {np.mean(pr/ob):.2f}, range {np.min(pr/ob):.2f}-{np.max(pr/ob):.2f}")
print(f"  relative error: median {100*np.median(np.abs(rel)):.0f}%, max {100*np.max(np.abs(rel)):.0f}%")

print("\n=== what fraction of the paper's numbers did this session verify? ===")
comp=["containment curve","OH+alkane r and V","nine nuclear chains r/V/Sigma","alkane mp/bp/dHvap V,kappa,Sigma",
      "Ba I 6snf V, kappa, r (from Curry Table 1)","Prop 14.1 and its floor","Sigma null distribution",
      "scheduling experiment on Lambda","Lambda poset structure (118 cells, 3 maximal)"]
inh=["295-cell verification and 22 channels","rule-ablation costs (3.7x, 2.4x, 96.2%, 3.2x)",
     "closure tests (8e6 pairs, 24.4M pairs, dimension 8/9/10)","axis-ablation collision counts",
     "Sr I node 79% vs 100%","fine-structure 35.3%","Ti I 23 channels 0 interior",
     "Kr II 5591+-500 vs 5370.10","sec 13 six mechanisms (LOO rmse, p-values, 62%)",
     "Appendix A failure counts","offset-coordinate failure counts (222075/11696)"]
print(f"  computed here and reproducible from cited sources: {len(comp)}")
for c in comp: print(f"     - {c}")
print(f"  inherited from earlier drafts, NOT re-verified in this session: {len(inh)}")
for c in inh: print(f"     - {c}")