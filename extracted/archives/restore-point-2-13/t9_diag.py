#!/usr/bin/env python3
"""T9 — diagnose the generator's residue. For each of the 486 series, ask in order
which condition in store_gen.members() removed its levels. Writes a census; prints shape."""
import csv, os, re, sys
sys.path.insert(0, '.')
import store_gen as SG

src = list(csv.DictReader(open('MEASUREMENTS.tsv'), delimiter='\t'))
der = {}
for r in csv.DictReader(open('MEASUREMENTS-DERIVED.tsv'), delimiter='\t'):
    der[(r['Z'], r['charge'], r['l'], r['mult'], r['term'], r['n_lo'], r['n_hi'])] = r

rows = []
for r in src:
    Z, ch, L = int(r['Z']), int(r['charge']), int(r['l'])
    term, stored = r['term'].strip(), int(r['members'])
    sym = SG.MASS.get(Z, ('?',0))[0]
    path = f'spectra_raw/queue2/{sym}I.tsv'
    have_file = os.path.exists(path)
    lim_ok = True
    try: float(r['limit'])
    except Exception: lim_ok = False
    raw = SG.levels(sym) if have_file else []
    # stage counts
    n_cfg = n_L = n_term = n_parse = n_below = 0
    lim = float(r['limit']) if r.get('limit') else None
    for x in raw:
        if len(x) < 4: continue
        m = re.search(r'(\d+)([spdfghik])$', x[0].strip())
        if not m: continue
        n_cfg += 1
        if SG.LM.get(m.group(2)) != L: continue
        n_L += 1
        if x[1].strip() != term: continue
        n_term += 1
        v = x[3].strip()
        try: E = float(v.strip('[]').replace('+', ''))
        except ValueError: continue
        n_parse += 1
        if lim is not None and E >= lim: continue
        n_below += 1
    if not lim_ok:                   cause = 'A0_no_limit'
    elif not have_file:              cause = 'A_no_file'
    elif Z not in SG.MASS:           cause = 'B_Z_not_in_mass_table'
    elif n_L == 0:                   cause = 'C_no_level_at_this_l'
    elif n_term == 0:                cause = 'D_term_string_mismatch'
    elif n_parse == 0:               cause = 'E_energy_unparsed'
    elif n_below == 0:               cause = 'F_all_above_limit'
    elif n_below == stored:          cause = 'Z_match'
    elif n_below > stored:           cause = 'G_over_recover'
    else:                            cause = 'H_under_recover'
    rows.append(dict(Z=Z, charge=ch, l=L, term=term, sym=sym, stored=stored,
                     cfg=n_cfg, at_l=n_L, at_term=n_term, parsed=n_parse,
                     below=n_below, cause=cause))

with open('T9-RESIDUE.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t')
    w.writeheader(); w.writerows(rows)

from collections import Counter
c = Counter(x['cause'] for x in rows)
print(f'series examined: {len(rows)}')
for k in sorted(c): print(f'  {k:26s} {c[k]:4d}')
print(f'ion series (charge>0): {sum(1 for x in rows if x["charge"]>0)}')
print('written: T9-RESIDUE.tsv')
