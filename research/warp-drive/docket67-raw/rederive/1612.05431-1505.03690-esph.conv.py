import importlib.util, numpy as np
spec=importlib.util.spec_from_file_location('m',__import__('os').path.join(__import__('os').path.dirname(__file__),'1612.05431-1505.03690-esph.py')); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for kw in [dict(),dict(L=120.0),dict(eps=1e-4),dict(n=8000),dict(L=120.0,eps=1e-4,n=8000)]:
    s,t,f,h,B=m.solve(125.20/80.3692,**kw); print('phys',kw,s.status,s.message[:30],round(B,5))
for kw in [dict(),dict(L=120.0),dict(eps=1e-4),dict(L=120.0,eps=1e-4,n=8000)]:
    s,t,f,h,B=m.solve(None,hinf=True,**kw); print('hinf',kw,s.status,round(B,5))
for r in (2.0,3.0,5.0,20.0):
    s,t,f,h,B=m.solve(r,eps=1e-4); print('r',r,s.status,s.message[:40],round(B,4))
s,t,f,h,B=m.solve(0.02,L=400.0); print('0.02',s.status,round(B,5))
s,t,f,h,B=m.solve(0.02,L=800.0); print('0.02 L800',s.status,round(B,5))
