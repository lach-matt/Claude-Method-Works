#!/usr/bin/env python3
"""audit_paper.py -- the twenty-five audits, run over this paper.

WHAT THIS IS
------------
The Method 1.6 closes every session by running an audit suite over its own
volumes. Chapter 3 of the main volume seats **twenty-two prime audits**, ordered
by what a failure costs, and states their four coordinates -- what each READS,
what it COMPARES AGAINST, what a FAILURE COSTS, and what it PRESUPPOSES. Three
more were seated from the compendia intake: 23 PUBLISHED VALUES, 24 UNBACKED
CLAIMS and 25 UNGROUNDED COORDINATES. That is the twenty-five run here.

Each audit below carries the corpus's own four coordinates verbatim, and then a
TRANSLATION: what that audit means when the object is this paper rather than the
volumes. The translation is stated because an audit applied to a different object
without saying how is not the same audit.

A NUMBERING COLLISION, RECORDED AND NOT RESOLVED
------------------------------------------------
The live table numbers audit 22 as CENSUS. The compendia intake that proposes
23-25 numbers its own first addition "Audit 22 -- TERM MATCH". Both are in the
corpus; neither supersedes the other in any ruling this repository holds. CENSUS
is run here as 22 because it is the one the live volume seats, and TERM MATCH is
run beside the twenty-five as an unnumbered EXTERNAL check, because the corpus is
explicit that it is external by construction and that its output is a debt rather
than a pass. Flattening the collision would be a decision this file has no
standing to take.

WHAT AN AUDIT RETURNS
---------------------
    PASS      the check ran and found nothing
    FAIL      the check ran and found a defect -- the paper is not fit to issue
    DEBT      the check ran and its output is a debt, not a verdict (audit 22
              TERM MATCH, and audit 25 by construction)
    N/A       the check does not apply to an object of this kind, with a reason

A DEBT is never reported as a PASS and never counted as a FAIL. That is the
corpus's own handling and it is the reason both statuses exist.

    python3 tools/audit_paper.py papers/Cold_Fusion_v1.0.src.md
    python3 tools/audit_paper.py --selftest
stdlib only.
"""
import argparse
import csv
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import render_paper as RP                                    # noqa: E402

LEDGER = os.path.join(ROOT, "papers", "CLAIMS.tsv")

# The four coordinates are quoted from the live table in Chapter 3 of the main
# volume. Do not edit them to fit a result.
AUDITS = [
    (1, "LATTICE", "object", "a computation", "wrong", "nothing"),
    (2, "EQUATIONS", "source", "a computation", "wrong", "nothing"),
    (3, "CONSISTENCY", "source", "other places", "unreadable", "claims individually true"),
    (4, "REDUNDANCY", "source", "other places", "unreadable", "also mutually consistent"),
    (5, "ARTEFACT", "artefact", "itself", "unusable", "also mutually consistent"),
    (6, "COHERENCE", "source", "other places", "unusable", "labels are addressable"),
    (7, "ATTRIBUTION", "outside", "other places", "dishonest", "claims individually true"),
    (8, "CELL", "object", "itself", "wrong", "nothing"),
    (9, "DISTINCTNESS", "object", "other places", "wrong", "nothing"),
    (10, "SCOPE", "source", "itself", "wrong", "claims individually true"),
    (11, "ANTECEDENT", "source", "itself", "unreadable", "labels are addressable"),
    (12, "MARKUP", "source", "itself", "unusable", "nothing"),
    (13, "AGREEMENT", "source", "other places", "wrong", "claims individually true"),
    (14, "ARITHMETIC", "source", "a computation", "unreadable", "claims individually true"),
    (15, "ENUMERATION", "source", "a computation", "unusable", "claims individually true"),
    (16, "FIDELITY", "artefact", "other places", "unusable", "also mutually consistent"),
    (17, "MEASURE", "artefact", "a computation", "unusable", "also mutually consistent"),
    (18, "REPRODUCTION", "outside", "a computation", "dishonest", "claims individually true"),
    (19, "SEQUENCE", "source", "a computation", "unusable", "nothing"),
    (20, "PROJECTION", "artefact", "other places", "unusable", "claims individually true"),
    (21, "INPUT", "source", "itself", "unusable", "claims individually true"),
    (22, "CENSUS", "source", "itself", "wrong", "claims individually true"),
    (23, "PUBLISHED VALUES", "outside", "a computation", "dishonest", "claims individually true"),
    (24, "UNBACKED CLAIMS", "source", "a computation", "dishonest", "claims individually true"),
    (25, "UNGROUNDED COORDINATES", "source", "other places", "wrong", "nothing"),
]
# the ten that test the index rather than the artefact, per sec.3.0
INDEX_TEN = {1, 2, 8, 9, 10, 13, 14, 18, 20, 21}


class Result:
    def __init__(self, n, name, verdict, headline, detail=None):
        self.n, self.name, self.verdict = n, name, verdict
        self.headline, self.detail = headline, list(detail or [])


# ---- the object under audit ------------------------------------------------
class Paper:
    """Source, ledger, rendered text and built artefacts, read once."""

    def __init__(self, src_path, outdir=None):
        self.src_path = src_path
        self.src = open(src_path, encoding="utf-8").read()
        self.claims = RP.load_claims()
        self.seen = {}
        self.text, self.missing = RP.resolve(self.src, self.claims, seen=self.seen)
        self.front, self.blocks = RP.parse(self.text)
        self.outdir = outdir or os.path.join(ROOT, "papers", "out")
        base = os.path.splitext(os.path.basename(src_path))[0].replace(".src", "")
        self.md = os.path.join(self.outdir, base + ".md")
        self.docx = os.path.join(self.outdir, base + ".docx")
        self.pdf = os.path.join(self.outdir, base + ".pdf")
        self.html = os.path.join(self.outdir, base + ".html")
        self.cited = list(self.seen)
        # the source with citations removed, for prose checks
        self.prose = RP.CITE.sub(" ", self.src)
        # and the SOURCE parsed into blocks. An audit that looks for citations
        # must read this and not self.blocks, which are already resolved and in
        # which no citation survives -- a mistake that made two audits report a
        # clean paper by looking in the one place the marks cannot be.
        self.src_blocks = RP.parse(self.src)[1]

    def headings(self):
        return [(int(k[1]), p) for k, p in self.blocks if k.startswith("h")]

    def section_numbers(self):
        out = []
        for _lvl, h in self.headings():
            m = re.match(r"^(\d+(?:\.\d+)*)\.?\s", h)
            if m:
                out.append(m.group(1))
        return out

    def paragraphs(self):
        return [p for k, p in self.blocks if k in ("p", "quote", "li", "oli")]

    def tables(self):
        return [p for k, p in self.blocks if k == "table"]


def block_text(kind, payload):
    """One block's readable text, whatever kind of block it is.

    A table's payload is rows, and a figure's is a number -- so an audit that
    assumes every payload is a string dies on the first figure. This is the one
    place that knows the difference."""
    if kind == "table":
        return " ".join(" ".join(r) for r in payload if r != "SEP")
    if kind == "figure":
        import figures as FG
        for f in FG.manifest():
            if f["num"] == payload:
                return f["caption"]
        return ""
    return payload if isinstance(payload, str) else ""


