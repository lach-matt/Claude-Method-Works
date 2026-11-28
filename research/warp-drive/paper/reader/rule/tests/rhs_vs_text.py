# The right-hand side as printed in P-APPC2 (eq:appc-rhs) against solver/rhs_gen.h, definition by definition:
# both are parsed to Python syntax trees (⊙ -> *, constants -> their rational values, names mapped), compared in order.
import re, ast, sys
from fractions import Fraction as Fr
appc, gen = sys.argv[1], sys.argv[2]
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
txt = open(appc).read()
a = txt.index('    t₀ := Ω⁻² ⊙ s_v'); b = txt.index('{#eq:appc-rhs}')
lines = txt[a:b].split('\n'); defs = []
for l in lines:
    if not l.strip(): continue
    m = re.match(r'^    (\S+) := (.*)$', l)
    if m: defs.append([m.group(1), m.group(2)])
    else: defs[-1][1] += ' ' + l.strip()
def norm_text(name, e):
    e = e.replace('Ω⁻²', 'iOM2').replace('Ω²', 'OM2').replace('e^(−S)', 'iES').replace('e^S', 'ES').replace('R⁻¹', 'iR')
    e = e.translate(SUB).replace('⊙', '*').replace('−', '-').replace('X_m', 'Xm').replace('X_n', 'Xn').replace('X_R', 'XR')
    e = re.sub(r'\((\d+)/(\d+)\)', lambda m: 'C_%d_%d' % (Fr(int(m.group(1)), int(m.group(2))).numerator, Fr(int(m.group(1)), int(m.group(2))).denominator), e)
    e = re.sub(r'(?<![\w])(\d+)(?![\w/])', r'C_\1_1', e)
    name = name.translate(SUB).replace('X_m', 'Xm').replace('X_n', 'Xn').replace('X_R', 'XR').replace('X_W', 'XW').replace('X_s', 'Svv')
    return name, e
g = open(gen).read()
knum = [int(x) for x in re.search(r'RHS_KNUM\[\] = \{(.*?)\};', g).group(1).split(',')]
kden = [int(x) for x in re.search(r'RHS_KDEN\[\] = \{(.*?)\};', g).group(1).split(',')]
gd = re.findall(r'^\s*const auto (\w+) = (.*);\s*$', g, re.M)
def norm_gen(e):
    return re.sub(r'K\[(\d+)\]', lambda m: 'C_%d_%d' % (Fr(knum[int(m.group(1))], kden[int(m.group(1))]).numerator, Fr(knum[int(m.group(1))], kden[int(m.group(1))]).denominator), e)
T = [norm_text(n, e) for n, e in defs]
print('printed definitions: %d; generated: %d' % (len(T), len(gd)))
bad = 0
for (tn, te), (gn, ge) in zip(T, gd):
    if tn != gn: print('name differs:', tn, gn); bad += 1; continue
    at, ag = ast.dump(ast.parse(te, mode='eval')), ast.dump(ast.parse(norm_gen(ge), mode='eval'))
    if at != ag: print('definition %s differs:\n  text: %s\n  gen:  %s' % (tn, te[:200], norm_gen(ge)[:200])); bad += 1
print('definitions that differ: %d' % bad)
