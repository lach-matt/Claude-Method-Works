# PREDICTION — item (1)(c), s25. Written before any number was computed.
PK1 eps_KI(f) == DE_J within interpolation error (<=1e-4) on Cs and Sc.  -> HELD (1e-16).
PK2 resid_KI == resid_J: Cs -0.0019, Sc -0.0435; KI is degenerate with column J.  -> HELD.
PK3 non-degenerate variant requires screening alpha: chosen -> inadmissible; linear-response -> item (2).  -> structural, stands.
Harness fault (mine, not physics): first pass duplicated the f=1 endpoint -> nan gradient; corrected, rerun. Recorded.