# BRIDGE — THE LÖWDIN SESSION 6 (2026-08-15)
Successor to BRIDGE-LOWDIN-SESSION-5.md (read in full). Bank restore-point-2_13 (R 1700) UNCHANGED;
nothing written to register/index/store. Pack-5 verified 134/134, 0 hash mismatches. Context at handoff
~85%. Written under §H.10. Everything this session produced is in LOWDIN-PACK-6.tar.gz (MANIFEST-PACK-6.txt).

## 1 · M ruled this session, in order
1. Chapter 34 rewrite happens ONLY when the Löwdin solution is fully complete and closed without questions.
   Bridge-5 §3 item 2 is WITHDRAWN from the resumption order until then.
2. Find the five sequence misses from disk (done, §2).
3. Run the owed checks before asking for the closure ruling (done, §2).
4. **P must be DERIVABLE.** A two-sided corridor with a chosen constant does not close the four.
5. tfd.py / rad.py location: M does not know; project knowledge does not hold them (searched: only the
   13 files of CODE-LOWDIN-2_13.txt are extracted). They are in restore-point-2_13.tar.gz and LOWDIN-PACK-4.

## 2 · Done, all on pack-5 disk (step3_rows.jsonl, ground.py)
- **Attribution table** (ATTRIBUTION-TABLE-SESSION-6.md): 17 rows, 7 web searches. 8 STATED, 3 PARTLY,
  5 NOT FOUND, 1 mixed. Three corrections owed to the record: (a) R 1450 credited Belokolos 2017 for the
  period-two structure — Kitagawara & Barut 1983 J Phys B 16 3305 is prior by 34 yr; (b) Spectra
  Compendium's collapse coordinate is Schwarz 2010 JCE 87 444 Fig 1 in substance; (c) rule A's ion reading
  extends a known 4s/3d argument (Meek–Allen 2002 CPL 362, Vanquickenborne, Melrose–Scerri, Bills,
  Schwarz) — the 106-step TFD closed-core RULE is not found. Only rows 13–17 remain "first" candidates.
  Nearest prior to Step 3: Wong 1979 JCE 56 714 / ten Hoor 1986 IJQC 30 831 (TF as GLOBAL occupancy).
  Latter RM-1416-AEC: RAND page exposes no PDF; Phys Rev 99 510 paywalled. Still owed at source.
- **The five sequence misses** (SEQUENCE-MISSES-SESSION-6.md): four (Mn, Tc, Gd, Cm) are one class —
  entrant would pair into an exactly-half-full d5/f7 shell and goes to the runner-up instead. Ten steps
  in the walk have that form; six pair and hit (Fe, Ru, Tb, Os, Bk, Hs). Half-full alone is not the
  discriminant. In EA (closed core) no penalty corridor exists (constant or scaled: Helly-EMPTY). In EB
  (charge 1) constant P ∈ (0.125, 0.218) Ha or k|E| with k ∈ (0.437, 0.529) separates 10/10.
  Applied over 106: A 96 → 100, exactly the four move, opening sequence 17/17 unchanged; outside the
  corridor it degrades (99 at 0.12, 98 at 0.22). Leave-one-out over the class: 10/10.
  Physics: exchange lost on pairing into a half-filled shell (Hund) — owned, textbook. Structural reading:
  OPENINGS read at the closed core, PAIRING-AT-HALF read at charge 1. R 1449's class in the TFD frame.
  P status: CHOSEN inside a two-sided bound (§H.6). NOT closed under ruling 4.
- **Lr** (Z 103): 6d below 7p in both objects (EA 0.396, EB 0.181). Non-relativistic kernel; 7p1/2 spin-orbit
  is the known cause (Eliav 1995 PRL 74 1126; Sato 2015 Nature 520 209). Outside the kernel's domain,
  stated as such — the status f had for ν. Not a member of the pairing class.

## 3 · Next chat's work, in order
**T1 — DERIVE P.** Route: P_l = (2l+1)·J_H(nl); J_H from Slater F^k(nl,nl) of the ENTRANT shell in the
   CHARGE-1 object (rule B potential): d: (F^2+F^4)/14; f: (286F^2+195F^4+250F^6)/6435. Rebuild u(r) via
   eigen()/_shoot on tfd.potential(Z,1); normalise; F^k by double quadrature; ten species only.
   NEEDS tfd.py + rad.py (bank 2_13 or PACK-4) — first act: recover them, verify against the gate
   0.143/−0.010. Test it must pass (EB gaps, Ha): 3d (0.0108, 0.2978) · 4d (0.0262, 0.2245) ·
   4f (0.0569, 0.2180) · 5f (0.1250, 0.2145) · 5d < 0.3766 · 6d < 0.3261. 5f is the tight window;
   free-ion J_H(4f)~1.0 eV → 7 J_H ~7 eV would FAIL 4f (5.93 eV): the derivation can fail. Screening
   in the neutral is expected to lower F^k; the kernel decides. Owner: assistant.
   Fallback if kernel u(r) too crude for F^k: MEASURED F^k from spectroscopic term analyses, per species
   (outside search). Owner: assistant; M to rule on admissibility as MEASURED.
T2 — Then ask M the closure ruling again with the derived P in hand.
T3 — Lookups still owed outside: Ac III 6d–5f, Ra II nf (NIST), Latter's tables (source not reached);
   FLAG 1 Rb I / Y III in the measured grade. Owner: assistant.
T4 — Record: R 1701–1724 (Session 5 list) + this session's R 1725 attribution table · R 1726 K&B correction
   to R 1450 (append, §H.4) · R 1727 Schwarz attribution · R 1728 the pairing class and its corridors ·
   R 1729 M's derivability ruling · R 1730 Lr outside kernel · index write of COMPUTED-TFD as computed
   grade (R 1715 ruling), each write regenerating artefacts and both gates. Owner: writing chat.
Chapter 34: NOT until closure (ruling 1).

## 4 · Figures: MEASURED / CHOSEN / INHERITED (§H.6)
MEASURED: the ten EB/EA gaps (from pack-5 kernel); ground configs (NIST 5.12). CHOSEN: P and k inside
their corridors; the pairing-class definition (d/f exactly half-full at Z−1); Hs ground config is a
PREDICTION in ground.py, not a measurement, and is one of the six hits. INHERITED: everything in bridge-5 §2.

## 5 · Faults / flags (R 1671 shape)
- Sandbox network OFF this session; all outside search via web tools. Latter/RAND: no PDF exposed.
- tfd.py/rad.py absent from pack-5 and project knowledge; derivation blocked, not attempted by proxy.
- Bridge-5 flags stand: DIAG-QFINAL file set aside; Rb I / Y III FLAG 1; generic project files removal M's call.
- One echo I/O error in the sandbox during manifest write; retried clean, hashes verified.

## 6 · Files
LOWDIN-PACK-6.tar.gz: ATTRIBUTION-TABLE-SESSION-6.md · SEQUENCE-MISSES-SESSION-6.md · MANIFEST-PACK-6.txt.
Bring with LOWDIN-PACK-5 (has step3_rows.jsonl, ground.py, shoot.c, out/), BRIDGE-LOWDIN-SESSION-5.md,
LOWDIN-HANDOFF-4.md, LOWDIN-PACK-4 (for tfd.py/rad.py), CODE-LOWDIN-2_13.txt, COORDINATES-2_13.csv,
register, compendia. Unread inventory unchanged from bridge-5 (~380k words, ~4k read).
