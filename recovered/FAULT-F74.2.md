# F74.2 — THE AUDIT WAS SCOPED TO THE WRAPPER AND MISSED THE REAL LEVER. Session 74.
**SEVERITY: SCOPE. TOUCHES NO SCORED ROW — and the row it would have touched came out clean
when measured properly (see PROVENANCE-TRACE-S74.md).**

**WHAT HAPPENED.** R-D was posed, by s73 and then by me, as an audit of `ground_occ`. The
derivation chain does not call `ground_occ`. It calls **`ground.expand`**, which `ground_occ`
merely wraps: `def ground_occ(Z): return [tuple(t) for t in G.expand(Z)]`.
**SO THE HEADLINE FINDING OF THE s74 AUDIT — "nlchain.py: ZERO SITES" — WAS TRUE OF THE NAME
AND FALSE OF THE THING.** nlchain.py consumes the observed table at four sites, lines 86-89.

**THIS IS F54.2's FAULT EXACTLY.** F54.2: a patch targeted function defaults in t7c_kernel that
the real call path bypassed positionally, and every clause-3 result computed on it was vacuous.
Here an audit targeted a wrapper name that the real call path bypasses. **Same failure, same
module family, twenty sessions apart: THE NAME AUDITED WAS NOT THE LEVER USED.**

**HOW IT WAS CAUGHT.** Not by reading. By the poison test — patching the lever and running the
chain to see whether it dies. It died at Z=3, immediately, on `ground.expand`. Source-tracing
had said clean twice.

**STANDING, PROPOSED TO M — the natural extension of R 1968:**
**AN AUDIT BY NAME IS NOT AN AUDIT. THE LEVER MUST BE POISONED AND THE CONSUMER MUST DIE.**
A name-scoped audit reports on the name; only an executed poison reports on the dependency.

**WHAT IS NOT AFFECTED.** No scored row. The properly scoped trace found the consumption is on
the SCORE side, after the entrant is chosen, and the blind walk confirmed it experimentally.