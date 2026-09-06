import re, sys, importlib.util as iu
def apply(ATTR, path="mathreg.py"):
    s=open(path,encoding="utf-8").read()
    n=0
    for k,(src,note) in ATTR.items():
        i=s.find(f'R("{k}"')
        if i<0: i=s.find(f"R('{k}'")
        if i<0: print(f"      {k}: absent"); continue
        nx=[x for x in (s.find('\nR("',i+1), s.find("\nR('",i+1)) if x>0]
        j=min(nx) if nx else len(s)
        blk=s[i:j]
        mg=re.search(r"""(['"])(PROVED|COMPUTED|CITED|DEFINITIONAL|MEASURED)\1""",blk)
        if mg:
            pre=blk[:mg.start()]; last=None
            for mm in re.finditer(r"""(['"])([^'"]*)\1""",pre): last=mm
            if last and last.group(2).strip():
                blk=blk[:last.start(2)]+last.group(2)+"; "+src+blk[last.end(2):]
        blk=re.sub(r'check\s*=\s*None\s*,','',blk)
        mc=re.search(r"""check\s*=\s*(['"])(.*?)\1""",blk,re.S)
        if mc: blk=blk[:mc.start(2)]+mc.group(2)+"  "+note+blk[mc.end(2):]
        else:
            mn=re.search(r"""named\s*=\s*(['"])[^'"]*\1\s*\)""",blk)
            if mn: blk=blk[:mn.start()]+f'check="{note}",\n  '+blk[mn.start():]
            else: blk=re.sub(r"\)\s*$", f',\n  check="{note}")\n', blk.rstrip()+"\n")
        s=s[:i]+blk+s[j:]; n+=1
    for k in ATTR:
        s=s.replace(f'"{k}  PRIOR ART','"PRIOR ART').replace(f"'{k}  PRIOR ART","'PRIOR ART")
        kk=k.split(".")[1]
        s=s.replace(f'"{kk}  PRIOR ART','"PRIOR ART').replace(f"'{kk}  PRIOR ART","'PRIOR ART")
    s=re.sub(r',\s*;\s*([^"\n]+?)"([^"\n]*)",', lambda m: f', "{m.group(2)}; {m.group(1).strip()}",', s)
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
    print(f"  {n} attributed · {len(mm.REG)} objects load")
    return mm.REG