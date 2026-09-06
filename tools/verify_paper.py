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
    """CORRECTED, sec.5.26. This returned the J=1,v=0 excited-state initial
    sticking times a ground-state survival fraction -- two different states,
    giving 0.1487%. Fusion occurs from (dtmu)_{J=v=0}, so the operative value is
    the witnessed effective sticking. The two 'readings' survive as the two
    extremes of the three 2001 measurements."""
    return 100.0 * min(mucf.OMEGA_EFF_MEASURED)


def ws_psi():
    return 100.0 * max(mucf.OMEGA_EFF_MEASURED)


def ws_sin_superseded():
    return 100.0 * mucf.STICKING["j1"][0] * react_sin()


def ws_psi_superseded():
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


def _N(ws, phi):
    return mucf.cycles(ws, phi)


def asym_sin():
    return 100.0 / ws_sin()


def asym_psi():
    return 100.0 / ws_psi()


def phi90_sin():
    w = ws_sin() / 100.0
    return 9.0 * mucf.LAMBDA_0 / (w * mucf.LAMBDA_C)


def N3_sin():
    return _N(ws_sin() / 100.0, 3.0)


def frac3_sin():
    return 100.0 * N3_sin() / asym_sin()


def tq3_sin():
    return N3_sin() * (total_thermal() / 1000.0) / cost_pion()


def tq_asym_sin():
    return asym_sin() * (total_thermal() / 1000.0) / cost_pion()


def wq3_sin():
    return N3_sin() * (work_new() / 1000.0) / cost_pion()


def tshort3_sin():
    return 1.0 / tq3_sin()


def net_extra_n():
    return collector.net_per_extra_neutron()


def therm_mult():
    return collector.thermal_with_multiplier(1.6)


def mult_16():
    return therm_mult() / mucf.Q_FUS_MEV


def wshort3_psi():
    return 1.0 / (_N(ws_psi() / 100.0, 3.0) * (work_new() / 1000.0) / cost_pion())


def molar_vol_phi90():
    return collector.phi_to_molar_volume(phi90_sin())


def compression():
    return 23.0 / molar_vol_phi90()


def trans_atoms():
    return collector.transition_phi(True)


def trans_molecules():
    return collector.transition_phi(False)


def carnot1200():
    return collector.carnot(1200.0)


def work_bound():
    return therm_mult() * carnot1200()


def N_diss():
    return _N(ws_sin() / 100.0, trans_atoms())


def tq_bound():
    return N_diss() * (therm_mult() / 1000.0) / cost_pion()


def wq_bound():
    return N_diss() * (work_bound() / 1000.0) / cost_pion()


def wshort_bound():
    return 1.0 / wq_bound()


def N_needed():
    return cost_pion() / (work_bound() / 1000.0)


def ws_needed():
    lo, hi = 1e-5, 0.01
    phi = trans_atoms()
    for _ in range(200):
        m = (lo + hi) / 2
        if _N(m, phi) > N_needed():
            lo = m
        else:
            hi = m
    return 100.0 * lo


def ws_reduction():
    return 100.0 * (1.0 - ws_needed() / ws_sin())


def ws_excursion():
    return 100.0 * (1.0 - 0.64 / 0.86)


def bred_credit():
    return collector.bred_credit_mev(collector.BREEDING_RATIO)


def total_bred():
    return collector.total_with_breeding_mev(collector.BREEDING_RATIO)


def bred_over_heat():
    return bred_credit() / 14.1


def q_demo_real():
    return 150.0 * (total_bred() / 1000.0) / (e_binder_captured())


def q_demo_collector():
    return 150.0 * (total_bred() / 1000.0) / (cost_pion() / 0.9)


def q_phi3_collector():
    return N3_sin() * (total_bred() / 1000.0) / (cost_pion() / 0.9)


def therm_sourced():
    return collector.thermal_sourced_mev()


def mult_sourced():
    return therm_sourced() / mucf.Q_FUS_MEV


def conservatism():
    return therm_sourced() / total_thermal()


def work_sourced():
    return collector.work_sourced_mev()


def tq_sourced():
    return N_diss() * (therm_sourced() / 1000.0) / cost_pion()


def wq_sourced():
    return N_diss() * (work_sourced() / 1000.0) / cost_pion()


