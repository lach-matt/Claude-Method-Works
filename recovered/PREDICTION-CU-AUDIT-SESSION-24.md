# PREDICTION — bridge-23 s3(1) Cu audit, session 24 (2026-08-16). Ruling: "continue in order" (M). Written BEFORE any run.
Object: t7c_corrz.py corr="Z", SIC_NOCLAMP=1 (standing). Cu row: EZ -0.3735, meas -0.3839, resid_Z +0.0104 (SHORT).
Audit read (no run): meas = IP(Cu I) + E(Cu II 3d9 4s 3D_3), the LOWEST J LEVEL of the hole term (served.tsv, s13).
TABLE-CHAIN-15 carries so/hund shift = 0 on every 3d row while 5d rows carry Lande SO and 4f rows carry SO + own-orbital Hund-II.
So the 3d rows are compared level-to-term-average without the term the 4f/5d rows receive. Two tests, both derivable, no constant:

## A. Lande SO on the Cu row (same object/method as t7c_so.py on 5d: zeta_3d from the converged TS potential, c = 137.035999)
Cu I 3d10 has no SO structure; the SO structure is in the ion hole (3d9 4s 3D, inverted, J=3 lowest). The removed electron is j=5/2
(l+1/2): eps_j = eps_avg + zeta*l/2 = eps_avg + zeta_3d. The chain average must be shifted SHALLOWER to compare with the J=3 level.
PC1: zeta_3d(Cu, TS potential) in [0.0030, 0.0045] Ha; shift = +zeta_3d; Cu resid_Z moves +0.0104 -> +0.013..+0.015. Cu stays SHORT.
PC2: the shift is of the same size as the recalled Cu II 3D interval (3D_3 sits ~720 cm-1 = 0.0033 Ha below the term centre;
     RECALLED-NOT-ENTERED, comparison only) to within a factor 1.4.
Consequence if PC1 holds: the SO term does NOT explain Cu's shortness; it worsens it. Same term applies to Ti (2D3/2 hole, +),
Cr (6D1/2, +), Ni (4F9/2 inverted, +); Ni additionally lacks a Hund-II term (4F vs quartet average) -- flagged, not run in this item.

## B. The named candidate: entrant-down channel SIC weight (t7c_cuaudit.py = t7c_corrz.py VERBATIM + env FENT; FENT=0.5 = standing)
Standing (PZ-81 fractional occupation): the entrant's SIC potential is built from f_ent*|phi_ent|^2 with f_ent = 1/2 (Slater/Janak TS).
Alternative tested: FENT=1.0 -- occupation-independent orbital SIC potential (unit-normalised orbital density in v_H and v_x).
PS0 (gate): FENT=0.5 reproduces t7c_corrz.jsonl EZ for Cu (-0.3735), Cs (-0.1428 = -0.1397-0.0031), Sc (-0.3211 = -0.2966-0.0245) to 1e-4.
PS1: FENT=1.0 deepens Cu by between -0.010 and -0.045 Ha (v_H scales x2, v_x scales x2^(1/3) on the direct term -0.0415 at f=1/2),
     landing Cu resid in [-0.035, 0.000]; predicted to OVERSHOOT (resid < -0.005), i.e. not a closure of Cu.
PS2: FENT=1.0 moves Cs (closed at +0.0003) by <= -0.003 -> Cs leaves the closed class. Class failure regardless of Cu.
PS3: FENT=1.0 moves Sc (over -0.0265) further over by >= 0.010.
Consequence: if PS2 holds, the alternative weight is REJECTED as a rule (it opens closed rows); Cu's shortness is not a weight artefact.
Thresholds chosen (stated): "closed" <= 0.003 Ha; "worsens" = |resid| grows by > 0.001.
Runs: Cu, Cs, Sc only (smallest first). One SCF each per FENT; ~15 s each; timeout 200; jsonl appended, resumable.
