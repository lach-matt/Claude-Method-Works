import numpy as np, eldata as ed
from scipy import stats

print("="*76)
print("OPTION A: LABEL LATTICE CELLS WITH EXCHANGE-ENERGY DATA")
print("="*76)
print("""  The physics of anomalous configurations: for a d-block element the
  competition is between (n-1)d^k ns^2 and (n-1)d^(k+1) ns^1. Promoting an
  s electron to d costs promotion energy but gains exchange energy, which
  scales with the number of parallel-spin pairs created. Exchange stabilisation
  for a subshell with k electrons of parallel spin goes as K*C(m,2) where m
  is the number of unpaired electrons.

  Λ cannot generate K. But Λ tells us m directly from (ℓ,k) via Hund's rule.
  So: label each cell with its Hund-rule unpaired count, and the number of
  exchange pairs. That is metric-adjacent information indexed BY the lattice.""")

def hund_unpaired(l,k):
    """Unpaired electrons in subshell (l,k) under Hund's first rule."""
    cap_half = 2*l+1          # orbitals
    if k <= cap_half: return k
    return 2*cap_half - k

def exch_pairs(l,k):
    """Parallel-spin pairs = C(m_up,2) + C(m_down,2)."""
    orb = 2*l+1
    up = min(k, orb)
    dn = max(0, k-orb)
    return up*(up-1)//2 + dn*(dn-1)//2

# label every cell
print()
print("  Exchange-pair count E(ℓ,k) across the lattice (a Λ-indexed label):")
print(f"  {'ℓ':>3} " + " ".join(f"{k:>3}" for k in range(1,15)))
for l in range(4):
    row=[]
    for k in range(1,15):
        row.append(f"{exch_pairs(l,k):>3}" if k<=2*(2*l+1) else "  ·")
    print(f"  {l:>3} " + " ".join(row))

# Now: do anomalies cluster in this labelling?
ANOM = {24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
print()
print("="*76)
print("DOES THE EXCHANGE LABEL SEPARATE ANOMALOUS FROM NORMAL ELEMENTS?")
print("="*76)

# For d-block and f-block elements, compute the exchange GAIN of promoting
# s->subshell: E(l,k+1) - E(l,k)
rows=[]
for z in sorted(ed.E):
    n,l,k = ed.E[z]
    if l < 2: continue           # d and f blocks only
    if k >= 2*(2*l+1): continue  # need room to promote
    gain = exch_pairs(l,k+1) - exch_pairs(l,k)
    rows.append((z, ed.SYM[z], n,l,k, gain, z in ANOM))

ga=[r[5] for r in rows if r[6]]
gn=[r[5] for r in rows if not r[6]]
print(f"  d/f-block elements with room to promote: {len(rows)}")
print(f"    anomalous ({len(ga)}): mean exchange gain = {np.mean(ga):.2f}")
print(f"    normal    ({len(gn)}): mean exchange gain = {np.mean(gn):.2f}")
t,p = stats.ttest_ind(ga,gn,equal_var=False)
print(f"    Welch t = {t:+.2f},  p = {p:.4f}")
u,pu = stats.mannwhitneyu(ga,gn,alternative='two-sided')
print(f"    Mann-Whitney U p = {pu:.4f}")