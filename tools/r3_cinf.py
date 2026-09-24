#!/usr/bin/env python3
"""r3_cinf.py -- R3 class CINF, the c -> inf twin repair: register 1706's eleven, corrected by a new entry.

Executes docs/R3-CLASS-CINF.md on the author's approval of its wording. The finding (docs/LOWDIN-RECOVERED.md):
the eleven elements the Lowdin paper and register 1706 state as displaced at c -> inf were measured against a
table that had run at c = 137.035999 in restart mode (the project's own fault F59.3); the record's instrument,
recovered and run at both settings (lowdin/chain/), displaces Th, Rf and Z = 120 and nothing else.

The corpus's own mechanic, and nothing else: a Register entry is never edited -- the repair is a new appended
entry citing 1706, in the Register's own form, and the volume sites are repaired in place under a guarded
build with that entry (DEFERRED.md; the withdrawn-law class r3-wl.py is the precedent and this follows its
shape). Count-asserted substitutions on six members of the two live bundles, each anchored by content; a
reverse guard recovers every old member's md5 and both old bundles' md5 from the new bytes before anything is
written; the extent and count sites are driven to their fixed point; kinds.py recounts the Register's kinds
table on the new Register text; MANIFEST.tsv is regenerated as close.py regenerates it.

Usage:  python3 tools/r3_cinf.py                       dry run: everything in memory, nothing written under method/
        python3 tools/r3_cinf.py --entry N            the entry number to use (default 1793; see the note below)
        python3 tools/r3_cinf.py --write DIR          write the new members, both new bundles and a MEMBER-INDEX.tsv
                                                      under DIR (never under method/; refuses to overwrite)
        python3 tools/r3_cinf.py --w PATH             with --write: append PATH's W-entry text to WORKING-REGISTER.md
                                                      the way close.py does (must begin '### W-' and end '\\n\\n')

The entry number.  R3-CLASS-WL.md (seated, HELD under RUL-128) drafts entries 1793-1794 for the withdrawn-law
class.  Numbers are assigned at application, so this class takes the first free number when it is applied:
1793 if it goes first, 1795 if the withdrawn-law class goes first.  The instrument asserts that the number
it is given has no entry in the Register as seated and no EXCISED marker in the live bundle.

Nothing here decides the wording: the candidate texts below are the ones docs/R3-CLASS-CINF.md puts to the
author, and M's wording governs (edit here and in the spec together).  Seating the written tree into method/
is the close's business -- MEMBER-INDEX.tsv is emitted for it, and method/verify.py must pass on the result.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METHOD = os.path.join(REPO, "method")
MEM = os.path.join(METHOD, "members")
MAIN_BUNDLE = os.path.join(METHOD, "The_Method_1_6_BUILD90_main_and_register.md")
COMP_BUNDLE = os.path.join(METHOD, "The_Method_1_6_BUILD180_compendia_papers_audits.md")
MAIN_MD5 = "49065309b0c4fe8e055f693aed295cca"
COMP_MD5 = "ea5becc40e13debe4faaf6c7e0cde960"
NEW_MAIN_NAME = "The_Method_1_6_BUILD91_main_and_register.md"
NEW_COMP_NAME = "The_Method_1_6_BUILD181_compendia_papers_audits.md"

MAIN = "The_Method_1_6-2.md"
REG = "The_Method_1_6___The_Register-2.md"
PAPER = "THE-LOWDIN-SOLUTION-2.md"
MC = "The_Method_1_6___Mathematical_Compendium-2.md"
PC = "The_Method_1_6___The_Physics_Compendium-2.md"
IOI = "The_Method_1_6___The_Index_of_Indices-2.md"
WR = "WORKING-REGISTER.md"
MEMBER = re.compile(rb"^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n", re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()

# the record: what the recovered instrument measured (lowdin/chain/, docs/LOWDIN-RECOVERED.md)
ELEVEN = "Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf"
DISPLACED = "Th (6d → 5f, away from the observed 6d), Rf (5f → 6d, the observed channel) and Z = 120 (8s → 7d, unwitnessed)"


def read(name):
    with open(os.path.join(MEM, name), "rb") as fh:
        return fh.read()


def S(L, n, must):
    l = L[n - 1]
    assert must in l, "L%d does not carry %r: %r" % (n, must, l[:90])
    return l


def col(l, old, new):
    assert l.count(old) == 1, (old, l[:80])
    return l.replace(old, new)


def apply(text, subs):
    t = text
    for name, a, b in subs:
        assert t.count(a) == 1, "%s: anchor occurs %d times" % (name, t.count(a))
        assert a != b, name
        t = t.replace(a, b)
    return t


def reverse(text, subs):
    t = text
    for name, a, b in reversed(subs):
        assert t.count(b) == 1, "%s: reverse anchor occurs %d times" % (name, t.count(b))
        t = t.replace(b, a)
    return t


def texts(entry):
    """Every substitution, anchored by content on the seated members; the drafts M approves or edits."""
    N = str(entry)
    m = read(MAIN).decode("utf-8"); ML = m.split("\n")
    r = read(REG).decode("utf-8"); RL = r.split("\n")
    p = read(PAPER).decode("utf-8"); PL = p.split("\n")
    c = read(MC).decode("utf-8"); CL = c.split("\n")
    q = read(PC).decode("utf-8"); QL = q.split("\n")
    i = read(IOI).decode("utf-8"); IL = i.split("\n")
    out = {}

    # ---------------------------------------------------------------- the main volume, three sites + the extent line
    l9772 = S(ML, 9772, "**And the table is relativistic, visibly.** The identical walk at c → ∞ misplaces")
    l9773 = S(ML, 9773, "eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf. Silver and mercury")
    l9774 = S(ML, 9774, "are misfiled by the non-relativistic equation. *The wall chart is not a solution")
    l9775 = S(ML, 9775, "of the Schrödinger equation without light in it.*")
    l9866 = S(ML, 9866, "| **the relativistic table** | the c → ∞ twin walk, eleven elements apart |")
    l10805 = S(ML, 10805, "LS.twin the twin operator, c → ∞")
    l7373 = S(ML, 7373, "1,635 entries, 1 to 1792, at this build (2026-08-29)")
    n_entries = 1635 + (entry - 1792)
    n_mature = 1470 + (entry - 1792)
    out[MAIN] = [
        ("§35 L9772-L9775, the relativistic paragraph", "\n".join([l9772, l9773, l9774, l9775]) + "\n",
         "**And the table is relativistic at thorium.** The identical walk at c → ∞ moves\n"
         "its entrant at Th (6d to 5f, away from nature), at Rf (5f to 6d, the observed\n"
         "channel) and at Z = 120 (8s to 7d), and nowhere else. The eleven this chapter\n"
         "first printed — " + ELEVEN + " — were the chain measured\n"
         "against a table that had run at c = 137.035999 with every step restarted from\n"
         "the observed configuration, and are withdrawn (register " + N + "). *The actinide\n"
         "opening of the wall chart is not a solution of the Schrödinger equation without\n"
         "light in it; the rest of the chart is indifferent to it.*\n"),
        ("§35.5 L9866, the table row", l9866 + "\n",
         "| **the relativistic table** | the c → ∞ twin walk, three rows apart — Th, Rf, Z = 120 (register " + N + ") |\n"),
        ("Appendix L10805, the LS.twin status", l10805 + "\n",
         col(l10805, "measured · exhaustive · none found", "re-measured at c → ∞: Th, Rf, Z = 120 (" + N + ")") + "\n"),
        ("extent L7373", l7373 + "\n",
         col(l7373, "1,635 entries, 1 to 1792, at this build (2026-08-29)",
             "%s entries, 1 to %s, at this build (2026-09-24)" % ("{:,}".format(n_entries), N)) + "\n"),
    ]

    # ---------------------------------------------------------------- the Register: the extent lines, and the entry appended
    l6 = S(RL, 6, "**1635 entries, 1 to 1792.**")
    l65 = S(RL, 65, "**1635 entries, 1 to 1792** (genesis 1–94, superseded 95–164, mature record 165–1792)")
    out[REG] = [
        ("Register L6", l6 + "\n",
         col(col(l6, "**1635 entries, 1 to 1792.**", "**%d entries, 1 to %s.**" % (n_entries, N)),
             "and 165 to 1791, 1,470 entries, are the mature record",
             "and 165 to %s, %s entries, are the mature record" % (N, "{:,}".format(n_mature))) + "\n"),
        ("Register L65", l65 + "\n",
         col(l65, "**1635 entries, 1 to 1792** (genesis 1–94, superseded 95–164, mature record 165–1792)",
             "**%d entries, 1 to %s** (genesis 1–94, superseded 95–164, mature record 165–%s)" % (n_entries, N, N)) + "\n"),
    ]
    ENTRY = ("### " + N + "\n\n"
             "**REGISTER 1706'S ELEVEN WERE MEASURED AGAINST THE TABLE THE PROJECT HAD ALREADY VOIDED; AT A GENUINE "
             "c → ∞ THE WALK'S ENTRANT MOVES AT THORIUM, RUTHERFORDIUM AND Z = 120, AND NOWHERE ELSE.** *Entry 1706 "
             "states that the identical walk at c → ∞ (Λ_cinf, 107 rows) disagrees with Λ_chain at " + ELEVEN + ", every "
             "one an error of the equation-without-light against nature. The instrument that walked Λ_chain, recovered "
             "whole from the project's own conversations and run again, reproduces every sealed step it printed; the "
             "table 1706 compared against reproduces too, and it is the one the project's own fault record (F59.3) had "
             "voided six sessions before the paper was written: its driver bound c where the field never reads it, so "
             "it walked at c = 137.035999 in restart mode, each step from the observed configuration. The eleven are "
             "therefore the chain's memory against a memoryless restart at one and the same c, and at eight of them — "
             "Mn, Zn, Ag, Cd, Lu, Hg, Lr, Rf — it is the restart's entrant that nature holds and the chain's that "
             "departs. The walk re-run with the constant removed, by the project's own remedy for that fault, differs "
             "from the walk at c = 137.035999 at " + DISPLACED + " — and at no other row; silver and mercury do not "
             "move. The project's own scorer returns 96 of 107 steps at either setting, the step failures swapping "
             "Rf for Th, and 73 and 76 of 107 configurations. What 1706 stated survives at one witnessed element: the "
             "table is relativistic at thorium, where the equation without light files the entrant under 5f and nature "
             "has 6d; at rutherfordium it is the relativistic chain that departs from nature, and every other measured "
             "row is indifferent to c. The quarantine standing is kept and its object renamed: the sealed Λ_cinf is a "
             "restart walk at c = 137.035999 — contrast, never data — and the c → ∞ walk is the re-run. Corrected at "
             "the paper's abstract, relativistic clause, §VIII and Figure 5's caption, at §35's three sites, and at the "
             "twin entries of the Mathematical Compendium, the Physics Compendium and the Index of Indices; Figure 5 as "
             "printed drew the withdrawn comparison and stands captioned as such until it is redrawn from the re-run. "
             "Entry 1706 stands as written.* Registers 1701; 1703; 1706; 1712. (a correction.)\n")
    out["ENTRY"] = ENTRY
    assert r.endswith("(a correction.)\n") and not r.endswith("\n\n"), "Register tail form changed"
    assert not re.search(r"^### %s\b" % N, r, re.M), "entry %s already exists in the Register" % N

    # ---------------------------------------------------------------- the paper, four sites
    l13 = S(PL, 13, "and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them.")
    l45 = S(PL, 45, "*(Relativistic clause.) The law is scalar-relativistic in an essential way")
    l156 = S(PL, 156, "They disagree at eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, and Rf.")
    l160 = S(PL, 160, "***Figure 5.** The relativistic table against its c → ∞ counterfactual, element by element. Eleven disagreements, every one an error against nature.*")
    out[PAPER] = [
        ("abstract L13", l13 + "\n",
         col(l13, "and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them.",
             "and shows where the observed table is relativistic: with the speed of light taken to infinity, the same construction moves its entrant at thorium, away from nature, at rutherfordium, toward it, and at Z = 120, and nowhere else.") + "\n"),
        ("relativistic clause L45", l45 + "\n",
         "*(Relativistic clause.) The law is scalar-relativistic at one measured row: repeating the entire construction with c → ∞ inverts the channel competition at thorium and the entrant with it, moves the entrant at rutherfordium to the observed channel, and moves the first unwitnessed entrant at Z = 120; at every other row the entrant is the same at both settings.*\n"),
        ("§VIII L156", l156 + "\n",
         "The second boundary statement is the deeper one, and it is corrected here. The construction was repeated with the speed of light sent to infinity — the same equation, the same algorithm, the one admitted constant removed. The table first compared against Λ_chain had not been that: the project's own audit found, before this paper was written, that its driver set c where the field never reads it, so it had walked at c = 137.035999 with each step restarted from the observed configuration, and the eleven disagreements this paper first printed (" + ELEVEN + ") measured the chain's memory against a memoryless restart at one and the same c — at eight of them it was the restart, not the chain, that held nature's channel. Re-run with the constant removed by the project's own remedy, the same construction differs from its relativistic twin at three rows and no other: thorium, where the entrant moves from 6d to 5f and the equation without light departs from nature; rutherfordium, where it moves from 5f to the observed 6d and it is the relativistic chain that departs; and Z = 120, unwitnessed, where 8s gives way to 7d. Silver and mercury do not move; the project's scorer returns 96 of 107 steps at either setting. The relativistic clause therefore rests on thorium: the actinide opening of the periodic table hanging on the classroom wall is not a solution of the non-relativistic Schrödinger equation, and the rest of the chart is, to the reach of this construction, indifferent to the speed of light. Figure 5 as printed drew the withdrawn comparison and is captioned as such.\n"),
        ("Figure 5 caption L160", l160 + "\n",
         "***Figure 5.** The relativistic table against the table the project sealed as its c → ∞ counterfactual, element by element — withdrawn: the second table ran at c = 137.035999 in restart mode, so its eleven disagreements are the chain against a restart at one c, not against the constant. At a genuine c → ∞ the disagreements are thorium, rutherfordium and Z = 120.*\n"),
    ]

    # ---------------------------------------------------------------- the Mathematical Compendium, one site
    l3216 = S(CL, 3216, "**The identical entrant operator with the constant removed disagrees with the c = 137.035999 operator at eleven elements")
    out[MC] = [
        ("MC L3216, the twin operator", l3216 + "\n",
         "**The identical entrant operator with the constant removed disagrees with the c = 137.035999 operator at " + DISPLACED + ", and nowhere else; the eleven first printed here (" + ELEVEN + ") were the c = 137.035999 operator against a restart walk at the same c, and are withdrawn (register " + N + ")**\n"),
    ]

    # ---------------------------------------------------------------- the Physics Compendium, four sites
    q227 = S(QL, 227, "**What it indexes.** The identical walk with the one constant removed. 107 rows.")
    q235 = S(QL, 235, "**Must be measured.** Nothing; it is compared, not scored: **eleven entrants")
    q236 = S(QL, 236, "differ from Λ_chain** (Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf), and every")
    q237 = S(QL, 237, "difference is an error against nature, since the relativistic walk scores 107/107")
    q238 = S(QL, 238, "(register 1706).")
    q240 = S(QL, 240, "**What physics does.** It states that the observed periodic table is not a")
    q241 = S(QL, 241, "solution of the non-relativistic equation. **What it does NOT do:** serve as a")
    q603 = S(QL, 603, "the twin index Λ_cinf disagrees with Λ_chain at eleven elements, each an error against nature (register 1706)")
    out[PC] = [
        ("PC L227, what Λ_cinf indexes", q227 + "\n",
         "**What it indexes.** The identical walk with the one constant removed, 119 rows.\n"
         "The 107-row table first sealed under this name had run at c = 137.035999 with\n"
         "every step restarted from the observed configuration, and is withdrawn\n"
         "(register " + N + ").\n"),
        ("PC L235-L238, must be measured", "\n".join([q235, q236, q237, q238]) + "\n",
         "**Must be measured.** Nothing; it is compared, not scored: **three entrants\n"
         "differ from Λ_chain** — Th (6d → 5f, against nature), Rf (5f → 6d, the observed\n"
         "channel) and Z = 120 (8s → 7d) — and no other; register 1706's eleven were\n"
         "measured against the withdrawn table (register " + N + ").\n"),
        ("PC L240-L241, what physics does", q240 + "\n" + q241 + "\n",
         "**What physics does.** It states that the actinide opening of the observed\n"
         "periodic table is not a solution of the non-relativistic equation, and that\n"
         "the rest of the table is indifferent to c. **What it does NOT do:** serve as a\n"),
        ("PC L603, where c fails", q603 + "\n",
         col(q603, "the twin index Λ_cinf disagrees with Λ_chain at eleven elements, each an error against nature (register 1706)",
             "the twin index Λ_cinf disagrees with Λ_chain at thorium, against nature, at rutherfordium, toward it, and at Z = 120, and nowhere else (register " + N + ")") + "\n"),
    ]

    # ---------------------------------------------------------------- the Index of Indices, three sites
    i1882 = S(IL, 1882, "| **Λ_cinf** | that the periodic table is not a solution of the non-relativistic equation |")
    i1933 = S(IL, 1933, "**What it holds.** The identical 107-row walk at c → ∞.")
    i1939 = S(IL, 1939, "**Role for Λ.** None as data, everything as contrast: **eleven of its entrants")
    i1940 = S(IL, 1940, "differ from Λ_chain's, and all eleven are wrong against nature.** It exists to")
    i1941 = S(IL, 1941, "state that Λ's subject is relativistic, and it is quarantined from every other")
    i1942 = S(IL, 1942, "use (register 1706).")
    out[IOI] = [
        ("IoI L1882, the table row", i1882 + "\n",
         "| **Λ_cinf** | that the periodic table's actinide opening is not a solution of the non-relativistic equation, and the rest of it is indifferent to c |\n"),
        ("IoI L1933, what it holds", i1933 + "\n",
         "**What it holds.** The identical walk at c → ∞, 119 rows; the 107-row table first\n"
         "held here had run at c = 137.035999 in restart mode and is withdrawn (register " + N + ").\n"),
        ("IoI L1939-L1942, role for Λ", "\n".join([i1939, i1940, i1941, i1942]) + "\n",
         "**Role for Λ.** None as data, everything as contrast: **three of its entrants\n"
         "differ from Λ_chain's — thorium, wrong against nature; rutherfordium, the observed\n"
         "channel; Z = 120, unwitnessed.** It exists to state where Λ's subject is\n"
         "relativistic, and it is quarantined from every other use (register " + N + ").\n"),
    ]
    return out


def manifest_text(main_members, comp_members):
    """close.py's manifest, byte for byte in form."""
    rows = ["bundle\tname\tbytes\tmd5\tlines"]
    for tag, ms in (("main", main_members), ("compendia", comp_members)):
        for n, b in sorted(ms):
            if n == "MANIFEST.tsv":
                continue
            rows.append("%s\t%s\t%d\t%s\t%d" % (tag, n, len(b), md5(b), b.count(b"\n")))
    return ("\n".join(rows) + "\n").encode("utf-8")


