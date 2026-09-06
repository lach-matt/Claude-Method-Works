# THE METHOD 1.6 — HANDOFF TO A NEW SESSION

*Written 2026-08-10 after the session's rclone mount failed (every mount returning
EIO: outputs, uploads, transcripts). Everything below is what a new session needs
to resume with no gap.*

---

## 1 · WHAT TO UPLOAD, AND WHAT IS MISSING FROM IT

**Upload `restore-point-1_6p.tar.gz`.** It is complete through **register 1426**.

Missing from it, and recoverable from the previous session's transcript:

- **registers 1427–1433** (dumped verbatim in that transcript, one message before
  this one) — Λ_ladder's closure, B2a's resolution, C3's falsifier, C4's swaps,
  topic C complete, and the timing-line fix
- **six code changes**, listed at the end of that dump

Reapply by appending the seven entries to `REGISTER-DATA.md`, rebuilding with
`python3 register_gen.py > REGISTER.md`, and redoing the six edits. Then run both
gates (§4). If they pass, the state is identical.

---

## 2 · THE ZENO DIRECTIVE — the prime protocol

**No operation runs unbounded.** Every step declares a budget, writes its result
before the next begins, and is skipped on a rerun if it has already succeeded. A
step exceeding its budget is halved and retried, so work that cannot finish whole
finishes in pieces.

    from zeno import step, halve, State
    with State("audits") as st:
        n = step(st, "lattice pairs", lambda: count_pairs(L), budget=120)
        for part in halve(cells, budget=90):
            ...

Three guarantees: nothing is lost to a timeout — the last completed step is on
disk; a rerun costs only what has not succeeded; an overrun is reported, not
silently fatal. State lives in `.zeno/*.json` on **local** disk, so it survives a
mount failure.

**Session discipline, from the same directive:** phases close before the next
opens; no action until all inputs are acknowledged complete; reopens permitted
only on recorded facts. **And the lesson of 2026-08-10: apply it to the
execution, not only to the builds.** When a save path fails, stop and checkpoint
before continuing — a checkpoint converts an unrecoverable loss into a resumable
one.

---

## 3 · THE THREE PROTOCOLS — run them, they are code

    domain_protocol.py   four questions before any FIT. Blocks pooling.
                         1 DOMAIN which single cell of Λ_phys · 2 CARRIER which
                         variable the law runs in · 3 COUNT points ≥ 3× parameters
                         · 4 POOLING am I combining cells? If yes, STOP.

    contingency.py       four questions before any CHECK is reported (R 1383).
                         1 WITNESS construct an admissible neighbour that FAILS
                         · 2 SPACE state the admissible set BEFORE running
                         · 3 RATE what fraction of comparable objects fail
                         · 4 VANISHING does a factor vanish at the tested point?
                         A forced check is LABELLED, not deleted.

    roundtrip.py         four questions before a GENERATED artefact is trusted
                         (R 1389). DECLARE · ISOLATE (never regenerate over the
                         held copy) · DIFF · REFUSE (write nothing rather than a
                         partial file). 5 of 5 currently round-trip.

---

## 4 · THE GATES — both must pass before anything is called done

    python3 The_Method_1_6_audits.py     → ALL TWENTY-FIVE PASS
    python3 roundtrip.py                 → 5 of 5 round-trip

Rebuild chain: `register_gen.py > REGISTER.md` · `compendium.py > COMPENDIUM.md`
· `indices.py > INDICES.md` · `physics.py` and `spectra.py` write in place ·
`press_compendia.py` renders all five PDFs.

**Three artefacts have hand-authored tails** that the generators append and would
otherwise drop: `COMPENDIUM-TAIL.md`, `INDICES-TAIL.md`, `PHYSICS-TAIL.md`.
`physics.py` refuses to write without its tail; the other two do not need to.

---

## 5 · WHERE THE WORK STANDS

**Register 165–1433, 1,227 entries. All twenty-five audits pass.**

### Closed this session

- **Λ_ladder closed** — 14 ladders, 9 cells, E = 0, X-ray pair at the subvalence
  seat. Open since R 1356.
- **Λ_xray built** — 33 dipole lines → 9 transition types, E = 0, from Λ's own
  alphabet with no new data. Moseley recovered: slope 3.1906 against Bohr's
  3.1944, 0.12%.
- **Λ_spectra closes at the LIMIT** — the index runs to the last available
  species and stops. E = 58; 38 beyond the limit; 20 within, of which **11 are
  the Madelung exceptions, each nameable**.
- **The update rule derived** — a is placed at a corridor endpoint, which is a
  CROSSING where two subshells are exactly degenerate. Per-block monotone ascent
  gives zero violations in 106 steps and reproduces all eight recorded a values.
- **Topic C complete** — the nuclear corridor: ratio-4 identity, six pairs, three
  candidates eliminated, falsifier survived (the 82–126 shell holds both senses
  and is one region), refuted under all four orderings.
- **A.derived closed by measurement** — replace is free (E stays 0), adjoin is
  forbidden (E goes 0 → 47, box 24 → 168).
- **The walk is a calendar** — (block, position) gives E = 2, and **E equals the
  number of missing elements exactly**. The index is 120; the table is 118.

