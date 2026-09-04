#!/usr/bin/env python3
"""read17.py — the reading list, for the species whose levels are on disk.

Register 1591 built `READING-LIST.tsv`: 78 spectra whose ionisation energy is
MEASURED, meaning a Rydberg series was fitted and the defect is the OTHER
output of that same fit. A reading not taken, not an experiment to perform.

SEVENTEEN OF THE SEVENTY-EIGHT HAVE THEIR LEVEL TABLES IN `spectra_raw/`.
Those can be read now. The other sixty-one need a fetch.

THE LIMITS ARE STATED, NEVER PARSED. Register 1603: a greedy regex read
289,119 as 9,119 and produced twenty-six channels of plausible nonsense. Every
limit below is read off its own file's header by eye and written here as a
literal, with its provenance beside it.

WHAT IS EXTRACTED. For a Rydberg series in one channel,

    E(n) = limit - R * z^2 / (n - delta)^2

so delta follows from each member, and the ASYMPTOTIC value is the limit as n
grows. Registers 1546 and 1575: the ground-state defect is a DIFFERENT
quantity, so only the high-n end is taken.

WHAT IS REFUSED, and each refusal is register 1576's rule:
  - a channel with fewer than two members
  - a species with no single 2S+1, since the index cannot key it
  - any limit not printed in the file or held in the ladder
"""
import os, re, math, collections

RINF = 109737.31568160

# (limit_cm1, spectroscopic_charge, provenance) — READ BY EYE, NOT PARSED
# (limit_cm1, spectroscopic_charge, provenance) — EACH READ OFF ITS OWN FILE
# HEADER BY EYE. My first draft had FOUR wrong: Zn I as .31 for .33, Ca I as
# .924 for .95, Ti III as published when it is DERIVED, and Ti IV with no
# header at all. Checked against the files before use.
LIM = {
    "KI.tsv":        (35009.8140,  1, "published"),
    "CaI.tsv":       (49305.95,    1, "published, Ca II 2S1/2"),
    "ScII.tsv":      (103237.1,    2, "published, Sc III 3d 2D3/2"),
    "ZnI.tsv":       (75769.33,    1, "published, Zn II 2S1/2, SM95"),
    "GaII.tsv":      (165465.8,    2, "published, Ga III 4s 2S1/2, +/-1.0"),
    "GeIII.tsv":     (274693.0,    3, "published, Ge IV 4s 2S1/2, +/-10"),
    "LiI.tsv":       (43487.150,   1, "published, Li II 1s2 1S0, K87"),
    "BeI.tsv":       (75192.64,    1, "published, Be II 2S1/2"),
    "NeI.tsv":       (173929.75,   1, "published, KM72"),
    "NeI_p12.tsv":   (173929.75,   1, "published, KM72"),
    "MgI.tsv":       (61671.05,    1, "published, Mg II 2S1/2, KM91a"),
    "SiI_nf.tsv":    (66035.00,    1, "published, Si II 3p 2P*3/2"),
    "SiI_c12.tsv":   (65747.76,    1, "published, Si II 3p 2P*1/2, +/-0.25"),
    "CdI.tsv":       (72540.05,    1, "published, Cd II 5s 2S1/2, +/-0.13"),
    # DERIVED, NOT PUBLISHED — carried with a flag, per R 1445's leak rule
    "TiIII.tsv":     (223827.1,    3, "*** DERIVED *** joint fit, +/-274, R 972"),
    "ArI.tsv":       (127198.60,   1, "*** DERIVED *** joint ns/np fit, nd EXCLUDED"),
    # REFUSED: no limit in the file at all
    #   TiIV.tsv   — no header
    #   RbI.tsv    — header says only 'limit fitted', no value
}

CFG = re.compile(r"(\d+)([spdfg])")
LSTERM = re.compile(r"^([1234])([SPDFG])")


