# Handoff: N1*, the counterpart theorem, and the response paper to Huneau and Luk (item 522)

The commission and its instructions are in `../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`.

- `MANIFEST.tsv`: every file of the proof (instruments, data, Lean, the record's write-ups, scratch), with bytes, md5,
  items, role and label, as of the handoff commit (first made at 522, brought forward at 524).
- `scratch/`: the working derivations behind items 517-520, with their own README. Not seated; the instruments in
  `../lemmas/` are authoritative.

Branch `claude/warp-drive-theory-ditjk4`. Find the handoff commit with
`git log -1 -- research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`.

To start the session, paste this as its first message:

> You are commissioned by M (item 522) to finish N1* and the five-dimensional counterpart of Huneau and Luk's
> theorem, then write a formal response paper to their theorem. Fetch branch `claude/warp-drive-theory-ditjk4` of
> `lach-matt/Claude-Method-Works`, base your own branch on it, and follow
> `research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md` exactly; every file of the proof is listed
> with its md5 in `research/warp-drive/docket68/handoff-n1star/MANIFEST.tsv`. Work inline, report, then pause.
