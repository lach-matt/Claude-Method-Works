# P-CIVP2: the characteristic problem without smallness (Tier 2, Route CQ) — report

Proof text: `research/warp-drive/paper/reader/proofs/P-CIVP2.md` (751 lines, section + Placement).
`python3 lint.py proofs/P-CIVP2.md`: no hits other than the `[[pending:…]]` markers and the cross-file labels a
single-file run cannot see; every referenced label is defined in a chapter or in the file. Max line length 121.
Nothing outside the proof file, the scratchpad and this report was written. `assemble.py` was not run.
Tier 1 (`proofs/P-CIVP.md`) did not exist at any point of this work, so its labels appear as pending markers.

## Go/no-go

**G1 — PASS.** For h = −2e^(2α)(du⊗dv + dv⊗du) + e^(2β)(dϑ − b du)², frame e3 = e^(−α)(∂_u + b∂_ϑ), e4 = e^(−α)∂_v,
e1 = e^(−β)∂_ϑ, sympy (scratch `civp2/g1_frame.py`, `g1_verify.py`, `g1_box.py`, `g1_f5.py`) verified with zero
residual, for arbitrary α, β, b: the coefficient formulas (χ = e4β, χ̲ = e3β + e^(−α)∂_ϑb, ϖ = −½e4α, ϖ̲ = −½e3α,
ζ = −¼e^(β−2α)∂_vb, η = ζ + e1α, η̲ = −ζ + e1α, ξ = ξ̲ = 0); the three commutators; the Luk-ordered transports
(F1) e4χ, (F2) e4η, (F3) e3ϖ and their exchanges, whose only curvature is Ric[h] and which contain no angular
derivative of an unknown; the "dropped" equations (F4) e3χ, (F5) e3η and exchanges (these contain e1η, e1ϖ̲); □_h in
two double-null forms; div_h(q h⁻¹dv) = −½e^(−α)(e3q + χ̲q). `g1_dust5.py` verified the 5D link
div_g(q g⁻¹du) = e^(2ψ) div_h(q h⁻¹du). The dust density enters only the two Raychaudhuri equations (M_44, M_33).
All of this is written in the text as derivations (lem:civp-large-frame, connection table, Ricci in the frame).
Note against the scoping report: written with h (not g3) the dust laws carry **no** e^ψ weight.

**G2 — PASS.** The 23-unknown evolution system (eq:civp-large-system: 10 fields transported by ∂_u + b∂_ϑ, 13 by
∂_v; the waves in the first-order form of [CCTW16, (4.47)–(4.50)]) multiplied by e^α has A^u = diag(I₁₀, 0),
A^v = diag(0, I₁₃), A^ϑ = (bI₁₀, Q; Qᵀ, 0) with Q four entries −e^(α−β) (`g2_system.py`: symmetric, (2.8) blocks,
zero ψψ angular block). Coefficients are smooth for all f (log variables α, β), positivity holds for all f. Hypotheses
of Theorem 3.9 checked one by one in Step 2 of the theorem's proof: Y = ℝ/πℤ compact 1-dimensional (n = 2), (2.1) with
Euclidean product and flat connection (compatible, splitting-preserving), (2.7)–(2.8), ℓ ≥ 6 > (n+9)/2, smooth data,
and global solvability of (3.100)–(3.101) (lem:civp-large-data (b)(i): the transports are ODEs reproducing the cone
data by the constraints, plus linear ODEs). Route Q was not needed.

## Route taken

Route CQ with identification by option (ii), adapted: the CCTW Theorem 5.3 continuation in u + v is run with
**null–null corner problems only** (a characteristic rectangle whose two lower edges lie in the known region reaches
past the front {u + v = t*}, also at the ends on the cones), so no Cauchy or mixed problems are needed. Each local
corner development is compared with the strip solution by an energy estimate (lem:civp-large-energy (b)); gluing is by
comparison with the strip solution. Localisation: cut-off ϱ(ϑ) keeping (2.8) exactly (A^u, A^v unchanged), periodised on
ℝ/πℤ, finite speed from lem:civp-large-energy (a) with an explicit trade-off (c1, c2) giving spread ≲ √(uv).
Option (i) (propagating the dropped equations, G3) was examined and not used: the defect system has ungoverned
transverse derivatives (e.g. e4 of the χ̲-defect) and closes only through Bianchi in a mixed wave–transport form.

## Lemma status