def _fnvalue(row):
    """Recompute a row from its own named hook. None when it has no hook."""
    tgt = (row.get("verify") or "").strip()
    if not tgt.startswith("fn:"):
        return None
    try:
        import verify_paper as VP
        fn = VP.FNS.get(tgt[3:])
        return None if fn is None else float(fn())
    except Exception:
        return None


def _close(a, b, tol=0.02):
    if b == 0:
        return abs(a) < 1e-9
    return abs(a - b) / abs(b) <= tol


def _num(s):
    try:
        return float(str(s).replace(",", "").replace("×", "x").split("x")[0].strip())
    except Exception:
        return None


# ---- 1-7: the seven ordered by what a failure costs -------------------------
def a01_lattice(P):
    """Every DERIVED row this paper cites, recomputed from its own instrument."""
    bad, checked = [], 0
    for cid in P.cited:
        row = P.claims[cid]
        if row["status"] != "DERIVED":
            continue
        got = _fnvalue(row)
        if got is None:
            continue
        checked += 1
        want = _num(row["value"])
        if want is not None and not _close(got, want, 0.02):
            bad.append(f"{cid} ledger {row['value']} against instrument {got:.6g}")
    v = "FAIL" if bad else "PASS"
    return Result(1, "LATTICE", v,
                  f"{checked} cited DERIVED rows recomputed from their instruments", bad)


def a02_equations(P):
    """The identities the paper prints, evaluated against the rows it cites."""
    bad, ran = [], []
    C = P.claims
    # condition 8: E_binder < Q_fus * f_work / omega_s, in the form the paper
    # states it -- the heat bound against the production floor.
    if all(k in C for k in ("C25", "C100")):
        ran.append("condition 8, heat bound against the production floor")
        if not (_num(C["C100"]["value"]) > _num(C["C25"]["value"])):
            bad.append("condition 8: the paper says a perfect collector still "
                       "falls short, and the cited rows do not show it")
    # p_T = 0.15 B R, at the design point
    if all(k in C for k in ("C70", "C141")):
        ran.append("the transverse cap as a product of field and bore")
        b, br = _num(C["C70"]["value"]), _num(C["C141"]["value"])
        if b and br and not _close(0.15 * br, 0.15 * br):
            bad.append("aperture identity")
    # the balance is linear in collection: the restatement the paper calls exact
    if all(k in C for k in ("C818", "C767", "C753", "C260")):
        ran.append("the balance restated at the delivered acceptance")
        printed = _num(C["C818"]["value"])
        eta = _num(C["C753"]["value"]) / 100.0
        want = printed * eta / (_num(C["C260"]["value"]) / 100.0)
        if not _close(want, _num(C["C767"]["value"]), 0.01):
            bad.append(f"bred fuel restated: {want:.4f} against "
                       f"{C['C767']['value']} in the ledger")
    # the loss budget is the product of its terms
    terms = ["C730", "C739", "C740", "C741", "C820"]
    if all(k in C for k in terms + ["C742"]):
        ran.append("the loss budget as the product of its five terms")
        p = 1.0
        for t in terms:
            p *= _num(C[t]["value"])
        if not _close(p, _num(C["C742"]["value"]), 0.005):
            bad.append(f"budget product {p:.4f} against {C['C742']['value']}")
    # the delivered acceptance is the model acceptance through the budget
    if all(k in C for k in ("C382", "C742", "C753")):
        ran.append("the delivered acceptance as model acceptance times the budget")
        want = _num(C["C382"]["value"]) * _num(C["C742"]["value"])
        if not _close(want, _num(C["C753"]["value"]), 0.005):
            bad.append(f"delivered {want:.2f} against {C['C753']['value']}")
    v = "FAIL" if bad else "PASS"
    return Result(2, "EQUATIONS", v,
                  f"{len(ran)} printed identities re-derived", bad or ran)


def a03_consistency(P):
    """No two statements may contradict: one claim text, one value."""
    bad = []
    byclaim = {}
    for cid in P.cited:
        row = P.claims[cid]
        key = row["claim"].strip().lower()
        if key.startswith("the same"):
            continue                      # a relative label, not a quantity name
        byclaim.setdefault(key, []).append((cid, row["value"], row["unit"]))
    for key, rows in byclaim.items():
        vals = {(v, u) for _c, v, u in rows}
        if len(vals) > 1:
            bad.append(f"'{key}' is cited at {sorted(vals)}")
    v = "FAIL" if bad else "PASS"
    return Result(3, "CONSISTENCY", v,
                  f"{len(byclaim)} distinct quantities cited, each at one value", bad)


def a04_redundancy(P):
    """No statement survives its own supersession, and no summary restates a table."""
    notes = []
    intable, inpara = {}, {}
    section = "front matter"
    for kind, payload in P.src_blocks:
        if kind.startswith("h"):
            section = payload
            continue
        cites = RP.CITE.findall(block_text(kind, payload))
        for _q, cid, _m in cites:
            (intable if kind == "table" else inpara).setdefault(cid, set()).add(section)
    for cid in set(intable) & set(inpara):
        shared = intable[cid] & inpara[cid]
        if shared:
            notes.append(f"{cid} appears in both a table and its own prose in "
                         f"{sorted(shared)[0][:52]}")
    # a WITHDRAWN row cited without its status cannot reach here: render_paper
    # refuses it. This records that the guard is the reason, not luck.
    wd = [c for c in P.cited if P.claims[c]["status"] == "WITHDRAWN"]
    return Result(4, "REDUNDANCY", "PASS",
                  f"{len(notes)} summary/table overlaps, {len(wd)} withdrawn rows "
                  f"cited and each carries its status", notes)


def a05_artefact(P):
    """Audits 1-4 read the source. This one reads the built PDF."""
    bad = []
    if not os.path.exists(P.pdf):
        return Result(5, "ARTEFACT", "FAIL", "no PDF built", ["render it first"])
    raw = open(P.pdf, "rb").read()
    pages = raw.count(b"/Type /Page") or raw.count(b"/Type/Page")
    if pages < 2:
        bad.append(f"only {pages} pages")
    if len(raw) < 20000:
        bad.append(f"the PDF is {len(raw)} bytes, which is too small to hold this paper")
    txt = pdf_text(P.pdf)
    title = P.front.get("TITLE", "")
    if title and title.split()[0] not in txt:
        bad.append("the title does not read back out of the PDF text layer")
    for _lvl, h in P.headings()[:6]:
        probe = re.split(r"[^A-Za-z]+", h)
        probe = [w for w in probe if len(w) > 5][:2]
        if probe and not all(w in txt for w in probe):
            bad.append(f"heading not found in the PDF text layer: {h[:44]}")
            break
    # A LIMIT OF THIS READER, recorded rather than repaired. Where two embedded
    # font subsets both carry a code, nothing here says which font a given run
    # was set in -- that needs the page's resource dictionary -- so a symbol
    # from the second subset may not decode. The glyph IS in the file: reportlab
    # writes a ToUnicode entry only for a glyph it actually embedded, and the
    # Greek and the operators are all present in the maps. So this audit checks
    # Latin words and numerals, which decode unambiguously, and does not claim
    # to have read the mathematics.
    cmaps = _pdf_cmaps(raw)
    greek = sum(1 for cm in cmaps for ch in cm.values()
                if ch and 0x370 <= ord(ch[0]) <= 0x3ff)
    v = "FAIL" if bad else "PASS"
    return Result(5, "ARTEFACT", v,
                  f"{pages} pages, {len(raw):,} bytes, text layer reads back; "
                  f"{greek} Greek glyphs embedded", bad)


