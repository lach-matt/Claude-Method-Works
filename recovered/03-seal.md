SOURCE: the register session 1.8.5, 2026-08-15
ARTEFACT: regchat.py
TITLE: SELF-CORRECTION — `close` SEALED OVER AN EXISTING BANK ON ITS FIRST RUN, AND A SEAL IS NEVER OVERWRITTEN.
BODY:
*The version picker used `re.search` across three directory listings and took the FIRST match rather
than the highest, so it computed the bank name already in force and wrote over it — and over the copy
already staged in outputs. Caught immediately, because the verification step that follows tried to
open the successor and found no such file. The failure was loud, which is the only reason it was one
turn long.*
**Two faults, one shape, and both are this session's own material: first, an instrument that reads a
population and takes what it happens to reach first rather than what the population says — R 1578's
object-versus-observer fault and R 1701's 205 cliques, now committed by my own code. Second, a
destructive default: a seal is a fixed point of the record and MUST NOT be silently replaced.
`close` now takes the maximum version across uploads, home and outputs, and REFUSES if the target
already exists rather than overwriting it. Refusal where an operation would destroy, per §2.9.**