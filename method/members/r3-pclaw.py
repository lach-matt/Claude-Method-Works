#!/usr/bin/env python3
"""r3-pclaw.py — R3: the corridor law enters the Physics Compendium; the count its template asks for is recorded
as one the compendium can no longer supply. BUILD204 -> BUILD205 compendia; BUILD100 -> BUILD101 main.

M's ruling (this R3): the THEOREM to the Mathematical Compendium (done at BUILD200, r3-mc-nos), the LAW to the
Physics Compendium, kind = "derived here" (params.py's _KIND[3]). DEF-153G-2 drafted the entry and held it on one
field, "N objects rest on it", which register 1740 defines as seeds plus transitive dependents in the compendium's
own dependency graph. MEASURED: the seated Mathematical Compendium prints 299 objects as `### Title` and no
dependency field — the "depends on" lines register 1749 walked are not printed at this build (seven occurrences
of the phrase, none a field), and qgraph.py, the member that walks them, builds a 0-node graph and exits 0
(DEF-153F item 2). So the count is not computable from the artefact for this entry or for the twenty-seven
parameters that print one: those counts are record-carried figures of register 1740's build, the class register
1813 entered for the §2.21 readouts. The entry prints what IS readable — four objects state the corridor — and
says so. Nothing is invented (register 1400's precedent).

PLACEMENT. The Löwdin-solution section of the Physics Compendium, in that section's own interface template,
immediately before "The collapse condition — interface only", whose text already names "the domain where
Chapter 34's corridor is silent". Not among Λ_phys's twenty-seven parameters: the law is not a parameter, and
a twenty-eighth row would move counts the volume prints. The kind line M ruled on is kept as the entry's second
line, as the Λ_phys entries carry theirs.

The compendia member is hand-authored territory by design (register 1503's precedent for the Löwdin tail); the
upstream debt — PHYSICS-TAIL.md, physics.py — is named and not paid here.

Sites: PC +35 lines (one entry). Register +4 (entry 1814). Ruling A holds.

Usage:  python3 r3-pclaw.py            dry run
        python3 r3-pclaw.py --write    writes staging members + BUILD205 compendia + BUILD101 main
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD204_compendia_papers_audits.md'); OLD_C_MD5 = 'fa8c8434938c420f7ba60511084e6acd'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD205_compendia_papers_audits.md')
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD100_main_and_register.md'); OLD_M_MD5 = 'a5f153e019de627fdd1f227a192a1653'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD101_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build205') + os.sep
PC = 'The_Method_1_6___The_Physics_Compendium-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

old_pc = open(MEM + PC, 'rb').read(); p = old_pc.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read(); r = old_reg.decode('utf-8')

ENTRY = """## The corridor law — interface only

*Chapter 34's law, as physics. The mechanism — the corridor as a system of linear
inequalities, and the hull form beneath it — is stated once, in the Mathematical
Compendium addition; this entry records what the law claims about nature and where
it could have failed.*

**derived here** · from this work · valid Z = 3–108 · four objects state it; the transitive count is not computable at this build (register 1814)

**What it states.** The subshell the differentiating electron enters is always one
the ν form can select at all: a vertex of the lower convex hull of the points
(√r, n), r = p + q/2(2ℓ+1), over the Pauli-admissible subshells — equivalently, its
corridor of admissible slopes `a` is non-empty. It holds at all 106 steps, Z = 3 to
108, in the node-only form and the finished form alike, and it could have failed at
any of them (§34.5; registers 1445, 1460, 1463).

**The transition.** From the observed ground configurations (NIST ASD 5.12,
register 1306) to a corridor per step: the two hull-edge slopes flanking the entrant.
The identity of the corridor with the hull-edge slopes is asserted at 0 mismatches
over 106 steps, in both forms.

**Must be measured.** Every step. The law is a statement about which configurations
nature realises, so it is *verified* and never *proved*; the theorem beside it — the
necessity of state — is the mathematics and needs no observation, and the law is
what observation adds.

**What physics does.** It supplies the entrant; the law says the entrant is never
outside the form's reach. **What it does NOT do:** select the entrant — every step
admits two to six hull vertices and one carried number decides among them (§34.6);
and non-emptiness refutes nothing: an empty corridor refutes the form and a
non-empty one does not confirm it (register 1460). **Where it fails:** not known
past Z = 108, where NIST lists no neutral ground configuration.

