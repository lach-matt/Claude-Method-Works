import re,sys,os
for b in sys.argv[1:]:
    t=open(b).read()
    for m in re.finditer(r'<<<FILE: (.+?)>>>\n(.*?)\n<<<END FILE: \1>>>',t,re.S):
        open(os.path.join('/home/claude/build',m.group(1)),'w').write(m.group(2)+'\n')
        print(m.group(1), len(m.group(2)))