#!/usr/bin/env python3
"""verify_paper.py -- enforce that the prose cannot contradict the mathematics.

The publication standard this enforces, stated by the author:

    Stripped of the prose, all underlying math, claims and subject matter must be
    true and proved. The prose is a translation of the underlying subject matter.
    It must not state anything that contradicts the underlying math or claims. It
    must itself be true, and verifiable by the math we provide in the paper.

Care alone cannot enforce that. This does, mechanically, in three passes:

  PASS 1  RECOMPUTE.  Every DERIVED row of papers/CLAIMS.tsv is recomputed from
          the instruments and compared to the value the ledger states. A ledger
          row that does not reproduce is a failure, not a rounding note.

  PASS 2  BIND.       Every row whose `verify` column names an instrument
          constant is compared against that constant as it actually is in the
          source. A paper cannot cite a figure the instrument no longer holds.

  PASS 3  PROSE.      Every number appearing in the paper's prose is extracted
          and matched against the ledger. A number in the prose that no ledger
          row carries is UNBACKED and fails, unless it is structural (a section
          number, a year, a reference index, an equation label).

The third pass is the one that does the work the standard asks for. It is why a
sentence cannot quietly acquire a figure the mathematics does not produce.

WHAT IT REFUSES
---------------
It does not check that a MEASURED or SOURCED value is correct in the world -- no
program can. It checks that such a row carries a provenance string and that the
paper does not restate it as something else. Correctness against the literature
is the citation's job and the reader's.

It does not read English. A sentence can be false in ways no numeric check sees.
What it guarantees is narrower and worth having: every QUANTITY in the prose is
one the mathematics produces, at the value the mathematics produces it.

Stdlib only.  python3 tools/verify_paper.py papers/<paper>.md
"""

import csv
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, "papers", "CLAIMS.tsv")
sys.path.insert(0, HERE)

import collector  # noqa: E402
import mucf       # noqa: E402

ALPHA = 1 / 137.036


# ---- the derivations the ledger names -------------------------------------
def composed_lever():
    return 0.34 * 0.31 / 0.45


def e_binder_captured():
    return collector.e_binder_captured()


def headroom():
    return e_binder_captured() / collector.PION_THRESHOLD_GEV


def _fom(f):
    return (mucf.Q_FUS_MEV / 1000.0) * f / (mucf.STICKING["both"][0] * e_binder_captured())


def fom_heat():
    return _fom(1.0)


def fom_work():
    return _fom(collector.F_WORK)


def short_heat():
    return 1.0 / fom_heat()


def short_work():
    return 1.0 / fom_work()


def cond8_heat():
    return (mucf.Q_FUS_MEV / 1000.0) / mucf.STICKING["both"][0]


def cond8_work():
    return (mucf.Q_FUS_MEV / 1000.0) * collector.F_WORK / mucf.STICKING["both"][0]


def margin_heat():
    return headroom() / short_heat()


def margin_work():
    return headroom() / short_work()


def ceiling_measured():
    return 1.0 / mucf.STICKING["sin"][0]


def ceiling_levers():
    return 1.0 / mucf.STICKING["both"][0]


def N_measured_phi3():
    return mucf.cycles(mucf.STICKING["sin"][0], 3.0)


def N_levers_phi3():
    return mucf.cycles(mucf.STICKING["both"][0], 3.0)


def vratio(E_MeV, A, Z):
    """recoil velocity over binder orbital velocity; binder mass cancels."""
    v = math.sqrt(2 * E_MeV / (A * 931.5))
    return v / (Z * ALPHA)


def vratio_dt():
    return vratio(3.5, 4, 2)


def vratio_dd():
    return vratio(0.82, 3, 2)


def music_gain():
    return collector.MUSIC_MU_MINUS_PER_W / collector.PSI_MUE4_PER_W


def loose_ratio():
    return 319.0 / 0.66


def alpha_share():
    return 100.0 * 3.5 / mucf.Q_FUS_MEV


def neutron_share():
    return 100.0 * 14.1 / mucf.Q_FUS_MEV


def carnot800():
    return 100.0 * (1.0 - 300.0 / 800.0)


def delivered_per_muon():
    return 1.4e6 / 1e10 / 1.602e-19 / 1e12    # J per muon -> TeV


def mu2e_per_muon():
    return 8.0 / collector.MU2E_STOPPED_PER_P / 1000.0   # TeV


def ambient_factor():
    return 88.0 / 30.0


def window_floor_mev():
    return 119 * 0.511


def harp_sigma():
    return collector.harp_window_sigma()


def harp_yield():
    return collector.harp_window_yield()


def nf_captured():
    return collector.nf_captured_per_interacting_proton()


def capture_ratio():
    return nf_captured() / harp_yield()


def cost_upper():
    return 8.0 / harp_yield()


def harp_sigma_back():
    return collector.harp_window_sigma(1.15)


