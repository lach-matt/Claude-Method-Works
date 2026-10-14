# What the large end's interior is required to be (item 391)

*First headed* 2026-10-14, on M's item 391, "Continue": the next step of the order approved at 384 that does not rest on
SOURCE. The rows are O1b (no curvature singularity on the passage) and O1c (every causal route of the passage complete)
at the large end. The small end's are proved (o1c_oneway, verified 337). This is the specification, worked from M's
rulings and the record's own methods, with what is already settled. Computed in `interior_large.py` (I0-I5; selftest
4/4, mutants 4/4). Labels: M's (a ruling), computed, deduced, READ, estimate.

## What M's rulings fix

1. **One object, one way.** Our black-hole face, then 273's quantum region, then position 2's white-hole face: "different
   views of the same object" (132). Nothing from position 2 enters the passage: "You are forgetting that the passage is
   one-way only" (270, 277). M's.
2. **README only, complete, no Cauchy horizon.** The option text M chose at 273: "One-way, complete, README only, no Cauchy
   horizon". Classical GR is given up inside a small quantum region, and only there. The bulk is never empty (320), so
   its content enters at its own order. M's.
3. **Position 2's face opens with the README and closes when the corridor holds nothing** (109, 390). Computed in
   junction_own G10: the face closes as the README's last part leaves the anti-trapped region. M's.
4. **Position 2's side carries its own values**: its own r_s2 (240) and its own sigma2 (226, 387, 388). The object's
   interior is at our sigma, which is forced wherever the junction would rise (junction_own G6). M's, computed.
5. **Einstein's law holds outside the quantum region** (324-328): the Gauss-Bonnet coupling is zero, so gravity keeps the
   one light cone. Derived, C9 verified.

## What the record's own methods already give at the large end

6. **The 4D stretch is settled.** The plane reads four-dimensional Schwarzschild outside the hole (C3). Inside, its own
   time T is monotone along every causal geodesic, as in o1c_oneway Z2. Between the face and any R_c > 0, T spans less
   than pi r0/2, and null geodesics have a finite affine length. Computed, exact (I1).
7. **That stretch ends where the bulk dimension enters**: the curvature radius reaches ell at
   R_5 = 12^(1/6) (r0 ell^2)^(1/3). That is 3.26 ell at r0 = 10 ell and 7.02 ell at 100 ell. Computed (I2).
8. **273's quantum region lies far below R_5.** Even on the 4D form it would sit at 4.95e-14 R_5 (with ell at its
   ceiling, l5 = 1.54e-25 m). So between the two lies a five-dimensional stretch of the large hole's interior.
   Computed (I2); the region's boundary is 273 (b)'s estimate.
9. **The README's own route is settled.** Inside the README's shell the geometry is flat (273's construction;
   o1c_oneway Z2b). The shell's generators are radial null geodesics there, affinely parametrized, at every dimension,
   and on the 4D outer side as well. They run from our face to 273's region in finite affine parameter, with no
   curvature on the inner side, and they do not depend on the 5D stretch's interior. Reflected, the README leaves
   position 2's past interior the same way, by its face, which then closes (390). Computed, exact (I3).

## What is required, and not yet held

The passage also includes the open interior behind the shell, where the bulk's own content may cross after the
README (o1c_oneway Z6; 320). Between R_5 and 273's region that interior is the large brane hole's five-dimensional core.
The record holds no solution for it: C3 is the exterior, READ, and the interior was never computed (item 356). Required of
it:

- **(a)** A function strictly monotone along every future causal geodesic there, with its rate bounded below away from
  our face. That is what brings every route to 273's region in finite affine parameter; T plays this part in the 4D
  stretch, and Z2's T at the small end. For O1c.
- **(b)** No Cauchy horizon: no inner horizon before 273's region. From 273's option text.
- **(c)** Curvature finite until 273's region, with no singularity forming off the shell before the README reaches it.
  For O1b.
- **(d)** The same on position 2's side, with its own r_s2 and sigma2.

## Two routes, and their cost

- **A proof** covering every static vacuum interior of the large brane hole. It would rest on Einstein's law in the bulk
  and on the plane at sigma > 0, both of which meet the null energy condition. Light: worked in the conversation, with no
  runs.
- **A computed interior**: the two-dimensional (time, radius, bulk) problem that the runs at 365-367 attempted and 384
  dropped. Heavy: hours of runs and much of a week's data. Worth it only once (a)-(c) say what it must show, which they
  now do.

The board's order, to be overruled by M at any point: the proof first.

## Item 392: Zeno's halves as the method for the 5D stretch

M, 392: "The zeno paradox describes halves and their halved segmentation. This can be a useful model for run such a
large size computation". Considered, and checked first where the answer is exact (`zeno_method.py` Z0-Z5; selftest 6/6,
mutants 3/3).

**The method.**
- Cut the remaining distance to the end in halves.
- Rescale each half to one size and give it the same fixed effort.
- Hand each half's end state to the next.
- Once the rescaled halves settle to one form, the rest is that form's geometric series: Zeno's sum, with its tail
  bounded.

The run then costs the number of halvings (about 45 for the 5D stretch), not the ratio of its ends (2e13).

