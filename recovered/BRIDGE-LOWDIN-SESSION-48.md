# BRIDGE — LOWDIN SESSION 48

Open Session 49 from this document. Everything below is either DERIVED in s48 or RECALLED
and flagged. The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 48 DID

The **4f block was closed** (Z=61..71, eleven steps) and the **5d block was opened**
(Z=72..75, four steps). The chain now stands at **74 rows, Z = 2..75**, every step at rung 0 —
the guard was invoked nowhere in fifteen steps. Two new instruments were built and run:
`pb4_terms.py` (two-configuration competition with Slater term energies) and `pb4_so.py`
(first-order spin-orbit on the hfc2 field). Four prediction files were filed BEFORE their
runs and all four were scored.

---

## §2 · THE RULING OF THE SESSION — BANDS ARE DROPPED, CLAUSES ONLY

M's ruling, taken after five bands had been filed on collapsing channels and four had failed
in the SAME direction (too shallow): PO-1, PO-4, PC4F-2 (83x), PCE-2. A band is a linear
extrapolation; collapse is not linear. In every case the CLAUSE held while the band failed.

**Bands are filed ONLY where the band IS the mechanism claim.** The one band filed on that
basis in s48 — PB-5, that 5d rises monotonically across the whole 4f block — **HELD, clause
and threshold**. One mechanism band held; four extrapolation bands failed. The form change is
evidenced, not asserted.

---

## §3 · THE 4f BLOCK, CLOSED AND SCORED (PREDICTION-4fBLOCK-61-71)

    Z    ent  rec   ok      D_4f      4f step     D_5d      5d step   margin
    61   4f   4f   True   -0.43256   -0.01786   -0.24181   +0.00191   0.19075
    62   4f   4f   True   -0.44722   -0.01466   -0.23944   +0.00237   0.20778
    63   4f   4f   True   -0.45906   -0.01184   -0.23667   +0.00277   0.22239
    64   4f   5d   FALSE  -0.46840   -0.00934   -0.23355   +0.00312   0.23485
    65   4f   4f   True   -0.47545   -0.00705   -0.23012   +0.00343   0.24533
    66   4f   4f   True   -0.48043   -0.00498   -0.22642   +0.00370   0.25401
    67   4f   4f   True   -0.48348   -0.00305   -0.22246   +0.00396   0.26102
    68   4f   4f   True   -0.48475   -0.00127   -0.21829   +0.00417   0.26646
    69   4f   4f   True   -0.48434   +0.00041   -0.21391   +0.00438   0.27043
    70   4f   4f   True   -0.48236   +0.00198   -0.20935   +0.00456   0.27301
    71   4f   5d   FALSE  -0.47890   +0.00346   -0.20464   +0.00471   0.27426

**PB-1 HELD** — 4f took all nine of 61,62,63,65,66,67,68,69,70.
**PB-2 HELD** — ok=False at Gd(64) and Lu(71) and nowhere else, as filed.
**PB-5 HELD** — no negative 5d step anywhere in 61..71; D_5d(71) = -0.20464, above the filed
-0.235. The rises ACCELERATE monotonically, +0.00075 at 59 to +0.00471 at 71.
**PB-6 SPLIT** — ok_score filed 63 of 70, got **exactly (63,70)**. cfg_score filed to stay at
49, got **(51,70)**: FAILED, and informatively (see §4).
**PB-7 HELD** — no constant introduced.

Physics worth carrying: **4f's step turns POSITIVE at Z=69** as intra-shell repulsion
overtakes the nuclear pull, while 5d keeps retreating faster, so the margin still widens to
0.274 at Lu.

---

## §4 · THE STRUCTURAL FINDING — cfg MATCHES WHERE ok FAILS

The two cfg PASSES in the block are at **64 and 71 — the two elements where ok FAILS**. The
walk spent Z=57 on 5d and cannot vacate it, so its 4f count reaches 7 at Gd and 14 at Lu, and
the record's Gd is 4f7 5d1 6s2 and its Lu is 4f14 5d1 6s2.

**The walk and the record agree on the STATE at exactly the steps where they disagree about
which electron was added.** Those disagreements are bookkeeping about the differentiating
electron — the Cr(24) class, part 2's business — and they leave the n+l ORDERING untouched.
**La(57) remains the only place in 75 elements where the ordering itself fails.**

PD-4 predicts this structure recurs a third time at Hg(80). If it does, it is structural.

---

## §5 · THE PROMOTION MECHANISM — WHAT s48 ESTABLISHED AND WHAT IT DID NOT

PB-4 named Gd and Lu as the elements to test for exchange. **That framing was wrong and the
correction was registered BEFORE the run** (PREDICTION-PB4-TEST §1): at 64 the field was
choosing between 4f7 5d1 6s2 and 4f6 5d2 6s2 and it chose the record's configuration — it
never faced 4f8. **The divergence has ONE origin, Z=59**, where the record vacates 5d and
takes two 4f. Everything from 59 to 71 descends from that step.

**Z=59 (Pr), A = 4f2 5d1 6s2 (walk) vs B = 4f3 6s2 (record):**

    dAVG  = -0.048991      PT-1 HELD   field prefers A at avg-of-config
    dTERM = +0.045148      PT-2 HELD   exchange pushes toward B -- closes 92% of the gap
    dTOT  = -0.003844      PT-3 FAILED exchange does NOT flip it
    dSO   = -0.004177      PS-2 FAILED SO moves it the WRONG WAY
    dTOT+dSO = -0.008021               net residual against the record

