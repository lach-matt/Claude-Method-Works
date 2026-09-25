"""nlcfg.py -- s45 item 1: THE CONFIGURATION COLUMN. BLOCKING per s44 §2(5).

`ok` in nlchain.jsonl compares STEPS (rectag == entrant). The walk produces a STATE.
This driver adds the STATE comparison beside it. Both stay; comparison decides.

    cfg_chain(Z) = seed 1s + entrants of steps 2..Z      (nlchain.cfg_from_chain, unmodified)
    cfg_ok(Z)    = cfg_chain(Z) == ground.expand(Z)      as a NORMALISED MULTISET (F42.2)

nlchain.py is IMPORTED AND NEVER PATCHED (M's ruling (b), s44). No SCF is run: the column is
a pure function of sealed nlchain.jsonl and ground.py.

usage: python3 nlcfg.py show      both columns, both scores, both first divergences
       python3 nlcfg.py gate      standing gate: fixed expectations, exit non-zero on failure
       python3 nlcfg.py --fail    can-fail demonstration (perturbs one chain step in memory)
"""
import sys, os
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import nlchain as NC
import ground as G

TAG = lambda n, l, k: f"{n}{'spdfg'[l]}{k}"


def norm(cfg):
    """normalised multiset: dict (n,l)->int occ, zero-occupancies dropped. Order-independent."""
    d = {}
    for n, l, k in cfg:
        d[(int(n), int(l))] = d.get((int(n), int(l)), 0) + int(round(k))
    return {k: v for k, v in d.items() if v > 0}


def as_str(cfg):
    return ''.join(TAG(n, l, k) for (n, l), k in sorted(norm(cfg).items()))


def column(rows, perturb=None):
    """returns {Z: dict(cfg_chain, rec_cfg, cfg_ok, ok, str_ok)}"""
    if perturb:
        rows = {z: dict(r) for z, r in rows.items()}
        rows[perturb]['ent_nl'] = [5, 0]          # in-memory only; jsonl untouched
    out = {}
    for Z in sorted(rows):
        if Z < 2: continue
        try:
            chain = NC.cfg_from_chain(Z, rows)
        except KeyError:
            continue
        try:
            rec = G.expand(Z)
        except (KeyError, IndexError):
            out[Z] = dict(cfg_chain=as_str(chain), rec_cfg=None, cfg_ok=None,
                          ok=rows[Z]['ok'], str_ok=None)
            continue
        cfg_ok = norm(chain) == norm(rec)
        # PCC-0a: the string comparison is computed too, and only compared to the multiset.
        str_ok = as_str(chain) == as_str(rec)
        out[Z] = dict(cfg_chain=as_str(chain), rec_cfg=as_str(rec), cfg_ok=cfg_ok,
                      ok=rows[Z]['ok'], str_ok=str_ok)
    return out


def scores(col):
    c = [v for v in col.values() if v['cfg_ok'] is not None]
    o = [v for v in col.values() if v['ok'] is not None]
    cf = sorted(Z for Z, v in col.items() if v['cfg_ok'] is False)
    of = sorted(Z for Z, v in col.items() if v['ok'] is False)
    return dict(cfg_score=(sum(1 for v in c if v['cfg_ok']), len(c)),
                ok_score=(sum(1 for v in o if v['ok']), len(o)),
                cfg_fail=cf, ok_fail=of,
                cfg_first=(cf[0] if cf else None), ok_first=(of[0] if of else None),
                disagree=sorted(Z for Z, v in col.items()
                                if v['cfg_ok'] is not None and v['ok'] is not None
                                and v['cfg_ok'] != v['ok']),
                str_mismatch=sorted(Z for Z, v in col.items()
                                    if v['str_ok'] is not None and v['str_ok'] != v['cfg_ok']))


def show(col, s):
    print(f"  {'Z':>4} {'ent':>4} {'rec':>4} {'ok':>6} {'cfgok':>6}  {'cfg_chain':<26} {'rec_cfg':<26}")
    rows = NC.load()
    for Z in sorted(col):
        v = col[Z]
        if v['cfg_ok'] is True and v['ok'] is True: continue     # print only the informative rows
        print(f"  {Z:>4} {rows[Z]['ent']:>4} {str(rows[Z]['rec_ent']):>4} {str(v['ok']):>6} "
              f"{str(v['cfg_ok']):>6}  {v['cfg_chain']:<26} {str(v['rec_cfg']):<26}")
    print(f"\n  CONFIG score {s['cfg_score'][0]}/{s['cfg_score'][1]}   "
          f"STEP (`ok`) score {s['ok_score'][0]}/{s['ok_score'][1]}")
    print(f"  FIRST CONFIG DIVERGENCE: {s['cfg_first']}   FIRST STEP DIVERGENCE: {s['ok_first']}")
    print(f"  config failures : {s['cfg_fail']}")
    print(f"  step   failures : {s['ok_fail']}")
    print(f"  columns disagree at {len(s['disagree'])}: {s['disagree']}")
    print(f"  nesting: cfg<=ok {set(s['cfg_fail'])<=set(s['ok_fail'])}  "
          f"ok<=cfg {set(s['ok_fail'])<=set(s['cfg_fail'])}")
    print(f"  string-vs-multiset mismatches: {s['str_mismatch']}")


