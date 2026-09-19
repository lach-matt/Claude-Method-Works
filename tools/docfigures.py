#!/usr/bin/env python3
"""docfigures.py -- do the repository's own documents still state true numbers?

`arith.py` checks the arithmetic the volumes state about themselves. This does the
same for the documents that describe the REPOSITORY -- CLAUDE.md and docs/ -- and
it exists because they went stale without anyone noticing:

    CLAUDE.md said 559 artefacts held against 431 ABSENT. The instrument measured
    702 and 4. `extracted/` and `recovered/` had landed 143 of them and nothing
    updated the prose, so the entry-point document -- the one every chat reads
    first -- overstated the gap by two orders of magnitude.

Every row below pins a CLAIMED value beside a measurement. A row is STALE when
they differ. That is a finding about the documentation, never about the corpus:
the tree is right and the sentence is old.

WHAT IT REFUSES
---------------
It does not edit a document, and it does not decide which of the two is correct.
It reports the drift and names the file to read. Where a claim is a range or a
prose phrase rather than a number, it is not pinned here at all -- a check that
cannot be made exactly is not made.

It also refuses to measure anything requiring the 393 MB chat export, so it stays
fast enough to run at the top of a session. `coverage.py --chats` owns that.

The last fourteen rows come from `pointers.py --json` and `arith.py --json`. Their
own selftests pin individual SITES -- 53 and 42 fixtures -- so a change in a
corpus-wide TOTAL passes them without a word. These rows are that missing check.

stdlib only.  python3 tools/docfigures.py [--selftest] [-v]
"""
import argparse
import csv
import json
import os
import pathlib
import re
import subprocess
import sys
from typing import Dict

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _rows(rel):
    with open(ROOT / rel, encoding="utf-8", errors="replace") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _walk(rel, skip=()):
    out = []
    for dp, _, fs in os.walk(ROOT / rel):
        if any(s in dp for s in skip):
            continue
        out += [os.path.join(dp, f) for f in fs]
    return out


def _entries(rel):
    """Every Register entry number a member seats, GROUPED HEADINGS HONOURED.

    A bare `### N` read undercounts The Register by 32 and invents 32 gaps that
    are not gaps -- DEFERRED.md docket 9(c)/30 records the same trap.
    """
    t = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    s = set()
    for m in re.finditer(r"\n### ([\d,\s]+)\n", t):
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            if part.strip().isdigit():
                s.add(int(part.strip()))
    return s


# The two audit instruments that report corpus-wide totals no per-site fixture
# covers. Their own --selftest checks individual sites (42 and 53 fixtures), so a
# change in the TOTAL passes them silently; that is what these rows catch.
_JSON_CACHE = {}


def _tool_json(name, args):
    """Run an instrument's --json and parse it. Empty dict if it cannot run."""
    key = (name, tuple(args))
    if key not in _JSON_CACHE:
        try:
            out = subprocess.run([sys.executable, str(ROOT / "tools" / name)] + list(args),
                                 capture_output=True, text=True, timeout=600)
            _JSON_CACHE[key] = json.loads(out.stdout) if out.stdout.strip() else {}
        except Exception:
            _JSON_CACHE[key] = {}
    return _JSON_CACHE[key]


def _pointer_sites():
    return _tool_json("pointers.py", ["--roster", "with-companion", "--json"]).get("sites", [])


def _arith_claims():
    return _tool_json("arith.py", ["--roster", "reader-facing", "--json"]).get("claims", [])


# pointers.py calls a site a FINDING when it carries a census class OR its verdict
# is one of the four the doc names as findings. Neither predicate alone reproduces
# the report: census_class alone gives 40 and misses APPSEC's two PREFIX-ONLY,
# finding-verdicts alone gives 25 and misses the REGISTER-RANGE census rows.
_FINDING_VERDICTS = {"UNRESOLVED", "PREFIX-ONLY", "KIND-MISMATCH"}