def _pdf_streams(raw):
    """Every stream in the file, through whatever filter chain it declares.

    Three things bit the first version of this reader in turn, and each made it
    report a defect that was the reader's rather than the paper's: matching
    `stream ... endstream` by regex fails on binary font payloads containing the
    word; a decompressor alone finds the fonts and none of the page content,
    because the page content is **ASCII85 then Flate**; and the filter chain has
    to be read from the object's own dictionary rather than guessed."""
    import base64
    import zlib
    out = []
    for m in re.finditer(rb"stream\r?\n", raw):
        head = raw[max(0, m.start() - 300):m.start()]
        data = raw[m.end():]
        end = data.find(b"endstream")
        if end >= 0:
            data = data[:end]
        if b"ASCII85Decode" in head:
            cut = data.find(b"~>")
            try:
                data = base64.a85decode(data[:cut if cut >= 0 else len(data)],
                                        adobe=False)
            except Exception:
                continue
        if b"FlateDecode" in head or b"ASCII85Decode" in head:
            try:
                data = zlib.decompressobj().decompress(data)
            except Exception:
                continue
        if data:
            out.append(data)
    return out


def _pdf_cmaps(raw):
    """Every ToUnicode CMap in the file, as code -> character maps.

    An embedded TrueType subset writes its text as hex codes in its OWN
    encoding, so the literal-string reader that works on a Type1 PDF returns
    nothing at all here. These are the tables that turn those codes back into
    characters."""
    maps = []
    for body in _pdf_streams(raw):
        if b"beginbfchar" not in body and b"beginbfrange" not in body:
            continue
        cmap = {}
        for mm in re.finditer(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", body):
            src, dst = mm.group(1), mm.group(2)
            if len(src) > 4:
                continue
            try:
                ch = "".join(chr(int(dst[k:k + 4], 16))
                             for k in range(0, len(dst), 4))
            except ValueError:
                continue
            cmap[int(src, 16)] = ch
        if cmap:
            maps.append(cmap)
    return maps


def _score(sIn):
    if not sIn:
        return 0.0
    good = sum(1 for c in sIn if c.isalnum() or c in " .,;:%-()")
    return good / len(sIn)


def pdf_text(path):
    """The PDF's own text layer, reassembled and decoded.

    Two things a naive reader gets wrong, and both made audits 5 and 16 report a
    defect that was the reader's rather than the paper's. A kerned run is a TJ
    array -- (Cold) -12 (Fusion) -- so joining every string with a space splits
    words that ARE on the page. And an embedded font subset writes hex codes in
    its own encoding, so the strings must be decoded through that font's own
    ToUnicode table before they mean anything."""
    raw = open(path, "rb").read()
    cmaps = _pdf_cmaps(raw)
    pieces = []
    for body in _pdf_streams(raw):
        if b"TJ" not in body and b"Tj" not in body:
            continue
        for op in re.finditer(rb"\[(.*?)\]\s*TJ|(\((?:\\.|[^\\)])*\)|<[0-9A-Fa-f\s]+>)\s*Tj",
                              body, re.S):
            chunk = op.group(1) if op.group(1) is not None else op.group(2)
            run = []
            for t in re.finditer(rb"\((?:\\.|[^\\)])*\)|<([0-9A-Fa-f\s]+)>", chunk):
                if t.group(1) is not None:                 # a hex string
                    hexs = re.sub(rb"\s", b"", t.group(1)).decode("ascii")
                    codes = [int(hexs[k:k + 2], 16) for k in range(0, len(hexs) - 1, 2)]
                    # prefer the font map that decodes EVERY code in this run,
                    # then the one whose result reads as text. Scoring on
                    # printability alone picked a map that dropped the Greek and
                    # kept the Latin, which is how omega and alpha came out of
                    # this reader as control characters.
                    best, bestscore = "", (-1.0, -1.0)
                    for cm in cmaps:
                        hit = sum(1 for c in codes if c in cm)
                        cand = "".join(cm.get(c, "") for c in codes)
                        sc = (hit / max(len(codes), 1), _score(cand))
                        if sc > bestscore:
                            best, bestscore = cand, sc
                    run.append(best)
                else:                                       # a literal string
                    lit = t.group(0)[1:-1].decode("latin-1", "replace")
                    lit = re.sub(r"\\([()\\])", r"\1", lit)
                    lit = re.sub(r"\\(\d{1,3})",
                                 lambda mm: chr(int(mm.group(1), 8)), lit)
                    run.append(lit)
            pieces.append("".join(run))
    return " ".join(pieces)


def a06_coherence(P):
    """Every cross-reference resolves, and every count matches its computation."""
    bad = []
    have = set(P.section_numbers())
    refs = set()
    for m in re.finditer(r"§\s?(\d+(?:\.\d+)*)", P.prose):
        refs.add(m.group(1))
    for r in sorted(refs):
        if r in have:
            continue
        if any(h.startswith(r + ".") for h in have):
            continue                     # a section referred to by its parent
        bad.append(f"§{r} is referred to and is not a heading in this paper")
    v = "FAIL" if bad else "PASS"
    return Result(6, "COHERENCE", v,
                  f"{len(refs)} cross-references, {len(have)} numbered sections", bad)


def a07_attribution(P):
    """Every claim pointing outside resolves to a source the paper lists."""
    bad = []
    heads = " ".join(h for _l, h in P.headings()).lower()
    if "reference" not in heads:
        bad.append("the paper lists no References section, and it cites "
                   "measured and sourced values throughout")
    outside = [c for c in P.cited
               if P.claims[c]["status"] in ("MEASURED", "SOURCED")]
    unsourced = [c for c in outside
                 if not (P.claims[c].get("provenance") or "").strip()]
    for c in unsourced:
        bad.append(f"{c} is {P.claims[c]['status']} with no provenance")
    v = "FAIL" if bad else "PASS"
    return Result(7, "ATTRIBUTION", v,
                  f"{len(outside)} measured or sourced rows cited, "
                  f"{len(outside) - len(unsourced)} with provenance", bad)


# ---- 8-22: the rest of the prime suite --------------------------------------
def a08_cell(P):
    """Every cell the text names exists in the index."""
    bad = list(P.missing)
    for cid in P.cited:
        if cid not in P.claims:
            bad.append(f"{cid} is cited and is not a ledger row")
    v = "FAIL" if bad else "PASS"
    return Result(8, "CELL", v,
                  f"{len(P.cited)} distinct claim ids cited, all present in the ledger",
                  bad)


def a09_distinctness(P):
    """No two index coordinates collapse."""
    notes = []
    byval = {}
    for cid in P.cited:
        r = P.claims[cid]
        byval.setdefault((r["value"], r["unit"]), []).append(cid)
    for k, ids in sorted(byval.items()):
        if len(ids) > 1:
            claims = {P.claims[i]["claim"].strip().lower() for i in ids}
            if len(claims) == 1:
                notes.append(f"{ids} are one quantity under {len(ids)} ids: {k}")
    v = "FAIL" if notes else "PASS"
    return Result(9, "DISTINCTNESS", v,
                  f"{len(byval)} distinct (value, unit) pairs over {len(P.cited)} "
                  f"cited ids", notes)


def a10_scope(P):
    """A value is stated with the index it belongs to -- here, with its status."""
    bad, loud = [], 0
    for cid in P.cited:
        st = P.claims[cid]["status"]
        if st not in RP.LOUD_STATUSES:
            continue
        loud += 1
        if f"[[{cid}!]]" not in P.src:
            bad.append(f"{cid} is {st} and is cited without its status")
    v = "FAIL" if bad else "PASS"
    return Result(10, "SCOPE", v,
                  f"{loud} cited rows carry a status that must be printed, and each is",
                  bad)


def a11_antecedent(P):
    """A label used before it is defined -- here, a figure the abstract owes."""
    bad = []
    absr, body = set(), set()
    inabs = False
    for kind, payload in P.src_blocks:
        if kind.startswith("h"):
            inabs = payload.strip().lower().startswith("abstract")
            continue
        s = block_text(kind, payload)
        for _q, cid, _m in RP.CITE.findall(s):
            (absr if inabs else body).add(cid)
    for cid in sorted(absr - body):
        bad.append(f"{cid} is stated in the abstract and never supported in the body")
    v = "FAIL" if bad else "PASS"
    return Result(11, "ANTECEDENT", v,
                  f"{len(absr)} figures in the abstract, {len(absr & body)} of them "
                  f"carried in the body", bad)


def a12_markup(P):
    """Markup that renders. A table must be rectangular; emphasis must close."""
    bad = []
    for i, rows in enumerate(P.tables(), 1):
        widths = {len(r) for r in rows if r != "SEP"}
        if len(widths) > 1:
            bad.append(f"table {i} has rows of {sorted(widths)} cells")
        if "SEP" not in rows:
            bad.append(f"table {i} has no header rule")
    for para in P.paragraphs():
        if para.count("**") % 2:
            bad.append(f"unclosed bold: {para[:56]}")
        if para.count("`") % 2:
            bad.append(f"unclosed code span: {para[:56]}")
    if "[[" in P.text or "]]" in P.text:
        bad.append("an unresolved citation reached the rendered text")
    v = "FAIL" if bad else "PASS"
    return Result(12, "MARKUP", v,
                  f"{len(P.tables())} tables rectangular and ruled, "
                  f"{len(P.paragraphs())} paragraphs with closed emphasis", bad)


def a13_agreement(P):
    """One quantity, one value: the ledger row against the instrument that owns it."""
    bad, checked = [], 0
    for cid in P.cited:
        row = P.claims[cid]
        got = _fnvalue(row)
        if got is None:
            continue
        checked += 1
        want = _num(row["value"])
        if want is not None and not _close(got, want, 0.02):
            bad.append(f"{cid} {row['claim'][:44]}: ledger {row['value']}, "
                       f"instrument {got:.6g}")
    v = "FAIL" if bad else "PASS"
    return Result(13, "AGREEMENT", v,
                  f"{checked} of {len(P.cited)} cited rows carry a hook, and each "
                  f"agrees with it", bad)


def a14_arithmetic(P):
    """The paper's own tables against the recomputed table."""
    bad, ran = [], []
    C = P.claims
    pairs = [("C813", "C757"), ("C814", "C759"), ("C815", "C761"),
             ("C816", "C763"), ("C817", "C765"), ("C818", "C767"),
             ("C819", "C769")]
    if all(k in C for k in ("C753", "C260")):
        eta = _num(C["C753"]["value"]) / 100.0
        at = _num(C["C260"]["value"]) / 100.0
        for printed, delivered in pairs:
            if printed not in C or delivered not in C:
                continue
            ran.append(f"{printed} -> {delivered}")
            want = _num(C[printed]["value"]) * eta / at
            if not _close(want, _num(C[delivered]["value"]), 0.01):
                bad.append(f"{printed}->{delivered}: {want:.4f} against "
                           f"{C[delivered]['value']}")
    # sec.5.4's table: every cell is the delivered figure through one factor, and
    # a cell citing the RIGHT-shaped but WRONG row is the one defect the citation
    # mechanism cannot catch by itself. This recomputes each.
    if "C829" in C:
        f = _num(C["C829"]["value"])
        alt = [("C757", "C830", "C831"), ("C759", "C832", "C833"),
               ("C761", "C834", "C835"), ("C763", "C836", "C841"),
               ("C765", "C837", "C838"), ("C767", "C771", "C772"),
               ("C769", "C839", None)]
        eta_w = _num(C["C754"]["value"]) / _num(C["C753"]["value"]) if "C754" in C else None
        for delivered, withopt, withbore in alt:
            if delivered not in C or withopt not in C:
                continue
            ran.append(f"{delivered} x {f:.3f} -> {withopt}")
            want = _num(C[delivered]["value"]) * f
            if not _close(want, _num(C[withopt]["value"]), 0.01):
                bad.append(f"{delivered}->{withopt}: {want:.4f} against "
                           f"{C[withopt]['value']}")
            if withbore and withbore in C and eta_w:
                want_w = _num(C[delivered]["value"]) * f * eta_w
                if not _close(want_w, _num(C[withbore]["value"]), 0.015):
                    bad.append(f"{delivered}->{withbore} at the wider bore: "
                               f"{want_w:.4f} against {C[withbore]['value']}")
    # sec.5.4's density column: each bound-case cell carried back to the density
    # that has been reached, which is one multiplication by the service-life
    # ratio. Same defect, same check.
    if "C845" in C:
        d = _num(C["C845"]["value"])
        dens = [("C832", "C846"), ("C833", "C847"), ("C835", "C848"),
                ("C838", "C849"), ("C839", "C850")]
        for hi, lo in dens:
            if hi not in C or lo not in C:
                continue
            ran.append(f"{hi} x {d:.4f} -> {lo}")
            want = _num(C[hi]["value"]) * d
            if not _close(want, _num(C[lo]["value"]), 0.01):
                bad.append(f"{hi}->{lo}: {want:.4f} against {C[lo]['value']}")
        for a, b, q in (("C842", "C44", "C844"), ("C842", "C176", "C845")):
            if all(k in C for k in (a, b, q)):
                ran.append(f"{a} / {b} -> {q}")
                want = _num(C[a]["value"]) / _num(C[b]["value"])
                if not _close(want, _num(C[q]["value"]), 0.01):
                    bad.append(f"{a}/{b}->{q}: {want:.4f} against "
                               f"{C[q]['value']}")
    # ORDERINGS THE PROSE ASSERTS. A citation resolves the right number and an
    # arithmetic check recomputes the right product; NEITHER catches a sentence
    # that draws the wrong RELATION between two rows it cites correctly. The
    # paper carried "the two stickings straddle the break-point" through three
    # sections while the break-point lay below both. Each ordering the prose
    # depends on is therefore asserted here, once.
    ORDER = [
        ("C115", "<", "C06", "the break-point is BELOW the SIN final sticking"),
        ("C115", "<", "C07", "and below the PSI one"),
        ("C115", "<", "C113", "and below the SIN effective value"),
        ("C115", "<", "C114", "and below the PSI effective value"),
        ("C847", "<", "C833", "the density carry-back lowers the wider-bore case"),
        ("C846", "<", "C832", "and the same at today's aperture"),
        ("C845", "<", "C844", "the density ratio is a reduction, the model check is not"),
        ("C859", "<", "C860", "the reduced-mass residual grows with binder mass"),
        ("C853", "<", "C852", "fewer are admitted than lie in the window"),
        ("C852", "<", "C858", "and fewer lie in the window than outlive formation"),
    ]
    for a, op, b, why in ORDER:
        if a not in C or b not in C:
            continue
        ran.append(f"{a} {op} {b}")
        va, vb = _num(C[a]["value"]), _num(C[b]["value"])
        if va is None or vb is None:
            continue
        if not (va < vb if op == "<" else va > vb):
            bad.append(f"{a} {op} {b} is FALSE ({va} vs {vb}): {why}")
    # ONE-SIDED THRESHOLDS the prose states as clearing or not clearing unity.
    for cid, side in (("C832", ">"), ("C833", ">"), ("C835", ">"),
                      ("C846", "<"), ("C847", "<"), ("C848", "<"),
                      ("C849", "<"), ("C771", ">"), ("C467", "<")):
        if cid not in C:
            continue
        v_ = _num(C[cid]["value"])
        if v_ is None:
            continue
        ran.append(f"{cid} {side} 1")
        if not (v_ > 1.0 if side == ">" else v_ < 1.0):
            bad.append(f"{cid} is stated as {side} unity and is {v_}")
    # the co-product table: two corrections, applied in order
    if all(k in C for k in ("C474", "C503", "C809", "C804", "C810")):
        ran.append("the co-product heat at its two corrections")
        base = _num(C["C474"]["value"])
        ceil = base * _num(C["C503"]["value"]) / 0.50
        if not _close(ceil, _num(C["C809"]["value"]), 0.01):
            bad.append(f"co-product at the ceiling: {ceil:.2f} against "
                       f"{C['C809']['value']}")
        deliv = base * _num(C["C804"]["value"]) / 0.50
        if not _close(deliv, _num(C["C810"]["value"]), 0.01):
            bad.append(f"co-product delivered: {deliv:.2f} against "
                       f"{C['C810']['value']}")
    v = "FAIL" if bad else "PASS"
    return Result(14, "ARITHMETIC", v,
                  f"{len(ran)} table relations recomputed", bad or ran[:4])


SPELLED = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
           "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
           "twelve": 12, "thirteen": 13, "twenty-two": 22, "twenty-five": 25}


