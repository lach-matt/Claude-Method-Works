#!/usr/bin/env python3
"""ground.py -- the OBSERVED ground configurations, Z = 1 to 108.

NIST ASD ver. 5.12, GSIE interface, retrieved 2026-08-09:
    Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD Team (2024).
    NIST Atomic Spectra Database, DOI 10.18434/T4W30F.

Register 1306. Every previous version of this work built configurations by aufbau
and patched the exceptions by hand. That table was wrong at Pd -- aufbau plus my
patch gave [Kr]4d9 5s, and the observed configuration is [Kr]4d10 with no 5s at
all -- and at Lr, which is [Rn]5f14 7s2 7p and not 6d.

This file is READ, not computed. It is the ordering the Loewdin challenge asks
about, stated by measurement.
"""
CORE = {"Ne":10, "Ar":18, "Kr":36, "Cd":48, "Xe":54, "Hg":80, "Rn":86}
CORECFG = {
 "Ne":"1s2 2s2 2p6",
 "Ar":"1s2 2s2 2p6 3s2 3p6",
 "Kr":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
 "Cd":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
 "Xe":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
 "Hg":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2",
 "Rn":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6"}

# Z : (element, ground shells as printed, ground level)
GROUND = {
1:("H","1s","2S1/2"), 2:("He","1s2","1S0"), 3:("Li","1s2 2s","2S1/2"),
4:("Be","1s2 2s2","1S0"), 5:("B","1s2 2s2 2p","2P*1/2"), 6:("C","1s2 2s2 2p2","3P0"),
7:("N","1s2 2s2 2p3","4S*3/2"), 8:("O","1s2 2s2 2p4","3P2"),
9:("F","1s2 2s2 2p5","2P*3/2"), 10:("Ne","1s2 2s2 2p6","1S0"),
11:("Na","[Ne]3s","2S1/2"), 12:("Mg","[Ne]3s2","1S0"), 13:("Al","[Ne]3s2 3p","2P*1/2"),
14:("Si","[Ne]3s2 3p2","3P0"), 15:("P","[Ne]3s2 3p3","4S*3/2"),
16:("S","[Ne]3s2 3p4","3P2"), 17:("Cl","[Ne]3s2 3p5","2P*3/2"),
18:("Ar","[Ne]3s2 3p6","1S0"),
19:("K","[Ar]4s","2S1/2"), 20:("Ca","[Ar]4s2","1S0"),
21:("Sc","[Ar]3d 4s2","2D3/2"), 22:("Ti","[Ar]3d2 4s2","3F2"),
23:("V","[Ar]3d3 4s2","4F3/2"), 24:("Cr","[Ar]3d5 4s","7S3"),
25:("Mn","[Ar]3d5 4s2","6S5/2"), 26:("Fe","[Ar]3d6 4s2","5D4"),
27:("Co","[Ar]3d7 4s2","4F9/2"), 28:("Ni","[Ar]3d8 4s2","3F4"),
29:("Cu","[Ar]3d10 4s","2S1/2"), 30:("Zn","[Ar]3d10 4s2","1S0"),
31:("Ga","[Ar]3d10 4s2 4p","2P*1/2"), 32:("Ge","[Ar]3d10 4s2 4p2","3P0"),
33:("As","[Ar]3d10 4s2 4p3","4S*3/2"), 34:("Se","[Ar]3d10 4s2 4p4","3P2"),
35:("Br","[Ar]3d10 4s2 4p5","2P*3/2"), 36:("Kr","[Ar]3d10 4s2 4p6","1S0"),
37:("Rb","[Kr]5s","2S1/2"), 38:("Sr","[Kr]5s2","1S0"),
39:("Y","[Kr]4d 5s2","2D3/2"), 40:("Zr","[Kr]4d2 5s2","3F2"),
41:("Nb","[Kr]4d4 5s","6D1/2"), 42:("Mo","[Kr]4d5 5s","7S3"),
43:("Tc","[Kr]4d5 5s2","6S5/2"), 44:("Ru","[Kr]4d7 5s","5F5"),
45:("Rh","[Kr]4d8 5s","4F9/2"), 46:("Pd","[Kr]4d10","1S0"),
47:("Ag","[Kr]4d10 5s","2S1/2"), 48:("Cd","[Kr]4d10 5s2","1S0"),
49:("In","[Cd]5p","2P*1/2"), 50:("Sn","[Cd]5p2","3P0"),
51:("Sb","[Cd]5p3","4S*3/2"), 52:("Te","[Cd]5p4","3P2"),
53:("I","[Cd]5p5","2P*3/2"), 54:("Xe","[Cd]5p6","1S0"),
55:("Cs","[Xe]6s","2S1/2"), 56:("Ba","[Xe]6s2","1S0"),
57:("La","[Xe]5d 6s2","2D3/2"), 58:("Ce","[Xe]4f 5d 6s2","1G*4"),
59:("Pr","[Xe]4f3 6s2","4I*9/2"), 60:("Nd","[Xe]4f4 6s2","5I4"),
61:("Pm","[Xe]4f5 6s2","6H*5/2"), 62:("Sm","[Xe]4f6 6s2","7F0"),
63:("Eu","[Xe]4f7 6s2","8S*7/2"), 64:("Gd","[Xe]4f7 5d 6s2","9D*2"),
65:("Tb","[Xe]4f9 6s2","6H*15/2"), 66:("Dy","[Xe]4f10 6s2","5I8"),
67:("Ho","[Xe]4f11 6s2","4I*15/2"), 68:("Er","[Xe]4f12 6s2","3H6"),
69:("Tm","[Xe]4f13 6s2","2F*7/2"), 70:("Yb","[Xe]4f14 6s2","1S0"),
71:("Lu","[Xe]4f14 5d 6s2","2D3/2"), 72:("Hf","[Xe]4f14 5d2 6s2","3F2"),
73:("Ta","[Xe]4f14 5d3 6s2","4F3/2"), 74:("W","[Xe]4f14 5d4 6s2","5D0"),
75:("Re","[Xe]4f14 5d5 6s2","6S5/2"), 76:("Os","[Xe]4f14 5d6 6s2","5D4"),
77:("Ir","[Xe]4f14 5d7 6s2","4F9/2"), 78:("Pt","[Xe]4f14 5d9 6s","3D3"),
79:("Au","[Xe]4f14 5d10 6s","2S1/2"), 80:("Hg","[Xe]4f14 5d10 6s2","1S0"),
81:("Tl","[Hg]6p","2P*1/2"), 82:("Pb","[Hg]6p2","(1/2,1/2)0"),
83:("Bi","[Hg]6p3","4S*3/2"), 84:("Po","[Hg]6p4","3P2"),
85:("At","[Hg]6p5","2P*3/2"), 86:("Rn","[Hg]6p6","1S0"),
87:("Fr","[Rn]7s","2S1/2"), 88:("Ra","[Rn]7s2","1S0"),
89:("Ac","[Rn]6d 7s2","2D3/2"), 90:("Th","[Rn]6d2 7s2","3F2"),
91:("Pa","[Rn]5f2 6d 7s2","4K11/2"), 92:("U","[Rn]5f3 6d 7s2","5L*6"),
93:("Np","[Rn]5f4 6d 7s2","6L11/2"), 94:("Pu","[Rn]5f6 7s2","7F0"),
95:("Am","[Rn]5f7 7s2","8S*7/2"), 96:("Cm","[Rn]5f7 6d 7s2","9D*2"),
97:("Bk","[Rn]5f9 7s2","6H*15/2"), 98:("Cf","[Rn]5f10 7s2","5I8"),
99:("Es","[Rn]5f11 7s2","4I*15/2"), 100:("Fm","[Rn]5f12 7s2","3H6"),
101:("Md","[Rn]5f13 7s2","2F*7/2"), 102:("No","[Rn]5f14 7s2","1S0"),
103:("Lr","[Rn]5f14 7s2 7p","2P*1/2"), 104:("Rf","[Rn]5f14 6d2 7s2","3F2"),
105:("Db","[Rn]5f14 6d3 7s2","4F3/2"), 106:("Sg","[Rn]5f14 6d4 7s2","0"),
107:("Bh","[Rn]5f14 6d5 7s2","5/2"), 108:("Hs","[Rn]5f14 6d6 7s2","4"),
}

import re
_L = {"s":0, "p":1, "d":2, "f":3, "g":4}

def expand(Z):
    """the ground configuration as a list of (n, l, occ), cores expanded"""
    _, sh, _lv = GROUND[Z]
    m = re.match(r"\[(\w\w)\](.*)", sh)
    txt = (CORECFG[m.group(1)] + " " + m.group(2)) if m else sh
    out = []
    for tok in txt.split():
        t = re.match(r"(\d+)([spdfg])(\d*)", tok)
        if t: out.append((int(t.group(1)), _L[t.group(2)], int(t.group(3) or 1)))
    return out

def occ_count(Z):
    return sum(o for _, _, o in expand(Z))

def core_p(Z, l):
    """orbitals of this l in the ground configuration of the atom with Z electrons"""
    return sum(1 for n, ll, o in expand(Z) if ll == l and o > 0)

def outer(Z):
    """the outermost subshell by (n, l) in filling order -- the LAST one listed"""
    return expand(Z)[-1]

if __name__ == "__main__":
    print("  THE OBSERVED GROUND CONFIGURATIONS  —  NIST ASD 5.12\n")
    bad = [Z for Z in GROUND if occ_count(Z) != Z]
    print(f"      {len(GROUND)} elements · electron count checks: "
          f"{len(GROUND)-len(bad)}/{len(GROUND)}")
    if bad: print(f"      mismatched: {bad}")
    print()
    print("  THE FILLING SEQUENCE, READ FROM THE CONFIGURATIONS\n")
    prev = None; seq = []
    for Z in range(1, 109):
        cur = {(n, l): o for n, l, o in expand(Z)}
        if prev is not None:
            new = [k for k in cur if k not in prev or cur[k] > prev.get(k, 0)]
            gone = [k for k in prev if k not in cur or cur[k] < prev.get(k, 0)]
            if new:
                for k in new:
                    if k not in [s[0] for s in seq]: seq.append((k, Z))
        prev = cur
    L = "spdfg"
    print("      " + "  ".join(f"{n}{L[l]}" for (n, l), Z in seq))
    print()
    print(f"      {len(seq)} subshells opened across Z = 1 to 108")