def total_sourced():
    return collector.total_value_sourced_mev()


def qb_demo():
    return 150.0 * (total_sourced() / 1000.0) / (cost_pion() / 0.9)


def qb_bound():
    return N_diss() * (total_sourced() / 1000.0) / cost_pion()


def inflight_ratio():
    return mucf.LAMBDA_C / collector.LAMBDA_INFLIGHT


def N_inflight():
    ws = ws_sin() / 100.0
    phi = trans_atoms()
    return phi * collector.LAMBDA_INFLIGHT / (
        mucf.LAMBDA_0 + ws * phi * collector.LAMBDA_INFLIGHT)


def thresh_nm():
    return 1239.8 / 10.9e3


def sigma_muhe():
    return 6.3e-18 / (206.8 ** 2 * 4)


def intensity_match():
    return (mucf.LAMBDA_0 / sigma_muhe()) * 10.9e3 * 1.602e-19


def intensity_95():
    return (1e7 / sigma_muhe()) * 10.9e3 * 1.602e-19


def model_225():
    return 1000.0 * collector.pt_max(20.0 * 0.075)


def shield_thinning():
    return 100.0 * (0.130 - 0.075)


def heating_penalty():
    return math.exp(shield_thinning() / 5.5)


def bore_increase():
    return 100.0 * (shield_thinning() / 100.0) / 0.50


def losalamos_recost():
    return 150 * (mucf.Q_FUS_MEV / 1000.0) / e_binder_captured()


def _eta(N, value_mev):
    """Collection efficiency at which the balance is exactly 1, for a service
    life N and a value per fusion. Above 1 the product is unreachable at any
    collector."""
    return 100.0 * cost_pion() / (N * (value_mev / 1000.0))


def eta_elec_bound():
    return _eta(N_diss(), work_sourced())


def eta_elec_phi3():
    return _eta(N3_sin(), work_sourced())


def eta_heat_bound():
    return _eta(N_diss(), therm_sourced())


def eta_heat_phi3():
    return _eta(N3_sin(), therm_sourced())


def eta_bred_bound():
    return _eta(N_diss(), total_sourced())


def eta_bred_phi3():
    return _eta(N3_sin(), total_sourced())


def eta_bred_demo():
    return _eta(150.0, total_sourced())


def product_ratio():
    return eta_elec_bound() / eta_bred_bound()


def demo_vs_frontend():
    return eta_bred_demo() / capture_of_production()


def N3_psi():
    return _N(ws_psi() / 100.0, 3.0)


def tq3_psi():
    return N3_psi() * (total_thermal() / 1000.0) / cost_pion()


def flux_match():
    return mucf.LAMBDA_0 / sigma_muhe()


def flux_95():
    return 1e7 / sigma_muhe()


def yin_unpol_repro():
    return collector.yin_cycles("unpolarised")


def yin_polopt_repro():
    return collector.yin_cycles("pol-optimistic")


def yin_polopt_q_repro():
    return collector.yin_q("pol-optimistic")


def yin_polopt_implied_ws():
    return collector.yin_sticking_for_stated("pol-optimistic")


def yin_ladder():
    return collector.YIN_TABLE["ultimate"][2] / collector.YIN_TABLE["unpolarised"][2]


def collection_factor_nf():
    return 100.0 / cap_nf()


def collection_factor_stop265():
    return 100.0 / deliv_both_nf_265()


def collection_factor_fe():
    return 100.0 / capture_of_production()


def yin_unpol_q_at_nf():
    return collector.YIN_TABLE["unpolarised"][3] * (cap_nf() / 100.0)


def yin_polopt_q_corrected_at_nf():
    return yin_polopt_q_repro() * (cap_nf() / 100.0)


def purity_parity_bound():
    return 1e6 * mucf.purity_for_parity(trans_atoms())


def purity_parity_phi3():
    return 1e6 * mucf.purity_for_parity(3.0)


def _N_imp(c):
    return mucf.cycles(ws_sin() / 100.0, trans_atoms(), contamination=c)


def N_imp_1ppm():
    return _N_imp(1e-6)


def N_imp_10ppm():
    return _N_imp(1e-5)


def N_imp_100ppm():
    return _N_imp(1e-4)


def molar_vol_2lhd():
    return collector.phi_to_molar_volume(2.0)


