# What publishing these papers to the site will need

Measured on 2026-09-21. This file is a note for the author, not part of any paper.

## 1. The papers are built on a different branch from the site

| | commits |
|---|---|
| on this branch, not on the site's branch | 234 |
| on the site's branch, not here | 441 |

The two lines of work diverged at a common ancestor and have not been merged since. The site, its
generator and the research tree live on the site's branch; the volumes, the store and these papers
live here. Nothing about that is broken — it is two lines of work — but the papers cannot appear on
the site until the two meet. That is a decision for the author, and there are two shapes it can take:
merge the branches, or cherry-pick `papers/method/` onto the site's branch as a single addition.
The second is smaller and touches nothing else.

## 2. The site's generator does not carry figures for papers from the research tree

The generator treats papers from the store and papers from the research tree differently. For a
store paper it resolves each image against the extracted tree, copies the file, and records its md5
against the ledger. For a research-tree paper it does neither: every image becomes the placeholder
text *[figure N: not carried]*, by construction.

These papers carry figures, and the figures are load-bearing. Publishing them as they are would put
that placeholder on the page wherever a figure belongs. The fix is small and local — give the
research-tree branch of the generator the same image handler the store branch has, sourcing each
file from the paper's own `figures/` directory and measuring its md5 at build, since these papers
have no ledger row. `FIGURES.tsv` in each paper directory carries what that handler needs.

## 3. Each paper is registered by four facts

The generator's registry of research-tree papers takes, per paper: its path, a slug for the URL, a
short name for the shelf, and an optional PDF to offer as a download. Ten new entries are needed.
The PDFs these papers render are the ones to offer.

## 4. The guard

The site refuses to ship any string that cites the unpublished books. `lint.py` in this directory
mirrors that guard's patterns and adds the paper contract's own, and every paper is required to pass
it before it is offered for review. The generator will re-apply its own guard at build; a paper that
passes `lint.py` should pass it, and if one does not, the generator's finding governs.
