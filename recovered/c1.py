#!/usr/bin/env python3
"""C1: does the induced field commutator on a null hypersurface vanish between
distinct generators?

Setup.  A massless scalar on a null hypersurface N with coordinates (u, y),
u affine along the generators, y transverse.  The presymplectic potential is

    theta = int_N  delta phi  L_l phi  eta

so the presymplectic form is

    Omega = int du d^{d-2}y  sqrt(q)(u,y)  [ delta phi  ^  d_u delta phi ]

On a NON-EXPANDING horizon Theta = 0, so L_l mu = Theta mu = 0 and sqrt(q) is a
function of y ALONE.  Crucially Omega contains NO TRANSVERSE DERIVATIVES.

We discretise and invert Omega numerically, then read off the bracket.
"""
import numpy as np

def build_omega(NY, NU, sqrtq, transverse_coupling=0.0):
    """Antisymmetric symplectic matrix on the discretised null surface.
    Field values phi[i,j], i over generators (y), j over affine parameter (u).
    Omega(phi, phi') = sum_y sqrt(q)(y) sum_u [ phi d_u phi' - phi' d_u phi ] du
    transverse_coupling>0 adds an artificial d_y term, as a control."""
    N = NY*NU
    idx = lambda i,j: i*NU + j
    O = np.zeros((N,N))
    du = 1.0
    for i in range(NY):
        w = sqrtq[i]
        for j in range(NU):
            # forward difference in u, antisymmetrised
            jp = j+1
            if jp < NU:
                a,b = idx(i,j), idx(i,jp)
                O[a,b] += w/(2*du); O[b,a] -= w/(2*du)
    if transverse_coupling:
        for i in range(NY-1):
            for j in range(NU):
                a,b = idx(i,j), idx(i+1,j)
                O[a,b] += transverse_coupling; O[b,a] -= transverse_coupling
    return O

def block_structure(M, NY, NU, tol=1e-9):
    """Max |entry| in off-diagonal generator blocks."""
    off = 0.0
    for i in range(NY):
        for k in range(NY):
            if i==k: continue
            blk = M[i*NU:(i+1)*NU, k*NU:(k+1)*NU]
            off = max(off, np.abs(blk).max())
    dia = 0.0
    for i in range(NY):
        blk = M[i*NU:(i+1)*NU, i*NU:(i+1)*NU]
        dia = max(dia, np.abs(blk).max())
    return off, dia

print('  C1 -- DOES THE INDUCED BRACKET FACTORISE OVER GENERATORS?')
print()
for NY,NU in [(4,6),(6,8),(8,10)]:
    rng=np.random.default_rng(0)
    sqrtq = 1.0 + 0.5*rng.random(NY)          # a y-dependent transverse metric
    O = build_omega(NY,NU,sqrtq)
    offO,diaO = block_structure(O,NY,NU)
    # invert on the non-degenerate part
    Oi = np.linalg.pinv(O)
    offB,diaB = block_structure(Oi,NY,NU)
    print('  NY=%d generators, NU=%d points   sqrt(q) varies over y' % (NY,NU))
    print('     Omega       : max off-generator block %.3e   max within-generator %.3e' % (offO,diaO))
    print('     Omega^{-1}  : max off-generator block %.3e   max within-generator %.3e' % (offB,diaB))
    print('     -> bracket between DISTINCT generators: %s'
          % ('ZERO' if offB<1e-9 else 'NONZERO %.3e'%offB))
    print()

print('  CONTROL: add an artificial transverse derivative term to Omega')
NY,NU=6,8
rng=np.random.default_rng(0); sqrtq=1.0+0.5*rng.random(NY)
for tc in [0.0, 0.05, 0.2]:
    O=build_omega(NY,NU,sqrtq,transverse_coupling=tc)
    Oi=np.linalg.pinv(O)
    offB,_=block_structure(Oi,NY,NU)
    print('     transverse coupling %.2f  ->  off-generator bracket %.3e  %s'
          % (tc,offB,'ZERO' if offB<1e-9 else 'NONZERO'))
print()
print('  THE ANALYTIC FORM, FOR COMPARISON')
print('     Omega = int du d^{d-2}y sqrt(q)(y) [ delta phi ^ d_u delta phi ]')
print('     is block diagonal in y because it contains NO d_y.')
print('     inverting block by block gives')
print('        { phi(u,y), phi(u\',y\') }  =  ( 1 / (4 sqrt(q)(y)) ) sgn(u-u\') delta^{d-2}(y-y\')')
print('     which vanishes for y != y\'.')
print()
print('  WHAT THIS DOES AND DOES NOT SHOW')
print('     SHOWS: if the symplectic form has no transverse derivatives, the bracket')
print('            is diagonal in y, and this is a matter of linear algebra, not symmetry.')
print('            it holds for ANY y-dependence of sqrt(q), hence on any null surface')
print('            with u-independent transverse metric -- which is exactly an NEH.')
print()
print('     DOES NOT SHOW: that the symplectic form has no transverse derivatives for')
print('            an INTERACTING theory, or for fields with gauge/tensor structure.')
print('            for a minimally coupled scalar the potential is delta phi L_l phi eta,')
print('            with no d_y, by inspection. for gravitons Chandrasekaran-Flanagan\'s')
print('            Omega_H = int delta Psi ^ delta Psi-dot has the same form.')
print()
print('     AND DOES NOT SHOW: anything about the STATE. the ALGEBRA factorising')
print('            leaves the Markov question (C2) untouched.')
