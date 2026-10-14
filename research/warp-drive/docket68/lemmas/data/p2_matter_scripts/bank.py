"""bank.py -- collect the item-221 runs into lemmas/data/p2_matter_rows.json (scratch -> repository, one direction)."""
import json, glob, os, hashlib
OUT = "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas/data/p2_matter_rows.json"
res = lambda f: [json.loads(l[7:]) for l in open(f) if l.startswith("RESULT ")]
cal = {"pbe0_def2": {}, "pbe_gth": {}}
for f in sorted(glob.glob("cal2_*.log")):
    o = res(f)[0]; cal["pbe0_def2"][o["el"]] = o
for f in sorted(glob.glob("calpbe_*.log")):
    r = res(f)
    if r: cal["pbe_gth"][r[0]["el"]] = r[0]
atoms = {}
for o in res("atoms_law.log"):
    atoms.setdefault(o["el"], {})["%g" % o["delta_eV"]] = o["states"]
mols = []
for f in sorted(glob.glob("m2_*.log")):
    r = res(f)
    if not r: continue
    o = r[0]
    keep = {k: o[k] for k in ("mol", "law", "delta_eV", "re", "we", "De_eV", "D0_eV", "fit_resid_meV", "spin_at_min", "Nd_fine",
                              "atom_ground_Nd", "atom_gap_eV", "coarse", "fine", "sec") if k in o}
    if "E_atoms" in o: keep["E_atoms_run"] = o["E_atoms"]; keep["atom_states_run"] = o["atom_states"]
    mols.append(keep)
sols, groups = [], {}
for f in sorted(glob.glob("s3_*.log")):                      # s3_<el>_<law>[_x].log: an _x file extends the scan
    r = res(f)
    if r:
        el, law = f[3:-4].split("_")[:2]
        groups.setdefault((el, law), []).extend(r)
for (el, law), r in sorted(groups.items()):
    sols.append(dict(el=el, law=law, delta_eV=r[0]["delta_eV"], nk=r[0]["nk"], nk_ibz=r[0]["nk_ibz"], sigma=r[0]["sigma"],
                     ke=r[0]["ke"], mesh=r[0]["mesh"], struct=r[0].get("struct", "fcc"), N_obs=r[0].get("N_obs", 10.0),
                     rows=sorted(({k: x[k] for k in ("a", "V_bohr3", "E", "E_raw", "conv", "cycles", "Nd", "mu", "eps_d_minus_EF_eV", "sec")}
                                  for x in r), key=lambda x: x["a"])))
branches = {f[3:-4]: res(f) for f in sorted(glob.glob("br_*.log"))}
follows = {f[3:-4]: res(f) for f in sorted(glob.glob("fw_*.log"))}
mx2 = [res(f)[0] for f in sorted(glob.glob("x2_*.log")) if res(f)]
bands = [x for f in sorted(glob.glob("bd_*.log")) for x in res(f)]
robust = {"note": "the law with Mulliken's d count in place of Lowdin's (LAW_KIND=mulliken): the same count on a free atom, so the same delta",
          "molecules": [res(f)[0] for f in sorted(glob.glob("mk_*.log")) if res(f)],
          "solids": {f[3:-4]: sorted(res(f), key=lambda x: x["a"]) for f in sorted(glob.glob("sk_*.log")) if res(f)}}
code = {n: hashlib.sha256(open(n, "rb").read()).hexdigest() for n in ("law.py", "mol.py", "run_mol2.py", "calibrate2.py", "atoms_law.py", "solid3.py", "branch.py", "mx2.py", "band.py", "follow.py", "bank.py")}
d = json.load(open(OUT)) if os.path.exists(OUT) else {}
earth = {"source": "McDonough W.F. (2003) Compositional Model for the Earth's Core, Treatise on Geochemistry vol. 2, ch. 2.15, Table 3 (bulk Earth; ppm by mass), read 2026-10-11 through the web connectors from https://www.mso.anu.edu.au/PSI/PSI_Meetings/Entries/2007/6/13_The_bulk_composition_of_the_Earth_(1)_files/Treatise%20on%20Geochemistry%202003%20McDonough.pdf",
         "status": "READ", "majors_ppm_note": "every Table 3 entry above 30 ppm, for the bulk Earth's mean atomic mass and Cr's atom fraction",
         "majors_ppm": {"H": 260, "C": 730, "O": 297000, "Na": 1800, "Mg": 154000, "Al": 15900, "Si": 161000, "P": 715, "S": 6350, "Cl": 76,
                        "K": 160, "Ca": 17100, "Ti": 810, "V": 105, "Cr": 4700, "Mn": 800, "Fe": 320000, "Co": 880, "Ni": 18200, "Cu": 60, "Zn": 40},
         "bulk_ppm": {"Cr": 4700, "Cu": 60, "Nb": 0.44, "Mo": 1.7, "Ru": 1.3, "Rh": 0.24, "Pd": 1, "Ag": 0.05, "La": 0.44,
                                        "Ce": 1.13, "Gd": 0.37, "Pt": 1.9, "Au": 0.16, "Th": 0.055, "U": 0.015},
         "core_ppm_note": "Table 4, the core", "core_ppm": {"Cr": 9000, "Cu": 125, "Mo": 5, "Ru": 4, "Rh": 0.74, "Pd": 3.1, "Ag": 0.15, "Pt": 5.7, "Au": 0.5},
         "silicate_ppm_note": "the table preceding Table 3 in the same chapter (silicate Earth); the excerpt read did not carry its heading", "silicate_ppm": {"Cr": 2625, "Cu": 30, "Mo": 0.05, "Ru": 0.005, "Rh": 0.001, "Pd": 0.004, "Ag": 0.008, "La": 0.65, "Ce": 1.68, "Pt": 0.007, "Au": 0.001, "Th": 0.08, "U": 0.02}}
