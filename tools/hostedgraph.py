#!/usr/bin/env python3
"""hostedgraph.py -- the record of what the HOSTED Graphify index measured, and when.

There are two graphs of this repository and they are not versions of one number
(`docs/GRAPH-HOSTED.md`). `graphify-out/graph.json` is a file: anyone can re-count
it, and `docfigures.py` does. The hosted index at https://api.graphify.com/mcp is
a service: it rebuilds unannounced -- three times in one session on 2026-09-06 --
and its figures can be read only through the MCP server, which no stdlib program
can call. So the hosted numbers printed in `docs/GRAPH-HOSTED.md` are the one
class of figure in this repository that NOTHING could catch drifting.

This closes that hole, in the only way an offline instrument can:

    HOSTED-GRAPH.tsv is the record. `--record` writes a row from a measurement
    handed to it. `docfigures.py` then pins what the DOCUMENT says against what
    the RECORD says.

WHAT IT DOES NOT DO, AND WHY
----------------------------
It does not call the service. It cannot: the MCP server is not reachable from a
stdlib script, and inventing an HTTP client here would make a checked figure
depend on an unchecked network. An agent with the MCP tools reads the numbers and
hands them over; this program only writes them down and does the arithmetic.

It therefore CANNOT tell you the record is current. A row is a measurement of one
build at one time, and it stays true about that build forever. `--age` reports how
old the record is so a reader can judge; it is not a failure.

THE PIN IS DOCUMENT-AGAINST-RECORD, NOT DOCUMENT-AGAINST-LIVE
-------------------------------------------------------------
Deliberately. Pinning the prose against the live service would go STALE every time
the service rebuilt -- several times a day -- and a check that cries wolf is a
check nobody reads. Re-recording is a deliberate act; forgetting to update the
prose afterwards is the real error, and that is what gets caught.

stdlib only.  python3 tools/hostedgraph.py [--record --json F] [--age] [--selftest]
"""
import argparse
import csv
import datetime as _dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "HOSTED-GRAPH.tsv"

COLUMNS = [
    "recorded_at", "build_id", "commit_sha", "pipeline", "model",
    "nodes", "edges", "communities",
    "labels_paren", "labels_e", "labels_e_code", "note",
]

# The figures a caller must supply. Anything absent makes the row a refusal
# rather than a partial record -- half a measurement is not a measurement.
REQUIRED = [c for c in COLUMNS if c not in ("recorded_at", "note")]

INT_FIELDS = ("nodes", "edges", "communities",
              "labels_paren", "labels_e", "labels_e_code")


def rows():
    """Every recorded measurement, oldest first. Missing file is not an error --
    it means nothing has been recorded yet, which is a true statement."""
    if not TSV.exists():
        return []
    with TSV.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def latest():
    """The most recent row, or None. The record is append-only: an older row is
    not wrong, it is a measurement of an older build."""
    r = rows()
    return r[-1] if r else None


def derived(row):
    """The two figures docs/GRAPH-HOSTED.md states that are not read directly off
    the service but computed from it.

    `noncode_max` is the BOUND, and it is the whole reason the document says
    'at most' rather than a number. Every label containing '()' sampled was
    file_type=code, so code nodes >= labels_paren, so non-code <= nodes - that.
    It is an upper bound on the hosted document layer and NOT a count of it:
    no MCP tool enumerates hosted nodes by kind."""
    n = int(row["nodes"])
    paren = int(row["labels_paren"])
    e = int(row["labels_e"])
    return {
        "noncode_max": n - paren,
        "e_pct": round(100.0 * e / n, 1),
    }


def bound_vs_local(row, local_semantic):
    """The hosted document layer as a percentage of the local semantic layer --
    an upper bound over an exact count, so the result is itself a bound."""
    return round(100.0 * derived(row)["noncode_max"] / local_semantic, 1)


def record(payload, note=""):
    row = {c: "" for c in COLUMNS}
    missing = [k for k in REQUIRED if not str(payload.get(k, "")).strip()]
    if missing:
        raise SystemExit("refusing to record a partial measurement; missing: %s"
                         % ", ".join(missing))
    for k in REQUIRED:
        row[k] = str(payload[k]).strip()
    for k in INT_FIELDS:
        int(row[k])                      # raises rather than storing a non-number
    row["note"] = note or str(payload.get("note", ""))
    # An explicit recorded_at is honoured so a measurement taken earlier can be
    # written down later without claiming to be newer than it is.
    row["recorded_at"] = str(payload.get("recorded_at", "")).strip() or \
        _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _dt.datetime.strptime(row["recorded_at"], "%Y-%m-%dT%H:%M:%SZ")   # or refuse
    existing = rows()
    if existing and existing[-1]["build_id"] == row["build_id"]:
        print("  build %s is already the latest row; replacing it in place."
              % row["build_id"][:8])
        existing = existing[:-1]
    with TSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        for r in existing + [row]:
            w.writerow(r)
    print("  recorded build %s at commit %s" % (row["build_id"][:8], row["commit_sha"][:7]))
    return 0


