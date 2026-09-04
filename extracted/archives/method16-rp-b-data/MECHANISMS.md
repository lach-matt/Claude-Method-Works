# MECHANISMS IDENTIFIED IN THE SPECTRA WORK

**Staged for the mathematics register.** Each is a mechanism the compendium's own
measurements exposed, not something quoted from the literature and not something the
computation was told. They are listed here with the registers that establish them and the
evidence that would falsify them, ready to be entered as objects in `mathreg.py` once the
Spectra Compendium is closed.

**Format matches `mathreg.py`**: key · statement · grade · source · dependencies.

---

## P.qdt — the quantum defect measures core penetration

**A Rydberg electron's quantum defect measures how far its orbital reaches into the ionic
core.** Everything below is a consequence of that one statement, and the compendium tests
it four independent ways without ever encoding it.

  grade    MEASURED
  source   registers 693, 707, 713, 714
  depends  —
  falsify  any species where the defect fails to fall monotonically with ℓ

---

## P.lcollapse — the ℓ-collapse

**The defect falls monotonically with ℓ and reaches zero by f.** Core penetration decreases
as the centrifugal barrier pushes the orbital outward; by ℓ = 3 the orbital no longer
reaches the core at all.

  evidence  **145 of 145 adjacent-ℓ pairs correct, ZERO inverted.** *Register 770's single inversion was a PARSING fault — Si III's two
            captures read as separate cores — and dissolved when they were merged
            into one series set (register 772).*
            Li II 0.18 → 0.05 → 0.002 → 0.0003 across s, p, d, f
            Ne I  1.29 → 0.84 → 0.015
            Ne II 0.93 → 0.62 → 0.07 → 0.006 → 0.000 across s, p, d, f, g
                  (f corrected at register 722: the three-member run gave −0.046
                   with spread 0.079; restoring the 5f member gives +0.010 with
                   spread 0.0002 — the negative sign was P.trunc, not physics)
  grade     MEASURED
  source    registers 693, 702, 713, 714
  depends   P.qdt
  falsify   one clean inversion at a defect large enough to measure

---

## P.iso — the isoelectronic ladder

**For a given element and ℓ, the defect falls as the core charge rises.** A tighter
potential holds the outer electron further out, so it penetrates less.

  evidence  **across the table, where the defect exceeds 0.3: 15 of 15 fall.**
            **along ISOELECTRONIC sequences, where the core is held fixed: 8 of 9
            s and p ladders exact** — 12e⁻ Mg I 1.5967 → Al II 1.2369 → Si III 1.0415;
            11e⁻ Na I 1.3506 → Mg II 1.0777 → Al III 0.9049; 10e⁻ Ne I 1.3074 →
            Na II 1.0326 → Mg III 0.8560. *The one failure, 2e⁻ p, is a SIGN CHANGE:
            He I's −0.0133 is register 694's exchange, and P.iso says nothing about sign.*
            Li across THREE stages and six ℓ values, falling at every one
            Mg s/p/d · Na s · Zn p/d · Ne s/p
            **below 0.3: 10 of 20, which is chance**
  **A FUNCTIONAL FORM (registers 932-935).** P.iso was an ordering until a ten-rung
  extrapolation tested it. **delta(c) = a + b*ln(c+1)/c**, fitted on the 12-electron
  ns 1S ladder from charge 1 to 15 with an rms of 0.0065.
      *Mg I 1.5967 → Al II 1.2369 → Si III 1.0415 → P IV 0.9018 → S V 0.8043*
      *predicted Fe XV (charge 15): **0.3877**.  measured: **0.3880 +/- 0.0038**.*
  **A FIT FOR ONE SEQUENCE AT ONE l, NOT A LAW (registers 942-945).** *Isoelectronic
  extrapolation of quantum defects is Edlén's method, Handbuch der Physik 1964; the
  field's standard parameterisations are screening-based (Z − σ), not logarithmic.*
  **And the form does not generalise**: leave-one-out gives 12-electron ns 1.9–2.0%
  of range, np 9–11%, **nd and nf 47–65%, and every helium-like ladder 14–62%**.

  **The predictions were nonetheless real (registers 937-940).**
  *INTERIOR: Ca IX predicted 0.5557 / measured 0.5385; Ti XI predicted 0.4849 /
  measured 0.4738 — and at n = 4 alone, 0.0071 and 0.0041.*
  *The ³S ladder, NEVER fitted for prediction, fitted on charges 1-5 and tested at
  9, 11, 15, 17, 19: mean error **0.0059** across a defect falling 1.660 → 0.347,
  which is **0.4% of the range**, with the charge-15 point agreeing to 0.0001.*
  **The evidence is stability and interpolation, not one distant hit**: refitting
  with Fe XV included moves the prediction at charge 25 by 0.0002, while the
  alternatives move by 0.04 to 0.13.

  grade     MEASURED
  source    registers 708, 716, 717, 718, 932-936
  depends   P.qdt
  falsify   a fall→rise reversal at a defect above 0.3

