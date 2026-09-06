#!/usr/bin/env python3
"""store_gen2.py — the store's generator, repaired at T9.

Three faults in store_gen.py, each diagnosed at T9 and each against a rule
already on record:

  1. It reconstructed series on (l, term) where R 1650 declares the split is
     (l, term, parent) AS PRINTED. It therefore pooled levels across parent
     cores — 69 of 107 over-recoveries explained by this alone.
  2. It applied one LS-shaped config regex to all four coupling languages
     (R 1663), so jK recovered at 33% against LS's 72%. The row's own
     `language` column declared the language and was never read.
  3. Where it could not read a config it dropped the row silently — the
     §2.9 fault, arriving as omission rather than as coercion. 68 series
     vanished from the output entirely rather than being refused with a reason.

What is NOT repaired here, and is named rather than fixed: the LIMIT is still
inherited from the store. R 1650's fallback clause ("else the first limit above
its top member") is what R 1664 voided on 145 rows; a generator that re-derived
limits would have to re-derive that too, and that is the series construction's
remaining half.

Refusal, per §2.9: a series that cannot be read is written with members_found=0
and a NAMED reason. It is never dropped.
"""
import re, csv, statistics as st, os, sys
sys.path.insert(0, '.')
from store_gen import RINF, AMU, MASS, LM, levels

SHELL = re.compile(r'(\d+)([spdfghik])(\d*)$')


def outer(config):
    """The Rydberg electron's (n, l), or a named refusal.

    The config is a dot-joined chain; the last component is the outer electron
    in all four languages. What differs between languages is the DECORATION —
    jK and jj append <j> to the component and nest the parent in parentheses —
    so the decoration is stripped and the same shell is read underneath.
    Returns (n, l, None) or (None, None, reason).
    """
    c = config.strip()
    if not c:
        return None, None, 'config_empty'
    c = c.rstrip('?')
    c = re.sub(r'<[^>]*>', '', c)          # drop <j> on the component
    part = c.split('.')[-1]
    part = part.rstrip('?')
    if part.endswith(')'):                  # last component is a parent group
        return None, None, 'no_outer_electron'
    m = SHELL.search(part)
    if not m:
        return None, None, 'shell_unreadable'
    if m.group(3) and int(m.group(3)) > 1:
        return None, None, 'outer_occupancy_gt_1'
    return int(m.group(1)), LM[m.group(2)], None


def parent_of(config):
    """The printed parent: the last parenthesised group, decoration kept.
    R 1650 says AS PRINTED, so <j> is retained — 2P*<3/2> and 2P*<1/2> are
    different parents and the store records them as such."""
    g = re.findall(r'\(([^()]*)\)', config)
    return g[-1].strip() if g else ''


def members(sym, R, lim, L, term, parent):
    """delta(n) for every level of THIS series below the limit.
    The series is (l, term, parent). Where the store records no parent the
    parent condition is not applied — R 1664's 'no parent stated' is a bin of
    its own, not a filter with an empty argument."""
    out, refusals = [], []
    for r in levels(sym):
        if len(r) < 4:
            continue
        cfg = r[0].strip()
        if r[1].strip() != term:
            continue
        n, l, why = outer(cfg)
        if why:
            refusals.append(why)
            continue
        if l != L:
            continue
        if parent and parent_of(cfg) != parent:
            continue
        v = r[3].strip()
        br = v.startswith('[')
        try:
            E = float(v.strip('[]').replace('+', ''))
        except ValueError:
            refusals.append('energy_unparsed')
            continue
        if E >= lim:
            continue
        out.append((n, n - R ** 0.5 / ((lim - E) ** 0.5), br))
    return sorted(out), refusals


def main():
    src = list(csv.DictReader(open('MEASUREMENTS.tsv'), delimiter='\t'))
    cols = ['Z', 'charge', 'l', 'mult', 'term', 'parent', 'language',
            'n_lo', 'n_hi', 'members_stored', 'members_found', 'count_match',
            'delta_stored', 'delta_median', 'delta_mean', 'delta_asym',
            'spread', 'bracketed', 'asym_bracketed', 'delta_status', 'refusal']
    out, agree, matched, refused = [], 0, 0, 0
    for r in src:
        Z = int(r['Z'])
        term = r['term'].strip()
        parent = r['parent'].strip()
        stored = int(r['members'])
        base = [r['Z'], r['charge'], r['l'], r['mult'], term, parent,
                r['language'].strip(), r['n_lo'], r['n_hi'], stored]
        if Z not in MASS:
            out.append(base + [0, 'no'] + [''] * 8 + ['Z_not_in_mass_table'])
            refused += 1
            continue
        sym, mass = MASS[Z]
        R = RINF / (1 + 1 / (mass * AMU))
        try:
            lim = float(r['limit'])
        except ValueError:
            out.append(base + [0, 'no'] + [''] * 8 + ['no_limit_recorded'])
            refused += 1
            continue
        pts, refs = members(sym, R, lim, int(r['l']), term, parent)
        if not pts:
            why = max(set(refs), key=refs.count) if refs else 'no_level_matched'
            out.append(base + [0, 'no'] + [''] * 8 + [why])
            refused += 1
            continue
        d = [p[1] for p in pts]
        ok = (len(pts) == stored)
        matched += ok
        med, mean, asym = st.median(d), st.mean(d), d[-1]
        if ok and abs(med - float(r['delta'])) < 1e-4:
            agree += 1
        out.append(base + [len(pts), 'yes' if ok else 'no', r['delta'],
                           f'{med:.5f}', f'{mean:.5f}', f'{asym:.5f}',
                           f'{max(d)-min(d):.5f}', sum(p[2] for p in pts),
                           'yes' if pts[-1][2] else 'no', r['delta_status'], ''])
    with open('MEASUREMENTS-DERIVED2.tsv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(cols)
        w.writerows(out)
    print(f'series written          {len(out)} of {len(src)}  (none dropped)')
    print(f'refused with a reason   {refused}')
    print(f'member count reproduces {matched} of {len(src)-refused} recovered')
    print(f'median = stored delta   {agree} of {matched} exact-count series')
    print('written                 MEASUREMENTS-DERIVED2.tsv')


if __name__ == '__main__':
    main()
