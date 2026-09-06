#!/usr/bin/env python3
# RULING 62's SUBSTITUTION — design per site under RULING 61.
# Anchors are EXTRACTED from the Register by regex and never transcribed.
# Branch A: a readable body exists in Part VI  -> point at its section.
# Branch B: no body exists in the works        -> name the object (Ruling 61's own fallback).
import re, sys

REG = 'The_Method_1_6___The_Register-2.md'

XR  = "the Spectra Compendium's \u00a7 *The X-ray transition energies*"
LAD = "the Spectra Compendium's Part VI \u00a7 *The isoelectronic ladder*"   # Part III shares the name
LEV = "the Spectra Compendium's \u00a7 *The two level tables*"
NUC = "the Spectra Compendium's \u00a7 *The nuclear supply*"
IEN = "the Spectra Compendium's \u00a7 *The ionisation energies of the neutral atoms*"
QDF = "the Spectra Compendium's \u00a7 *The quantum defects of the light ladders*"
STG = "the Spectra Compendium's \u00a7 *The staged cells*"

# (line, regex on that line, replacement)
SPEC = [
 (5082, r"`XRAY-L3M5\.tsv` is now held:",
        "The L\u03b1\u2081 rows set out in " + XR + " are now held:"),
 (5090, r"`captures/XRAY-L3M4\.tsv` is held, 78 rows Ca to Fm\.",
        "The L\u03b1\u2082 rows set out in " + XR + " are held, 78 rows Ca to Fm."),
 (5090, r"in writing `XRAY-L3M5\.tsv` I COPIED",
        "in writing the L\u03b1\u2081 rows I COPIED"),
 (5094, r"XRAY-L3M1\.tsv at 88 rows \([^)]*\), XRAY-L3M4\.tsv at 78 \([^)]*\), XRAY-L3M5\.tsv at 78 \([^)]*\), XRAY-L2M1\.tsv at 88 \([^)]*\) and XRAY-L2M4\.tsv at 78 \([^)]*\)",
        "L\u2113 at 88 rows, L\u03b1\u2082 at 78, L\u03b1\u2081 at 78, L\u03b7 at 88 and L\u03b2\u2081 at 78 \u2014 the first three among the six transitions set out in " + XR + ", the last two held but not carried into that supply"),
 (5098, r"`XRAY-L1N2\.tsv` \([^)]*\) and `XRAY-L1N3\.tsv` \([^)]*\) are held",
        "The L\u03b3\u2082 rows (67) and the L\u03b3\u2083 rows (65), set out in " + XR + ", are held"),
 (5202, r"the six isotope anchors held in `XRAY-KL3\.tsv`",
        "the six isotope anchors held in the K\u03b1\u2081 rows set out in " + XR),

 (5106, r"`captures/LADDER-K-Kr\.tsv` is held: 495 rows",
        "The K\u2013Kr ladder set out in " + LAD + " is held: 495 rows"),
 (5134, r"match `LADDER-K-Kr\.tsv` \u2014 captured hours earlier",
        "match the K\u2013Kr ladder set out in " + LAD + " \u2014 captured hours earlier"),
 (5138, r"agrees with the held `LADDER-K-Kr\.tsv` to 4e-09 eV",
        "agrees with the held K\u2013Kr ladder set out in " + LAD + " to 4e-09 eV"),
 (5138, r"CORRECTED AND HELD AS `captures/LEVELS-K-I\.tsv`, with the corrected row flagged",
        "CORRECTED AND HELD AS a K I level table of its own, with the corrected row flagged"),
 (5334, r"form that produced `LADDER-K-Kr\.tsv`'s 495 multi-charge rows",
        "form that produced the 495 multi-charge rows of the K\u2013Kr ladder set out in " + LAD),
 (5326, r"`LADDER-H-Ar-I-III\.tsv` in the working root and 100\+ level files in `spectra_raw/`",
        "the H\u2013Ar ladder now set out in " + LAD + ", and 100+ level tables besides"),
 (5338, r"`LADDER-H-Ar-I-III\.tsv` \u2014 51 rows, hydrogen through argon at charges 0, \+1 and \+2 \u2014 SITS IN THE WORKING ROOT AND HAS ALL SESSION",
        "THE H\u2013Ar LADDER \u2014 51 rows, hydrogen through argon at charges 0, +1 and +2, set out in " + LAD + " \u2014 HAS BEEN HELD ALL SESSION"),

 (5142, r"Held as `captures/LEVELS-Fe-I\.tsv` with the ionisation potential excluded",
        "Held as the Fe I level table set out in " + LEV + ", with the ionisation potential excluded"),
 (5146, r"Held as `captures/LEVELS-Kr-I\.tsv` with those two rows marked DISPUTED in the file",
        "Held as the Kr I level table set out in " + LEV + ", with those two rows marked DISPUTED"),
 (5198, r"written into `captures/LEVELS-Kr-I\.tsv` alongside both refuted values",
        "written into the Kr I level table set out in " + LEV + ", alongside both refuted values"),

 (5158, r"Held as `captures/AME2020-A9\.tsv` with the verification written into the file\.",
        "Held as the A = 9 isobar chain set out in " + NUC + ", with the verification written beside it."),
 (5174, r"But `AME2020-A9\.tsv` is marked SUPERSEDED",
        "But the A = 9 isobar chain set out in " + NUC + " is marked SUPERSEDED"),
 (5210, r"CAPTURED AS `RADII-actinide\.tsv`: 23 rows covering",
        "CAPTURED AS the measured actinide radii set out in " + NUC + ": 23 rows covering"),
 (5222, r"Held as `captures/RADII-Bk-Cf-PREDICTED\.tsv`, labelled PREDICTED NOT MEASURED in its first line, so no later session can mistake it for a capture",
        "Held as the predicted berkelium and californium radii set out in " + NUC + ", labelled PREDICTED NOT MEASURED in the first line, so no later session can mistake them for a capture"),

 (5330, r"Captured as `IE-neutral-all\.tsv` and cross-checked",
        "Captured as the neutral first ionisation energies set out in " + IEN + ", and cross-checked"),
 (5298, r"SIXTY-EIGHT CELLS CAPTURED as `QDEFECT-TOPbase\.tsv` \u2014 exactly the charge-edge extension",
        "SIXTY-EIGHT CELLS CAPTURED, set out in " + QDF + " \u2014 exactly the charge-edge extension"),

 (5531, r"captures/NEUTRALS-STAGING\.tsv holds 554 staged cells in the index's own schema",
        "the staged cells set out in " + STG + " hold 554 cells in the index's own schema"),
 (5603, r"R 1649 named `captures/NEUTRALS-STAGING\.tsv` as the source of the 554",
        "R 1649 named the staged cells \u2014 set out in " + STG + " \u2014 as the source of the 554"),
 (5603, r"`spectra_raw` and `MEASUREMENTS\.tsv` share NO species",
        "the queue2 level tables and the measurement store share NO species"),
 (5611, r"`phase4\.py` READS `MEASUREMENTS\.tsv`; nothing builds it\. The chain queue2 \u2192 `captures/NEUTRALS-STAGING\.tsv` \u2192 `MEASUREMENTS\.tsv` survives ONLY AS DATA \u2014 neither step's code is in the bank, and `NEUTRALS-STAGING\.tsv` is referenced nowhere in the tree but the register",
        "the measurement store is read but nothing builds it. The chain from the queue2 level tables through the staged cells to the measurement store survives ONLY AS DATA \u2014 neither step's code is in the bank, and the staged cells are named nowhere but the register. The staged cells are set out in " + STG + "; the measurement store is one of the two bodies that part records as not held"),
 (5575, r"MEASUREMENTS\.tsv is the repair: many measurements to one cell",
        "The measurement store is the repair: many measurements to one cell"),
 (5619, r"keys are duplicated in MEASUREMENTS\.tsv",
        "keys are duplicated in the measurement store"),
 (5635, r"MEASUREMENTS\.tsv has carried it exactly in `term` and `parent`",
        "the measurement store has carried it exactly in its term and parent columns"),
 (5639, r"The `mult` column of MEASUREMENTS\.tsv is hereby shown",
        "The mult column of the measurement store is hereby shown"),
 (5667, r"The authored MEASUREMENTS\.tsv is NOT rewritten",
        "The authored measurement store is NOT rewritten"),

 (1761, r"The rows are recovered to `SPECTRA-DATA\.tsv`, extracted once from the source that held them",
        "The rows are recovered to a store of their own, extracted once from the source that held them"),
 (5551, r"The held row in SPECTRA-DATA\.tsv reads Ga I",
        "The held row in the published-values store reads Ga I"),
]

