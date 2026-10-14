# Comment on ICRP Publication 23, "Report of the Task Group on Reference Man" (W. S. Snyder, M. J. Cook, E. S. Nasset, L. R. Karhausen, G. P. Howells and I. H. Tipton; Pergamon, 1975)

*Draft, DOCKET 67 step 3 (one comment per source). Kept in the repository. Not sent or posted anywhere.*

## Version read

- **Not an arXiv source.** What was read is a text layer, not the printed page:
  - **Chapter 2 (pp. 273-334)** was read as the **OCR text layer** of a .docx that M supplied: Drive file 16DVXUYgP--2YmXOP4VaAguXyIY_rWqM9, 79,841 bytes, md5 09a25adf33de8b2997bf9e355a115746. The copy read is held in the session scratchpad (`d67/reaudit2/icrp23_p273-334.docx`), not in the repository; the repository's `reaudit2/` holds the scripts and records made from it.
  - The .docx contains no page images. Its text layer is its only content.
  - Table 110 (pp. 327-328), the Table 109 total (p. 327), the Chapter 2 introduction (p. 273) and the notes for Table 108 (pp. 274-288) read cleanly. Table 108 itself (pp. 289-324) is not readable in this layer.
  - The front matter to p. 61 was read by an earlier re-audit.
- **The route to the printed PDF was refused.** The publisher's PDF (sagepub) was refused by the network proxy (HTTP 403). It also exceeds the 20 MB limit of the alphaXiv reader. It was not obtained by any other route.
- The drafting pass did not re-read the source. The verification pass (2026-10-04) re-opened the same .docx (md5 unchanged) and re-read its text layer at the Table 110 rows for Na and Cl (p. 327), the Chapter 2 introduction (p. 273) and the chlorine note for Table 108 (p. 287). Both findings read there as stated below.

## Summary

The ICRP 23 values our work relies on are confirmed in the text layer: the 70 kg Reference Man, the Table 110 masses of the eleven bulk elements and ten trace elements we use, and the two-significant-figure rounding rule. No ICRP 23 value is contradicted by any computation here. We record two small **discrepancies** in Chapter 2: one table cell whose per-cent figure does not match its mass, and a table numbering in the introduction that is off by one. The first may be an OCR misreading, which cannot be settled without the page image.

## Findings

### Table 110 (p. 327): the per-cent cell for chlorine (discrepancy, possibly OCR)

- **The source states** (Table 110, "Reference Man: total body content for some elements", p. 327), as the text layer reads it: Cl, **95 g**, **0.12 %** of body weight.
- **What we find:**
  - 95/70,000 = **0.136 %**, which rounds to 0.14 at the table's precision. The neighbouring row bears this out: Na, 100 g (0.143 %), is printed 0.14.
  - The other 33 rows that carry a per-cent entry agree with their grams to the printed precision.
  - The 95 g is consistent with the notes for Table 108 (p. 287). They cite Moore et al.'s estimate of 98 g of exchangeable chloride in a 70-kg man, "approximately the same value as the sum of the chlorine content of individual organs", and Cotlove and Hogben's 84-94 g.
  - So the per-cent cell is the one that disagrees. Whether this is a misprint or a misreading by the OCR cannot be settled without the page image.
- **Shown by:** `research/warp-drive/docket67-raw/reaudit2/icrp-23-reference-man.py` and `.out` ("rows with a per-cent entry: 34; inconsistent: [('Cl', 95, '0.12', 0.1357…)]"; "PASS the only gram/per-cent disagreement is Cl"); `reaudit2/icrp-23-reference-man.json`, `hypothesis_drift` ("SOURCE OR OCR DISCREPANCY"). The chlorine note's page, p. 287 rather than p. 288, is a correction recorded in `reaudit2/VERDICTS.json` ("the chlorine note … is on p.287, not p.288") and confirmed in the verification re-read.
- **Class:** discrepancy (a misprint or an OCR misreading).

### Chapter 2 introduction (p. 273): table numbering (discrepancy)

- **The source states** (p. 273, as read): "Table 108 summarizes the weights … Table 109 summarizes the elemental content".
- **What we find:** the tables themselves put the weights in Table 109 (with the total body at 70,000 g, p. 327) and the total-body element contents in Table 110 (pp. 327-328). Table 108 is the tissue-by-tissue element table. The introduction's numbering is one lower than the tables'.
- **Shown by:** `reaudit2/icrp-reference-adult-and-ci-chondrite.json`, `hypothesis_drift` ("SOURCE DISCREPANCY, not owner's"); `reaudit2/VERDICTS.json`.
- **Class:** discrepancy.

## What stands

- **Reference Man.** The 70 kg reference adult male: Table 109's total body of 70,000 g, and the p. 274 note that the asterisked weights sum to 70 kg.
- **Table 110's masses.** All 11 bulk-element masses the tree uses (O 43,000; C 16,000; H 7,000; N 1,800; Ca 1,000; P 780; K 140; S 140; Na 100; Cl 95; Mg 19 g) and ten trace masses agree exactly with Table 110. Cl 95 g is consistent with the p. 287 note.
- **The rounding rule.** All values are rounded to two significant figures, with four exceptions (p. 273).
- **No ICRP 23 value is contradicted.**

## Scope

These findings concern the OCR text layer of ICRP Publication 23, Chapter 2, in the copy named above. Nothing here is a statement about the printed page, which has not been seen.
