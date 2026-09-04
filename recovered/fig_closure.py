import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Patch
from matplotlib.lines import Line2D

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

fig = plt.figure(figsize=(12.4, 4.1))
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.0, 1.12], wspace=0.30)

OK  = '#2c5f9e'
BAD = '#b02a4a'
GREY= '#b9b3a9'

# ── (a) k-constraint: one-sided, closure holds ──────────────────
ax = fig.add_subplot(gs[0])
ls = np.arange(0, 4)
for l in ls:
    cap = 2*(2*l+1)
    ax.add_patch(Rectangle((l-0.32, 1), 0.64, cap-1+0.0,
                           facecolor=OK, alpha=0.16, edgecolor=OK, lw=0.9))
    ax.plot([l-0.32, l+0.32], [cap, cap], color=OK, lw=2.0)
    ax.plot([l-0.32, l+0.32], [1, 1], color='#333', lw=1.6)
ax.text(3.55, 14, 'k ≤ 2(2ℓ+1)\nupper bound,\nrises with ℓ', fontsize=8,
        color=OK, va='center')
ax.text(3.55, 1.0, 'k ≥ 1\nconstant floor', fontsize=8, color='#333', va='center')

# demonstrate a meet staying inside
a = (2, 9); b = (3, 6)
mtp = (min(a[0],b[0]), min(a[1],b[1]))
for pt, lab, col in [(a,'a',OK), (b,'b',OK), (mtp,'a ∧ b',OK)]:
    ax.scatter([pt[0]],[pt[1]], s=52, color=col, zorder=6, edgecolors='white', lw=0.8)
    ax.annotate(lab, pt, xytext=(7,5), textcoords='offset points',
                fontsize=8.5, fontweight='bold', color=col)
ax.plot([a[0],mtp[0]],[a[1],mtp[1]], color=OK, lw=1.0, ls=(0,(3,2)), zorder=4)
ax.plot([b[0],mtp[0]],[b[1],mtp[1]], color=OK, lw=1.0, ls=(0,(3,2)), zorder=4)
ax.text(1.0, 16.4, 'meet lands inside Λ  ✓', fontsize=9, color=OK, fontweight='bold')

ax.set_xlim(-0.7, 5.4); ax.set_ylim(0, 17.6)
ax.set_xticks(range(4)); ax.set_xticklabels(['s','p','d','f'], fontsize=9)
ax.set_xlabel('ℓ', fontsize=9.5); ax.set_ylabel('k  (occupancy)', fontsize=9)
ax.set_title('(a)  k: one-sided bound', fontsize=10, loc='left')
ax.grid(alpha=0.15, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)

# ── (b) m-constraint: two-sided, closure fails ──────────────────
ax = fig.add_subplot(gs[1])
for l in ls:
    ax.add_patch(Rectangle((l-0.32, -l), 0.64, 2*l if l>0 else 0.001,
                           facecolor=BAD, alpha=0.14, edgecolor=BAD, lw=0.9))
    ax.plot([l-0.32, l+0.32], [ l,  l], color=BAD, lw=2.0)
    ax.plot([l-0.32, l+0.32], [-l, -l], color=BAD, lw=2.0)
ax.text(3.55, 2.6, 'm ≤ ℓ\nupper bound', fontsize=8, color=BAD, va='center')
ax.text(3.55, -2.6, 'm ≥ −ℓ\nfloor VARIES\nwith ℓ', fontsize=8, color=BAD, va='center',
        fontweight='bold')

a2 = (3, -3); b2 = (1, 1)
mt2 = (min(a2[0],b2[0]), min(a2[1],b2[1]))   # (1, -3) : |m|>l  -> outside
for pt, lab, col, inside in [(a2,'a',BAD,True), (b2,'b',BAD,True), (mt2,'a ∧ b',BAD,False)]:
    ax.scatter([pt[0]],[pt[1]], s=52,
               color=col if inside else 'white', zorder=6,
               edgecolors=col, lw=1.6)
    ax.annotate(lab, pt, xytext=(7,5), textcoords='offset points',
                fontsize=8.5, fontweight='bold', color=col)
ax.plot([a2[0],mt2[0]],[a2[1],mt2[1]], color=BAD, lw=1.0, ls=(0,(3,2)), zorder=4)
ax.plot([b2[0],mt2[0]],[b2[1],mt2[1]], color=BAD, lw=1.0, ls=(0,(3,2)), zorder=4)
ax.annotate('', xy=(1.0,-3.0), xytext=(1.0,-1.0),
            arrowprops=dict(arrowstyle='-|>', color=BAD, lw=1.5))
ax.text(0.15, -3.9, 'meet falls OUTSIDE Λ  ✗', fontsize=9, color=BAD, fontweight='bold')
ax.axhline(0, color='#999', lw=0.6)

ax.set_xlim(-0.7, 5.4); ax.set_ylim(-4.6, 4.4)
ax.set_xticks(range(4)); ax.set_xticklabels(['s','p','d','f'], fontsize=9)
ax.set_xlabel('ℓ', fontsize=9.5); ax.set_ylabel('m  (magnetic)', fontsize=9)
ax.set_title('(b)  m: two-sided bound', fontsize=10, loc='left')
ax.grid(alpha=0.15, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)

# ── (c) tally of the four coordinate systems ────────────────────
ax = fig.add_subplot(gs[2])
rows = [
 ('(n, ℓ, k)\noriginal',              0,    0, True,  'k has a constant floor'),
 ('(n, ℓ, m, s)\nhydrogenic unfold',  0, 4040, False, 'm ≥ −ℓ floor varies'),
 ('(n, ℓ, m+ℓ, s)\nshifted unfold',   0,    0, True,  'floor restored, but\nm+ℓ is not m'),
 ('(n, ℓ, m-index, s)\nre-indexed',   0,    0, True,  'same objection'),
]
y = np.arange(len(rows))[::-1]
for i,(lab, bj, bm, ok, note) in enumerate(rows):
    yy = y[i]
    col = OK if ok else BAD
    ax.add_patch(Rectangle((0.02, yy-0.34), 0.30, 0.68, facecolor=col, alpha=0.12,
                           edgecolor=col, lw=0.9))
    ax.text(0.17, yy, lab, ha='center', va='center', fontsize=7.8, color='#222')
    ax.text(0.40, yy+0.13, f'meet failures: {bm}', fontsize=8,
            color=col, fontweight='bold' if not ok else 'normal', va='center')
    ax.text(0.40, yy-0.16, note, fontsize=7.4, color='#555', va='center')
    ax.text(0.97, yy, 'LATTICE' if ok else 'NOT A\nLATTICE', ha='right', va='center',
            fontsize=8, color=col, fontweight='bold')
ax.set_xlim(0,1.02); ax.set_ylim(-0.7, len(rows)-0.3)
ax.axis('off')
ax.set_title('(c)  closure across coordinate systems', fontsize=10, loc='left')
ax.text(0.02, -0.62, 'All four contain exactly 210 cells. Only the bound structure differs.',
        fontsize=7.6, style='italic', color='#666')

plt.savefig('/home/claude/fig8_closure.png', bbox_inches='tight')
print('ok')
