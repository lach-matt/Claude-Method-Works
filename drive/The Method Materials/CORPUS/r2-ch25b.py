# r2-ch25b.py — Appendix E part 2 (`### E.3` to `## Appendix F`), the PROSE / POINTER / PP claims (chat 138).
# Reads MEMBERS by name; imports r2lib by path; deterministic. Pointers resolved to the CLAIM under both resolvers (body_range, section_span);
# PP diff from the PP heading-form line (strip the section number from BOTH sides; PP sub-headings are unmarked, some without a blank line above).
import os, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
P = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

def rbody(n):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch25b — Appendix E part 2 (E.3–E.8), prose / pointers / PP diff; conventions named inline')
s = lettered(M, 'E.3')[-1]; f = lettered(M, 'Appendix F')[-1]; U = M[s - 1:f - 1]
def strip_md(t): return re.sub(r'[*_`\\]', '', t)
def norm(t): return re.sub(r'\s+', ' ', strip_md(t)).strip()
JOIN = norm(' '.join(U))
def home(i):
    for j in range(i, 0, -1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*|[A-G]\.\d+(?:\.\d+)*|Appendix [A-G])', M[j - 1])
        if m: return m.group(1)
    return '?'
def sites(pat, MM=M, lo=1, hi=None, flags=0): return [i for i in range(lo, hi or len(MM) + 1) if re.search(pat, MM[i - 1], flags)]

# §0 PP diff — headings from the PP heading-form line for E.3; body lines compared markup-normalised
def pheads(MM, lo, hi): return [(i, re.sub(r'^\s*#*\s*E\.\d(?:\.\d)*\s*', '', MM[i - 1]).strip()) for i in range(lo, hi) if re.match(r'^\s*(#{1,4}\s*)?E\.\d(?:\.\d)*\s+[A-Z]', MM[i - 1])]
pE3 = [i for i, l in enumerate(P, 1) if re.match(r'^\s*(#{1,4}\s*)?E\.3\s+[A-Z]', l)][-1]; pF = [i for i, l in enumerate(P, 1) if re.match(r'^\s*#{1,4}\s*Appendix F\b', l)][-1]
mh = pheads(M, s, f); ph = pheads(P, pE3, pF)
print('§0 PP diff: main L%d–L%d (%d lines) vs PP P%d–P%d (%d lines)' % (s, f - 1, f - s, pE3, pF - 1, pF - pE3))
print('   headings (section number stripped from both sides): main %d %s' % (len(mh), [(i, t[:40]) for i, t in mh])); print('   PP %d %s' % (len(ph), [(i, t[:40]) for i, t in ph]))
print('   PP heading-form lines WITHOUT a blank line above (read on their text): %s' % [(i, t[:40]) for i, t in ph if P[i - 2].strip()])
print('   heading text only-main: %s ; only-PP: %s' % (sorted(set(t for i, t in mh) - set(t for i, t in ph)), sorted(set(t for i, t in ph) - set(t for i, t in mh))))
mb = [norm(l) for l in U if l.strip() and not re.match(r'^\s*(#{1,4}\s*)?E\.\d', l)]; pb = [norm(l) for l in P[pE3 - 1:pF - 1] if l.strip() and not re.match(r'^\s*(#{1,4}\s*)?E\.\d', l)]
om = [l for l in mb if l not in set(pb)]; op = [l for l in pb if l not in set(mb)]
print('   body non-blank: main %d, PP %d, shared %d, only-main %d, only-PP %d' % (len(mb), len(pb), len(set(mb) & set(pb)), len(om), len(op)))
[print('   only-main: ' + l[:150]) for l in om]; [print('   only-PP:   ' + l[:150]) for l in op]

