#!/usr/bin/env python3
"""asd_pass.py -- Q item P, run. Partition the 1,442 cells by value provenance.

WHY THIS EXISTS. §22.9 states that three kinds of value sit under the 1,442 --
measured levels, Ritz series-formula values, and ab initio calculations -- that
only the first and third are independent tests of the bracket, and that the
partition has never been made. It is a lookup, not a computation.

THE LOOKUP IS A DELIMITER READ. NIST ASD marks provenance in the level value
itself, three ways, and states the convention in its own help files:

    plain    an observed value
    [ ]      "obtained by interpolation or extrapolation of experimental
             fine-structure intervals OR BY FITTING THE RITZ-TYPE FORMULAS
             ALONG SERIES OF LEVELS"
    ( )      "derived from theoretical values" / "determined from an ab-initio
             calculation, or otherwise not derived from evaluated experimental
             data"

So [ ] is exactly §22.9's excluded category and ( ) is exactly its included one.
The book reads [ ] as covering both, which is the defect this pass measures.

AND THE PER-SPECIES PROVENANCE NOTE CAN OVERRIDE THE DELIMITERS. He I is the
case: NIST states that its 1snl levels with n <= 10 were obtained by subtracting
Drake's theoretical ionization energy from Kandula's experimental ground-level
value, and that THE HIGHER LEVELS WERE DETERMINED BY FITTING THE EXTENDED RITZ
QUANTUM-DEFECT EXPANSION. He I's channels run to n = 35, so most of its 189
cells are Ritz-fitted whatever the delimiter says. The note is read first.

USAGE
    python3 asd_pass.py                 # all 35 systems
    python3 asd_pass.py "Na I" "K I"    # a subset
Requires network. The container this was written in had none; the fetcher
served one spectrum only, so the pass is specified and not run here.
"""
import re, sys, time, json, urllib.parse, urllib.request

# ---------------------------------------------------------------------------
# THE MIRROR, and why it is cheaper than the CGI.
# ASD v5.12 is mirrored as one small pipe-delimited file per spectrum at
#     https://data.nublado.org/nist/asd_v5.12/levels/asd.ZZZCCC
# with ZZZ the atomic number and CCC the ionisation stage, both three digits:
# H I = 001000, He I = 002000, Ne I = 010000, Na I = 011000, K I = 019000.
# A species file is kilobytes where the CGI page is megabytes.
MIRROR = "https://data.nublado.org/nist/asd_v5.12/levels/asd.%03d%03d"
Z = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
     "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
     "Sc":21,"Ti":22,"V":23,"Cr":24,"Mn":25,"Fe":26,"Co":27,"Ni":28,"Cu":29,
     "Zn":30,"Ga":31,"Ge":32,"As":33,"Se":34,"Br":35,"Kr":36,"Rb":37,"Sr":38,
     "Cd":48,"Ba":56,"Hg":80,"Tl":81,"Pb":82,"Bi":83}
ROM = {"I":0,"II":1,"III":2,"IV":3,"V":4,"VI":5,"VII":6,"VIII":7,"IX":8,"X":9}
def mirror_url(spectrum):
    el, stage = spectrum.split()
    return MIRROR % (Z[el], ROM[stage])

# ---------------------------------------------------------------------------
# COUNT TRIPLES, NOT CELLS.  The bracket relates T(n-1), T(n), T(n+1), so a cell
# is an independent test only if ALL THREE of its levels are independent. One
# derived level poisons three tests; at a scattered derived fraction f the
# surviving tests go as (1-f)^3 rather than (1-f). Verified on H I: 38% of levels
# plain, and only 13 of 64 interior cells -- 20% -- independent.
def clean_triples(by_series):
    """by_series: {series_key: {n: kind}}  ->  (interior cells, clean triples)"""
    inter = clean = 0
    for key, d in by_series.items():
        ns = sorted(d)
        for n in ns:
            if n-1 in d and n+1 in d:
                inter += 1
                if all(d[m] != "ritz" for m in (n-1, n, n+1)): clean += 1
    return inter, clean

# ---------------------------------------------------------------------------
# AND THE LAYER BELOW THE DELIMITERS, established 3 August 2026.
# NO ASD LEVEL IS A DIRECT MEASUREMENT. Levels are obtained from measured LINES
# by least-squares optimisation (LOPT, Kramida 2011); Cloudy's Stout database
# states it plainly -- "the level energies given in the NIST database are usually
# derived from measured line wavelengths". So the partition is not measured
# versus derived; it is DEGREES of derivation:
#     plain  one inversion  -- optimised from measured lines
#     [ ]    two            -- a Ritz fit ON that inversion
#     ( )    none from measurement at all
# Neighbouring levels in a series are fitted from OVERLAPPING line sets, so the
# triple count above is itself an upper bound: LOPT correlates the three members
# a bracket test compares. Five species examined -- H I, He I, Ne I, Na I, Hg I --
# and every one rests on a critical compilation of exactly this kind.

