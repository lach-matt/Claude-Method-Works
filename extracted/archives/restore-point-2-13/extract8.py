#!/usr/bin/env python3
"""extract8.py — read the eight on-disk spectra and take the defects.

Register 1596 found eight species that are UNBOUNDED and UNWITNESSED with
their level tables already in `spectra_raw/`:

    Al IV · Ar I · Ba III · Bi II · Mg III · Rb I · Sc II · Y III

WHAT IS BEING EXTRACTED, and it is the asymptotic defect, not the ground one.
Register 1546 established these are different quantities and register 1575
measured the gap as l-dependent. For a Rydberg series in one (l, term) channel,

    E(n) = limit - R_M * z^2 / (n - delta)^2

so with three or more members delta can be fitted directly. With exactly two
the fit is exact and carries no residual, which register 727's two-member gate
already allows; with fewer than two the channel is refused.

THE LIMIT. Some files print it in the header, some say it was DERIVED by the
lowest-rms rule of register 1065. Where a limit is printed it is used; where it
is not, the channel is REFUSED rather than have the limit and the defect fitted
together, which would set the parameter that produces the answer (R 1445).

REDUCED MASS. R_M = R_inf / (1 + m_e / M) with M the atomic mass. Register 1376
computed the mass shift null for delta everywhere below 1e-3, so R_inf is used
and the choice is recorded rather than hidden.
"""
import os, re, math, collections

RINF = 109737.31568160          # cm^-1
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co "
       "Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb "
       "Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re "
       "Os Ir Pt Au Hg Tl Pb Bi").split()
Z = {s: i + 1 for i, s in enumerate(SYM)}
ROM = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}
LMAP = {"s": 0, "p": 1, "d": 2, "f": 3, "g": 4, "h": 5}

TARGETS = [("AlIV", 13, 4), ("ArI", 18, 1), ("BaIII", 56, 3), ("BiII", 83, 2),
           ("MgIII", 12, 3), ("RbI", 37, 1), ("ScII", 21, 2), ("YIII", 39, 3)]


def read(path):
    """(header, rows). A row is (config, term, J, level). Columns vary between
    files, so the row is parsed by SHAPE and never by fixed position."""
    head, rows = [], []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("#"):
            head.append(line)
            continue
        if not line.strip():
            continue
        f = line.split("\t")
        if f[0] == "config":
            continue
        nums = [i for i, x in enumerate(f) if re.fullmatch(r"-?\d+\.?\d*", x.strip())]
        if not nums:
            continue
        lvl = float(f[nums[-1]])
        rows.append((f[0].strip(), f[1].strip() if len(f) > 1 else "",
                     f[2].strip() if len(f) > 2 else "", lvl))
    return head, rows


# the H-Ar ladder supplies limits the level files do not print. Register 1596
# found it in the working root. It confirms Mg III's printed 646,402.0 to the
# digit — two independent sources agreeing — and supplies Ar I's 127,109.842.
LADLIM = {}
for _l in open("LADDER-H-Ar-I-III.tsv", encoding="utf-8"):
    if _l.startswith("#") or not _l.strip():
        continue
    _f = _l.rstrip("\n").split("\t")
    if _f[0] == "at_num":
        continue
    try:
        LADLIM[(int(_f[0]), int(_f[2].replace("+", "")) + 1)] = float(_f[6])
    except (ValueError, IndexError):
        pass


def limit_from(head):
    """the printed ionisation limit, or None. NEVER fitted alongside delta."""
    for h in head:
        if re.search(r"limit\s+(NOT|not)\s+printed", h):
            return None
        m = re.search(r"limit[^=]*=\s*([\d,]+\.?\d*)", h)
        if m:
            return float(m.group(1).replace(",", ""))
    return None


def channel(cfg):
    """(n, l) of the outer orbital named in the configuration string."""
    m = re.findall(r"(\d+)([spdfgh])", cfg)
    if not m:
        return None
    n, l = m[-1]
    return int(n), LMAP[l]


print("  THE EIGHT ON-DISK SPECTRA — reading, not fetching\n")
print(f"    {'species':<10}{'rows':>6}{'limit':>12}{'channels':>10}  note")
OUT = []
for fn, z, c in TARGETS:
    p = f"spectra_raw/{fn}.tsv"
    head, rows = read(p)
    lim = limit_from(head) or LADLIM.get((z, c))
    ch = collections.defaultdict(list)
    for cfg, term, J, lvl in rows:
        k = channel(cfg)
        if k:
            ch[(k[1], term)].append((k[0], lvl))
    note = "" if lim else "*** no printed limit — REFUSED ***"
    print(f"    {SYM[z-1]+' '+str(c):<10}{len(rows):>6}"
          f"{(f'{lim:,.1f}' if lim else '—'):>12}{len(ch):>10}  {note}")
    if not lim:
        continue
    for (l, term), pts in sorted(ch.items()):
        pts = sorted(set(pts))
        if len(pts) < 2:
            continue
        # delta from each member, then the asymptotic value as n -> inf
        ds = []
        for n, lvl in pts:
            E = lim - lvl
            if E <= 0:
                continue
            ds.append((n, n - c * math.sqrt(RINF / E)))
        if len(ds) < 2:
            continue
        OUT.append((z, c, l, term, ds))

print()
print("  THE DEFECTS, per channel. delta_n is the value at each member; the")
print("  ASYMPTOTIC value is the limit as n grows, taken as the highest member")
print("  where the series is flat and refused where it is not.")
print()
print(f"    {'species':<9}{'l':>2} {'term':<6}{'n range':>9}{'delta_n':>28}{'asymptotic':>12}{'flat?':>8}")
FINAL = []
for z, c, l, term, ds in OUT:
    ds = sorted(ds)
    ns = [n for n, _ in ds]
    vs = [d for _, d in ds]
    spread = max(vs) - min(vs)
    # the series is FLAT when the last two members agree to 0.02, which is the
    # tolerance the index's own filler is checked at (R 1576)
    flat = len(vs) >= 2 and abs(vs[-1] - vs[-2]) < 0.02
    asym = vs[-1]
    shown = " ".join(f"{v:.3f}" for v in vs[:5])
    print(f"    {SYM[z-1]+' '+str(c):<9}{'spdfgh'[l]:>2} {term:<6}"
          f"{f'{ns[0]}-{ns[-1]}':>9}{shown:>28}{asym:>12.4f}"
          f"{('yes' if flat else 'NO'):>8}")
    if flat:
        FINAL.append((z, c, l, term, asym, len(ds)))
print()
print(f"  ** {len(FINAL)} CHANNELS FLAT AND USABLE of {len(OUT)} with two or more members. **")
import json
json.dump([[z, c, l, t, a, n] for z, c, l, t, a, n in FINAL],
          open("/tmp/extracted8.json", "w"))