---

## P.dcollapse — the d-collapse competes with the ladder

**As charge rises the d orbital CONTRACTS, so it penetrates MORE — the opposite of P.iso.**
Two mechanisms act against each other; where the defect is large P.iso dominates, where it
is small P.dcollapse can win.

  evidence  **all ten apparent P.iso exceptions are d, all small, all in this direction:**
            Ne d 0.014 → 0.071 · Na d 0.014 → 0.053 · Si d 0.035 → 0.229
  **generalised (registers 734–736): an orbital collapses at the onset of the shell it
  belongs to, and while collapsing it LEAVES the Rydberg series.** 3d collapses across the
  first transition row; **4f collapses across the lanthanides and barium sits at its onset**
  — Ba III's 4f gives δ ≈ 1.0 against neon's f at 0.006, and disagrees with 5f by 0.15
  where a Rydberg pair agrees to 0.001. *The signature is identical in both cases: the
  lowest member disagrees with the rest and its defect is anomalously large.* **The
  two-member gate rejects exactly these without being told anything about shell filling.**

  *And P.lcollapse survives it: Ba III still runs nd 2.13 → nf 0.95 → ng 0.030. Collapse
  changes the SIZE of a defect, not its order.*

  grade     MEASURED
  source    registers 719, 734, 735, 736
  depends   P.iso
  falsify   an s or p exception to P.iso, which this cannot explain

---

## P.polar — beyond ℓ = 3 the defect measures core POLARISABILITY, not penetration

**At ℓ ≥ 4 the orbital never reaches the core, so penetration cannot be what is measured.
What remains is the dipole the outer electron induces in the core, felt from outside.**

  evidence  **the non-penetrating defect grows with Z: Li −0.0036 · Ne +0.0009 ·
            Ar +0.0062 · Sc +0.0073 · Ba +0.0301 · Bi +0.0381 — slope +0.0005 per
            unit Z across seven elements.**
            **and it falls fast with ℓ within one element**, as an induced dipole must:
            Ar g 0.0062 → h 0.0019 → i 0.0010
            Li g −0.0036 → h −0.0041 → i −0.0048 → k −0.0082 (a two-electron core has
            almost nothing to polarise; the residual is register 679's reduced-mass
            and QED correction)
  **PRECEDENT (register 788): this is Freeman & Kleppner, Phys. Rev. A 14, 1614 (1976)** —
  "polarization of the core electrons by the valence electron is shown to be the dominant
  contribution to the quantum defect." *Nothing here is first. Zn+ was measured at
  18.33 ± 0.95 a0^3 from the same 4snf series this compendium holds; caesium has been
  measured to l = 8, beyond our l = 7.*

  **INCONCLUSIVE on magnitude (registers 792–795).** *An attempt to fit alpha_d and alpha_q
  from the l >= 4 defects did not work: three of nine many-electron cores gave positive
  values — Al III 7.2, Ar II 68.8, Mg II 3.4 a0^3 — all roughly ten times published, and
  six gave negative.* **Whether the fault is the implementation or the data is not
  diagnosed.**

  *Register 791 read this failure as proof of a noise floor and was WITHDRAWN: the
  compendium's own channels give |delta| over spread of s 68.7 · p 29.7 · d 5.9 · f 5.6 ·
  g 9.7 · h 21.0 · i 3.7 · k 5.9 — every l exceeds its own scatter. And the fit had been
  run on BARE NUCLEI, which have no core to polarise; Li III's -1096.7 is a category
  error in the test, not a finding about the data.*

  grade     MEASURED (direction only)
  source    registers 731, 732, 733, 788, 789, 790, 791
  depends   P.lcollapse
  falsify   a heavy element with a smaller high-ℓ defect than a light one at the same ℓ

    **P.qdt measures how far an orbital reaches INTO the core and dies by ℓ = 3.
    P.polar measures how much the core deforms when an orbital passes OUTSIDE
    it, and it is all that survives beyond ℓ = 3.**

