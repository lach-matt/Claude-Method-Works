"""Second-session pass on the gr-qc/9607003 audit: run AFTER mk_gr-qc_9607003.py.
Re-read gr-qc/9607003 (all 17 pp.), Kontou-Sanders 2003.01815 (pp.1,20-25,27,34) and
Fewster-Eveson gr-qc/9805024 (all 13 pp.) at alphaXiv; re-ran the script (now 28 checks)."""
import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
P = D + "/audits/gr-qc_9607003.json"
r = json.load(open(P))

r["source"]["via"] += ("; RE-READ in full in a second session (all 17 pages again), every quotation re-checked. "
  "Note: Eq.(1) is quoted on p.2 from Ref.[21] (Ford-Roman PRD 51, 4277 (1995)), where it was first derived; "
  "this paper re-derives it as Eq.(17), the m -> 0 limit of Eq.(16), by a plane-wave method.")

h = r["published_hypotheses"]
h[6] = ("H7 holds for ALL t0 > 0 in flat space; the extension to curved spacetime / boundaries for t0 << smallest local "
  "curvature radius and/or boundary distance is ARGUED in ref.[23] (PRD 53, 5496), not proved in this paper. The paper "
  "names TWO supporting cases: p.2-3 'we proved that the inequality Eq.(1) holds in the case of the Casimir effect for "
  "sampling times much smaller than the distance between the plates' (in [23]), and p.3/p.11 the static closed and open "
  "Robertson-Walker QIs of ref.[24] (gr-qc/9608005), which reduce to Eq.(1) for short sampling times")

d = r["hypothesis_drift"]
d[4] = ("DROPPED part of H7: noise.py:185-187 quotes Sec.4 as 'sampling time ... much smaller than the smallest local "
  "radius of curvature'; the source continues 'and/or the distance to any boundaries in the spacetime', and prefaces it "
  "'Recently we argued that such bounds should also hold'. The quotation is accurate as far as it goes, but it is "
  "labelled 'Ford-Roman's own condition', and the source's own status for it is an ARGUED extension (ref.[23]) with two "
  "worked cases (Casimir plates, proved in [23]; static RW, ref.[24]), not a theorem of this paper.")
d[5] += (" CAVEAT on the inference, recorded both ways: FE's own printed Eq.(5.6) (gr-qc/9805024 p.8, READ) gives exactly "
  "27/(2048 pi^2 tau^4) = 9/64 of Ford-Roman at the Lorentzian, and FE p.6 say they do not expect even their own bound to "
  "be attained. But FE's stated class is smooth, even, non-negative samplers that 'decay rapidly at infinity', the "
  "Lorentzian decays only as t^-2 (script L3), and FE call their derivation 'somewhat formal and lacking in mathematical "
  "rigour' (p.9). So '4D Ford-Roman is not saturated' is supported by FE's own application of their bound, not proved "
  "here. In 2D it is firm: Flanagan's bound is OPTIMAL, and at the Lorentzian it is 1/6 of Ford-Roman's 2D bound "
  "(script L1, matching FE p.8 'six times stronger'), so Ford-Roman's 2D Lorentzian constant is provably not attained.")
d.append("ATTRIBUTION, not a fault: achievable.py:327-332 and the canonical names cite the massless bound as "
  "'gr-qc/9607003 Eq.(1)'. That location is correct, but on p.2 Eq.(1) is quoted from Ref.[21] (Ford-Roman PRD 51, 4277 "
  "(1995)), which first derived it; gr-qc/9607003 re-proves it as Eq.(17). The merged key "
  "'ford-roman-1995-qi-massless-scalar' points at the 1995 paper, which this audit did not open (NAMED-NOT-READ); the "
  "coefficient 3/(32 pi^2) is the same in both.")

rd = r["rederivation"]
rd["outcome"] = rd["outcome"].replace("ALL PASS (25 checks", "ALL PASS (28 checks").replace(
  "K: crossover 0.307933 l_P", "L (added in the second session): Flanagan's optimal 2D bound at the Lorentzian is "
  "exactly 1/6 of Ford-Roman's 2D Eq.(25) and FE's 2D bound 1/4 of it (INT f'^2/f = 1/(2 t0^2)), both as FE p.8 prints; "
  "the Lorentzian tail is t^-2, outside FE's rapid-decay class. K: crossover 0.307933 l_P")