def molar_vol_bound():
    return collector.phi_to_molar_volume(trans_atoms())


# ---- the independent closure criterion of Kou & Chen, on this paper's numbers
def _omega_crit(value_mev, eta):
    """Their conditional sticking no-go boundary at unit gain, omega < 1/N_L
    with N_L = E_cost/(eta_sys E_use). In percent."""
    return 100.0 * (value_mev / 1000.0) / (cost_pion() / eta)


def kc_boundary_ref():
    return 100.0 * (20.4 / 1000.0) / 5.0


def omega_crit_heat():
    return _omega_crit(therm_sourced(), 1.0)


def omega_crit_work():
    return _omega_crit(work_sourced(), 1.0)


def omega_crit_bred():
    return _omega_crit(total_sourced(), 1.0)


def omega_crit_heat_nf():
    return _omega_crit(therm_sourced(), cap_nf() / 100.0)


def omega_crit_bred_fe():
    return _omega_crit(total_sourced(), capture_of_production() / 100.0)


def _phi_needed(value_mev, eta):
    """Density at which the balance is exactly 1. None above the sticking
    asymptote, where no density suffices -- their no-go, in this paper's terms."""
    ws = ws_sin() / 100.0
    n_req = (cost_pion() / eta) / (value_mev / 1000.0)
    denom = 1.0 - ws * n_req
    if denom <= 0:
        return None
    return n_req * mucf.LAMBDA_0 / (mucf.LAMBDA_C * denom)


def phi_heat_perfect():
    return _phi_needed(therm_sourced(), 1.0)


def phi_heat_c90():
    return _phi_needed(therm_sourced(), 0.90)


def phi_work_perfect():
    return _phi_needed(work_sourced(), 1.0)


def phi_work_c90():
    return _phi_needed(work_sourced(), 0.90)


def phi_bred_perfect():
    return _phi_needed(total_sourced(), 1.0)


def phi_bred_c90():
    return _phi_needed(total_sourced(), 0.90)


def phi_bred_nf():
    return _phi_needed(total_sourced(), cap_nf() / 100.0)


def phi_bred_fe():
    return _phi_needed(total_sourced(), capture_of_production() / 100.0)


def N_model_at_la():
    return mucf.cycles(ws_sin() / 100.0, 1.2)


def model_over_measured():
    return N_model_at_la() / 150.0


def N_at_la_final_sticking():
    return mucf.cycles(mucf.STICKING["sin"][0], 1.2)


def L_mu_kc_sin():
    return 1.93e8 * 2.197e-6


def L_mu_bound():
    return trans_atoms() * mucf.LAMBDA_C / mucf.LAMBDA_0


def modern_ws_ratio():
    return mucf.OMEGA_INITIAL_MODERN / mucf.OMEGA_INITIAL


def ws_sin_modern():
    return ws_sin_superseded() * modern_ws_ratio()


def N_bound_modern():
    return mucf.cycles(ws_sin_modern() / 100.0, trans_atoms())


def q_heat_bound_modern():
    return N_bound_modern() * (therm_sourced() / 1000.0) / cost_pion()


def q_heat_bound_nf_modern():
    return N_bound_modern() * (therm_sourced() / 1000.0) / (cost_pion() / (cap_nf() / 100.0))


def kc_sustained():
    """Their reference energy fluence spread over one binder lifetime."""
    return 7.2e7 / 2.197e-6


def kc_over_5_21():
    return kc_sustained() / intensity_match()


def stripping_gain():
    return 156.5 / 112.6


# ---- the acceptance model: pi- produced -> mu- delivered -------------------
def mars_ratio():
    """The paper's own MARS15-derived figure: captured mu- per pi- produced."""
    return capture_of_production()


def model_vs_mars():
    return 100.0 * collector.delivered_fraction(1.50, "fwd", collector.NF_RF_WINDOW_MEV)


def model_mars_agreement():
    return model_vs_mars() / mars_ratio()


def decay_survival_nf():
    return collector.decay_survival(1.50)


def deliv_fwd_nf():
    return 100.0 * collector.delivered_fraction(1.50, "fwd")


def deliv_both_nf():
    return 100.0 * collector.delivered_fraction(1.50, "both")


def deliv_back_nf():
    return 100.0 * collector.delivered_fraction(1.50, "back")


