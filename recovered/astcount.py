import re,sys,subprocess,importlib
sys.argv=['x']; import build as b
def residues(src,fix=False,strip=False):
    L=open(b.B+src,encoding='utf-8').read().splitlines()
    if strip:
        s=[i for i,l in enumerate(L) if re.match(r'^#{1,3} (Contents|CONTENTS)\b',l)]
        if s:
            i=s[0]; j=i+1
            while j<len(L) and not re.match(r'^## (Part|PART|1\.|Preface|PREFACE)',L[j]): j+=1
            L=L[:i]+L[j:]
    if fix: L=b.fix_bodies(L)
    L=[b.esc_us(l) for l in L]
    open('tmp_ast.md','w',encoding='utf-8').write('\n'.join(L))
    r=subprocess.run(['pandoc','tmp_ast.md','-t','plain','--from','markdown+pipe_tables+smart','--wrap=none'],capture_output=True,text=True)
    lines=[l for l in r.stdout.splitlines() if '*' in l]
    return sum(l.count('*') for l in lines),lines
vols=[('The_Method_1_6-2.md',False,True),('The_Method_1_6___The_Register-2.md',True,False),('The_Method_1_6___Mathematical_Compendium-2.md',False,False),('The_Method_1_6___The_Physics_Compendium-2.md',False,False),('The_Method_1_6___The_Index_of_Indices-2.md',False,False),('The_Method_1_6___Spectra_Compendium-2.md',False,False)]
if __name__=='__main__':
    for v,f,s in vols:
        n,lines=residues(v,f,s); print(v,n,len(lines))
        open('ast_'+v[:20]+'.txt','w').write('\n'.join(lines))