---

"""
ANCHOR = '\n---\n\n## The collapse condition — interface only\n'
assert p.count(ANCHOR) == 1 and p.count('## The corridor law') == 0
p = p.replace(ANCHOR, '\n---\n\n' + ENTRY + '## The collapse condition — interface only\n')
assert p.count('## The corridor law — interface only') == 1

E1814 = """

### 1814

**THE CORRIDOR LAW ENTERS THE PHYSICS COMPENDIUM AS AN INTERFACE ENTRY, AND THE COUNT ITS TEMPLATE ASKS FOR IS ONE THE COMPENDIUM CAN NO LONGER SUPPLY.** *M's ruling: the theorem to the Mathematical Compendium, the law to the Physics Compendium, its kind derived here. The law is placed in the Löwdin-solution section in that section's own interface template, beside the collapse condition, whose entry already names the domain where the corridor is silent — not among Λ_phys's twenty-seven parameters, since a law is not a parameter and a twenty-eighth row would move counts the volume prints. What it states: the entrant is always a vertex of the lower convex hull of (√r, n) over the Pauli-admissible subshells, its corridor of slopes non-empty, at all 106 steps in both forms, and it could have failed at any of them; it is verified and never proved, the theorem beside it being the mathematics.* **The template's 'N objects rest on it' is defined at register 1740 as the seeds plus every transitive dependent in the compendium's own dependency graph. Measured: the seated Mathematical Compendium prints 299 objects as titled sections and no dependency field — the lines register 1749 walked are not printed at this build, seven occurrences of the phrase and none a field — and qgraph.py, the member that walks them, builds a graph of no nodes and exits 0.** *So the count is not computable from the artefact, for this entry or for the twenty-seven that print one: Λ_phys's counts are the record-carried figures of register 1740's build, which is register 1813's class. The entry prints what is readable — four objects state the corridor: the corridor as linear inequalities, the falsification of a selection rule, the necessity of state, the collapse condition — and says the transitive count is not computable. Nothing is invented; register 1400's precedent governs. The upstream debt is unchanged: the Physics Compendium's tail is hand-authored by design and physics.py is not a member.* Registers 1306; 1400; 1445; 1460; 1463; 1503; 1740; 1749; 1813. (a measurement.)"""
assert r.count('### 1814\n') == 0 and r.rstrip().endswith('(a measurement.)')
r = r.rstrip() + E1814 + '\n'

new_p = p.encode('utf-8'); new_r = r.encode('utf-8')
print('pc  %d -> %d B, lines %+d' % (len(old_pc), len(new_p), p.count('\n') - old_pc.decode('utf-8').count('\n')))
print('reg %d -> %d B, lines %+d' % (len(old_reg), len(new_r), r.count('\n') - old_reg.decode('utf-8').count('\n')))
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((PC, old_pc.decode('utf-8'), p), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved)); assert not moved

if WRITE: assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
open(OUT + PC, 'wb').write(new_p); open(OUT + REG, 'wb').write(new_r)

def rebuild(old_path, old_md5, name, old_body, new_body, label):
    ob = open(old_path, 'rb').read(); assert md5(ob) == old_md5, label + ' md5 mismatch'
    ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob)); assert ms[name] == old_body
    nb = ob.replace(block(name, old_body), block(name, new_body)); assert nb.count(block(name, new_body)) == 1
    rv = nb.replace(block(name, new_body), block(name, old_body)); assert md5(rv) == old_md5, label + ' reverse FAILED'
    print('%s: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines %d members' % (label, old_md5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
    return nb
nbc = rebuild(OLD_C, OLD_C_MD5, PC, old_pc, new_p, 'BUILD204 -> BUILD205')
nbm = rebuild(OLD_M, OLD_M_MD5, REG, old_reg, new_r, 'BUILD100 -> BUILD101')
if WRITE:
    assert not os.path.exists(NEW_C) and not os.path.exists(NEW_M)
    open(NEW_C, 'wb').write(nbc); open(NEW_M, 'wb').write(nbm); print('written', NEW_C, NEW_M)
else:
    print('DRY RUN — nothing installed')
