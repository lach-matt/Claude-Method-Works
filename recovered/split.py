import re,sys
for src in sys.argv[1:]:
    txt=open(src,encoding='utf-8').read()
    for m in re.finditer(r'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>', txt, re.S):
        name,body=m.group(1),m.group(2)
        open(name,'w',encoding='utf-8').write(body)
        print(name, len(body.splitlines()))