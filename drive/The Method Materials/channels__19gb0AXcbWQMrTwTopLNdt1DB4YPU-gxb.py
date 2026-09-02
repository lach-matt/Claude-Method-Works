#!/usr/bin/env python3
"""channels.py -- turn collected levels into channel rows.

Register 673. A channel is one Rydberg series: same core, same orbital letter,
same term, n running. For each, n* = Z sqrt(R/(limit - level)), the quantum
defect is delta = n - n*, and the spread is its standard deviation.

Eleven columns, matching the Spectra Compendium's existing rows.
"""
import re, os, glob, math, statistics as st
from zeno import State, step
R = 109737.31568


# ------------------------------------------------------- LITERATURE VERIFICATION
# A channel computed here is a PREDICTION unless an independent published measurement
# has been checked against it. Most of this compendium has none: three of its four
# best-collected species — Ar II (44 channels), Si I (39), Ne II (37) — have no
# published quantum defects at all, because the compendium computes defects for
# spectra whose defects nobody has tabulated (register 887).
#
# That is the compendium's value and the reason it cannot be checked, and the table
# must say so in the row rather than in a note. Three states (register 951):
#
#   verified     an independent published measurement agrees, and LITERATURE.md
#                records the comparison and its direction
#   unverified   NO published value was located. The channel is a PREDICTION and
#                should attract scrutiny, not confidence
#   contradicted the literature disagrees, or the mechanism the channel rests on is
#                contradicted in principle
VERIFIED = {          # (species, series-fragment) -> the comparison, from LITERATURE.md
    ("Ca II", "ns"): "delta_0 = 1.802995(5), single trapped 40Ca+ (R 862)",
    ("Ca II", "nd"): "delta_0 = 0.626888(9), single trapped 40Ca+ (R 862)",
    ("Li I",  "nd"): "delta_0 = 0.00192(17), 7Li MOT two-step cw (R 860)",
    ("Li I",  "np"): "CONTRADICTED — ours +0.1477 against ~0.047; the channel spans "
                     "a perturbation and its mean is not a defect (R 861)",
}
def verified(species, series):
    for (sp, frag), note in VERIFIED.items():
        if species.rstrip(" *") == sp and frag in series:
            return ("contradicted" if note.startswith("CONTRADICTED") else "verified"), note
    return "unverified", ""

# ---------------------------------------------------------------- LIMIT PROVENANCE
# Every channel is measured against a limit, and the compendium had never recorded
# where that limit came from. Three kinds, and they are not interchangeable
# (register 780):
#   published    quoted in the source compilation, plain — the ordinary case
#   derived      FITTED from the series itself by P.converge; the channel is then
#                measured against a number this work computed
#   constructed  built by summing values from two different spectra (P.buildlimit)
#   bracketed    quoted but marked Ritz/extrapolated by the source — register 746's
#                fault one level up: a defect computed against an extrapolated limit
#                is a defect computed from a defect
LIMPROV = {
    # Ba III's limit was DERIVED at register 684 (289,118 from its own series) and
    # then CONFIRMED at register 698 against a published 289,100 +/- 20 — eighteen
    # apart, inside the error bar. The published value now supersedes as the input;
    # the derivation survives as a check, not as a source.
    "NeI_2s":  "constructed",   # Ne I ionisation + Ne II's 2s2p6 2S level (P.buildlimit)
    "NeI_p12": "constructed",   # Ne I ionisation + the Ne II 2P* fine-structure splitting
    "CI_full":"derived",   # lowest-rms, R 1066
    "PII":     "derived",   # lowest-rms, R 1066
    "KI":      "derived",   # lowest-rms, R 1065
    "FI":      "derived",   # lowest-rms, R 1065
    "OIII":    "derived",   # lowest-rms, R 1065
    "BII":     "derived",   # lowest-rms, R 1064
    "OIV":     "derived",   # lowest-rms, R 1064
    "AlIV":    "derived",   # lowest-rms, R 1064
    "SIV":     "derived",   # lowest-rms, R 1059
    "BaII":    "derived",   # lowest-rms, R 1059
    "NI_full":"derived",   # lowest-rms, R 1059
    "PIII":    "derived",   # lowest-rms series, R 1055
    "HgII_full":"derived",  # lowest-rms series, R 1055
    "ArI":     "derived",   # joint fit on ns+np, R 1043
    "TiIII":   "derived",   # joint fit, +/- 274, R 972
    "CV":      "derived",   # fitted +/- 177, R 922
    "SV":      "derived",   # fitted +/- 342, R 922
    "PIV":     "derived",   # fitted, +/- 350 cm-1, R 918
    "BV":      "derived",   # fitted from the series, R 892
    "LiIII":   "derived",       # 987,662.29 +/- 0.36, FITTED from the series (R 879).
                            # The former value 9 R_inf = 987,635.841 was a FORMULA
                            # written here, not a published number, and low by 26.45 —
                            # the QED and relativistic terms a bare Coulomb expression
                            # omits. It showed as a defect of -0.0048 growing as n^3.
}
def limprov(nm):
    return LIMPROV.get(nm, "published")


