import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
from collections import Counter
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

fig = plt.figure(figsize=(12.6, 4.0))
gs = fig.add_gridspec(1, 3, width_ratios=[1.1, 1.0, 1.25], wspace=0.30)

# ── (a) Madelung planes slicing the (n, l) face of Lambda ───────
ax = fig.add_subplot(gs[0])
# draw admissible (n,l) cells, shade by n+l
maxn = 8
for n in range(1, maxn):
    for l in range(0, min(n, 5)):
        lev = n + l
        col = plt.cm.viridis((lev - 1) / 11.0)
        ax.add_patch(Rectangle((l - 0.44, n - 0.44), 0.88, 0.88,
                               facecolor=col, edgecolor='white', lw=0.8, alpha=0.92))
        cap = 2 * (2 * l + 1)
        ax.text(l, n, str(cap), ha='center', va='center', fontsize=7.4,
                color='white' if lev < 8 else '#111', fontweight='bold')
# diagonal lines of constant n+l
for lev in range(1, 12):
    xs = np.array([-0.6, 4.6])
    ys = lev - xs
    m = (ys >= 0.4) & (ys <= maxn - 0.4)
    if m.sum() > 1:
        ax.plot(xs[m], ys[m], color='#444', lw=0.7, ls=(0, (4, 2)), alpha=0.7, zorder=5)
ax.set_xlim(-0.75, 4.75); ax.set_ylim(0.3, maxn - 0.3)
ax.set_xticks(range(5)); ax.set_xticklabels(['s', 'p', 'd', 'f', 'g'], fontsize=9)
ax.set_yticks(range(1, maxn)); ax.tick_params(labelsize=8)
ax.set_xlabel('ℓ  (subshell)', fontsize=9)
ax.set_ylabel('n  (shell)', fontsize=9)
ax.invert_yaxis()
ax.set_title('(a)  Madelung planes n + ℓ = const', fontsize=10, loc='left')
ax.text(2.45, 1.35, 'each cell labelled\nwith capacity 2(2ℓ+1)', fontsize=7.4,
        color='#333', style='italic', ha='left')

# ── (b) period lengths as slice volumes ─────────────────────────
ax = fig.add_subplot(gs[1])
L = [(n, l) for n in range(1, 40) for l in range(0, n)]
c = Counter()
for n, l in L:
    c[n + l] += 2 * (2 * l + 1)
levs = list(range(1, 13))
vals = [c[i] for i in levs]
cols = [plt.cm.viridis((i - 1) / 11.0) for i in levs]
bars = ax.bar(levs, vals, color=cols, edgecolor='#333', lw=0.6, width=0.74)
for lv, v in zip(levs, vals):
    ax.text(lv, v + 1.6, str(v), ha='center', fontsize=7.8, fontweight='bold')
# bracket the equal pairs
for i in range(0, 12, 2):
    a, b = levs[i], levs[i + 1]
    yv = vals[i] + 9
    ax.plot([a, a, b, b], [yv - 3.5, yv, yv, yv - 3.5], color='#b02a4a', lw=1.0)
    ax.text((a + b) / 2, yv + 1.5, '=', ha='center', fontsize=9,
            color='#b02a4a', fontweight='bold')
ax.set_xlabel('Madelung level  n + ℓ', fontsize=9)
ax.set_ylabel('cells in slice', fontsize=9)
ax.set_xticks(levs); ax.tick_params(labelsize=8)
ax.set_ylim(0, 95)
ax.set_title('(b)  slice volumes pair exactly', fontsize=10, loc='left')
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top', 'right']].set_visible(False)
ax.text(0.50, 0.90, '2, 2, 8, 8, 18, 18, 32, 32, 50, 50 …\nthe period lengths',
        transform=ax.transAxes, fontsize=8, ha='center', color='#b02a4a', style='italic')

# ── (c) Janet left-step table as the projection ─────────────────
ax = fig.add_subplot(gs[2])
# Janet: rows = n+l blocks, s-block on the right, f on the left
JAN = []
order = []
for lev in range(1, 9):
    row = []
    for l in range(4, -1, -1):
        n = lev - l
        if 1 <= n and l <= n - 1 and l <= 3:
            row.append((n, l))
    if row:
        JAN.append((lev, row))

# build element lookup by (n,l) block in filling order
byblock = {}
for z in sorted(ed.E):
    n, l, k = ed.E[z]
    byblock.setdefault((n, l), []).append(z)

x0 = 0
ymap = {}
for ri, (lev, row) in enumerate(JAN):
    xoff = 0
    # count total width of the row to right-align
    width = sum(2 * (2 * l + 1) for (n, l) in row)
    start = 32 - width
    for (n, l) in row:
        cap = 2 * (2 * l + 1)
        col = ed.BLOCK_COLOR[['s', 'p', 'd', 'f'][l]]
        ax.add_patch(Rectangle((start + xoff, -ri), cap, 0.82,
                               facecolor=col, alpha=0.42, edgecolor='#666', lw=0.5))
        ax.text(start + xoff + cap / 2, -ri + 0.41, ['s', 'p', 'd', 'f'][l],
                ha='center', va='center', fontsize=8, color='#222', fontweight='bold')
        xoff += cap
    ax.text(33.4, -ri + 0.41, f'{lev}', fontsize=7.6, va='center', color='#555')
    ax.text(-1.2, -ri + 0.41, f'{width}', fontsize=7.6, va='center',
            ha='right', color='#b02a4a', fontweight='bold')

ax.text(33.4, 1.15, 'n+ℓ', fontsize=7.6, ha='center', color='#555')
ax.text(-1.2, 1.15, 'width', fontsize=7.6, ha='right', color='#b02a4a')
ax.set_xlim(-3.2, 35.5); ax.set_ylim(-7.9, 1.8)
ax.axis('off')
ax.set_title('(c)  Janet left-step table = Λ projected along n + ℓ',
             fontsize=10, loc='left')
hl = [Patch(facecolor=ed.BLOCK_COLOR[b], alpha=0.42, label=f'{b}-block')
      for b in ['s', 'p', 'd', 'f']]
ax.legend(handles=hl, frameon=False, fontsize=7.6, ncol=4,
          loc='lower center', bbox_to_anchor=(0.5, -0.10))

plt.savefig('/home/claude/fig7_order.png', bbox_inches='tight')
print('ok')
