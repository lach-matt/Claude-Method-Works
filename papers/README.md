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
| `Muon_Catalysed_Fusion_v1.1.md` | The muon-catalysed fusion paper. Supersedes `recovered/Muon_Catalysed_Fusion_v1.0.md` (1 Aug 2026). Revises §3.2, §4 and §5; §§1–2, 3.1, 3.3–3.6 and 6 stand. |
| `Corrigendum_MuCF_v1_0.md` | The seven corrections to v1.0, as a standalone formal corrigendum. |
| `Muon_Collection_Budget_v1.0.md` | The per-stage collection budget the companion's §5.5 names as its deciding open item. Built from published MuSIC, Mu2e, COMET and PSI figures. |

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