---

## P.selfsame — one series measured in disjoint n windows gives one defect

**A Rydberg series is the same object at every n. Splitting it into two windows with no
member in common and computing each separately must give the same defect — and does.**

  evidence  **67 of 72 channels agree between disjoint halves to better than 0.05
            (register 811)** — Be III, Be IV, B III and Li II to 0.0001–0.0005.
            *The two failures span a wide n-range, which register 751 predicted.*
            Si I ns (1/2,1/2)* J=1: +1.8758 over n = 6–10, +1.8763 over n = 13–21 —
            agreement 0.0005, no overlapping member.
            J=0: +1.8930 against +1.8872 (0.006)
            nd J=1: +0.0524 over 14–22 against +0.0716 over 30–44
  grade     MEASURED
  source    registers 747, 748
  depends   P.qdt
  falsify   a defect that drifts systematically with n in an unperturbed series

    **This is stronger than ℓ-ordering or J-consistency. Those compare DIFFERENT
    series and ask whether they stand in the right relation; this compares one
    series to ITSELF across a gap and asks whether it is the same object at both
    ends. A defect that drifted with n would mean the Rydberg formula is the
    wrong model.**

---

## P.lens — near the limit the defect is measured through a worsening lens

**delta depends on (limit - E), which shrinks as n^2 while the level's measurement error
does not. The fractional error therefore grows as n^3, and a long series is precise at the
bottom and blind at the top.**

  **WEAKENED at scale (register 827).** *Tested on 79 channels: only **44 have a wider
  spread in their high half — 56%, interval 45–66%**, barely above chance. Where the span
  is long enough for the n³ growth to show, the predicted ratio is 4.2 and the **observed
  median is 1.3**.* **The direction is real; the magnitude is an order of magnitude smaller
  than the mechanism states.**

  evidence  **Si I nd, one series: a 0.05 cm-1 shift moves delta by 0.0018 at n = 20 and
            by 0.0193 at n = 44 — eleven-fold amplification.** The observed drift across
            that series is 0.019, which is the whole amplification.
            *Three alternatives were tested and failed: a wrong limit (the series fits
            65,747.71 ± 0.12 against a published 65,747.76 ± 0.25), the Ritz second term
            (improvement 1.0x, wrong magnitude), and quotation precision (the 2-decimal
            levels scatter MORE than the 1-decimal ones).*
  grade     MEASURED
  source    registers 749, 750, 751
  depends   P.qdt
  **confirmed on one series at both ends (register 752):** Si I nd (3/2,5/2) J=3 gives
  **+0.0615 ± 0.0021 over n = 8–13** against +0.0570 ± 0.0366 over n = 20–56 — *identical
  series, spread seventeen times smaller at the low end, defects agreeing to 0.005.*

    **This INVERTS part of P.trunc.** Truncating a series at low n removes channels
    and widens what remains — that stands. But EXTENDING one upward past where the
    lens closes does not improve it: a six-member run at n = 8–13 beats a
    thirty-seven-member run at n = 20–56. *Length helps until the lens closes.*

  falsify   a long series whose spread does not grow toward the limit

    **This QUALIFIES P.selfsame rather than refuting it.** Register 747's windows
    agreed to 0.0005 because both sat at low n where the lens is sharp. Two windows
    can only be compared where the amplification is comparable across them, and
    that condition belongs with the check.

