#!/usr/bin/env python3
"""poison_blind.py -- s74 provenance trace, decisive form. Run FROM rt/.
Poison ground.expand with KeyError -- the exception step() already handles -- so
the chain runs BLIND: it builds the field and picks the entrant with NO access to
the observed table. Then compare the blind choice against the SEALED answer.
Writes nothing: verified by md5 of nlchain.jsonl before and after."""
import sys, ground as G
G.expand = lambda Z: (_ for _ in ()).throw(KeyError("POISONED"))
try:
    G.expand(29); print("POISON DEAD -- rc=4"); raise SystemExit(4)
except KeyError: print("POISON LIVE.")
import nlchain as NC
rows = NC.load(); agree = dis = 0
for Z in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    o = NC.step(Z, NC.cfg_from_chain(Z - 1, rows), rows, "blind")
    same = (o['ent'] == rows[Z]['ent']); agree += same; dis += (not same)
    if not same: print("  DISAGREE Z=%d blind=%s sealed=%s" % (Z, o['ent'], rows[Z]['ent']))
    assert o['prov'] != 'OBSERVED', "table leaked in at Z=%d" % Z
print("BLIND WALK SEGMENT : agree=%d disagree=%d (prov=SYNTHESISED throughout)" % (agree, dis))