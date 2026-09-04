#!/usr/bin/env python3
# r2-ch13w — chat 88 — prose batch for the Chapter 19 section read (main L5381-L5548).
# Deterministic; prints no wall-clock time. Every pointer resolved to the CLAIM, not the heading.

import os, re
H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
def L(i): return M[i - 1]
def strip(t): return t.replace('**', '').replace('*', '').strip()
LO, HI = 5381, 5548

print('=== r2-ch13w  Chapter 19 prose batch ===')
print('range L%d-L%d (%d lines); volumes %s' % (LO, HI, HI - LO + 1,
      {k: len(v) for k, v in V.items()}))

# ------------------------------------------------ 1. pointers to the claim
print('\n-- 1. pointers resolved to the CLAIM, not the heading --')
def heading_line(sec):
    """Body heading for a section number, taking the LATER match (the front-matter
    contents list at L120-L172 is not the body -- chat 87's fix)."""
    hits = [i for i, t in enumerate(M, 1)
            if re.match(r'^#{2,4} %s[ .]' % re.escape(sec), t.strip())]
    return hits[-1] if hits else None

def extent(start):
    for i in range(start + 1, len(M) + 1):
        if M[i - 1].startswith('#') and re.match(r'^#{1,4} ', M[i - 1]):
            return i - 1
    return len(M)

CLAIMS = [
    (5445, '\u00a719.5', 'four documents ... rho <= 2 ... every route closed',
     ['not retrieved', '\u03c1 \u2264 2', 'every route closed']),
    (5447, '\u00a719.6', 'step 2 lists seven route types',
     ['primary', 'preprint', 'review', 'compilation', 'citing paper', 'deposit', 'database']),
    (5461, '\u00a729', 'the range \u00a729 wants', ['Ritz', '244']),
    (5471, '\u00a729.5', 'the exact question \u00a729.5 asks of that chapter',
     ['Edl\u00e9n', 'one remove']),
    (5476, '\u00a719.6', 'lists the review route third of seven', ['review']),
    (5492, '\u00a721.5', "a count printed where a coordinate was needed",
     ['translation', 'coordinate']),
    (5511, '\u00a719.1', 'defines R(c) = { i : c \u2208 S\u1d62 }', ['R(c)', 'route set']),
    (5515, '\u00a719.1', '\u03c1 \u2265 2 survives the loss of any single source',
     ['\u03c1 \u2265 2', 'survives']),
    (5529, '\u00a719.3', 'the secondary can beat the primary', ['secondary', 'primary']),
    (5547, 'Chapter 28', 'the author violated step 1, recorded in Chapter 28',
     ['step 1', 'violat', 'retriev']),
]
for site, sec, what, keys in CLAIMS:
    tgt = heading_line(sec.replace('\u00a7', '').replace('Chapter ', ''))
    if tgt is None:
        print('   L%-5d %-12s UNRESOLVED (no body heading)' % (site, sec)); continue
    end = extent(tgt)
    body = '\n'.join(M[tgt - 1:end]).lower()
    found = [k for k in keys if k.lower() in body]
    print('   L%-5d %-12s -> L%-5d-%-5d  keys %d/%d found %s  %s'
          % (site, sec, tgt, end, len(found), len(keys), found[:4],
             'CLAIM PRESENT' if len(found) == len(keys) else 'CLAIM SHORT'))

# ---------------------------------------- 2. register citations, incl. lowercase
print('\n-- 2. register citations in range (uppercase and lowercase forms) --')
R = V['reg']
def reg_entry(n):
    for i, t in enumerate(R, 1):
        if t.strip() == '### %d' % n:
            j = i + 1
            body = []
            while j <= len(R) and not R[j - 1].strip().startswith('### '):
                body.append(R[j - 1]); j += 1
            return i, '\n'.join(body)
    return None, ''
cites = set()
for i in range(LO, HI + 1):
    for m in re.finditer(r'[Rr]egisters? (\d{2,4})(?:\u2013(\d{2,4}))?', L(i)):
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        for n in range(a, b + 1):
            cites.add((n, i))