---

## P.coreblind — the defect does not depend on the parent term

**A defect belongs to ℓ and the core's charge — not to which state the core is in.**

  **CONTRADICTED IN PRINCIPLE by MQDT (register 947).** The standard framework defines
  the defect as **mu_{l,lambda,alpha+}**, depending explicitly on the internal quantum
  state alpha+ of the ionic core, and its whole apparatus exists because different core
  states give different channels with different defects. *Ne II's agreement across
  26,000 cm-1 and Si I's across 287 are real; a general principle they are not.*

  **TWO instances. Register 815's seven were WITHDRAWN at register 845** — they compared
  duplicate rows under two notations, not two parent cores. *Ar II's `(³P)ns ⁴P J=5/2`
  and `3s2.3p4.(3P).ns 4P J=5/2` are one series from two captures.*
            **Ne II's two parent cores converge 26,000 cm⁻¹ apart — ³P at 330,388.6 and
            ¹D at 356,229.3 — and give the same defect: ns 0.86–0.99 against 0.9849,
            nd 0.055–0.081 against 0.0700.**
  grade     MEASURED
  source    registers 709, 710
  depends   P.qdt
  falsify   two cores of one ion giving different defects at the same ℓ

---

## P.jj — J-inconsistency marks where LS coupling fails

**A defect should not depend on J. Where it does, the coupling scheme has changed.**

  evidence  **114 of 129 J-pairs consistent within 0.05 — interval 82–93% (register 818).**
            *Tested on the RAW LEVELS with J left free, which doubles the sample over
            testing built channels.* **And the failures concentrate as the mechanism
            requires: heavy elements (Z > 47) fail at 23%, light at 8%** — Ba III four
            times, Bi II twice, Bi III once. *The earlier figure was 52 of 65 — and **30 further pairs are EXCLUDED as trivial**: where
            the compilation prints one level for both J, the two defects are identical
            and the pair cannot fail, so it tests nothing (register 775) — heavy or strongly split systems where jj coupling has
            displaced LS. *Bi III np ²P° splits 3.7096 against 3.6044: a real 0.105
            separation at Z = 83.*
  grade     MEASURED
  source    register 703
  depends   P.qdt
  falsify   J-inconsistency in a LIGHT, weakly-split system

---

## P.perturb — a large spread is a perturbed series, not bad data

**Where a state of the same symmetry cuts through a Rydberg run, the series' defect
scatters. The scatter is a measurement of the perturbation.**

  evidence  Al I 3s².nd ²D, 32 members, spread 0.6297 — the 3s3p² ²D perturber
            Li I np, 41 members, spread 0.6779
            against Zn I np, 28 members, spread 0.0033, unperturbed
  **and the perturber can be NAMED from the source (register 741).** Si I's nd channels
  give 1P* spread 0.0044 (clean) against 1D* 0.177, 1F* 0.151, 3F* J=4 0.213 — and ASD's
  leading-percentage column reads **`3s2.3p.3d 3D* — 80 3p.nd : 14 3s.3p3 3D*`**: the
  3s3p3 configuration mixing 14% into the series. *`channels.py` never reads that column.*

  grade     MEASURED
  source    registers 696, 704, 741, 742
  depends   P.qdt
  falsify   a perturbed series with a small spread, or the reverse

---

## P.converge — a Rydberg series measures its own limit

**A series with enough members determines the ionisation limit it converges to, to within
the published uncertainty.**

  evidence  **Ba III's limit fitted at 289,118 from 11 and 10 members; ASD publishes
            289,100 ± 20. Eighteen apart, INSIDE the error bar.** The fine structure
            closes three ways: 17,550 published, 17,566 derived, 17,549.5 measured.
  grade     MEASURED
  source    registers 684, 685, 686, 698, 699
  depends   P.qdt
  falsify   a long clean series whose fitted limit misses the published one

