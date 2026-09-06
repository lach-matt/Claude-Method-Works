import numpy as np, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

D = json.load(open('/home/claude/hydride_fit.json'))
zs = D['zs']; y = np.array(D['y']); pred = np.array(D['pred']); lp = np.array(D['loo_pred'])

fig = plt.figure(figsize=(12, 3.9))
gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 1, 1.05], wspace=0.30)

# ── (a) observed vs predicted ───────────────────────────────────
ax = fig.add_subplot(gs[0])
for z, o, p in zip(zs, y, pred):
    b = ed.block(z)
    ax.scatter(p, o, s=34, c=ed.BLOCK_COLOR[b], edgecolors='white', lw=0.5, zorder=3)
lim = [-130, 80]
ax.plot(lim, lim, color='#888', lw=0.9, ls='--', zorder=1)
ax.set_xlim(lim); ax.set_ylim(lim)
for z in [46, 70, 78]:
    i = zs.index(z)
    ax.annotate(ed.SYM[z], (pred[i], y[i]), fontsize=8.5, fontweight='bold',
                xytext=(6, -3), textcoords='offset points', color='#333')
ax.set_xlabel('predicted  ΔH$_f$  (kJ · mol$^{-1}$ H)', fontsize=9)
ax.set_ylabel('measured  ΔH$_f$  (kJ · mol$^{-1}$ H)', fontsize=9)
ax.set_title('(a)  two-coordinate model', fontsize=10, loc='left')
ax.grid(alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.04, 0.94, f"R² = {D['r2']:.2f}\nLOO R² = {D['loo']:.2f}\nRMSE = {D['rmse']:.0f}",
        transform=ax.transAxes, fontsize=8.2, va='top',
        bbox=dict(fc='white', ec='#bbb', lw=0.6, pad=4))
hl = [Line2D([],[],marker='o',ls='',ms=6,mfc=ed.BLOCK_COLOR[b],mec='white',label=f'{b}-block')
      for b in ['d','f']]
ax.legend(handles=hl, frameon=False, fontsize=8, loc='lower right')

# ── (b) model comparison, fit vs cross-validated ────────────────
ax = fig.add_subplot(gs[1])
tb = D['table']
keep = ['Z','k','l','l+Hcp','l+Q0','l+k','l+n+k+Q0+Hcp']
sel = [r for lab in keep for r in tb if r['model'] == lab]
labels = [r['model'].replace('Hcp','H$_{cp}$').replace('Q0','|Q$_0$|') for r in sel]
fitv = [r['r2'] for r in sel]; loov = [r['loo'] for r in sel]
ypos = np.arange(len(sel))
ax.barh(ypos+0.19, fitv, height=0.36, color='#b8cbe0', edgecolor='#33526e', lw=0.6, label='in-sample R²')
ax.barh(ypos-0.19, loov, height=0.36, color='#2c5f9e', edgecolor='#1c3f6e', lw=0.6, label='cross-validated R²')
ax.axvline(0, color='#555', lw=0.8)
ax.set_yticks(ypos); ax.set_yticklabels(labels, fontsize=8.5)
ax.invert_yaxis()
ax.set_xlabel('variance explained', fontsize=9)
ax.set_xlim(-0.16, 0.78)
ax.set_title('(b)  which coordinates matter', fontsize=10, loc='left')
ax.legend(frameon=False, fontsize=7.8, loc='lower right')
ax.grid(axis='x', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
# mark the preferred model
i_pref = keep.index('l+k')
ax.text(0.70, i_pref, '←preferred', fontsize=8, color='#0a7a3a',
        va='center', fontweight='bold')

# ── (c) permutation null ────────────────────────────────────────
ax = fig.add_subplot(gs[2])
rng = np.random.default_rng(11)
# regenerate null for display
ZS = zs; Y = y
lv = np.array([ed.E[z][1] for z in ZS], float)
kv = np.array([ed.E[z][2] for z in ZS], float)
X0 = np.column_stack([np.ones(len(Y)), lv])
b0,*_ = np.linalg.lstsq(X0, Y, rcond=None); p0 = X0@b0
base = 1-np.sum((Y-p0)**2)/np.sum((Y-np.mean(Y))**2)
null = []
for _ in range(4000):
    kk = rng.permutation(kv)
    Xp = np.column_stack([np.ones(len(Y)), lv, kk])
    bb,*_ = np.linalg.lstsq(Xp, Y, rcond=None); pp = Xp@bb
    null.append(1-np.sum((Y-pp)**2)/np.sum((Y-np.mean(Y))**2)-base)
null = np.array(null)
ax.hist(null, bins=44, color='#c9c4bc', edgecolor='#8a8378', lw=0.4)
ax.axvline(D['obs_gain'], color='#b02a4a', lw=2.0)
ax.annotate(f"observed\n+{D['obs_gain']:.2f}", xy=(D['obs_gain'], ax.get_ylim()[1]*0.72),
            xytext=(-58, 0), textcoords='offset points', fontsize=8.5,
            color='#b02a4a', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#b02a4a', lw=1.1))
ax.set_xlabel('gain in R² from adding k', fontsize=9)
ax.set_ylabel('shuffles', fontsize=9)
ax.set_title('(c)  is the k term real?', fontsize=10, loc='left')
ax.text(0.97, 0.60, f"p = {D['perm_p']:.4f}\n(10,000 shuffles)", transform=ax.transAxes,
        fontsize=8.2, ha='right', va='top',
        bbox=dict(fc='white', ec='#bbb', lw=0.6, pad=4))
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)

plt.savefig('/home/claude/fig5b_hydride.png', bbox_inches='tight')
print('ok')