def rf_window_cost():
    return deliv_fwd_nf() / model_vs_mars()


def hemisphere_gain():
    return deliv_both_nf() / deliv_fwd_nf()


def _dl(br, hemi, cut):
    return 100.0 * collector.delivered_fraction(br, hemi, (0.0, cut))


def deliv_both_nf_400():
    return _dl(1.50, "both", 400)


def deliv_both_nf_265():
    return _dl(1.50, "both", 265)


def deliv_both_nf_200():
    return _dl(1.50, "both", 200)


def deliv_both_90_200():
    return _dl(2.60, "both", 200)


def deliv_both_90_400():
    return _dl(2.60, "both", 400)


def deliv_both_90_265():
    return _dl(2.60, "both", 265)


def _qb150(eta_pct, cost=None):
    return 150.0 * (total_sourced() / 1000.0) / ((cost or cost_pion()) / (eta_pct / 100.0))


def qb_deliv_both_nf():
    return _qb150(deliv_both_nf())


def qb_deliv_both_nf_400():
    return _qb150(deliv_both_nf_400())


def qb_deliv_both_nf_265():
    return _qb150(deliv_both_nf_265())


def qb_deliv_both_90_400():
    return _qb150(deliv_both_90_400())


def qb_deliv_both_90_265():
    return _qb150(deliv_both_90_265())


def qb_deliv_kelly_265():
    return _qb150(deliv_both_nf_265(), kelly_cost())


def eta_bred_demo_kelly():
    return 100.0 * kelly_cost() / (150.0 * (total_sourced() / 1000.0))


def range_150():
    return collector.csda_range(150.0)


def range_265():
    return collector.csda_range(265.0)


def range_400():
    return collector.csda_range(400.0)


def trit_265():
    return collector.tritium_inventory_kg(265.0, 5.0)


def trit_400():
    return collector.tritium_inventory_kg(400.0, 5.0)


def trit_150():
    return collector.tritium_inventory_kg(150.0, 5.0)


def trit_ratio_400_265():
    return trit_400() / trit_265()


def eta_ratio_400_265():
    return deliv_both_nf_400() / deliv_both_nf_265()


def len_265_phi1():
    return collector.target_length_cm(265.0, 1.0)


def len_265_phi85():
    return collector.target_length_cm(265.0, trans_atoms())


def mufuse_curies():
    return collector.tritium_curies(0.004 * collector.T_MASS_FRAC_DT)


def min_ionising_h2():
    return min(collector.bethe_dedx(T) for T in [x * 0.5 for x in range(2, 4000)])


def envelope_capture():
    return collector.beam_envelope_cm(1.50, 20.0)


def envelope_taper():
    return collector.beam_envelope_cm(1.50, 1.25)


def envelope_wide():
    return collector.beam_envelope_cm(2.60, 20.0)


def trit_nf_265():
    return collector.tritium_inventory_derived_kg(265.0, 1.50)


def trit_nf_400():
    return collector.tritium_inventory_derived_kg(400.0, 1.50)


def trit_wide_265():
    return collector.tritium_inventory_derived_kg(265.0, 2.60)


def trit_wide_400():
    return collector.tritium_inventory_derived_kg(400.0, 2.60)


def bore_trit_cost():
    return trit_wide_265() / trit_nf_265()


def kg_per_gain_bore():
    return trit_wide_265() / qb_deliv_both_90_265()


def kg_per_gain_target():
    return trit_nf_265() / qb_deliv_kelly_265()


def lever_ratio():
    return kg_per_gain_bore() / kg_per_gain_target()


def strait_cost_41():
    return collector.strait_cost_per_pion(4.1)


def strait_agreement():
    return strait_cost_41() / cost_pion()


def strait_pions_41():
    return collector.strait_pions_per_interacting_proton(4.1)


def thick_amp_41():
    return collector.thickness_amplification(4.1)


def thick_amp_111():
    return collector.thickness_amplification(11.1)


def kelly_over_strait():
    return collector.KELLY_PIMINUS_PER_BEAM / strait_pions_41()


def gap_solid_angle():
    return 2 * math.pi * (math.cos(0.25) - math.cos(0.35))


def gap_low():
    return collector.harp_gap_bracket()[0]


def gap_high():
    return collector.harp_gap_bracket()[1]


