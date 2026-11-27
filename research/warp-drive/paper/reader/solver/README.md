# Solver for the certified approximant (double-double / quad-double)

Code that computes the coefficients printed in the tables of the approximant (P-APPC's printed form,
F = F_seed + (v − ½)^4 Σ χ_i ψ_j G_ij, G_ij Chebyshev in (t, σ, x)), and the checks around it. Working files and
large outputs live outside the repository (scratchpad `bsolv/`); only code and small validation outputs are here.

## The formulation

- Unknowns R, m, n, W, s of (u, v, x) in the double-null gauge of the class; ξ = arsinh((u + 1)/a), a = 1/500.
- **The axis-regular evolution system** (`derive.py`, from `regform.py` = P-APPC lem:appc-regular):
  E1 = (f_11 − f_xx)/(1 + x), E2 = (f_22 − f_xx)/(1 − x), E3 = f_xx, E4 = f_ln give (R, m, n, W)_uv, with
  coefficient matrix of determinant −1/(Ω⁸R) (nondegenerate at the axes; solved explicitly), and E5 = f_lx/√w
  gives s_vv (no u-derivatives: a transport along each outgoing cone). The divisions by 1 ± x are exact polynomial
  divisions. `gen.py` writes `rhs_gen.h` (a C++ template, 948 multiplications after CSE); `gen_res.py` writes
  `res_gen.h`, the eight residual components f_ab/ρ of lem:appc-regular (f_lx, f_nx divided by √(1 − x²)).
- **Data**: N₀ = {v = ½}: the seed (lem:tl5-seed); N₁ = {u = −10}: m, n of eq:cone-data, W = W_seed, R from the
  Raychaudhuri equation, s from its own transport. The boxes of def:appc-layouts extend beyond the region (u < −10,
  v < ½, v > 7/2): the solver computes the analytic continuation by solving the Goursat problem in all four quadrants
  around the corner (−10, ½), with the data continued analytically (env = sin⁴(π(v − ½)/3) without cut-off).
- **Discretization**: Chebyshev–Lobatto in x (M + 1 nodes, axes included); a tensor grid of cells in (ξ, v), each
  with Chebyshev–Lobatto nodes of degrees p_ξ, p_v; the cell problem is the Goursat integral equation
  G = P(G) := B + I[Ψ(G)]. Unknown G = (F − F_seed)/(v − ½)⁴ in every cell; in the cells adjacent to N₀ the
  v-nodes are Radau nodes excluding v = ½ and the update uses the exact operators q ↦ ε⁻⁴∫₀^ε t³q (uv-equations) and
  φ ↦ ε⁻⁴∫₀^ε (ε − t)t²φ (shift), so G is produced directly near N₀ and never by dividing a solution by (v − ½)⁴.
