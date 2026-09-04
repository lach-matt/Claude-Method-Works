# Amendment 2 / Ruling 61 — the MECHANISMS.md family. G0p: anchors EXTRACTED. G0q: validated IN POSITION.
import ast, sys
REG='The_Method_1_6___The_Register-2.md'
src=open('build.py',encoding='utf-8',errors='surrogateescape').read()
for n in ast.parse(src).body:
    if isinstance(n,ast.Assign) and getattr(n.targets[0],'id',None)=='SUBS': S=ast.literal_eval(n.value)
# the text a NEWLY APPENDED pair actually meets: after all existing pairs fire, in order
t=open(REG,encoding='utf-8',errors='surrogateescape').read()
for a,b in S[REG]:
    assert t.count(a)==1, 'existing pair broken: %r' % a[:60]
    t=t.replace(a,b)

SPEC=[
 (1957, '*`MECHANISMS.md` holds*',
        '*The P family, set out in the Mathematical Compendium at § P. The spectral mechanisms, holds*'),
 (2009, '**`MECHANISMS.md` GAINS P.polar',
        "**THE MATHEMATICAL COMPENDIUM'S P FAMILY GAINS P.polar"),
 (2189, 'The mechanism list held fifteen, `MECHANISMS.md` fourteen — P.termsplit was registered at 739 and never given an entry — and `QUEUE.md` still named the ten of register 720.',
        'One list held fifteen, a second fourteen — P.termsplit was registered at 739 and never given an entry — and a third still named the ten of register 720.'),
 (3077, '*Their evidence lives in the analysis scripts and in `MECHANISMS.md`, which is not the same as a verifier that reruns on every build.*',
        '*Their evidence lives in the analysis and in the P family listing at § P. The spectral mechanisms of the Mathematical Compendium, which is not the same as a standing verifier.*'),
]
L=t.split('\n')
run=t; ok=[]
for ln,a,b in SPEC:
    line=L[ln-1]
    assert line.count(a)==1, 'L%d: anchor occurs %d times ON ITS LINE' % (ln, line.count(a))
    assert run.count(a)==1, 'L%d: anchor occurs %d times IN THE SWEPT FILE' % (ln, run.count(a))
    assert a!=b, 'L%d: anchor equals replacement' % ln
    assert b not in run, 'L%d: replacement already present' % ln
    run=run.replace(a,b)          # IN POSITION — later anchors meet the earlier replacements
    ok.append((a,b))
    print('L%-5d VALID  anchor %d ch -> %d ch' % (ln, len(a), len(b)))
print('ALL %d VALIDATED IN POSITION' % len(ok))
print('split-lines before %d  after %d' % (len(t.split('\n')), len(run.split('\n'))))
for nm in ('MECHANISMS.md','QUEUE.md'):
    print('%-16s remaining after these pairs: %d' % (nm, run.count(nm)))
import json; json.dump(ok, open('/home/claude/work/amd2_mech.json','w'))