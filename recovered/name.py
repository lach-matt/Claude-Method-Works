import re, importlib.util as iu
def setnames(NAMES, path="mathreg.py"):
    s=open(path,encoding="utf-8").read(); n=0
    for k,nm in NAMES.items():
        nm=nm.replace("'","")
        i=s.find(f'R("{k}"')
        if i<0: i=s.find(f"R('{k}'")
        if i<0: print(f"      {k}: absent"); continue
        nx=[x for x in (s.find('\nR("',i+1), s.find("\nR('",i+1)) if x>0]
        j=min(nx) if nx else len(s)
        blk=s[i:j]
        if re.search(r"""named\s*=\s*(['"])\s*\1""",blk):
            blk=re.sub(r"""named\s*=\s*(['"])\s*\1""", f'named="{nm}"', blk)
        elif "named=" in blk:
            blk=re.sub(r"""named\s*=\s*(['"])[^'"]*\1""", f'named="{nm}"', blk)
        else:
            blk=re.sub(r"\)\s*$", f',\n  named="{nm}")\n', blk.rstrip()+"\n")
        s=s[:i]+blk+s[j:]; n+=1
    open(path,"w",encoding="utf-8").write(s)
    try:
        sp=iu.spec_from_file_location("_m",path); mm=iu.module_from_spec(sp)
        sp.loader.exec_module(mm)
    except SystemExit: pass
    except SyntaxError as e:
        print(f"  SYNTAX line {e.lineno}: {(e.text or '')[:110]}"); return None
    sp=iu.spec_from_file_location("_m",path); mm=iu.module_from_spec(sp)
    try: sp.loader.exec_module(mm)
    except SystemExit: pass
    left=len([k for k,v in mm.REG.items() if not (v.get("named") or "").strip()])
    print(f"  {n} named · {left} still unnamed")
    return mm.REG