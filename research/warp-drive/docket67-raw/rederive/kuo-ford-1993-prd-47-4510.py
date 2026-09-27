#!/usr/bin/env python3
"""DOCKET 67 audit: Kuo & Ford, Phys. Rev. D 47, 4510 (1993) -- the PUBLISHED JOURNAL VERSION.

The tree's use (fluctuation.py:122-128, 135, 483; ledger.py:1037-1042, 861) is a SCOPE statement:
the journal version is NAMED-NOT-READ, and the v1 discrepancies MUST NOT be quoted as errors in
it until it is read.  What is checkable here:
  B  bibliographic facts from files actually on disk (v1 harvest header; journal page range and
     month as restated by later papers' bibliographies)
  A  the v1 discrepancies that the scope clause protects, re-derived (so the clause is protecting
     real, reproducible v1 findings and not artefacts) -- exact Fock algebra + z3
  T  the tree is internally consistent with its own scope: JOURNAL_VERSION_READ False, the clause
     present, no file quoting a journal-version equation
What is NOT checkable here: the journal text itself (alphaXiv quota exceeded; journals.aps.org,
arxiv.org, pubmed, crossref, inspirehep all refused by the egress proxy on 2026-09-26).
Read-only: nothing under research/ is written.
"""
import hashlib, os, re, sys, importlib.util
import sympy as sp
import z3

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
WD = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []
def chk(name, got, want):
    ok = (got == want)
    print("  [%s] %-70s %s" % ("ok" if ok else "FAIL", name, got))
    if not ok: fails.append(name)

print("B. BIBLIOGRAPHIC FACTS, from files on disk")
v1 = os.path.join(D67, "src/casmag/all/gr-qc_9304008v1.txt")
raw = open(v1, "rb").read()
chk("B1 v1 harvest md5", hashlib.md5(raw).hexdigest(), "f1a6628604751cf61b2a4bd411b00153")
t = raw.decode("utf-8", "replace")
chk("B2 v1 header 'arXiv:gr-qc/9304008v1 6 Apr 1993'", "arXiv:gr-qc/9304008v1 6 Apr 1993" in t, True)
chk("B3 preprint 'TUTP-93-1' / 'February 1993'", ("TUTP-93-1" in t) and ("February 1993" in t), True)
chk("B4 v1 carries no journal reference (no 'Phys. Rev. D 47' in its text)", "Phys. Rev. D 47" in t or "4510" in t, False)
pages = len(re.findall(r"===== PAGE \d+ =====", t))
chk("B5 v1 preprint pages in harvest", pages, 19)
r1 = open(os.path.join(D67, "src/casmag/all/2512.17789v2.txt"), encoding="utf-8", errors="replace").read()
chk("B6 journal page range 4510-4519 restated (2512.17789v2 ref [7])", "4510–4519" in r1 or "4510-4519" in r1, True)
r2 = open(os.path.join(D67, "src/_cache_gr-qc_9805037.txt"), encoding="utf-8", errors="replace").read()
chk("B7 journal month 'May 1993' restated (gr-qc/9805037 ref [46])", bool(re.search(r"vol\. 47, p\. 4510, May\s+1993", r2)), True)
print("     => journal: 10 printed pages, May 1993; v1: 19 preprint pages, posted 6 Apr 1993,")
print("        dated Feb 1993.  v1 precedes the journal issue by ~5-6 weeks: it is a pre-proof")
print("        manuscript; whether proofs changed any equation is NOT determinable from here.")

print("\nA. THE v1 DISCREPANCIES THE CLAUSE PROTECTS, RE-DERIVED (exact Fock algebra)")
K, eps = sp.symbols("K epsilon", positive=True)
c = sp.symbols("c", real=True)          # c = cos(2 theta)
th = sp.symbols("theta", real=True)
N = 8
def a_op():
    M = sp.zeros(N, N)
    for n in range(1, N): M[n-1, n] = sp.sqrt(n)
    return M
a = a_op(); ad = a.T
z = sp.exp(2*sp.I*th)
T = K*(2*ad*a - z*a*a - sp.conjugate(z)*ad*ad)       # :T00: single mode, KF (2.10)-(2.14) as the tree reads them
# normal-ordered square :T^2: -- expand in a+^m a^n with all a+ left
def nsq():
    # :T^2: = K^2 [4 a+^2 a^2 + z^2 a^4 + zb^2 a+^4 - 4 z a+ a^3 - 4 zb a+^3 a + 2 a+^2 a^2]
    zb = sp.conjugate(z)
    return K**2*(4*ad**2*a**2 + z**2*a**4 + zb**2*ad**4 - 4*z*ad*a**3 - 4*zb*ad**3*a + 2*ad**2*a**2)
