"""dzeta.py -- s33 PREDICTION-DZETA: entrant-weighted zeta-differential D = A - B of (bench - S) between the SIC one-orbital line (n_ent, zeta=1)
and the total-density line (n_tot, zeta_tot), on the corr='S' hole-state SCF. Bench RECALLED (rz_mech.bench), comparison only. Appends dzeta.jsonl. usage: Z ..."""
import sys,os,json,time,numpy as np
assert os.environ.get("SIC_NOCLAMP")=="1" and os.environ.get("SUBCELL")=="1"
from t7c_corrz import scf_sic_corr; from t5_scf import ground_occ,minus; import corr_sosex as CS
from rz_mech import SH,bench   # rz_mech's module body: it runs its loop over sys.argv -- guard below