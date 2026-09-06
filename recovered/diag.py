import sys,os,math,numpy as np
sys.path.insert(0,'/home/claude/s88/pack88'); import prof88 as P, semi85 as S85
h,row,r,chans=P.row_channels(24); order=P.shells_by_r(h); print(order)
for tag,n,l,E,q,R,rank in chans:
    if R is None: continue
    for k in range(1,len(order)):
        y=P.profile_J(E,l,r,q,P.q_sub(h,order[:k]),R)
        print(tag, k, 'refused' if y['refused'] else 'ok', 'conv_rem=%.4f'%y['conv_rem'], 'b0p=%.4f b1p=%.4f'%(y['b0p'],y['b1p']), 'Kc=%.4f'%y['Kc'])