"""nlseal48.py -- s48: SEAL Z=57 THROUGH THE CHAIN'S OWN INSTRUMENT, OR DO NOT SEAL IT.

s47 computed Z=57 with nlstep47.py and flagged the row UNSEALED-CANDIDATE, because
appending it by hand would put two instruments in one sealed file. This script is the
alternative route: nlchain.step -- now guarded (s48) -- recomputes the step, and the row
is appended ONLY if the physics reproduces pack47/Z57-CANDIDATE-ROW.json EXACTLY.

WHAT IS COMPARED (physics, not bookkeeping): ent, ent_nl, margin, the full order list of
(tag, D) pairs to five decimals, the SET of failed channel tags, and nfail. Iteration
counts, seconds and error-message wording are NOT compared -- they are instrument
bookkeeping and the two instruments format them differently.

usage: python3 nlseal48.py check      recompute + compare, DO NOT write
       python3 nlseal48.py seal       recompute + compare, write only if identical
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nlchain as NC

CAND = '../pack47/Z57-CANDIDATE-ROW.json'
Z = 57


def compare(row, cand):
    out = []
    out.append(('ent', row['ent'], cand['ent']))
    out.append(('ent_nl', list(row['ent_nl']), list(cand['ent_nl'])))
    out.append(('ok', row['ok'], cand['ok']))
    out.append(('margin', row['margin'], cand['margin']))
    out.append(('nfail', row['nfail'], cand['nfail']))
    out.append(('fail_set', sorted(row['fail']), sorted(cand['fail'])))
    out.append(('order', [[k, v] for k, v in row['order']],
                [[k, v] for k, v in cand['order']]))
    out.append(('ref_cfg', row['ref_cfg'], cand['ref_cfg']))
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
    cand = json.load(open(CAND))
    rows = NC.load()
    if Z in rows:
        print(f"Z={Z} ALREADY IN {NC.OUT} -- nothing to do."); return 0
    cfg = NC.cfg_from_chain(Z - 1, rows)          # F42.2: built by the chain, not re-parsed
    print(f"  ref cfg(56) from chain: {''.join(f'{n}{chr(0)}' for n,l,k in [])}", end='')
    print(''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in cfg))
    row = NC.step(Z, cfg, rows, 'chain')
    print()
    bad = 0
    for name, got, want in compare(row, cand):
        same = (got == want)
        bad += (not same)
        print(f"  [{'PASS' if same else 'FAIL'}] {name:<9} got {got}")
        if not same:
            print(f"          {'':<9} want {want}")
    print()
    if bad:
        print(f"REPRODUCTION FAILED on {bad} field(s). NOT SEALED.")
        json.dump(row, open('../Z57-RERUN-DISAGREES.json', 'w'), indent=1)
        return 1
    print("REPRODUCTION EXACT -- the two instruments agree on every physics field.")
    if mode == 'seal':
        row['prov_note'] = ('recomputed s48 by nlchain.step (guarded); reproduces '
                            'pack47/Z57-CANDIDATE-ROW.json exactly on all physics fields')
        open(NC.OUT, 'a').write(json.dumps(row) + '\n')
        print(f"SEALED: appended Z={Z} to {NC.OUT}")
    else:
        print("check mode -- nothing written. Re-run with `seal` to append.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
