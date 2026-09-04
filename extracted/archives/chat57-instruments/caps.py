from itertools import product
def count(capn,cape,capl,capk,capf):
    c=0
    for n in range(1,capn+1):
      for l in range(0,min(capl,n-1)+1):
        for k in range(1,min(capk,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,cape+1):
              for f in range(0,min(capf,e-1)+1):
                c+=(min(4*f+2,q)+1)*(k+1)
    return c
rows=[]
for capn in range(1,8):
  for cape in range(1,8):
    for capl in range(0,4):
      for capk in range(1,15):
        for capf in range(0,4):
          rows.append((count(capn,cape,capl,capk,capf),(capn,cape,capl,capk,capf)))
rows.sort()
import json; json.dump(rows,open('caps.json','w'))
print(len(rows)); print([r for r in rows if r[1]==(3,3,1,3,1)])
# candidate "seventeenfold" tops
print([r for r in rows if 16400<=r[0]<=16800][:10])
