import os,importlib
for res in [(60,60,256,64),(60,60,64,256),(60,60,256,256)]:
    os.environ["NZ"],os.environ["NU"],os.environ["NPP"],os.environ["NPV"]=map(str,res)
    import sox_qres as S; importlib.reload(S)
    print(res,round(S.g2b(1.0),6),flush=True)