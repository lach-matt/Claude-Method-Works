# Register front matter, "What the entries are": counts of entries whose HEADLINE matches each pattern
# (case-insensitive; a body tag "(a finding.)" etc. overrides). Kinds overlap; not a partition. Register 1756.
import re,collections,sys
R=open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
i=R.find('\n### 165\n'); body=R[i:]
ents=re.split(r'\n### (\d+[a-z]?)\n',body)
ids,bodies=ents[1::2],ents[2::2]
PAT={
 'a correction':   r'CORRECT|WRONG|STALE|PUT RIGHT|AMEND|FIX|MISLOCAT|REPAIR|ERROR|OVERTAKEN|MISTAK|MISREAD|MISCOUNT',
 'a measurement':  r'\d',
 'prior art':      r'PRIOR ART|PUBLISHED|ALREADY (KNOWN|IN|DONE)|\b(1[5-9]\d\d|20[0-2]\d)\b|[A-Z][a-z]+ \(\d{4}\)',
 'a new protocol': r'PROTOCOL|\bRULE\b|RULED|RULING|MUST\b|NEVER AGAIN|PROCEDURE',
 'a withdrawal':   r'WITHDR|RETRACT|REMOVED|DROPPED|ABANDON|DISCARD',
 'a fault of mine':r'FAULT OF MINE|MY FAULT|MY ERROR|THE ASSISTANT|I (MIS|FAIL|WROTE|CARRIED)|MEA CULPA',
 'an open question':r'OPEN QUESTION|\bOPEN\b|UNSETTLED|CANNOT (CURRENTLY|YET)|UNKNOWN|UNRESOLVED|NOT (YET )?(SETTLED|KNOWN)',
}
TAG=r'\(\s*(a finding|a correction|a measurement|prior art|a new protocol|a withdrawal|a fault of mine|an open question)\.?\s*\)\*?\s*$'
cnt=collections.Counter()
for b in bodies:
    b=b.strip(); head=re.match(r'\*\*(.*?)\*\*',b,re.S); head=head.group(1) if head else b[:200]
    kinds={k for k,p in PAT.items() if re.search(p,head,re.I)}
    t=re.findall(TAG,b)
    if t: kinds={t[-1]}
    if not (kinds & {'a correction','a withdrawal','a fault of mine','an open question'}): kinds.add('a finding')
    for k in kinds: cnt[k]+=1
print(len(ids),dict(cnt))