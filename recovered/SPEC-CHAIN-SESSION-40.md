# SPEC-CHAIN (s40, item 1) — THE SELF-DRIVING WALK. Written BEFORE any code is changed (R 1449).
M's ruling s40: the literature above Z=108 is a COMPARISON COLUMN, never an input. The entrant above 108 is chosen by the
ruling field itself. Source debt of s40 paid at proposal: Desclaux 1973 (ADNDT 12, 311, Z=1-120), Fricke/Greiner/Waber 1971
(Theor. Chim. Acta 21, 235), Pyykko 2011 (PCCP 13, 161, Z<=172), ADNDT 2016 (Z=121-138). ALL FOUR SUPPLY ENERGIES FOR AN
ASSUMED CONFIGURATION; where the assumption is stated it is Madelung ("following Hund rules and the Madelung prescription",
ADNDT 2016). Importing any of them hands the walk the ordering the walk exists to produce. REFUSED AS INPUT ON THAT GROUND,
not on a provenance-label ground. RECALLED-NOT-ENTERED, comparison only.

## 1 · What is wrong with the present drivers
nlwalk_hf.entrant(Z) and hf_chan.py both compute the entrant as ground.expand(Z) MINUS ground.expand(Z-1). Both therefore
require the OBSERVED record at two consecutive Z, and ground.py raises KeyError above 108. The removal walk has a second
defect already registered at s39 (FINDING-WALK-25): it can only see OCCUPIED channels, so on 8 of 12 rows the competitor
(n-1)d is empty and the score is vacuous. Both defects have one cause: THE DRIVER IS TOLD THE ANSWER AND THEN CHECKS IT.

## 2 · The operation, stated
    config(Z+1) = config(Z) + one electron in the channel c that minimises E_HF(config(Z) + c)
The reference is the PREVIOUS NEUTRAL, not ground(Z) minus an entrant. Nothing is read from the record at any step past
the seed. D_chain(c) = E_HF(config(Z) + c) - E_HF(config(Z)), negative = bound; the chosen c is argmin.
This is aufbau performed rather than assumed, and it is SPEC-WALK-32's "tree of mechanisms beginning at hydrogen".

## 3 · Seed. CHOSEN and declared: config(1) = 1s(1). Hydrogen, one electron, no configuration question exists.
The chain is then RECORD-FREE from Z=2 upward. The observed table is a comparison column at every Z<=108 and absent above.

## 4 · Candidate channel rule. CHOSEN (a cost bound, not physics) and declared:
    c = (n,l) with occ(c) < 2(2l+1), n <= N+1, 0 <= l <= min(n-1, 4), where N = max n occupied in config(Z).
N+1 admits a new shell (without it Ne could never reach 3s). l<=4 admits g and is the only limit; it is the Janet-120 g
question and is stated as a bound rather than assumed away. NO n+l ANYWHERE IN THE RULE — the candidate set is generated
from occupancy and the node condition alone. Pruning by "never observed" is REFUSED: it imports the record.

## 5 · Error propagation is not a defect of the instrument, it is the measurement
A chain has no reset. One wrong entrant changes every configuration above it. That is the honest form of the question and
the score must be reported as FIRST DIVERGENCE Z, not as a per-element tally, because after the first divergence the rows
are not independent tests. Two scores are reported: (a) chained, from the seed; (b) restarted at each Z from the observed
config(Z-1) where Z<=108, which IS a per-element test and is what hf_chan already does.

## 6 · Provenance labels — TWO classes above 108, not one (R 1426: check whether the limit is the subject's or the collection's)
  Z <= 108  OBSERVED        NIST ASD 5.12 (R 1306), comparison column
  Z 109-118 SYNTHESISED-UNMEASURED   element exists, IUPAC-named, ground configuration NOT measured; ground.py stops at 108
                                     because the COLLECTION stops, not the subject
  Z 119-120 PREDICTED-UNSYNTHESISED  admitted to the index at R 1656 on Janet's authority, bound text already written
Every chain output above 108 carries label PREDICTED-BY-FIELD and names its own reference config. No literature value is
written into any data file; comparison is done in the finding text only.

## 7 · Held
No terms, no SO, no correlation, no F^k scale, no intermediate coupling. CORR=False. Frozen avg-of-config as everywhere
else, bound still NOT measured (PV-3 still owed). No constant beyond c. Nothing written to register/index/store.
