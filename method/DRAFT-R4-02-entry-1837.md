# DRAFT R4-02 — register 1837, for review before it is seated

Ruling 12 of `RULINGS-R4f` (M, 6 September 2026: *"yes. continue"* on the two §35 sites), executed by
`method/r4-a2.py`, BUILD111 -> BUILD112 main. **Dry run passes; nothing is written.**

## The two volume substitutions, count-asserted

```
§35.2 L9797
OLD  the field.** There is no g block below Z = 121, and the table did not have to be
NEW  the field.** There is no g block through Z = 125, and the table did not have to be

§35.5 L9898
OLD  | **no g block below 121** | the pinned channels, -1/(2n^2) |
NEW  | **no g block through 125** | the pinned channels, -1/(2n^2) |
```

Each anchor unique in the whole bundle; after the pass the main volume carries no `below Z = 121` and no
`below 121` at all; **the reverse recovers `3d31d58491643d1c6fdee82b18200ad2` exactly.** BUILD112 would be
2,058,530 B, md5 `b4ba96c2693fda0fd97f08e79e6b4ad6`, 18,699 lines. Counts re-taken in the same build:
1,679 entries, 1 to 1837, mature 165-1837 at 1,515, kinds over 1,609, correction class 187 -> 188.

**Not touched:** §35.4 and Appendix D.5.9 name no bound; the four sibling sites outside §35 (the Löwdin
companion L13, L47, L114 and the Mathematical Compendium L3182) stand, and whether ruling 12's
generalising rule reaches them is the next question.

## The entry, as it would be seated


### 1837

**§35 SAID THERE IS NO G BLOCK BELOW Z = 121 BECAUSE THAT IS WHERE THE WALK STOPPED; CARRIED FORWARD AND RE-FITTED NOWHERE, IT SAYS 125.** *§35.2 and §35.5 print the absence as a bound at Z = 121, and the bound was the data's, not the law's: the listing of observed ground configurations ends at Z = 108 and the chain runs to Z = 120, so 121 was simply the first unwalked charge. Carrying* a *= 1.9840594 out of lawrencium and re-fitting it nowhere, the law walks seventeen further elements as prediction rather than description, and every row is labelled one: 6d at 109–112, 7p at 113–118, 8s at 119–120 —* **twelve of twelve blocks as the accepted table has them, and the law was fitted to none of them** *— with* a *never forced out of its corridor, no reset at all, and t running 0.0492 to 0.6791 (Z = 119 alone has no fraction, where 8s opens and nothing bounds it above).* **And the g block does not open, for a reason the form states exactly: a node-free subshell has p = 0, so ν = n and a drops out of it entirely. 5g sits at ν = 5 for ever while 7d at a = 1.98 sits at 3.03, so for 5g to win, a would have to fall below 1 — and a has risen monotonically since potassium. Through Z = 125 the law never makes a g subshell the entrant, and at 121 itself it is 7d that takes the step.** *Repaired at §35.2 and §35.5 as two guarded substitutions, each anchor asserted unique in the whole bundle before and after, the reverse recovering the predecessor's md5. The pinned-channel measurement register 1704 records — every g channel at −1/(2n²) to storage precision across a hundred protons — is untouched and is what the wider bound rests on; 1704 is append-only and is corrected by this entry rather than edited. §35.4's "the finding that there is no g block" and Appendix D.5.9's index row name no bound and are not touched. Four sites outside §35 print the Z = 121 bound — the Löwdin companion at three places and the Mathematical Compendium's pinned-channel theorem — and they are NOT repaired here; whether this ruling's rule reaches them is M's and stands open.* **M's ruling of 6 September 2026 (RULINGS-R4f, ruling 12): where two true statements differ only in reach, the volume takes the more expanded one.** Registers 1702; 1704; 1712. (a correction.)