**Checked on the 4D interior, where the answer is exact.**
- 45 halves of 40 steps each reach 1.4e-14 of the radius, every half accurate to 1e-10.
- The same 1,800 steps spread uniformly lose 1e-6 accuracy at 0.01 of the radius, twelve orders short.
- The halves measure the approach themselves: time per halving falls by 2^-3/2 in 4D and 2^-2 in 5D (Kasner's
  exponents), and curvature rises 2^6 and 2^8 per halving.
- The tail bounded from the measured ratio matches the exact remainder to 1e-9.

**What the halves measure, against (a)-(c) above.**
- (a) The proper time to 273's region is the sum over the halves, finite once the per-halving ratio settles below 1.
- (b) No inner horizon: the clock stays monotone in every half. A ratio stalling at 1 would signal one.
- (c) Curvature finite in each half, its growth per halving measured, up to the bulk's Planck boundary.

**Where it applies to the record's interior runs** (`interior_large/README.md`, items 360-367). Those runs failed two
ways. The grid lost resolution toward the brane (B5, C1), and the chart ends at finite proper time (B6). Halving answers
both, three ways:
- **In time.** Halve the proper time left. Restart each half from the last state, with the fields rescaled by B6's
  fitted power laws (A, T ~ u; S, B ~ u^-2; F ~ u^-1, u = 1/(1 - s)), so they are of order one. Re-grid, and run the
  half at one fixed resolution. This replaces the continuous lapse driver that failed at C1.
- **In the bulk coordinate.** A halving mesh toward the brane, [0, 1/2], [1/2, 3/4], [3/4, 7/8], ..., with the same
  points in each part. The brane's sharpening gradients then cost the number of halvings.
- **In the hole's size.** Sample r0/ell at about 1, 2, 4, 8 and 16 (bt = 1 ... 16, all solved at stage B3), and test
  whether the measured ratios settle as r0 doubles. The large end beyond 20 ell then follows from the limit.

**The first run, if M approves it** (377: question, criterion, time; 384: cost stated first).
- **Question:** does one rescaled restart at bt = 1, from the trusted state near s = -0.5 (B7's damped Nx = 28 run),
  carry the solution over half the proper time left to the chart's end, at one fixed resolution per mesh part?
- **Pass:** the DeTurck norm stays at or below 1e-4, and the Chebyshev tails at or below 1e-6, at the half's end.
- **Time:** generating the rescaled equations (the record's `gen_*.py` take a few minutes), then one run, stopped at
  20 minutes.
- **Cost:** small next to the runs at 365-367.

Its result decides whether the second half is run.

**Item 393: run, and it failed its criterion** (`interior_large/README.md`, "Item 393").
- **The trusted state was rebuilt** and matches the record to 0.4 per cent.
- **The half reached s = -2.0** in 335 s, but phi rose to 6.4, against a criterion of 1e-4.
- **The brane, where the record's runs failed, stayed resolved** (phi <= 5e-4 there).
- **The error grew at the first interface, x = 1/2, and in the axis part.** That part was under-resolved from the start,
  where the curvature is largest.

The second half is not run. A second attempt at the same half would halve toward both ends, give the axis part more
points, and couple the parts by penalty. It is for M to approve.

**Item 394: approved, checked, run -- it failed earlier** (`interior_large/README.md`, "Item 394").
- **The joining, checked on a known solution.** The coupling derived from the discrete energy, with the axis folded away
  (all fields are even in x), is strictly stable. It holds the error at 2.5e-13 to s = 40, where item 393's joining
  grows to 1e93 and the single grid to 27.
- **The interior run.** It held to s = -0.54, then blew up from s = -0.56, at the brane node. The coupling's spread
  reaches that node, and the record's Israel rows fix it algebraically. The model check had shown that an algebraic
  slope condition at an end node is unstable in this scheme.
- **The next fix, for M:** impose the brane conditions weakly, in the same energy form. The second half is not run.

**Item 395: the third attempt -- the brane imposed weakly** (`interior_large/README.md`, "Item 395").
- **Checked on the model first.** With b zero at the brane, as it is in the interior, the weak far end holds the error at
  1e-12.
- **The board's sign error.** The first two runs failed on it: the coupling's damping was derived for time running
  forward in s, and the interior runs backward. The spectrum found it: 186 per unit -s on the joining before the brane,
  falling to 1.05 when corrected.
- **The corrected run** held the DeTurck norm under 1e-4 to s = -0.80, the farthest yet. It stopped where A, and with it
  g_ss, reached zero at x = 0.22: the s-slicing degenerates there.
- **Open:** whether that is the solution or the scheme. The record's own single grid continued to s = -0.8 would decide
  it, in about 5 minutes, for M to approve.

**Item 396: the comparison -- the solution's, and benign** (`interior_large/README.md`, "Item 396").
- **The record's own grid**, continued to s = -0.80, reaches A = 0 at x = 0.227 at the same s as the third attempt. The
  two agree to about 1e-3 everywhere.
- **It is benign.** There the s-slices stay spacelike (g^ss < 0), the metric Lorentzian and the system hyperbolic
  (b^2 + a > 0). Only d_s tips outside the light cone.
- **So the stop was the coupling's own assumption** (a > 0), not anything in the interior.
- **Next, for M:** a coupling built on the characteristic speeds, which stay real; checked on the model, then the same
  half.