- **Difference arithmetic** (`diff.h`): Ψ is evaluated as Ψ(seed + D) − Ψ(seed) without cancellation (each
  intermediate quantity carries the seed's value and the perturbation), so G is obtained with an error relative to
  the perturbation, not to R ≈ 10.
- **Defect correction**: the residual r = P(G) − G in the working precision (dd or qd), the correction by Picard
  sweeps in double in difference arithmetic about the current state; each outer step gains about 11–16 digits
  (3–4 outer steps in dd, 5–6 in qd).
- **Output**: each finished cell is evaluated (barycentric) at the Chebyshev–Lobatto nodes of every element box that
  meets it; `coef` turns these values into the element's Chebyshev coefficients; the first-row cells also give the
  Taylor coefficients of G at v = ½ (the jets on N₀⁺, orders 4..12 of F).
- `jets.cpp`: the same jets by the transport hierarchy along N₀ (Taylor arithmetic through the same equations;
  s_k algebraic, a_k by a linear transport in u with the seed's coefficients, initial values the data's Taylor
  coefficients at (−10, ½)) — an independent check of the jets the approximant carries.

## Build (gcc ≥ 11, OpenMP; no -ffast-math)

    python3 derive.py derive.pkl && python3 gen.py derive.pkl rhs_gen.h && python3 gen_res.py res_gen.h
    for P in dd qd; do F=""; [ $P = qd ] && F=-DUSE_QD
      g++ -O2 -march=native -fopenmp -std=c++17 $F -o solver_$P solver.cpp
      g++ -O2 -march=native -fopenmp -std=c++17 $F -o coef_$P coef.cpp
      g++ -O2 -march=native -fopenmp -std=c++17 $F -include array -o evalres_$P evalres.cpp
      g++ -O2 -march=native -fopenmp -std=c++17 $F -o jets_$P jets.cpp; done

`rhs_gen.h` and `res_gen.h` are generated but kept here so that a build needs no sympy.

## Run

    python3 mkcfg.py CASE M PXI PV NCOL1 NCOL2 NROW1 NROW2 NT NS PREFIX [threads] [quadrants] [key=value ...]
    ./solver_dd PREFIX.cfg          # or solver_qd; resumes from PREFIX.ckpt if present, --fresh to restart

CASE is s1A, s2A, s2D or s1D (rep.py's names: seed, region). NCOL1/NROW1: cells from the corner (−10, ½) toward
larger ξ / v; NCOL2/NROW2 the other side (u < −10, v < ½). NT, NS: Lobatto degrees at which the element boxes are
sampled. Useful keys: `tol` (outer tolerance, relative; 1e-31 dd, 1e-42 qd), `floor` (stop the outer loop below this
residual; 1e-28 dd, 1e-39 qd production), `lowswitch` (qd builds: outer steps with a residual above it are
evaluated in dd; 1e-24), `ckpt_minutes` (default 20), `stopcol`, `stopcells`, `threads`.
A log line 'not converged, last update …' means the last residual exceeded 1000 × tol; with floor > 1000 × tol it is
harmless (the cell stopped at the floor). **Resume**: a checkpoint (`PREFIX.ckpt`) is written at the end of a column at least every `ckpt_minutes` and at the
end of every quadrant; rerunning the same command continues from it. `PREFIX.log` has one line per column.

## Outputs

| file | content |
|---|---|
| PREFIX.elem | G at the element boxes' Lobatto nodes, per element and field (binary; `bsio.read_elem`) |
| PREFIX.jets | Taylor coefficients of G at v = ½ from the first-row cells (`bsio.read_jets`) |
| PREFIX.coef | `coef_dd PREFIX.elem PREFIX.coef`: Chebyshev coefficients per element and field (`approx.read_coef`) |
| PREFIX.log, PREFIX.ckpt | progress (one line per column) and the checkpoint |

Post-processing: `tables.py` (quanta, printed blocks with line checks and block sums, read back, page count,
`_approx.txt` for evalres, `_z.pkl` for the certification), `evalres_*` (the residual of a printed or unquantized
approximant at sample points, in dd or qd: floating diagnostics), `post.py` (that, over a set of quanta), `rates.py`
(decay rates against S-APP), `jets_*` and `jetcheck.py` (the v-jets on N₀⁺ by the transport hierarchy, and the
carried jets of a run or a table against them), `bsio.py`, `approx.py` (readers and the approx.txt writer),
`consts.py` (spectral constants).

## Certification (from the printed integers; python-flint)

    python3 cert3.py CASE TABLE_z.pkl I J N1 N2 N3 RHO1 RHO2 RHO3 PREC K OUT.json   # element's own residual
    python3 overlapK.py CASE TABLE_z.pkl I J K OUT.json [PREC]                      # the overlaps, orders <= K
    python3 certsum.py DIR [mu ...]       # B = own + Lambda per order, from DIR/c30_IJ.json and DIR/ovK_IJ.json

`cert3.py` is P-APPC prop:appc-element-bound with exact integer re-expansions (FLINT `fmpz_mat`) and slab-wise ball
arithmetic, derivative orders ≤ K; `cert3.py --majorant CASE TABLE_z.pkl I J 2,1.5,1.4 2.5,1.6,1.4 ...` scans M over
choices of ρ before the full run (choose ρ per element: M explodes where the table prints noise). `overlapK.py` is prop:appc-overlap for orders ≤ K with
(K + 2)-jets (derivative-majorant arithmetic; the seed's derivatives by bivariate Taylor arithmetic in balls).
`cert2.py`/`overlap2.py` are N-APP1's procedures with one quantum per block (they reproduce N-APP1 exactly).
`napp1/` holds N-APP1's modules these import (`rep.py` layouts and seed, `cert.py`, `majorant.py`, `overlap.py`,
`regform.py`), copied unchanged; `NAPP1=dir` points elsewhere. Memory: ≈ 2 GB per element at 2M nodes.

## Validation outputs here

See `validation/` (small text files): comparison with the record's run, convergence in p, cell size and M, jets
against the hierarchy (unquantized and the p = 30 tables), residuals of the printed tables, and the certificate of
the pilot's p = 30 tables (`cert_s2A_p30.txt`: cert3, overlapK, certsum, and the overlap-lever measurement).

## Findings that bear on the printed form (measured; details in the report B-SOLV)

- **The box extensions into the side quadrants.** def:appc-layouts extends the boxes of the elements (1, ·) and
  (·, 1) beyond u = −10 and below v = ½, where the polynomial must represent the analytic continuation of the
  solution of the characteristic problem into the quadrants u < −10 < ..., v > ½ and u > −10, v < ½. There the
  angular modes grow like e^(2l√|ΔuΔv|) (the Riemann function I₀ instead of J₀): measured ρ_x falls from ≈ 2.3 on
  N₁ ∪ N₀ to 1.52 at the corner (u, v) = (−1.94, 0.4145) (|c₈₀| ≈ 1e-20) and 1.73 at (−10.59, 3.58), against
  |c₈₀| ≤ 1e-31 everywhere in the region itself. Boxes that start at u = −10 and v = ½ (no inner nine tenths at
  those two edges) avoid this entirely; `mkcfg.py` configs can carry both layouts (extra `elem` lines).
- **Double-double noise and the certificate.** The dd coefficients reach a noise floor ≈ 1e-33 (absolute); quanta
  below it print noise in two directions at once and the polyellipse majorant M explodes. Certifiable dd tables
  need p ≤ 30–31 (pilot); finer quanta need the qd solution.
- **The overlaps at derivative order K.** The partition's derivatives up to order K + 2 (φ₆/(2d)⁶ ≈ 4e13 in v)
  multiply the element mismatch on the strips, bounded by coefficient sums of the exact difference polynomial. On
  the pilot's p = 30 tables they set the certified bound (≈ 1e-15 at level 0, ≈ 1e-4 at order 4); the mismatch is
  the tables' truncation (≈ 200 quanta), so the overlap term falls with the quantum.
- **Format**: at p ≳ 30 the block sums S₁, S₂, S₀ have ~p digits and do not fit with their labels on one 121-character
  line; `tables.py` sets them one per line.