T2 = nsq()
psi = sp.zeros(N, 1); psi[0] = 1; psi[2] = eps
nrm = 1 + eps**2
ev = lambda O: sp.simplify((psi.T*O*psi)[0] / nrm)
rho = sp.simplify(sp.expand_complex(ev(T)).rewrite(sp.cos))
T2v = sp.simplify(sp.expand_complex(ev(T2)).rewrite(sp.cos))
rho_c = sp.simplify(sp.expand_trig(rho).subs(sp.cos(2*th), c))
rho_c = sp.simplify(rho_c.subs(sp.cos(th)**2, (1+c)/2))
print("     exact <:T00:>   =", sp.factor(rho_c))
print("     exact <:T00^2:> =", sp.factor(T2v))
middle = 2*K*eps*(2*eps - sp.sqrt(2)*c)/nrm
final_printed = K*eps*(2*eps - sp.sqrt(2)*c)/nrm
chk("A1 exact rho equals (2.16) middle line", sp.simplify(rho_c - middle), 0)
chk("A2 (2.16) printed final / exact", sp.simplify(final_printed/middle), sp.Rational(1, 2))
p37 = 12*K**2*eps**2/nrm**2
chk("A3 exact <:T00^2:> = 12K^2eps^2/(1+eps^2)", sp.simplify(T2v - 12*K**2*eps**2/nrm), 0)
chk("A4 (3.7) printed / exact = 1/(1+eps^2)", sp.simplify(p37/T2v - 1/nrm), 0)
Delta = sp.simplify(1 - rho_c**2/T2v)
chk("A5 exact Delta = 1-(2eps-sqrt2 c)^2/(3(1+eps^2))",
    sp.simplify(Delta - (1 - (2*eps - sp.sqrt(2)*c)**2/(3*nrm))), 0)
D38 = (10*eps + sp.sqrt(2)*c)/(12*eps)
w = {eps: sp.Rational(1, 10), c: 1}
chk("A6 witness eps=1/10,theta=0: exact Delta (4 dp)", round(float(Delta.subs(w)), 4), 0.5134)
chk("A7 witness eps=1/10,theta=0: printed (3.8) (4 dp)", round(float(D38.subs(w)), 4), 2.0118)

# z3: rho<0 => 1/3 < Delta < 1 (Delta as KF (3.2), with |.|; on rho<0 the |.| is inactive, checked)
e, cc = z3.Reals("e cc")
s2 = z3.Real("s2")
base = [e > 0, cc >= -1, cc <= 1, s2 > 0, s2*s2 == 2]
rho_neg = (2*e - s2*cc) < 0                      # sign of rho (K>0, eps>0)
Dz = 1 - (2*e - s2*cc)**2/(3*(1 + e*e))
def solve(extra):
    s = z3.Solver(); s.add(*base); s.add(*extra); return s.check()
chk("A8 vacuity: rho<0 reachable", solve([rho_neg]), z3.sat)
chk("A9 rho<0 and Delta>=1 (i.e. KF 'Delta>1') -- UNSAT", solve([rho_neg, Dz >= 1]), z3.unsat)
chk("A10 rho<0 and Delta<=1/3 -- UNSAT", solve([rho_neg, Dz <= z3.RealVal(1)/3]), z3.unsat)
chk("A11 rho<0 and Delta<0 (|.| active) -- UNSAT", solve([rho_neg, Dz < 0]), z3.unsat)

print("\nT. THE TREE AGAINST ITS OWN SCOPE (read-only import)")
sys.path.insert(0, WD)
spec = importlib.util.spec_from_file_location("fluctuation", os.path.join(WD, "fluctuation.py"))
fl = importlib.util.module_from_spec(spec); spec.loader.exec_module(fl)
chk("T1 fluctuation.JOURNAL_VERSION_READ", fl.JOURNAL_VERSION_READ, False)
chk("T2 docstring: journal version NAMED-NOT-READ",
    bool(re.search(r"Phys\. Rev\. D 47, 4510 \(1993\), is\s+NAMED-NOT-READ", fl.__doc__)), True)
chk("T3 docstring: 'MUST NOT be quoted as errors in the journal version until it is read'",
    "MUST NOT be quoted as errors in the journal version until it is read" in re.sub(r"\s+", " ", fl.__doc__), True)
chk("T4 fluctuation.SOURCE scoped to v1", fl.SOURCE.endswith("gr-qc/9304008 v1"), True)
hits = []
for root, _, files in os.walk(WD):
    for f in files:
        if f.endswith((".py", ".md", ".txt", ".tex")):
            p = os.path.join(root, f)
            try: s = open(p, encoding="utf-8", errors="replace").read()
            except Exception: continue
            if re.search(r"47,?\s*4510", s): hits.append(os.path.relpath(p, WD))
chk("T5 files naming PRD 47 4510 (expect only fluctuation.py, ledger.py)", sorted(hits), ["fluctuation.py", "ledger.py"])
# does any file assert that the JOURNAL carries an error?
bad = []
for p in hits:
    s = re.sub(r"\s+", " ", open(os.path.join(WD, p), encoding="utf-8").read())
    for m in re.finditer(r"[^.]{0,200}4510[^.]{0,200}", s):
        seg = m.group(0)
        if re.search(r"(journal|published)[^.]{0,80}(is|are) (wrong|in error|erroneous)", seg, re.I):
            bad.append((p, seg[:160]))
chk("T6 no file asserts the journal version is in error", bad, [])
print("\n%s" % ("ALL CHECKS OK" if not fails else "FAILED: %s" % fails))
sys.exit(1 if fails else 0)