# ---------------------------------------------------------------------------
# GATE 83 EXPECTATIONS.  Restated for 53 rows at s46 open (was 47 rows, s45).
#
# TWO KINDS OF CLAUSE, AND THE DISTINCTION IS BINDING (s45 general ruling):
#
#   GROWS WITH THE CHAIN -- cfg_score, ok_score.  Both denominators are the
#   chain length.  Every step the walk gains raises BOTH terms if the step
#   passes.  A change here is NOT divergence until it is checked against the
#   row count; it must be RESTATED whenever nlchain.jsonl is extended, and the
#   restatement belongs to the session that extends it.
#     s45 (47 rows): (39, 47) and (42, 47)
#     s46 (53 rows): (45, 53) and (48, 53)   <- the 5p row added six passes
#     s47 (55 rows): (47, 55) and (50, 55)   <- Cs(55) and Ba(56) pass BOTH columns
#     s48 (56 rows): (48, 56) and (51, 56)   <- La(57) sealed; passes BOTH columns
#     s48 (57 rows): (49, 57) and (52, 57)   <- Ce(58); passes BOTH columns, so the
#                    walk reproduced 4f1 5d1 6s2 with NO promotion operator
#     s48 (59 rows): (49, 59) and (54, 59)   <- Pr(59) and Nd(60).  BOTH pass the ok
#                    column and BOTH fail the cfg column: +2 to ok_score, +0 to
#                    cfg_score.  The first extension in this chain to split the
#                    two columns, and the mechanism is named below.
#     s48 (70 rows): (51, 70) and (63, 70)   <- the 4f block closed, Z=61..71.
#                    ok_score +9 (61,62,63,65,66,67,68,69,70 pass; 64 and 71 fail).
#                    cfg_score +2, AND THE TWO PASSES ARE AT 64 AND 71 -- the very
#                    elements where the ok column fails.  See the note below; this
#                    was predicted the other way by PB-6 and the prediction failed.
#   The restatement is arithmetic, not judgement: rows added, passes counted.
#   It is divergence ONLY if a row that passed stops passing.
#
#   CHAIN-LENGTH-INVARIANT -- cfg_first, ok_first, ok_fail, str_mismatch.
#   A CHANGE IN ANY OF THESE FOUR IS DIVERGENCE AND IS TO BE READ AS SUCH.
#
#   PREFIX-INVARIANT -- cfg_fail, disagree.  s48 RECLASSIFIES these two, because
#   the extension to Pr(59)/Nd(60) falsified their stated invariance and the
#   honest repair is to state what is actually invariant rather than to widen the
#   expectation quietly.  They were called invariant when every extension had
#   passed BOTH columns; that was a property of the rows added, not of the
#   clauses.  What is binding is now stated exactly:
#     (i)  no Z already listed may disappear, and
#     (ii) no Z may appear that is BELOW the previous extension point.
#   An append at the growing end is admissible ONLY with a named mechanism.
#   THE MECHANISM FOR {59, 60}: the walk has no promotion operator.  It placed
#   5d1 at La(57) and cannot vacate it, so its cfg carries 5d1 through Pr and Nd,
#   while the record gives 4f3 6s2 and 4f4 6s2 with NO 5d occupancy.  The cfg
#   column therefore fails at 59 and 60 for a reason the walk is already known to
#   lack, and the ok column passes at both because the ENTRANT is 4f either way.
#   This is the promotion operator becoming measurable rather than argued, and it
#   is owed as its own object -- it is NOT closed by being named here.
#
# The failure of this gate at s46 open was expected, was stated in advance in
# README-HANDOFF-45, and trips exactly the two growing clauses -- 6 of 8 pass.
# ---------------------------------------------------------------------------
#   THE Gd/Lu COINCIDENCE, RECORDED AT THE GATE BECAUSE THE GATE IS WHERE IT SHOWS.
#   cfg PASSES at 64 and 71, the two elements where ok FAILS.  The walk spent Z=57
#   on 5d and has run one 4f behind the record ever since, so its 4f count reaches
#   7 at Z=64 and 14 at Z=71 -- and the record's Gd is 4f7 5d1 6s2 and its Lu is
#   4f14 5d1 6s2.  The two agree on the STATE at exactly the two steps where they
#   disagree on which electron was added.  The disagreement at Gd and Lu is
#   therefore bookkeeping about the differentiating electron, not a disagreement
#   about the configuration -- which is the Cr(24) class, and is part 2's business.
#     s48 (74 rows): (55, 74) and (63->67, 74)  <- 5d block opened, Z=72..75.  All four
#                    steps pass BOTH columns: +4 to each.  4f has closed and left the
#                    open-channel competition; the walk's cfg tracks the record again.
#     s49 (79 rows): (58, 79) and (71, 79)  <- 5d block CLOSED, Z=76..80.  ok_score +4
#                    (76,77,78,79 pass; 80 fails).  cfg_score +3 (76,77,80 pass; 78 and 79
#                    fail).  BOTH integers were filed in advance by PD-6 and BOTH are exact.
#
# F49.1 -- ok_fail WAS DECLARED CHAIN-LENGTH-INVARIANT AND Hg(80) FALSIFIED THAT.
#   Registered before the score was read, and repaired the same way s48 repaired cfg_fail
#   and disagree rather than widening the expectation quietly.  ok_fail is RECLASSIFIED as
#   PREFIX-INVARIANT on the same two binding conditions: (i) no Z already listed may
#   disappear, (ii) no Z may appear below the previous extension point.  An append at the
#   growing end is admissible ONLY with a named mechanism.
#   THE MECHANISM FOR {80}: the walk has held 6s2 since Ba(56) and has no operator that can
#   vacate a closed s shell.  At Hg the record's 5d is already full at 5d10 and its
#   differentiating electron goes to 6s, while the walk -- whose 5d reaches 10 only at 80 --
#   must say 5d.  This is the SAME missing operator as at 78 and 79, running in the opposite
#   direction (there the record moves 6s->5d and the walk cannot; here the record has already
#   spent 5d and the walk has not).  It is the Cr(24) class throughout and it leaves the n+l
#   ORDERING untouched.
#   AND IT WAS PREDICTED: PD-2 filed ok(72..79)=True, ok(80)=False before Z=72 was run.  An
#   append foreseen by a filed clause is the strongest admissibility this taxonomy allows; a
#   surprise append at the growing end would still be divergence.
#
#   THE Gd/Lu/Hg STRUCTURE, THIRD OCCURRENCE.  cfg PASSES at 80, where ok FAILS -- as it does
#   at 64 and at 71.  PD-4 filed this as structural before the block was walked and it held.
#   Three times now the walk and the record agree on the STATE at exactly the step where they
#   disagree about which electron was added.  Three occurrences with one named cause is no
#   longer a coincidence at the gate: it is the signature of a missing promotion operator,
#   which is owed as its own object and is NOT closed by being named here.
#     s50 (107 rows): (73, 107) and (96, 107)   <- THE FULL WALK, Z=2..108. The
#                    derivation's terminal restatement; the chain does not grow
#                    again inside the evidentiary boundary (RULING-108).
#                    ok_score +4 over 101 rows: 103 and 104 FAIL, 105..108 pass.
#                    cfg_score +5: 103 FAILS, 104..108 ALL PASS -- the cfg column
#                    RECOVERS, which PG-6 predicted it would not.
#   MECHANISM FOR THE cfg RECOVERY AT 104, named as prefix-invariance requires:
#   the walk entered the actinides with TWO offsets -- one 5f behind, one 6d
#   ahead -- and they CANCEL at Rf(104).  The walk's 104th step puts its
#   fourteenth electron in 5f while it already carries 6d2 7s2, giving
#   5f14 6d2 7s2, which is exactly the record's Rf.  From 105 the two run in
#   lockstep in 6d.  The record's 7p1 at Lr(103) does not persist into 104, so
#   the walk's failure to open 7p costs it 103 only.  Two offsets that cannot
#   cancel one at a time cancelled simultaneously, and the walk rejoined the
#   record for the last five elements of the derivation.
#   MECHANISM FOR ok_fail {103, 104}: the walk must spend both steps reaching
#   5f14 -- it is one 5f behind -- while the record opens 7p at 103 and 6d at
#   104.  Same missing promotion operator, and NOT closed by being named.
GATE = dict(cfg_score=(73, 107), ok_score=(96, 107), cfg_first=24, ok_first=25,
            cfg_fail=[24, 29, 41, 42, 44, 45, 46, 47, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 78, 79, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103],
            ok_fail=[25, 30, 43, 47, 48, 64, 71, 80, 96, 103, 104],
            disagree=[24, 25, 29, 30, 41, 42, 43, 44, 45, 46, 48, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104],
            str_mismatch=[])


def gate(s):
    bad = 0
    for k, want in GATE.items():
        got = s[k]
        got = list(got) if isinstance(got, list) else got
        good = (got == want)
        print(f"  [{'PASS' if good else 'FAIL'}] {k:<12} got {got}  want {want}")
        bad += (not good)
    print(f"\nNLCFG GATE: {'PASS -- all clauses' if not bad else f'FAIL -- {bad} clause(s)'}")
    return 1 if bad else 0


if __name__ == '__main__':
    a = sys.argv[1:]
    rows = NC.load()
    p = 30 if '--fail' in a else None
    col = column(rows, perturb=p)
    s = scores(col)
    if a and a[0] == 'gate':
        sys.exit(gate(s))
    show(col, s)
    if p: print("\n  (--fail: step 30's entrant forced to 5s IN MEMORY; nlchain.jsonl untouched)")
