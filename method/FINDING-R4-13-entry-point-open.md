# FINDING R4-13 — the entry-point excess is an open question, and this is its shape. NOT REPAIRED.

M, 6 September 2026, on the drift of t/t(ℓ) with ℓ: *"is this an open question?"*

**Yes.** It was open before this pass, it is open now, and its shape has changed. `method/proofs/
entrypoint.py` §5 measures everything below; its selftest asserts register 1335's slopes and r²
values, rebuilt from the ionisation energies.

## Where the record stood

**Register 1337:** *"**Not derived**: a common factor of 1.029, both p and d 2.9 % high, which two ℓ
values cannot adjudicate."* Open, and marked so.

**§34.10 then claimed it closed:** *"Λ_chem dissolved two residuals … **the 1.029 was arithmetic**: the
excess above U is 0.028 of the spread at p and 0.785 at d, a ratio of 27.7, and the apparent 2.9 %
agreement came from comparing a ratio at p, where t ≈ 1, with a ratio at d, where t ≈ 1.78."*

**That dissolution compares the wrong residual.** The law predicts t(ℓ) = √(ℓ(ℓ+1)/2), so the
residual is t_meas / t_pred — 1.028 at p and 1.030 at d, agreeing to 0.2 %. The *excess above U*,
t − 1, is a different quantity that the law makes no claim about, and its ratio of 27.7 says nothing
about whether the multiplicative factor is common. **Two points agreeing on a factor to 0.2 % is not
arithmetic; it is either a regularity or a coincidence, and two points cannot tell which.**

**The third point tells.** f gives 1.040. **The factor is not common**, so register 1337's *"common
factor"* was a two-point over-reading, and §34.10's dissolution was right in its conclusion and wrong
in its reason. Both are superseded by the measurement.

## A candidate closure for p and d, from the corpus's own numbers, made nowhere in the record

Register 1337 reads t *"at the subshell's OPENING"* — where the entrant already holds **one
electron** — and says *"t rises linearly with occupancy across each subshell, r² 0.90 to 0.95."*
Register 1335 measures the slope per subshell. **The law's p is the node count, a q = 0 quantity.
Nowhere does the record carry t back to q = 0.** Doing so, with 1335's own slopes:

| | t at q = 1 | t at q = 0 | predicted | excess before → after |
|---|---|---|---|---|
| p, median of four | 1.0284 | 0.9949 to 1.0121 | 1.0000 | **+2.84 % → −0.5 % to +1.2 %** |
| d, mean of two | 1.7846 | 1.7219 | 1.7321 | **+3.04 % → −0.58 %** |

The p range is the two ways of extrapolating one electron back — one slope back from the q = 1
point, or the fitted line's own intercept — and they bracket the answer. **The 2.9 % the record could
not derive is mostly the occupancy offset: one electron's worth of slope, read at the opening.**
Carried back, the p and d excesses fall from about +3 % to within a percent, and the sign is no
longer fixed.

Three of register 1335's four p slopes rebuild from the ionisation energies to the fourth decimal.
6p rebuilds as +0.0339 in `a`, which is **+0.0276 per corridor width** — the figure the register
prints, in the other unit. Its r² is exact either way. Recorded, not scored.

## And f does not close that way, for a reason that is physical and a limit that is the data's

| | slope across the filling | t at q = 1 | t at q = 0 | predicted | excess |
|---|---|---|---|---|---|
| 5f, Pa to Am | **−0.0009**, r² 0.01 | 2.5476 | 2.549 to 2.567 | 2.4495 | **+4.0 % to +4.8 %** |

**The actinide first ionisation energies are flat across the 5f filling** — Pa 5.89, U 6.19, Np 6.27,
Pu 6.03, Am 5.97 eV — so the slope is zero and the extrapolation moves nothing. **And the reason is
that an actinide ionises from 7s, not from 5f.** `a_meas = (n − ν)/√p` takes the first ionisation
energy as the entrant's, which is right at a p opening (aluminium loses its 3p electron) and wrong
at an f opening (protactinium loses a 7s). **So the f point is reading the wrong electron**, and
so, for that matter, are the d points — yttrium and lanthanum ionise from 5s and 6s — though those
happen to extrapolate well.