# §1 pointers in the unit — every §-pointer and lettered pointer resolved under BOTH resolvers with a claim token
PTR = [(i, m) for i in range(s, f) for m in re.findall(r'§(\d+(?:\.\d+)*)(?!\.\d)(?!\d)', M[i - 1])]
print('§1 numeric pointers in the unit: %d at %s' % (len(PTR), sorted({m for i, m in PTR})))
def probe(sec, toks, label):
    try:
        a, b = body_range(M, sec); a2, b2 = section_span(M, sec)
    except Exception as e:
        print('   §%s — NO HEADING (%s)' % (sec, e)); return
    res = []
    for tk in toks:
        nb = [i for i in range(a, b) if re.search(tk, M[i - 1], re.I)]; ns = [i for i in range(a2, b2) if re.search(tk, M[i - 1], re.I)]
        res.append('%s body %d span %d' % (tk, len(nb), len(ns)))
    print('   §%s %s body L%d–L%d span L%d–L%d: %s' % (sec, label, a, b, a2, b2, '; '.join(res)))
probe('12.11.1', [r'target-spin', r'six .*tests|six independent', r'Λ₉|Lambda_9|Λ9'], 'E.3 lead / E.8: item E answered here; Λ₉ six tests')
probe('29.7', [r'excess width', r'Newton decrement', r'partial identification', r'zero-error capacity', r'nine'], 'items C, G: the nine literatures and their vocabulary')
probe('12.11.6', [r'veto', r'proposal', r'calibrat'], 'item D: E(X) proposal vetoed by structure the index does not carry')
probe('31.3.4', [r'13 ≤ h', r'208', r'540', r'21,528', r'131', r'128', r'twelve', r'30,108', r'502'], 'item D\'s slice (where E.3\'s figures live)')
probe('30.3', [r'law', r'procedure', r'reorderab', r'polynomial', r'realisab', r'residue', r'Dilworth', r'Larson', r'width', r'J\(Λ\)', r'characteris', r'd = 2'], 'items F, G; E.5–E.8')
probe('30.3.5', [r'law', r'procedure', r'residue', r'realisab'], 'item F: *states the law, the procedure, and the residue — realisability*')
probe('24.9', [r'three kinds', r'independently', r'circular', r'Ritz', r'1,442'], 'item P: §24.9 concedes three kinds of value, two independently checkable')
probe('2.16', [r'first unmet', r'grid', r'downstream', r'reachable'], 'E.4: §2.16\'s grid, first unmet requirement')
probe('2.16.1', [r'access', r'difficulty', r'cost', r'reachable'], 'E.4: *§2.16.1 claims* what blocks is access')
probe('32.2', [r'\|Q\|', r'seven', r'assert'], 'E.4.1: *§32.2 asserted |Q| = 7*')
probe('2.10', [r'enumerate targets', r'before searching', r'SEARCH BEFORE DERIVING', r'search before deriving', r'derive'], 'E.7: *§2.10 says: enumerate targets before searching. It should have said, and now does: SEARCH BEFORE DERIVING*')
probe('30', [r'Frattini', r'NP-complete', r'Ryter', r'Schmid', r'Adams', r'Dwinger', r'Stahl', r'Wille', r'Yannakakis'], 'E.6 against Chapter 30')
probe('29.8', [r'Frattini', r'NP-complete', r'Stahl', r'Wille', r'Yannakakis', r'complexit'], 'E.6 against §29.8')
probe('28', [r'30\.3', r'reorderab', r'Siggers', r'Rival', r'sublattice'], 'E.8: *Sixty-odd corrections come from §30.3 alone*')
probe('7', [r'constructed', r'Λ₈|Λ8|Lambda_8'], 'item F: *its structure is constructed in Chapter 7*')
# Chapter 28's correction items citing §30.3 material: count numbered items whose text names 30.3 / reorderab / Siggers / Rival / sublattice
a28, b28 = section_span(M, '28'); items28 = [i for i in range(a28, b28) if re.match(r'^\s*\d+[\.)]\s', M[i - 1])]
hit28 = [i for i in items28 if re.search(r'30\.3|reorderab|Siggers|Rival|sublattice|subdirect|tight', M[i - 1], re.I)]
print('   Chapter 28 numbered item lines %d; items naming 30.3 / reorderab / Siggers / Rival / sublattice / subdirect / tight: %d %s (E.8 *Sixty-odd*; a token probe, not a reading — witness only)' % (len(items28), len(hit28), hit28[:12]))
# lettered pointers
for tag, toks in (('E.1.2', [r'CLOSED', r'depends']), ('E.4', [r'grid', r'reachable']), ('E.5', [r'precedent', r'derived']), ('E.2', [r'closed', r'Yes'])):
    hits = lettered(M, tag); print('   lettered %s heading hits %s%s' % (tag, hits, '' if hits else ' — NO HEADING (E.4: unmarked line L%s)' % (sites(r'^E\.4 ', M) or ['?'])[0]))
