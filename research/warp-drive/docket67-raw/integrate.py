"""Integrate DOCKET 67 grades: shard aggregation -> re-audit supersession -> adjudication.
Writes research/warp-drive/docket67-raw/VERIFIED-GRADES.tsv (one row per audited key) and prints the tally.
Precedence (later wins): shard final_grade < REAUDIT-GRADES.tsv final_grade (if not PENDING/DISPUTED)
< adjudication final_grade. An entry still disputed with no adjudication is marked UNRESOLVED."""
import json, glob, csv, os, sys
R = '/home/user/Claude-Method-Works/research/warp-drive/docket67-raw'
ADJ = R + '/adjudications'
rows = {}
for f in sorted(glob.glob(R + '/shards/shard*.json')):
    for a in json.load(open(f))['audits']:
        rows[a['key']] = dict(key=a['key'], shard=os.path.basename(f)[5:7], audit=a['grade'],
            proposals='/'.join(v.get('proposed_grade', '?') for v in a['verifiers']),
            rule=a['final_grade'], disputed=a['disputed'], reaudit='', adjudicated='',
            read_status=a['source'].get('read_status', ''), final=a['final_grade'], basis='shard')
for r in csv.DictReader(open(R + '/REAUDIT-GRADES.tsv'), delimiter='\t'):
    k = r['key']
    if k not in rows: print('reaudit key not in shards:', k, file=sys.stderr); continue
    rows[k]['reaudit'] = r['final_grade']
    if r['final_grade'] in ('STANDS', 'NARROWED', 'WRONG', 'DATA-DEPENDENT', 'OPEN'):
        rows[k]['final'] = r['final_grade']; rows[k]['basis'] = 'reaudit'
adj = {}
for f in glob.glob(ADJ + '/*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    if 'key' in d and 'final_grade' in d: adj[d['key']] = d
for k, d in adj.items():
    if k not in rows: print('adjudicated key not in shards:', k, file=sys.stderr); continue
    rows[k]['adjudicated'] = d['final_grade']; rows[k]['final'] = d['final_grade']; rows[k]['basis'] = 'adjudication'
    rows[k]['read_status'] = d.get('source_read_status', rows[k]['read_status'])
for r in rows.values():
    if r['basis'] == 'shard' and r['disputed'] and r['rule'] == 'OPEN': r['final'] = 'UNRESOLVED'
cols = ['key', 'shard', 'audit', 'proposals', 'rule', 'reaudit', 'adjudicated', 'final', 'basis', 'read_status']
with open(R + '/VERIFIED-GRADES.tsv', 'w') as o:
    o.write('\t'.join(cols) + '\n')
    for k in sorted(rows): o.write('\t'.join(str(rows[k][c]) for c in cols) + '\n')
from collections import Counter
print(len(rows), dict(Counter(r['final'] for r in rows.values())))
print('basis', dict(Counter(r['basis'] for r in rows.values())))
print('OPEN/UNRESOLVED:', sorted(k for k, r in rows.items() if r['final'] in ('OPEN', 'UNRESOLVED')))
print('WRONG:', sorted(k for k, r in rows.items() if r['final'] == 'WRONG'))
