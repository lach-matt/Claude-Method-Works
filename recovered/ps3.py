import numpy as np, json, sox_table as T
B0=dict(rs=np.log([1,2,3,5,10]),e=[-0.0600,-0.0448,-0.0369,-0.0281,-0.0186]); B1=dict(rs=np.log([2,5,10]),e=[-0.0240,-0.0154,-0.0105])
def bench(rs,z):
    l=np.log(rs); e0=np.interp(l,B0['rs'],B0['e']); e1=np.interp(l,B1['rs'],B1['e']); return (1-z)*e0+z*e1
tab=json.load(open('ring_table.json')); RS=np.array(tab['rs']); ring=np.array([tab['eps'][str(i)] for i in range(11)])/2.0
sox=np.array(json.load(open('sox_table.json'))['eps2x'])
print(" rs   z  |  R=ring/2+E0B   S=ring/2+sox   bench   R-b     S-b")
mx=0; rows=[]
for z,iz in ((0.0,0),(1.0,10)):
    for rs in (1,2,3,5,10):
        b=bench(rs,z); r=ring[iz]+0*RS; e_r=np.interp(np.log(rs),np.log(RS),ring[iz]); e_s=np.interp(np.log(rs),np.log(RS),sox[iz])
        Rv=e_r+T.E0B; Sv=e_r+e_s
        print(f"{rs:5.2f} {z:3.1f} | {Rv:+.5f}   {Sv:+.5f}   {b:+.5f}   {Rv-b:+.4f}  {Sv-b:+.4f}")
        rows.append(dict(rs=rs,z=z,R=float(Rv),S=float(Sv),bench=b))
        if 1<=rs<=5 and not (z==1.0 and rs<2): mx=max(mx,abs(Sv-b))
print("PS-3 max|S-bench| rs in [1,5] (zeta 1 from rs 2, first anchor):",round(mx,4),"<= 0.003 ->","HELD" if mx<=0.003 else "FAILED")
json.dump(rows,open('sox_bench_compare.json','w'))