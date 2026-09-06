# REBUILD-BUILD184.md — how BUILD184 is rebuilt from Drive alone, with no upload by M

Written by chat 151-B, fourth segment — the one that empties DEF-143 item 11's order. **BUILD184 is not in Drive
as a single file**: a 6.0 MB bundle cannot be created through the Drive connector, which takes content inline
only. It does not need to be. BUILD184 is *bit-exactly determined* by BUILD183 — itself by BUILD182 +
BUILD183-PARTS, itself by BUILD181 + BUILD182-PARTS, itself by BUILD180 + BUILD181-PARTS, itself by BUILD179 +
BUILD180-PARTS, all in Materials — plus the fourteen parts in this folder.

**Every part below was uploaded by Claude and read back byte-for-byte against the copy that went into the build.**

## Inputs

| object | where | bytes | md5 |
|---|---|---|---|
| BUILD90 main | Materials, `1lJ9R3vqAz3TNriJOyxJIKJGh5HqwY7GH` | 1,983,081 | 49065309b0c4fe8e055f693aed295cca |
| BUILD183 compendia | rebuilt from BUILD182 + BUILD183-PARTS | 5,920,198 | d215c184aee08b884d8748fb6d79c0cb |
| W-193.md.part00 | this folder | 3,321 | 1e423a733542bf5028cd3be8fcf687d5 |
| W-193.md.part01 | this folder | 2,849 | 294a29e76d373c25f0bcbbf2be62e227 |
| DEF-151d.md.part00 | this folder | 3,733 | 225187ecdb0f1dd787d853512edfb3be |
| DEF-151d.md.part01 | this folder | 3,629 | a90bc17973b8486afbded658093368ff |
| DOCKET-151d.md | this folder | 3,279 | faa8cfa8e0408d4c009e599aa5b605ef |
| READ-28b2.md.part00 | this folder | 3,934 | 70c9a5f7581f5ed9d992ac11a349467e |
| READ-28b2.md.part01 | this folder | 3,877 | 82f8eeb34c1fc9a883b57967a38e3255 |
| CENSUS-CLOSURES-28b2.tsv | this folder | 1,510 | 564764a4e92f7b296389fa7818998c77 |
| r2-28b2.py.part00 | this folder | 4,298 | fa632f33e9bf73357727c9b1aad994df |
| r2-28b2.py.part01 | this folder | 4,332 | e6427b1f965dd16ee6073e0cb84fa667 |
| r2-28b2.py.part02 | this folder | 4,200 | b209d6bb825dcee8e9247a66099416a0 |
| r2-28b2.py.part03 | this folder | 4,227 | 5b637b22c430841c42081a0c85e28734 |
| REBUILD-BUILD184.md.part00 / .part01 | this folder | this file, split | — |

Reassemble before anything else, each `cat` in part order:
`W-193.md` (**6,170 B, `897c35cb924188a9e893a9140e1dc3c1`**), `DEF-151d.md` (**7,362 B,
`d3f69c52c55027b33e927c27381c5de1`**), `READ-28b2.md` (**7,811 B, `fe431b7c7cbb2961aa77e7d80dfb9e54`**).

**Every part here is under 4.4 KB, and that is deliberate.** BUILD183-PARTS recorded the reason: `base64Content`
removes the *transport* failure mode but not the *transcription* one, and at ~8–10 KB of base64 that segment
produced two wrong uploads in four attempts, both caught by the read-back byte count. Twelve of twelve went up
byte-exact once parts were capped near 5 KB, so this build caps them lower still and splits **every** close
member, not only the instrument. Each split is `split -n l/N` at line boundaries and each concatenation was
verified to reproduce its file exactly before any part was uploaded.

## Steps

0. Rebuild BUILD183 first, per REBUILD-BUILD183.md (and its chain back through 182, 181, 180) — **assert
   `d215c184aee08b884d8748fb6d79c0cb`.** Everything below is on top of it.
1. `cat r2-28b2.py.part00 r2-28b2.py.part01 r2-28b2.py.part02 r2-28b2.py.part03 > members/r2-28b2.py`
   — **assert 17,057 B, md5 `ccb9fc499e8d20e953936f472dab34b2`.** Stop if it differs.
2. Regenerate the golden: `gate.py bank r2-28b2`
   — **assert 14,026 B, md5 `553c84c9d548389da05c9aaf77ce243d`, 165 lines.** The instrument is deterministic (no
   wall clock, no randomness) and `gate.py run r2-28b2` reproduced this golden exactly in chat 151-B, so the
   output is carried as a derivation rather than as a transcription. Stop if it differs.
3. Put the reassembled `READ-28b2.md` and `CENSUS-CLOSURES-28b2.tsv` in `members/` unchanged.
4. Run the close, `--append` before `--members`:

```
python3 members/close.py \
  --old  The_Method_1_6_BUILD183_compendia_papers_audits.md \
  --new  The_Method_1_6_BUILD184_compendia_papers_audits.md \
  --w    W-193.md \
  --append DEFERRED.md DEF-151d.md \
  --append DOCKET.md   DOCKET-151d.md \
  --members members/r2-28b2.py members/r2-28b2.out members/READ-28b2.md members/CENSUS-CLOSURES-28b2.tsv
```

5. **Assert the result: 5,977,919 B, md5 `d4350094449e3a4bf488315e21199bd4`, 67,533 lines, 357 members.**
   `close.py`'s own reverse guard must also report that stripping the appended text recovers
   `d215c184aee08b884d8748fb6d79c0cb`. Any mismatch stops the chat with a report; nothing here is to be patched
   into agreement.

Expected inside the rebuilt bundle: MANIFEST.tsv 24,056 B / `11e2e43e938a21176e2c3bdfaed24902` / 359 lines (358
listed); WORKING-REGISTER.md 932,240 B / `84fc75211fb075369651ef5f3284fc4d` / 8,013 lines, 194 W entries ending
W-193; DEFERRED.md 417,777 B / `fb39f84dbf0b702174ec5acf27b74714` / 3,461 lines; DOCKET.md 64,938 B /
`0eddf7e5eeb0e4969c87786b0386ecbf` / 420 lines.

## Standing

**W-190's loop ruling governs and is unchanged:** a chat opens from Drive, works with Graphify as the substrate
for state and cross-check, and closes by writing only these small parts and the handoff back to Drive.

**The gate at this build:** GATE-ch151Bclose4, verdict PASS, run against a fresh re-extract of BUILD184 — census
byte-identical, `run --core` 5/5, MANIFEST OK 358 listed / 359 extracted, and **72 of 72 banked goldens
reproduce**, with every golden separately verified byte-identical to its copy in the bundle after the sweep.
§0a remains empty.

**What this build closes.** DEF-143 item 11's order of computable re-derivations is **empty**: nine families,
the last four in this chat (26b-02/-03, 27a-02, 28a-06, 28b-06). No new re-derivation is owed by item 11. What
the order now waits on is **R3's rulings** — 26c-02's three standing totals, 27a-02's disjoint sets, 28a-06's
figure, 28b-07's block scope — and the census rows left engaged and open (mc 387–672, mc 293).