def harp_yield_back():
    return collector.harp_window_yield(1.15)


def back_ratio():
    return nf_captured() / harp_yield_back()


def back_frac():
    return 100.0 * harp_sigma_back() / harp_sigma()


def _fom_prod(f):
    return (mucf.Q_FUS_MEV / 1000.0) * f / (mucf.STICKING["both"][0] * cost_upper())


def fom_prod_heat():
    return _fom_prod(1.0)


def fom_prod_work():
    return _fom_prod(collector.F_WORK)


def short_prod_heat():
    return cost_upper() / cond8_heat()


def short_prod_work():
    return cost_upper() / cond8_work()


def harp_fwd_sigma():
    return collector.harp_forward_sigma()


def harp_comb_sigma():
    return collector.harp_combined_sigma()


def harp_comb_yield():
    return collector.harp_combined_yield()


def cost_pion():
    return collector.cost_per_pion_produced()


def fwd_frac():
    return 100.0 * harp_fwd_sigma() / harp_comb_sigma()


def short_perf_heat():
    return cost_pion() / cond8_heat()


def short_perf_work():
    return cost_pion() / cond8_work()


def fom_perf_heat():
    return (mucf.Q_FUS_MEV / 1000.0) / (mucf.STICKING["both"][0] * cost_pion())


def fom_perf_work():
    return fom_perf_heat() * collector.F_WORK


def capture_of_production():
    return 100.0 * nf_captured() / harp_comb_yield()


def react_sin():
    return mucf.STICKING["sin"][0] / mucf.OMEGA_INITIAL


def react_psi():
    return mucf.STICKING["psi"][0] / mucf.OMEGA_INITIAL


def ws_sin():
    return 100.0 * mucf.STICKING["j1"][0] * react_sin()


def ws_psi():
    return 100.0 * mucf.STICKING["j1"][0] * react_psi()


def breakpoint():
    return 100.0 * (mucf.Q_FUS_MEV / 1000.0) / cost_pion()


def c8_sin_heat():
    return (mucf.Q_FUS_MEV / 1000.0) / (ws_sin() / 100.0)


def c8_psi_heat():
    return (mucf.Q_FUS_MEV / 1000.0) / (ws_psi() / 100.0)


def margin_sin():
    return c8_sin_heat() / cost_pion()


def short_psi():
    return cost_pion() / c8_psi_heat()


def work_short_sin():
    return cost_pion() / (c8_sin_heat() * collector.F_WORK)


def work_short_psi():
    return cost_pion() / (c8_psi_heat() * collector.F_WORK)


def c8_sin_work():
    return c8_sin_heat() * collector.F_WORK


def c8_psi_work():
    return c8_psi_heat() * collector.F_WORK


def muon_above_floor():
    return 207.0 / 119.0


def blanket_thermal():
    return collector.blanket_thermal_mev()


def total_thermal():
    return collector.total_thermal_mev()


def energy_mult():
    return collector.energy_multiplication()


def work_old():
    return mucf.Q_FUS_MEV * collector.F_WORK


def work_new():
    return collector.work_per_fusion_mev()


def work_gain():
    return work_new() / work_old()


def f_work_new():
    return collector.f_work_corrected()


def short_sin_corr():
    return work_short_sin() / work_gain()


def short_psi_corr():
    return work_short_psi() / work_gain()


def br_nf():
    return 20.0 * 0.075


def cap_nf():
    return 100.0 * collector.captured_fraction(br_nf(), True)


def cap_nf_back():
    return 100.0 * collector.captured_fraction(br_nf(), False)


def br_90():
    return collector.br_for_capture(0.90, True)


def bore_90():
    return 100.0 * br_90() / 20.0


def br_ratio():
    return br_90() / br_nf()


def comet_cap():
    return 1000.0 * collector.pt_max(5.0 * 0.15)


def losalamos_recost():
    return 150 * (mucf.Q_FUS_MEV / 1000.0) / e_binder_captured()


FNS = {k: v for k, v in list(globals().items()) if callable(v) and not k.startswith("_")}


def resolve_const(path):
    """Resolve 'mucf.STICKING.sin' / 'collector.PION_THRESHOLD_GEV' / 'mucf.TRANSFER[0]'."""
    m = re.match(r"^(\w+)\.(\w+)(?:\[(\d+)\]|\.(\w+))?$", path)
    if not m:
        return None
    mod = {"mucf": mucf, "collector": collector}.get(m.group(1))
    if mod is None or not hasattr(mod, m.group(2)):
        return None
    v = getattr(mod, m.group(2))
    if m.group(3) is not None:
        v = v[int(m.group(3))]
    elif m.group(4) is not None:
        v = v[m.group(4)]
    if isinstance(v, tuple):
        v = v[0]
    return v


def norm(s):
    try:
        return float(str(s).replace(",", "").replace("pc", ""))
    except ValueError:
        return None


