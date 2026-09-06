# R 1968 / F54.2: DIRECT EXPERIMENTAL VERIFICATION.
# Poison BOTH the observed-table wrapper (t5_scf.ground_occ) AND the underlying
# generator (ground.expand) it wraps.  Poisoning only the wrapper would repeat
# F54.2 exactly: a lever bypassed by the real call path.
import t5_scf, ground as G

def poison(name):
    def f(*a, **k):
        raise RuntimeError("POISON: %s consumed on the derivation path %s" % (name, a))
    return f

t5_scf.ground_occ = poison("ground_occ")
_realexp = G.expand
G.expand = poison("ground.expand")

# CAN-FAIL, BOTH DIRECTIONS, BEFORE ANY ROW IS READ.
live = 0
for fn, nm in ((t5_scf.ground_occ, "ground_occ"), (G.expand, "ground.expand")):
    try:
        fn(29); print("POISON DEAD on %s -- rc=4" % nm); raise SystemExit(4)
    except RuntimeError:
        live += 1
print("POISON LIVE on both levers (%d/2): any consumer must now die." % live)

import nlchain as NC
rows = NC.load()
print("sealed rows loaded: %d" % len(rows))
ok = 0
for Z in range(3, 19):
    cfg = NC.cfg_from_chain(Z - 1, rows)
    if cfg is None:
        print("no chain cfg at Z=%d" % (Z - 1)); break
    try:
        NC.step(Z, cfg, rows, "poison")
    except RuntimeError as e:
        print("CONSUMED ->", e); raise SystemExit(1)
    ok += 1
print("WALKED %d chain steps (Z=3..%d) WITH BOTH TABLE LEVERS POISONED." % (ok, 2 + ok))