# Handoff: G0r (P-GRD15 on top of P-GRD14). Not started; this note is what the next writer needs.

Scratchpad root: `SP = /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad`.
Report to `SP/reader/reports/G0r.md`, with a copy in `SP/g0r/`. Rules as before:
- nice -n 19, at most two level*.py jobs at once;
- launch from the scratchpad;
- no repository edits, nothing committed;
- do not read method/, drive/, extracted/ or recovered/.

## The task (coordinator)

Evaluate P-GRD15 (sec:tl5-hff, Section 57.30, merged at becf0eb0; confirmed text proofs/P-GRD15.md at 7cad931e, md5
21ef7990) on top of P-GRD14. Both texts are already saved here:
- `SP/g0r/P-GRD15.md` (md5 21ef7990 checked);
- `SP/g0r/ch87_becf0eb0.md`, with sec:tl5-hff from line 7645 to the end.

The changes:
- **lem:tl5-hff-rho, route (𝔯)**, at N ≥ 6 with option (b) only. The ϱ parts of the products go through
  𝔰_P⁰ ≤ C_P⁰e^(φ/2)Y_s + C_(P,0)⁰η₀:
  - 𝔯_ϱ^f = ϱ𝒮[μ⁻¹(1 − 𝔵^z)⁻¹𝔤^l_(ϱ,t)k₂^z C_P⁰e^(φ/2)] is added to 𝔯;
  - ε^f = 𝒮[s_N + μ⁻¹(1 − 𝔵^z)⁻¹𝔤^l_(ϱ,t)k₂^z C_(P,0)⁰η₀ϱ];
  - route (𝔰) is the old one. Take the better route per case at level 6.
- **lem:tl5-hff-zero**, at every level. The zeroth-order step takes |Ψ_(ZC)|² through the energy of the shorter word C:
  - the coefficient 1/(2Ω̂²z̲) becomes 6μ𝔷²𝔨₂ (7μ𝔷²𝔨₂ for words shared in a family);
  - the part 8𝔲₀⁻¹|D̂∂_γ|² goes the same way, inside 𝔲₀^♯;
  - the smaller bound is taken pointwise;
  - the word h has its own leaf weight 𝔶₀^h ≤ μ⁻², to be optimised (𝔶₀^h = 𝔶₀ is the old case).
- **def:tl5-hff-constants:**
  - C_P⁰ = max(𝔤₁C_S^h, C_S^f) and C_(P,0)⁰ = max(𝔤₁C_(0,0)^h, C_(0,0)) replace 𝔤₁C_S^l and 𝔤₁C_(0,0);
  - C_S^h goes into 𝔨_rec^p;
  - 𝔐_p^(m) uses C_S^h at b = 0 and C_S^f at b ≥ 1;
  - max(C_(0,0)^h, C_(0,0)) is used in the η₀ parts of lem:tl5-hfp-low's step;
  - Y_f is the smaller root, as in P-GRD14.

Report:
1. The max-min targets at L4 and L6, all four cases, against G0q, with each lever's gain (switched off in turn).
2. What binds afterwards.
3. The quantities the Comparison could not price:
   - 𝔯_ϱ^f and η₀/𝔰₁^v at the L6 optima;
   - μ⁻¹C_(P,0)⁰η₀ against 0.1𝔰₁^v at the supremum;
   - the cost C_(E,0)(𝔶^h)/C_(E,0)(𝔶) of h's own weight;
   - the falls of C_S^f and C_S^h separately;
   - at L6, the split of 𝔐_p^(2) by its C₁ part.
4. Updated prices of the C₁ term of 𝔨_rec^p (÷ 2), with the |T|⁻¹ / λ_M^(−½) / K_rec split, as in G0q §G0q.2.

## Baseline (G0q, P-GRD14, main grid; computed)

| | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| L4 max min | −21.732 | −20.675 | −28.682 | −25.731 |
| L4 what binds | closing (𝔰_\* 0.20 spare) | closing (0.28) | 𝔰_\* (0.07) | 𝔰_\* (0.01) |
| L6 max min | −31.721 | −28.528 | −40.251 | −34.525 |
| L6 | ϱ and f balance; 𝔰_\* 4.65 below the closing | 3.45 | 5.82 | 4.69 |
| L4: 𝔨_rec^p C₁ term ÷ 2 | +0.09 | +0.24 | +0.06 | +0.29 |
| L6: ϱ coefficient × 0.1 | +0.90 | +0.61 | +0.81 | +0.40 |

- At L4, sup C_P^v is held by 𝔨_rec^p in all four cases (+0.10 / +0.40 / +0.19 / +0.52 over sup 𝔤₁C_S). At L6 the
  family term k₁𝔐_p leads every point.
- At every L4 optimum, S_F is its products f₂𝔎^D (4.2–6.8 decades above the linear part), and 𝔎 is led by C_P^v 𝔨_B.

## The code

- **Current program: `SP/g0p/levelQ.py`** = `SP/g0l/levelZ_head.py` + `SP/g0p/levelL_mid.py` + `SP/g0p/levelQ_tail.py`.
- How levelQ_tail is built:
  - `SP/g0p/patchQ.py` builds `levelQ_tail.py` from `SP/g0p/levelL_tail.py`.
  - levelL_tail comes from `patchL.py`, then a hand-added `G0P_CSS` line, then `patchL2.py`. So re-running patchL.py
    alone does not reproduce levelL_tail.py: it drops the CSS line.