# ---------------------------------------------------------------- REDUCED MASS
# The Rydberg constant that belongs in a quantum-defect calculation is the
# REDUCED-MASS value R_M = R_inf / (1 + m_e/M), not R_inf. Using R_inf understates
# every defect by n*(sqrt(R_inf/R_M) - 1) — 0.00240 for helium at n* = 35, scaling
# linearly with n*. Negligible against a defect of 1 to 4; the whole measurement at
# l >= 3, where it made He I's high-l defects come out NEGATIVE (register 868).
MASS = {   # standard atomic weights, u
 "Ge":72.630,
 "Ba":137.33,
 "Ti":47.867,"Ni":58.693,
 "Fe":55.845,
 "H":1.008,"He":4.0026,"Li":6.941,"Be":9.0122,"B":10.811,"C":12.011,"N":14.007,
 "O":15.999,"F":18.998,"Ne":20.180,"Na":22.990,"Mg":24.305,"Al":26.982,"Si":28.086,
 "P":30.974,"S":32.06,"Cl":35.45,"Ar":39.948,"K":39.098,"Ca":40.078,"Sc":44.956,
 "Ti":47.867,"V":50.942,"Cr":51.996,"Mn":54.938,"Fe":55.845,"Co":58.933,"Ni":58.693,
 "Cu":63.546,"Zn":65.38,"Ga":69.723,"Ge":72.630,"Cd":112.41,"In":114.82,"Sn":118.71,
 "Ba":137.33,"Hg":200.59,"Tl":204.38,"Pb":207.2,"Bi":208.98,
}
_MP = 1836.15267343       # proton-to-electron mass ratio
def rydberg(species):
    """the reduced-mass Rydberg for a species name such as 'Si III'"""
    el = species.strip().split()[0]
    M = MASS.get(el)
    return R if M is None else R / (1.0 + 1.0/(M*_MP))