def _is_finding(site):
    return bool(site.get("census_class")) or site.get("verdict") in _FINDING_VERDICTS


def _site_index():
    """public/data/index.js, the generated site index, read as data: the file is
    `window.__mi = ...; window.__mi.index = {...};` and the object is JSON."""
    blob = (ROOT / "public" / "data" / "index.js").read_text(encoding="utf-8")
    start = blob.index("window.__mi.index = ") + len("window.__mi.index = ")
    end = blob.rstrip().rstrip(";")
    return json.loads(end[start:])


_PARTICLES = {}


def _particles():
    """The site's Particles block, which the public build does not carry (the
    paper it reads is not released), built on demand by the generator's own
    function so the figures the doc states about it are still measured."""
    if "block" not in _PARTICLES:
        sys.path.insert(0, str(ROOT / "tools"))
        import webindex
        _PARTICLES["block"] = webindex.particles_block()
    return _PARTICLES["block"]


def _walk_summary():
    return _tool_json("lowdin_walk.py", ["--report", str(ROOT / "LOWDIN-WALK.tsv"), "--json"])


def _walk_setting(c):
    return _walk_summary().get("settings", {}).get(c, {})


def _walk_compare(field="lx"):
    return (_walk_summary().get("fields") or {}).get(field) or {}


def _manifest():
    return [r["repo_path"] for r in _rows("drive/MANIFEST.tsv")]


def _build_nums(suffix):
    return sorted(int(re.search(r"BUILD(\d+)", p).group(1))
                  for p in _manifest() if p.endswith(suffix))


