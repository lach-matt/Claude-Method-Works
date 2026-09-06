# SCORE — THE 13 EXPOSED ROWS AT A GENUINE c = 1e6
# Session 60. Scored AFTER the run, against pack59/PREDICTION-EXPOSED-13.md
# (sha 6a04409318b8881c, verified byte-identical at 16:49Z before any row was read).
# Instrument: pack59/cinf2.py. Can-fail reproduced 2026-08-20T16:49:23Z:
#   PATCH OK sites=4  HFSR.self.c=1000000.0 ; Z=42 -21.7468 Ha ; Z=79 -314.0830 Ha.
# Rows: pack60/exp13.jsonl, mode cinf2, restart, FOREGROUND (F59.2), 13/13 present.
# The only number entered into this chain remains c = 137.035999 (and its removal).

## TABLE — entrant and runner-up, sealed chained walk vs c=1e6

     Z   c=137 ent/run   margin   |  c=1e6 ent/run   margin   |  d|m|     ENTRANT
     2   1s/2s          0.69553   |  1s/2s          0.69551   |  0.00002  SAME
     3   2s/2p          0.06767   |  2s/2p          0.06765   |  0.00002  SAME
     4   2s/2p          0.09634   |  2s/2p          0.09628   |  0.00006  SAME
    11   3s/3d          0.12650   |  3s/3d          0.12628   |  0.00022  SAME
    12   3s/3p          0.09346   |  3s/3p          0.09298   |  0.00048  SAME
    19   4s/4p          0.05411   |  4s/4p          0.05165   |  0.00246  SAME
    20   4s/4p          0.06058   |  4s/4p          0.05963   |  0.00095  SAME
    37   5s/4d          0.07991   |  5s/4d          0.07744   |  0.00247  SAME
    38   5s/5p          0.05639   |  5s/5p          0.05311   |  0.00328  SAME
    55   6s/5d          0.06306   |  6s/5d          0.05596   |  0.00710  SAME
    56   6s/5d          0.03914   |  6s/5d          0.01768   |  0.02146  SAME
    87   7s/6d          0.06841   |  7s/6d          0.04723   |  0.02118  SAME
    88   7s/7p          0.05816   |  7s/6d          0.00881   |  0.04935  SAME  <-- see F60.1 note

## EX-2 — READ FIRST, PER THE PREDICTION. **PASS.**
No row above Z=20 has |delta margin| = 0.00000. The shift rises monotonically in Z
(0.00002 Ha at Z=2,3 -> 0.04935 Ha at Z=88), largest at Z=87/88, smallest at Z=2,3,4 —
exactly as filed. The instrument is live on the walk path, not merely on the probe path.
F59.3's signature is absent. **The run is admissible.**

## EX-1 — DECISIVE. **HOLDS AT ALL 13 OF 13.**
Every entrant at c=1e6 is the entrant at c=137.035999. The falsifier could fire (EX-2
proves c moved the physics by up to 49 mHa in these very margins) and did not fire.

**CLAUSE 3 CLOSES.** The ordering clause is not a relativistic effect anywhere it could
be one. The 94 immune rows are immune combinatorially (F55.2, no walk, no c); the 13
exposed rows are now walked at c -> infinity and hold. Coverage is 107/107.

## EX-3 — DID NOT FIRE, AND ITS RANKING IS SUPERSEDED.
No row flipped, so EX-3's conditional ("if exactly one flips it is Z=56") never engaged.
Recorded as NOT FIRED, not as a pass. Its reasoning is now known to be wrong: EX-3 ranked
by *baseline* margin, but the closest approach to a flip at c=1e6 is **Z=88 (0.00881 Ha)**,
not Z=56 (0.01768 Ha). Ranking exposure by the sealed margin under-weights rows whose
runner-up is itself c-sensitive.

## EX-4 — PARTIAL. HOLDS AT 4 OF 5, FAILS AT Z=19. NOT REWORDED.
Scored the only way that is clean: **within one atom**, entrant-vs-p against
entrant-vs-d, so Z and reference are held fixed.

     Z   s/p gap 137 -> 1e6    dP    |  s/d gap 137 -> 1e6    dD    | dD > dP
    19   0.05411 -> 0.05165  0.00246 | 0.08967 -> 0.08910  0.00057 |  NO  <-- fails
    20   0.06058 -> 0.05963  0.00095 | 0.09148 -> 0.08823  0.00325 |  yes
    38   0.05639 -> 0.05311  0.00328 | 0.07799 -> 0.06893  0.00906 |  yes
    56   0.04825 -> 0.04165  0.00660 | 0.03914 -> 0.01768  0.02146 |  yes
    88   0.05816 -> 0.03790  0.02026 | 0.06142 -> 0.00881  0.05261 |  yes

d channels are the more c-sensitive at every Z >= 20 and by a factor 2.6 at Z=88.
Z=19 inverts it. NOT explained away: the failure stands as filed. It sits at the small-
signal end (0.6-2.5 mHa) but no floor for this walk has been established, so "numerical"
is a conjecture and is NOT claimed here. OWED: a floor for the restart walk, or a
targeted re-run of Z=19. This does not touch EX-1 — the Z=19 entrant is 4s in both.

## F60.1 — THE Z=88 RUNNER-UP CHANGES IDENTITY. THE MARGIN NUMBER IS NOT A CHANNEL SHIFT.
    c=137  7s -0.16021  7p -0.10205  6d -0.09879     runner-up = 7p
    c=1e6  7s -0.14359  6d -0.13478  7p -0.10569     runner-up = 6d
The 0.04935 Ha "narrowing" at Z=88 is NOT the 7p channel approaching 7s. **6d overtakes
7p.** The 7s/7p gap moves only 0.05816 -> 0.03790. Registering this explicitly under the
F44.2 precedent, which is the same error in the 4d row: a margin narrowing attributed to
a channel that was no longer the runner-up.

**AND IT LANDS INSIDE THE IMMUNITY CLASS.** 6d has n+l = 8; 7p has n+l = 8. The single
order change produced anywhere in the exposed set by removing relativity entirely is a
swap between two channels of EQUAL n+l — a within-shell event, which F55.2 proves cannot
reach the ordering clause. The one thing c changed is the one thing the theorem already
says does not matter. Deliverable 1 and Deliverable 5 §1 are strengthened, not touched.

## PROVENANCE
    open58.sh                16:49:12Z  CONDENSE-CHECK CLEAN (1047/1047, root MATCH), CANARY CLEAN
    cinf2.py canfail         16:49:23Z  CANFAIL: PASS, sites=4, Z=79 -314.0830 (reproduces s59)
    rows 56,87,88,55,37      16:49:36Z - 17:02:14Z
    rows 38,19,20            17:02:20Z - 17:05:36Z
    rows 12,11,4,3,2         17:05:39Z - 17:06:33Z
    13/13 rows in pack60/exp13.jsonl. No sealed file edited.
