import os,importlib
for res in [(160,160,40,40),(60,60,96,96),(320,320,40,40),(60,60,192,192)]:
    os.environ["NZ"],os.environ["NU"],os.environ["NPP"],os.environ["NPV"]=map(str,res)
    import sox_qres as S; importlib.reload(S)
    print(res,round(S.g2b(1.0),6),flush=True)