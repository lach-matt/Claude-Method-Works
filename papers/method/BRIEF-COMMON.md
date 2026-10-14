# Common brief for every paper-drafting agent

You are drafting one research paper for a public website, from a set of unpublished books by
Matthew Lach ("M"). Read, in this order, before writing anything:

1. `/home/user/Claude-Method-Works/papers/method/PAPER-SPEC.md` — the contract. Every rule in it binds.
2. `/home/user/Claude-Method-Works/research/warp-drive/paper/THE-HIERARCHY-LAW.md` — the model paper
   (its §0, §1, §10 and status words). Match its register and its precision.
3. `/home/user/Claude-Method-Works/research/warp-drive/PROOF-ASSISTANT.md`, then `prover.py` and
   `machinecheck.py` beside it — the Z3 harness and how an obligation, its guards and its box are
   stated. `proofs.py` there is the exact-arithmetic prover for algebraic identities (Fraction and
   grid-above-degree); use its method for every identity.
4. The source passages named in your paper's brief, IN FULL, with `sed -n A,Bp` on the volume file.
   Read and comprehend the material; do not identify results or errors by pattern. Where a passage
   cites another section, follow it. Where a later passage or a correction in the record supersedes
   an earlier one, the later governs and you say so in SOURCES.md.

The six volumes are under `/home/user/Claude-Method-Works/method/members/`:
`The_Method_1_6-2.md` (the main volume, chapters; the heading map is `grep -nE '^#{1,3} '`),
`The_Method_1_6___Mathematical_Compendium-2.md`, `The_Method_1_6___The_Physics_Compendium-2.md`,
`The_Method_1_6___Spectra_Compendium-2.md`, `The_Method_1_6___The_Index_of_Indices-2.md`,
`The_Method_1_6___The_Register-2.md` (the record of every finding by number: `grep -n '^### N'`
finds entry N; read an entry when a passage cites it).

Environment: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH` puts Python 3.12 first;
z3, numpy and matplotlib are installed. Prefix long commands with `timeout 280`. Use absolute paths.

Hard rules:
- Write only inside your paper's directory. Never edit anything under `method/`, `drive/`, `tools/`,
  `recovered/`, `extracted/`, `research/`, or another paper's directory.
- `check.py` imports instruments by path (`importlib.util.spec_from_file_location`); it never copies
  their code. Reference implementations for the guard may be written fresh (that is the point of an
  independent implementation) but the object under test is the seated one.
- Every number in the paper is produced by `check.py` or is CITED. If the source's figure does not
  reproduce, the paper prints the reproduced figure and SOURCES.md records both; you never adjust a
  check to match a text.
- The published text carries no reference to the books, their chapters, registers, builds, scripts,
  files, working record or process — see PAPER-SPEC.md §8. Run `python3 papers/method/lint.py <dir>`
  until it is clean.
- Proofs are complete. A step you cannot justify is a gap you report, not a sentence you smooth over.
- Figures: prefer the audited plates listed in `/home/user/Claude-Method-Works/method/PROOF-FIGURES.tsv`
  (copy the `source_file` into `figures/`, record path and md5 in FIGURES.tsv); compute new ones with
  `figures.py` from the data `check.py` verifies. Caption numbers are in `check.py`.
- Finish with: `python3 check.py` clean, `python3 check.py --selftest` clean (negative control
  refuted), `lint.py` clean, `python3 papers/method/render.py <dir>` producing the PDF.

Your final message is a report, not the paper: the paper's title and section list, the count of
obligations by status (PROVED / MACHINE-CHECKED with boxes / EXHAUSTIVE with families / SAMPLED /
CITED), the figures used and their provenance, lint and render results, and — most important —
every claim of the source you could NOT reproduce or prove, stated plainly, and every place where
you had to choose an interpretation.