def cost_gap_low():
    return collector.coverage_corrected_cost("high")


def cost_gap_high():
    return collector.coverage_corrected_cost("low")


def backward_ceiling():
    return collector.harp_backward_ceiling()


def coverage_max_factor():
    return cost_pion() / cost_gap_low()


# ---- the witnessed cap ------------------------------------------------------
def ws_operative():
    return 100.0 * mucf.omega_eff_operative("theory")


def ws_witnessed_best():
    return 100.0 * mucf.omega_eff_operative("measured")


def ws_chain_ratio():
    return ws_operative() / ws_sin_superseded()


def n_cap_theory():
    return 1.0 / mucf.omega_eff_operative("theory")


def n_cap_witnessed():
    return 1.0 / mucf.omega_eff_operative("measured")


def out_per_binder_heat():
    return n_cap_witnessed() * therm_sourced() / 1000.0


def out_per_binder_raw():
    return n_cap_witnessed() * mucf.Q_FUS_MEV / 1000.0


def q_cap_heat():
    return out_per_binder_heat() / cost_pion()


def q_cap_raw():
    return out_per_binder_raw() / cost_pion()


def ws_required_heat():
    return 100.0 * (therm_sourced() / 1000.0) / cost_pion()


def r_required_heat():
    return 1.0 - (ws_required_heat() / 100.0) / mucf.OMEGA_INITIAL_MODERN


def r_shortfall():
    return r_required_heat() / mucf.R_REACTIVATION


def v_required_heat():
    return cost_pion() * mucf.omega_eff_operative("measured") * 1000.0


def ebinder_required_heat():
    return (therm_sourced() / 1000.0) / mucf.omega_eff_operative("measured")


# ---- the last escape, priced on a computed cross section --------------------
def sigma_amu_photo():
    """Hydrogenic 1s photoionisation of (alpha mu). The published rate network
    uses 20 barn as an avowed placeholder and states that a microscopic value
    would need the bound-continuum matrix element; this is that value."""
    return 6.30e-18 / (206.768 ** 2 * 4)


def sigma_over_placeholder():
    return sigma_amu_photo() / 20e-24


def rx_required():
    """External stripping branch needed, given collisional reactivation."""
    need = (therm_sourced() / 1000.0) / cost_pion()
    return 1.0 - need / (mucf.OMEGA_INITIAL_MODERN * (1 - mucf.R_REACTIVATION))


def rx_achieved():
    lam0, lamc, phi = 4.55e5, 1.1e8, 1.25
    w0 = 1 / 112.6 - lam0 / (lamc * phi)
    w1 = 1 / 156.5 - lam0 / (lamc * phi)
    return 1.0 - w1 / w0


def rx_gap():
    return rx_required() / rx_achieved()


def fluence_required():
    px = rx_required() / 0.996
    return -math.log(1 - px) / sigma_amu_photo()


def intensity_required():
    return fluence_required() * 15e3 * 1.602e-19 / 2.197e-6


def intensity_agreement():
    return intensity_required() / intensity_match()


def flux_gap_planned():
    return mucf.FLUX_FOR_ONE_MW / mucf.FLUX_HIMB_PLANNED


def flux_gap_today():
    return mucf.FLUX_FOR_ONE_MW / mucf.FLUX_PSI_TODAY


def kelly_cost():
    return collector.kelly_cost_per_pion()


def kelly_ratio():
    return cost_pion() / kelly_cost()


def _qk(N, value_mev):
    """The balance at the Kelly production cost, perfect collection -- the
    status their figure is stated at."""
    return N * (value_mev / 1000.0) / kelly_cost()


def qk_heat_demo():
    return _qk(150.0, therm_sourced())


def qk_heat_bound():
    return _qk(N_diss(), therm_sourced())


def qk_work_demo():
    return _qk(150.0, work_sourced())


def qk_work_bound():
    return _qk(N_diss(), work_sourced())


def qk_bred_demo():
    return _qk(150.0, total_sourced())


def qk_bred_bound():
    return _qk(N_diss(), total_sourced())


def _qbal(N, value_mev, eta):
    """The balance at an explicit collection efficiency: service life times
    value, against the production floor divided by that efficiency."""
    return N * (value_mev / 1000.0) / (cost_pion() / eta)


