import numpy as np, eldata as ed
from collections import Counter
# Pettifor Mendeleev numbers
MN={1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,
17:99,19:10,20:16,21:19,22:51,23:54,24:57,25:60,26:61,27:64,28:67,29:72,30:76,31:81,
32:84,33:89,34:93,35:98,37:9,38:15,39:20,40:49,41:53,42:56,43:59,44:62,45:65,46:69,
47:71,48:75,49:79,50:83,51:88,52:92,53:97,55:8,56:14,57:33,58:32,59:31,60:30,62:28,
63:18,64:27,65:26,66:25,67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,76:63,
77:63,78:66,79:70,80:74,81:78,82:82,83:87,84:91,85:96,90:47,92:45}
# Binary AB compounds with well-established structure types.
# Compiled from standard inorganic/intermetallic references.
AB=[
# rock salt B1
('Li','F','B1'),('Na','F','B1'),('K','F','B1'),('Rb','F','B1'),('Na','Cl','B1'),
('K','Cl','B1'),('Rb','Cl','B1'),('Li','Cl','B1'),('Na','Br','B1'),('K','Br','B1'),
('Li','Br','B1'),('Na','I','B1'),('K','I','B1'),('Li','I','B1'),('Rb','Br','B1'),
('Mg','O','B1'),('Ca','O','B1'),('Sr','O','B1'),('Ba','O','B1'),('Mn','O','B1'),
('Fe','O','B1'),('Co','O','B1'),('Ni','O','B1'),('Cd','O','B1'),('Ca','S','B1'),
('Sr','S','B1'),('Ba','S','B1'),('Mn','S','B1'),('Pb','S','B1'),('Pb','Se','B1'),
('Pb','Te','B1'),('Sn','Te','B1'),('Ca','Se','B1'),('Ba','Se','B1'),('Sc','N','B1'),
('Ti','N','B1'),('V','N','B1'),('Zr','N','B1'),('Ti','C','B1'),('Zr','C','B1'),
('V','C','B1'),('Nb','C','B1'),('Ta','C','B1'),('Hf','C','B1'),
# zinc blende B3
('Zn','S','B3'),('Zn','Se','B3'),('Zn','Te','B3'),('Cd','Te','B3'),('Hg','S','B3'),
('Hg','Se','B3'),('Hg','Te','B3'),('Ga','As','B3'),('Ga','P','B3'),('Ga','Sb','B3'),
('In','P','B3'),('In','As','B3'),('In','Sb','B3'),('Al','As','B3'),('Al','P','B3'),
('Al','Sb','B3'),('Be','S','B3'),('Be','Se','B3'),('Be','Te','B3'),('Cu','Cl','B3'),
('Cu','Br','B3'),('Cu','I','B3'),('B','N','B3'),('B','P','B3'),('B','As','B3'),
# wurtzite B4
('Zn','O','B4'),('Al','N','B4'),('Ga','N','B4'),('In','N','B4'),('Be','O','B4'),
('Cd','S','B4'),('Cd','Se','B4'),('Ag','I','B4'),('Mn','Te','B4'),
# CsCl B2 (salts + intermetallics)
('Cs','Cl','B2'),('Cs','Br','B2'),('Cs','I','B2'),('Tl','Cl','B2'),('Tl','Br','B2'),
('Tl','I','B2'),('Ni','Al','B2'),('Co','Al','B2'),('Fe','Al','B2'),('Cu','Zn','B2'),
('Ag','Mg','B2'),('Au','Zn','B2'),('Li','Ag','B2'),('Li','Hg','B2'),('Mg','Tl','B2'),
('Ni','Ti','B2'),('Cu','Pd','B2'),('Ag','Cd','B2'),('Au','Cd','B2'),('Be','Cu','B2'),
('Ru','Al','B2'),('Rh','Al','B2'),('Pd','In','B2'),
# NiAs B8
('Ni','As','B8'),('Fe','S','B8'),('Co','S','B8'),('Ni','S','B8'),('Cr','S','B8'),
('Fe','Se','B8'),('Co','Se','B8'),('Ni','Se','B8'),('Cr','Se','B8'),('Ni','Sb','B8'),
('Pt','Sn','B8'),('Mn','As','B8'),('Fe','Te','B8'),('Ni','Te','B8'),('Cr','Sb','B8'),
# CuAu L10
('Cu','Au','L10'),('Fe','Pt','L10'),('Co','Pt','L10'),('Mn','Ni','L10'),('Ti','Al','L10'),
('Fe','Pd','L10'),('Mn','Pt','L10'),('Cr','Pt','L10'),
# NaTl B32 (Zintl)
('Na','Tl','B32'),('Li','Al','B32'),('Li','Zn','B32'),('Li','Cd','B32'),('Li','In','B32'),
('Li','Ga','B32'),
# CrB B33
('Cr','B','B33'),('Mo','B','B33'),('Ta','B','B33'),('Nb','B','B33'),('W','B','B33'),
# FeB B27
('Fe','B','B27'),('Mn','B','B27'),('Co','B','B27'),('Ni','B','B27'),
]
SYM2Z={v:k for k,v in ed.SYM.items()}
rows=[]
for a,b,st in AB:
    za,zb=SYM2Z[a],SYM2Z[b]
    if za not in MN or zb not in MN: continue
    rows.append(dict(A=a,B=b,st=st,za=za,zb=zb))
print(f"binary AB compounds with Pettifor data: {len(rows)}")
print("structure types:",dict(Counter(r['st'] for r in rows)))
import json
json.dump(rows,open('/home/claude/ab.json','w'))
json.dump(MN,open('/home/claude/mn.json','w'))