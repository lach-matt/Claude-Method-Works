"""numerical Kretschmann scalar from g, dg, ddg at many points; and the jets of the P3 s-chart metric"""
import numpy as np
import sympy as sp


def kretschmann(g, dg, ddg, ricci=False):
    """g (N,d,d); dg (N,d,d,d) with dg[:,c,a,b] = d_c g_ab; ddg (N,d,d,d,d) ddg[:,c,e,a,b] = d_c d_e g_ab"""
    gi = np.linalg.inv(g)
    # Christoffel of the first kind, then second kind
    G1 = 0.5 * (np.einsum("nbda->nabd", dg) + np.einsum("ndab->nabd", dg) - np.einsum("nabd->nabd", dg))
    # G1[n,a,b,d] = 1/2 (d_b g_da + d_d g_ba - d_a g_bd)  : Gamma_{a b d} (first index lowered)
    G1 = 0.5 * (np.transpose(dg, (0, 2, 1, 3)) + np.transpose(dg, (0, 2, 3, 1)) - dg)
    # check: dg[n,c,a,b]; want G1[n,a,b,c] = 1/2(d_b g_ac + d_c g_ab - d_a g_bc)
    G1 = 0.5 * (np.einsum("nbac->nabc", dg) + np.einsum("ncab->nabc", dg) - np.einsum("nabc->nabc", dg))
    Gam = np.einsum("npa,nabc->npbc", gi, G1)                       # Gamma^p_bc
    dgi = -np.einsum("npa,neab,nbq->nepq", gi, dg, gi)              # d_e g^pq
    # d_e G1[a,b,c] = 1/2 (d_e d_b g_ac + d_e d_c g_ab - d_e d_a g_bc)
    dG1 = 0.5 * (np.einsum("nebac->neabc", ddg) + np.einsum("necab->neabc", ddg) - np.einsum("neabc->neabc", ddg))
    dGam = np.einsum("nepa,nabc->nepbc", dgi, G1) + np.einsum("npa,neabc->nepbc", gi, dG1)   # d_e Gamma^p_bc
    # R^a_bcd = d_c Gam^a_db - d_d Gam^a_cb + Gam^a_ce Gam^e_db - Gam^a_de Gam^e_cb
    R = (np.einsum("ncadb->nabcd", dGam) - np.einsum("ndacb->nabcd", dGam)
         + np.einsum("nace,nedb->nabcd", Gam, Gam) - np.einsum("nade,necb->nabcd", Gam, Gam))
    Rl = np.einsum("nap,npbcd->nabcd", g, R)
    Ru = np.einsum("nabcd,nbq,ncr,nds->naqrs", R, gi, gi, gi)
    if ricci == "mixed":
        Ric = np.einsum("nabad->nbd", R)
        return np.einsum("nab,nbc->nac", gi, Ric)
    if ricci:
        Ric = np.einsum("nabad->nbd", R)
        return np.einsum("nabcd,nabcd->n", Rl, Ru), np.einsum("nbd,nbd->n", gi, Ric)
    return np.einsum("nabcd,nabcd->n", Rl, Ru)


def sym_jets(gsym, coords, funcs, jetmap):
    """lambdify g, dg, ddg of a sympy metric in coords whose entries contain funcs(s, x); jetmap maps
    Derivative / function objects to jet symbols.  Returns f(args) -> (g, dg, ddg) at theta = pi/2"""
    d = len(coords)
    G = gsym
    dG = [[[sp.diff(G[a, b], c) for b in range(d)] for a in range(d)] for c in coords]
    ddG = [[[[sp.diff(G[a, b], c, e) for b in range(d)] for a in range(d)] for e in coords] for c in coords]
    return G, dG, ddG


if __name__ == "__main__":
    # test 1: AdS5 in Poincare form ds^2 = (dz^2 + dx_mu dx^mu)/z^2 -> K = 40
    t, r, ch, th, ph = sp.symbols("t r chi theta phi")
    co = [t, r, ch, th, ph]

    def numeric(G, pts):
        d = 5
        dG = [[[sp.diff(G[a, b], c) for b in range(d)] for a in range(d)] for c in co]
        ddG = [[[[sp.diff(G[a, b], c, e) for b in range(d)] for a in range(d)] for e in co] for c in co]
        fg = sp.lambdify(co, G, "numpy"); fd = sp.lambdify(co, dG, "numpy"); fdd = sp.lambdify(co, ddG, "numpy")
        g = np.array([np.array(fg(*p), dtype=float) for p in pts])
        dg = np.array([np.array(fd(*p), dtype=float) for p in pts])
        ddg = np.array([np.array(fdd(*p), dtype=float) for p in pts])
        return kretschmann(g, dg, ddg)

    G = sp.diag(-1 / r**2, 1 / r**2, 1 / r**2, 1 / r**2, 1 / r**2)
    print("AdS5 Poincare:", numeric(G, [(0, 0.7, 0.3, 1.1, 0.2), (0, 2.0, 0.1, 0.5, 0.0)]), "expect 40")
    mu_ = sp.Rational(3, 2)
    f = 1 - mu_ / r**2
    G = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(ch)**2, r**2 * sp.sin(ch)**2 * sp.sin(th)**2)
    pts = [(0, 1.7, 0.6, 1.2, 0.0), (0, 3.0, 1.0, sp.pi / 2, 0.0)]
    print("Tangherlini:", numeric(G, [(a, b, c, float(dd), e) for a, b, c, dd, e in pts]),
          "expect", [72 * 1.5**2 / p[1]**8 for p in pts])
    # 4D Schwarzschild padded with a flat fifth direction: K = 48 M^2/r^6
    M = 1.0
    f4 = 1 - 2 * M / r
    G = sp.diag(-f4, 1 / f4, r**2, r**2 * sp.sin(ch)**2, 1)
    print("Schwarzschild x R:", numeric(G, [(0, 2.5, 0.7, 0, 0)]), "expect", 48 / 2.5**6)
