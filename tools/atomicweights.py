#!/usr/bin/env python3
"""atomicweights.py -- the standard atomic weights and isotopic compositions of the elements.

Why it exists. The site's builder and gravity modes refused a mass whenever no isotope was
typed: water had none and iron none. The repository held one nuclear table, AME2020 Table I,
which gives every nuclide's mass and says nothing of what nature mixes. These two tables say
that, and both are the IUPAC Commission on Isotopic Abundances and Atomic Weights' (CIAAW):

  STANDARD-ATOMIC-WEIGHTS.tsv   the standard atomic weights of the Atomic Weights 2021 report
                                (T. Prohaska et al., Pure Appl. Chem. 94, 573 (2022),
                                doi:10.1515/pac-2019-0603), with CIAAW's 2024 revisions
  ISOTOPIC-COMPOSITIONS.tsv     the representative isotopic compositions of the elements, with
                                the same three elements' 2024 revisions

How they are reached. ciaaw.org, iupac.org and the publisher are refused by this environment's
proxy; PyPI is not. `periodictable` 2.1.0 carries both tables as text in its mass.py, taken
from ciaaw.org on 2023-07-06, so the instrument downloads that wheel, pinned by the sha256 PyPI
publishes, and reads the text without importing anything from it. The tables CIAAW prints now
differ from that text at three elements, zirconium, gadolinium and lutetium, revised by the
Commission in 2024; their rows are quoted in REVISED_* below from ciaaw.org as read on
2026-10-17 (the pages state that these three are the 2024 revisions). Every other row checked
against the live pages agrees with the text.

Where the text departs from CIAAW it is not followed. Beside the interval CIAAW prints for
nitrogen, argon and lead, the wheel adds compositions of its own choosing (air for nitrogen and
argon, the 2013 table for lead). CIAAW prints the interval only, so the interval is what is
captured, and the representative value of an isotope given only as an interval is the interval's
midpoint, marked DERIVED; it is used to name the most abundant isotope and for nothing exact.

A standard atomic weight is a value with its uncertainty or, for the fourteen elements whose
terrestrial composition varies, an interval [a, b] beside the abridged value CIAAW gives for it.
An element with no standard atomic weight (no stable isotope and no characteristic terrestrial
composition: Tc, Pm, Po to Ac, Np and beyond) has no row, and the site refuses its mass rather
than inventing one.

READ, never hand-edited; regenerate. stdlib only.

    python3 tools/atomicweights.py               # download the pinned wheel, write tables/ciaaw/
    python3 tools/atomicweights.py --wheel PATH  # the same from a wheel already on disk
    python3 tools/atomicweights.py --verify      # the tables on disk are what the wheel gives
    python3 tools/atomicweights.py --selftest    # the tables against CIAAW's own figures
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tables", "ciaaw")
WEIGHTS_TSV = "STANDARD-ATOMIC-WEIGHTS.tsv"
COMPOSITIONS_TSV = "ISOTOPIC-COMPOSITIONS.tsv"
CAPTURE_TSV = "CAPTURE.tsv"
AME_REL = "extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv"

WHEEL = {
    "project": "periodictable",
    "version": "2.1.0",
    "filename": "periodictable-2.1.0-py3-none-any.whl",
    "sha256": "e9155d2bf5ac10050abeff2f99096d4f04312c0c8a6bb432e28744367c5064b3",
    "json": "https://pypi.org/pypi/periodictable/2.1.0/json",
    "member": "periodictable/mass.py",
}
CITATION_WEIGHTS = ("T. Prohaska et al., Standard atomic weights of the elements 2021 (IUPAC Technical Report), "
                    "Pure Appl. Chem. 94, 573-600 (2022); with the CIAAW's 2024 revisions of Zr, Gd and Lu")
DOI_WEIGHTS = "10.1515/pac-2019-0603"
CITATION_COMPOSITIONS = ("CIAAW, Isotopic compositions of the elements 2024, ciaaw.org; the 2021 edition as transcribed "
                         "with the 2024 revisions of Zr, Gd and Lu. Earlier edition: J. Meija et al., Isotopic compositions "
                         "of the elements 2013 (IUPAC Technical Report), Pure Appl. Chem. 88, 293-306 (2016)")
DOI_COMPOSITIONS = "10.1515/pac-2015-0503"
READ_ON = "2026-10-17"

# The 2024 revisions, quoted from https://www.ciaaw.org/atomic-weights.htm and
# https://www.ciaaw.org/isotopic-abundances.htm as read on 2026-10-17 (digit groups closed up).
REVISED_WEIGHTS = {40: "91.222(3)", 64: "157.249(2)", 71: "174.96669(5)"}
REVISED_COMPOSITIONS = {
    40: {90: "0.5147(6)", 91: "0.1123(6)", 92: "0.1716(4)", 94: "0.1736(7)", 96: "0.0278(4)"},
    64: {152: "0.00204(2)", 154: "0.02187(9)", 155: "0.14828(60)", 156: "0.20493(22)", 157: "0.15657(17)",
         158: "0.24820(20)", 160: "0.21811(28)"},
    71: {175: "0.97414(5)", 176: "0.02586(5)"},
}
# Where the text gives a composition of its own beside CIAAW's interval (air; the 2013 table).
NOT_CIAAW = {7: "composition for air", 18: "composition for air", 82: "composition from the 2013 table"}

WEIGHT_COLS = ["Z", "symbol", "element", "kind", "value", "uncertainty", "low", "high", "notes", "edition", "transcribed"]
COMP_COLS = ["Z", "symbol", "A", "value", "uncertainty", "low", "high", "representative", "status", "notes", "edition", "transcribed"]


def fetch_wheel():
    """The pinned wheel from PyPI, held to the sha256 PyPI publishes for it."""
    meta = json.load(urllib.request.urlopen(WHEEL["json"], timeout=60))
    hit = [f for f in meta["urls"] if f["filename"] == WHEEL["filename"]]
    if not hit:
        raise SystemExit("PyPI lists no %s" % WHEEL["filename"])
    if hit[0]["digests"]["sha256"] != WHEEL["sha256"]:
        raise SystemExit("PyPI's sha256 for %s is not the pinned one" % WHEEL["filename"])
    blob = urllib.request.urlopen(hit[0]["url"], timeout=120).read()
    return blob


def mass_text(blob):
    if hashlib.sha256(blob).hexdigest() != WHEEL["sha256"]:
        raise SystemExit("the wheel's sha256 is not the pinned %s" % WHEEL["sha256"])
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        return z.read(WHEEL["member"])


def block(text, name):
    """The body of one triple-quoted table in mass.py, read as text."""
    m = re.search(r'^%s = """\\\n(.*?)"""' % name, text, re.S | re.M)
    if not m:
        raise SystemExit("mass.py has no %s table" % name)
    return m.group(1).rstrip("\\\n")


def value_unc(s):
    """'55.845(2)' -> (55.845, 0.002); '207.2(1.1)' -> (207.2, 1.1); '1' -> (1.0, 0.0)."""
    m = re.fullmatch(r"(\d+(?:\.(\d+))?)(?:\(([\d.]+)\))?", s)
    if not m:
        raise ValueError("not a value: %r" % s)
    v, dec, u = m.group(1), m.group(2) or "", m.group(3)
    if u is None:
        unc = 0.0
    elif "." in u:
        unc = float(u)
    else:
        unc = int(u) * 10.0 ** (-len(dec))
    return float(v), unc


VAL_RE = re.compile(r"^(?P<val>\d[\d.]*(?:\([\d.]+\))?)?\s*(?:\[(?P<lo>[\d.]+),\s*(?P<hi>[\d.]+)\])?\s*(?P<notes>[a-z ]*)$")


def parse_weights(text):
    rows = []
    for line in block(text, "element_mass").split("\n"):
        if not line.strip():
            continue
        f = line.split("\t")
        Z, sym, name = int(f[0]), f[1].strip(), f[2].strip()
        rest = "\t".join(f[3:]).strip().replace("\t", " ")
        m = VAL_RE.match(rest)
        if not m or not m.group("val"):
            raise SystemExit("element_mass: cannot read %r" % line)
        transcribed = rest
        edition = "2021"
        val = m.group("val")
        if Z in REVISED_WEIGHTS:
            val, edition = REVISED_WEIGHTS[Z], "2024"
        v, u = value_unc(val)
        lo, hi = m.group("lo"), m.group("hi")
        rows.append({"Z": Z, "symbol": sym, "element": name, "kind": "interval" if lo else "value",
                     "value": val.split("(")[0], "uncertainty": _fmt(u), "low": lo or "", "high": hi or "",
                     "notes": " ".join(m.group("notes").split()), "edition": edition, "transcribed": transcribed})
    return rows


def parse_compositions(text, symbols):
    rows, Z = [], None
    for line in block(text, "isotope_abundance").split("\n"):
        if not line.strip():
            continue
        if line[0] not in " \t":
            Z = int(line.split()[0])
            continue
        parts = line.strip().split(None, 1)
        A, rest = int(parts[0]), parts[1].strip().replace("\t", " ") if len(parts) > 1 else ""
        m = VAL_RE.match(rest)
        if not m:
            raise SystemExit("isotope_abundance: cannot read %r" % line)
        val, lo, hi, edition = m.group("val"), m.group("lo"), m.group("hi"), "2021"
        if Z in REVISED_COMPOSITIONS:
            val, lo, hi, edition = REVISED_COMPOSITIONS[Z].get(A), None, None, "2024"
            if val is None:
                raise SystemExit("the 2024 revision of Z = %d names no A = %d" % (Z, A))
        if Z in NOT_CIAAW:
            val = None
        if val:
            v, u = value_unc(val)
            rep, status = v, "READ"
        else:
            v, u = None, None
            rep, status = (float(lo) + float(hi)) / 2, "DERIVED"
        rows.append({"Z": Z, "symbol": symbols.get(Z, ""), "A": A, "value": "" if v is None else val.split("(")[0],
                     "uncertainty": "" if u is None else _fmt(u), "low": lo or "", "high": hi or "",
                     "representative": _fmt(rep), "status": status,
                     "notes": " ".join(m.group("notes").split()), "edition": edition, "transcribed": rest})
    return rows


def _fmt(x):
    return ("%.12g" % x) if isinstance(x, float) else str(x)


def tsv(rows, cols):
    out = io.StringIO()
    out.write("\t".join(cols) + "\n")
    for r in rows:
        out.write("\t".join(str(r[c]) for c in cols) + "\n")
    return out.getvalue().encode("utf-8")


def build(blob):
    text = mass_text(blob).decode("utf-8")
    weights = parse_weights(text)
    symbols = {r["Z"]: r["symbol"] for r in weights}
    comps = parse_compositions(text, symbols)
    member = mass_text(blob)
    capture = [("source", "PyPI %s %s" % (WHEEL["project"], WHEEL["version"])), ("wheel", WHEEL["filename"]),
               ("wheel_sha256", WHEEL["sha256"]), ("member", WHEEL["member"]),
               ("member_md5", hashlib.md5(member).hexdigest()),
               ("transcribed_from", "https://www.ciaaw.org/atomic-weights.htm and isotopic-abundances.htm, 2023-07-06 (the 2021 edition)"),
               ("revised_2024", "Zr, Gd, Lu: quoted from ciaaw.org as read on %s" % READ_ON),
               ("not_followed", "; ".join("Z = %d: the text's %s, beside CIAAW's interval" % (z, w) for z, w in sorted(NOT_CIAAW.items()))),
               ("weights_citation", CITATION_WEIGHTS), ("weights_doi", DOI_WEIGHTS),
               ("compositions_citation", CITATION_COMPOSITIONS), ("compositions_doi", DOI_COMPOSITIONS),
               ("status", "READ; a representative value given only as an interval is its midpoint, DERIVED")]
    cap = ("key\tvalue\n" + "".join("%s\t%s\n" % kv for kv in capture)).encode("utf-8")
    return {WEIGHTS_TSV: tsv(weights, WEIGHT_COLS), COMPOSITIONS_TSV: tsv(comps, COMP_COLS), CAPTURE_TSV: cap}, weights, comps


def load_wheel(path):
    if path:
        with open(path, "rb") as fh:
            return fh.read()
    return fetch_wheel()


def read_tsv(name):
    with open(os.path.join(OUT_DIR, name), encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        return [dict(zip(head, line.rstrip("\n").split("\t"))) for line in fh if line.strip()]


def most_abundant(comps):
    best = {}
    for r in comps:
        z, rep = int(r["Z"]), float(r["representative"])
        if z not in best or rep > best[z][1]:
            best[z] = (int(r["A"]), rep)
    return {z: a for z, (a, _) in best.items()}


def selftest():
    """The written tables against CIAAW's own printed figures, and against AME2020."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-66s %s" % (label, "ok" if good else "FAIL: got %r, want %r" % (got, want)))

    W = {int(r["Z"]): r for r in read_tsv(WEIGHTS_TSV)}
    C = read_tsv(COMPOSITIONS_TSV)
    check("84 elements carry a standard atomic weight", len(W), 84)
    check("H: the interval CIAAW prints, and its abridged value", (W[1]["low"], W[1]["high"], W[1]["value"], W[1]["kind"]),
          ("1.00784", "1.00811", "1.0080", "interval"))
    check("Fe 55.845(2), U 238.02891(3), as printed", (W[26]["value"], W[26]["uncertainty"], W[92]["value"], W[92]["uncertainty"]),
          ("55.845", "0.002", "238.02891", "3e-05"))
    check("the 2024 revisions: Zr 91.222(3), Gd 157.249(2), Lu 174.96669(5)",
          [(W[z]["value"], W[z]["edition"]) for z in (40, 64, 71)], [("91.222", "2024"), ("157.249", "2024"), ("174.96669", "2024")])
    check("Pb is an interval [206.14, 207.94]", (W[82]["kind"], W[82]["low"], W[82]["high"]), ("interval", "206.14", "207.94"))
    check("fourteen elements are intervals", sum(1 for r in W.values() if r["kind"] == "interval"), 14)
    check("no weight for Tc, Pm, Po, At, Rn, Fr, Ra, Ac, Np; Bi, Th, Pa, U carry one",
          ([z in W for z in (43, 61, 84, 85, 86, 87, 88, 89, 93)], [z in W for z in (83, 90, 91, 92)]), ([False] * 9, [True] * 4))
    water = 2 * float(W[1]["value"]) + float(W[8]["value"])
    check("water's molar mass from the abridged weights: 18.015 g/mol", round(water, 3), 18.015)
    fe = [r for r in C if r["Z"] == "26"]
    check("Fe's composition as CIAAW prints it", [(r["A"], r["value"], r["uncertainty"], r["status"]) for r in fe],
          [("54", "0.05845", "0.00105", "READ"), ("56", "0.91754", "0.00106", "READ"), ("57", "0.02119", "0.00029", "READ"),
           ("58", "0.00282", "0.00012", "READ")])
    n = [r for r in C if r["Z"] == "7"]
    check("N: CIAAW's interval only; the text's air value is not followed",
          [(r["value"], r["low"], r["high"], r["status"]) for r in n],
          [("", "0.99578", "0.99663", "DERIVED"), ("", "0.00337", "0.00422", "DERIVED")])
    check("Zr's 2024 composition", [(r["A"], r["value"], r["edition"]) for r in C if r["Z"] == "40"][:2],
          [("90", "0.5147", "2024"), ("91", "0.1123", "2024")])
    top = most_abundant(C)
    check("the most abundant isotope: H-1 C-12 N-14 O-16 Fe-56 Zr-90 Gd-158 Lu-175 Pb-208 U-238",
          [top[z] for z in (1, 6, 7, 8, 26, 40, 64, 71, 82, 92)], [1, 12, 14, 16, 56, 90, 158, 175, 208, 238])
    check("every element with a weight has a composition, and no other", sorted(top), sorted(W))
    # an element whose isotopes all carry a value sums to 1 within their stated uncertainties
    bad = []
    for z in sorted(top):
        rows = [r for r in C if int(r["Z"]) == z]
        if all(r["value"] for r in rows):
            s = sum(float(r["value"]) for r in rows)
            if abs(s - 1) > sum(float(r["uncertainty"] or 0) for r in rows) + 1e-9:
                bad.append((z, s))
    check("compositions sum to 1 within their uncertainties", bad, [])
    with open(os.path.join(ROOT, AME_REL), encoding="utf-8") as fh:
        # comment lines first; the last of them names the columns: Z N A symbol ...
        ame = {(int(f[0]), int(f[2])) for f in (l.rstrip("\n").split("\t") for l in fh if l.strip() and not l.startswith("#"))}
    missing = [(r["Z"], r["A"]) for r in C if (int(r["Z"]), int(r["A"])) not in ame]
    check("every isotope of the compositions is a nuclide of AME2020 Table I", missing, [])
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--wheel", help="a copy of %s already on disk" % WHEEL["filename"])
    ap.add_argument("--verify", action="store_true", help="the tables on disk are what the wheel gives")
    ap.add_argument("--selftest", action="store_true", help="the tables against CIAAW's own figures")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    files, weights, comps = build(load_wheel(a.wheel))
    if a.verify:
        diff = [n for n, b in files.items() if not os.path.exists(os.path.join(OUT_DIR, n)) or open(os.path.join(OUT_DIR, n), "rb").read() != b]
        print("tables/ciaaw/: %s" % ("as the wheel gives them" if not diff else "DIFFERS: " + ", ".join(diff)))
        return 1 if diff else 0
    os.makedirs(OUT_DIR, exist_ok=True)
    for n, b in files.items():
        with open(os.path.join(OUT_DIR, n), "wb") as fh:
            fh.write(b)
        print("  wrote tables/ciaaw/%-28s %7d bytes  md5 %s" % (n, len(b), hashlib.md5(b).hexdigest()))
    print("  %d elements with a standard atomic weight (%d revised 2024), %d isotopes in their compositions"
          % (len(weights), sum(1 for r in weights if r["edition"] == "2024"), len(comps)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
