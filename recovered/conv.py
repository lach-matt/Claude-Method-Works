import os,sys,time,importlib
for res in [(60,60,40,40),(100,100,64,64),(160,160,96,96)]:
    os.environ["NZ"],os.environ["NU"],os.environ["NPP"],os.environ["NPV"]=map(str,res)
    import sox_qres as S; importlib.reload(S)
    t=time.time(); vals=[S.g2b(q) for q in (0.05,0.5,1.0,2.5)]; print(res,[round(v,6) for v in vals],round(time.time()-t,1),flush=True)