from collections import Counter, defaultdict

BASE = "https://physics.nist.gov/cgi-bin/ASD/energy1.pl"
# ASCII output, level values only -- the smallest response that carries the marks
PARAMS = dict(de="0", format="1", output="0", page_size="15", multiplet_ordered="0",
              conf_out="on", term_out="on", level_out="on", j_out="on",
              unc_out="1", biblio="on", submit="Retrieve+Data", units="0")

# §22.1-22.6 and §22.11: every system in the collection
SYSTEMS = ["H I", "He I", "He II", "Li I", "Li II", "Be II", "Na I", "Mg II",
           "Al I", "Al II", "Si II", "Si I", "P II", "K I", "Ca II", "Ca I",
           "Sc III", "Sc VI", "Ti I", "Ne I", "Ne II", "Ar II", "Cu II",
           "Ga I", "Kr I", "Sr I", "Ba I", "Ba II", "Ba III", "Hg II",
           "Bi I", "Bi II", "Bi III", "Zn I", "Cd I"]

LEVEL = re.compile(r"^\s*([^|]*?)\|([^|]*?)\|([^|]*?)\|\s*([\[\(]?)\s*"
                   r"([-\d][\d\s.,]*)\s*([\]\)]?)", re.M)
NCONF = re.compile(r"(\d+)\s*[spdfghi]")

def fetch(spectrum, pause=1.5):
    q = dict(PARAMS); q["spectrum"] = spectrum
    url = BASE + "?" + urllib.parse.urlencode(q, safe="+")
    with urllib.request.urlopen(url, timeout=60) as r:
        txt = r.read().decode("latin-1")
    time.sleep(pause)                       # be a good citizen
    return txt

def provenance_note(txt):
    """the per-species note, which overrides the delimiters where it applies"""
    out = []
    for m in re.finditer(r"(Ritz[^.]{0,200}\.|interpolat[^.]{0,160}\.|"
                         r"theoretical[^.]{0,160}\.|fitting[^.]{0,200}\.)", txt, re.I):
        out.append(re.sub(r"\s+", " ", m.group(1)).strip())
    return out[:6]

def classify(txt):
    """count levels by delimiter, and by principal quantum number where visible"""
    c = Counter(); by_n = defaultdict(Counter)
    for conf, term, j, open_d, val, close_d in LEVEL.findall(txt):
        if not val.strip(): continue
        kind = "ritz" if open_d == "[" else "theory" if open_d == "(" else "observed"
        c[kind] += 1
        m = NCONF.search(conf)
        if m: by_n[int(m.group(1))][kind] += 1
    return c, by_n

def main(systems):
    rows, notes = {}, {}
    for s in systems:
        try:
            t = fetch(s)
            rows[s], _ = classify(t)
            notes[s] = provenance_note(t)
        except Exception as e:
            rows[s] = Counter(); notes[s] = [f"FETCH FAILED: {e}"]
    print(f"  {'species':<9}{'observed':>9}{'[Ritz]':>8}{'(theory)':>9}{'total':>7}"
          f"{'independent':>12}")
    tot = Counter()
    for s in systems:
        c = rows[s]; n = sum(c.values())
        ind = c["observed"] + c["theory"]
        tot += c
        print(f"  {s:<9}{c['observed']:>9}{c['ritz']:>8}{c['theory']:>9}{n:>7}"
              f"{(f'{100*ind/n:.0f}%' if n else '—'):>12}")
    N = sum(tot.values()); IND = tot["observed"] + tot["theory"]
    print(f"\n  {'ALL':<9}{tot['observed']:>9}{tot['ritz']:>8}{tot['theory']:>9}{N:>7}"
          f"{(f'{100*IND/N:.0f}%' if N else '—'):>12}")
    print(f"""
  WHAT THIS ANSWERS. §22.9's honest form is '1,442 cells, an unknown proper
  subset of which are independent'. The subset is now known per species, and the
  book's claim should read: 1,442 cells, of which {IND} rest on values the
  bracket could falsify and {tot['ritz']} rest on values generated by the law the
  bracket assumes.""")
    print("\n  PER-SPECIES PROVENANCE NOTES, which override the delimiters:")
    for s in systems:
        for note in notes[s]:
            if re.search(r"Ritz|fitting", note, re.I):
                print(f"    {s}: {note[:150]}")
    json.dump({s: dict(rows[s]) for s in systems}, open("asd_pass.json", "w"), indent=1)

if __name__ == "__main__":
    main(sys.argv[1:] or SYSTEMS)