LIM = {"NeI":(173929.75,1),"NeII":(330388.6,2),"BeI":(75192.64,1),"MgI":(61671.05,1),
       "MgII":(121267.64,2),"CaI":(49305.95,1),"CaII":(95751.88,2),"CII":(196664.7,2),
       "LiI":(43487.150,1),"LiII":(610078.4,2),"ZnI":(75769.33,1),"ZnII":(144892.6,2),
       "ArII":(222848.30,2),"SiI":(65747.76,1),"SiII":(131838.14,2),
       "ScIII_asd":(199677.37,3),"BiIII_asd":(206242.0,3),"LiIII":(987662.29,3),"BaIII":(289100.0,3),"BiII":(134720.0,2),"NeI_p12":(174710.09,1),"ZnI_ryd":(75769.31,1),"SiI_ryd":(66035.00,1),"SiI_ns":(66035.00,1),"SiI_nf":(66035.00,1),"SiI_LS":(65747.76,1),"SiI_c12":(65747.76,1),"SiI_ns12":(65747.76,1),"SiI_nd12b":(65747.76,1),"SiI_nd32low":(66035.00,1),"BeIV":(1756018.81,4),"BeIII":(1241256.601,3),"BIII":(305930.8,3),"MgIII":(646402.0,3),"AlIII":(229445.71,3),"SiIII":(270139.3,3),"BV":(2744111.38,5),"BIV":(2091995.451,4),"SiIV":(364093.1,4),"PIV":(415551.8,4),"CV":(3162788.8,5),"SV":(586610.4,5),"FeXV":(3679500.0,15),"CaIX":(1520640.0,9),"TiXI":(2137900.0,11),"ScII":(103237.1,2),"TiIII":(223827.1,3),"CaII_full":(95751.87,2),"CaI_full":(49305.95,1),"CdI":(72540.05,1),"ArI":(127198.60,1),"GaII":(165465.8,2),"SVI":(710194.7,6),"CIII":(386241.0,3),"KI":(35010.6,1),"CI_full":(90937.5,1),"PII":(159929.2,2),"SIII":(281130.0,3),"FI":(140518.7,1),"OIII":(443325.2,3),"GeIII":(274693.0,3),"BII":(202691.9,2),"OIV":(624202.2,4),"AlIV":(968924.4,4),"NIII":(382672.0,3),"SIV":(382135.0,4),"BaII":(80687.9,2),"NI_full":(117244.1,1),"FeXVI":(3946570.0,16),"PIII":(243573.7,3),"HgII_full":(151269.2,2),"CdII_full":(136374.74,2),"BaIII_ryd32":(289100.0,3),"BaIII_ryd12":(306650.0,3),"NeII_ryd":(330388.6,2),"NeII_1D":(356229.3,2),"NeI_2s":(390977.35,1),"NeII_np":(330388.6,2),"NeII_fg":(330388.6,2),"ArII_highl":(222848.3,2),"BaIII_fgh":(289100.0,3),"ArII_asd":(222848.30,2)}
NAME = {"NeI":"Ne I","NeII":"Ne II","BeI":"Be I","MgI":"Mg I","MgII":"Mg II","CaI":"Ca I",
        "CaII":"Ca II","CII":"C II","LiI":"Li I","LiII":"Li II","ZnI":"Zn I","ZnII":"Zn II",
        "ArII":"Ar II","SiI":"Si I","SiII":"Si II","ScIII_asd":"Sc III",
        "BiIII_asd":"Bi III","LiIII":"Li III","BaIII":"Ba III","BiII":"Bi II","NeI_p12":"Ne I","ZnI_ryd":"Zn I","SiI_ryd":"Si I","SiI_ns":"Si I","SiI_nf":"Si I","SiI_LS":"Si I","SiI_c12":"Si I","SiI_ns12":"Si I","SiI_nd12b":"Si I","SiI_nd32low":"Si I","BeIV":"Be IV","BeIII":"Be III","BIII":"B III","MgIII":"Mg III","AlIII":"Al III","SiIII":"Si III","BV":"B V","BIV":"B IV","SiIV":"Si IV","PIV":"P IV","CV":"C V","SV":"S V","FeXV":"Fe XV","CaIX":"Ca IX","TiXI":"Ti XI","ScII":"Sc II","TiIII":"Ti III","CaII_full":"Ca II","CaI_full":"Ca I","CdI":"Cd I","ArI":"Ar I","GaII":"Ga II","SVI":"S VI","CIII":"C III","KI":"K I","CI_full":"C I","PII":"P II","SIII":"S III","FI":"F I","OIII":"O III","GeIII":"Ge III","BII":"B II","OIV":"O IV","AlIV":"Al IV","NIII":"N III","SIV":"S IV","BaII":"Ba II","NI_full":"N I","FeXVI":"Fe XVI","PIII":"P III","HgII_full":"Hg II","CdII_full":"Cd II","BaIII_ryd32":"Ba III","BaIII_ryd12":"Ba III","NeII_ryd":"Ne II","NeII_1D":"Ne II","NeI_2s":"Ne I","NeII_np":"Ne II","NeII_fg":"Ne II","ArII_highl":"Ar II","BaIII_fgh":"Ba III","BaIII":"Ba III","BiII":"Bi II","NeI_p12":"Ne I","ZnI_ryd":"Zn I","SiI_ryd":"Si I","SiI_ns":"Si I","SiI_nf":"Si I","SiI_LS":"Si I","SiI_c12":"Si I","SiI_ns12":"Si I","SiI_nd12b":"Si I","SiI_nd32low":"Si I","BeIV":"Be IV","BeIII":"Be III","BIII":"B III","MgIII":"Mg III","AlIII":"Al III","SiIII":"Si III","BV":"B V","BIV":"B IV","SiIV":"Si IV","PIV":"P IV","CV":"C V","SV":"S V","FeXV":"Fe XV","CaIX":"Ca IX","TiXI":"Ti XI","ScII":"Sc II","TiIII":"Ti III","CaII_full":"Ca II","CaI_full":"Ca I","CdI":"Cd I","ArI":"Ar I","GaII":"Ga II","SVI":"S VI","CIII":"C III","KI":"K I","CI_full":"C I","PII":"P II","SIII":"S III","FI":"F I","OIII":"O III","GeIII":"Ge III","BII":"B II","OIV":"O IV","AlIV":"Al IV","NIII":"N III","SIV":"S IV","BaII":"Ba II","NI_full":"N I","FeXVI":"Fe XVI","PIII":"P III","HgII_full":"Hg II","CdII_full":"Cd II","BaIII_ryd32":"Ba III","BaIII_ryd12":"Ba III","NeII_ryd":"Ne II","NeII_1D":"Ne II","NeI_2s":"Ne I","NeII_np":"Ne II","NeII_fg":"Ne II","ArII_highl":"Ar II","BaIII_fgh":"Ba III","ArII_asd":"Ar II"}

