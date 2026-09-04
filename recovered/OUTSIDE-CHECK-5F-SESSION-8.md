# OUTSIDE CHECK — THE 5f KERNEL — SESSION 8 (2026-08-16)
Bridge-7 T3 (Bk F^k owed) run as an outside CHECK only. Under M's ruling (session 7, §8) measured F^k do
NOT enter the law; this file tests the kernel where the derived law's margins are thinnest (5f: Cm 0.015,
Bk 0.009 Ha above the window floor). Bank UNCHANGED; nothing written to register/index/store.

## 0 · Prediction, stated before the lookup
Kernel J_H(4f) ran 15 % high against Tb³⁺ (Carnall 1989). If J_H(5f) runs 15 % high, P_ii = 7(J_H − K)
drops ~0.030 Ha at Cm and Bk: both fall BELOW. Prediction: a 15 % 5f overshoot breaks Cm and Bk.

## 1 · Found and ENTERED
Cm³⁺:LaCl₃, Gruber, Cochran, Conway, Nicol (J. Chem. Phys., 1960s; via a 2009 secondary that quotes the
set): Racah E¹ 4621.47, E² 17.70, E³ 399.42 cm⁻¹. Inverted (Nielson–Koster convention, F₂ = F²/225,
F₄ = F⁴/1089, F₆ = 25F⁶/184041; E¹ = (70F₂+231F₄+2002F₆)/9, E² = (F₂−3F₄+7F₆)/9, E³ = (5F₂+6F₄−91F₆)/3):
**F² 61,855 · F⁴ 55,414 · F⁶ 38,960 cm⁻¹ → J_H = 5,942 cm⁻¹ = 0.02707 Ha.**
Kernel Cm J_H(5f) = 0.02893 → kernel/measured = **1.069 (7 % high)**, not 15 %. Prediction FALSIFIED.
Cm P_ii with measured J_H and kernel K: 7·(0.02707 − 0.0089) = **0.1272 — IN by 0.002 Ha** (floor 0.125).
Caveats stated: (a) older analysis, and its F⁴/F² = 0.90 is high against later systematics (~0.8);
(b) trivalent F^k are an UPPER bound on the charge-1 value the law asks for, so the true derived margin
at Cm is ≤ 0.002 Ha under this check.

## 2 · Recalled and NOT entered (protocol: recalled ≠ read)
Carnall's systematic Cm³⁺:LaCl₃ values (JCP 96, 8713 (1992) and the 1989 systematics) are remembered as
roughly F² 55k, F⁴ 44k, F⁶ 33k cm⁻¹. NOT read this session; NOT entered. If they stand, J_H ≈ 0.0230 Ha,
kernel 26 % high, and Cm P_ii ≈ 0.10 — BELOW. Stated so the gap cannot close over: which Cm³⁺ set is
authoritative decides whether the outside check passes or fails at Cm. **Owed at source.**
Bk³⁺: still not found (as session 7). Owed.

## 3 · What this says (stated, not decided)
- The 5f result is not robust: the entered check exhausts 87 % of Cm's margin; the recalled check breaks it.
- This is the "thin 5f margins" residue of bridge-7 §2(a) made concrete. It is a KERNEL question (the
  one-electron TFD u(r) at 5f), not a counting question — same diagnosis as Tb at 4f (session 7 §7).
- The only derivable path is a better u(r) at f (self-consistency / non-local exchange), bridge-7 T1'.
  A factor is not derivable and is not offered.
</EOF
python3 - <<'EOF'
p="BRIDGE-LOWDIN-SESSION-8.md"; s=open(p).read()
s=s.replace("""- COMPUTED-TFD.tsv floor audit""","""- T3 outside check on the 5f kernel (OUTSIDE-CHECK-5F-SESSION-8.md): prediction (15 % overshoot breaks
  Cm/Bk) stated first; Cm³⁺ (Gruber, LaCl₃) entered → kernel J_H(5f) 7 % high, Cm P_ii 0.1272 IN by 0.002.
  Carnall's own Cm³⁺ set recalled (~26 % high → Cm BELOW) but NOT read → NOT entered → owed at source.
  Bk³⁺ still not found. The 5f residue is a kernel question; T1' is the only derivable route.
- COMPUTED-TFD.tsv floor audit""")
s=s.replace("Bk F^k\n      (Carnall 1992) as outside CHECK only.","Carnall's own\n      Cm³⁺ and Bk³⁺ F^k at source (decides the 5f outside check).")
s=s.replace("R 1737\n      COMPUTED-TFD floor audit clean (0/103,545).","R 1737\n      COMPUTED-TFD floor audit clean (0/103,545) · R 1738 5f outside check (Cm 7 % / recalled 26 %, owed).")
s=s.replace("LOWDIN-PACK-8.tar.gz: REPAIR-FLOOR-SESSION-8.md ·","LOWDIN-PACK-8.tar.gz: REPAIR-FLOOR-SESSION-8.md · OUTSIDE-CHECK-5F-SESSION-8.md ·")
s=s.replace("pack5fix/{eigen_fix.py,","pack5fix/{eigen_fix.py, audit_tfd_floor.py,")
open(p,'w').write(s)