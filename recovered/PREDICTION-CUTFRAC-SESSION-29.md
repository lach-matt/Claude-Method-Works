# PREDICTION — mechanism B for the class-row remainder: the chain-Z correlation's eps_c >= 0 cut (r_s > r_s*) removes correlation where a diffuse
# entrant lives. Written BEFORE any run.  s29. Test: cutfrac.py — one neutral SCF per class row (frachf HFCf, f=1, SUBCELL=1), then on the converged
# density: r_cut = outermost radius where eps_c[total] < 0; F_out = entrant charge beyond r_cut; F_self = entrant charge where eps_c[n_e] >= 0 (its own SIC
# density); required := meas - D_HF - so/hund (chain columns); delivered := DEc_sc / required (from frachf.jsonl). No new form, no constant.
Census in hand: delivered = Sc 0.93 · La 0.65 · Lu 0.62 · Y 0.61 · Cs 0.16 (Gd set aside: 4f-adjacent). Missing = 0.002 · 0.010 · 0.012 · 0.013 · 0.013.
PB1 F_out groups as Sc < {Y, La, Lu} < Cs, with Sc < 0.15 and Cs > 0.50; no ordering claimed inside the middle group.
PB2 (1 - delivered) has the same three-group order as F_out (Sc lowest, Cs highest): the cut fraction ranks the remainder.
PB3 F_self > F_out on every row (the entrant's own density is sparser than the total: its SIC piece is cut earlier), and F_self(Cs) > 0.8.
PB4 If B is the whole mechanism, missing/required is bounded above by F_out on every row (you cannot lose more than lives past the cut). A row with
    missing/required > F_out falsifies "B alone" and points to A (core-valence) for the excess.
Stop rule: six SCFs, one pass, no scan; failed predictions reported with mechanism; no alternative correlation form is tried (that would be a form choice, i.e. a ruling).