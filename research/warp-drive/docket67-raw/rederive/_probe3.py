import sympy as sp, mpmath as mp, sys, time
sys.path.insert(0,'/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive')
exec(open('/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/_probe2.py').read().split("t0=time.time()")[0])
stat=Gmixed(VS*prof(sp.sqrt(x**2+y**2+z**2)))
com=Gmixed(-VS*(1-prof(sp.sqrt(x**2+y**2+z**2))))
lab=Gmixed(VS*prof(sp.sqrt((x-VS*t)**2+y**2+z**2)))
L={k:sp.lambdify((t,x,y,z),e,'mpmath') for k,e in (('lab',lab),('stat',stat),('com',com))}
sys.path.insert(0,'/home/user/Claude-Method-Works/research/warp-drive')
import typefour
for (px,py) in [(0.6,0),(0.9,0),(0.9,0.3),(1.0,0),(1.0,0.2),(1.05,0.4),(1.2,0.3)]:
    out=[]
    for k in ('lab','com','stat'):
        M=mp.matrix(L[k](0,mp.mpf(px),mp.mpf(py),0))/(8*mp.pi)
        ev=mp.eig(M)[0]
        n=mp.sqrt(sum(M[i,j]**2 for i in range(4) for j in range(4)))
        im=max(abs(mp.im(e)) for e in ev)
        cp=[mp.nstr(c,8) for c in (sum(ev), )]
        out.append('%s |T|=%s Im/|T|=%s tr=%s'%(k,mp.nstr(n,6),mp.nstr(im/n,5),mp.nstr(mp.re(sum(ev)),6)))
    tf=typefour.classify((px,py,0.0))
    print((px,py),' | '.join(out),' | typefour |T|=%.5f r=%.4f %s'%(tf[0],tf[2],tf[3]))