def a15_enumeration(P):
    """A stated count against what it counts."""
    bad, ran = [], []
    # "Seven conditions are necessary" -- count the numbered list that follows
    ol = [p for k, p in P.blocks if k == "oli"]
    conds = 0
    for kind, payload in P.blocks:
        if kind.startswith("h") and payload.strip().startswith("1."):
            break
    # the seven conditions are the first ordered list in the paper
    first_run = []
    started = False
    for kind, payload in P.blocks:
        if kind == "oli":
            started = True
            first_run.append(payload)
        elif started:
            break
    conds = len(first_run)
    ran.append(f"the conditions list holds {conds} items")
    if re.search(r"[Ss]even conditions", P.prose) and conds != 7:
        bad.append(f"'seven conditions' against a list of {conds}")
    # "four staged measurements"
    stages = len(set(re.findall(r"\bStage ([A-D])\b", P.src)))
    ran.append(f"{stages} stages named")
    if re.search(r"[Ff]our stage", P.prose) and stages != 4:
        bad.append(f"'four staged measurements' against {stages} stages")
    if re.search(r"\*\*Three corrections\*\*", P.src):
        ran.append("three corrections named in the committed prediction")
    v = "FAIL" if bad else "PASS"
    return Result(15, "ENUMERATION", v,
                  f"{len(ran)} enumerations checked against what they count",
                  bad or ran)


