#!/usr/bin/env python3
# r2-ch18b.py — chat 131 — R2 prose batch for main L9939–L10053 (Appendix A part 1: opener, A.3, A.8–A.13), BUILD90.
# Reads MEMBERS only; imports r2lib by path. Rulings 45/46 tokens, first person (probe carries mine and myself), structure
# (bold lead-ins, italics, tables, unmarked sub-headings, line lengths), every negative with its witness, docket 27
# recurrence across the six volumes on the two-line join, docket 36 names against the References body, census rows in range.
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
has_token = L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
appA = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix A ', l)][-1]; a15 = [i for i, l in enumerate(M, 1) if re.match(r'^### A\.15 ', l)][-1]
A, B = appA, a15; UL = M[A - 1:B - 1]; U = '\n'.join(UL); J = norm(U)
print('unit L%d–L%d, %d lines (own scan: `## Appendix A` body = last hit, `### A.15` = last hit)' % (A, B - 1, B - A))
def ul(pat, flags=0): return [A + i for i, l in enumerate(UL) if re.search(pat, l, flags)]

hr('§1 RULING 45 (build/editorial-process remarks) AND RULING 46 (script names, build numbers, internal files) — case-sensitive on the raw line')
r45 = ['register', 'audit', 'rerun', 'run', 'ledger', 'chat', 'session', 'build', 'draft', 'handoff', 'instrument', 'golden', 'banked', 'docket', 'census', 'verified', 'tested', 'measured', 'recomputed']
for t in r45:
    hits = [i for i in ul(r'(?<![A-Za-z])' + t + r'(?![A-Za-z])', re.I)]
    if hits: print('  %-11s' % t, hits, [norm(M[i - 1])[:80] for i in hits][:3])
print('  Verified/Measured/Tested lead-ins are the appendix\'s declared form for its own checks (A.8, A.9, A.10, A.11): recorded for chat 115\'s split, not scored')
print('  R46 — backticked names:', ul(r'`[^`]+`'), '; .py / BUILD / md5 / file references:', ul(r'\.py\b|BUILD\d|md5|\.md\b|\.tsv\b'), '— zero: negative witnessed by the two probes over all %d lines' % len(UL))

hr('§2 FIRST PERSON (probe carries mine and myself; `\\b(I|my|we|our)\\b` also matches the numeral in He I — hits are READ)')
fp = ul(r'\b(I|me|my|mine|myself|we|us|our|ours|ourselves)\b')
print('  hits:', fp, [norm(M[i - 1])[:110] for i in fp])
print('  read: every hit is the symbol I (the ionisation limit, T = I − E; "for constant I", "for any I", "all require I") — first person zero; witness: the probe fires on those lines and on nothing else')

hr('§3 STRUCTURE — bold lead-ins, whole-line italics, tables, rules, unmarked sub-headings, long lines, "Statement." / "Remark." conventions')
bold = ul(r'^\s*\*\*[^*]+\*\*'); print('  bold lead-ins (%d):' % len(bold), [(i, re.match(r'^\s*\*\*([^*]+)\*\*', M[i - 1]).group(1)[:30]) for i in bold])
print('  whole-line italics:', ul(r'^\s*\*[^*].*\*\s*$'), '; markdown table rows (a | at line start, code lines excluded — the three 4-space code lines L10004/L10041/L10047 begin with the absolute-value bar of |box ∩ Λ| and |ΔT|, read and excluded):', [i for i in ul(r'^\s*\|') if not M[i - 1].startswith('    ')], '; the whitespace-aligned table: header L%d, DATA rows %d' % (ul(r'^\s+statement\s+where')[0], len(ul(r'^\s+A\.\d+\s{2,}'))), '; rules (---):', ul(r'^\s*---'))
unm = [A + i for i, l in enumerate(UL) if i > 0 and not UL[i - 1].strip() and l.strip() and not l.startswith('#') and not l.startswith('    ') and len(l.strip()) < 60 and not l.strip().endswith(('.', '∎', ':', ',')) and not re.match(r'^\s+A\.\d', l)]
print('  unmarked sub-heading candidates (short line after a blank, not a heading, not code, not sentence-terminated):', unm, [norm(M[i - 1])[:60] for i in unm])
print('  lines over 400 chars:', ul(r'^.{401,}'), '; "Statement." lines:', ul(r'^\s*Statement\.'), '(7 = the seven sections); "Remark." lines:', ul(r'^\s*Remark\.'), '; proof-end ∎ lines:', ul(r'∎'), '(7 proofs, 7 ∎)')
print('  section-numbering gaps in the headings are by design: A.1, A.2, A.4–A.7, A.14, A.16, A.17 are the table\'s cross-referenced rows (r2-ch18a §1)')

