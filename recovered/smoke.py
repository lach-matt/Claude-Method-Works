import sox_qres as S, numpy as np, time
P=np.array([0.3,1.0,1.7]); print('rho ball', S.rho_q(3.0,P,np.zeros(3)), (4*np.pi/3)*(1-3*P/4+P**3/16))
P2=np.array([0.5]); Pp=np.array([0.8]); r=S.rho_q(3.0,P2,Pp); Pm=np.sqrt(0.5**2+0.8**2); print('rho ball perp', r, (4*np.pi/3)*(1-3*Pm/4+Pm**3/16))
t=time.time(); print('g2b(1.0)',S.g2b(1.0), time.time()-t)