- Suggested route: `SP/g0r/patchR.py` reads `SP/g0p/levelQ_tail.py` and writes `SP/g0r/levelR_tail.py`.
  - Each replacement goes through `rep(old, new)`, which asserts the count is 1.
  - Then `cat SP/g0l/levelZ_head.py SP/g0p/levelL_mid.py SP/g0r/levelR_tail.py > levelR.new`, check it with
    `python3 -c "import ast; ..."`, and `mv` it into place. Jobs read the file when they start, so an atomic mv matters.
- Sites in `levelQ_tail.py` (line numbers as of G0q):
  - **C_S^l**, lines ~291–306 (`if U0ON:`):
    - XS_ = 1/(2·O2·zlb) is the coefficient 1/(2Ω̂²z̲) that lem:tl5-hff-zero replaces by 6μ𝔷²𝔨₂ (7μ𝔷²𝔨₂ for family
      words), taking the smaller per point;
    - YS_ = 8|D̂∂_γ|²XS_ + 2𝔨₁, U0W = sqrt(YS_/XS_), bracket gSl = R⁻³·2·sqrt(XS_·YS_);
    - faceopt(4, …) is the face-weight search; FR[2] is the rank-2 leaf factor;
    - C_S^h needs its own leaf weight 𝔶₀^h: see the leaf constants below.
    - Then `CSx = CSx * G0P_CSS`.
  - **𝔤₁ = G1X** is defined right after `CSx, C00x, C1rx = ...` (~line 291). The sites `G1X * CSx` / `G1X * C00x` are
    listed by `grep -n "G1X \* C" levelQ_tail.py`: d['CP'], d['CP0'], d['CsW'], d['CsW0'], d['Cs0u'], d['CSN'], KK, KK0
    and the diagnostics. These become C_P⁰ = max(𝔤₁C_S^h, C_S^f) and C_(P,0)⁰.
  - **𝔨_rec^p**, ~line 353: `krec = KSK*SQ(7)*(KRC1*C1k + z1*sqrt(mu)*C1 + z2*mu*CSx) + mu*RS*CSx`. C_S^h goes here.
  - **𝔐_p**, ~line 425: `Mp = lambda m_: sqrt(sum(CSx**2 + C1W[(mu,x,7**b_)]**2 for b_ in range(m_+2)))`. Use C_S^h at
    b_ = 0 and C_S^f at b_ ≥ 1. For the C₁ split of 𝔐_p^(2), compare sqrt(Σ C1W²) with Mp(2).
  - **The ϱ parts at level 6**, `RHON` block: crho / gxr (𝔤_(ϱ,t) with 𝔠^ϱ), Rrho, R0, and rt1/rt2/rt3 in the rule. Route
    (𝔯) adds 𝔯_ϱ^f to 𝔯 (the 𝔯 budget, rt2) and replaces ε's ϱ coefficient by ε^f. Keep route (𝔰) and take the better
    per case.
  - **Lever 1 (Y_c)**: `leps_s = log(s1/(4*Ka_)) - lsupW + log(1+sqrt(0.9))`. For Y_f use the same construction.
  - Closing: lclose = log(0.1/Kc_) − lStot. Budget of 𝔰_\*: A-term s1/2, ϱ term s1/4, η₀ term s1/4.
- **Leaf constants**: `SP/g0m/ceq.py`, C2(r, y0, y1, J2MAX), C_(E,r)(𝔶)² = (1/2π²) Σ d/(𝔶₀ + 𝔶₁c + c²). The cost of h's
  own weight is C_(E,0)(𝔶^h)/C_(E,0)(𝔶). The weights 𝔶 = (μ^(−2s), μ^(−s)), and the optima all take s = 1.
- **Diagnostics already carried** (per optimum, in `J['patt'][N][mu]`):
  - lead_frac and CP_over_2CS (both levels);
  - krec_sup, Krec_T_share, … (L4; `q15.py` prints them and the deduced weighted-family bracket);
  - u0 (C_S changes).
  - ruleQ.py prints the S_F split (lin/prod) and KKlead from the record's last entry.
- **Runner**: copy `SP/g0p/runQ.sh` to `runR.sh` (it sets the main grid; L4 TH 7 values and SB {1e-2, 1e-4, 1e-6}; L6 TH = 1
  and SB {1e-4, 1e-6, 1e-8}), and `schedQ.sh` to `schedR.sh`. One job is about 2.3 min at L4 and 3 min at L6.
- **The background time limit is two hours.** G0q's scheduler was killed at it and two jobs had to be run again. Split
  queues to under ~100 jobs-minutes each, or chain several schedulers.
- **Check first**: P-GRD15 switched off must reproduce G0q (−21.73 at s1 D_A, μ = 10⁻⁵, L4; −31.72 at L6).

## Pitfalls met before

- Duplicate waiter processes: keep one waiter per output.
- `ruleQ.py` needs `tuple(...)` when formatting JSON lists.
- Wrap new diagnostics in try/except so that a shape error cannot kill a run.
- Level-6 `patt` carries lead_frac only since G0q.
