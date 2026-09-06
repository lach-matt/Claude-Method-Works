"""seedscore.py -- s61. Scores P3 of PREDICTION-SEED-INDEPENDENCE (sha 192d08537bf28e9e)
under F61.2's remedy: baseline is the harness's OWN seed-A row, comparison is made on the
A n X INTERSECTION of converged channels, and the dropped set is derived from
nlchain.candidates() -- deterministic, no SCF, no re-run, no edit to seedtest.py.

The sealed-row columns as filed are printed beside the corrected ones, not removed.

usage:  python3 ../pack61/seedscore.py            score
        python3 ../pack61/seedscore.py --selftest can-fail, in three directions
run from rt/.
"""
import sys, os, json, copy

sys.path.insert(0, os.getcwd())
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import nlchain as NC

SRC = "../pack61/seedO.jsonl"
DMARGIN_BOUND = 0.005          # P3: |dmargin| < 5 mHa
DEPTH_BOUND = 0.005            # same bound applied channelwise on the intersection


def load(path=SRC):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    by = {}
    for r in rows:
        by.setdefault(r["Z"], {})[r["mode"]] = r
    return by


def cand_tags(Z, chain):
    cfg = NC.cfg_from_chain(Z - 1, chain)
    return [NC.tagof(x) for x in NC.candidates([tuple(x) for x in cfg])]


def margin_on(order, keys):
    """runner-up minus winner, restricted to `keys`, using order's own depths."""
    d = {k: v for k, v in order if k in keys}
    s = sorted(d, key=lambda k: d[k])
    return (None if len(s) < 2 else round(d[s[1]] - d[s[0]], 6)), s


def compare(A, X, cands):
    kA = [k for k, _ in A["order"]]; kX = [k for k, _ in X["order"]]
    inter = set(kA) & set(kX)
    dA = dict(A["order"]); dX = dict(X["order"])
    dd = {k: round(dX[k] - dA[k], 6) for k in inter}
    mA, sA = margin_on(A["order"], inter)
    mX, sX = margin_on(X["order"], inter)
    return dict(
        n_inter=len(inter),
        ord_A=[k for k in kA if k in inter],
        ord_X=[k for k in kX if k in inter],
        ORDER_INT_MATCH=[k for k in kA if k in inter] == [k for k in kX if k in inter],
        max_dD=max((abs(v) for v in dd.values()), default=0.0),
        worst=max(dd, key=lambda k: abs(dd[k])) if dd else None,
        margin_int_A=mA, margin_int_X=mX,
        dmargin_int=(None if mA is None or mX is None else round(mX - mA, 6)),
        ENT_MATCH_A=(X["ent"] == A["ent"]),
        dropped_A=sorted(set(cands) - set(kA)),
        dropped_X=sorted(set(cands) - set(kX)),
    )


def score(by, chain, quiet=False):
    verdict = {"entrant": "PASS", "order": "PASS", "margin": "PASS"}
    lines = []
    for Z in sorted(by):
        cands = cand_tags(Z, chain)
        A = by[Z].get("seedA")
        if A is None:
            lines.append(f"Z={Z}: NO SEED-A ROW -- not scorable"); continue
        # derived dropped-set counts must reproduce each row's own nfail
        for m, r in sorted(by[Z].items()):
            drop = set(cands) - set(k for k, _ in r["order"])
            tick = "ok" if len(drop) == r["nfail"] else "MISMATCH"
            lines.append(f"Z={Z} {m}: order {len(r['order']):>2}/{len(cands)}  "
                         f"nfail {r['nfail']}  dropped {sorted(drop)}  [{tick}]")
        for m in ("seedB", "seedC"):
            X = by[Z].get(m)
            if X is None:
                lines.append(f"Z={Z} {m}: NO-DATA (row absent or seed did not converge)")
                continue
            c = compare(A, X, cands)
            if not c["ENT_MATCH_A"]: verdict["entrant"] = "FAIL"
            if not c["ORDER_INT_MATCH"]: verdict["order"] = "FAIL"
            if c["dmargin_int"] is not None and abs(c["dmargin_int"]) >= DMARGIN_BOUND:
                verdict["margin"] = "FAIL"
            if c["max_dD"] >= DEPTH_BOUND: verdict["margin"] = "FAIL"
            lines.append(
                f"Z={Z} A->{m}: ent {A['ent']}->{X['ent']} {'OK' if c['ENT_MATCH_A'] else 'CHANGED'}"
                f" | inter {c['n_inter']} ORDER_INT_MATCH={c['ORDER_INT_MATCH']} {c['ord_X']}"
                f" | max|dD| {c['max_dD']*1000:.3f} mHa @{c['worst']}"
                f" | margin_int {c['margin_int_A']} -> {c['margin_int_X']}"
                f"  dmargin_int {(c['dmargin_int'] or 0)*1000:+.3f} mHa"
                f" || AS FILED vs sealed: ORDER_MATCH={X['ORDER_MATCH']} dmargin={X['dmargin']}")
    if not quiet:
        print("\n".join(lines))
        print(f"P3  entrant {verdict['entrant']} · order-on-intersection {verdict['order']}"
              f" · margin/depth<5mHa {verdict['margin']}")
    return verdict


def selftest(chain):
    """CAN-FAIL in three directions. A scorer that cannot go red is not a scorer."""
    by = load()
    base = score(by, chain, quiet=True)
    assert base == {"entrant": "PASS", "order": "PASS", "margin": "PASS"}, base
    print(f"  phase 0  unperturbed          -> {base}   (must be all PASS)")

    b = copy.deepcopy(by); r = b[19]["seedB"]; r["ent"] = "3d"
    v = score(b, chain, quiet=True)
    print(f"  phase 1  entrant forced 3d    -> {v}   entrant must read FAIL")
    assert v["entrant"] == "FAIL"

    b = copy.deepcopy(by); r = b[19]["seedB"]
    d = dict(r["order"]); d["3d"] = -0.99          # 3d driven below 4s: order inverts
    r["order"] = sorted([[k, x] for k, x in d.items()], key=lambda t: t[1])
    v = score(b, chain, quiet=True)
    print(f"  phase 2  3d depth -> -0.99    -> {v}   order and margin must read FAIL")
    assert v["order"] == "FAIL" and v["margin"] == "FAIL"

    b = copy.deepcopy(by); r = b[19]["seedB"]
    r["order"] = [[k, (x - 0.010 if k == "3d" else x)] for k, x in r["order"]]
    v = score(b, chain, quiet=True)
    print(f"  phase 3  3d shifted -10 mHa   -> {v}   margin must read FAIL, order PASS")
    assert v["margin"] == "FAIL" and v["order"] == "PASS"

    v = score(load(), chain, quiet=True)
    print(f"  phase 4  reloaded from disk   -> {v}   must return to all PASS")
    assert v == base
    print("SELFTEST: the scorer goes red on entrant, on order, and on depth, and returns.")


if __name__ == "__main__":
    chain = NC.load()
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        selftest(chain)
    else:
        score(load(), chain)
