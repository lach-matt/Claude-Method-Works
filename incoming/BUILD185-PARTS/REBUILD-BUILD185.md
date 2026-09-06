# REBUILD-BUILD185.md — how BUILD185 is rebuilt from Drive alone, with no upload by M

Written by chat 152. **BUILD185 is not in Drive as a single file**: a 6.0 MB bundle cannot be created through the
Drive connector, which takes content inline only. It does not need to be. BUILD185 is *bit-exactly determined* by
**BUILD184**, which M uploaded whole to Materials as `The_Method_1_6_BUILD184_compendia_papers_audits.md`
(fileId `1GcPBhK-zhPxC24K4HGxHhvMzq8DntdC2`, **5,977,919 B · md5 d4350094449e3a4bf488315e21199bd4**), plus the
thirteen parts in this folder. **No REBUILD chain is needed** — BUILD184 is fetched by fileId and asserted, and the
180→184 chain in BUILD180-PARTS … BUILD184-PARTS is now only a fallback if that md5 ever disagrees.

**Every part below was uploaded by Claude and read back byte-for-byte against the copy that went into the build.**

## Inputs

| object | where | bytes | md5 |
|---|---|---|---|
| BUILD90 main | Materials, `1lJ9R3vqAz3TNriJOyxJIKJGh5HqwY7GH` | 1,983,081 | 49065309b0c4fe8e055f693aed295cca |
| BUILD184 compendia | Materials, `1GcPBhK-zhPxC24K4HGxHhvMzq8DntdC2` | 5,977,919 | d4350094449e3a4bf488315e21199bd4 |
| W-194.md.part00 / .part01 | this folder | 4,635 / 3,838 | 8840da56… / 00f3b949… |
| DEF-152.md.part00 / .part01 | this folder | 3,361 / 3,066 | 9c08cad0… / 3b42ee68… |
| DOCKET-152.md.part00 / .part01 | this folder | 2,642 / 2,277 | c10e288c… / b55282d7… |
| READ-32a.md.part00 / .part01 / .part02 | this folder | 3,368 / 3,357 / 3,229 | ce77f192… / 4ed70514… / e1ca49e9… |
| CENSUS-CLOSURES-32a.tsv | this folder | 301 | f72818a3dc011cb6fa7ab383fd23b6c3 |
| r2-32a.py.part00 … .part04 | this folder | 4,474 / 4,510 / 4,449 / 4,563 / 4,364 | 06075416… / 8a7f7bdf… / 29b81acc… / 6275ebce… / 3d0974e2… |

Reassemble first, each `cat` in part order:
`W-194.md` (**8,473 B, `caffe734a4126504ea60c12816c7293b`**), `DEF-152.md` (**6,427 B,
`2b8a23f18b996c3cda6288b4f1c34e62`**), `DOCKET-152.md` (**4,919 B, `b8d3bf5876ffc73e1c5b71bf01406089`**),
`READ-32a.md` (**9,954 B, `7a36f9b4f0f32ef0546a821fa07e011b`**), `r2-32a.py` (**22,360 B,
`15a9047af4a637eb7bdb05d0ea982878`**, 306 lines).

Parts are capped near 4.6 KB and **every** close member is split, which is BUILD183-PARTS' standing structural fix:
`base64Content` removes the *transport* failure mode but not the *transcription* one, and at 8–10 KB of base64 that
segment produced two wrong uploads in four attempts. Each split is `split -n l/N` at line boundaries and every
concatenation was verified to reproduce its file exactly before any part was uploaded.

## Steps

0. **Fetch BUILD90 and BUILD184 by fileId and assert both md5s.** The Drive connector returns base64 that spills to
   a local file; decode with `validate=True`. Extract 359 members (2 + 357). **Assert MANIFEST.tsv 24,056 B /
   `11e2e43e938a21176e2c3bdfaed24902` / 359 lines and WORKING-REGISTER.md 932,240 B /
   `84fc75211fb075369651ef5f3284fc4d` / 8,013 lines** — if those two match, the extractor is byte-exact.
1. `cat r2-32a.py.part00 … .part04 > members/r2-32a.py` — **assert 22,360 B, md5
   `15a9047af4a637eb7bdb05d0ea982878`.** Stop if it differs.
2. Regenerate the golden: `gate.py bank r2-32a` — **assert 16,587 B, md5
   `0d5d75a2264ff50217db542a5baf28c6`, 179 lines.** The instrument is deterministic (no wall clock, no randomness)
   and `gate.py run r2-32a` reproduced this golden exactly in chat 152 both before and after the close, so the
   output is carried as a derivation rather than as a transcription. Stop if it differs.
   **`r2-32a.py` needs Prints & Proofs at `/home/claude/PP_The_Method_1_6.md`** — in Drive that file is titled
   **The Method 1.6.md** in *The Method Prints & Proofs* (folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, 738,550 B / `49900cf41f818ab789bb90fc596ac977` / 11,371 lines). It is not
   named PP_*, which is why a title search for `PP_The_Method` finds nothing.
