# DERIVE P — SESSION 7 (2026-08-16)
Bridge-6 T1, run. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Code: pack5/derive_P.py (+ tfd.py, rad.py copied from LOWDIN-PACK-4 code/), output pack5/derive_P.json.

## 0 · Kernel recovered and verified first
tfd.py / rad.py recovered from LOWDIN-PACK-4 code/. gate2.py rerun: rms 0.143 / bias −0.010 over 39
channels; regenerated gate2.json byte-identical to the held copy. Verified before any use.

## 1 · Route (bridge-6, M's ruling 4: P must be DERIVABLE)
P_l = (2l+1)·J_H(nl). J_H(d) = (F²+F⁴)/14; J_H(f) = (286F²+195F⁴+250F⁶)/6435.
F^k(nl,nl) = ∫∫ u²(r₁)u²(r₂) r<^k/r>^(k+1). u(r): entrant shell in the CHARGE-1 TFD object
(tfd.potential(Z,1), the rule-B object that produced the EB gaps), at the pack-5 kernel's E(n,l);
Numerov outward to the outer turning point, inward from r_max, matched; normalised.
Quadrature validated on hydrogen: F⁰(1s1s) 0.62500 (exact 0.625); F⁰,F²,F⁴(3d3d) 0.08605/0.04542/
0.02962 vs analytic 0.08605/0.04542/0.02962. Mesh 3000→6000: P moves < 1e-4.

## 2 · Result — the ten species, per-species P (Ha; 1 Ha = 27.211 eV)
| el | Z | shell | E_B | F² | F⁴ | F⁶ | J_H | P | P eV | test | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mn | 25 | 3d | −0.352 | 0.297 | 0.182 | — | 0.0343 | 0.171 | 4.66 | miss: P > 0.0108 | PASS |
| Fe | 26 | 3d | −0.493 | 0.350 | 0.216 | — | 0.0404 | 0.202 | 5.50 | hit: P < 0.2978 | PASS |
| Tc | 43 | 4d | −0.318 | 0.237 | 0.152 | — | 0.0278 | 0.139 | 3.78 | miss: P > 0.0262 | PASS |
| Ru | 44 | 4d | −0.387 | 0.260 | 0.167 | — | 0.0305 | 0.152 | 4.14 | hit: P < 0.2245 | PASS |
| Gd | 64 | 4f | −0.227 | 0.441 | 0.273 | 0.196 | 0.0355 | 0.249 | 6.76 | miss: P > 0.0569 | PASS |
| **Tb** | 65 | 4f | −0.412 | 0.498 | 0.311 | 0.223 | 0.0402 | **0.281** | 7.65 | hit: P < 0.2180 | **FAIL** (+0.063) |
| Os | 76 | 5d | −0.600* | 0.337 | 0.226 | — | 0.0402 | 0.201 | 5.47 | hit: P < 0.3766 | PASS |
| Cm | 96 | 5f | −0.286 | 0.352 | 0.227 | 0.166 | 0.0289 | 0.203 | 5.51 | miss: P > 0.1250 | PASS |
| **Bk** | 97 | 5f | −0.391 | 0.378 | 0.245 | 0.180 | 0.0312 | **0.219** | 5.95 | hit: P < 0.2145 | **FAIL** (+0.004) |
| Hs | 108 | 6d | −0.492 | 0.249 | 0.166 | — | 0.0297 | 0.148 | 4.04 | hit: P < 0.3261 | PASS |
*Os E_B(5d) sits at the bisection floor (see §4); its true gap is larger, so PASS a fortiori.

**8 of 10.** Both d shells and 5d/6d pass. 4f fails at Tb by 0.063 Ha (1.7 eV, ~29 %); 5f fails at Bk
by 0.004 Ha (0.11 eV, ~2 %). Bridge-6 named 4f as the place a free-ion J_H would fail (7 J_H ≈ 7 eV
vs 5.93 eV window); the kernel's screening lowered it to 6.76–7.65 eV — not enough.

## 3 · Clause scored over 106 steps with the derived P (owed-check form)
Rule A argmin in E_A; if that subshell is d/f and exactly half-full at Z−1, re-decide in E_B with the
species' own derived P on it. **96 → 98 / 106.** Moved: Mn, Tc, Gd, Cm → HIT; Tb, Bk → MISS.
No other step changes (only the ten can, by construction). Opening sequence untouched (none is an opening).
Compare: chosen P in (0.125, 0.218) gave 100 (bridge-6, CHOSEN, §H.6). The derived P is not inside
that corridor for the f entrants — it is derived, and it does not close the four.

## 4 · Fault found in pack-5 (flag, R 1671 shape)
step3_rows.jsonl: **24 of 106 rows carry an E_B value equal to −0.6 exactly** — the eigen bisection floor
−0.6ζ² with ζ = 1 in the charge-1 object (Session 4 fault (ii) fixed the floor for large ζ; at ζ = 1 deep
shells lie below it). Rows: O F Ne (2p) · Co Ni Cu (3d) · Zn (4s) · Br Kr (4p) · Dy Ho Er Tm Yb (4f) ·
W Re Os Ir Pt Au (5d) · Es Fm Md No (5f). In every one the clipped subshell is already the argmin, so no
rule-B hit/miss changes, but the E_B MAGNITUDES and gaps on those rows are understated. E_A rows: 0 at floor.
Only Os in the class is affected (upper bound of the 5d window is a lower bound on the true gap).
Not repaired here (would touch a pack-5 artefact); owed: rerun step3 with a deeper floor for charge 1.

## 5 · What this says, stated plainly and not decided
- The route M ruled runs end to end from the kernel with no chosen constant. It fits d and misses f.
- The failure is at the shell where an unscreened one-electron F^k is known to overshoot most (4f, compact);
  Hartree–Fock and spectroscopic F^k for lanthanides run ~20–30 % below bare-orbital values (Racah/
  Cowan reduction — literature figure, not measured here). The Bk miss (2 %) is inside that scale.
- Two honest readings: (i) the kernel's u(r) is too crude for F^k at f — bridge-6's fallback (MEASURED
  F^k from term analyses, per species) applies, M to rule on admissibility; (ii) (2l+1)J_H over-counts
  the exchange lost — the pairing electron in the 5d alternative also loses/gains exchange, and the
  correct penalty is a DIFFERENCE, which is a different route and a different derivation.
- Nothing about ν, α, or Chapter 34 changes. Ruling 1 (no chapter until closure) stands.

## 6 · Figures (§H.6)
MEASURED (from the kernel): the ten P, F^k, E_B. CHOSEN: none — that is the point of this session.
INHERITED: EB windows (SEQUENCE-MISSES-SESSION-6), step3_rows.jsonl, ground.py (NIST 5.12), tfd/rad kernel.