**Z=64 (Gd), A = 4f7 5d1 6s2 (record) vs B = 4f8 6s2:**

    dAVG  = +0.015588      PT-4 clause FAILED -- at avg-of-config the field puts Gd in 4f8,
                           which is NOT the record's Gd. The flat field gets Gd WRONG.
    dTERM = -0.184146      exchange reverses it by 184 mHa; sign OPPOSITE to Z=59 as filed
    dTOT  = -0.168558      PT-4 dTOT clause HELD -- record's configuration lands lower
    dTOT+dSO = -0.163454   PS-4 HELD -- SO does not disturb Gd

**Exchange is the named mechanism**: it is what makes Gd's half-filled shell win, and it
accounts for 92% of the promotion at Pr, computed on the walk's own field with no new
constant. Terms were COMPUTED by the Slater diagonal-sum rule, not asserted: B's lowest term
at 59 came out **4I with J=9/2** (Pr's actual ground level) and A's at 64 came out **8S** with
the coupled label **9D** (Gd's actual ground term). Neither was entered.

**Two structural results fell out.** 4f7 takes **zero** first-order SO shift (half-filled,
L=0, 8S) — Gd's entire SO shift comes from its single 5d electron, so the shell that wins Gd
on exchange cannot be moved by spin-orbit. And at Pr, A gets **two** SO bites (4f2 at
-0.012259 PLUS 5d1 at -0.004510) against B's single 4f3 shell at -0.012592 — the lone 5d
electron's own SO stabilisation is what defeated PS-2.

**THE RESIDUE IS -8.021 mHa AT Z=59. RESIDUE IS NOT CLOSURE. This is the smallest open object
in the chain and the sharpest target the project has.**

---

## §6 · THE 5d BLOCK, OPENED (PREDICTION-5dBLOCK-72-80, filed before Z=72)

    Z    ent  rec   ok      D_5d      step       D_6p     margin
    72   5d   5d   True   -0.19978   +0.00486   -0.15471  0.04507
    73   5d   5d   True   -0.23854   -0.03876   -0.15981  0.07873
    74   5d   5d   True   -0.27704   -0.03850   -0.16395  0.11309
    75   5d   5d   True   -0.31567   -0.03863   -0.16740  0.14827

PD-1, PD-2, PD-5 holding at four of nine steps. 4f closed at 71 and has LEFT the open-channel
competition entirely. **From 73 the steps are almost exactly constant** — -0.03876, -0.03850,
-0.03863, a spread of 0.00026 across three protons — a flat linear deepening, against the 4f
block's collapse-then-saturate profile (-0.261 falling to -0.009). **Two blocks, two filling
mechanisms, one field, no parameter distinguishing them.** The Z=72 positive step is the
handoff artefact: 5d was still retreating at Lu when the new block opened.

---

## §7 · GATES AND FAULTS

Gates 1..71 diffed to ZERO against sealed GATES-47-OPEN.log (sole difference gate 6 `sec`
8->9, excluded by rule). PT8 dsum <= 2.78e-17. 77: 0 UNSAFE. **78: 63/70 at block close,
FIRST DIVERGENCE 25 — unmoved.** 79+80 PASS. 81 PASS. **83 restated TWICE and PASS 8/8**, can
-fail exit 1. 84 PASS 6/6, all exits read unpiped.

**Gate 83's invariance taxonomy was AMENDED, not widened quietly.** cfg_fail and disagree were
declared chain-length-invariant; the extension to Pr/Nd falsified that. They are now
**PREFIX-invariant**: no listed Z may disappear, none may appear below the previous extension
point, and an append at the growing end requires a NAMED mechanism. The mechanism is recorded
in the gate's own text.

**F48.1** — SESSION-47-COMBINED.md's header states ok=984; the true count is **985**. It
omits itself: the manifest's 985th entry is the combined document, sealed after its own header
was written. README-47 says ok=N and is correct. Benign; the s48 header is written after
sealing.
**F48.2 (label-only)** — for multi-open-shell configurations `pb4_terms.low_A` reports terms
of the single largest open shell (4f2 -> 3H) while `dE_A` is computed across ALL open shells
via hund_det. Energies two-shell and correct; printed LABEL one-shell and incomplete. No
result depends on it.
**TIMING FLAG (R 1449)** — **Z=59 and Z=60 ran with NO prediction covering them**;
PREDICTION-Ce58 §4 declares Pr(59) onward not predicted. Both rows are logged as results and
are **NOT scored as predictions**. Registered, not suppressed.
**DECLARED APPROXIMATION** — `pb4_so.py` treats multi-open-shell SO **shell-additively in the
LS limit**; a coupled 4f2·5d treatment is NOT done. Declared before the run. It is precisely
the 5d1 term that decided PS-2, so this approximation is load-bearing and is owed a check.

---

## §8 · ORDERED WORK LIST FOR SESSION 49

1. **Finish the 5d block, Z=76..80.** PD-3 (cfg fails at exactly Pt(78) and Au(79)), PD-4
   (cfg matches where ok fails, third occurrence, at Hg(80)) and **PD-6's two integers —
   ok_score (71,79) and cfg_score (58,79)** are the live scoreable items. Restate gate 83.
2. **Correlation on configuration competition at Z=59.** The LAST untested candidate for the
   -8.021 mHa residual. The s37 class-flat ruling was established for IONIZATION classes and
   explicitly does NOT transfer to configuration competition — this is open, not closed.
   Run S-form (CORR=True) on both configurations on the same instrument.
3. **Coupled 4f2·5d SO at Z=59**, to test the declared shell-additive approximation that
   decided PS-2 against the prediction. Comparison decides between 2 and 3; both must run.
4. **PREDICTION-OPENINGS REFILED BEFORE Z=89.** Binding. No current file covers past Z=80.
5. Continue the walk 81 onward under a filed prediction.
6. The promotion operator, as its own object. It is NAMED (exchange, 92% at Pr) but NOT BUILT,
   and naming is not closure.
7. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s48.
