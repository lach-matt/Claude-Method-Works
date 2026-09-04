#!/usr/bin/env python3
"""r2-ch15q — prose batch for the chat-111 section read:
main L7856-L7939 (§29-§29.2.2) with L8222-L8237 (§28.10).

Pointers under both resolvers with the claim located, attributions, rulings 45/46,
the narrated-past-state forms, the false-universal census rows, and the PP witness.
Counts and figures are r2-ch15p.

Resolvers from r2lib by path.  body_range, the two-line join and the sentence-final
pointer regex are carried verbatim with provenance comments (r2lib owes all three).
"""
import importlib.util, os, re

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOLS = {
    'main':    'The_Method_1_6-2.md',
    'reg':     'The_Method_1_6___The_Register-2.md',
    'mc':      'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':      'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':     'The_Method_1_6___The_Index_of_Indices-2.md',
    'spectra': 'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
M = V['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

A0, A1, B0, B1 = 7856, 7939, 8222, 8237
RANGE = list(range(A0, A1 + 1)) + list(range(B0, B1 + 1))


# provenance: owed to r2lib since chat 105.
def body_range(lines, sec):
    s = heading_line(lines, sec)
    if s is None:
        return None
    for i in range(s + 1, len(lines) + 1):
        if re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', lines[i - 1].strip()):
            return (s, i)
    return (s, len(lines) + 1)


# provenance: owed to r2lib since chat 110.  '§N(?![\d.])' rejects a pointer that ends a
# sentence; the two-lookahead form does not.
PTR = re.compile(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)')


# provenance: owed to r2lib since chat 107.
def join_sites(lines, phrase):
    p = phrase.lower()
    raw = [i for i, t in enumerate(lines, 1) if p in re.sub(r'\s+', ' ', t).lower()]
    jn = []
    for i in range(1, len(lines)):
        j = re.sub(r'\s+', ' ', lines[i - 1] + ' ' + lines[i]).lower()
        if p in j and i not in raw and (i + 1) not in raw:
            jn.append(i)
    return raw, jn


def claim_in(sec, toks, resolver=body_range):
    """Token test over a section BODY, heading line excluded (chat 110's F-class:
    a body-less section otherwise resolves on a word in its own title)."""
    r = resolver(M, sec)
    if r is None:
        return None
    txt = '\n'.join(M[r[0]:r[1] - 1])
    return {t: has_token(txt, t) for t in toks}


out = []
P = out.append
P('r2-ch15q — prose batch, main L7856-L7939 (§29-§29.2.2) + L8222-L8237 (§28.10)')

# ---------------------------------------------------------------- 1. pointers
P('')
P('1. EVERY §-POINTER IN THE UNIT, UNDER BOTH RESOLVERS')
ptrs = {}
for i in RANGE:
    for s in PTR.findall(M[i - 1]):
        ptrs.setdefault(s, []).append(i)
for s in sorted(ptrs, key=lambda x: [int(y) for y in x.split('.')]):
    br, sp = body_range(M, s), section_span(M, s)
    hl = heading_line(M, s)
    P('  §%-10s cited L%-22s heading %-7s body %-14s span %s'
      % (s, ','.join(str(x) for x in ptrs[s]), hl, br, sp))
    if hl:
        P('  %-12s %s' % ('', re.sub(r'\s+', ' ', M[hl - 1].strip())[:96]))
    else:
        P('  %-12s NO HEADING — resolve as a table row or a lettered heading' % '')

# ---------------------------------------------------------------- 2. claim tests
P('')
P('2. THE THREE POINTERS THAT NAME WHAT THE TARGET SAYS — claim, not heading')
P('  a. L7907 "the position §29.3 below already states — E(X) is deliberately not claimed as novel"')
P('     §29.3 body tokens: %s' % claim_in('29.3', ['E(X)', 'novel', 'unprecedented', 'deliberately']))
for k, lines in V.items():
    r, j = join_sites(lines, 'deliberately not claimed as novel')
    if r or j:
        P('     phrase "deliberately not claimed as novel" %s raw %s join %s' % (k, r, j))
P('  b. L7916 "This is the shape §29.4 already describes — Q growing at nearly every step"')
P('     §29.4 body tokens: %s' % claim_in('29.4', ['Q', 'growing', 'scope', 'novelty', 'priority']))
for ph in ('growing at nearly every step', 'grows at nearly every step', 'while its scope falls'):
    for k, lines in V.items():
        r, j = join_sites(lines, ph)
        if r or j:
            P('     "%s" %-6s raw %s join %s' % (ph, k, r, j))
P('  c. L7905 "§29.2 asks what component this work owns"')
P('     §29.2 body tokens: %s' % claim_in('29.2', ['component', 'owns', 'owner', 'claimed']))
P('  d. L7937 "§32.1.4 proves none of them can"')
P('     §32.1.4 body tokens: %s' % claim_in('32.1.4', ['ℛ', 'operator', 'axis', 'index']))
P('  e. L7896 "does it state its falsification conditions? yes, §32.5"')
P('     §32.5 body tokens: %s' % claim_in('32.5', ['falsif', 'condition', 'fail']))
P('  f. L7890 "quoted and cited at §23.8.4"')
P('     §23.8.4 body tokens: %s' % claim_in('23.8.4', ['Moore', 'Manski', 'Shannon', 'IEEE']))
P('  g. L7923 "The promotion arithmetic of §12.11.0.10"')
P('     §12.11.0.10 body tokens: %s' % claim_in('12.11.0.10', ['promotion', 'branch', 'bits']))

# ---------------------------------------------------------------- 3. attributions
P('')
P('3. ATTRIBUTIONS MADE IN THE UNIT — other sites in six volumes')
for nm in ('Gödel', 'Boole', 'Nörlund', 'Steffensen', 'Aitken', 'Seki', 'Nesterov',
           'Nemirovskii', 'Moore', 'Manski', 'Shannon', 'Edlén', 'Galois', 'Stahl', 'Wille'):
    hits = {k: [i for i, t in enumerate(lines, 1) if nm in t][:5]
            for k, lines in V.items()}
    hits = {k: v for k, v in hits.items() if v}
    P('  %-12s %s' % (nm, hits))
P('  P20 sites in main: %s' % [i for i, t in enumerate(M, 1) if re.search(r'\bP20\b', t)][:10])
P('  "Chapter 16" / "Chapter 27" in the unit: %s'
  % [(i, re.sub(r'\s+', ' ', M[i - 1].strip())[:56]) for i in RANGE
     if re.search(r'Chapter (16|27)', M[i - 1])])

# ---------------------------------------------------------------- 4. narrated past state
P('')
P('4. THE NARRATED-PAST-STATE CLASS (docket 15) — every word-form')
for ph in ('an earlier draft', 'an earlier version', 'a previous draft',
           'the earlier draft', 'nothing had ever looked'):
    r, j = join_sites(M, ph)
    P('  main "%-22s" raw %-38s join %s' % (ph, r[:9], j[:6]))
P('  in the unit: %s' % [(i, re.sub(r'\s+', ' ', M[i - 1].strip())[:70]) for i in RANGE
                         if re.search(r'earlier (draft|version)|had ever looked', M[i - 1], re.I)])

# ---------------------------------------------------------------- 5. rulings 45 / 46
P('')
P('5. RULINGS 45 (build/editorial-process remarks) AND 46 (script or file names) IN THE UNIT')
R45 = ['this session', 'across this session', 'an earlier draft', 'the author has answered',
       'recorded here', 'in one sitting', 'arrived last', 'had not noticed']
R46 = ['regex', '.py', 'build', 'script', 'BUILD', 'commit']
for i in RANGE:
    t = M[i - 1]
    h45 = [p for p in R45 if p.lower() in re.sub(r'\s+', ' ', t).lower()]
    h46 = [p for p in R46 if re.search(r'(?<![A-Za-z])' + re.escape(p) + r'(?![A-Za-z])', t)]
    if h45 or h46:
        P('  L%-6d 45%-32s 46%-14s %s' % (i, h45, h46, re.sub(r'\s+', ' ', t.strip())[:62]))

# ---------------------------------------------------------------- 6. census rows
P('')
P('6. THE FIVE CENSUS ROWS IN RANGE — false universals, read against the sentence')
for cid, ln, tok in ((708, 7920, '238'), (1171, 7863, 'never'), (1172, 7867, 'always'),
                     (1173, 7928, 'never'), (1178, 8231, 'never')):
    P('  %-5d L%-6d %-6s %s' % (cid, ln, tok, re.sub(r'\s+', ' ', M[ln - 1].strip())[:96]))
P('  every never/always/only/every in the unit:')
for i in RANGE:
    for w in ('never', 'always', 'no amount', 'every component', 'unlike novelty', 'only'):
        if has_token(M[i - 1], w.split()[0]) and w.split()[0] in M[i - 1].lower():
            P('    L%-6d %-14s %s' % (i, w.split()[0], re.sub(r'\s+', ' ', M[i - 1].strip())[:72]))
            break

# ---------------------------------------------------------------- 7. heading sentence
P('')
P('7. HEADING SENTENCES FINISHING IN THE BODY (docket 18)')
for sec, hl in (('29', 7856), ('28.10', 8222)):
    P('  §%-7s heading L%d  %s' % (sec, hl, M[hl - 1].strip()[:72]))
    nxt = next((i for i in range(hl + 1, hl + 6) if M[i - 1].strip()), None)
    P('  %-9s first body line L%s  %s' % ('', nxt, M[nxt - 1].strip()[:78] if nxt else '-'))

# ---------------------------------------------------------------- 8. PP witness
P('')
P('8. PRINTS & PROOFS WITNESS — which sentences post-date the input')
for ph in ('an earlier draft did', 'six of the eleven items', 'the three documents we could not reach',
           'the modular interval at', 'Nothing had ever looked', 'Q growing at nearly every step'):
    rm, jm = join_sites(M, ph)
    rp, jp = join_sites(PP, ph)
    P('  "%-40s" main %-14s PP %s' % (ph[:40], (rm or jm)[:4], (rp or jp)[:4] or 'ABSENT'))

print('\n'.join(out))