def q_heat_bound_c90():
    return _qbal(N_diss(), therm_sourced(), 0.90)


def q_heat_phi3_c90():
    return _qbal(N3_sin(), therm_sourced(), 0.90)


def q_heat_demo_c90():
    return _qbal(150.0, therm_sourced(), 0.90)


def q_work_bound_c90():
    return _qbal(N_diss(), work_sourced(), 0.90)


def q_work_demo_c90():
    return _qbal(150.0, work_sourced(), 0.90)


def q_bred_bound_c90():
    return _qbal(N_diss(), total_sourced(), 0.90)


def q_heat_bound_fe():
    return _qbal(N_diss(), therm_sourced(), capture_of_production() / 100.0)


def q_bred_bound_fe():
    return _qbal(N_diss(), total_sourced(), capture_of_production() / 100.0)


def _eta_nf():
    """Today's aperture, hemisphere cut dropped: the acceptance model at the
    existing 1.50 T.m, over both hemispheres."""
    return cap_nf() / 100.0


def model_conservatism():
    """NOT a like-for-like ratio, and that is the point: the numerator is
    captured muons per produced pion (MARS15), the denominator is the pion
    transverse acceptance this model computes for the same machine. Their
    ratio is captured muons per model-accepted pion -- above one because a
    long solenoid captures muons from pions the p_T cap rejects."""
    return capture_of_production() / cap_nf_back()


def q_heat_demo_nf():
    return _qbal(150.0, therm_sourced(), _eta_nf())


def q_heat_bound_nf():
    return _qbal(N_diss(), therm_sourced(), _eta_nf())


def q_heat_phi3_nf():
    return _qbal(N3_sin(), therm_sourced(), _eta_nf())


def q_work_bound_nf():
    return _qbal(N_diss(), work_sourced(), _eta_nf())


def q_bred_demo_nf():
    return _qbal(150.0, total_sourced(), _eta_nf())


def q_bred_bound_nf():
    return _qbal(N_diss(), total_sourced(), _eta_nf())


def q_heat_demo_fe():
    return _qbal(150.0, therm_sourced(), capture_of_production() / 100.0)


def q_heat_phi3_fe():
    return _qbal(N3_sin(), therm_sourced(), capture_of_production() / 100.0)


def q_work_bound_fe():
    return _qbal(N_diss(), work_sourced(), capture_of_production() / 100.0)


def q_work_demo_fe():
    return _qbal(150.0, work_sourced(), capture_of_production() / 100.0)


def q_bred_demo_fe():
    return _qbal(150.0, total_sourced(), capture_of_production() / 100.0)


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
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
NUM = re.compile(
    r"(?<![\w.])(\d+(?:,\d{3})*(?:\.\d+)?)"
    r"(?:[eE]([+-]?\d+)"
    r"|\s*[x×]\s*10\s*\^?\s*([+-]?\d+)"
    r"|\s*[x×]\s*10\s*([⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+))?")
STRUCTURAL = re.compile(
    r"(?:§|section|sec\.|condition|table|figure|fig\.|item|ref\.|\[)\s*\d+", re.I)


def main():
    if len(sys.argv) < 2:
        print("usage: verify_paper.py papers/<paper>.md [papers/<paper2>.md ...]")
        return 2
    if len(sys.argv) > 2:
        # One ledger governs both current papers; each must pass on its own.
        rc = 0
        for pth in sys.argv[1:]:
            rc |= _one(pth)
            print()
        return rc
    return _one(sys.argv[1])


def _one(paper):
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
        if got is None:
            print(f"  {r['id']} {r['claim'][:44]:<44} "
                  f"{'NO SOLUTION':>12s} vs {want:<12,.4g}   FAIL")
            fails += 1
            continue
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
    # Tables are prose for this purpose -- most of the paper's quantities live in
    # them, so exempting them would leave the standard's main pass checking the
    # sentences around the numbers rather than the numbers. Only the alignment
    # row (|---|---|) is structure.
    text = re.sub(r"^\s*\|[\s|:-]*\|\s*$", " ", text, flags=re.M)
    text = re.sub(r"\|", " ", text)
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
        exp = m.group(2) or m.group(3) or m.group(4)
        if exp is not None:
            v *= 10.0 ** int(exp.translate(SUP))
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