weights = {"source": "IUPAC 2013 standard atomic weights (conventional values), as carried by pyscf.data.elements.MASSES 2.14; Ac is the mass of its longest-lived isotope", "status": "READ",
           "Cr": 51.9961, "Cu": 63.546, "Nb": 92.90637, "Mo": 95.95, "Ru": 101.07, "Rh": 102.9055, "Pd": 106.42, "Ag": 107.8682, "La": 138.90547,
           "Ce": 140.116, "Gd": 157.25, "Pt": 195.084, "Au": 196.966569, "Ac": 227.02775, "Th": 232.0377, "H": 1.008, "U": 238.02891,
           "C": 12.011, "O": 15.999, "Na": 22.98976928, "Mg": 24.305, "Al": 26.9815385, "Si": 28.085, "P": 30.973762, "S": 32.06, "Cl": 35.45,
           "K": 39.0983, "Ca": 40.078, "Ti": 47.867, "V": 50.9415, "Mn": 54.938044, "Fe": 55.845, "Co": 58.933194, "Ni": 58.6934, "Zn": 65.38}
hh = {"source": "Huber K.P. and Herzberg G., Constants of Diatomic Molecules, via the NIST Chemistry WebBook (SRD 69), read 2026-10-11 through the web connectors: https://webbook.nist.gov/cgi/cbook.cgi?Formula=Cu2&NoIon=on&Units=SI&cDI=on and ...Formula=Ag2...",
      "status": "READ", "CuCu": {"state": "X 1Sigma+", "we": 264.55, "re": 2.2197}, "AgAg": {"state": "X 1Sigma g+", "we": 192.4}}
d.update(earth=earth, weights=weights, huber_herzberg=hh)
d.update(branches=branches, follows=follows, mx2=mx2, bands=bands, robust=robust)
d["what"] = ("item 221: matter in position 2 -- the rows behind lemmas/p2_matter.py.  Molecules: UKS PBE0/def2-TZVP (+def2 ECP "
    "for Ag, Au), PySCF 2.14.  Solids: PBE, GTH-PBE pseudopotentials, GTH-DZVP-MOLOPT-SR, 4x4x4 k (irreducible wedge), Fermi "
    "smearing 0.01 Ha, 160 Ha cutoff on a fixed mesh per metal; d band on 8x8x8, smearing 0.005 Ha.  Position 2's law "
    "(RECONSTRUCTED): E' = E + delta (N_d - N_obs) on each exception atom, N_d its Lowdin d count; delta calibrated per "
    "method so the free atom's aufbau configuration lies 0.05 eV (min) or the NIST gap (mirror) below the observed one.  "
    "Computed 2026-10-11 in a scratch environment; read-only on the corpus.")
d["code_note"] = ("sha256 of the scripts as committed beside this file (p2_matter_scripts/).  They grew during the work: "
    "earlier rows were made by earlier states that differ only in what was added later -- output fields (E_atoms), options "
    "(separate observed/aufbau spins, a fixed FFT mesh, the Mulliken switch, first-order extrapolation for an unbracketed "
    "crossing) -- so each banked row's numerical path is the committed script's at its defaults; the variable-mesh solid "
    "scans that the fixed mesh replaced are not banked")
d.update(calibration=cal, atoms_pbe0=atoms, molecules=mols, solids=sols, code_sha256=code)
json.dump(d, open(OUT, "w"), indent=1)
print("banked: cal", {k: sorted(v) for k, v in cal.items()}, "atoms", sorted(atoms), "molecules", len(mols), "solids", [(s["el"], s["law"], len(s["rows"])) for s in sols])