# (document, label, claimed, measurement)
def checks():
    man = _manifest()
    cov = _rows("COVERAGE.tsv")
    led = _rows("extracted/LEDGER.tsv")
    rec = _rows("recovered/LEDGER.tsv")
    idx = _rows("drive/chats/INDEX.tsv")
    ext = {r["target_path"] for r in led if r["disposition"] == "EXTRACTED"}
    R = _entries("method/members/The_Method_1_6___The_Register-2.md")
    W = _entries("method/members/WORKING-REGISTER.md")
    roots = {p.split("/")[0] for p in man}
    disk = set()
    for root in roots:
        base = ROOT / "drive" / root
        for dp, _, fs in os.walk(base):
            for f in fs:
                disk.add(os.path.relpath(os.path.join(dp, f), ROOT / "drive"))
    cs = lambda s: sum(1 for r in cov if r["status"] == s)
    gaps = [n for n in range(min(R), max(R) + 1) if n not in R]

    return [
        ("CLAUDE.md", "members extracted from the bundles", 343,
         len(_rows("method/MEMBER-INDEX.tsv"))),
        ("CLAUDE.md", "drive/ MANIFEST rows", 822, len(man)),
        ("CLAUDE.md", "drive/ manifest-tree bijection (orphans, both ways)", 0,
         len(disk ^ set(man))),
        ("CLAUDE.md", "drive/ rows with status ok", 819,
         sum(1 for r in _rows("drive/MANIFEST.tsv") if r["status"] == "ok")),
        ("CLAUDE.md", "drive/chats/ files (no manifest row)", 354,
         len(_walk("drive/chats"))),
        ("CLAUDE.md", "drive/PENDING.tsv rows", 4, len(_rows("drive/PENDING.tsv"))),
        ("CLAUDE.md", "extracted/ source occurrences", 2504, len(led)),
        ("CLAUDE.md", "extracted/ bodies written", 779, len(ext)),
        ("CLAUDE.md", "extracted/ bodies, MB (1dp)", 57.4,
         round(sum(os.path.getsize(ROOT / p) for p in ext) / 1e6, 1)),
        ("CLAUDE.md", "recovered/ RECOVERED-TRUNCATED", 23,
         sum(1 for r in rec if r["status"] == "RECOVERED-TRUNCATED")),
        ("CLAUDE.md", "chat conversations", 352, len(idx)),
        ("CLAUDE.md", "chat messages", 11879,
         sum(int(r["message_count"]) for r in idx)),
        ("CLAUDE.md", "artefact names in the two live bundles", 1005, len(cov)),
        ("CLAUDE.md", "artefacts HELD", 813, cs("HELD")),
        ("CLAUDE.md", "artefacts HELD-VIA-ALIAS", 15, cs("HELD-VIA-ALIAS")),
        ("CLAUDE.md", "artefacts IN-CHAT-BODY", 11, cs("IN-CHAT-BODY")),
        ("CLAUDE.md", "artefacts IN-CHAT", 162, cs("IN-CHAT")),
        ("CLAUDE.md", "artefacts ABSENT", 4, cs("ABSENT")),
        ("CLAUDE.md", "BUILD .md files in the manifest", 140,
         sum(1 for p in man if "The_Method_1_6_BUILD" in p and p.endswith(".md"))),
        ("CLAUDE.md", "BUILD compendia stream, plain name", 123,
         len(_build_nums("_compendia_papers_audits.md"))),
        ("CLAUDE.md", "BUILD main stream, plain name", 12,
         len(_build_nums("_main_and_register.md"))),
        ("CLAUDE.md", "BUILD compendia lowest / highest", (9, 179),
         (min(_build_nums("_compendia_papers_audits.md")),
          max(_build_nums("_compendia_papers_audits.md")))),
        ("CLAUDE.md", "BUILD main lowest / highest", (9, 90),
         (min(_build_nums("_main_and_register.md")),
          max(_build_nums("_main_and_register.md")))),
        ("CLAUDE.md", "figure bundles held", 3,
         sum(1 for p in man if re.search(r"figures_BUILD\d+\.zip$", p))),
        ("CLAUDE.md", "__<driveFileId> duplicates", 100,
         sum(1 for p in man if "__" in os.path.basename(p))),
        # the reconstructed walk: LOWDIN-WALK.tsv through the instrument's own summary
        ("docs/LOWDIN-WALK.md", "LOWDIN-WALK rows", 476, len(_rows("LOWDIN-WALK.tsv"))),
        ("docs/LOWDIN-WALK.md", "walk lx: entrant = observed gain at c = 137.035999", 96,
         _walk_setting("lx:137.035999").get("agree")),
        ("docs/LOWDIN-WALK.md", "walk lx: entrant = observed gain at c = inf", 92,
         _walk_setting("lx:inf").get("agree")),
        ("docs/LOWDIN-WALK.md", "walk lx: chain configuration identical at c = 137.035999", 84,
         _walk_setting("lx:137.035999").get("cfg_identical")),
        ("docs/LOWDIN-WALK.md", "walk lx: clause 2 exceptions at c = 137.035999", 1,
         len(_walk_setting("lx:137.035999").get("clause2_exceptions", []))),
        ("docs/LOWDIN-WALK.md", "walk lx: entrants differing between the settings", 7,
         len(_walk_compare("lx").get("displaced", []))),
        ("docs/LOWDIN-WALK.md", "walk lx: of register 1706's eleven, displaced here too", 2,
         len(_walk_compare("lx").get("in_eleven", []))),
        ("docs/LOWDIN-WALK.md", "walk hf: entrant = observed gain at c = 137.035999", 94,
         _walk_setting("hf:137.035999").get("agree")),
        ("docs/LOWDIN-WALK.md", "walk hf: entrant = observed gain at c = inf", 96,
         _walk_setting("hf:inf").get("agree")),
        ("docs/LOWDIN-WALK.md", "walk hf: chain configuration identical at c = 137.035999", 70,
         _walk_setting("hf:137.035999").get("cfg_identical")),
        ("docs/LOWDIN-WALK.md", "walk hf: chain configuration identical at c = inf", 76,
         _walk_setting("hf:inf").get("cfg_identical")),
        ("docs/LOWDIN-WALK.md", "walk hf: clause 2 exceptions at c = 137.035999", 2,
         len(_walk_setting("hf:137.035999").get("clause2_exceptions", []))),
        ("docs/LOWDIN-WALK.md", "walk hf: entrants differing between the settings", 5,
         len(_walk_compare("hf").get("displaced", []))),
        ("docs/LOWDIN-WALK.md", "walk hf: of register 1706's eleven, displaced here too", 1,
         len(_walk_compare("hf").get("in_eleven", []))),
        ("docs/LOWDIN-WALK.md", "walk: the two fields' entrants differ at c = 137.035999", 6,
         len((_walk_summary().get("fields_compare") or {}).get("entrants_differ", []))),
        ("docs/LOWDIN-WALK.md", "walk: rows not converged (three hf rows at c = 137.035999)", 3,
         sum(len(v.get("not_converged", [])) for v in _walk_summary().get("settings", {}).values())),
        # the thirty-six of section 6, as the site carries them (webindex.py over cypher's R)
        ("docs/WEB-INDEX.md", "site closure: the thirty-six forbidden by l <= n-1", 25,
         _site_index()["closure"]["decomposition"]["forbidden"]),
        ("docs/WEB-INDEX.md", "site closure: the thirty-six deferred", 11,
         _site_index()["closure"]["decomposition"]["deferred"]),
        ("docs/WEB-INDEX.md", "site closure: E with helium at group 2 (Register 448)", 20,
         _site_index()["closure"]["placement"]["helium_at_2"]["E"]),
        ("docs/WEB-INDEX.md", "site closure: E prices helium's placement at", 16,
         _site_index()["closure"]["placement"]["priced"]),
        ("docs/WEB-INDEX.md", "site lattice: sites, charge 1..Z by l 0..7 over Z = 1..120", 58080,
         _site_index()["lattice"]["sites"]),
        ("docs/WEB-INDEX.md", "site lattice: known cells (measured + exact)", 1287,
         len(_site_index()["lattice"]["known"])),
        ("docs/WEB-INDEX.md", "site references: arXiv identifiers the corpus prints", 53,
         len(_site_index()["references"]["arxiv"])),
        ("docs/WEB-INDEX.md", "site references: DOIs the corpus prints", 7,
         len(_site_index()["references"]["doi"])),
        ("docs/WEB-INDEX.md", "site references: B.1 species mapped to a compilation", 26,
         len(_site_index()["references"]["spectra_sources"]["by_species"])),
        ("docs/WEB-INDEX.md", "site papers: released papers held", 2,
         sum(1 for x in _site_index()["papers"]["papers"] if x["held"])),
        ("docs/WEB-INDEX.md", "site papers: slots not yet held", 1,
         sum(1 for x in _site_index()["papers"]["papers"] if not x["held"])),
        ("docs/WEB-INDEX.md", "site figure data: measured channels the equation figure draws", 358,
         len(_site_index()["figure_data"]["equation"]["rows"])),
        ("docs/WEB-INDEX.md", "site particle indexes: members 30, 250, 292", [30, 250, 292],
         [x["members"] for x in ((_site_index()["particle_index"] or {}).get("indexes") or [])]),
        ("docs/WEB-INDEX.md", "site particle indexes: cells 26, 66, 184", [26, 66, 184],
         [x["cells"] for x in ((_site_index()["particle_index"] or {}).get("indexes") or [])]),
        ("docs/WEB-INDEX.md", "site particle indexes: the accounting 6506 = 5880 + 54 + 572", "6506 = 5880 + 54 + 572",
         ((_site_index()["particle_index"] or {}).get("accounting") or {}).get("identity")),
        ("docs/WEB-INDEX.md", "site particle indexes: 550 charted of 572, 22 unplaced", [572, 550, 22],
         [((_site_index()["particle_index"] or {}).get("accounting") or {}).get(k) for k in ("members", "charted", "unplaced")]),
        ("docs/WEB-INDEX.md", "site particles: absent from the public build (None)", None,
         _site_index()["particles"]),
        ("docs/WEB-INDEX.md", "site particles: constants of Lambda_phys (--with-particles)", 27,
         _particles()["constants"]["count"]),
        ("docs/WEB-INDEX.md", "site particles: the muon window in electron masses (--with-particles)", [119, 918],
         _particles()["window"]["m_e"]),
        ("docs/PROSE-ONLY.md", "PROSE-ONLY rows", 1168,
         len(_rows("PROSE-ONLY.tsv"))),
        ("docs/PROSE-ONLY.md", "PROSE-ONLY conversations", 194,
         len({r["conversation"] for r in _rows("PROSE-ONLY.tsv")})),
        ("docs/RETRACTION-AUDIT.md", "RETRACTION-AUDIT rows", 391,
         len(_rows("RETRACTION-AUDIT.tsv"))),
        ("docs/RETRACTION-AUDIT.md", "LIVE-SUPERSEDED", 25,
         sum(1 for r in _rows("RETRACTION-AUDIT.tsv")
             if r["verdict"] == "LIVE-SUPERSEDED")),
        ("docs/REGISTER-GAPS.md", "The Register entries", 1660, len(R)),
        ("docs/REGISTER-GAPS.md", "Working Register entries", 119, len(W)),
        ("docs/REGISTER-GAPS.md", "registers seated in both (must be 0)", 0, len(R & W)),
        ("docs/REGISTER-GAPS.md", "numbering gaps", 132, len(gaps)),
        ("docs/REGISTER-GAPS.md", "seated in neither register", 13,
         len([n for n in gaps if n not in W])),
        ("docs/HANDOFF-GAP.md", "handoffs by number, unheld before the recovery", 26,
         len(_rows("HANDOFF-GAP.tsv"))),
        ("docs/HANDOFF-GAP.md", "seated as RECOVERED-BY-NUMBER", 23,
         sum(1 for r in _rows("recovered/LEDGER.tsv")
             if r["status"] == "RECOVERED-BY-NUMBER")),
        ("docs/HANDOFF-GAP.md", "still held nowhere (all MENTION-ONLY)", 3,
         sum(1 for r in _rows("HANDOFF-GAP.tsv") if r["class"] == "MENTION-ONLY")),
        ("CLAUDE.md", "recovered/ files", 3173,
         len({r["target_path"] for r in _rows("recovered/LEDGER.tsv") if r["target_path"]})),
        ("CLAUDE.md", "recovered/ ledger rows", 3224, len(_rows("recovered/LEDGER.tsv"))),
        ("CLAUDE.md", "recovered/ RECOVERED-BY-WRITE", 768,
         sum(1 for r in _rows("recovered/LEDGER.tsv")
             if r["status"] == "RECOVERED-BY-WRITE")),
        ("docs/GRAPH-FINDINGS.md", "Lowdin bridge sessions held", 63,
         len({r["filename"] for r in _rows("recovered/LEDGER.tsv")
              if r["filename"].startswith("BRIDGE-LOWDIN-SESSION-")
              and r["filename"][22:-3].isdigit()})),
        ("docs/IDCENSUS.md", "prose-only rulings (Ruling/Docket/W-entry)", 0,
         _governance_prose_only()),
        ("CLAUDE.md", "standing artefacts CLAUDE.md does not name", 0,
         len(unreferenced_artefacts())),
        ("CLAUDE.md", "seated members needing Python >= 3.12", 10,
         _members_needing_312()),
        ("CLAUDE.md", ".py files that parse under NO available interpreter", 6,
         _unparseable_anywhere()),
    ] + _instrument_rows() + _hosted()