def age_seconds(row, now=None):
    """Signed, on purpose. A hand-supplied recorded_at can sit slightly ahead of
    the clock, and `timedelta.days` floors that to -1 -- which reads as a fault
    when it is only skew. The caller phrases it; this returns the truth."""
    now = now or _dt.datetime.now(_dt.timezone.utc)
    t = _dt.datetime.strptime(row["recorded_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=_dt.timezone.utc)
    return (now - t).total_seconds()


def age_phrase(row, now=None):
    s = age_seconds(row, now)
    if s < 0:
        return "stamped %d minute(s) ahead of this clock" % round(-s / 60)
    if s < 3600:
        return "%d minute(s) old" % (s // 60)
    if s < 86400:
        return "%d hour(s) old" % (s // 3600)
    return "%d day(s) old" % (s // 86400)


def report(show_age=False):
    r = latest()
    if not r:
        print("  no measurement recorded. HOSTED-GRAPH.tsv is absent or empty.")
        print("  that is not a fault: nothing has been measured yet.")
        return 0
    d = derived(r)
    print("  HOSTED GRAPHIFY INDEX -- last recorded measurement\n")
    print("      build            %s" % r["build_id"])
    print("      commit           %s" % r["commit_sha"])
    print("      pipeline/model   %s / %s" % (r["pipeline"], r["model"]))
    print("      recorded         %s" % r["recorded_at"])
    print()
    print("      nodes            %s" % r["nodes"])
    print("      edges            %s" % r["edges"])
    print("      communities      %s" % r["communities"])
    print("      labels with ()   %s   (all sampled were file_type=code)" % r["labels_paren"])
    print("      labels with e    %s   (%s%% of nodes)" % (r["labels_e"], d["e_pct"]))
    print()
    print("      DERIVED, and a BOUND not a count:")
    print("      non-code nodes   <= %s" % d["noncode_max"])
    print()
    print("      %d measurement(s) on record." % len(rows()))
    if show_age:
        print("      the record is %s. The service rebuilds unannounced," % age_phrase(r))
        print("      so age is information, not a failure.")
    return 0


def selftest():
    """Structural, like docfigures': the totals are what go stale, so the totals
    are not the fixtures. These assert the arithmetic and the refusals."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-58s = %-7s expected %-7s %s" % (label, got, want, "ok" if good else "FAIL"))

    fake = {"nodes": 1000, "edges": 900, "communities": 100, "labels_paren": 400,
            "labels_e": 500, "labels_e_code": 200, "build_id": "b", "commit_sha": "c",
            "pipeline": "p", "model": "m"}
    check("non-code bound is nodes minus paren labels", derived(fake)["noncode_max"], 600)
    check("e-percentage is one decimal place", derived(fake)["e_pct"], 50.0)
    check("bound against a local semantic count is a percentage",
          bound_vs_local(fake, 1200), 50.0)

    # a partial measurement is refused, not stored half-written
    partial = dict(fake); partial.pop("labels_e")
    try:
        record(partial)
        refused = False
    except SystemExit:
        refused = True
    check("a measurement missing a field is refused", refused, True)

    now = _dt.datetime(2026, 1, 2, tzinfo=_dt.timezone.utc)
    check("an age of one day reads as days",
          age_phrase({"recorded_at": "2026-01-01T00:00:00Z"}, now), "1 day(s) old")
    check("a record stamped ahead of the clock is not reported as negative",
          age_phrase({"recorded_at": "2026-01-02T00:30:00Z"}, now),
          "stamped 30 minute(s) ahead of this clock")

    r = rows()
    check("every recorded row carries every column",
          all(set(x) >= set(COLUMNS) for x in r) if r else True, True)
    check("the record is append-only and ordered oldest-first",
          [x["recorded_at"] for x in r] == sorted(x["recorded_at"] for x in r), True)
    check("no build_id is recorded twice",
          len({x["build_id"] for x in r}), len(r))
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--record", action="store_true",
                    help="write a measurement into HOSTED-GRAPH.tsv")
    ap.add_argument("--json", metavar="F",
                    help="the measurement, as JSON; '-' reads stdin")
    ap.add_argument("--note", default="", help="a note stored with the row")
    ap.add_argument("--age", action="store_true", help="also report the record's age")
    ap.add_argument("--selftest", action="store_true",
                    help="assert the arithmetic and the refusals")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.record:
        if not a.json:
            raise SystemExit("--record needs --json F (or --json - for stdin)")
        text = sys.stdin.read() if a.json == "-" else pathlib.Path(a.json).read_text()
        return record(json.loads(text), note=a.note)
    return report(show_age=a.age)


if __name__ == "__main__":
    sys.exit(main())
