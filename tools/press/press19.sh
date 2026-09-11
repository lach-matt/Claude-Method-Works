#!/bin/sh
# The Method 1.9 — the prose-pass print. Seven volumes, figures placed from
# method/PROOF-FIGURES.tsv (every plate read against its caption's own numbers).
# The volumes' own headings still read 1.6: 1.9 is the PRINT, not a new edition.
set -e
I="The Method 1.6 — print 1.9, for the prose pass<br>pressed 11 September 2026 from BUILD311"
sh press3.sh The_Method_1_6-2.md                                 main-1.9         "THE METHOD 1.6" 3 "$I" strip
sh press3.sh The_Method_1_6___The_Register-2.md                  register-1.9     "THE METHOD 1.6 — THE REGISTER" 3 "$I"
sh press3.sh The_Method_1_6___Mathematical_Compendium-2.md       mathematical-1.9 "THE METHOD 1.6 — MATHEMATICAL COMPENDIUM" 3 "$I"
sh press3.sh The_Method_1_6___The_Physics_Compendium-2.md        physics-1.9      "THE METHOD 1.6 — THE PHYSICS COMPENDIUM" 3 "$I"
sh press3.sh The_Method_1_6___Spectra_Compendium-2.md            spectra-1.9      "THE METHOD 1.6 — SPECTRA COMPENDIUM" 3 "$I"
sh press3.sh The_Method_1_6___The_Index_of_Indices-2.md          indices-1.9      "THE METHOD 1.6 — THE INDEX OF INDICES" 3 "$I"
sh press3.sh The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md threebody-1.9    "THE THREE-BODY PROBLEM FOR UNKNOWN MASSES" 3 "$I"
echo ALL DONE
