# papers/ — independent application papers

Formal research papers prepared for publication. **Not** part of the method volumes and **not**
members of either live bundle: `method/` and `drive/` are resource material for this tree and are
never written to by it.

The shape follows the standing architectural ruling recorded at `PROSE-ONLY.tsv` PO-0233:

> All exploratory applications, such as cold fusion, should be restructured as independent papers
> that utilise my lattice, and placed post reference page of the main paper as Appendixes, no longer
> taking any part in the subject matter of the main paper. … Each exploratory application should have
> its own abstract tying it to the main paper subject, and its own list of references.

So each paper here carries **its own abstract and its own references**, states its relation to the
lattice, and asserts nothing about the main paper's subject matter.

| file | what it is |
|---|---|
| **`Cold_Fusion_Proof_v1.0.src.md`** | **The proof paper.** What the project originally set out to do, and nothing else: a structural definition of cold fusion, the two uniqueness theorems (the binder, and the fuel), the eighth condition, the measured production floor, the balance stated at the acceptance actually delivered, and the procedure that would witness the configuration. It prices no blanket and no co-product, and it says so. 25 audits pass, `verify_paper.py` passes all three passes. |
| **`Cold_Fusion_v1.0.src.md`** | **The drafted paper, and the one to read.** A single publication consolidating the three working documents below and answering the project's three directives in order: prove the reaction, identify the materials, lay out the procedure. **Its prose states no number of its own** — it carries `[[Cnnn]]` citations, which `tools/render_paper.py` resolves against `CLAIMS.tsv` at render time, so pass 3 of the publication standard is true by construction rather than by care. Rendered to Markdown, HTML, `.docx` and PDF in `papers/out/`, all four from that one source. Audited by `tools/audit_paper.py` against the twenty-five audits The Method runs over its own volumes — see `docs/AUDIT-PAPER.md`. |
| `out/` | the rendered artefacts. **Generated — never hand-edit them**; edit the source and re-render. |
| **`Cold_Fusion_Binder_Economy_v1.0.md`** | **A working paper**, and the largest of the three the draft consolidates. Supersedes and retires the three retired below. Definition, the seven conditions, the unique realisation, the eighth condition that decides net energy, the two routes to a positive balance, and §10 — the laboratory programme, four staged measurements on apparatus that exists. |
| **`Cold_Fusion_Specification_and_Procedure_v1.0.md`** | **The executable half.** The reaction specified to the last free parameter, a bill of materials in two columns (a bench demonstration and a reactor-scale target), and the laboratory procedure that witnesses it — with what it returns and what it cannot stated before anything else. |
| **`Independent_Reconciliation_v1.0.md`** | **Its companion**, and a paper in its own right. Sets the work above beside four independent results published while it was being done: an independent derivation of condition 8, an independent proposal of the same fission-breeding escape, an independent pricing of the stripping route, and an optimised production target. Reports three corrections, one of them to the companion's own service-life model. |
| `CLAIMS.tsv` | The claims ledger: every quantity the current paper states, with status, provenance and its verifying computation. |
| `Muon_Catalysed_Fusion_v1.1.md` *(retired)* | The muon-catalysed fusion paper. Supersedes `recovered/Muon_Catalysed_Fusion_v1.0.md` (1 Aug 2026). Revises §3.2, §4 and §5; §§1–2, 3.1, 3.3–3.6 and 6 stand. |
| `Corrigendum_MuCF_v1_0.md` *(retired)* | The seven corrections to v1.0, as a standalone formal corrigendum. |
| `Muon_Collection_Budget_v1.0.md` *(retired)* | The per-stage collection budget the companion's §5.5 names as its deciding open item. Built from published MuSIC, Mu2e, COMET and PSI figures. |

## Provenance and status

`recovered/Muon_Catalysed_Fusion_v1.0.md` is a **generated** file — extracted byte-exact from the
chat export by `tools/recover.py`, md5-pinned in `recovered/LEDGER.tsv` under status
`RECOVERED-BY-WRITE`. It is therefore **never hand-edited**, and v1.1 is issued here as a new
document rather than as an edit to it. v1.0 remains in `recovered/` exactly as extracted.

Six of the seven corrections were not derived here. They come from the chat export — conversation
`transitions` (2026-08), messages 578–594 — and were banked in no file of this repository before
`docs/MUCF-ENERGY-AXIS.md`. That document is the working record with re-verification commands;
`Corrigendum_MuCF_v1_0.md` is the publishable form of the same delta.

**Docket C-8 is not closed by this tree.** It records that *Muon-Catalysed Fusion* is cited at
References R.3 of the main bundle and is not a member of either bundle, leaving three of its
companion-side claims unmeasurable by the book's own audits. Closing it requires seating a member,
which would write to `method/`. These papers deliberately do not.

## Reproducing the figures

`python3 tools/mucf.py --selftest` — asserts v1.0's Table 5.1, its three breakeven thresholds, and
every figure in the corrigendum. Stdlib only. See `docs/MUCF-ENERGY-AXIS.md`.

`python3 tools/collector.py --selftest` — asserts each published figure in the budget paper against
its recomputation, and reports the one 5 % rounding divergence in a source rather than silencing it.
`--machines` prints what machines actually cost per muon; the default report prints the budget and
the 15.3 % allocation. Stdlib only.

**A note on the budget paper's status.** It corrects the companion's own §4: the 5 GeV per muon at
which the energy balance prices its binder is aspirational, not achieved, and the best published
figure is 5 TeV per stopped μ⁻. v1.1 carries that correction at §4.2, in its abstract, in its
provenance and as item 7 of its correction list. The algebra of the balance is unaffected; its
reference point is not.

## The publication standard, and how it is enforced

> Stripped of the prose, all underlying math, claims and subject matter must be true and proved. The
> prose is a translation of the underlying subject matter. It must not state anything that
> contradicts the underlying math or claims. It must itself be true, and verifiable by the math we
> provide in the paper.

`tools/verify_paper.py` enforces that mechanically, in three passes: it **recomputes** every `DERIVED`
row of `CLAIMS.tsv` from the instruments; it **binds** every row naming an instrument constant to that
constant as the source actually holds it; and it **scans the prose**, failing on any number no ledger
row carries. The third pass is the one that does the work — a sentence cannot quietly acquire a figure
the mathematics does not produce. **Pass 3 reads the tables too.** It did not at first — it stripped
markdown table rows as "structure" — and since most of the paper's quantities live in tables, that
left the standard's main pass checking the sentences around the numbers rather than the numbers.
Five figures had been standing unbacked when the exemption was removed; all five now carry rows.

    python3 tools/verify_paper.py papers/Cold_Fusion_Binder_Economy_v1.0.md \
                                 papers/Cold_Fusion_Specification_and_Procedure_v1.0.md \
                                 papers/Independent_Reconciliation_v1.0.md

**One ledger governs both current papers.** They were split for readability, not into separate
evidence bases: `CLAIMS.tsv` carries every quantity either states, and each paper must pass all three
passes on its own. The retired documents carry withdrawn figures by design and will fail pass 3; that
is the correct result, not a regression.

What it does **not** do: check that a `MEASURED` or `SOURCED` value is true in the world — that is the
citation's job — and it does not read English. Its guarantee is narrower and worth having: every
quantity in the prose is one the mathematics produces, at the value it produces.