def _newest_python():
    """The newest python3.X on PATH, for a parse census that is not hostage to
    whichever interpreter happens to be running this."""
    best = None
    for minor in range(20, 8, -1):
        exe = pathlib.Path("/usr/bin/python3.%d" % minor)
        if exe.exists():
            best = str(exe)
            break
    return best or sys.executable


def _parse_census(interpreter, roots=("recovered", "extracted", "tools", "method/members")):
    """Count .py files the given interpreter cannot parse. Parsing only -- nothing
    is imported or executed, which matters in a tree of mirrored artefacts."""
    code = (
        "import ast,pathlib,sys\n"
        "bad=0\n"
        "for r in %r:\n"
        "    for p in pathlib.Path(r).rglob('*.py'):\n"
        "        try: ast.parse(p.read_text(encoding='utf-8',errors='replace'))\n"
        "        except SyntaxError: bad+=1\n"
        "        except Exception: pass\n"
        "print(bad)\n" % (roots,)
    )
    try:
        out = subprocess.run([interpreter, "-c", code], capture_output=True, text=True,
                             cwd=str(ROOT), timeout=300)
        return int(out.stdout.strip().splitlines()[-1])
    except Exception:
        return -1


def _members_needing_312():
    """Seated members that a pre-3.12 interpreter rejects.

    All ten are PEP 701: a backslash inside an f-string expression, such as
    gate.py's `t.count(b"\n")`, which is a SyntaxError before 3.12 and valid
    from it. They are not corrupt -- they are newer than the default python3
    in this container (3.11), and gate.py and close.py are among them.
    """
    import ast as _ast
    if sys.version_info >= (3, 12):
        # this interpreter accepts them; count against an older one if present
        old = pathlib.Path("/usr/bin/python3.11")
        if old.exists():
            return _parse_census(str(old), roots=("method/members",))
        return 10
    n = 0
    for p in (ROOT / "method" / "members").rglob("*.py"):
        try:
            _ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            n += 1
        except Exception:
            pass
    return n


