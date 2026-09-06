import numpy as np
C=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13]); 
K=np.array([.00640,.248,1.09,2.36,3.80,5.20,6.76,8.11,9.70,11.0,12.3,13.2,15.1])
U=np.array([.20,.20,.20,.20,.25,.20,.20,.20,.20,.20,.20,.20,.25])/2  # stated -> 1 sigma
cont=[100,100,99.9,99.6,98.8,95.1,92.8,86.3,79.2,69.4,68.3]
print(" C  min frac step   1sigma   step/sigma   containment")
for j,i in enumerate(range(1,12)):
    s=min(abs(K[i]-K[i-1]),abs(K[i+1]-K[i]))/K[i]
    print(f"{C[i]:3d}   {s:7.3f}      {U[i]:.3f}     {s/U[i]:6.2f}       {cont[j]:5.1f}%")