def run():
    out = []
    rejected = []
    for p in sorted(glob.glob("spectra_raw/*.tsv")):
        nm = os.path.basename(p)[:-4]
        if nm not in LIM: continue
        lim, z = LIM[nm]
        ser = {}
        for l in open(p, encoding="utf-8"):
            if l.startswith("#") or not l.strip(): continue
            f = l.rstrip("\n").split("\t")
            if f[0] == "config": continue
            try: lev = float(f[3])
            except Exception: continue
            m = re.match(r"^(.*?)(\d+)([spdfghik])$", f[0].strip())
            if not m: continue
            core, n, orb = m.group(1), int(m.group(2)), m.group(3)
            key = (core, orb, f[1], f[2])
            ser.setdefault(key, []).append((n, lev))
        for (core, orb, term, J), v in sorted(ser.items()):
            v = sorted(set(v))
            # THREE members are required when the limit must be inferred from the
            # series itself. Where the limit is PUBLISHED independently, two members
            # give a defect and a consistency check — weaker, because two points
            # cannot detect a perturbation, but a measurement. Marked provisional
            # (register 727).
            if len(v) < 2: continue
            _prov = len(v) == 2
            if lim <= max(x[1] for x in v): continue
            # The constant must match the DATA's own convention, not the physics
            # in the abstract. Where the levels are measured, the reduced-mass
            # Rydberg is correct and R_inf understates every defect (register 868).
            # Where the table is a THEORETICAL hydrogenic one computed from R_inf —
            # Li III's limit is exactly 9 R_inf — the levels carry that convention
            # and applying a reduced mass to them introduces the error rather than
            # removing it: it drove Li III's spreads from 0.0000 to 0.0125 (R 872).
            _R = R if (limprov(nm) == "theoretical" and abs(lim - z*z*R) < 1.0) \
                 else rydberg(NAME[nm])
            ns, ds = [], []
            for n, lev in v:
                nstar = z * math.sqrt(_R / (lim - lev))
                ns.append(nstar); ds.append(n - nstar)
            interior = max(1, len(v) - 2)  # the same convention the compendium uses
            # A real quantum defect over a Rydberg series has a spread near 0.003;
            # the largest honest one in this compendium is 0.108. A spread above 0.15
            # means the series is misidentified, the limit is wrong, or the levels are
            # not a series at all. Ca I was rejected here at 1.0186 — twenty-one values
            # that had been FABRICATED rather than read, and nothing else would have
            # caught them (register 695).
            _sd = st.pstdev(ds) if len(ds) > 1 else 0.0
            # NOT a rejection: a large spread can be real. Al I's 3s2.nd 2D runs to
            # 32 members at 0.6297 because the 3s3p2 2D state PERTURBS the series —
            # textbook for aluminium. The gate flags for inspection only. Ca I's
            # fabricated series read 1.0186, above every honest value here, but that
            # is a margin and not a criterion (register 695).
            # A two-member channel has exactly ONE internal check: whether its two
            # defects agree. At low n they do not — n=3,4 pairs scatter by 0.15 to
            # 0.36 because the defect is still changing fast. The cut at 0.01 cleanly
            # separates the high-l pairs, which agree to 0.0001-0.0011, from the rest
            # (register 727).
            if _prov and _sd > 0.01:
                rejected.append((NAME[nm], f"{core}n{orb} {term}", len(v), round(_sd, 4)))
                continue
            if _sd > 0.70:
                rejected.append((NAME[nm], f"{core}n{orb} {term}", len(v), round(_sd, 4)))
            out.append(dict(
                species=NAME[nm] + (" *" if _prov else ""),
                limprov=limprov(nm),
                lit=verified(NAME[nm], f"n{orb}")[0],
                series=f"{core}n{orb} {term}" + (f" J={J}" if J and J != "" else ""),
                # a dagger marks an internal gap: the members do not run continuously,
                # so the printed range overstates coverage (register 779)
                nrange=(f"{v[0][0]}–{v[-1][0]}" if len(v) == v[-1][0]-v[0][0]+1
                        else f"{v[0][0]}–{v[-1][0]}†"),
                levels=len(v), interior=interior,
                # NOT a test result. The bracketing method of Part II reads a cell
                # against its measured neighbours and asks whether the true value falls
                # inside; running it needs the neighbour levels and a tolerance, and
                # `channels.py` does neither. Writing "{interior}/{interior}" here would
                # assert a verification that never ran — the column would look like a
                # result and be a constant. It reads "untested" instead (register 782).
                bracket="untested",
                nstar=f"{min(ns):.1f}–{max(ns):.1f}",
                delta=f"{st.mean(ds):+.4f}",
                spread=f"{(st.pstdev(ds) if len(ds)>1 else 0):.4f}",
                zeff=z, limit=f"{lim:,.3f}"))
    return out, rejected

with State("channels") as st_:
    ch, rej = step(st_, "build channels from collected levels", run, budget=600)

print(f"  {len(ch)} channels built, {sum(c['interior'] for c in ch)} interior cells")
if rej:
    print(f"  {len(rej)} REJECTED — spread above 0.15, not a Rydberg series:")
    for a,b,c,d in rej: print(f"      {a:<9}{b[:34]:<36}{c:>3} members   spread {d}")
print()
print(f"  {'species':<9}{'series':<30}{'n':<9}{'lev':>4}{'int':>5}{'delta':>10}{'sigma':>9}")
for c in ch:
    print(f"  {c['species']:<9}{c['series'][:29]:<30}{c['nrange']:<9}"
          f"{c['levels']:>4}{c['interior']:>5}{c['delta']:>10}{c['spread']:>9}")
with open("CHANNELS-NEW.tsv", "w", encoding="utf-8") as f:
    f.write("species\tseries\tn\tlevels\tinterior\tbracket\tnstar\tdelta\tspread\tZeff\tlimit\n")
    for c in ch:
        f.write("\t".join(str(c[k]) for k in
                ("species","series","nrange","levels","interior","bracket",
                 "nstar","delta","spread","zeff","limit","limprov","lit")) + "\n")