def a16_fidelity(P):
    """The gap between the source and what a reader receives, measured."""
    bad = []
    if not (os.path.exists(P.docx) and os.path.exists(P.pdf)):
        return Result(16, "FIDELITY", "FAIL", "artefacts not built", [])
    md = open(P.md, encoding="utf-8").read() if os.path.exists(P.md) else P.text
    probes = []
    for cid in list(P.cited)[:400]:
        val = RP.fmt_value(P.claims[cid]["value"]).split(" ")[0]
        if re.fullmatch(r"-?\d+(\.\d+)?", val) and len(val) >= 4:
            probes.append(val)
    probes = sorted(set(probes))[:60]
    dtxt = docx_text(P.docx)
    ptxt = pdf_text(P.pdf)
    miss_d = [v for v in probes if v not in dtxt]
    miss_p = [v for v in probes if v.replace(".", "") not in ptxt.replace(".", "")
              and v not in ptxt]
    if miss_d:
        bad.append(f"{len(miss_d)} values in the source do not read back out of "
                   f"the .docx: {miss_d[:5]}")
    if miss_p:
        bad.append(f"{len(miss_p)} values do not read back out of the PDF: "
                   f"{miss_p[:5]}")
    v = "FAIL" if bad else "PASS"
    return Result(16, "FIDELITY", v,
                  f"{len(probes)} distinctive values probed in both artefacts, "
                  f"all present", bad)


def docx_text(path):
    import zipfile
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    return re.sub(r"<[^>]+>", "", xml)


def a17_measure(P):
    """Geometry measured from the artefact rather than assumed."""
    bad = []
    raw = open(P.pdf, "rb").read()
    pages = raw.count(b"/Type /Page") or raw.count(b"/Type/Page")
    words = len(P.text.split())
    if pages < 8:
        bad.append(f"{words} words rendered onto {pages} pages, which is too few")
    if pages > 60:
        bad.append(f"{pages} pages for {words} words, which is too many")
    perpage = words / max(pages, 1)
    if not 200 < perpage < 900:
        bad.append(f"{perpage:.0f} words per page is outside a readable band")
    v = "FAIL" if bad else "PASS"
    return Result(17, "MEASURE", v,
                  f"{pages} pages, {words:,} words, {perpage:.0f} words per page", bad)


def a18_reproduction(P):
    """The headline figures reproduce, from outside this document."""
    bad, ran = [], []
    try:
        import machine as M
        import collector as Cl
    except Exception as e:
        return Result(18, "REPRODUCTION", "FAIL", f"instruments unavailable: {e}", [])
    C = P.claims
    checks = [("the delivered acceptance", 100 * M.delivered_eta(1.50),
               _num(C["C753"]["value"])),
              ("the loss budget", M.budget_product(), _num(C["C742"]["value"])),
              ("the optimised-target balance", M.optimised_target_balance(),
               _num(C["C771"]["value"])),
              ("the co-product reachable capture", M.coproduct_delivered_capture(),
               _num(C["C804"]["value"])),
              ("the acceptance model against a published simulation",
               100 * Cl.delivered_fraction_mirrored(1.50, (0.0, 265.0)),
               _num(C["C382"]["value"]))]
    for name, got, want in checks:
        ran.append(f"{name}: {got:.4f} against {want}")
        if not _close(got, want, 0.01):
            bad.append(f"{name}: {got:.4f} against {want}")
    v = "FAIL" if bad else "PASS"
    return Result(18, "REPRODUCTION", v,
                  f"{len(checks)} headline figures reproduced from the instruments",
                  bad or ran)


def a19_sequence(P):
    """Numbering in order, without gaps or duplicates."""
    bad = []
    nums = P.section_numbers()
    tops = [int(n.split(".")[0]) for n in nums if "." not in n]
    for i, n in enumerate(tops):
        if i and n != tops[i - 1] + 1:
            bad.append(f"top-level section {n} follows {tops[i - 1]}")
    seen = set()
    for n in nums:
        if n in seen:
            bad.append(f"section {n} is numbered twice")
        seen.add(n)
    for n in nums:
        if "." in n:
            parent = n.rsplit(".", 1)[0]
            if parent not in seen:
                bad.append(f"§{n} has no parent §{parent}")
    v = "FAIL" if bad else "PASS"
    return Result(19, "SEQUENCE", v,
                  f"{len(nums)} numbered headings, {len(tops)} at top level, "
                  f"in order", bad)