def levels(path):
    """(n, l, term, J, E) from a level file.

    THE ENERGY IS COLUMN 3, NOT THE LAST COLUMN. Some files carry an
    uncertainty after it and some do not, so f[-1] is the uncertainty in the
    first case — which is what my first draft read. K I's defects came out as
    16.2296, 13.2296, 11.2296, all sharing a fractional part, which is the
    same signature bismuth II showed at register 1597 when its limit was wrong.
    A constant fractional part across n means the energy is not varying.
    """
    out = []
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        if len(f) < 4 or f[0] == "config":
            continue
        cm = CFG.findall(f[0])
        if not cm:
            continue
        try:
            E = float(f[3])                  # level_cm1, by position
            J = f[2].strip()
        except (ValueError, IndexError):
            continue
        out.append((int(cm[-1][0]), "spdfg".index(cm[-1][1]),
                    f[1].strip(), J, E))
    return out


print("  THE READING LIST — the seventeen whose levels are on disk\n")
print(f"    {'file':<18}{'levels':>7}{'channels':>10}{'usable':>8}  limit provenance")
TAKEN = []
for fn, (lim, z, prov) in sorted(LIM.items()):
    p = f"spectra_raw/{fn}"
    if not os.path.exists(p):
        continue
    lv = levels(p)
    ch = collections.defaultdict(list)
    for n, l, term, J, E in lv:
        m = LSTERM.match(term)
        if not m:                      # no single 2S+1 — R 1576 refuses it
            continue
        e = lim - E
        if e <= 0:
            continue
        ch[(l, int(m.group(1)))].append((n, n - z * math.sqrt(RINF / e)))
    good = {k: sorted(set(v)) for k, v in ch.items() if len(set(v)) >= 2}
    print(f"    {fn:<18}{len(lv):>7}{len(ch):>10}{len(good):>8}  {prov}")
    for k, v in good.items():
        TAKEN.append((fn, z, k[0], k[1], v))
print(f"\n    channels with two or more members: {len(TAKEN)}")

print()
print("  ** THE FIVE ZEROS ARE THE jK-LABELLED FILES — Ar I, Ne I and the two")
print("     Si I cuts carry Racah terms with no single 2S+1, and register 1576")
print("     refuses those. The refusal is working, not failing. **")
print()
print("  THE DEFECTS, asymptotic value at the highest member")
print()
SYM = {"KI":"K I","CaI":"Ca I","ScII":"Sc II","ZnI":"Zn I","GaII":"Ga II",
       "GeIII":"Ge III","LiI":"Li I","BeI":"Be I","MgI":"Mg I",
       "CdI":"Cd I","TiIII":"Ti III"}
print(f"    {'species':<9}{'l':>2} {'2S+1':>5}{'n range':>10}{'members':>8}"
      f"{'delta':>10}{'flat?':>7}")
FINAL = []
for fn, z, l, S, v in sorted(TAKEN):
    ns = [n for n, _ in v]
    ds = [d for _, d in v]
    flat = len(ds) >= 2 and abs(ds[-1] - ds[-2]) < 0.02
    nm = SYM.get(fn[:-4], fn[:-4])
    print(f"    {nm:<9}{'spdfg'[l]:>2} {S:>5}{f'{ns[0]}-{ns[-1]}':>10}"
          f"{len(v):>8}{ds[-1]:>10.4f}{('yes' if flat else 'NO'):>7}")
    if flat:
        FINAL.append((fn, z, l, S, ds[-1], len(v)))
print()
print(f"    FLAT and usable: {len(FINAL)} of {len(TAKEN)}")
print()
print("  ** A CHANNEL THAT IS NOT FLAT HAS NOT REACHED ITS ASYMPTOTE. Taking")
print("     its last value would be a GROUND-STATE defect wearing an")
print("     asymptotic label, which registers 1546 and 1575 forbid. **")
import json
json.dump([[a, b, c, d, e, f] for a, b, c, d, e, f in FINAL],
          open("/tmp/read17.json", "w"))