print('   *audit 15* (L11057; docket 33 numbering): sites main %s ; Register %s' % ([(i, home(i)) for i in sites(r'\baudit 15\b')], sites(r'\baudit 15\b', R)[:8]))

# §2 attributions — every name the unit prints, in the `## References` body (LAST heading hit)
refs = [i for i, l in enumerate(M, 1) if re.match(r'^#{1,3}\s*References\b', l)][-1]; RB = '\n'.join(M[refs:])
names = ['Paschen', 'Götze', 'Runge', 'Kreuzer', 'Skarke', 'Dilworth', 'Larson', 'Rival', 'Siggers', 'Birkhoff', 'Chen', 'Koh', 'Tan', 'Sharp', 'Stephen', 'Tucker', 'Booth', 'Lueker', 'Fulkerson', 'Gross', 'Schaefer', 'Ryter', 'Schmid', 'Adams', 'Dwinger', 'Ritz']
print('§2 `## References` body from L%d: %s' % (refs, {n: len(re.findall(r'\b' + n + r'\b', RB)) for n in names}))
print('   absent from the References body: %s' % [n for n in names if not re.search(r'\b' + n + r'\b', RB)])
print('   *Springer Book Archives* / *Encyklopädie* / *Order 11* / *Algebra Universalis* in References: %s' % {t: len(re.findall(t, RB)) for t in ('Springer Book Archives', 'Encyklopädie', 'Order 11', 'Algebra Universalis')})

# §3 first-person probe (mine, myself carried; the Roman numeral of a species excluded), Ruling 45 / 46 candidates
FP = re.compile(r'\b(I|my|me|mine|myself|we|our|us)\b'); SP = re.compile(r'\b[A-Z][a-z]? (I|II|III|IV|V|VI|VII)\b')
fp = [(i, M[i - 1].strip()[:70]) for i in range(s, f) if FP.search(SP.sub('', M[i - 1])) and not re.match(r'^\s*I\s+—', M[i - 1]) and not re.search(r'\bI\b\s+the spectroscopic', M[i - 1])]
print('§3 first-person hits (label lines `I —` and the grid row `I  the …` excluded): %s' % fp)
r45 = [(i, M[i - 1].strip()[:80]) for i in range(s, f) if re.search(r'this session|this author|this work|This chapter|this chapter|the register\b|audit \d+', M[i - 1])]
print('   Ruling 45 / 46 candidates: %s' % r45)
print('   *This chapter is where that is done* L11220 inside an APPENDIX: sites of `This chapter` in appendices %s' % [(i, home(i)) for i in sites(r'\bThis chapter\b') if i > heading_line(M, '36')])

# §4 phrase probes on the markup-stripped join (single-witness / withdrawn-figure checks)
for ph in ('three kinds of value', 'only two are independently checkable', 'SEARCH BEFORE DERIVING', 'enumerate targets before searching', 'not one open question blocks', 'the only column whose value has never changed',
           'An assertion is not an enumeration', 'Nine components, nine precedents', 'is it reachable from here', '3/2 bound', 'measured 3/4', 'Sixty-odd', 'closed at d = 2', 'nine unentered literatures'):
    outs = [(i, home(i)) for i in range(1, len(M) + 1) if ph.lower() in norm(M[i - 1]).lower() and not (s <= i < f)]
    print('   %-45s in unit %s ; outside %s' % (ph, ph.lower() in JOIN.lower(), outs[:8]))
