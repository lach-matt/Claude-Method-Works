#!/usr/bin/env python3
"""AUDIT 27 -- POSSIBILITY BOUND.
For any object X with observed box B and cell count |X|:  0 <= E(X) <= B - |X|.
Any reported E outside that range is impossible, not merely unverified.
This is the audit that would have caught 8,856 without recomputation."""
import json, re, sys
D=json.load(open('/home/claude/paper/data.json'))
E3=json.load(open('/home/claude/paper/data3.json'))
F=json.load(open('/home/claude/paper/data4.json'))
MD=open('/mnt/user-data/outputs/Transitions.md').read()

rows=[]   # (name, cells, box, E, source)
def add(n,c,b,e,s): rows.append((n,c,b,e,s))

# --- from the datasets, wherever cells/box/E appear together
add('violation index (9)',   E3['nine']['cells'],   E3['nine']['box'],   E3['nine']['E'],   'data3.nine')
add('violation index (15)',  E3['fifteen']['cells'],E3['fifteen']['box'],E3['fifteen']['E'],'data3.fifteen')
add('axis index',            E3['axis_index']['cells'],E3['axis_index']['box'],E3['axis_index']['E'],'data3.axis_index')
add('V3 geometry',           F['V3']['cells'],      F['V3']['box'],      F['V3']['E'],      'data4.V3')
add('V6 solution',           F['V6']['cells'],      F['V6']['box'],      F['V6']['E'],      'data4.V6')
add('local null surface',    F['null_surface']['cells'],F['null_surface']['box'],F['null_surface']['E'],'data4.null_surface')
add('ANEC proof index',      F['anec_index']['covered'],F['anec_index']['box'],F['anec_index']['E'],'data4.anec_index')
add('charger index',         F['charger_index']['cells'],F['charger_index']['box'],F['charger_index']['E'],'data4.charger_index')
for d in E3['density_ladder']:
    if d['object'] not in ('Lambda_13','axis index'):
        add(d['object']+' (density ladder)', d['cells'], d['box'], None, 'data3.density_ladder')

# --- operations whose object is a PROJECTION: the box is the product of the
#     value counts of the coordinates the operation keeps.
OPS=[('slide within rows (15)', 3, [4,2,5], F['recomputed_values']['repair_slide_15'],
      'acts on the minimal triple {X_exp, U_ghost, NEC_pt}'),
     ('slide within rows (15) AS PUBLISHED', 3, [4,2,5], F['recomputed_values']['repair_slide_paper'],
      'the figure an earlier draft carried'),
     ('slide within rows (9)', 3, [4,3,5], 10, 'nine-letter analogue, data.json'),
     ('the minimal triple (15)', 3, [4,2,5], 1, 'the triple itself'),
     ('merge by linearisation (15)', 14, None, F['recomputed_values']['repair_linearise_15'],
      'collapses two axes; box is the 15-letter box divided by one axis'),
    ]

print('  AUDIT 27 -- POSSIBILITY BOUND')
print('  rule: 0 <= E <= box - cells.  a reported E outside that range is IMPOSSIBLE.')
print()
print('  %-40s %8s %10s %8s %10s %s' % ('object','cells','box','E','max E','verdict'))
fails=[]
for n,c,b,e,s in rows:
    mx=b-c
    if e is None:
        v='—  (no E reported)'
    elif 0<=e<=mx: v='ok'
    else: v='*** IMPOSSIBLE ***'; fails.append((n,e,mx,s))
    print('  %-40s %8s %10s %8s %10s %s' % (n,f'{c:,}',f'{b:,}',('—' if e is None else f'{e:,}'),f'{mx:,}',v))
print()
print('  OPERATIONS ON PROJECTIONS  (box = product of the kept coordinates\' value counts)')
print('  %-42s %6s %10s %8s %10s %s' % ('operation','d','box','E','max E','verdict'))
for n,d,vc,e,note in OPS:
    if vc is None:
        print('  %-42s %6d %10s %8s %10s %s' % (n,d,'(see note)',f'{e:,}','—','not boundable from here'))
        continue
    b=1
    for x in vc: b*=x
    mx=b            # E <= box - cells, and cells >= 1, so E <= box - 1; use box as the loose ceiling
    v='ok' if 0<=e<b else '*** IMPOSSIBLE ***'
    if v.startswith('*'): fails.append((n,e,b-1,note))
    print('  %-42s %6d %10d %8s %10d %s' % (n,d,b,f'{e:,}',b-1,v))
print()
if fails:
    print('  FAILURES')
    for n,e,mx,s in fails:
        print('     %-44s reported %-10s ceiling %-8s  %s' % (n,f'{e:,}',f'{mx:,}',s))
else:
    print('  no impossible values found')
print()
print('  WHAT THE AUDIT COSTS AND WHAT IT CATCHES')
print('     cost: one multiplication and one comparison per reported defect.')
print('     catches: any value that exceeds the ambient box of the object producing it.')
print('     does NOT catch: a wrong value that is merely inside the bound.')
print('     -> it is a necessary condition, not a sufficient one, and it is free.')
print()
print('  COVERAGE')
n_checked=len([r for r in rows if r[3] is not None])+len([o for o in OPS if o[2] is not None])
print('     objects with a reported (cells, box, E) triple : %d' % n_checked)
print('     objects whose box is not recorded              : %d'
      % (len([r for r in rows if r[3] is None])+len([o for o in OPS if o[2] is None])))
print('     -> the gap in this audit is objects that report E without reporting a box.')
print('        those cannot be bound-checked, and 8,856 was one of them until now.')
