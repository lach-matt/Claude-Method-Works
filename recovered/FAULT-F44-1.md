# F44.1 — TWO GATES WERE SPECIFIED AGAINST MODULES THAT CARRY NO ENTRY POINT, AND ONE OF THEM EXITS 0 WHILE COMPUTING NOTHING

Registered s44, at the gate step, BEFORE any Z>=39 work was opened.

## 0 · WHAT WAS MEASURED

**Gate 79**, as written in `README-HANDOFF-43.md`:

    NEW (79): PP-0 probe gate -- t7e_probe root vs parent solve_one on Z=21 3d, |de| < 1e-8.

Run as specified:

    $ python3 t7e_probe.py
    (no output)
    $ echo $?
    0

`t7e_probe.py` contains **no `__main__` block** — `grep -c '__main__' pack42/t7e_probe.py` returns **0**,
and the same holds for `t7f_rep.py`. The file imports its dependencies, defines `CAP`, `CapHFC`,
`make_shoot` and `capture`, and ends. Executing it as a script performs the imports and exits
successfully having compared nothing.

**Gate 80**, as written in `BRIDGE-LOWDIN-SESSION-43.md` §6:

    `D_of(HFCN,(3,2),Z=21)` equals `D_of(hfc2.HFC,(3,2),Z=21)` ... and `run(HFCN, CFG_CA+4d, 21)`

Run as specified against `t7g_exc`:

    AttributeError: module 't7g_exc' has no attribute 'D_of'

`t7g_exc.py` is 41 lines: one docstring, `import hfc2`, `class NodeCountMismatch`, `class HFCN`.
`D_of`, `run` and `CFG_CA` are defined in **`t7f_rep.py`** (lines 76, 79, 91), not in `t7g_exc`.
The gate text names the object under test and omits the module that drives it.

## 1 · WHY THE TWO HALVES ARE NOT THE SAME FAULT

Gate 80 **fails loudly**. An `AttributeError` cannot be mistaken for a pass; the gate is
under-specified but not dangerous, and the correct invocation is recoverable by reading the tree.

Gate 79 **passes silently**. `rc=0` is the signal every gate block records, and `gates_run.sh`
records exactly that. Had gate 79 been placed inside the numbered block rather than run by hand,
the log would carry `### GATE 79 / ### rc=0` with an empty body, and a future session diffing
gate logs would find byte-identity and read it as reproduction.

**This is R 1671's class and F43.1's class, one level further out.** R 1671: an instrument that
narrows its own input reports on what it admitted. F43.1: `sha256sum -c` reports on what the
manifest lists, and an unlisted file does not fail the check, it fails to be a file. Here: a
module with no entry point does not fail its gate, it fails to be a gate. **The exit code of a
Python module executed as a script is a statement about the import system, not about physics.**

The deeper point, and it is the reason this is registered rather than quietly fixed: gate 79 was
adopted in s42 *specifically to protect the instrument that produced that session's finding*
(bridge 42 §6: "It protects the instrument that produced this session's finding"). It has been
carried in the README through s43's open and s43's seal. **It has never been capable of failing.**
§4.6 says a pass is evidence only if the check can fail; gate 79 has been in the ledger for two
sessions as a pass that was never a check.

## 2 · WHAT THE GATES ACTUALLY REPORT WHEN DRIVEN CORRECTLY

Both PASS, on the filed numbers. Driven through `t7f_rep`:

**Gate 79 (PP-0), Z=21, healthy l=2 n=3 channel, config CFG_CA + 3d^1:**

    parent solve_one e   = -0.3808072853        (filed s42: -0.3808072853, exact match)
    probe root of log(nrm)= -0.3808072846        (filed s42: -0.3808072844)
    |de|                 = 6.67e-10              (filed 8.4e-10; bound 1e-8)
    log(nrm) at parent e = -2.825e-09            (filed -2.8e-09; bound 1e-6)
    nd at root           = 0                     (as required)

The parent eigenvalue reproduces to all ten filed digits. The probe root differs from the filed
root in the tenth decimal (2e-10). **That is the root-finder's tolerance, not the field**: s42's
bracket is not recorded in the pack, mine is `brentq` on [e-2e-6, e+2e-6] with `xtol=1e-14`.
Both roots sit an order of magnitude inside the gate's own 1e-8 bound and both give `nd = 0`.
Stated rather than smoothed: the gate is reproduced, the tenth digit is not, and the reason the
tenth digit cannot be reproduced is that **the bracket was never filed**.

**Gate 80, Z=21:**

    D_of(HFCN,(3,2),21) = {ok:True, D:-0.266643, it:[30,35], eps_ent:-0.335639}
    D_of(HFC ,(3,2),21) = {ok:True, D:-0.266643, it:[30,35], eps_ent:-0.335639}
    -> IDENTICAL, matching the s42 D1 reference exactly. Inertness holds.

    run(HFCN, nlchain.add(CFG_CA,(4,2)), 21) -> ok=False
    NodeCountMismatch: Z=21 4d nodes 0 (target 1) at e=-0.083340
      -- no normalisable 1-node solution in THIS field

The named exception carries Z, channel, node count, target and eigenvalue, as adopted under M's
ruling (2) of s43. No bracket, no scan, no number changed.

## 3 · REMEDY OWED

Gates 79 and 80 must become **runnable as written**. Two candidate forms, and the choice is M's
because it sets a precedent for every future diagnostic module:

  (a) Add a `__main__` block to `t7e_probe.py` and `t7g_exc.py`. Keeps the gate text as filed.
      Cost: edits two sealed pack files, which §H.4 discourages and which would break their
      manifest hashes.

  (b) Write one driver, `gate7980.py`, in pack44, which imports the modules and prints the six
      numbers above with PASS/FAIL against the filed bounds. Sealed pack files untouched.
      Cost: the gate text in the README must be corrected to name the driver.

**(b) is recommended** — it leaves the sealed tree byte-identical and puts the gate where every
other gate lives, in a script that `gates_run.sh` can call. Either way the gate must be shown to
FAIL before it is accepted: for 79, by perturbing the parent's e by 1e-7 and confirming the
|de| bound trips; for 80, by asserting inertness against a deliberately non-inert subclass.

**Until that driver exists and has been shown to fail, gates 79 and 80 are recorded as PASSED BY
HAND THIS SESSION, not as standing gates.**

## 4 · GENERAL FORM, FOR THE REGISTER

**A GATE IS NOT A CLAIM ABOUT A MODULE; IT IS A SCRIPT THAT RUNS AND CAN RETURN NON-ZERO.**
A gate recorded as a sentence in a README is an intention. The three faults now share one shape:
the verifier that could not see an unlisted file (F43.1), the thread-detector that could not see
an ownerless thread (R 1671), and the gate that could not see a missing entry point (F44.1).
In each, the instrument's input was narrowed by the same expression that was supposed to test it.