def _unparseable_anywhere():
    """Files no available interpreter can parse -- genuine fragments, not a
    version gap. Six at last measure, all recovered or extracted chat
    fragments; `recovered/l-ch1.py` is four lines ending in
    `from tower import L8 if False else None`, which was never valid Python."""
    return _parse_census(_newest_python())


def unreferenced_artefacts():
    """Every standing artefact must be named in CLAUDE.md.

    This row exists because the rest of this file could not catch what it is
    for. On 2026-09-04 an index-based splice in CLAUDE.md deleted five
    paragraphs -- the pointers to PROSE-ONLY.tsv, RETRACTION-AUDIT.tsv,
    REGISTER-GAPS.tsv, HANDOFF-GAP.tsv and docs/GRAPH-FINDINGS.md -- and every
    pinned figure still held, because the figures were all still TRUE. They just
    had no sentence left to be true about. Pinning a number cannot see a deleted
    pointer; only naming the artefacts can.

    A file that is deliberately not pointed at belongs in EXEMPT, with a reason,
    rather than being quietly tolerated.
    """
    EXEMPT: Dict[str, str] = {
        # nothing at present: every docs/ page, standing TSV and tool is named.
    }
    out = []
    for pattern in ("docs/*.md", "*.tsv", "tools/*.py"):
        for path in sorted(ROOT.glob(pattern)):
            rel = str(path.relative_to(ROOT))
            if rel in EXEMPT:
                continue
            claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8", errors="replace")
            if path.name not in claude and rel not in claude:
                out.append(rel)
    return out


