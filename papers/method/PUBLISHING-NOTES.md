# How these papers reached the site

Written 2026-09-21 as a note of what publishing would need; rewritten 2026-09-24 when it was done.
This file is a note for the author, not part of any paper.

## 1. Two branches, and how the papers crossed

The papers were built on the book branch, `claude/book-repairs-corrections-zu5nmq`, which holds
the store, the volumes and the full history of the drafting, auditing and repair. The site lives
on `main`, and the two had diverged by 234 commits one way and 441 the other with no merge between
them. The papers crossed as a single addition: a branch off `main`,
`claude/papers-to-site-zu5nmq`, received `papers/method/` in one commit and the generator change
in a second, and `main` was fast-forwarded to it on the author's instruction of 2026-09-24. The
two branches remain otherwise unmerged. The book branch's copy of `papers/method/` is the record;
the site's copy is the one the site reads. A change to a paper is made on the site's branch and
carried back to the book branch by hand, or the other way, but is never made on one alone.

## 2. The generator carries the papers' figures

Before this pass the site's generator carried figures for papers from the store and replaced every
image in a research-tree paper with a placeholder. It now has the branch the papers needed: a
registry entry marked as carrying its own figures has each image resolved against the paper's
directory, copied to the site's data under the paper's slug, and its md5 measured at build, there
being no ledger row. The old branch of the handler still stands for a paper not so marked. The
selftest asserts the fourteen papers in order, that each of the ten carries every figure it cites
and its PDF with an md5, and that the guard measures zero book citations in each.

## 3. What a rebuild needs

The site's data is built with the research tree at a named commit of another branch
(`--warp-root`, `--warp-commit`), because one of the earlier papers on the shelf has its source
there and not on `main`. The data now on the site was built from that tree at `27dd39c`, the same
commit the shelf was last built from, so nothing but the build stamps and the papers moved. A
rebuild that omits the option drops that earlier paper to a slot and fails the selftest at a
check that predates this work.

## 4. The guard

The site refuses to ship any string that cites the unpublished books. `lint.py` in this directory
mirrors that guard's patterns and adds the paper contract's own, and every paper passed it before
it was offered for review. The generator's guard measured zero book citations in each at build,
and the name map carries each paper's path so the path the site prints resolves to the paper's
short name, never to a file name.
