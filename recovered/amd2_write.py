import json,re,sys
B='/home/claude/build/build.py'
BOUND=" ],\n 'The_Method_1_6___Mathematical_Compendium-2.md': [\n"
def write(jsonfile,label):
    src=open(B,encoding='utf-8').read()
    assert src.count(BOUND)==1, 'boundary occurs %d times'%src.count(BOUND)
    pairs=json.load(open(jsonfile))
    blk='  # --- '+label+'\n'
    for n,a,rep in pairs:
        blk+='  (%r,\n   %r),   # L%d\n'%(a,rep,n)
    open(B,'w',encoding='utf-8').write(src.replace(BOUND,blk+BOUND,1))
    return len(pairs)
if __name__=='__main__':
    print('wrote',write(sys.argv[1],sys.argv[2]),'pairs')