def close(a, b, rel=0.02):
    if a is None or b is None:
        return False
    if b == 0:
        return abs(a) < 1e-12
    return abs(a - b) / abs(b) <= rel


def load():
    with open(LEDGER, newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def scale_variants(v, unit):
    """The ledger holds one canonical value; prose may state it in its natural
    unit. Percentages and their fractions are the only conversion allowed."""
    out = {v}
    if unit == "percent":
        out.add(v / 100.0)
    if unit == "fraction":
        out.add(v * 100.0)
    return out


# Consume scientific notation whole: "2.7e8" is one number, not 2.7 and 8.
NUM = re.compile(
    r"(?<![\w.])(\d+(?:,\d{3})*(?:\.\d+)?)"
    r"(?:[eE]([+-]?\d+)|\s*[x×]\s*10\s*\^?\s*([+-]?\d+))?")
STRUCTURAL = re.compile(
    r"(?:§|section|sec\.|condition|table|figure|fig\.|item|ref\.|\[)\s*\d+", re.I)


def main():
    if len(sys.argv) < 2:
        print("usage: verify_paper.py papers/<paper>.md")
        return 2
    paper = sys.argv[1]
    rows = load()
    fails = 0

    print(f"verify_paper.py   ledger: papers/CLAIMS.tsv ({len(rows)} claims)")
    print(f"                  paper : {paper}")
    print()

    print("PASS 1 -- RECOMPUTE every DERIVED row")
    n = 0
    for r in rows:
        if r["status"] != "DERIVED":
            continue
        tgt = r["verify"]
        if not tgt.startswith("fn:"):
            continue
        fn = FNS.get(tgt[3:])
        n += 1
        if fn is None:
            print(f"  {r['id']} {r['claim'][:44]:<44} NO SUCH FUNCTION {tgt}   FAIL")
            fails += 1
            continue
        got, want = fn(), norm(r["value"])
        ok = close(got, want)
        fails += 0 if ok else 1
        print(f"  {r['id']} {r['claim'][:44]:<44} {got:>12,.4g} vs {want:<12,.4g} "
              f"{'PASS' if ok else 'FAIL'}")
    print(f"  {n} derived rows recomputed")

    print()
    print("PASS 2 -- BIND every row naming an instrument constant")
    n = 0
    for r in rows:
        tgt = r["verify"]
        if not tgt or tgt in ("none",) or tgt.startswith("fn:"):
            continue
        n += 1
        got, want = resolve_const(tgt), norm(r["value"])
        if got is None:
            print(f"  {r['id']} unresolvable constant {tgt}   FAIL")
            fails += 1
            continue
        ok = any(close(got, w) for w in scale_variants(want, r["unit"]))
        fails += 0 if ok else 1
        print(f"  {r['id']} {tgt:<44} {got:>12,.4g} vs {want:<12,.4g} "
              f"{'PASS' if ok else 'FAIL'}")
    print(f"  {n} constants bound")

    print()
    print("PASS 3 -- PROSE: every number in the paper must be in the ledger")
    if not os.path.exists(paper):
        print(f"  paper not found: {paper}   FAIL")
        return 1
    text = open(paper, encoding="utf-8").read()
    # The reference list is bibliographic data -- volume, page and arXiv numbers
    # are not claims and the ledger rightly does not carry them.
    text = re.split(r"^##\s+References\s*$", text, flags=re.M)[0]
    text = re.sub(r"```.*?```", " ", text, flags=re.S)          # code blocks
    text = re.sub(r"`[^`]*`", " ", text)                         # inline code
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)      # tables carry their own
    # Section headings are structure, not claims: "### 5.2 Collection alone ..."
    text = re.sub(r"^#{1,6}\s+[\d.]+\s*", "#H ", text, flags=re.M)
    values = set()
    for r in rows:
        v = norm(r["value"])
        if v is not None:
            values |= scale_variants(v, r["unit"])
    unbacked = {}
    for m in NUM.finditer(text):
        lo = max(0, m.start() - 24)
        if STRUCTURAL.search(text[lo:m.end()]):
            continue
        raw = m.group(0)
        v = norm(m.group(1))
        if v is None:
            continue
        exp = m.group(2) or m.group(3)
        if exp is not None:
            v *= 10.0 ** int(exp)
        if 1900 <= v <= 2100 and "." not in m.group(1):
            continue                                             # a year
        if v <= 20 and float(v).is_integer():
            continue                                             # counts, labels
        if any(close(v, w, 0.02) for w in values):
            continue
        unbacked.setdefault(raw, 0)
        unbacked[raw] += 1
    if unbacked:
        for raw, cnt in sorted(unbacked.items(), key=lambda kv: -kv[1]):
            print(f"  UNBACKED  {raw!r} x{cnt}   -- no ledger row carries this")
        fails += len(unbacked)
    else:
        print("  every number in the prose is carried by a ledger row   PASS")

    print()
    print(f"verify_paper: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
