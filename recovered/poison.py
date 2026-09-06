# R 1968 / F54.2: DIRECT EXPERIMENTAL VERIFICATION, not source-tracing.
# Poison the observed table. If the derivation consumes it ANYWHERE on its
# execution path, it must now die. If it walks, it does not consume it.
import t5_scf
_real = t5_scf.ground_occ
def poisoned(Z):
    raise RuntimeError("POISON: ground_occ() was consumed by the derivation path at Z=%s" % Z)
t5_scf.ground_occ = poisoned

# CAN-FAIL, BOTH DIRECTIONS: prove the poison actually bites before trusting a pass.
try:
    t5_scf.ground_occ(29); print("POISON DEAD -- rc=4"); raise SystemExit(4)
except RuntimeError:
    print("POISON LIVE: a consumer would die.")

import nlchain as NC
rows = NC.load()
cfg = None; n = 0
for Z in range(2, 31):
    try:
        r = NC.step(Z, cfg, rows, "poisontest")
    except RuntimeError as e:
        print("CONSUMED:", e); raise SystemExit(1)
    except Exception as e:
        print("OTHER ERROR (not the table):", type(e).__name__, str(e)[:90]); raise SystemExit(2)
    n += 1
print("WALKED %d steps Z=2..30 with the observed table POISONED." % n)