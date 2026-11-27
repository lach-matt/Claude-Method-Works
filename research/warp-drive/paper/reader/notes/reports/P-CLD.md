# P-CLD report: lem:class-leaf-differences (chapter 81), full proof

File: research/warp-drive/paper/reader/proofs/P-CLD.md, 706 lines, md5 7f6e5177553ef28e6a48a286fd6827bc.
Uncommitted. No other repository file was edited. Old texts are quoted from HEAD edafc288, and chapters 81 and 83 are
unchanged since 29d76871.

## What the file proves
- Definitions paragraph. Charts are general, as in sec:loc-axis-leaves. The radius r_* ≤ ρ1(p)/4 is a parameter. A state
  carries W_U = (g, ∂g, p_A, Θ_A), C¹ on the slice. Bounds (M, c) are the C¹ norms of W_U plus lower bounds for g on TΣ,
  for −g⁻¹(dτ,dτ) and for |p_A(∂_z)| on the axis. H_L[U] is Tier 3's reading (p_A(n), the sign of p_A(∂_z), and Π the
  γ3-orthogonal complement of p_A^Σ). Leaves, σ[U] and arcs are defined here.
- NEW lem:class-leaf-states (The leaves of a state). Constants depend on (M, c), ρ1(p) and r_* only.
  - (a) Foliation. The difference quotients in the axis point lie in [1/2, 3/2], and |Δh′| ≤ C r|Δz0|. Smooth states
    give smooth leaves, smooth in parameters, and z0[U] is smooth. |σ| ≤ C.
  - (b) A pointwise bound along one arc.
  - (c) An L² bound on any set closed under the arcs of the first state, with a constant independent of the set and
    of δ.
  - Only C² of g is needed. By invariance C3 = ∂_(y2)γ3(∂_z, ∂_(y2)), a first derivative of g at the point.
    eq:class-leaf-g gives G = r(…) − q(C3 r + γ_zz q)²/det₂, hence |∂_z G| ≤ C(r + |q|).
- lem:class-leaf-differences, restated with the same label and title. ů is any smooth state (a solution being one case).
  Balls are local: 𝒩_m is the sum of the L² norms of ∂^j(W_U − W_ů) on Σ∩𝒰, at most twice eq:class-energy for solutions.
  The bounds hold for every δ ≤ δ_0 with fixed balls.
  - (a) ‖∂^α(σ[U]² − σ[ů]²)‖ ≤ C𝒩_k for |α| ≤ k. This holds for states (x-derivatives) and for families or solutions
    (spacetime derivatives at each time). For m > k, ‖σ[U]² − σ[ů]²‖_(H^m) ≤ C_m 𝒩_m, with C_m depending on 𝒩_(m−1).
  - (b) The L² Lipschitz bound and |σ| ≤ C on 𝔅′. This is lem:class-leaf-states (c) with D the slice.
  - (c) The leaves: Σ_(j≤2) ‖∂_(z0)^j δh‖_(L²(I;H^(k+2−j))) ≤ C𝒩_k, which is what def:class-adapted uses. For families,
    the derivatives of order ≤ k−2 are bounded pointwise.
  - Last statement: the leaves are the level sets of u_A. The proof is written out.
- The proof of (a) and (c) has seven steps:
  - Smooth states suffice, by density together with (b).
  - Leaf coordinates (z0, y), with the comparison of H^m norms on 𝒰_δ and in (z, y) (weight 2πz, Jacobian in [1/2, 3/2]).
  - The divergence form, 𝔙 = y𝔰 with 𝔰 the Hardy average of Φ, ∂_y h = 𝔓(y, h, y𝔰), and σ² = 2|χ̸ − ½(tr χ̸)γ̸|² in
    Cartesian form.
  - Low-order sup bounds, and rules (P) for products and (Q) for composition.
  - Transverse derivatives (z0, τ) from the radial Volterra form in s = h′/r, with η = r² ∫ θ δs(θr) dθ. This is the
    zero-order bound and the shift.
  - Derivatives along the disc, from the flat Laplacian of the radial potential u_X (lem:class-interior-regularity with
    L = Δ only).
  - Back to (z, y) through Λ_U⁻¹.
