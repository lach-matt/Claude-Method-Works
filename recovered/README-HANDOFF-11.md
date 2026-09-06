# LOWDIN-HANDOFF-11 — single archive superseding HANDOFF-6 + PACK-7..PACK-11 (2026-08-16)
Contents: pack5, pack6, BRIDGE-LOWDIN-SESSION-5.md (= HANDOFF-6 verbatim) · pack7 · pack8 · pack9 · pack10 · pack11.
Each sub-pack keeps its own original MANIFEST (still verifiable in place). MANIFEST-HANDOFF-11.txt covers all files.
Latest bridge: pack11/BRIDGE-LOWDIN-SESSION-11.md. Bank restore-point-2_13 (R 1700) unchanged.
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/;
cp pack10/* rt/; cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c
Gate: python3 derive_P_fix.py; python3 derive_P2_fix10.py; python3 derive_P3_fix10.py; cmp derive_P3.json pack8/pack5fix/derive_P3_fix.json
Verify: while read h f; do [ "$(sha256sum "$f"|cut -c1-16)" = "$h" ] || echo MISMATCH $f; done < <(grep -v MANIFEST-HANDOFF-11 MANIFEST-HANDOFF-11.txt)