- def:civp-large-data, lem:civp-large-frame (G1), lem:civp-large-reduction, prop:civp-large-system (G2),
  lem:civp-large-data, lem:civp-large-energy: **complete**, self-contained.
- thm:civp-large (b) localisation, (c) uniqueness in the gauge (among solutions equal to g0 near the axes), (d) the
  neighbourhood: **complete**, independent of Tier 1.
- thm:civp-large (a) existence/identification: **complete given prop:civp-large-corner**.
- prop:civp-large-corner (developments near a corner sphere, large data, uniform size σ(Λ)): **depends on Tier 1**.
  Its proof is written as "Tier 1's proof with smallness of the data replaced by smallness of the rectangle", naming
  the three steps that change (Cauchy step by thm:class-kato (a) + rem:class-kato-local instead of
  thm:class-kato-stability (a); finite speed with the solution's own cone field; gauge construction near the data's).

## Not closed

1. `[[pending:civp-tier1-local]]`, `[[pending:civp-tier1-theorem]]`: Tier 1 must provide its engine in a form that
   covers prop:civp-large-corner (general corner (u_c, v_c), arbitrary lengths, b = 0 on the in-edge, data equal to
   the background near the axes, size σ depending only on C^m bounds Λ). If Tier 1 proves only small data on fixed
   Q1, this proposition is a gap: it is the only place where existence of a genuine solution enters.
2. `[[pending:civp-tier1-cin-cones]]`: the 𝒞_in analogue of prop:loc-cones; the text assumes Tier 1's gauge is
   b = 0 on 𝒞_in (the definition of cone data imposes it). If Tier 1 fixes another gauge, def:civp-large-data and the
   𝒞_in part of lem:civp-large-data change.
3. Assumed, as in the scoping report's Tier 1: the background exists in the gauge on a neighbourhood of Q1 × S³. Only
   neighbourhoods of the cones are really used (Theorem 3.9 could be applied to the two strips separately); not
   rewritten. Whether Q1 with v1 > 4.5, u1 > 7.2 lies in the background's domain was not checked
   (rem:civp-large-beyond states the dust cases under that condition).
4. δ is not explicit: δ = min(s1, s2) (eq:civp-large-delta) from a*, b* of [CCTW16, Cor. 3.11] (existence only) and
   sup |b|, sup e^(α−β), sup |∂_vb| of the strip solution. No estimate of the solution. Axes (Tier 3), finite
   regularity and measure-valued densities not covered; all stated in rem:civp-large-domain.

## Citations verified

[CCTW16] read twice: alphaXiv full text, and page-located PDF queries of arXiv:1406.3009v2. Pages are arXiv v2 pages
(the appendix's convention): (2.1)–(2.2) p. 6; (2.7)–(2.9) p. 7; bar convention and (3.2) p. 11; Theorem 3.9
pp. 32–33 (statement quoted in the new Appendix entry, including "unique within the class of C¹ solutions, and is
smooth if ϕ̄ and ψ̄ are"); Corollary 3.11 and Remark 3.12 p. 35; (4.47)–(4.56) pp. 47–48; Theorem 5.3 p. 54, proof
pp. 55–56 (t := u + v, t*). **Misprint in [CCTW16]:** (4.48) and (4.50) print ℓ(ϕ0) = ψ0 and ω(ψ0) = ϕ0 (also in
(4.56)); with ϕ0 = ψ0 = h they must read ℓ(ϕ0) = ψ₋ and ω(ψ0) = ϕ₊. The edition does not quote these equations.
Bibliography: the publisher's page (impan.pl, citation metadata) gives **Dissertationes Math. 515 (2016), 1–67**,
DOI 10.4064/dm732-7-2015 (the edition prints "(2016), 1–72"; the author's homepage also lists 1–72). Placement item 8
proposes "515 (2016), 1–67". Crossref/OpenAlex were unreachable through the proxy.

## Placement (in the proof file)

Section goes in chapter 83 after Tier 1's section, before sec:loc-kid. Old/new texts given for: 83 opening (8–9),
83 paragraph after prop:loc-cones (593–600), 90 (line 200), 01 (190–191), 03 "More families" (367); two Appendix A
entries thm:std-cctw-existence and thm:std-cctw-strips in sec:std-characteristic; the [CCTW16] entry. Chapters 80, 81,
82, 87 unchanged. Line numbers are those of 2026-11-20 sources; chapters are being edited concurrently.