- Cited and checked: lem:class-volterra (its proof uses only G(0) and the bounds eq:class-leaf-g-bounds),
  lem:class-leaf (b), (c), lem:class-gauss (b), (c), step (1) of lem:class-planar-shear, lem:class-interior-regularity,
  eq:class-leaf-volterra, eq:class-shear-leaf, prop:class-flat-model (b), thm:std-bh-embedding, thm:std-bh17-embedding
  and thm:std-sy-extension. eq:class-leaf-cartesian and lem:sobolev are not used: lem:sobolev is stated for the annuli
  A(τ), so Sobolev's embedding is applied directly on Σ∩𝒰.

## Changes from the reader's replacement text (R-P-CIVP4 Major 5)
Kept: the zero-order bound and the shift by the radial form, the integration over the axis points, and (b) from the
leaf-by-leaf bound. Changed:
1. The radial form is used for every transverse derivative, not only for order zero. The reader's |δh| ≤ C r‖F‖ covers
   order zero only. In the Cartesian form, η = ∫_0^1 ∂_y η(ty)·y dt is not bounded in L² by ∂_y η (a logarithmic loss).
2. The leaf-by-leaf bound needs C² of g, not C³ (see above). This also settles the reasoning of minor 2 for Tier 4.
3. The old elliptic step is replaced. It absorbed the quadratic terms across shrinking discs, which fails, and its
   coefficients carry U's leaf. The replacement is the divergence form plus the flat Laplacian.
4. STATEMENT CHANGE, FOR DECISION: (a) bounds σ² rather than σ − σ̊.
   - An H^k bound for σ itself needs a loss-free H^m bound for the coefficient α = T(K2,K2)/|y|² of a G-invariant tensor
     αδ + β y⊗y. σ contains α of K_Σ and of ∂γ3, through K_Σ(e2,e2) and ν(log B3).
   - Pointwise |α| ≤ |T| holds. In H^m the provable bound loses one derivative (α = tr T − 𝒜(div(T y))). A loss-free
     bound needs Rellich-type inequalities for angular mode 2, which the paper does not contain.
   - Every use of (a) goes through σ², the closure −½σ²: Steps 6, 9 and Smoothness of thm:class-stability,
     lem:loc-axis-system (a), Tier 4's corner proof and lem:class-leaf-reference (a).
   - The old step (5) of lem:class-planar-shear relies on the same unproved bound. That is outside this file and is
     reported here.
5. Higher orders: C_m depends on 𝒩_(m−1). Placement 6 rewrites thm:class-stability *Smoothness* to work by induction on
   σ, and that argument is sound.

## Placement (8 replacements; each old text was checked to occur exactly once as whole lines at HEAD)
- Item 1: 81:1324–1357 (lem:class-leaf-differences) is replaced by the block. Tier 3's item 8 clause is carried in.
- Items 2–4: lem:class-leaf-reference (Tier 4, merged).
  - 1373–1374: H_L now refers to the new definitions.
  - 1388–1391: δ_V := min(δ_0, r_V/8, δ_𝔐), and the dependence is corrected.
  - 1449–1480: its proof of (a) and (b), whose steps (i)–(vii) were "changes to the proof of lem:class-leaf-differences
    (a)" and no longer match, becomes "lem:class-leaf-differences with ů := V".
  - These items are needed together with item 1. Its (o) and (b′) keep their own proofs.
- Item 5: def:class-adapted 1590–1591 and 1605–1606 now cite lem:class-leaf-differences (c).
- Item 6: thm:class-stability *Smoothness* 1745–1757, as in change 5.
- Item 7: chapter 83, lem:loc-axis-system (a), 2933–2934, worded for (a) on σ².
- Crosswalk: 16 new rows (lem:class-leaf-states and 15 eq: labels), each pinned P-CLD.md@PENDING:N to its label line
  (all verified). Changed rows: lem:class-leaf-differences, lem:class-leaf-reference, def:class-adapted,
  thm:class-stability and lem:loc-axis-system.

## How each later tier uses it
- Tier 3 (merged): its item 8 is absorbed and no statement changes. lem:loc-axis-shear is lem:class-leaf-states (c)
  with D := Ō. Its uses of 𝔅, 𝔅′, δ and the last statement are served. lem:loc-axis-system (a) needs item 7.
- Tier 4 (merged as lem:class-leaf-reference):
  - (o) and (b′) are also lem:class-leaf-states (a) and (c). (c) is stronger: it takes an arc hypothesis and C² of g.
  - (a) and (b) follow at once, with δ ≤ δ_V and fixed balls as ch83 needs.
  - Its uses in ch83 go through σ² or (b): (F1), (F2), Smoothness, uniqueness, and the shells.
  - Outside this file: (o) Step 1 and (b′) bound n, K_Σ and κ_A1 by C² of g without lower bounds for −g⁻¹(dτ,dτ) and
    for g on TΣ. The bounds (M, c) here include them, and item 3 names them.
