#!/usr/bin/env python3
"""T9 probe. Two questions, computed not assumed:
 (1) do the 128 count-disagreements resolve if the store's own n_lo..n_hi window is applied?
 (2) for the 68 term-string misses, what terms DO exist at that l, and how do they differ?"""
import csv, os, re, sys, collections
sys.path.insert(0, '.')
import store_gen as SG

src = list(csv.DictReader(open('MEASUREMENTS.tsv'), delimiter='\t'))
res = {(r['Z'], r['l'], r['term']): r['cause']
       for r in csv.DictReader(open('T9-RESIDUE.tsv'), delimiter='\t')}

fixed = collections.Counter()
term_rows = []
for r in src:
    Z, L, term = int(r['Z']), int(r['l']), r['term'].strip()
    cause = res.get((str(Z), str(L), term), '?')
    if cause == 'Z_match': continue
    sym = SG.MASS[Z][0]
    lim = float(r['limit']); stored = int(r['members'])
    nlo, nhi = int(r['n_lo']), int(r['n_hi'])
    raw = SG.levels(sym)
    hits, terms_at_l = [], collections.Counter()
    for x in raw:
        if len(x) < 4: continue
        m = re.search(r'(\d+)([spdfghik])$', x[0].strip())
        if not m or SG.LM.get(m.group(2)) != L: continue
        terms_at_l[x[1].strip()] += 1
        if x[1].strip() != term: continue
        try: E = float(x[3].strip().strip('[]').replace('+', ''))
        except ValueError: continue
        if E >= lim: continue
        hits.append(int(m.group(1)))
    if cause == 'D_term_string_mismatch':
        near = [t for t in terms_at_l if t.replace('*', '').strip() == term.replace('*', '').strip()]
        term_rows.append(dict(Z=Z, sym=sym, l=L, stored_term=term, stored_members=stored,
                              n_terms_at_l=len(terms_at_l),
                              parity_variant=';'.join(near) if near else '',
                              sample_terms=';'.join(list(terms_at_l)[:6])))
    else:
        win = [n for n in hits if nlo <= n <= nhi]
        if len(win) == stored: fixed['n_window_fixes'] += 1
        elif len(hits) == stored: fixed['already'] += 1
        else: fixed['still_wrong'] += 1

with open('T9-TERMS.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(term_rows[0].keys()), delimiter='\t')
    w.writeheader(); w.writerows(term_rows)

print('--- Q1: does the store n_lo..n_hi window explain the 128? ---')
for k in sorted(fixed): print(f'  {k:18s} {fixed[k]:4d}')
print('--- Q2: the 68 term misses ---')
print(f'  with a parity-only variant present: {sum(1 for r in term_rows if r["parity_variant"])}')
print(f'  with NO level of any term at l    : {sum(1 for r in term_rows if r["n_terms_at_l"]==0)}')
print('  written: T9-TERMS.tsv')
