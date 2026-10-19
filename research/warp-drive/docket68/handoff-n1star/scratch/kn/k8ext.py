import numpy as np, pickle, sympy as sp, mpmath as mp
exec(open('k8.py').read().split("Z=np.linspace(0.005,1.2,600)")[0].replace("'numpy')\nq=pickle","'mpmath')\nq=pickle",1))
mp.mp.dps=80
Zs=np.concatenate([np.linspace(1.2,3,40),np.linspace(3.2,30,40)]); THs=np.linspace(0.03,np.pi/2-0.03,61); PH=np.linspace(0,2*np.pi,145)
lamT=np.zeros(len(Zs))
for i,zz in enumerate(Zs):
    a=0.5*(1-1/zz**2); b=0.5/zz**2; w=0          # T-energy density coefficients (f_r^2, f_th^2)
    for t in THs:
        eF=np.array([float(x) for x in E['F'](mp.mpf(zz),mp.mpf(t))]); eG=np.array([float(x) for x in E['G'](mp.mpf(zz),mp.mpf(t))])
        e=(np.cos(PH)[:,None]*eF[None,:]-np.sin(PH)[:,None]*eG[None,:])
        P=np.abs(e[:,0])/a; S=np.abs(e[:,2])/b; Qn=np.abs(e[:,1])/(2*np.sqrt(a*b))
        w=max(w,((P+S)/2+np.sqrt(((P-S)/2)**2+Qn**2)).max())
    lamT[i]=w
k=lamT.max(); print('kappa_ext (per unit A env mu^-1/4, units 1/sqrt mu):',k,'at z',Zs[lamT.argmax()])
for zz in (1.2,1.5,2,3,5,10,30): print(zz,float(np.interp(zz,Zs,lamT)))
rh=72762.0; D=269.15; mu0=np.sqrt(72)/rh**2; dmu=1-mu0; S8=35/128
s=np.linspace(0,1,200001); env=np.sin(np.pi*s)**4
mup=dmu*env**2/(S8*D); mu=mu0+np.concatenate([[0],np.cumsum((mup[1:]+mup[:-1])/2*np.diff(s*D))])
A=np.sqrt(9*dmu/(2*D*S8)); Ap=A*env/mu**0.25
G=np.trapz(k*Ap/np.sqrt(mu),s*D); print('crude exterior exponent Gamma:',G)
w=10.0; lam_=w/(2*np.pi)/rh                       # lambda in r_h units
strain=(2/3)*lam_*Ap/np.sqrt(mu)/1.2**1.5         # at z = 1.2, relative
print('max exterior strain (z>=1.2):',strain.max(),' averaged estimate Gamma*strain:',np.trapz(k*Ap/np.sqrt(mu)*strain,s*D))
pickle.dump(dict(Z=Zs,lamT=lamT,G=G),open('k8ext.pkl','wb'))