print('   *3/4* volume-wide: %s ; *3/2* volume-wide: %s' % ([(i, home(i)) for i in sites(r'\b3/4\b')], [(i, home(i)) for i in sites(r'\b3/2\b')]))
print('   *An assertion is not an enumeration* — Register 211 body: %s' % (rbody(211) or '')[:160])
# E.6's two references and E.6's claim *at least one settled NP-complete* — the sentence's own witness is the citation; volume sites of Frattini / NP-complete
print('   Frattini sites %s ; NP-complete sites %s ; Ryter %s' % ([(i, home(i)) for i in sites(r'Frattini')], [(i, home(i)) for i in sites(r'NP-complete')], [(i, home(i)) for i in sites(r'Ryter')]))
# item A's figures at their source §25.6.3 — printed short
a, b = body_range(M, '25.6.3'); print('§5 §25.6.3 body L%d–L%d (item A\'s figures; printed rather than probed):' % (a, b)); [print('   L%d %s' % (i, M[i - 1].rstrip()[:160])) for i in range(a, b) if M[i - 1].strip()]
a, b = body_range(M, '31.3.4'); print('   §31.3.4 lines carrying 13 ≤ h / 208 / 131 / 128 / twelve:'); [print('   L%d %s' % (i, M[i - 1].rstrip()[:170])) for i in range(a, b) if re.search(r'13 ≤ h|\b208\b|\b131\b|\b128\b|twelve', M[i - 1])]
a, b = body_range(M, '2.10'); print('   §2.10 body L%d–L%d lines carrying enumerate / search / deriv:' % (a, b)); [print('   L%d %s' % (i, M[i - 1].rstrip()[:170])) for i in range(a, b) if re.search(r'enumerat|search|deriv', M[i - 1], re.I)]

# §6 witnesses printed (a short cited passage is printed, not probed)
from decimal import Decimal as D, ROUND_HALF_UP
HC = D('1.239841984e-4'); v = D('736688')
print('§6 §25.6.3 L7045 E = 736,688 cm⁻¹: × hc = %s eV (printed 91.338 at L7046 and E.3 L11059); 10⁷/736,688 = %s nm (printed 13.5743) — E.3 prints the eV of the POINT value beside the bracket, without the point value' % (
      (v * HC).quantize(D('0.001'), ROUND_HALF_UP), (D(10) ** 7 / v).quantize(D('0.0001'), ROUND_HALF_UP)))
def show(lines, label):
    print('   ' + label); [print('   L%d %s' % (i, M[i - 1].rstrip()[:175])) for i in lines]
show([(i) for i in sites(r'realisab')], 'realisab sites (item F: *§30.3.5 states … the residue — realisability*):')
a, b = body_range(M, '2.16.1'); show([i for i in range(a, b) if M[i - 1].strip()], '§2.16.1 body (E.4 L11126 *what §2.16.1 claims for it*):')
show([70, 9827], 'SEARCH BEFORE DERIVING outside the unit (E.7 L11209 *§2.10 … now does*):')
show([8096, 8549, 8572], 'NP-complete / Ryter sites in §29.8, §30.3.8, §30.3.9 (E.6 L11196 *This book has not read it*):')
a28, b28 = section_span(M, '28'); show([i for i in range(a28, b28) if re.search(r'30\.3', M[i - 1])], 'Chapter 28 lines naming 30.3 (E.8 *Sixty-odd corrections come from §30.3 alone*):')
show([8497, 8500, 11670], '3/2 in §30.3.4 and 3/2 · 3/4 in Appendix G (E.7 L11204 *Rival\'s 3/2 bound contains the measured 3/4*):')
a, b = section_span(M, '12.11.1'); show([i for i in range(a, b) if re.search(r'\btests?\b|target|spin', M[i - 1])][:10], '§12.11.1 span lines with test / target / spin (E.8 *Λ₉ passed six independent tests*; Register 384 *item E answered at §12.11.1*):')
a, b = body_range(M, '24.9'); show([i for i in range(a, b) if re.search(r'independen|checkab|circular|three kinds', M[i - 1])], '§24.9 lines with independen / checkab / circular / three kinds (item P):')
for ph in ('Newton decrement', 'partial identification', 'excess width', 'zero-error capacity'):
    print('   %-24s volume sites %s' % (ph, [(i, home(i)) for i in sites(ph)]))
print('   Register 368 (PP\'s removed paragraph cites it) body: %s' % (rbody(368) or 'NO HEADING')[:150])
print('   Register lines (volume-wide) naming 208 / 540 / 21,528 — Register 1437 among their entries: %s' % [i for i in sites(r'\b208\b|\b540\b|21,528', R) if 0 < i])
print('END r2-ch25b')
