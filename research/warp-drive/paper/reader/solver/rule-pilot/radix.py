import pickle, math, numpy as np
zs = pickle.load(open('/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/bsolv/s2A_dd/tab_30_z.pkl','rb'))
tot = {}; n = 0; neg = 0; zeros = 0
def nsym(v, b):
    v = abs(v); s = 1
    while v >= b: v //= b; s += 1
    return s
for key, (p, z) in zs.items():
    for a in range(z.shape[0]):
        for b in range(z.shape[1]):
            row = z[a, b]; nz = np.nonzero(row)[0]
            if len(nz) == 0: continue
            for v in row[:nz[-1] + 1]:
                v = int(v); n += 1; neg += v < 0; zeros += v == 0
                for base in (10, 32, 64, 85):
                    tot[base] = tot.get(base, 0) + nsym(v, base)
print('entries', n, 'negative', neg, 'zeros', zeros)
for base in (10, 32, 64, 85):
    chars = tot[base] + neg + n          # digits + sign + separator
    print('base %d: symbols %d (%.2f per entry); with sign and separator %d; ratio to decimal %.3f' % (base, tot[base], tot[base]/n, chars, chars / (tot[10] + neg + n)))
# self-delimiting variant: sign folded into the first symbol and no separator (needs a terminator alphabet split)