---

## P.trunc — truncation removes channels and degrades those it leaves

**Cutting a series at low n removes most channels rather than a proportional share, AND
widens the defect of the ones that survive.**

  evidence  Ne I: 33 Handbook levels → **0 channels**; the full ASD table → 4
            Si II: truncated → 4 channels of 3 members; full → 9 of up to 8
            Ba III: three-member runs spread 0.07–0.10; ten- and fifteen-member runs
            spread **0.014–0.027 on the same series**
  grade     MEASURED
  source    registers 675, 676, 677, 705, 706
  depends   —
  falsify   a short series whose defect matches its long-run value as tightly

---

## P.buildlimit — a limit can be constructed from two spectra and tested by convergence

**Where a series converges on a state above its own ionisation threshold, no published
limit exists; it is the sum of two numbers from two different spectra, and the series'
convergence is the test that the sum is right.**

  evidence  **Ne I's 2s.2p⁶.np converges on 173,929.75 + 217,047.598 = 390,977.35,
            and gives δ = +0.8408 with spread 0.0191 over ten members** — landing between
            ns 1.29 and nd 0.015 as P.lcollapse requires.
  grade     MEASURED
  source    registers 711, 712
  depends   P.converge, P.lcollapse
  **STILL AT ONE INSTANCE (register 816), and it cannot be strengthened on data in hand.**
  *The mechanism needs a series converging on a state ABOVE its own ionisation threshold.
  Ar II and Ba IV hold single 3s.3p6 and 5s.5p6 levels but no Rydberg run on them.*
  **The capture that would test it: Ar I's 3s.3p6.np series, the exact analogue of Ne I's.**

  falsify   a constructed limit whose series fails to converge on it

---

## P.jsplit — the defect splits by the outer electron's j when there is something to couple to

**Not by the defect's size. The split measures whether the electron's spin has a partner:
either an OPEN-SHELL core carrying angular momentum of its own, or a nuclear charge large
enough that the electron's own spin-orbit matters.**

  evidence  **29 j-split pairs across ten species, separating by a factor of 227 in the
            medians:**
              open-shell or heavy : median **0.0454**  (19 pairs)
              closed-shell, light : median **0.0002**  (10 pairs)
            **the two causes are independent** — open cores give 0.036 at Z = 10–18,
            while a CLOSED core at Z = 83 gives 0.052
              splits   Ne II 2p⁴ ³P · Ar II 3p⁴ ³P · Si I 3s².3p ²P° · Bi I · Bi III
              does not Li I · Li III · C II 2s² · Mg II 2p⁶ · Sc III 3p⁶ · Si II 3s²
  grade     MEASURED
  source    registers 754, 756, 757, 758, 759
  depends   P.qdt
  falsify   a closed-shell light species with a split above 0.01, or an open-shell one below

    **Registers 754–756 filed this as an open question because no ratio to the
    defect survived the data. That was the clue: the two quantities are not
    related, so no ratio between them could be.** *Si I splits by 0.13 on a
    defect of 0.07 because its core is open; Bi III splits by 0.105 on a defect
    of 3.0 because Z = 83.*

---

## P.termsplit — at ℓ = 3 the defect splits by the core's TERM while J-pairs stay together

**Distinct from P.jsplit. There the outer electron's own j does the splitting; here the
core's angular arrangement does, and the electron's J-pairs land on top of each other.**

  evidence  **12 of 15 groups across the compendium have terms separating by more than
            their J-pairs do — 80%, interval 55–93% (register 826). Median within-term
            spread 0.0011 against between-term 0.0462, a factor of forty-two.**
            **Si I nf on the ²P°₃/₂ core, eight four-member series:**
              2[3/2] −0.0006 · 2[9/2] +0.017 · 2[5/2] +0.028 · 2[7/2] +0.047
            **each J-pair agrees to 0.001 while different terms separate by up to 0.048**
  grade     MEASURED
  source    register 739
  depends   P.qdt
  falsify   a term-split with J-pairs that scatter as widely as the terms do

    *At ℓ = 3 the electron is far enough out that what it feels is the core's
    angular arrangement rather than its charge distribution.*

