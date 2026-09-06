# FINDING — T0(b) TFD vs SCF: one functional, two languages, and the map between them (session 9)
Data: step3B_fixed.jsonl (TFD, repaired floor) vs step3_hfs.jsonl (SCF), 630 (Z,shell) pairs, Z 3–108.
P5 HOLDS on the stated criterion (|mean|/sd = 0.41 over 630) but is MARGINAL per shell and ONE-SIGNED:
   SCF deeper than TFD in every shell (s −0.03, p −0.07, d −0.08, f −0.09 Ha). A bias, not a centred noise.
P6 FAILS as framed. E_SCF − E_TFD is NOT an oscillation about zero. It is a STEP keyed to occupancy:
   3d −0.04 Ha (Z ≤ 19) → −0.20 (Ca) → −0.40 (Sc), i.e. it switches on at collapse onset and then grows
   with the shell's electron count (Mn d5 −0.16, Fe d6 −0.27; Gd f7 −0.53, Tb f8 −0.65; Cm f7 −0.51,
   Bk f8 −0.64: ≈ −0.10 Ha per added d electron, ≈ −0.12 per f). TFD tracks the pre-collapse branch.
P7 not reached (depends on P6).
Class decomposition (T0b_classdecomp.txt): at 9 of 10 class steps the SCF−TFD gap growth is carried by the
   ENTRANT's own residual (0.16–0.65 Ha), the runner moving 0.06–0.23. Os is the exception (5d LESS bound
   under SCF, +0.15; gap shrinks 0.55 → 0.36).
Reading (stated, not decided): the two kernels are the same E[ρ] (same nucleus, Hartree, Dirac exchange,
   Latter tail) differing only in the kinetic-energy language — T_TF[ρ] vs T_s[φ] — and the translation is
   NOT a mean over Z. It is the occupied-shell localisation term (Fermi 1928 / Griffin–Cowan–Andrew
   collapse), absent in TF (Lieb–Simon: TF is the smooth Z→∞ limit, no shells), present in SCF, and roughly
   linear in the shell's occupancy N. Because the SCF density is SPIN-AVERAGED it carries the average
   intra-shell repulsion of the N electrons but not the Hund exchange that singles out half-filling; that is
   why the pairing class survives in both kernels but the gap it must bridge is N-scale under SCF and
   one-electron scale under TFD. This is option (a) stated as a mechanism: the derivable penalty inside the
   SCF object is the whole-shell Hund term, and the linear residual is its measure.
Chosen constants: none. Nothing written to register/index/store.