- Tier 5 (P-CIVP5, under reading): compatible.
  - Its Block A1 goes after lem:class-leaf-reference; the labels do not collide.
  - lem:class-leaf-arc (a)–(c) equals lem:class-leaf-states (a)–(c) with the two states swapped, so it can be cited
    instead.
  - lem:class-leaf-tame step (6): bounding D^α η for transverse α by (H) fails, because the weight s⁻¹ gives a
    logarithmic loss. Step 5 here (the radial form in s) repairs it.
  - Its σ = 𝔖(…, 𝒜Φ) meets the coefficient issue of change 4. Stated for σ², it holds.
  - Its 𝔤-variant (∂g replaced by a free field) is not covered by the divergence-form part here, which uses true
    derivatives of γ3.
  - Its text still says "H_L[Θ_A] of lem:class-leaf-differences". After item 1 this should read "defined before
    lem:class-leaf-states". This is a harmless pointer.

## Scratch merge (git archive of HEAD edafc288, in scratchpad/reader/scratch/pcld/, items 1–8 applied)
- lint.py --chapters: 62 files, 4944 labels, 0 hits.
- assemble.py --check: labels 4944, problems 0.
- assemble.py: problems 0. The new lemmas are Lemma 51.28 (lem:class-leaf-states) and Lemma 51.29
  (lem:class-leaf-differences); lem:class-leaf-reference becomes 51.31.
- lint.py --paper: 0 hits.
- In the assembled region every line is ≤ 121 characters, with no bad wrapped-line starts. In the file, every line is
  ≤ 121 characters and the only "- " line starts are list items in the non-merged notes.

## Round 2 (the coordinator's two conditions for the σ²-form)
- File: proofs/P-CLD.md is now 797 lines, md5 67d1d46d29bf60540d4414971c6e34f4. The previous version was 706 lines,
  md5 7f6e5177. The delta against HEAD is +100 −9 lines. The block, its labels and the crosswalk pins are unchanged.
- Condition (2): lem:class-planar-shear.
  - New placement item 8 restates its bound (81:1286) for ‖σ²‖_(H^k).
  - The same item proves step (5) (81:1318–1319) from the Cartesian form of χ̸ in the frame X_i = ∂_(y_i) + ∂_i h ∂_z,
    with σ² = 2|χ̸ − ½(tr χ̸)γ̸|² (lem:class-gauss (b)), Moser's estimate, and the sup bounds of step (3).
  - None of the lemma's uses needs the bound for σ itself. They use steps (1), (3) and (4) or its constants: 81:1437,
    1445, 1464, 1659, 1757; 83:503; and 81:1327 and 1356 inside the old text of item 1.
  - New placement item 9 changes the opening paragraph of ch:class-system (81:17–18) to say that the expansion recovers
    the square of the planar shear.
- Condition (1): the file's notes now list every use of lem:class-leaf-differences (a) and every H^k bound of σ in all
  chapter sources at HEAD 9d133b0c (chapters unchanged since 5a238875 and edafc288). Only chapters 81, 82 and 83 contain
  any. Each entry has its line numbers and how it is handled.
  - Uses of (a) all go through σ² or need only (c):
    - 81:1388–1391, 1405, 1449–1474 (lem:class-leaf-reference);
    - 81:1590–1591 and 1605–1606 (def:class-adapted, the leaves, now (c));
    - 81:1675 (Step 6) and 81:1704 (Step 9, (F1));
    - 81:1745–1748 (Smoothness);
    - 82:2198–2199 and 82:2229 (prop:vlasov-uniform-n);
    - 83:2933–2934, 2975, 3697–3698, 3714–3716.
  - H^k bounds of σ itself:
    - 81:18, reworded by item 9;
    - 81:1286 and 1318–1319, restated and proved by item 8;
    - 81:1747, replaced by item 6;
    - 81:1102–1103, flat model only, already proved in prop:class-flat-model (b);
    - 81:1137, qualitative.
  - L² and L^∞ uses are listed as unaffected. Chapter 82's σ2 (82:1802, 1957) is qualitative smoothness with its own
    proof.
  - No H^k bound of σ itself remains.
