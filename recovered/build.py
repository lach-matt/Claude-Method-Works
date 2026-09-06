import re,sys,subprocess,os,pathlib
B='/home/claude/build/'
def build(src,out,title,strip_contents=False,toc_depth=2):
    t=open(B+src,encoding='utf-8').read()
    L=t.splitlines()
    # first H1 becomes the document title
    h1=[i for i,l in enumerate(L) if l.startswith('# ')]
    if h1: L[h1[0]]=''
    if strip_contents:
        # remove the book's literal contents block: lines between 'Contents' heading and next '## ' body heading
        s=[i for i,l in enumerate(L) if re.match(r'^#{1,3} (Contents|CONTENTS)\b',l)]
        if s:
            i=s[0]; j=i+1
            while j<len(L) and not re.match(r'^## (Part|PART|1\.|Preface|PREFACE)',L[j]): j+=1
            L=L[:i]+L[j:]; print('contents block removed',i,j)
    md='\n'.join(L)
    meta=f'---\ntitle: "{title}"\nauthor: "Matthew Lach"\ndate: "Build 6 — 2026-08-24"\n---\n\n'
    open('tmp.md','w',encoding='utf-8').write(meta+md)
    cmd=['pandoc','tmp.md','-o',out,'--from','markdown+pipe_tables+smart','--toc','--toc-depth',str(toc_depth),'--resource-path',B,'--reference-doc','ref.docx']
    r=subprocess.run(cmd,capture_output=True,text=True); print(r.stderr[-1500:])
    print(out,os.path.getsize(out))
if __name__=='__main__':
    build(*sys.argv[1:4],strip_contents=('strip' in sys.argv),toc_depth=int(sys.argv[-1]) if sys.argv[-1].isdigit() else 2)