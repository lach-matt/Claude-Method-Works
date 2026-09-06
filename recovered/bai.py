import numpy as np
# Curry, JPCRD 33, 725 (2004), Table 1: Ba I 6snf 3F2 series, as published.
# n : level/cm-1 : decimal places quoted
raw=[(4,34602.765,3),(5,37394.868,3),(6,38815.700,3),(7,39678.176,3),
     (9,40613.87,2),(10,40895.14,2),(11,41100.7,1),(12,41251.2,1),
     (17,41647.85,2),(18,41689.80,2),(19,41725.39,2),(20,41755.48,2),
     (21,41782.02,2),(22,41804.59,2),(23,41824.30,2),(24,41841.63,2),(25,41856.85,2)]
print("published 6snf 3F2 members:", [r[0] for r in raw])
print("gaps at n =", sorted(set(range(4,26))-{r[0] for r in raw}), " <- exactly the paper's 11.2 predictions\n")

def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def kap(y,q):
    y=np.asarray(y,float); D=y[2:]-2*y[1:-1]+y[:-2]
    return np.mean(np.abs(D))/(q/np.sqrt(2)), len(D)

# contiguous blocks only (Sigma needs equal index spacing)
blocks={"n=4-7":[r for r in raw if 4<=r[0]<=7],
        "n=9-12":[r for r in raw if 9<=r[0]<=12],
        "n=17-25":[r for r in raw if 17<=r[0]<=25]}
print(f"{'block':10}{'members':>9}{'q':>8}{'V pooled':>10}{'V split':>9}{'Sigma':>8}{'k pooled':>11}{'k worst sub':>13}")
for name,b in blocks.items():
    n=np.array([x[0] for x in b],float); y=np.array([x[1] for x in b]); q=10.0**(-min(x[2] for x in b))
    i=np.arange(len(y))
    vp=V(y); ve=V(y[i%2==0]) if (i%2==0).sum()>=3 else np.nan
    vo=V(y[i%2==1]) if (i%2==1).sum()>=3 else np.nan
    vs=np.nanmean([ve,vo]); S=2*vs/vp if not np.isnan(vs) else np.nan
    kp,_=kap(y,q)
    ks=[kap(y[i%2==0],q)[0] if (i%2==0).sum()>=3 else np.nan, kap(y[i%2==1],q)[0] if (i%2==1).sum()>=3 else np.nan]
    print(f"{name:10}{len(b):>9}{q:>8.3g}{vp:>10.2f}{vs:>9.2f}{S:>8.2f}{kp:>11.0f}{np.nanmin(ks):>13.0f}")

# r for the main block, using the source's own stated uncertainty
b=blocks["n=17-25"]; y=np.array([x[1] for x in b])
sig=0.1   # Curry sec.2 ref 6 (Armstrong et al.): "typical uncertainties ... on the order of 0.1 cm-1"
r=[min(abs(y[i]-y[i-1]),abs(y[i+1]-y[i]))/sig for i in range(1,len(y)-1)]
print(f"\nn=17-25: min r = {min(r):.0f}  (sigma = 0.1 cm-1, Armstrong et al. via Curry sec. 2)")
print(f"         if sigma were 1e-3 cm-1 as sec 15.2 states: min r = {min(r)*100:.0f}")
print(f"mean bracket width {np.abs(y[2:]-y[:-2]).mean():.2f} cm-1;  two-point interp error {np.abs(y[2:]-2*y[1:-1]+y[:-2]).mean()/2:.2f} cm-1")