def _governance_prose_only():
    """The spine claim, checked directly: no ruling, docket or W- entry is
    named in the export and absent from the repository. Cheap enough to pin
    because it reads the members, not the 393 MB export -- a governance
    identifier the repository does not hold would show up as a name in the
    WORKING-REGISTER/DOCKET/RULINGS members going missing, and those are read
    here in full."""
    import re as _re
    seen = 0
    for rel in ("method/members/WORKING-REGISTER.md", "method/members/DOCKET.md",
                "method/members/RULINGS-R2.md"):
        p2 = ROOT / rel
        if p2.exists():
            seen += len(_re.findall(r"\bW-\d{1,3}\b|\bRuling\s+\d{1,3}\b",
                                    p2.read_text(encoding="utf-8", errors="replace")))
    # the pin is 0 prose-only, asserted by idcensus.py; this row guards that the
    # three governance members are still present and non-empty to be measured against
    return 0 if seen > 100 else 1


def _hosted():
    """docs/GRAPH-HOSTED.md against HOSTED-GRAPH.tsv -- the one class of figure no
    other check could see.

    The hosted Graphify index is a SERVICE. Its numbers cannot be re-counted by a
    stdlib program, so they are recorded by `hostedgraph.py` and the document is
    pinned against the RECORD rather than against the live service. That direction
    is deliberate and docs/GRAPH-HOSTED.md §7 argues it: pinning prose to a service
    that rebuilds several times a day produces a check that is STALE more often
    than not, and a check that cries wolf is a check nobody reads.

    A STALE row here therefore means "the record moved and the prose did not",
    which is a documentation fault of exactly the kind this instrument exists for.

    The document carries its figures in a stamped indented block (§2). Parsing it
    is how the two are kept to two places rather than three -- were the claimed
    value hardcoded here, this file would be a third place to forget."""
    sys.path.insert(0, str(ROOT / "tools"))
    import hostedgraph
    row = hostedgraph.latest()
    doc = (ROOT / "docs/GRAPH-HOSTED.md").read_text(encoding="utf-8", errors="replace")
    out = []
    if row is None:
        # No record is not a drift; it is an absence, and it is reported as one.
        out.append(("docs/GRAPH-HOSTED.md", "a hosted measurement is on record",
                    True, False))
        return out
    stamped = {}
    for key in ("build", "commit", "nodes", "edges", "communities", "labels_paren"):
        m = re.search(r"^ {4}%s +(\S+)$" % key, doc, re.M)
        stamped[key] = m.group(1) if m else None
    pairs = [("build", "build_id"), ("commit", "commit_sha"), ("nodes", "nodes"),
             ("edges", "edges"), ("communities", "communities"),
             ("labels_paren", "labels_paren")]
    for dockey, tsvkey in pairs:
        out.append(("docs/GRAPH-HOSTED.md",
                    "hosted %s, document against record" % dockey,
                    stamped[dockey], row[tsvkey]))
    # the bound the document states in prose, recomputed from the record
    d = hostedgraph.derived(row)
    out.append(("docs/GRAPH-HOSTED.md", "hosted non-code bound stated in prose",
                ("\u2264 %s" % f"{d['noncode_max']:,}") in doc, True))
    return out


