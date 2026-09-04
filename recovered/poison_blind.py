# THE DECISIVE FORM.  Poison ground.expand with KeyError -- the exception step()
# already handles -- so the walk runs BLIND: it builds the field and picks the
# entrant with NO access to the observed table, and records prov=SYNTHESISED.
# Then compare its blind choice against the SEALED answer.
import ground as G, json
_real = G.expand
def blind(Z): raise KeyError("POISONED")
G.expand = blind
try:
    G.expand(29); print("POISON DEAD -- rc=4"); raise SystemExit(4)
except KeyError: print("POISON LIVE.")

import nlchain as NC
rows = NC.load()
agree = dis = 0
for Z in range(3, 21):
    cfg = NC.cfg_from_chain(Z - 1, rows)
    o = NC.step(Z, cfg, rows, "blind")
    sealed = rows[Z]['ent']
    same = (o['ent'] == sealed)
    agree += same; dis += (not same)
    if not same: print("  DISAGREE Z=%d blind=%s sealed=%s" % (Z, o['ent'], sealed))
    assert o['prov'] != 'OBSERVED', "table leaked in at Z=%d" % Z
print("BLIND WALK Z=3..20 : agree=%d disagree=%d  (prov=SYNTHESISED throughout)" % (agree, dis))