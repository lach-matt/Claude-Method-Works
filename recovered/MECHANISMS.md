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

  evidence  **103 adjacent-ℓ pairs across the compendium, ZERO inverted.**
            Li II 0.18 → 0.05 → 0.002 → 0.0003 across s, p, d, f
            Ne I  1.29 → 0.84 → 0.015
            Ne II 0.93 → 0.62 → 0.07 → 0 (f smaller than its own spread)
  grade     MEASURED
  source    registers 693, 702, 713, 714
  depends   P.qdt
  falsify   one clean inversion at a defect large enough to measure

---

## P.iso — the isoelectronic ladder

**For a given element and ℓ, the defect falls as the core charge rises.** A tighter
potential holds the outer electron further out, so it penetrates less.

  evidence  **where the defect exceeds 0.3: 15 of 15 fall, no exceptions.**
            Li across THREE stages and six ℓ values, falling at every one
            Mg s/p/d · Na s · Zn p/d · Ne s/p
            **below 0.3: 10 of 20, which is chance**
  grade     MEASURED
  source    registers 708, 716, 717, 718
  depends   P.qdt
  falsify   a fall→rise reversal at a defect above 0.3

---

## P.dcollapse — the d-collapse competes with the ladder

**As charge rises the d orbital CONTRACTS, so it penetrates MORE — the opposite of P.iso.**
Two mechanisms act against each other; where the defect is large P.iso dominates, where it
is small P.dcollapse can win.

  evidence  **all ten apparent P.iso exceptions are d, all small, all in this direction:**
            Ne d 0.014 → 0.071 · Na d 0.014 → 0.053 · Si d 0.035 → 0.229
  grade     MEASURED
  source    register 719
  depends   P.iso
  falsify   an s or p exception to P.iso, which this cannot explain

---

## P.coreblind — the defect does not depend on the parent term

**A defect belongs to ℓ and the core's charge — not to which state the core is in.**

  evidence  **Ne II's two parent cores converge 26,000 cm⁻¹ apart — ³P at 330,388.6 and
            ¹D at 356,229.3 — and give the same defect: ns 0.86–0.99 against 0.9849,
            nd 0.055–0.081 against 0.0700.**
  grade     MEASURED
  source    registers 709, 710
  depends   P.qdt
  falsify   two cores of one ion giving different defects at the same ℓ

---

## P.jj — J-inconsistency marks where LS coupling fails

**A defect should not depend on J. Where it does, the coupling scheme has changed.**

  evidence  **32 of 38 series consistent within 0.05. The failures are Bi II, Bi III,
            Ba III, Ar II** — heavy or strongly split systems where jj coupling has
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
  grade     MEASURED
  source    registers 696, 704
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
  falsify   a constructed limit whose series fails to converge on it

---

## Note on entry

**These are PHYSICAL mechanisms, and the mathematics register has held mathematical
objects.** Whether they enter as a new family `P.*` or as an appendix to the Spectra
Compendium is a decision for when the spectra work closes — but the evidence and the
falsifiers are recorded now, while they are fresh, rather than reconstructed later.

*Register 720.*