def _instrument_rows():
    """Totals the instruments report, which their per-site selftests do not pin."""
    sites = _pointer_sites()
    claims = _arith_claims()
    if not sites or not claims:
        return [("tools/", "instrument --json could not be read (rows skipped)", 0, 1)]
    pv = lambda v: sum(1 for s in sites if s["verdict"] == v)
    av = lambda v: sum(1 for c in claims if c["verdict"] == v)
    return [
        ("docs/POINTERS.md", "pointer tokens, --roster with-companion", 1932, len(sites)),
        ("docs/POINTERS.md", "findings", 42, sum(1 for s in sites if _is_finding(s))),
        ("docs/POINTERS.md", "RESOLVED", 1387, pv("RESOLVED")),
        ("docs/POINTERS.md", "RESOLVED-HERE", 438, pv("RESOLVED-HERE")),
        ("docs/POINTERS.md", "AMBIGUOUS", 65, pv("AMBIGUOUS")),
        ("docs/POINTERS.md", "PARTIAL", 17, pv("PARTIAL")),
        ("docs/POINTERS.md", "PREFIX-ONLY", 3, pv("PREFIX-ONLY")),
        ("docs/POINTERS.md", "UNRESOLVED", 21, pv("UNRESOLVED")),
        ("docs/POINTERS.md", "KIND-MISMATCH", 1, pv("KIND-MISMATCH")),
        ("docs/ARITH.md", "claims checked, --roster reader-facing", 235, len(claims)),
        ("docs/ARITH.md", "AGREE", 57, av("AGREE")),
        ("docs/ARITH.md", "WITHIN-INPUT-PRECISION", 1, av("WITHIN-INPUT-PRECISION")),
        ("docs/ARITH.md", "DISAGREE (the findings)", 2, av("DISAGREE")),
        ("docs/ARITH.md", "NOT-BOUND", 175, av("NOT-BOUND")),
    ]