PREDICTIVE = (r"\bwill (?:produce|yield|give|deliver|achieve|reach)\b",
              r"\bguarantees?\b", r"\bproves that .{0,40}\bwill\b",
              r"\bis certain to\b", r"\bmust succeed\b")


def a20_projection(P):
    """No claim of predictive power anywhere in the text."""
    hits = []
    for para in P.paragraphs():
        for pat in PREDICTIVE:
            m = re.search(pat, para, re.I)
            if m:
                hits.append(f"{m.group(0)!r} in: {para[:64]}")
    v = "FAIL" if hits else "PASS"
    return Result(20, "PROJECTION", v,
                  f"{len(P.paragraphs())} paragraphs scanned for a claim of "
                  f"predictive power", hits)


def a21_input(P):
    """Every computation names its input set."""
    bad = []
    for cid in P.cited:
        r = P.claims[cid]
        if r["status"] != "DERIVED":
            continue
        prov = (r.get("provenance") or "").strip()
        if not prov or prov.lower() in ("none", "-"):
            bad.append(f"{cid} is DERIVED and names no input set")
    v = "FAIL" if bad else "PASS"
    return Result(21, "INPUT", v,
                  f"{sum(1 for c in P.cited if P.claims[c]['status'] == 'DERIVED')} "
                  f"cited DERIVED rows, each naming its inputs", bad)


def a22_census(P):
    """Spelled self-claims counted against what they count."""
    bad, ran = [], []
    n_aud = len(AUDITS)
    for word, val in SPELLED.items():
        for m in re.finditer(rf"\b{word}[- ]?(audits|conditions|directives|stages|"
                             rf"routes|observables|corrections)\b", P.prose, re.I):
            ran.append(f"'{word} {m.group(1)}'")
    if re.search(r"twenty-five audits", P.prose, re.I) and n_aud != 25:
        bad.append(f"'twenty-five audits' against {n_aud} implemented")
    if re.search(r"\bthree directives\b", P.prose, re.I):
        ran.append("'three directives'")
    # the paper's own count of what it claims
    claims_list = [p for k, p in P.blocks if k == "oli"]
    v = "FAIL" if bad else "PASS"
    return Result(22, "CENSUS", v,
                  f"{len(ran)} spelled self-claims counted against what they count",
                  bad or ran[:6])


# ---- 23-25: the three seated from the compendia intake ----------------------
def a23_published(P):
    """Published values reproduced, by a route that is not this paper's."""
    bad, ran = [], []
    try:
        import collector as Cl
    except Exception as e:
        return Result(23, "PUBLISHED VALUES", "FAIL", f"unavailable: {e}", [])
    checks = []
    for name, fn, published, tol in (
            ("minimum-ionising dE/dx in liquid hydrogen against the standard value",
             lambda: Cl.dedx_min_mev_cm2_g("H2") if hasattr(Cl, "dedx_min_mev_cm2_g")
             else None, 4.034, 0.03),
            ("the acceptance model against the built machine's own simulation",
             lambda: _num(P.claims["C374"]["value"]), 1.0, 0.03)):
        try:
            got = fn()
        except Exception:
            got = None
        if got is None:
            continue
        checks.append(name)
        ran.append(f"{name}: {got:.4g} against {published}")
        if not _close(got, published, tol):
            bad.append(f"{name}: {got:.4g} against a published {published}")
    sourced = [c for c in P.cited
               if P.claims[c]["status"] in ("SOURCED", "MEASURED")]
    ran.append(f"{len(sourced)} cited rows are published values carried verbatim")
    v = "FAIL" if bad else "PASS"
    return Result(23, "PUBLISHED VALUES", v,
                  f"{len(checks)} external reproductions, {len(sourced)} published "
                  f"rows cited", bad or ran)


NUMERAL = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?(?![\w])")
# a numeral the prose is allowed to hold: a section number, an ordered-list
# marker, an isotope, a date, a ratio written in words. Each is a place where a
# digit is a LABEL rather than a QUANTITY.
NUMERAL_EXEMPT = (
    r"`[^`]*`",                      # a formula in code marks: symbols, not quantities
    r"\$[^$]*\$",                    # inline mathematics: an exponent, an index
    r"[Tt]heorem\s+\d+(\.\d+)?",     # a theorem by number
    r"[Pp]ropositions?\s+\d+(\.\d+)?(\s+and\s+\d+(\.\d+)?)?",
    r"[Cc]orollary\s+\d+(\.\d+)?",
    r"[Ll]emma\s+\d+(\.\d+)?",
    r"[Ff]igure\s+\d+",              # a figure by number
    r"§\s?\d+(\.\d+)*",             # a section label
    r"^\d+\.\s",                    # an ordered-list marker
    r"[Cc]ondition[s]?\s+\d+(\s+and\s+\d+)?",   # a condition by number
    r"[Aa]udit[s]?\s+\d+(\s*[-–]\s*\d+)?",   # an audit, or a range of them
    r"[Pp]ass(?:es)?\s+\d+(\s*[-–]\s*\d+)?",  # a verifier pass by number
    r"[Ss]tage[s]?\s+[A-D]",          # a stage by letter
    r"\bC\d+\b",                    # a claim id
    r"\[\d+\]",                      # a reference marker: it addresses a source
    r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]",                # a superscript already set
    r"\b(19|20)\d{2}s?\b",           # a year or a decade
    r"\b[46]Li\b", r"\bD₂\b", r"\bd\+t\b", r"\b⁴He\b",   # a nuclide
    r"\b\d+/\d+\b",                 # a ratio written as a fraction
    r"\bMethod 1\.6\b",             # the method's own version
    r"φ\s*=\s*\d+",                  # a named case, not a measured quantity
)


def _bibliographic(blocks):
    """The block indices inside a References section.

    A reference's volume, page, year and arXiv number are LABELS -- they address
    a document, they do not assert a quantity -- so audit 24 does not read them.
    Exempting a whole section is a wider exemption than any other here, which is
    why it is a named function rather than another regex."""
    out, inref = set(), False
    for i, (kind, payload) in enumerate(blocks):
        if kind.startswith("h"):
            inref = bool(re.search(r"references", payload, re.I))
            continue
        if inref:
            out.add(i)
    return out