def block(n, b):
    return b"<<<FILE: " + n.encode() + b">>>\n" + b + b"<<<END FILE: " + n.encode() + b">>>\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--entry", type=int, default=1793, help="the Register number the new entry takes (default 1793)")
    ap.add_argument("--write", metavar="DIR", help="write the new members and bundles under DIR (never method/)")
    ap.add_argument("--w", metavar="PATH", help="with --write: the W-entry text to append to WORKING-REGISTER.md")
    a = ap.parse_args(argv)
    N = a.entry

    old_main_b = open(MAIN_BUNDLE, "rb").read(); old_comp_b = open(COMP_BUNDLE, "rb").read()
    assert md5(old_main_b) == MAIN_MD5, "BUILD90 bundle md5 mismatch"
    assert md5(old_comp_b) == COMP_MD5, "BUILD180 bundle md5 mismatch"
    main_ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(old_main_b)]
    comp_ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(old_comp_b)]
    assert sorted(n for n, _ in main_ms) == sorted([MAIN, REG])
    dm, dc = dict(main_ms), dict(comp_ms)
    for n in (MAIN, REG):
        assert dm[n] == read(n), n + ": member differs from its bundle body"
    for n in (PAPER, MC, PC, IOI, WR):
        assert dc[n] == read(n), n + ": member differs from its bundle body"
    excised = re.findall(rb"EXCISED ([\d, ]+?)\s*:", old_main_b + old_comp_b)
    assert not any(str(N) in [x.strip() for x in e.decode().split(",")] for e in excised), "entry %d carries an EXCISED marker in a live bundle" % N
    wr = read(WR).decode("utf-8")
    assert not re.search(r"^### %d\b" % N, wr, re.M), "entry %d is seated in WORKING-REGISTER.md" % N
    reserved = "1793" in read("R3-CLASS-WL.md").decode("utf-8") and N in (1793, 1794)
    print("entry number %d%s" % (N, "  (NOTE: R3-CLASS-WL.md drafts 1793-1794 for the withdrawn-law class; whichever class applies first takes the number)" if reserved else ""))

    subs = texts(N)
    new = {}
    for name in (MAIN, REG, PAPER, MC, PC, IOI):
        old = read(name).decode("utf-8")
        t = apply(old, subs[name])
        if name == REG:
            t = t + "\n" + subs["ENTRY"]
            back = t[:-len("\n" + subs["ENTRY"])]
            assert md5(reverse(back, subs[name]).encode("utf-8")) == md5(read(name)), name + ": reverse FAILED"
        else:
            assert md5(reverse(t, subs[name]).encode("utf-8")) == md5(read(name)), name + ": reverse FAILED"
        new[name] = t
        print("%-46s %2d substitution(s)%s; reverse recovers the old md5 %s" % (name, len(subs[name]), " + the entry" if name == REG else "", md5(read(name))))

    # kinds.py recounts the Register's kinds table on the new text (as r3-wl.py does); only table lines may move
    with tempfile.TemporaryDirectory(prefix="r3cinf-") as td:
        rp = os.path.join(td, REG)
        open(rp, "w", encoding="utf-8").write(new[REG])
        pr = subprocess.run([sys.executable, os.path.join(MEM, "kinds.py"), rp, "--write"], capture_output=True, text=True, timeout=300)
        print("kinds.py --write:", (pr.stdout.strip() or pr.stderr.strip())[-300:])
        assert pr.returncode == 0, "kinds.py failed"
        final_r = open(rp, encoding="utf-8").read()
    NR, FL = new[REG].split("\n"), final_r.split("\n")
    assert len(FL) == len(NR), "kinds.py changed the line count"
    kdiff = [k + 1 for k in range(len(NR)) if FL[k] != NR[k]]
    for k in kdiff:
        print("   kinds L%d: %r -> %r" % (k, NR[k - 1][:70], FL[k - 1][:70]))
    assert all(re.match(r"\| \*\*", NR[k - 1]) or "entry headings" in NR[k - 1] for k in kdiff), "kinds.py touched a line outside its table"
    new[REG] = final_r

    # fixed-point checks over the six volumes
    vols = {MAIN: new[MAIN], REG: new[REG], MC: new[MC], PC: new[PC], IOI: new[IOI],
            "The_Method_1_6___Spectra_Compendium-2.md": read("The_Method_1_6___Spectra_Compendium-2.md").decode("utf-8")}
    ne = str(1635 + N - 1792)
    for pat in (r"1 to 1792\b", r"1 to %d\b" % N, r"\b1,?635 entries\b", r"\b%s,?%s entries\b" % (ne[:-3], ne[-3:]),
                r"eleven elements apart", r"Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf", r"register %d\b" % N):
        hits = {v.split("___")[-1].replace(MAIN, "main"): [k + 1 for k, l in enumerate(t.split("\n")) if re.search(pat, l)] for v, t in vols.items()}
        print("  %-48r %s" % (pat, " ".join("%s:%d" % (v, n) for v, ns in hits.items() for n in ns) or "0 sites"))
    hits_paper = [k + 1 for k, l in enumerate(new[PAPER].split("\n")) if "eleven" in l]
    print("  the paper's remaining 'eleven' lines: %s" % (hits_paper or "none"))

    # the bundles: replace the member bodies, regenerate MANIFEST.tsv, reverse-guard both
    nb = {n: t.encode("utf-8") for n, t in new.items()}
    new_main_b = old_main_b
    for n in (MAIN, REG):
        assert new_main_b.count(block(n, dm[n])) == 1
        new_main_b = new_main_b.replace(block(n, dm[n]), block(n, nb[n]))
    new_comp_b = old_comp_b
    if a.write and a.w:
        W = open(a.w, "rb").read()
        assert W.startswith(b"### W-") and W.endswith(b"\n\n"), "W text must begin '### W-' and end with a blank line"
        e = block(WR, dc[WR]); assert new_comp_b.count(e) == 1
        assert dc[WR].endswith(b"\n\n"), "WR body must end with a blank line"
        nb[WR] = dc[WR] + W
        new_comp_b = new_comp_b.replace(e, block(WR, nb[WR]))
    for n in (PAPER, MC, PC, IOI):
        assert new_comp_b.count(block(n, dc[n])) == 1
        new_comp_b = new_comp_b.replace(block(n, dc[n]), block(n, nb[n]))
    main_new_ms = [(n, nb.get(n, b)) for n, b in main_ms]
    comp_new_ms = [(n, nb.get(n, b)) for n, b in comp_ms]
    man = manifest_text(main_new_ms, comp_new_ms)
    assert manifest_text(main_ms, comp_ms) == dc["MANIFEST.tsv"], "the seated MANIFEST.tsv is not close.py's over the seated members"
    assert new_comp_b.count(block("MANIFEST.tsv", dc["MANIFEST.tsv"])) == 1
    new_comp_b = new_comp_b.replace(block("MANIFEST.tsv", dc["MANIFEST.tsv"]), block("MANIFEST.tsv", man))
    nb["MANIFEST.tsv"] = man
    # reverse guards
    rev = new_main_b
    for n in (MAIN, REG):
        assert rev.count(block(n, nb[n])) == 1; rev = rev.replace(block(n, nb[n]), block(n, dm[n]))
    assert md5(rev) == MAIN_MD5, "main bundle reverse FAILED"
    rev = new_comp_b
    for n in [x for x in (PAPER, MC, PC, IOI, "MANIFEST.tsv", WR) if x in nb]:
        assert rev.count(block(n, nb[n])) == 1; rev = rev.replace(block(n, nb[n]), block(n, dc[n]))
    assert md5(rev) == COMP_MD5, "compendia bundle reverse FAILED"
    print("main bundle reverse recovers md5 %s == BUILD90: True" % MAIN_MD5)
    print("compendia bundle reverse recovers md5 %s == BUILD180: True" % COMP_MD5)
    for n in sorted(nb):
        print("new %-46s %9s B  md5 %s  %6s lines" % (n, "{:,}".format(len(nb[n])), md5(nb[n]), "{:,}".format(nb[n].count(b"\n"))))
    print("new bundle %s  %s B  md5 %s  %s lines  %d members" % (NEW_MAIN_NAME, "{:,}".format(len(new_main_b)), md5(new_main_b), "{:,}".format(new_main_b.count(b"\n")), len(main_ms)))
    print("new bundle %s  %s B  md5 %s  %s lines  %d members" % (NEW_COMP_NAME, "{:,}".format(len(new_comp_b)), md5(new_comp_b), "{:,}".format(new_comp_b.count(b"\n")), len(comp_ms)))

    if not a.write:
        print("DRY RUN -- nothing written; BUILD90 and BUILD180 stay live")
        return 0
    out = os.path.abspath(a.write)
    assert not out.startswith(METHOD + os.sep) and out != METHOD, "refusing to write under method/"
    assert not os.path.exists(out), "%s exists -- never overwrite" % out
    os.makedirs(os.path.join(out, "members"))
    for n, b in nb.items():
        open(os.path.join(out, "members", n), "wb").write(b)
    open(os.path.join(out, NEW_MAIN_NAME), "wb").write(new_main_b)
    open(os.path.join(out, NEW_COMP_NAME), "wb").write(new_comp_b)
    # MEMBER-INDEX.tsv for the written tree: every member's bundle, size, md5 and byte offset, as method/'s
    rows = ["member\tbundle\text\tbytes\tmd5\tbundle_offset"]
    for tag, bundle, ms in (("BUILD91_main", new_main_b, main_new_ms), ("BUILD181_compendia", new_comp_b, comp_new_ms)):
        for n, b in ms:
            body = nb.get(n, b)
            head = b"<<<FILE: " + n.encode() + b">>>\n"
            off = bundle.index(head + body) + len(head)
            rows.append("%s\t%s\t%s\t%d\t%s\t%d" % (n, tag, os.path.splitext(n)[1], len(body), md5(body), off))
    body_rows = sorted(rows[1:], key=lambda r: r.split("\t")[0])
    open(os.path.join(out, "MEMBER-INDEX.tsv"), "w", encoding="utf-8").write("\n".join([rows[0]] + body_rows) + "\n")
    print("written", out, "-- the changed members, both new bundles and MEMBER-INDEX.tsv for the new tree; seating them into method/ is the close's")
    return 0


if __name__ == "__main__":
    sys.exit(main())