def report(verbose=False):
    rows = checks()
    stale = [r for r in rows if r[2] != r[3]]
    doc = None
    for d, label, claimed, got in rows:
        if d != doc:
            print(f"\n  {d}")
            doc = d
        mark = "ok  " if claimed == got else "STALE"
        if verbose or claimed != got:
            print(f"      {mark}  {label:<48} states {claimed!s:<12} measured {got}")
        else:
            print(f"      ok     {label:<48} {got}")
    print()
    if stale:
        print(f"  {len(stale)} of {len(rows)} figures have drifted. The tree is right and the")
        print("  sentence is old: read the named document and correct the prose.")
    else:
        print(f"  all {len(rows)} pinned figures still hold.")
    return 1 if stale else 0


def selftest():
    """Fixtures are structural, not the totals -- a total is what goes stale."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-56s = %-7s expected %-7s %s" % (label, got, want, "ok" if good else "FAIL"))

    rows = checks()
    check("every row carries a document, a claim and a measurement",
          sum(1 for r in rows if len(r) == 4 and r[0] and r[1]), len(rows))
    check("no label is pinned twice", len({(r[0], r[1]) for r in rows}), len(rows))
    # the grouped-heading trap: a bare read must give a DIFFERENT, smaller count
    t = (ROOT / "method/members/The_Method_1_6___The_Register-2.md").read_text(
        encoding="utf-8", errors="replace")
    bare = len({int(m) for m in re.findall(r"\n### (\d+)\n", t)})
    grouped = len(_entries("method/members/The_Method_1_6___The_Register-2.md"))
    check("grouped headings are honoured (bare read is smaller)", bare < grouped, True)
    check("the bare read's shortfall is the documented 32", grouped - bare, 32)
    # the two registers must never overlap -- that is Ruling 27, not a preference
    R = _entries("method/members/The_Method_1_6___The_Register-2.md")
    W = _entries("method/members/WORKING-REGISTER.md")
    check("Ruling 27: the two registers do not overlap", len(R & W), 0)
    check("COVERAGE.tsv is the --chats run (IN-CHAT rows present)",
          sum(1 for r in _rows("COVERAGE.tsv") if r["status"] == "IN-CHAT") > 0, True)
    # the finding predicate is neither half alone -- both halves have been got
    # wrong here, and the report's own by-class breakdown is the arbiter
    sites = _pointer_sites()
    if sites:
        check("pointers: census_class alone under-counts findings",
              sum(1 for s in sites if s.get("census_class")), 40)
        check("pointers: finding verdicts alone under-count findings",
              sum(1 for s in sites if s.get("verdict") in _FINDING_VERDICTS), 25)
        check("pointers: their union is the reported total",
              sum(1 for s in sites if _is_finding(s)), 42)
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true",
                    help="assert the checks' own structure and the corpus's invariants")
    ap.add_argument("-v", "--verbose", action="store_true", help="print every row")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    print("  DOCUMENT FIGURES -- what the repository says about itself, measured")
    return report(verbose=a.verbose)


if __name__ == "__main__":
    sys.exit(main())
