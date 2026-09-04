import math
# --- the dtmu molecule as a reaction vessel ---
R = 280e-15                     # m, internuclear separation
V = (4/3)*math.pi*R**3          # m^3, sphere of that radius
n_local = 2 / V                 # two nuclei
lam_fus = 1e12                  # s^-1, in-molecule fusion rate
rate_density = lam_fus / V      # reactions m^-3 s^-1
Q = 17.59e6 * 1.602e-19         # J per fusion
power_density = rate_density * Q
print('  THE dtmu MOLECULE AS A REACTION VESSEL')
print('     separation                 %.0f fm' % (R*1e15))
print('     vessel volume              %.3g m^3   (%.3g fm^3)' % (V, V*1e45))
print('     local nuclear density      %.3g m^-3' % n_local)
print('     instantaneous rate density %.3g fusions m^-3 s^-1' % rate_density)
print('     instantaneous power density %.3g W/m^3' % power_density)
print()
COMP=[('tokamak (ITER, n~1e20)',       1e20,  None),
      ('solid D2 at 20 K',             5.0e28,None),
      ('white dwarf core',             1e36,  None),
      ('solar core (protons)',         9.0e31, 6.5e13),
      ('ICF peak compression',         1e32,  1e39),
      ('neutron star crust',           1e42,  None),
      ('nuclear matter (saturation)',  1.7e44,None)]
print('  LOCAL NUMBER DENSITY, COMPARED')
print('     %-32s %-12s %s' % ('system','n (m^-3)','ratio  dtmu / system'))
for n,d,_ in COMP:
    print('     %-32s %-12.3g %.3g' % (n, d, n_local/d))
print()
print('  REACTION-RATE DENSITY, COMPARED')
for n,_,r in COMP:
    if r: print('     %-32s %-12.3g %.3g' % (n, r, rate_density/r))
print()
# --- duty cycle: what a macroscopic target actually sees ---
print('  THE DUTY CYCLE - WHY IT DOES NOT SCALE')
tau_mol = 1e-12                 # s, molecule lifetime before fusion
t_cycle = 3.8e-9                # s, transfer-limited cycle
duty = tau_mol/t_cycle
print('     molecule exists           %.0f ps' % (tau_mol*1e12))
print('     cycle time                %.1f ns' % (t_cycle*1e9))
print('     duty cycle                %.3g' % duty)
print()
for R_mu,lab in [(1e8,'present facilities'),(1e10,'best planned'),(1.2e15,'1 MW requirement')]:
    n_sites = R_mu * (2.197e-6)          # muons alive at steady state
    occupied_volume = n_sites * duty * V
    print('     at %-18s %.3g mu/s : %.3g muons alive, %.3g m^3 of fusing volume at any instant'
          % (lab, R_mu, n_sites, occupied_volume))
print()
V_target = 1e-3                 # 1 litre of fuel
for R_mu,lab in [(1e8,'present'),(1e10,'planned'),(1.2e15,'1 MW')]:
    n_sites = R_mu*2.197e-6
    avg_rate = R_mu*300/V_target        # fusions per m^3 per s, N=300 cycles
    print('     %-10s averaged over 1 litre : %.3g fusions m^-3 s^-1   (%.3g W/m^3)'
          % (lab, avg_rate, avg_rate*Q))
print()
print('     solar core power density  ~276 W/m^3')
print('     ITER volumetric target    ~1e6 W/m^3')
print()
print('  THE POINT')
print('     locally  : %.3g m^-3, ~%.0f orders above ICF peak' % (n_local, math.log10(n_local/1e32)))
print('     averaged : ordinary, and set entirely by the muon supply rate')
print('     the ratio between them is the duty cycle x site count = the flux gap.')