- Placement now has 9 items (11 replacements). Each old text occurs exactly once at HEAD 9d133b0c (checked by script).
- Scratch merge (git archive of HEAD 9d133b0c, all 11 replacements applied):
  - lint.py --chapters: 62 files, 4944 labels, 0 hits.
  - assemble.py --check: problems 0.
  - assemble.py: problems 0.
  - lint.py --paper: 0 hits.
  - No line in the file is over 121 characters, and there are no bad wrapped-line starts.

## Round 3 (fix round for R-P-CLD: 1 Major, 6 minor, 10 nits)
- File: proofs/P-CLD.md is now 914 lines, md5 39e7fd6766b1158ef60fd11b657cc9b7. It was 67d1d46d (797 lines). The delta
  against HEAD 60527421 is +197 −80 lines.
- Old texts were re-quoted from HEAD; chapters 81, 82 and 83 are unchanged since 9d133b0c.
- Major 1: new Placement 13 for lem:loc-lens-dependence (83:447–450 and 508–509), using the reader's text.
  - The radius r_* := 1/2, a δ ≤ δ_0 uniform over the axis points, finitely many p_i, and χ_Z at the scale δ.
  - 83:509–511 is moved in the use list to a new "Through δ" entry.
- minor 1: the reader's text. Steps 5 and 6 form one induction; R_j's top-order terms are absorbed with r″ (r″ is now
  fixed in Steps 4, 5 and 6); Step 5 holds on Q̂_(j−1).
- minor 2: the norm in eq:class-leaf-compose is restricted to ‖·‖′_(n+1), which leaves out T^(n+1).
- minor 3: Step 2 now also compares norms of the components of tensor fields, through the frame (∂_z, ρ1⁻¹K1, ∂_(x3), ∂_(x4)).
- minor 4: Placement 2 is widened to 81:1371–1376. One definition of *state* remains, and V is smooth up to the closure
  of 𝒰_(r_*).
- minor 5: new Placements 10 and 11 for (o) at 81:1378–1379 and (b′) at 81:1393–1395, with the lower bounds for
  −g⁻¹(dτ,dτ) and for g on TΣ_τ, and with ρ1(p). Placement 4's new text now says "at most twice 𝒩_k^V" and carries the
  same lower bounds.
- minor 6: new Placement 14 for 83:2714–2715: "H_L[V] as defined before lem:class-leaf-states".
- Nits:
  - nit 1: Placement 12 (81:1137).
  - nit 2: Placement 7's wording.
  - nit 3: □_g̊ ů_A.
  - nit 4: the Lipschitz argument is applied to p_A(∂_z) as well.
  - nit 5: the mean value clause.
  - nit 6: 𝔤̂ takes the argument h; the arguments of a_3 are listed.
  - nit 7: the condition a ≤ m − 4.
  - nit 8 (mine): a family is required to have its derivatives of order ≤ k continuous in τ into L² of the slices, which
    the solutions satisfy (C([τ0, τ1]; H^k), τ-derivatives from the equations). The approximations then converge
    uniformly near the time considered, and the bounds pass to the limit.
  - nit 9: the last statement is stated for states with g⁻¹(du_A, du_A) = 0, p_A = du_A, Θ_A = □_g u_A and
    ∂_z u_A ≠ 0, a solution being one case; its proof notes that no field equation is used.
  - nit 10: ρ1(p) is added to the dependence lists of Placement 3 and of (o) and (b′).
- Notes: the Tier 5 note now says that Block A1's second definitions of *state*, *bounds (M, c)* and *arc* do not stand
  (the definitions before lem:class-leaf-states do), and that its H_L pointer must change. The Tier 3 and Tier 4 notes
  and the changed crosswalk rows are updated: lem:class-leaf-reference, ch:class-system, and in chapter 83
  lem:loc-lens-dependence and sec:loc-axis-leaves.
- Placement now has 14 items (17 replacements), each old text exactly once at HEAD.
- Scratch merge (git archive of HEAD 60527421, all 17 replacements applied):
  - lint.py --chapters: 62 files, 5079 labels, 0 hits.
  - assemble.py --check: problems 0.
  - assemble.py: problems 0.
  - lint.py --paper: 0 hits.
  - No assembled line over 121 characters; in the file, no line over 121 and no bad wrapped-line starts.
- The 16 crosswalk pins were re-pinned to the label lines and checked.