L = r["later_literature"]
for e in L:
    if e["ref"].startswith("Kontou & Sanders"):
        e["what"] = e["what"].replace(
          "DISCREPANCY RECORDED, NOT A REFUTATION: (61) evaluated with f^2 = Lorentzian gives 27/(2048 pi^2) (script J1), not 3/(32 pi^2). The review's sentence reads loosely here (which function is Lorentzian, f or f^2, is ambiguous) and it is not an error in gr-qc/9607003.",
          "DISCREPANCY RECORDED, NOT A REFUTATION (re-read p.21-22): p.21 writes (61) with the weight f^2 and says it 'was first derived by Ford and Roman [73,74] for Lorentzian functions f(t) = t0/(pi(t^2+t0^2))'; p.22 then says 'for a Lorentzian function, C = 3/(32 pi^2)'. Read literally with f^2 = Lorentzian (Ford-Roman's actual weight), (61) gives 27/(2048 pi^2) = 9/64 of that C (script J1; FE's own Eq.(5.6)). So the review's C is Ford-Roman's own constant, not the value of (61), and the phrasing is loose about f versus f^2. Not an error in gr-qc/9607003. p.34 also records that Casimir negative energy is constant in time and violates AWEC: consistent with H3 (Eq.(1) is for no boundaries).")
        e["read_status"] = "READ (pp.1,20-25,27,34 via answer_pdf_queries; re-read in the second session)"
    if e["ref"].startswith("Fewster & Eveson"):
        e["what"] = ("Generalises Ford-Roman to smooth, even, non-negative samplers that are compactly supported or "
          "rapidly decaying, any dimension d >= 2, mass m >= 0 (abstract). 4D massless Eq.(5.5): rho >= -(1/16 pi^2) "
          "INT ((f^{1/2})'')^2 dt; at the Lorentzian Eq.(5.6) gives -27/(2048 pi^2 tau^4), 'which is 9/64 of Ford and "
          "Roman's result' (reproduced exactly here, script J1). In 4D the massless bound also bounds massive fields "
          "(Q_3 <= 1). In 2D their bound is 4x stronger than Ford-Roman at the Lorentzian and Flanagan's optimal one 6x "
          "(script L1, L2). This SHARPENS the bound (against M) and supports 'not saturated'. Stated limits (named, "
          "not hidden): a formal derivation 'lacking in mathematical rigour' (p.9); rapid decay required, which the "
          "Lorentzian (t^-2 tail) does not meet though FE apply (5.6) to it; state class 'sufficiently well-behaved', "
          "Hadamard hoped for. A sharp box (characteristic function) sampler gives NO bound (p.9, Garfinkle): "
          "consistent with the tree's no-ball-QI reading only for SHARP spacetime boxes, not a statement about "
          "smooth spatial averages.")
        e["read_status"] = "READ (all 13 pages via answer_pdf_queries, second session)"
L.append({"ref": "Fewster & Pfenning, J. Math. Phys. 47, 082303 (2006); Ford & Roman, PRD 87, 085001 (2013)",
  "effect": "narrows",
  "what": "Restated in Kontou-Sanders p.22 (eq.(64)): along a uniformly accelerated worldline the QWEI acquires "
    "acceleration terms and 'observers on non-inertial trajectories can experience negative energies for long times'; "
    "for sinusoidal motion 'the averaged energy density [can] become arbitrarily negative at a linear rate' (with the "
    "energy cost of the acceleration exceeding it). Ford-Roman's INERTIAL-observer hypothesis (H4) is therefore "
    "load-bearing. The tree's owners use the inertial case (achievable.py:196-198), so no drift; it is a scope limit.",
  "read_status": "READ-VIA-RESTATEMENT (2003.01815 p.22); the papers were not opened"})
L.append({"ref": "Helfer, CQG 13, L129 (1996) (cited as FE ref.[7]); Pfenning & Ford gr-qc/9805037; Fewster & Teo gr-qc/9812032",
  "effect": "extends",
  "what": "FE footnote 1 (p.2, READ): 'space averaged energy densities in 4-dimensions are not bounded below [7]' -- a "
    "published basis (one of them) for certify.py:154-159's 'no standard QI bounds' a spatial ball integral (the tree's own ledger "
    "D6 cites Ford-Helfer-Roman PRD 66 124012). Pfenning-Ford and Fewster-Teo (surfaced by discover_papers) extend the "
    "QI to curved and static spacetimes; not opened here.",
  "read_status": "Helfer NAMED-NOT-READ (restated in FE p.2 footnote); the other two NAMED-NOT-READ"})

r["grade_evidence"] = r["grade_evidence"].replace(
  "is in this paper an ARGUED claim with one worked example (static RW)",
  "is in this paper an ARGUED claim (ref.[23]) with two worked cases (Casimir plates, static RW)").replace(
  "The same computation shows Ford-Roman's Lorentzian constant is never attained, which independently confirms",
  "FE's own Eq.(5.6) (READ) prints that 9/64; it supports, but because the Lorentzian sits outside FE's stated "
  "rapid-decay class and FE's derivation is self-described as formal it does not prove, that Ford-Roman's 4D Lorentzian "
  "constant is never attained (in 2D Flanagan's optimal bound makes it firm, script L1). That supports")
r["grade_evidence"] += (" Second session: source, Kontou-Sanders and Fewster-Eveson re-read at alphaXiv; the script "
  "re-run (28 checks, all pass); every owner file:line quoted above was re-checked against the tree read-only.")
r["what_would_change_the_grade"] += (" Separately, the support for 'Ford-Roman 4D is not saturated' (and so for the "
  "tree's K = 0 WRONG record) would fall if FE's Eq.(5.6) were shown invalid for the Lorentzian sampler, which lies "
  "outside FE's stated rapid-decay class; it would not change this grade, which rests on the tree's usage.")
json.dump(r, open(P, "w"), indent=1, ensure_ascii=False)
print("ok", len(json.dumps(r)))
r = json.load(open(P))
d = r["hypothesis_drift"]
d[5] = d[5].replace("A proved bound 64/9 times tighter on the SAME functional means no state reaches Ford-Roman's Lorentzian constant: it is not attained.",
  "A bound 64/9 times tighter on the SAME functional, if valid for the Lorentzian, means no state reaches Ford-Roman's Lorentzian constant (see the caveat below).")
r["lacked_data"] = r["lacked_data"].replace("(a) The optimal sampler analysis (Fewster-Eveson 1998)",
  "(a) The general-sampler analysis (Fewster-Eveson 1998, READ; not itself optimal, per FE p.8-10)")
json.dump(r, open(P, "w"), indent=1, ensure_ascii=False)
print("ok2")
