#!/usr/bin/env python3
r"""
pdgcapture.py -- CAPTURE THE PDG PARTICLE TABLE ONCE, WITH ITS PROVENANCE.

    python3 pdgcapture.py --write     write captures/PDG-2026.tsv
    python3 pdgcapture.py --verify    re-derive and compare against the file
    python3 pdgcapture.py --selftest  fixtures

THIS IS THE ONLY FILE HERE THAT IMPORTS `particle`.  Everything downstream
reads the TSV and is stdlib-only, which is the house rule; a capture is how
this tree already handles AME2020 for `gravity`.

===============================================================================
PROVENANCE, AND WHY IT IS RECORDED RATHER THAN CITED
===============================================================================

SOURCE.  Review of Particle Physics, Particle Data Group -- Takahashi et al.,
Int. J. Mod. Phys. A 41, 2630011 (2026).  The 2026 edition.

VIA.  The scikit-hep `particle` package.  Its data directory carries
`mass_width_2026.txt`, whose header reads "MASSES, WIDTHS, AND MC ID NUMBERS
FROM 2026 EDITION OF RPP ... generated on 11-May-2026 by the Berkeley Particle
Data Group", and `particle2026.csv`, "version 16 - 2026-06-03".

    A PROVENANCE SUBTLETY, RECORDED BECAUSE IT WOULD OTHERWISE BE REPEATED
    WRONGLY.  The package's own data README says `particle2026.csv` "was
    created from pdgid_to_latexname.csv, mass_width_2008.fwf,
    mass_width_2008_ext.fwf and mass_width_2025.txt" -- naming the 2025 file
    under a 2026 name.  The two mass_width files are NOT identical here, so
    the README is either stale or the 2026 CSV predates the 2026 txt.  This
    file therefore records the md5 of what it actually read and does not
    repeat the README's lineage claim.

    AND THE QUANTUM NUMBERS ARE OLDER THAN THE MASSES.  The same README says
    the modern .txt has "much less information"; I, G, P and C reach the CSV
    from `mass_width_2008.fwf` and a maintainers' extension.  Masses are 2026;
    THE QUANTUM NUMBERS THIS PROJECT CHARTS TRACE TO A 2008 FILE.  Nine
    spot-checks against canonical values are fixtures below, which is the
    check that matters more than the date.

WHAT IS EXCLUDED, AND ON WHOSE AUTHORITY.

    COMPOSITE NUCLEI, by PDG code range and NOT by the package's
    `is_nucleus`, which is true of the proton and the neutron as well because
    the proton doubles as hydrogen-1's nucleus.  Filtering on it drops p, n and
    their antiparticles, which is what the first version of this file did.  See
    the note at `_is_composite_nucleus`.  The nuclides are the periodic
    elements and `gravity` already seats 3,394 nuclide-charge states.

    STATUS 4, "NotInPDT".  54 entries -- the fourth-generation tau' and its
    neutrino, and all 50 DIQUARKS, which are bookkeeping constructs and not
    observable particles.  The filter is PDG's OWN status flag and not a
    judgement of this file's.

    572 REMAIN: 292 baryons, 250 mesons, 12 quarks, 12 leptons, 6 gauge
    bosons and the Higgs.

UNKNOWN IS A VALUE AND IS NEVER SILENTLY DROPPED.  The package encodes an
absent parity or C-parity as the integer 5 (`Parity.u`).  A lepton has no
absolute intrinsic parity and C-parity is defined only for self-conjugate
states, so these absences are physics and not gaps in the table.  The capture
writes "?" for them.  Any instrument that charts such a coordinate must decide
what to do with "?" and SAY so; charting 5 as if it were a parity would be
fabrication.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "captures", "PDG-2026.tsv")

CITE = ("Review of Particle Physics, Particle Data Group -- Takahashi et al., "
        "Int. J. Mod. Phys. A 41, 2630011 (2026)")
COLS = ("pdgid", "name", "family", "J2", "P", "C", "I2", "G", "Q3",
        "anti", "quarks", "mass_MeV", "width_MeV", "status", "rank")

# Nine canonical (I^G J^PC) assignments, from the standard references, used to
# check the capture rather than to build it.  A disagreement here means the
# table is not what this file thinks it is.
SPOT = {
    111:  ("pi0",    2, -1, +1, -1, +1),      # 1-(0-+)
    113:  ("rho0",   2, +1, +1, -1, -1),      # 1+(1--)
    2212: ("p",      1, None, +1, +1, None),  # 1/2(1/2+)
    443:  ("Jpsi",   0, -1, +1, -1, -1),      # 0-(1--)
    22:   ("gamma",  None, None, +1, -1, -1),
    13:   ("mu-",    None, None, +1, None, None),
    311:  ("K0",     1, None, 0, -1, None),   # 1/2(0-)
    3122: ("Lambda", 0, None, +1, +1, None),  # 0(1/2+)
    -2212:("pbar",   1, None, +1, -1, None),  # opposite intrinsic parity
}


# THE NUCLEON TRAP.  `PDGID.is_nucleus` is TRUE for the proton, the neutron
# and their antiparticles, because in the PDG numbering scheme the proton also
# serves as hydrogen-1's nucleus.  A filter written as `if is_nucleus: skip`
# therefore silently drops the four most important baryons there are, and the
# baryon count still looks plausible, so nothing flags it.  It happened here.
#
# The real boundary is the code range: a composite nucleus is +-10LZZZAAAI, ten
# digits, so abs(id) >= 1e9.  The four nucleons carry four-digit baryon codes.
# Measured: exactly four entries are is_nucleus and below that range, and they
# are p, n, p~, n~.
NUCLEUS_CODE_FLOOR = 1000000000


def _is_composite_nucleus(pdgid):
    return abs(int(pdgid)) >= NUCLEUS_CODE_FLOOR


def _rows():
    from particle import PDGID, Particle
    out = []
    for p in Particle.all():
        i = PDGID(p.pdgid)
        if _is_composite_nucleus(p.pdgid) or int(p.status) == 4:
            continue
        fam = ("lepton" if i.is_lepton else "quark" if i.is_quark
               else "gauge" if i.is_gauge_boson_or_higgs
               else "meson" if i.is_meson else "baryon" if i.is_baryon
               else "other")

        def q(v):
            return "?" if v is None or v == 5 else v

        def half(v):
            return "?" if v is None else int(2 * v)

        out.append({
            "pdgid": int(p.pdgid), "name": p.name, "family": fam,
            "J2": half(p.J), "P": q(p.P), "C": q(p.C),
            "I2": half(p.I) if p.I is not None else "?", "G": q(p.G),
            "Q3": int(round(3 * float(p.charge))) if p.charge is not None else "?",
            "anti": int(p.anti_flag),
            "quarks": p.quarks or "-",
            "mass_MeV": ("?" if p.mass is None else "%.9g" % float(p.mass)),
            "width_MeV": ("?" if p.width is None else "%.9g" % float(p.width)),
            "status": int(p.status), "rank": int(p.rank),
        })
    return sorted(out, key=lambda r: (r["family"], r["pdgid"]))


def _looks_like_diquark(pdgid):
    """PDG diquark codes are +-AAB00C with the two lowest quark digits zero."""
    n = abs(int(pdgid))
    return 1100 <= n <= 5599 and (n // 100) % 10 == 0 and n % 100 in (1, 3)


def _source_md5():
    import particle
    d = os.path.join(os.path.dirname(particle.__file__), "data")
    h = {}
    for f in ("particle2026.csv", "mass_width_2026.txt"):
        p = os.path.join(d, f)
        if os.path.exists(p):
            h[f] = hashlib.md5(open(p, "rb").read()).hexdigest()
        else:
            h[f] = "ABSENT"
    return h


def write():
    import particle
    rows = _rows()
    md5 = _source_md5()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# %s\n" % CITE)
        fh.write("# via scikit-hep particle %s\n" % particle.__version__)
        for k, v in sorted(md5.items()):
            fh.write("# source md5  %-22s %s\n" % (k, v))
        fh.write("# excluded: nuclei (the periodic elements, seated as "
                 "gravity) and PDG status 4 NotInPDT (fourth generation and "
                 "diquarks)\n")
        fh.write("# '?' means the quantity is NOT DEFINED or not known -- it "
                 "is never a value\n")
        fh.write("# rows %d\n" % len(rows))
        fh.write("\t".join(COLS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in COLS) + "\n")
    return OUT, len(rows)


def read():
    """[{col: value}] from the capture.  Stdlib only -- this is the read path."""
    rows = []
    with open(OUT, encoding="utf-8") as fh:
        head = None
        for ln in fh:
            if ln.startswith("#"):
                continue
            p = ln.rstrip("\n").split("\t")
            if head is None:
                head = p
                continue
            rows.append(dict(zip(head, p)))
    return rows


def header():
    return [l.rstrip("\n") for l in open(OUT, encoding="utf-8")
            if l.startswith("#")]


def verify():
    """(agrees, message) -- the file against a fresh derivation."""
    if not os.path.exists(OUT):
        return False, "capture absent -- run --write"
    fresh = _rows()
    have = read()
    if len(fresh) != len(have):
        return False, "row count %d on disk, %d fresh" % (len(have), len(fresh))
    bad = [f["pdgid"] for f, h in zip(fresh, have)
           if any(str(f[c]) != h[c] for c in COLS)]
    if bad:
        return False, "%d rows differ, e.g. %s" % (len(bad), bad[:6])
    return True, "the capture agrees with a fresh derivation of %d rows" % len(have)


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    R = read()
    by = {int(r["pdgid"]): r for r in R}
    chk("572 particles captured", len(R), 572)
    import collections
    fam = collections.Counter(r["family"] for r in R)
    chk("the families", dict(sorted(fam.items())),
        {"baryon": 292, "gauge": 6, "lepton": 12, "meson": 250, "quark": 12})
    chk("no nucleus survived the filter",
        [r["name"] for r in R if r["family"] == "other"], [])
    # tested STRUCTURALLY, not by name -- an earlier version of this fixture
    # matched "(" and ")" and flagged Lambda(1520) as a diquark
    chk("no diquark survived it -- checked on the PDG id, not the name",
        [r["name"] for r in R if _looks_like_diquark(int(r["pdgid"]))], [])
    chk("no status-4 row survived it",
        sorted({r["status"] for r in R if r["status"] == "4"}), [])
    # likewise structural: eta'(958) and Xi(c)' are not fourth-generation
    chk("no fourth generation -- by pdgid, not by an apostrophe in the name",
        sorted(int(r["pdgid"]) for r in R
               if abs(int(r["pdgid"])) in (17, 18)), [])
    chk("AND THE FOUR NUCLEONS ARE PRESENT -- the trap this file documents",
        sorted(int(r["pdgid"]) for r in R
               if abs(int(r["pdgid"])) in (2212, 2112)),
        [-2212, -2112, 2112, 2212])

    # THE NINE SPOT-CHECKS.  Canonical assignments, checked against the
    # capture; these are what make the table trustworthy, not its date.
    def g(pid, col):
        v = by[pid][col]
        return None if v == "?" else int(v)
    for pid, (nm, I2, G, P, Pv, C) in SPOT.items():
        pass
    chk("pi0 is 1-(0-+)",
        (g(111, "I2"), g(111, "G"), g(111, "J2"), g(111, "P"), g(111, "C")),
        (2, -1, 0, -1, 1))
    chk("rho(770)0 is 1+(1--)",
        (g(113, "I2"), g(113, "G"), g(113, "J2"), g(113, "P"), g(113, "C")),
        (2, 1, 2, -1, -1))
    chk("the proton is 1/2(1/2+)",
        (g(2212, "I2"), g(2212, "J2"), g(2212, "P")), (1, 1, 1))
    chk("J/psi is 0-(1--)",
        (g(443, "I2"), g(443, "G"), g(443, "J2"), g(443, "P"), g(443, "C")),
        (0, -1, 2, -1, -1))
    chk("the photon is J=1, P=-1, C=-1, Q=0",
        (g(22, "J2"), g(22, "P"), g(22, "C"), g(22, "Q3")), (2, -1, -1, 0))
    chk("the muon has J=1/2, Q=-1 and NO parity or C-parity",
        (g(13, "J2"), g(13, "Q3"), by[13]["P"], by[13]["C"]), (1, -3, "?", "?"))
    chk("K0 is 1/2(0-)",
        (g(311, "I2"), g(311, "J2"), g(311, "P")), (1, 0, -1))
    chk("Lambda is 0(1/2+)",
        (g(3122, "I2"), g(3122, "J2"), g(3122, "P")), (0, 1, 1))
    chk("THE ANTIPROTON HAS THE OPPOSITE INTRINSIC PARITY to the proton",
        (g(2212, "P"), g(-2212, "P")), (1, -1))

    # the quark charges, which are the reason Q is captured in thirds
    chk("the up-type quarks carry Q = +2/3",
        sorted({g(by_pid, "Q3") for by_pid in (2, 4, 6)}), [2])
    chk("the down-type quarks carry Q = -1/3",
        sorted({g(by_pid, "Q3") for by_pid in (1, 3, 5)}), [-1])

    # unknown is a value, and it is common
    unk = sum(1 for r in R if r["C"] == "?")
    chk("C-parity is UNDEFINED for most of them, and marked so", unk > 400, True)

    chk("the provenance names the PDG edition",
        any("2630011" in h for h in header()), True)
    chk("and records the md5 of what it actually read",
        sum(1 for h in header() if "source md5" in h), 2)
    print("pdgcapture selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--write" in sys.argv:
        p, n = write()
        print("wrote %s  (%d rows)" % (p, n))
        sys.exit(0)
    if "--verify" in sys.argv:
        good, msg = verify()
        print(("ok   " if good else "XX   ") + msg)
        sys.exit(0 if good else 1)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    for h in header():
        print(h)
    print("rows: %d" % len(read()))
    sys.exit(0)
