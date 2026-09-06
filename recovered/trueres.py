import re,sys,subprocess; sys.argv=['x']; sys.path.insert(0,'/home/claude/build'); import build as b
def prep(src,fix=False,strip=False):
    L=open(b.B+src,encoding='utf-8').read().splitlines()
    if strip:
        s=[i for i,l in enumerate(L) if re.match(r'^#{1,3} (Contents|CONTENTS)\b',L[i])]
        if s:
            i=s[0]; j=i+1
            while j<len(L) and not re.match(r'^## (Part|PART|1\.|Preface|PREFACE)',L[j]): j+=1
            L=L[:i]+L[j:]
    if fix: L=b.fix_bodies(L)
    L=b.displays(L); L=[b.esc_us(l) for l in L]
    return '\n'.join(L)
def true_residues(src,fix=False,strip=False):
    md=prep(src,fix,strip).replace('\\*','\x03')
    r=subprocess.run(['pandoc','-t','plain','--wrap=none','--from','markdown+pipe_tables+smart'],input=md,capture_output=True,text=True)
    return [l for l in r.stdout.splitlines() if '*' in l]
vols=[('The_Method_1_6-2.md',False,True),('The_Method_1_6___The_Register-2.md',True,False),('The_Method_1_6___Mathematical_Compendium-2.md',False,False),('The_Method_1_6___The_Physics_Compendium-2.md',False,False),('The_Method_1_6___The_Index_of_Indices-2.md',False,False),('The_Method_1_6___Spectra_Compendium-2.md',False,False)]
if __name__=='__main__':
    sel=sys.argv[1:] if len(sys.argv)>1 else None
    for v,f,s in vols:
        lines=true_residues(v,f,s); print(v,'lines',len(lines),'stars',sum(l.count('*') for l in lines))
        open('res_'+v.replace('The_Method_1_6','M').replace('.md','')+'.txt','w',encoding='utf-8').write('\n'.join(lines))