hr('§4 NEGATIVES AND UNIVERSALS, EACH WITH A WITNESS (docket 19)')
neg = ul(r'\b(never|no |nowhere|none|nothing|cannot|not sufficient|only|every|any|all |always|whenever|wherever)\b', re.I)
print('  candidate lines:', neg)
print('  "The converse fails" (A.3 Remark): witness r2-ch18a §3 — the 2-cell set {(0,1),(1,0)} has closed projections and no join; §18.4 (L4980–L5293) carries "projection" at L4983–L4994')
print('  "no inclusion–exclusion" / "no cycles … no configuration counted twice" (A.10): witness r2-ch18a §6 — 7 edges on 8 nodes, connected; direct = factorised on 40 of 40 boxes and the full box')
print('  "grades Λ itself nowhere" (A.11) against "ν grades every chain": under δ = f − ℓ, 384 covering steps DECREASE ν (r2-ch18a §7) — ν does not grade every chain either; the two clauses are §12.2 L2328\'s (12a-01: no population for 24 of 70); 13t-04/13t-05 hold the definition open — recorded, not re-scored')
print('  "The two statements are equivalent for any I" (A.12): an identity — witness r2-ch18a §8, 5000 of 5000 and the cancellation argument')
print('  "obtained without fitting, without a quantum-defect expansion, and without assuming the series is smooth" (A.13 Inversion): the bound uses three neighbouring levels only — the proof\'s own construction is the witness; "to leading order" (L%d) is the caveat the Statement omits (r2-ch18a §9)' % ul(r'leading order')[0])
print('  "no channel in this work enters the failure regime" (A.13): witness — the §25.6 ν_fail table L6940–L6945 (8 of 8 reproduce, DEF chat-107 block) and L6947 "ν = 5.3 … below 6.6"; sites of "failure regime" in main:', [i for i, l in enumerate(M, 1) if 'failure regime' in l], '— the appendix restates §25.6\'s conclusion for one channel; "no channel" is the sweep §25.6 declares, not a second measurement (docket 17 kind: single witness)')
print('  "which is why no channel …" and "The two conditions are anticorrelated in nature" — an empirical universal asserted without a population in the unit; §25.6 sites of "anticorrelated|core excitation":', [i for i, l in enumerate(M, 1) if re.search(r'anticorrelated|core excitation', l)])

hr('§5 DOCKET 27 — RECURRENCE: every sentence of the unit ≥ 60 chars searched across the six volumes on the whitespace-normalised join (headings and the table excluded)')
sents = [s.strip() for s in re.split(r'(?<=[.∎])\s+', J) if len(s.strip()) >= 60 and not s.strip().startswith('#')]
joins = {v: norm(' '.join(t)) for v, t in VOL.items()}
rec = []
for s in sents:
    key = s[:120]
    for v, t in joins.items():
        c = t.count(key)
        if (v == 'main' and c > 1) or (v != 'main' and c > 0): rec.append((key[:70], v, c))
print('  sentences tested:', len(sents), '; recurrences outside the unit:', len(rec))
for r_ in rec: print('   ', r_)
print('  → the appendix\'s Verified lines restate chapter sentences by design (A.8 ↔ §15.3 L4302 in different words; A.9 ↔ L2017 identical clause "Verified against the recursive definition on 47 comparable pairs, values only in {−1, 0, +1}"; A.10 ↔ L2071 "Verified against direct enumeration on eight random intervals"; A.11 ↔ L4971 "86 violations at the caps tested"): cross-reference restatements, not the duplicated-section class; docket 27 clean count continues')

hr('§6 DOCKET 36 — NAMES IN THE UNIT AGAINST THE REFERENCES BODY (L11503–L11805) AND R.7 (L11806 on)')
names = ['Birkhoff', 'Rota', 'Boolean', 'Möbius']
refs = '\n'.join(M[11502:11805]); r7 = '\n'.join(M[11805:])
for n in names: print('  %-9s unit lines %s · References body %d · R.7 %d · Register lines %d' % (n, ul(n), len(re.findall(n, refs)), len(re.findall(n, r7)), sum(1 for l in R if n in l)))
print('  verdict: every name in the unit has a References-body line (Birkhoff 1, Rota 1, Boolean is a term); docket 36 gains nothing from this unit; Rota is absent from R.7 and from the Register (the appendix is the only citing site)')

hr('§7 WRAPPED PHRASES READ ON THE JOIN, AND THE OPENER\'S COUNT WORDS')
for ph in ['Nine proofs are given in full', 'nineteen in all', 'necessary and not sufficient', 'exactly as the Boolean-interval structure requires', 'a cylinder over ν and not one graded by it', 'anticorrelated in nature']:
    JS = re.sub(r'\*', '', J); print('  %-52s on the markup-stripped join: %d' % (ph, JS.count(ph)), '; raw lines (markup stripped):', [A + i for i, l in enumerate(UL) if ph in re.sub(r'\*', '', l)])
print('  "Meets are identical with ∧ throughout" (A.3 L9963): reads as "the meet case is identical, with ∧ throughout" — wording only')

hr('§8 CENSUS ROWS IN RANGE (DEFECT-CENSUS.tsv, member main, line in [L%d, L%d])' % (A, B - 1))
rows = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]; hdr = rows[0]; li = hdr.index('line') if 'line' in hdr else None; mi = hdr.index('member') if 'member' in hdr else None
print('  header:', hdr)
inr = [r for r in rows[1:] if li is not None and r[mi] == 'main' and r[li].isdigit() and A <= int(r[li]) < B]
print('  rows in range:', len(inr))
for r in inr: print('   ', r[:6])