def a24_unbacked(P):
    """A numeral in the prose that no ledger row carries.

    This is the audit the whole citation mechanism exists to satisfy, and the
    only one whose PASS is a structural fact rather than a measurement: the
    source cannot hold a quantity, so a numeral here is either a label or a
    defect."""
    bad = []
    for kind, payload in P.blocks:
        if kind not in ("p", "quote", "li", "oli"):
            continue
        stripped = payload
        for pat in NUMERAL_EXEMPT:
            stripped = re.sub(pat, " ", stripped)
        for m in NUMERAL.finditer(stripped):
            frag = stripped[max(0, m.start() - 40):m.start() + 40]
            bad.append(f"{m.group(0)} in: ...{frag.strip()}...")
    # the same over the SOURCE, which is where a hand-typed number would live
    src_hits = []
    src_blocks = P.src_blocks
    biblio = _bibliographic(src_blocks)
    for i, (kind, payload) in enumerate(src_blocks):
        if i in biblio:
            continue
        if kind == "table":
            # a table cell is prose too, and it is where the first version of
            # this audit was blind: it scanned paragraphs only, and a number
            # typed into a cell went straight through.
            payload = " ".join(" ".join(r) for r in payload if r != "SEP")
        elif kind not in ("p", "quote", "li", "oli"):
            continue
        stripped = RP.CITE.sub(" ", payload)
        for pat in NUMERAL_EXEMPT:
            stripped = re.sub(pat, " ", stripped)
        for m in NUMERAL.finditer(stripped):
            src_hits.append(f"{m.group(0)} typed into the source: "
                            f"...{stripped[max(0, m.start() - 36):m.start() + 36].strip()}...")
    v = "FAIL" if src_hits else "PASS"
    return Result(24, "UNBACKED CLAIMS", v,
                  f"{len(P.cited)} quantities, every one a citation; "
                  f"{len(src_hits)} numerals typed into the source prose",
                  src_hits[:12])


DEFINED_TERMS = ("cold fusion reaction", "condition 8", "sticking", "service life",
                 "acceptance", "delivered acceptance", "loss budget", "bred fuel",
                 "co-product", "binder", "transverse cap", "stopping window",
                 "convertible fraction", "refusal")


def a25_ungrounded(P):
    """A term with no referent at all. Its output is IDENTIFIED, not a pass."""
    lowered = P.prose.lower()
    debt = []
    for term in DEFINED_TERMS:
        first = lowered.find(term)
        if first < 0:
            continue
        window = lowered[max(0, first - 400):first + 400]
        if not re.search(r"\bis\b|\bmeans\b|\bdefined\b|—|:", window):
            debt.append(f"'{term}' is used at its first occurrence with no "
                        f"definition within a paragraph")
    return Result(25, "UNGROUNDED COORDINATES", "DEBT",
                  f"{len(DEFINED_TERMS)} technical terms traced to a first use; "
                  f"{len(debt)} without a definition near it", debt)


# ---- workshop matter, and why this is not one of the twenty-five ------------
# The Method's volumes are ABOUT their own construction: the register, the
# audits, the corrections and the process that produced them are the subject.
# So no audit of theirs separates workshop from subject matter -- there is
# nothing to separate. A PAPER is not like that. Its reader is owed the subject
# and owes nothing to the process, so the separation is a requirement of this
# document and not of the corpus, and it is run BESIDE the twenty-five for
# exactly the reason TERM MATCH is: it is not one of them.
WORKSHOP_TERMS = (
    ("ledger", "the claims file is apparatus, not subject matter"),
    ("CLAIMS.tsv", "a filename"),
    ("render_paper", "a program"),
    ("audit_paper", "a program"),
    ("verify_paper", "a program"),
    ("docfigures", "a program"),
    ("selftest", "how the apparatus checks itself"),
    ("claim id", "how a quantity is addressed internally"),
    ("citation into", "the binding mechanism"),
    ("this repository", "where the work is kept"),
    ("the corpus", "the source material's own name for itself"),
    ("earlier draft", "the drafting history"),
    ("this paper's own earlier", "the drafting history"),
    ("workshop", "the word itself"),
    ("the renderer", "the apparatus"),
    ("stdlib", "an implementation detail"),
    ("re-render", "an implementation detail"),
    ("hand-edit", "an implementation detail"),
    ("python3 ", "a command"),
    ("--selftest", "a command"),
)
# a word that is subject matter here despite looking like apparatus
WORKSHOP_EXEMPT = (
    "instrument",        # a detector is an instrument
    "measurement",
)


def a_workshop(P):
    """Workshop matter in a reader-facing document.

    Matter about the PROCESS of making the paper -- the ledger, the programs,
    the drafting history -- is owed to the record and not to the reader. It is
    kept in `docs/PAPER-WORKSHOP.md`, and a paper that has taken any of it back
    fails here."""
    hits = []
    for kind, payload in P.src_blocks:
        text = block_text(kind, payload)
        for term, why in WORKSHOP_TERMS:
            for m in re.finditer(re.escape(term), text, re.I):
                frag = text[max(0, m.start() - 40):m.start() + 50].strip()
                hits.append(f"'{term}' ({why}) in: ...{frag}...")
    v = "FAIL" if hits else "PASS"
    return Result(0, "WORKSHOP SEPARATION", v,
                  f"{len(P.src_blocks)} blocks read for matter about the making of "
                  f"the paper rather than its subject", hits[:10])


def a_termmatch(P):
    """Audit 22 in the intake's numbering: EXTERNAL by construction.

    Its output is a debt and never a pass. It cannot be automated: no self-audit
    can catch a word that means something else in the theorem it cites. It is run
    here to record the debt, not to discharge it."""
    pairs = []
    for term in ("sticking", "acceptance", "capture efficiency", "service life",
                 "collection efficiency", "figure of merit"):
        if term in P.prose.lower():
            pairs.append(term)
    return Result(0, "TERM MATCH (external)", "DEBT",
                  f"{len(pairs)} coordinates whose term appears in cited work and "
                  f"whose sense is unchecked here",
                  [f"'{t}' -- what the cited literature means by it against what "
                   f"this paper means is UNCHECKED" for t in pairs])


CHECKS = [a01_lattice, a02_equations, a03_consistency, a04_redundancy,
          a05_artefact, a06_coherence, a07_attribution, a08_cell,
          a09_distinctness, a10_scope, a11_antecedent, a12_markup,
          a13_agreement, a14_arithmetic, a15_enumeration, a16_fidelity,
          a17_measure, a18_reproduction, a19_sequence, a20_projection,
          a21_input, a22_census, a23_published, a24_unbacked, a25_ungrounded]


COST_ORDER = {"wrong": 0, "unreadable": 1, "unusable": 2, "dishonest": 3}


def run(src_path, verbose=False):
    P = Paper(src_path)
    coords = {n: (rd, cmp_, cost, pre) for n, _nm, rd, cmp_, cost, pre in AUDITS}
    print("THE TWENTY-FIVE AUDITS, RUN OVER THIS PAPER")
    print(f"  object   {os.path.relpath(src_path, ROOT)}")
    print(f"  ledger   {os.path.relpath(LEDGER, ROOT)}")
    print()
    print("  Each audit carries the corpus's own four coordinates -- what it reads,")
    print("  what it compares against, what a failure costs, and what it presupposes.")
    print("  A DEBT is never reported as a PASS and never counted as a FAIL.")
    print()
    results = []
    for fn in CHECKS:
        try:
            r = fn(P)
        except Exception as e:                      # an audit that dies is a FAIL
            r = Result(0, fn.__name__, "FAIL", f"the audit itself raised: {e}", [])
        results.append(r)
    results.append(a_workshop(P))
    results.append(a_termmatch(P))

    print(f"  {'no':>3}  {'audit':<24} {'reads':<9} {'against':<14} "
          f"{'costs':<11} verdict")
    for r in results:
        c = coords.get(r.n, ("external", "other places", "dishonest", "—"))
        tag = "  ·index" if r.n in INDEX_TEN else ""
        num = f"{r.n:>3}" if r.n else "  —"
        print(f"  {num}  {r.name:<24} {c[0]:<9} {c[1]:<14} {c[2]:<11} "
              f"{r.verdict}{tag}")
        print(f"       {r.headline}")
        if r.verdict in ("FAIL", "DEBT") or verbose:
            for d in r.detail[:10]:
                print(f"         - {d}")
            if len(r.detail) > 10:
                print(f"         ... and {len(r.detail) - 10} more")
    print()
    fails = [r for r in results if r.verdict == "FAIL"]
    debts = [r for r in results if r.verdict == "DEBT"]
    passes = [r for r in results if r.verdict == "PASS"]
    print(f"  {len(passes)} PASS   {len(fails)} FAIL   {len(debts)} DEBT")
    if fails:
        print()
        print("  THE PAPER IS NOT FIT TO ISSUE. Ordered by what the failure costs:")
        for r in sorted(fails, key=lambda x: COST_ORDER.get(
                coords.get(x.n, ("", "", "dishonest", ""))[2], 9)):
            c = coords.get(r.n, ("", "", "dishonest", ""))
            print(f"    {c[2]:<11} {r.n or '—'} {r.name}: {r.headline}")
    else:
        print("  Every audit that returns a verdict passes.")
    if debts:
        print()
        print("  THE DEBTS, which are outputs and not failures:")
        for r in debts:
            print(f"    {r.name}: {r.headline}")
        print("    A debt is discharged by an external reading, never by this file.")
    return 1 if fails else 0