3. Put the reassembled `READ-32a.md` and `CENSUS-CLOSURES-32a.tsv` in `members/` unchanged.
4. Run the close, `--append` before `--members`:

```
python3 members/close.py \
  --old The_Method_1_6_BUILD184_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD185_compendia_papers_audits.md \
  --w W-194.md \
  --append DEFERRED.md DEF-152.md \
  --append DOCKET.md DOCKET-152.md \
  --members members/r2-32a.py members/r2-32a.out members/READ-32a.md members/CENSUS-CLOSURES-32a.tsv
```

`close.py` asserts that the W text begins `### W-` **and ends with a blank line** — a single trailing newline is
not enough.

5. **Assert the result: 6,047,434 B, md5 `1a822dfe3dad7d87956275b90892e514`, 68,222 lines, 361 members.**
   `close.py`'s own reverse guard must also report that stripping the appended text recovers
   `d4350094449e3a4bf488315e21199bd4`. Any mismatch stops the chat with a report; nothing here is to be patched
   into agreement.

Expected inside the rebuilt bundle: MANIFEST.tsv 24,320 B / `f52043245cdb8ae8e79a34205243fb33` / 363 lines (362
listed); WORKING-REGISTER.md 940,713 B / `40afefa312c24f834828368f3a002b2b` / 8,031 lines, ending W-194;
DEFERRED.md 424,204 B / `9dfd12100fe3e6add5fb4b6dd9526929` / 3,475 lines; DOCKET.md 69,857 B /
`053be5575f4311cf305f459dbb1f3731` / 433 lines.

## The container this was built in, which is NOT the one earlier chats ran in

- **Default `python3` is 3.11**, under which `gate.py` and `r2-tools.py` do not parse (f-string backslash, legal
  only from 3.12). `/usr/bin/python3.12` and `3.13` exist. `gate.py` spawns children as the literal string
  `python3`, so running `gate.py` itself under 3.12 is not enough. **The fix touches no member:**
  `mkdir -p ~/bin; printf '#!/bin/sh\nexec /usr/bin/python3.12 "$@"\n' > ~/bin/python3; chmod +x ~/bin/python3`,
  then `export PATH=~/bin:$PATH` in **every** bash call — the environment does not persist between calls.
- **numpy, sympy, scipy and mpmath must be installed for 3.12** (`pip --break-system-packages`). `minmax` needs
  numpy; `r2-tb1` needs sympy.
- **`r2-ch20a` and `r2-ch26a` need `COORDINATES-2_13.csv` at `/mnt/project/`** (create the directory). It comes
  from the claude.ai Project's doc list via `project_read` — 10,912,381 B / `906d08be19630b6f824ec0164de11773` /
  104,833 lines; the Drive connector refuses it at its cap.
- **Bash calls time out at two minutes by default.** A batch containing `r2-ch23b` (214–249 s) or `r2-ch16b` (72–85
  s) needs an explicit longer timeout, and `gate.py run --all` is still not to be used (chat 151-B's silent kill).
- **`gate.py cert` exits 2 when any ERROR row is in the log, while still writing the file with `verdict PASS`.**
  The exit code is not the verdict; tally last-value-wins from the file.

## The gate at this build

**GATE-ch152close, 15:53 UTC, verdict PASS**, run against a fresh re-extract of BUILD185 — census byte-identical,
`run --core` 5/5, MANIFEST OK 362 listed / 363 extracted, **73 of 73 banked goldens OK on last value**, and every
one of the 73 verified byte-identical to its pre-close copy (the only difference being `r2-32a.out`, banked this
chat). §0a remains empty. The chat's opening gate was **GATE-ch152**, also PASS, at 72 of 72.

## Standing

**W-190's loop ruling governs and is unchanged:** a chat opens from Drive, works with Graphify as the substrate for
state and cross-check, and closes by writing only these small parts and the handoff back to Drive. Chat 152 re-ran
the GitHub probe the chat-151 handoff asked for; the private repo returned **404** again, the third consecutive new
session to do so after a re-consent. **The repository store-of-record ruling is not executable from Cowork and no
further session time goes to it.**

## What this build closes

**M's four rulings on the questions DEF-143 item 11's empty order was waiting on.** 26c-02 → **(c)**, a third state:
the origin of each of §32.1.4's three totals, executed here as `r2-32a.py`. 27a-02 → **(a)**. 28a-06 → **(a)**.
28b-07 → **(b)**. Rulings (a), (a) and (b) are seated for R3 in DEF-152 items 2–7 and are not executed here; the
chat-67 hold stands and no volume was edited. **No re-derivation is owed.** What remains is R3's execution of those
three rulings, the Register entries owed by DEF-152 items 1, 3, 5, 7, 8 and 9, and the two census bodies left
engaged and open — **mc 387–672 and mc 293**, untouched by this chat.
