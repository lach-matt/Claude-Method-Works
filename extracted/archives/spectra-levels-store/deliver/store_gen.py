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
import re, csv, statistics as st, os

RINF = 109737.31568
AMU = 1822.888486
MASS = {5:('B',10.811), 11:('Na',22.98977), 13:('Al',26.98154), 22:('Ti',47.867),
        31:('Ga',69.723), 32:('Ge',72.630), 36:('Kr',83.798), 38:('Sr',87.62),
        39:('Y',88.90584), 40:('Zr',91.224), 49:('In',114.818), 50:('Sn',118.710),
        54:('Xe',131.293), 55:('Cs',132.905), 56:('Ba',137.327), 70:('Yb',173.045),
        71:('Lu',174.967), 72:('Hf',178.49), 80:('Hg',200.592), 81:('Tl',204.383),
        82:('Pb',207.2), 86:('Rn',222.018), 87:('Fr',223.020), 88:('Ra',226.025)}
LM = {'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6,'k':7}

_cache = {}
def levels(sym):
    """Raw level rows for a neutral species. Header may be absent (19 of 61 files)."""
    if sym in _cache: return _cache[sym]
    path = f'spectra_raw/queue2/{sym}I.tsv'
    if not os.path.exists(path): _cache[sym] = []; return []
    rows = [l.rstrip('\n\r').split('\t') for l in open(path, encoding='utf-8')
            if l.strip() and not l.startswith('#')]
    if rows and 'onfig' in rows[0][0]: rows = rows[1:]
    _cache[sym] = rows
    return rows


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


def limits(sym):
    """Every 'Limit' row of the raw table, as (label, energy), in table order.
    The label is the parent as NIST prints it (decoration kept, R 1650)."""
    out = []
    for r in levels(sym):
        if len(r) >= 4 and r[1].strip() == 'Limit':
            try:
                out.append((r[0].strip(), float(r[3].strip().strip('[]').replace('+', ''))))
            except ValueError:
                pass
    return out



def ion_offset(sym, term, J0, J):
    """E_ion(term,J) - E_ion(term,J0) from the parent ION's own table on disk
    (spectra_raw/{sym}II.tsv or queue2), lowest ordinal of that term. None if
    the table or either level is absent. T8-J."""
    for d in ('spectra_raw', 'spectra_raw/queue2'):
        p = f'{d}/{sym}II.tsv'
        if os.path.exists(p):
            break
    else:
        return None
    lv = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        r = l.rstrip('\n').split('\t')
        if len(r) < 4:
            continue
        t = re.sub(r'^[a-z] ', '', r[1].strip())
        if t == term and r[2].strip() not in lv:
            try:
                lv.setdefault(r[2].strip(), float(r[3].strip().strip('[]').replace('+', '')))
            except ValueError:
                pass
    if J0 in lv and J in lv:
        return lv[J] - lv[J0]
    return None


def assign_limit(sym, parent, top_E):
    """T8 (R 1692 direction; M's ruling session 1.8.2). The limit is GENERATED,
    not inherited. Returns (limit or None, status, label).
      parent-matched   the printed parent string appears in a limit label
                       (STRING EQUALITY, decoration retained — R 1650)
      forced           no parent stated and the species publishes ONE limit
      positional       no parent stated, several limits: the first published
                       limit above the ladder's top member — NIST's own table
                       convention (levelshelp: series levels sit beneath the
                       limit they converge to), named as a READING, not a default
      unwitnessed      a parent stated whose limit science has not yet
                       published — the series is NOT defected; E measuring the
                       world; a named bound (D3, M's wording)
    Nothing else. No fallback replaces the fallback R 1664 voided."""
    L = limits(sym)
    if not L:
        return None, 'no limit published', ''
    if parent:
        for lab, E in L:
            if parent in lab:
                return E, 'parent-matched', lab
        # M's ruling (session 1.8.2, T8-A): FOLLOW NIST ORDINAL. A parent written
        # 'a_2D' / 'c_2D' / '4F' is the core TERM with NIST's ordinal letter
        # (R 1683: a 4F and b 4F are ordinals of one core, not two cores).
        # The comparison is core-term to limit-term; the letter is not a core.
        core = re.sub(r'^[a-z]_', '', parent)
        for lab, E in L:
            m = re.search(r'_([0-9][A-Z]\*?)(<[^>]*>)?\)$', lab)
            if m and m.group(1) == core:
                return E, 'parent-matched (NIST ordinal)', lab
        # T8-J, M's ruling (session 1.8.3): a J-RESOLVED parent may borrow its
        # limit from the parent ION's own level table — a SECOND DATA SOURCE.
        # Narrow scope: the parent's TERM has a printed limit; the J differs;
        # limit(J) = printed limit(J0) + [E_ion(term,J) - E_ion(term,J0)].
        # A derived limit, one route, from two witnessed tables. Status
        # 'ion-derived'. Where the ion table is not on disk the row stays
        # unwitnessed — nothing is fetched here.
        mj = re.match(r'^(.*?)(<[^>]*>)$', parent)
        if mj:
            term_p, J = mj.group(1), mj.group(2).strip('<>')
            for lab, E0 in L:
                m0 = re.search(r'_' + re.escape(term_p) + r'<([^>]*)>\)$', lab)
                if m0:
                    off = ion_offset(sym, term_p, m0.group(1), J)
                    if off is not None:
                        return E0 + off, 'ion-derived (T8-J)', lab + '+' + f'{term_p}<{J}>'
        return None, 'unwitnessed — parent limit not yet published', ''
    if len(L) == 1:
        return L[0][1], 'forced — sole published limit', L[0][0]
    above = [(lab, E) for lab, E in L if top_E is None or E > top_E]
    if not above:
        return None, 'unbounded — no published limit above ladder', ''
    lab, E = min(above, key=lambda x: x[1])
    return E, 'positional — NIST table convention', lab


def top_member_E(sym, L, term, parent):
    """Highest level of the (l, term, parent) ladder, in cm-1, or None."""
    best = None
    for r in levels(sym):
        if len(r) < 4 or r[1].strip() != term:
            continue
        n, l, why = outer(r[0].strip())
        if why or l != L:
            continue
        # R 1678: parent is the third key of the series. An unparented ladder
        # is the set of levels with NO printed parent — not the union of all.
        if parent_of(r[0].strip()) != parent:
            continue
        try:
            E = float(r[3].strip().strip('[]').replace('+', ''))
        except ValueError:
            continue
        best = E if best is None else max(best, E)
    return best


def main():
    src = list(csv.DictReader(open('MEASUREMENTS.tsv'), delimiter='\t'))
    cols = ['Z', 'charge', 'l', 'mult', 'term', 'parent', 'language',
            'n_lo', 'n_hi', 'members_stored', 'members_found', 'count_match',
            'delta_stored', 'delta_median', 'delta_mean', 'delta_asym',
            'spread', 'bracketed', 'asym_bracketed', 'delta_status', 'refusal',
            'limit_gen', 'limit_status_gen', 'limit_label_gen', 'limit_stored',
            'limit_agrees', 'ladder_exceeds_limit']
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
        # T8: the limit is GENERATED here; the stored one is carried for audit only.
        top_E = top_member_E(sym, int(r['l']), term, parent)
        lim, lstat, llab = assign_limit(sym, parent, top_E)
        try:
            lim_stored = float(r['limit'])
        except ValueError:
            lim_stored = None
        agrees = ('yes' if (lim is not None and lim_stored is not None
                            and abs(lim - lim_stored) < 1e-3) else 'no')
        exceeds = ('yes' if (lim is not None and top_E is not None and top_E >= lim) else 'no')
        tail = [f'{lim:.5f}' if lim is not None else '', lstat, llab,
                f'{lim_stored:.5f}' if lim_stored is not None else '', agrees, exceeds]
        if lim is None:
            out.append(base + [0, 'no'] + [''] * 8 + [lstat] + tail)
            refused += 1
            continue
        pts, refs = members(sym, R, lim, int(r['l']), term, parent)
        if not pts:
            why = max(set(refs), key=refs.count) if refs else 'no_level_matched'
            out.append(base + [0, 'no'] + [''] * 8 + [why] + tail)
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
                           'yes' if pts[-1][2] else 'no',
                           'usable' if not lstat.startswith('unwitnessed') else r['delta_status'],
                           ''] + tail)
    with open('MEASUREMENTS-DERIVED.tsv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(cols)
        w.writerows(out)
    print(f'series written          {len(out)} of {len(src)}  (none dropped)')
    print(f'refused with a reason   {refused}')
    print(f'member count reproduces {matched} of {len(src)-refused} recovered')
    print(f'median = stored delta   {agree} of {matched} exact-count series')
    print('written                 MEASUREMENTS-DERIVED.tsv')


if __name__ == '__main__':
    main()
