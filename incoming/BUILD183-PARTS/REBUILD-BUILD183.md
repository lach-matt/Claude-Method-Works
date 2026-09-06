# REBUILD-BUILD183.md — how BUILD183 is rebuilt from Drive alone, with no upload by M

Written by chat 151-B, third segment. **BUILD183 is not in Drive as a single file**: a 5.9 MB bundle cannot be created
through the Drive connector, which takes content inline only. It does not need to be. BUILD183 is *bit-exactly
determined* by BUILD182 — itself determined by BUILD181 + BUILD182-PARTS, itself by BUILD180 + BUILD181-PARTS, itself
by BUILD179 + BUILD180-PARTS, all in Materials — plus the ten parts in this folder.

**Every part below was uploaded by Claude and read back byte-for-byte against the copy that went into the build.**

## Inputs

| object | where | bytes | md5 |
|---|---|---|---|
| BUILD90 main | Materials, `1lJ9R3vqAz3TNriJOyxJIKJGh5HqwY7GH` | 1,983,081 | 49065309b0c4fe8e055f693aed295cca |
| BUILD182 compendia | rebuilt from BUILD181 + BUILD182-PARTS | 5,864,276 | 27e66a61061cec78283c4a88d53ba964 |
| W-192.md | this folder | 6,023 | 334fddaa39b581adebe05ba1d506fae6 |
| DEF-151c.md.part00 | this folder | 4,471 | fb1c26c90a19732b5232f5f8bc7103d3 |
| DEF-151c.md.part01 | this folder | 3,183 | a8c153d2634b6cb74fcc509cae837a9c |
| DOCKET-151c.md | this folder | 3,460 | 2a89c78c9bd7eac36d0d58bca2f3d746 |
| READ-28a2.md.part00 | this folder | 3,895 | 0293fa426e0ca78d9e2ac9bcc1562480 |
| READ-28a2.md.part01 | this folder | 3,809 | 849700188593f71610960d05d0203bd6 |
| CENSUS-CLOSURES-28a2.tsv | this folder | 1,580 | df436792af39ac4dbbdb5177386659bc |
| r2-28a2.py.part00 | this folder | 5,652 | 860009249f0130fb2ace8136b6bf8b7e |
| r2-28a2.py.part01 | this folder | 5,541 | f56554f1e13ca830f2313eb249eaed11 |
| r2-28a2.py.part02 | this folder | 5,483 | 0f5939f574d525211819dbc0c8ae8d0e |

Reassemble before anything else: `cat DEF-151c.md.part00 DEF-151c.md.part01 > DEF-151c.md` (**7,654 B,
`18180c2e6e56ccad6ed41a5cc5b9bf01`**) and `cat READ-28a2.md.part00 READ-28a2.md.part01 > READ-28a2.md` (**7,704 B,
`c5f9f345c869d0915e57072876836503`**).

**Why more parts here, and the finding that produced them.** `base64Content` with `disableConversionToGoogleType: true`
removes the *transport* failure mode chat 150 measured under `textContent` (HTML entities for `&` and `<`, a dropped
blank line), and 17 of 17 parts went up byte-exact under it across this chat's first two closes. It does not remove the
*transcription* failure mode, which is mine: **at ~8 KB and ~10 KB of base64 this chat produced two wrong uploads in
four attempts — one truncated (205 B against 6,023) and one three bytes short — and the read-back byte count caught
both.** They were trashed and re-created; nothing wrong ever entered a build. The structural fix is the one already in
the standing note, applied a notch further: **keep every part near 5 KB**, which is ~7 KB of base64 and has not yet
failed. So the two markdown members over 7 KB are split as well as the instrument. Every split is `split -n l/N` at
line boundaries and every concatenation was verified to reproduce its file exactly before any part was uploaded.

## Steps

0. Rebuild BUILD182 first, per REBUILD-BUILD182.md (which itself begins from REBUILD-BUILD181.md, and that from
   REBUILD-BUILD180.md) — **assert `27e66a61061cec78283c4a88d53ba964`.** Everything below is on top of it.
1. `cat r2-28a2.py.part00 r2-28a2.py.part01 r2-28a2.py.part02 > members/r2-28a2.py`
   — **assert 16,676 B, md5 `c7eafbaf76e9ddc908a3cc8af1423a32`.** Stop if it differs.
2. Regenerate the golden: `gate.py bank r2-28a2`
   — **assert 12,319 B, md5 `ef7253ed5b38cf51fdda4e9be42408fd`, 184 lines.** The instrument is deterministic (no wall
   clock, no randomness) and `gate.py run r2-28a2` reproduced this golden exactly in chat 151-B, so the output is
   carried as a derivation rather than as a transcription. Stop if it differs.
3. Put the reassembled `READ-28a2.md` and `CENSUS-CLOSURES-28a2.tsv` in `members/` unchanged.
4. Run the close, `--append` before `--members`:

```
python3 members/close.py \
  --old  The_Method_1_6_BUILD182_compendia_papers_audits.md \
  --new  The_Method_1_6_BUILD183_compendia_papers_audits.md \
  --w    W-192.md \
  --append DEFERRED.md DEF-151c.md \
  --append DOCKET.md   DOCKET-151c.md \
  --members members/r2-28a2.py members/r2-28a2.out members/READ-28a2.md members/CENSUS-CLOSURES-28a2.tsv
```

5. **Assert the result: 5,920,198 B, md5 `d215c184aee08b884d8748fb6d79c0cb`, 66,990 lines, 353 members.** `close.py`'s own
   reverse guard must also report that stripping the appended text recovers `27e66a61061cec78283c4a88d53ba964`.
   Any mismatch stops the chat with a report; nothing here is to be patched into agreement.

Expected inside the rebuilt bundle: MANIFEST.tsv 23,788 B / `c505db2913ce09f269377b6ac9f8d6bb` / 355 lines (354 listed);
WORKING-REGISTER.md 926,070 B / `8ff5659a24408f56be6eec2b91bb2f9e` / 7,999 lines, 193 W entries ending W-192;
DEFERRED.md 410,415 B / `25b74fd0d01af60f275f2a9ed28f75d9` / 3,448 lines; DOCKET.md 61,659 B /
`a1c5b10c67d3084d5005de8993625e07` / 410 lines.

## Standing

**W-190's loop ruling governs and is unchanged:** a chat opens from Drive, works with Graphify as the substrate for
state and cross-check, and closes by writing only these small parts and the handoff back to Drive.

**The gate at this build:** GATE-ch151Bclose3, verdict PASS, run against a fresh re-extract of BUILD183 — census
byte-identical, `run --core` 5/5, MANIFEST OK 354 listed / 355 extracted, and **71 of 71 banked goldens reproduce**,
with every golden verified byte-identical to its copy in the bundle after the sweep. §0a remains empty.

Three gate mechanics worth carrying, all measured here. `gate.py census` refuses to run while
`/home/claude/DEFECT-CENSUS.tsv` or `members/__pycache__` exists and says so — remove both in a delete-only call first.
`gate.py manifest` needs `--comp <bundle>` as soon as more than one compendia bundle sits in `/home/claude`, which is
always true straight after a close. And `gate.py cert` prepends `GATE-ch` to the label it is given: pass `151Bclose3`,
not `ch151Bclose3` — a mis-labelled certificate cannot be overwritten and has to be written again under the right name.
