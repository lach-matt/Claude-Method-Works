# Register front matter, "What the entries are": counts of entries whose HEADLINE matches each pattern
# (case-insensitive; a body tag "(a finding.)" etc. overrides). Kinds overlap; not a partition.
import re,collections,sys
R=open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
i=R.find('\n### 1\n'); body=R[i:]
ents=re.split(r'\n### ([\d, a-z]+)\n',body)
ids,bodies=ents[1::2],ents[2::2]
# RULING (chat 52): count the whole register 1-1786; the genesis supersession stubs 95-164 are
# provenance, not categorised entries, and are dropped.
_keep=[(x,b) for x,b in zip(ids,bodies) if not (x.strip().isdigit() and 95<=int(x.strip())<=164)]
ids=[x for x,_ in _keep]; bodies=[b for _,b in _keep]
PAT={
 'a correction':   r'CORRECT|WRONG|STALE|PUT RIGHT|AMEND|FIX|MISLOCAT|REPAIR|ERROR|OVERTAKEN|MISTAK|MISREAD|MISCOUNT',
 'a measurement':  r'\d',
 'prior art':      r'PRIOR ART|PUBLISHED|ALREADY (KNOWN|IN|DONE)|\b(1[5-9]\d\d|20[0-2]\d)\b|[A-Z][a-z]+ \(\d{4}\)',
 'a withdrawal':   r'WITHDR|RETRACT|REMOVED|DROPPED|ABANDON|DISCARD',
 'a fault of mine':r'FAULT OF MINE|MY FAULT|MY ERROR|THE ASSISTANT|I (MIS|FAIL|WROTE|CARRIED)|MEA CULPA',
 'an open question':r'OPEN QUESTION|\bOPEN\b|UNSETTLED|CANNOT (CURRENTLY|YET)|UNKNOWN|UNRESOLVED|NOT (YET )?(SETTLED|KNOWN)',
}
TAG=r'\(\s*(a finding|a correction|a measurement|prior art|a new protocol|a withdrawal|a fault of mine|an open question)\.?\s*\)\*?\s*$'
# 'a new protocol' is decided by an EXPLICIT, read-and-judged list (chat 52), not by a keyword — because
# "rule"/"must"/"ruling" are used for physics laws and for workshop protocols alike and no pattern
# separates them. The 24 below were judged one at a time. PROTO_PAT is kept only as a REVIEW FLAG: it
# surfaces keyword-matched entries not on the list so a future protocol candidate is noticed; it never
# adds to the count.
PROTO_IDS={168,185,323,374,506,514,515,587,1336,1355,1383,1673,1683,1694,1699,1722,1738,1740,1751,1758,1761,1762,1763,1768}
PROTO_PAT=r'PROTOCOL|\bRULE\b|RULED|RULING|MUST\b|NEVER AGAIN|PROCEDURE'
cnt=collections.Counter(); _proto_flag=[]
for i,b in zip(ids,bodies):
    b=b.strip(); head=re.match(r'\*\*(.*?)\*\*',b,re.S); head=head.group(1) if head else b[:200]
    kinds={k for k,p in PAT.items() if re.search(p,head,re.I)}
    if i.strip().isdigit() and int(i.strip()) in PROTO_IDS: kinds.add('a new protocol')
    elif re.search(PROTO_PAT,head,re.I): _proto_flag.append(i.strip())   # review flag only
    t=re.findall(TAG,b)
    if t: kinds={t[-1]}
    if ',' in i: kinds|={'a correction','a fault of mine'}   # grouped early fault entries, by mechanism
    if not (kinds & {'a correction','a withdrawal','a fault of mine','an open question'}): kinds.add('a finding')
    for k in kinds: cnt[k]+=1
print(len(ids),dict(cnt))
if _proto_flag: print('protocol REVIEW candidates (keyword match, not on list):',_proto_flag)
if '--write' in sys.argv:   # rewrite the Build 9 column and the heading count in the Register front matter
    R2=R
    for k,n in cnt.items():
        R2,c=re.subn(r'(\| \*\*'+re.escape(k)+r'\*\* \| )[\d,]+( \| )',lambda m:m.group(1)+f'{n:,}'+m.group(2),R2,count=1); assert c==1,k
    R2,c=re.subn(r'over the [\d,]+ entry headings',f'over the {len(ids):,} entry headings',R2); assert c==1
    open(sys.argv[1],'w',encoding='utf-8').write(R2); print('written')