def main():
    txt = open(REG, encoding='utf-8').read()
    L = txt.split('\n')
    pairs = []; bad = 0
    for ln, rx, rep in SPEC:
        line = L[ln-1]
        ms = list(re.finditer(rx, line))
        if len(ms) != 1:
            print('FAIL line %d: regex matched %d times' % (ln, len(ms))); bad += 1; continue
        a = ms[0].group(0)
        n = txt.count(a)
        if n != 1:
            print('FAIL line %d: anchor occurs %d times in file: %r' % (ln, n, a[:70])); bad += 1; continue
        if a == rep:
            print('FAIL line %d: replacement identical to anchor' % ln); bad += 1; continue
        if txt.count(rep) != 0:
            print('FAIL line %d: replacement already present' % ln); bad += 1; continue
        pairs.append((a, rep))
    print('sites specified: %d · pairs valid: %d · failures: %d' % (len(SPEC), len(pairs), bad))
    return pairs, bad

if __name__ == '__main__':
    pairs, bad = main()
    if bad == 0 and '--emit' in sys.argv:
        import json
        json.dump(pairs, open('/home/claude/work/r62_pairs.json', 'w'), ensure_ascii=False)
        print('emitted', len(pairs), 'pairs')
    sys.exit(1 if bad else 0)