**The survey cannot sharpen it.** Its highest measured f channel is at Z = 81. Every actinide 5f row
is *computed* and *unwitnessed*, bound *"open-shell core, 119 parents."* No measured 5f binding
energy exists in the corpus.

## What would close it, and none of it is here

1. **A subshell-resolved binding energy for the 5f electron at protactinium** — the 5f orbital's own
   ionisation, not the atom's first. Not in the corpus.
2. **Or a ruling that the entry-point law is a q → 0 statement**, which would bring p and d to
   within a percent of √(ℓ(ℓ+1)/2) and leave f as a single point on an estimated input reading the
   wrong electron — honestly stated as such.
3. **Or a second f opening**, which the periodic table does not have.

**Nothing is repaired here.** Register 1337's *"not derived"* stands; what has changed is that it now
stands over three ℓ values instead of two, with most of the p and d excess accounted for and the f
excess explained as a limit of the measurement rather than of the law.

---

## CORRECTION, later on 6 September: the record already carries the occupancy answer, at register 1353, and it goes the other way

The section above headed *"A candidate closure for p and d … made nowhere in the record"* is
**withdrawn**. It was made in the record, at register **1353**, and I had not read it:

> *AND T IS A CONSTANT OF THE SUBSHELL, NOT AN ENTRY POINT. With the Pauli fraction in the radicand,
> t barely moves across a subshell: 6p gives 1.0237, 1.0417, 1.0009, 1.0036, 0.9946, 0.9940 across
> all six occupancies — spread 0.048. The occupancy dependence measured at register 1335, sd 0.19,
> is entirely absorbed.*

Two things follow, and both undo the extrapolation above.

**The opening is q = 0 in the record's own convention, not q = 1.** The finished form's radicand is
p + q/2(2ℓ+1) with q the electrons *already present*: the first value in 1353's 6p row, 1.0237, is
register 1337's opening value unchanged, which it can only be if q = 0 there. So *"where the entrant
already holds one electron"* misread the convention, and carrying the opening back by one slope
step moved the reading to q = −1, a point that does not exist. The p and d figures headed *"t at
q = 0"* above are withdrawn; register 1337's opening values are the q = 0 reading.

**The occupancy dependence is not an offset to subtract; it is absorbed by the form.** Under the
finished form the fill of 6p sits at 1.00 to within a percent at every occupancy *except the
opening*, which stands 2.4 % above — the opposite of the picture above, where the opening was the
point to be corrected toward the others. The +2.9 % at the openings is therefore not *"mostly the
occupancy offset"*; it is what the openings read, on either form.

**What §34.7 actually claims was also read past.** The chapter does not claim t = √(ℓ(ℓ+1)/2) at
each opening. It prints register 1354's Λ_t row — *"a limit approached along n, not a constant:
the p row of Λ_t reads 1.120, 1.049, 1.022, 1.002 at n = 3, 4, 5, 6 — 6p sits 0.2 % above the
centrifugal value"* — so the book's statement is a **limit along n**, whose first term at p sits
12 % above it and whose first term at d (4d, 1.845) sits 6.5 % above. Against that statement an
f row consisting of its first term alone, at +4 % or more, is not a discrepancy of any kind.

The f-point analysis above stands on its own facts — the actinide ionisation energies are flat and
read the 7s electron — but its closing sentence, that no 5f binding energy exists in the corpus,
is corrected in **FINDING-R4-14**, which finds it in the derived field and rebuilds the field's
producer to regenerate it. Third time this pass that the record held what I called absent; the
standing rule is restated because it was not applied: **read the Register entries around a figure
before measuring past it.**
