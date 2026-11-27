"""The axis-regular evaluation scheme of the residual (no division by 1 +- x, no sqrt(w)): returns the eight
components as f_ab / rho with f_lx, f_nx divided by q = sqrt(w).  Every intermediate quantity is a polynomial in x and
the 2-jets of the fields, times powers of 1/R, e^{+-S}, e^{+-2W}.  Works on sympy symbols or on any number type with
+, -, *, / (division only by R, OM2, ES, muh and constants)."""

def regular_components(x, J, ES, OM2, one=1):
    R, m, n, W, s = (J[f] for f in ('R', 'm', 'n', 'W', 's'))
    w = (one + x) * (one - x)
    iR = one / R['']
    l = {a: R[a] * iR for a in ('u', 'v', 'x')}
    ll = {ab: R[ab] * iR - l[ab[0]] * l[ab[1]] for ab in ('uu', 'uv', 'vv', 'ux', 'vx', 'xx')}
    lr = dict(l); lr.update(ll)
    def comb(a):   # S, P, Q for a in u, v, uu, uv, vv
        return (((one + x) * m[a] + (one - x) * n[a]) / 3, (2 * (one + x) * m[a] - (one - x) * n[a]) / 3,
                (2 * (one - x) * n[a] - (one + x) * m[a]) / 3)
    def xd(mm, nn, mx, nx):
        return ((mm - nn + (one + x) * mx + (one - x) * nx) / 3, (2 * mm + nn + 2 * (one + x) * mx - (one - x) * nx) / 3,
                (-2 * nn - mm + 2 * (one - x) * nx - (one + x) * mx) / 3)
    S, P, Q = {}, {}, {}
    for a in ('u', 'v', 'uu', 'uv', 'vv'):
        S[a], P[a], Q[a] = comb(a)
    S['x'], P['x'], Q['x'] = xd(m[''], n[''], m['x'], n['x'])
    S['xx'] = (2 * m['x'] - 2 * n['x'] + (one + x) * m['xx'] + (one - x) * n['xx']) / 3
    P['xx'] = (4 * m['x'] + 2 * n['x'] + 2 * (one + x) * m['xx'] - (one - x) * n['xx']) / 3
    Q['xx'] = (-4 * n['x'] - 2 * m['x'] + 2 * (one - x) * n['xx'] - (one + x) * m['xx']) / 3
    for a in ('u', 'v'):
        S[a + 'x'], P[a + 'x'], Q[a + 'x'] = xd(m[a], n[a], m[a + 'x'], n[a + 'x'])
    keys = ('u', 'v', 'x', 'uu', 'uv', 'vv', 'ux', 'vx', 'xx')
    z = {a: lr[a] - S[a] for a in keys}       # regular parts zeta°, A°, B°
    A = {a: lr[a] + P[a] for a in keys}
    B = {a: lr[a] + Q[a] for a in keys}
    # weighted x-derivatives: check = w psi_x, ccheck = w^2 psi_xx (exact, regular)
    zc = w * z['x'] + x;           zcc = w * w * z['xx'] + (one + x * x)
    Ac = w * A['x'] + (one - x) / 2; Acc = w * w * A['xx'] - (one - x) * (one - x) / 2
    Bc = w * B['x'] - (one + x) / 2; Bcc = w * w * B['xx'] - (one + x) * (one + x) / 2
    b = w * s['']
    bu, bv, buv, bvv = w * s['u'], w * s['v'], w * s['uv'], w * s['vv']
    bx = w * s['x'] - 2 * x * s['']
    bux, bvx = w * s['ux'] - 2 * x * s['u'], w * s['vx'] - 2 * x * s['v']
    bxx = w * s['xx'] - 4 * x * s['x'] - 2 * s['']
    iO = one / OM2
    muh = 2 * ES * iR                       # mu = q muh
    imuh = R[''] / (2 * ES)
    tah = s['v'] * imuh * iO / 4            # tau = q tah
    etah = muh * W['x']                     # eta = q etah
    Yz = z['u'] + s[''] * zc
    om, omb = W['v'], W['u'] + b * W['x']
    k, kb = z['v'], z['u'] + s[''] * zc + bx
    Lk = z['vv']; Yk = z['uv'] + b * z['vx']
    Lkb = z['uv'] + s['v'] * zc + b * z['vx'] + bvx
    Lomb = W['uv'] + bv * W['x'] + b * W['vx']
    Ykb = z['uu'] + s['u'] * zc + 2 * b * z['ux'] + bux + s[''] * bx * zc + s[''] * s[''] * zcc + b * bxx
    Letah = muh * (W['vx'] - z['v'] * W['x'])
    Yetah = muh * (W['ux'] + b * W['xx'] - Yz * W['x'])
    Eeta = muh * muh * (w * W['xx'] - zc * W['x'])
    Ltah = tah * (z['v'] - 2 * om) + s['vv'] * imuh * iO / 4
    Ytah = tah * (Yz - 2 * omb) + (s['uv'] + s[''] * (w * s['vx'] - 2 * x * s['v'])) * imuh * iO / 4
    Etau = muh * tah * (zc - 2 * w * W['x']) + bvx * iO / 4
    RLL = -Lk + 2 * om * k - k * k
    RYY = -Ykb + 2 * omb * kb - kb * kb
    RLEh = -Letah + Ltah + 2 * k * tah
    RYEh = -Yetah - Ytah - 2 * kb * tah
    RLY = -Lkb - 2 * Lomb - k * kb + OM2 * (2 * Eeta + 2 * Etau + w * (4 * etah * etah + 8 * etah * tah - 4 * tah * tah))
    REE = -2 * Eeta - 2 * w * (etah * etah + tah * tah) + (Lkb + Yk + 2 * k * kb) * iO / 2
    def psi(p, pc, pcc):
        d = {'L': p['v'], 'Y': p['u'] + s[''] * pc}
        d['LL'] = p['vv']
        d['LY'] = p['uv'] + s['v'] * pc + b * p['vx']
        d['YY'] = p['uu'] + s['u'] * pc + 2 * b * p['ux'] + s[''] * bx * pc + s[''] * s[''] * pcc
        d['hLY'] = d['LY'] - 2 * OM2 * (etah + tah) * muh * pc
        d['MLL'] = d['LL'] - 2 * om * d['L'] + d['L'] * d['L']
        d['MYY'] = d['YY'] - 2 * omb * d['Y'] + d['Y'] * d['Y']
        d['MLY'] = d['hLY'] + d['L'] * d['Y']
        return d
    dA, dB = psi(A, Ac, Acc), psi(B, Bc, Bcc)
    lS = l['x'] + 2 * S['x']                # A°_x + B°_x - zeta°_x
    Sig_EE = (w * (A['xx'] + B['xx'] + A['x'] * A['x'] + B['x'] * B['x'] - z['x'] * (A['x'] + B['x']))
              + (one - 2 * x) * A['x'] - (one + 2 * x) * B['x'] + x * z['x'] - one / 2)
    Sig_11 = w * (A['xx'] + A['x'] * lS) - 2 * x * A['x'] + (one - x) / 2 * lS - one / 2
    Sig_22 = w * (B['xx'] + B['x'] * lS) - 2 * x * B['x'] - (one + x) / 2 * lS - one / 2
    ThA = w * (A['x'] * (A['x'] - z['x']) + A['xx']) + (one - x) / 2 * (A['x'] - z['x']) + (one - 3 * x) / 2 * A['x'] - one / 4
    ThB = w * (B['x'] * (B['x'] - z['x']) + B['xx']) - (one + x) / 2 * (B['x'] - z['x']) - (one + 3 * x) / 2 * B['x'] - one / 4
    a1 = (one + x) * A['x'] + one / 2       # (1 + x) A_x
    b1 = (one - x) * B['x'] - one / 2       # (1 - x) B_x
    sumMLEh = (muh * (A['vx'] + B['vx'] + a1 * m['v'] + b1 * n['v']) - (etah + tah) * (A['v'] + B['v']))
    sumMYEh = (muh * (A['ux'] + B['ux'] + a1 * m['u'] + b1 * n['u'] + s[''] * (ThA + ThB))
               - (etah - tah) * (dA['Y'] + dB['Y']))
    # E E parts without the mu^2 psi_x psi_x pieces (those are in the Sigmas)
    hEEr = lambda d: -(kb * d['L'] + k * d['Y']) * iO / 2
    NLL = RLL - dA['MLL'] - dB['MLL']
    NYY = RYY - dA['MYY'] - dB['MYY']
    NLY = RLY - dA['MLY'] - dB['MLY']
    NEE = REE - (hEEr(dA) + hEEr(dB)) - muh * muh * Sig_EE
    ipr = lambda d1, d2: -(d1['L'] * d2['Y'] + d1['Y'] * d2['L']) * iO / 2
    boxr = lambda d: -d['hLY'] * iO + hEEr(d)
    f = {'ll': NLL, 'ln': NLY * iO / 2, 'nn': NYY * iO * iO / 4,
         'lx': RLEh - sumMLEh, 'nx': (RYEh - sumMYEh) * iO / 2, 'xx': NEE,
         '11': -(boxr(dA) + ipr(dA, dA) + ipr(dA, dB)) - muh * muh * Sig_11,
         '22': -(boxr(dB) + ipr(dB, dB) + ipr(dA, dB)) - muh * muh * Sig_22}
    return f