---

## P.mono — the defect approaches δ₀ monotonically; PENETRATION falls, POLARISATION rises

**§25.6.1 rests on this. It is a strong tendency, not a law, and the ceiling on
establishing it is UNCERTAINTIES rather than sample size.**

  evidence  **TWO CLAIMS, not one (registers 985–987).** Banded by the size of the
            defect being tested, on resolved steps:
              **penetration, |δ| ≥ 0.1 : δ FALLS — 146 of 163, 90%, interval 84–93%**
              **polarisation, |δ| < 0.01: δ RISES —  52 of 52, 100%, interval 93–100%**
            **Combined 198 of 215 — 92%. As the single claim "δ falls": 66%.**
            *NIST's own compendium gives the reason: "the value of a is usually positive
            for core-penetration series and NEGATIVE for core-polarization series", where
            a is the Ritz δ₂ — and δ₂ < 0 makes the defect rise toward δ₀.*
            The earlier figure of **113 of 130 resolved steps falling — 87%** (register 821),
            on the five species carrying quoted uncertainties, restricted to steps
            exceeding their own error threefold.
            **The same test with error from quoted DECIMALS gives 55%, interval 51–58%
            — the intervals do not overlap** (register 822). Quotation understates the
            real error near a limit, and the cost is an 89% result driven to chance.
  grade     MEASURED (tendency)
  source    registers 802, 806, 821, 822, 823, 824
  depends   P.qdt
  falsify   a resolvable step in an unperturbed series rising by more than its error

    **RESOLVED by the literature (register 858).** The extended Ritz expansion
    **delta(n) = delta_0 + delta_2/(n-delta_0)^2 + delta_4/(n-delta_0)^4 + ...** is
    standard, and caesium's nF series is measured with **delta_2 = -0.2014(16),
    NEGATIVE, and its defects RISE with n** (0.03331591 at n=45 to 0.03333469 at
    n=50). *So the law is not "delta falls" but "delta approaches delta_0
    monotonically", and the direction is sign(delta_2) — a property of the channel.*
    **The 13% rising were never anomalies; the statement being tested was wrong.**

---

## P.charge — at s and p the defect falls with charge at fixed ELEMENT

**Not P.iso. That fixes the electron count; this fixes the element, and the two are
different relations on different axes of the index.**

  evidence  **37 of 37 monotone at l <= 1, no exceptions** (register 963) — He, Li, Be,
            B, C, Ne, Na, Mg, Al, Si, Ca, Zn, Bi, every element in the compendium with
            two or more charge states.
            *Li: LiI +0.405 → LiII +0.128 → LiIII +0.000 at s, and +0.078 → +0.037 →
            +0.000 at p. Bi: BiI +4.904 → BiII +4.369 → BiIII +3.987.*
  grade     MEASURED
  source    register 963
  depends   P.qdt
  falsify   an s or p defect that RISES with charge at fixed element

    **All nine failures are at l >= 2**, where P.dcollapse governs and d defects are
    already known to rise. The axis is applied only at s and p for that reason.

    **What it is for.** It is the third propagation axis in the index, and the one that
    reaches spectra isolated from every isoelectronic neighbour: Ne III, IV and V have no
    sequence partner measured, but sit on the same element as Ne I and Ne II. With it,
    and with register 964's fix to sparse-alphabet stepping, the index went from 747
    cells carrying no statement to **55**.

---

## Note on entry

**These are PHYSICAL mechanisms, and the mathematics register has held mathematical
objects.** Whether they enter as a new family `P.*` or as an appendix to the Spectra
Compendium is a decision for when the spectra work closes — but the evidence and the
falsifiers are recorded now, while they are fresh, rather than reconstructed later.

*Register 720.*