### The Löwdin standard

**Not complete.** It answers the ORDERING. It completes when it populates
Λ_spectra with δ per channel, verifiable against measured channels. End to end
with nothing fitted it reaches **99 of 106** against a Madelung null of 28; the
seven misses are the aufbau exceptions and are placement-independent.

---

## 6 · THE QUEUE — what is open

**A1 · the field shift.** Blocked: needs δ⟨r²⟩, the nuclear charge-radius
difference, which is neither held nor in the X-ray data. Six anchors exist in
`XRAY-KL3.tsv` (U, Pu, Cm, Am, Bk, Cf at two mass numbers each).

**A5b · δ = a·√p is REFUTED** (R 1416). R 1341's relation is an INDEX merge, not
a numeric identity. The Löwdin completion still needs a route from the walk to δ.

**A5c · the walk's cell as a transition.** R 1420: the landing axes refuse at
q = 2 and any SOURCE coordinate closes them. 12 of 106 steps have a real source;
94 come from outside. **Warning: minE over permutations is factorial — an axis
with 14 rungs OOM-kills the container. Cap the permutation count BEFORE building
the product.**

**B1 · Λ_xray wants the L-shell lines** — L2M1, L2M4, L3M1, L3M4, L3M5.

**B1b · is the σ-offset a COUNT?** Slater predicted 7.10 before measurement;
measured 5.30. The test that can fail: predict the 4p offset from L1N2/L1N3
BEFORE measuring.

**D2 · the ionisation ladders**, 15 of 108. Next: `K-Kr I-III`, the whole 3d block.

**D3 · Theodosiou, Inokuti & Manson 1986** — ~5,100 Hartree–Slater defects for all
ionisation stages of all ions with Z ≤ 50. The biggest single lever in the queue.

**D4 · AME2020 cited and not held** — E.nuclide = 9 cannot be reproduced.

**E2a · the Dirac coefficient** — A = 0.1162 against the derived 1/8, 7% low,
unexplained.

**G2 · Q.exch withdrawn** — the fitted sign is opposite the measured one; needs an
ℓ-dependent exchange term. It is six of Λ_spectra's eleven remaining cells.

**F2 · the book owes two chapters** — the Löwdin solution and the three-body
problem. **Nothing is written until both a target and a solution exist** (R 1359).

---

## 7 · CAPTURE — the route that works

**The person pastes a URL; Claude fetches it live.** Established after three
rounds of generated tables failed verification. Nothing is transcribed by anyone.

Generated data failed on: clean row counts where NIST is ragged, an absent
Ground-Shells column, energy errors of 0.2–11%, and **shell closures smoothed
away** — the discontinuity is the signal.

    ionisation:  physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=K-Kr+I-III&units=0
                 &format=1&at_num_out=on&sp_name_out=on&ion_charge_out=on
                 &seq_out=on&shells_out=on&level_out=on&e_out=0&unc_out=on

    X-ray:       physics.nist.gov/cgi-bin/XrayTrans/search.pl?element=All
                 &trans=KL3&units=eV&sorttype=energy      (swap trans=)

**Claude cannot vary a URL itself** — a fetch of an edited query returns the
previously seen page. Only URLs the person supplies are fetched fresh.

Held: `LADDER-H-Ar-I-III.tsv`, `XRAY-KL3.tsv`, `XRAY-KL2.tsv`, `XRAY-L1M.tsv`.

---

## 8 · THE RULES

Lock what is measured · one thing at a time · per element, not pooled · charge is
one symbol in three positions · evidence is not an object axis · calibrate on one
atom · **the neutral is not the table** · never fit across a language boundary ·
compendia answer, they do not argue · **read orderings from a source, never
compute or recall them** · **do not invent a cell or a column — reshuffle until it
fits or one cell remains** · **an index needs THREE axes, never two** ·
**an axis is determined when its values form a monotone chain** ·
**E = 0 is informative only where refusal was possible** ·
**never fill your own values when the source is supposed to be accurate** ·
**before calling a coordinate system new, ask whether its axes are the parent's
letters relabelled** · **read E as predictions, not defects**.

**And the purpose**: understanding, and sharing it in book form. Not novelty, not
priority. A result that reproduces a known one is stronger, not weaker — it is
checkable.

---

## 9 · RECURRING FAULTS TO WATCH FOR

These recurred repeatedly on 2026-08-10 and each cost real time:

1. **Reading a pattern in one's own output.** Placement-rule outputs read as
   measured values; binning artefacts read as structure (19 cells that were 24).
2. **Asserting a relation without computing it.** "Six of the eight are donors"
   — it was three, and three further inferences were built on it.
3. **Quoting a check before its null is known.** An integer search over 243
   combinations matching to 0.001; a 91% accuracy against an 87% baseline.
4. **Summary statistics over a series that turns.** A "negative drift" that was
   (last − first) across a rise-then-fall.
5. **Taking the collection's edge for the subject's.** `ground.py` stops at 108;
   the table runs to 118.
6. **Rebuilding what the restore point already contains.** `brack.py` builds the
   corridor exactly; a reimplementation scored 48/108 against its 106/106.