for n, site in sorted(cites):
    ln, body = reg_entry(n)
    kws = [w for w in ['\u03c1', 'retriev', 'route', 'Dunz', 'index', 'source', 'search']
           if w.lower() in body.lower()]
    print('   L%-5d register %-4d -> %s  on-subject keywords %s'
          % (site, n, ('reg L%d' % ln) if ln else 'MISSING', kws[:5] if ln else '-'))

# ------------------------------------------ 3. Chapter 18's two hand-offs
print('\n-- 3. Chapter 18 hand-offs into Chapter 19 --')
dep = [i for i in range(LO, HI + 1) if 'depth' in L(i).lower()]
print('   \u00a718.3 L4977-4978: %r' % (strip(L(4977))[:60] + ' ' + strip(L(4978))[:60]))
print('   "depth" in Chapter 19: %d sites %s  -> %s'
      % (len(dep), dep, 'PROMISE UNMET' if not dep else 'present'))
print('   "channel" in Chapter 19: %d sites'
      % len([i for i in range(LO, HI + 1) if 'channel' in L(i).lower()]))
print('   "measured members" in Chapter 19: %d sites'
      % len([i for i in range(LO, HI + 1) if 'measured members' in L(i).lower()]))
print('   \u00a718.6.1 L5325 indexes the bibliography on depth of entry: %s'
      % ('depth of entry' in L(5325)))
print('   \u00a719.5.3 L5518 index coordinates: %s'
      % re.search(r'built over (.+?) and fibred', strip(L(5518))).group(1))

# --------------------------------- 4. incoming pointers to Chapter 19 elsewhere
print('\n-- 4. every site outside Chapter 19 that points into it --')
for k, lines in V.items():
    for i, t in enumerate(lines, 1):
        if k == 'main' and LO <= i <= HI:
            continue
        for m in re.finditer(r'\u00a7?19\.(\d)(?:\.(\d))?|Chapter 19', t):
            print('   %-4s L%-6d %s' % (k, i, strip(t)[:104]))
            break

# --------------------------- 5. the L4550 attribution, measured against the file
print('\n-- 5. L4550-L4551 attributes a sentence to \u00a719.5 --')
quoted = 'a blocked \u03c1 = 1 cell is a stated gap, not an unexplained absence'
hits = [i for i, t in enumerate(M, 1) if quoted.lower() in t.lower()]
s195, s196 = 5432, 5538
print('   quoted sentence sites: %s' % hits)
for h in hits:
    which = '\u00a719.6' if h >= s196 else ('\u00a719.5' if h >= s195 else 'elsewhere')
    print('      L%d lies in %s' % (h, which))
print('   L4550 says: %r' % strip(L(4550))[:96])
print('   VERDICT: %s' % ('attribution one section short (\u00a719.6 not \u00a719.5)'
      if all(h >= s196 for h in hits) else 'attribution holds'))

# ------------------------------------------- 6. self-counts in the chapter
print('\n-- 6. self-counts --')
def count_rows(a, b, pred):
    return sum(1 for i in range(a, b + 1) if pred(L(i)))
print('   "Four documents ... not retrieved" (L5433): table rows L5451-5454 = %d'
      % count_rows(5451, 5454, lambda t: t.strip() != ''))
step2 = ' '.join(strip(L(i)) for i in (5540, 5541))
types = [x.strip() for x in re.sub(r'^\d\.\s*List route candidates per cell \u2014 ', '', step2).rstrip('.').split(',')]
print('   \u00a719.6 step 2 route types: %d %s' % (len(types), types))
print('   \u00a719.5.1 L5447 says "seven route types": %s'
      % ('EXACT' if len(types) == 7 else 'MISMATCH'))
print('   \u00a719.5.1 table columns: %s (route types omitted: %s)'
      % (strip(L(5450)).split()[1:6],
         [t for t in types if t.split()[0][:6] not in ' '.join(strip(L(5450)).split()[1:6])]))