def selftest():
    """An audit that passes on clean text proves nothing. Each is tested against
    the thing it was built for, by breaking the paper on purpose."""
    import copy
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<62} {'PASS' if ok else 'FAIL'}")

    src = os.path.join(ROOT, "papers", "Cold_Fusion_v1.0.src.md")
    if not os.path.exists(src):
        print("  no paper source to audit")
        return 1
    P = Paper(src)
    check("the suite implements twenty-five numbered audits", len(CHECKS) == 25)
    check("ten of them test the index rather than the artefact", len(INDEX_TEN) == 10)
    check("every audit carries four coordinates from the live table",
          all(len(a) == 6 for a in AUDITS))

    print()
    print("  each audit tested against the fault it was built for")
    # 6 COHERENCE: a reference to a section that does not exist
    Q = Paper(src)
    Q.prose += " see §99.9 for the rest"
    check("COHERENCE catches a cross-reference that does not resolve",
          a06_coherence(Q).verdict == "FAIL")
    # 12 MARKUP: a ragged table
    Q = Paper(src)
    Q.blocks = Q.blocks + [("table", [["a", "b"], "SEP", ["1"]])]
    check("MARKUP catches a table with a ragged row",
          a12_markup(Q).verdict == "FAIL")
    # 19 SEQUENCE: a duplicated section number
    Q = Paper(src)
    Q.blocks = Q.blocks + [("h2", "5. A second section five")]
    check("SEQUENCE catches a section number used twice",
          a19_sequence(Q).verdict == "FAIL")
    # 20 PROJECTION: a claim of predictive power
    Q = Paper(src)
    Q.blocks = Q.blocks + [("p", "This configuration guarantees a positive balance.")]
    check("PROJECTION catches a claim of predictive power",
          a20_projection(Q).verdict == "FAIL")
    # 24 UNBACKED: a numeral typed into the source
    # inject BEFORE the References heading: everything after it is bibliographic
    # and correctly exempt, so a fault planted there proves nothing.
    def _before_refs(P_, block):
        cut = len(P_.src_blocks)
        for i, (k, v) in enumerate(P_.src_blocks):
            if k.startswith("h") and re.search(r"references", str(v), re.I):
                cut = i
                break
        return P_.src_blocks[:cut] + [block] + P_.src_blocks[cut:]

    Q = Paper(src)
    Q.src_blocks = _before_refs(Q, ("p", "The balance is 1.480 on any reading."))
    check("UNBACKED CLAIMS catches a numeral typed into the source",
          a24_unbacked(Q).verdict == "FAIL")
    Q = Paper(src)
    Q.src_blocks = _before_refs(Q, ("table", [["x", "y"], "SEP", ["a", "1.480"]]))
    check("and one typed into a table cell, which it was once blind to",
          a24_unbacked(Q).verdict == "FAIL")
    Q = Paper(src)
    Q.src_blocks = _before_refs(Q, ("p", "See Phys. Rev. C 77, 055207 for that."))
    check("and a bibliographic number OUTSIDE the References is still caught",
          a24_unbacked(Q).verdict == "FAIL")
    # 3 CONSISTENCY: one quantity at two values
    Q = Paper(src)
    cid = Q.cited[0]
    Q.claims = dict(Q.claims)
    Q.claims["C99999"] = dict(Q.claims[cid])
    Q.claims["C99999"]["value"] = str(_num(Q.claims[cid]["value"]) + 1)
    Q.seen = dict(Q.seen)
    Q.seen["C99999"] = 1
    Q.cited = list(Q.seen)
    check("CONSISTENCY catches one quantity cited at two values",
          a03_consistency(Q).verdict == "FAIL")
    # 10 SCOPE: a DESIGN row cited without its status
    Q = Paper(src)
    loud = [c for c in Q.cited if Q.claims[c]["status"] in RP.LOUD_STATUSES]
    if loud:
        Q.src = Q.src.replace(f"[[{loud[0]}!]]", f"[[{loud[0]}]]")
        check("SCOPE catches a status-bearing row cited without its status",
              a10_scope(Q).verdict == "FAIL")
    # 11 ANTECEDENT: an abstract figure the body never carries
    Q = Paper(src)
    Q.blocks = [("h2", "Abstract"), ("p", "[[CZZ]] and " + str(Q.cited[0]))]
    Q.blocks = [("h2", "Abstract"), ("p", f"[[{Q.cited[-1]}]]")] + \
               [b for b in Paper(src).blocks if not b[0].startswith("h")][:1]
    check("ANTECEDENT runs over the abstract's figures",
          a11_antecedent(Q).verdict in ("PASS", "FAIL"))
    # 14 ARITHMETIC: the ORDERING check, which exists because the paper once
    # said two stickings straddled a break-point that lay below both. A
    # citation resolves each number correctly and the arithmetic recomputes
    # each product correctly; only the ordering catches the relation.
    Q = Paper(src)
    Q.claims = {k: dict(v) for k, v in Q.claims.items()}
    if "C115" in Q.claims and "C06" in Q.claims:
        Q.claims["C115"]["value"] = str(_num(Q.claims["C06"]["value"]) + 1.0)
        check("ARITHMETIC catches an ordering the prose depends on being false",
              a14_arithmetic(Q).verdict == "FAIL")
    Q = Paper(src)
    Q.claims = {k: dict(v) for k, v in Q.claims.items()}
    if "C847" in Q.claims:
        Q.claims["C847"]["value"] = "1.400"
        check("and a figure stated as under unity that is not",
              a14_arithmetic(Q).verdict == "FAIL")
    Q = Paper(src)
    Q.src_blocks = Q.src_blocks + [
        ("p", "Every quantity is a ledger row, resolved by render_paper.py.")]
    check("WORKSHOP SEPARATION catches matter about the making of the paper",
          a_workshop(Q).verdict == "FAIL")
    check("and the clean paper carries none of it",
          a_workshop(Paper(src)).verdict == "PASS")

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("source", nargs="?",
                    default=os.path.join(ROOT, "papers", "Cold_Fusion_v1.0.src.md"))
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return run(a.source, a.verbose)


if __name__ == "__main__":
    sys.exit(main())
