# B4d stage 4: the opening's null shell, on the plane (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage4.py`, selftest 4/4.

> **Under item 163 (2026-10-08): conditional on a withdrawn reading.** This shell is the opening as an instant step from
> our universe into eq. (17). Item 163 sets the instant aside, so this computes one model of the opening's leading
> edge, not the live corridor. D1–D3 stand as computations (a positive energy with a tension, which on the plane reads as
> an NEC break and under clause (B) as the bulk's Weyl jump). The live question is stage 5's. The verifier is deferred.

## The question

- **The setup.** Under your 162 the corridor takes its size at once, so it opens across a null shell.
- **The question.** What does that shell carry? On the plane, it joins our universe (flat, your 157) to the corridor's
  eq. (17).

## D1. The shell, computed

**The formula used** (Poisson, gr-qc/0207101, p.9, eqs. (5.12)–(5.14), READ).
- **Energy density:** μ = [m]/(4πr²).
- **Pressure:** p = [∂ψ/∂r]/(8π).
- These are for an ingoing shell, with the generators parameterized by λ = −r on both sides.

**What it gives:**

| quantity | result |
|---|---|
| mass function m₊ | m·(5/2 − 4x)/(2(1 − 3x/2)), with x = m/r: **m at the throat, 5m/4 far out** (E4's total) |
| energy density μ = m₊/(4πr²) | **positive** for every r > 2m |
| pressure p = −m/(16π(r − 2m)(2r − 3m)) | **negative** for every r > 2m: a tension, diverging at the throat |

**Control.** A shell from flat space into Schwarzschild gives Poisson's own μ = M/(4πr²) and p = 0 (eq. (5.6)),
exactly.

## D2. Read as matter on the plane, the tension breaks the null condition (deduced)

- **The test.** Take a future null vector n = a·k + b·N + c·e. Then S(n,n) = μb² + 2pab. With p < 0 this is negative
  once a is large enough.
- **So** the shell, read as 4D matter, breaks the null energy condition, just as eq. (17) itself does on the plane
  (opening.py O3).

## D3. Under your rulings it is not matter (deduced)

- **Why not.** Clause (B) says the plane carries no matter. So this 4D shell is the bulk's Weyl field jumping across
  the null cone, read on the plane. That is how E4 reads eq. (17)'s own deficit: as the bulk's pull, not matter.
- **What your 117/120 make of it.** That is the kind of break your 117/120 call an appearance: *"the NEC only ever
  appears to break, but never does"*.
- **The real test is in five dimensions (stage 5).** The null shell in the bulk sits across the cone's boundary, between
  eq. (17)'s static bulk and the bulk as it was before. It must carry non-negative energy in the five-dimensional sense.

## Caution for the verifier

- **The tension's sign may depend on a choice.** The pressure depends on how the shell's generators are parameterized.
  Poisson's section IV says the surface quantities transform under reparameterization.
- **Why it matters here.** The divergence at the throat comes from eq. (17)'s extremal horizon: F has a single zero
  there and H a double one, so e^ψ diverges.
- **The open check.** Whether the sign of p, and so D2, survives a reparameterization is not yet checked.

## Named hypotheses

- **Yours:** 117/120, 157, 162; clause (B).
- **The board's:**
  - reading the 4D shell as the bulk's Weyl field (D3), as E4 reads eq. (17);
  - the opening as one null shell (B4D-STAGE3.md).