print('   \u00a719.5.3 fibre rows: %d named + pooled (route type omitted: database)'
      % len(re.findall(r'([a-z]+)\s+\d+\s+\d+', ' '.join(strip(L(i)) for i in range(5521, 5524)))))
print('   "nine searches" (L5436): main sites %s'
      % [i for i, t in enumerate(M, 1) if 'nine searches' in t.lower()])
print('   "Three coverage gaps" (L5430): main sites %s'
      % [i for i, t in enumerate(M, 1) if 'coverage gap' in t.lower()])
print('   "The review route pays twice" (L5475): review-route documents in the table = %d'
      % sum(1 for i in (5451, 5452, 5453, 5454) if re.search(r'\s1\s', strip(L(i))[:60])))

# ------------------------------------------------- 7. attributions (R-ATTR)
print('\n-- 7. attribution pass (R-ATTR) --')
NAMES = ['Edl\u00e9n', 'Ritz', 'Paschen', 'G\u00f6tze', 'Dunz', 'CODATA', 'Hori', 'Korobov',
         'Birkhoff', 'Rota', 'Freuder', 'Lauritzen']
for n in NAMES:
    inch = [i for i in range(LO, HI + 1) if n in L(i)]
    if inch:
        print('   %-9s in Chapter 19 at %s' % (n, inch[:6]))
print('   persons named in Chapter 19 (of the reference list): %d'
      % sum(1 for n in NAMES if any(n in L(i) for i in range(LO, HI + 1))))
print('   Chapter 19 register citations: %d entries over %d sites'
      % (len({n for n, _ in cites}), len({s for _, s in cites})))

# ------------------------------------------- 8. vocabulary and the Dunz pair
print('\n-- 8. vocabulary, and the Dunz pair --')
print('   "UNKNOWN" in Chapter 19: %s' % [i for i in range(LO, HI + 1) if 'UNKNOWN' in L(i)])
print('   "UNKNOWN" elsewhere in main: %d sites'
      % len([i for i, t in enumerate(M, 1) if 'UNKNOWN' in t and not (LO <= i <= HI)]))
dz = [i for i, t in enumerate(M, 1) if 'Dunz' in t]
print('   Dunz sites in main: %s' % dz)
ref = ' '.join(strip(M[i - 1]) for i in range(11712, 11715))
print('   References entry L11712-11714: %r' % ref[:150])
print('   \u00a719.5.2 claims the entry adds "retrieved as a scan, unread": %s'
      % ('retrieved as a scan' in ref.lower()))
print('   \u00a719.5 L5434 lists Dunz among documents NOT retrieved: %s' % ('Dunz' in L(5434)))
print('   VERDICT 19.5.2: both statements present in the volume -> %s'
      % ('CONFIRMED, the book carries both' if 'retrieved as a scan' in ref.lower() else 'not confirmed'))
print('   em-dash for the initial at L11712: %s' % ('Dunz, \u2014' in L(11712)))
print('   Paschen & G\u00f6tze title L11626 vs Dunz title L11712:')
print('      P&G : %s' % re.search(r'\*(Seriengesetze[^*]*)\*', L(11626)).group(1))
print('      Dunz: %s' % re.search(r'\*(Seriengesetze[^*]*)\*', L(11712)).group(1))

# --------------------------------------- 9. the Edlen (year, title) pair
print('\n-- 9. Edl\u00e9n, named with two (year, title) pairs --')
for i in (11621, 11624):
    print('   References L%d: %s' % (i, strip(L(i))[:100]))
print('   \u00a719.5 L5433: %r' % strip(L(5433))[:78])
print('   \u00a719.5.1 table L5453: %r' % strip(L(5453))[:60])
print('   \u00a729.5 L7961: %r' % strip(L(7961))[:70])
print('   "Handbuch" sites in main: %s' % [i for i, t in enumerate(M, 1) if 'Handbuch' in t])
print('=== end r2-ch13w ===')
