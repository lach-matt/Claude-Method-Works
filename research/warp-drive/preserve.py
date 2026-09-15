#!/usr/bin/env python3
r"""
preserve.py -- DID A WRITE DESTROY SOMETHING?  A census of every instrument in
this tree whose content was replaced wholesale, and whether the superseded
content is still cited by anything.

M: "The preservation of superseded material is vital to verification and restore
needs."

    python3 preserve.py             the reading
    python3 preserve.py --selftest  fixtures
    python3 preserve.py --check     exit 1 if an unrecorded replacement stands

===============================================================================
0. WHAT THIS EXISTS BECAUSE OF
===============================================================================

On 2026-09-14 the channel index was written to `spectra.py`.  That name was
taken: `spectra.py` had been "information as the SPECTRUM of a charge state, not
the charge" since `ffbaa15`, and the write destroyed it.  `obstruct.py` cites
that file, `index3.py` carries five findings attributed to it, and `rates.py`
and `compress.py` both reason from its result.

    NOTHING CAUGHT IT, AND `--selftest` STRUCTURALLY COULD NOT.  A new file and a
    clobbered file are indistinguishable to a file's own fixtures: the channel
    index's fixtures passed on the first run, correctly, because they test the
    channel index.  Git reported it as `275 insertions(+), 343 deletions(-)` in a
    statistic nobody reads aloud.  See DOCKET 14.

===============================================================================
1. WHAT A REPLACEMENT IS, AND WHY THE TEST IS TWO-PART
===============================================================================

A commit REPLACES a file when it both

    (a) deletes more lines than it adds, or deletes at least HALF the file, and
    (b) changes the file's SELF-IDENTIFICATION -- the `name.py -- ...` line that
        every instrument in this tree opens its docstring with.

    NEITHER HALF IS ENOUGH ALONE.  A big refactor satisfies (a) and is not a
    replacement; a retitled docstring satisfies (b) and is not one either.  The
    `spectra.py` write satisfies both: 343 deleted against 275 added, and the
    identification line went from "information as the SPECTRUM of a charge
    state" to "THE CHANNEL INDEX".

===============================================================================
2. THE SEVERITY IS WHETHER ANYTHING STILL POINTS AT THE OLD CONTENT
===============================================================================

A replacement is survivable when nothing depended on what was there.  It is a
fault when something did, and that is measurable without judgement: search the
tree for citations of the file's path, and check whether they were written
BEFORE the replacement.  A citation older than the replacement was written about
the old content.

    CITED        a pre-replacement citation exists.  This is the dangerous row.
    UNCITED      nothing points at it.
    RECORDED     the replacement is named in DOCKET.md, so it is a known one.

===============================================================================
3. NO SYNTACTIC TEST SEPARATES A CLOBBER FROM A RE-DERIVATION.  MEASURED.
===============================================================================

Clause (b) finds seven replacements in this tree and only one is a clobber.  The
others are RE-DERIVATIONS: the same subject rewritten under a new scope, a new
reading, or a correction.  The obvious discriminator is how much of the file's
public API survives -- a revision should keep its function names.  It does not
work, and the numbers are the reason it is not used:

        spectra.py    THE CLOBBER          jaccard over top-level defs  0.06
        currency.py   a re-derivation                                   0.08
        transit.py    a re-derivation                                   0.08
        stationkeep.py                                                  0.23
        questions.py                                                    0.30
        hexad.py                                                        0.55

    A RE-DERIVATION UNDER A NEW SCOPE REWRITES ITS API AS COMPLETELY AS A
    CLOBBER DOES.  `currency.py` at 0.08 is more API-disjoint than the clobber
    at 0.06.  Any threshold that admits currency admits spectra.  The
    discriminator is semantic -- does the new file still concern the same
    object -- and this file will not guess at it.

    SO THE CONTRACT IS DIFFERENT AND NARROWER.  The guard SURFACES every
    replacement, checks the superseded content is recoverable, names who cited
    it beforehand, and requires each to be ADJUDICATED -- written up in
    DOCKET.md's adjudication table under its own commit.  It classifies nothing
    on its own.  That is what would have caught `spectra.py` on the day: not a
    verdict, but a row demanding one.

===============================================================================
4. RETROSPECTIVE IS TOO LATE, SO THERE IS A PROSPECTIVE CHECK TOO
===============================================================================

`replacements()` reads committed history.  It would have caught `spectra.py` --
the day AFTER the clobber, with the diff already pushed.  That is late, and the
limitation surfaced through a fixture: this file asserted it could see itself in
`git ls-files`, and failed, because it was not yet committed.

    `pending()` IS THE SAME TEST AGAINST THE WORKING TREE.  For every tracked
    instrument it compares the identification line at HEAD with the one on disk,
    and measures the deletion the same way.  A clobber that has been written but
    not committed shows up there, which is the only moment it is still free to
    fix.

    IT CANNOT SEE A FILE THAT WAS NEVER COMMITTED, and does not need to: a file
    with no history has overwritten nothing.  What it cannot see either is a
    replacement that carefully preserves the identification line, which is the
    same blind spot clause (b) has and is stated in section 5.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

To claim git loses anything.  Every superseded byte is recoverable from the
object store, which is exactly how `spectra.py` was restored; the danger is not
loss but SILENT loss -- a citation pointing at content that no longer answers to
its name.  `recoverable()` checks the old blob still resolves, and it always
should.

To be a hook.  `CLAUDE.md` says this is a document corpus and not to add CI.
This is an instrument with a `--check` mode that a person or a later ruling can
wire up; it installs nothing.

To judge a refactor.  Clause (b) is what keeps an honest rewrite out of the
report, and it is a heuristic: a replacement that carefully preserves the
identification line will not be caught, and `--check` cannot see it.  That limit
is the reason DOCKET 14's candidate 1 -- a diff-size check at commit time -- is
listed separately from this file.
"""

import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# DOCKET 14's adjudication table rules each of the seven: one CLOBBER, one
# RESTORE, five RE-DERIVATIONS.  A guard that ruled automatically would have been
# wrong six times out of seven, which is the argument for the narrow contract.
HERE = "research/warp-drive"
IDENT = re.compile(r"^\s*([A-Za-z_][\w]*\.py)\s*--\s*(.+)$", re.M)


def _git(*args):
    return subprocess.run(("git",) + args, cwd=ROOT, capture_output=True,
                          text=True, check=False).stdout


def instruments():
    """Every .py this tree tracks, repo-relative."""
    out = _git("ls-files", HERE).split()
    return sorted(p for p in out if p.endswith(".py"))


def ident_of(text):
    """The file's self-identification line, or None.

    Every instrument here opens its docstring `name.py -- what it is`.  That
    line is the file's claim about what it is, and a replacement changes it.
    """
    m = IDENT.search(text[:4000])
    return m.group(2).strip() if m else None


def history(path):
    """[(sha, added, deleted)] oldest first, for one path."""
    raw = _git("log", "--follow", "--numstat", "--format=%H", "--", path)
    out, sha = [], None
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.fullmatch(r"[0-9a-f]{40}", line):
            sha = line
        elif sha:
            parts = line.split("\t")
            if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
                out.append((sha, int(parts[0]), int(parts[1])))
                sha = None
    return list(reversed(out))


def blob(sha, path):
    return _git("show", "%s:%s" % (sha, path))


def replacements():
    """[(path, sha, added, deleted, old ident, new ident)] over the tree."""
    out = []
    for path in instruments():
        h = history(path)
        for i, (sha, add, dele) in enumerate(h):
            if i == 0:
                continue                       # the file's own creation
            prev = h[i - 1][0]
            before, after = blob(prev, path), blob(sha, path)
            if not before or not after:
                continue
            bulk = dele > add or dele >= len(before.splitlines()) / 2
            if not bulk:
                continue
            ob, oa = ident_of(before), ident_of(after)
            if ob and oa and ob != oa:
                out.append((path, sha, add, dele, ob, oa))
    return out


def citations(path, sha):
    """[(citer, written before the replacement?)] -- who points at this path.

    A citation older than the replacement was written about the OLD content.
    """
    base = os.path.basename(path)
    hits = _git("grep", "-l", "-F", base, "HEAD", "--", HERE).splitlines()
    when = _git("show", "-s", "--format=%ct", sha).strip()
    out = []
    for h in hits:
        f = h.split(":", 1)[-1]
        if os.path.basename(f) == base:
            continue
        first = _git("log", "--diff-filter=A", "--format=%ct", "--", f).split()
        older = bool(first and when and int(first[-1]) < int(when))
        out.append((f, older))
    return sorted(out)


def pending():
    """[(path, added, deleted, HEAD ident, working ident)] -- uncommitted ones.

    The prospective half of the guard.  Same two clauses as `replacements()`,
    applied to the working tree against HEAD, so a clobber is visible while it
    is still free to fix.
    """
    out = []
    for path in instruments():
        head = _git("show", "HEAD:%s" % path)
        if not head:
            continue
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            continue
        work = open(full, encoding="utf-8").read()
        if work == head:
            continue
        stat = _git("diff", "--numstat", "HEAD", "--", path).split()
        if len(stat) < 2 or not stat[0].isdigit() or not stat[1].isdigit():
            continue
        add, dele = int(stat[0]), int(stat[1])
        if not (dele > add or dele >= len(head.splitlines()) / 2):
            continue
        hb, wb = ident_of(head), ident_of(work)
        if hb and wb and hb != wb:
            out.append((path, add, dele, hb, wb))
    return out


def recoverable(path, sha):
    """The superseded blob still resolves in the object store."""
    h = history(path)
    prev = next((h[i - 1][0] for i, r in enumerate(h) if r[0] == sha and i), None)
    return bool(prev and blob(prev, path).strip())


ADJ_ROW = re.compile(r"^\|\s*`([^`]+\.py)`\s*\|\s*`([0-9a-f]{7,40})`\s*\|", re.M)


def adjudicated():
    """{(basename, short sha)} read from DOCKET.md's adjudication table.

    A GREP FOR THE FILENAME IS NOT ADJUDICATION and this used to do that: any
    mention anywhere in DOCKET.md counted, so `hexad.py` and `questions.py`
    passed for being discussed elsewhere entirely.  A row must name the file AND
    the commit that replaced it.
    """
    d = os.path.join(ROOT, HERE, "DOCKET.md")
    if not os.path.exists(d):
        return set()
    return {(m.group(1), m.group(2)[:7])
            for m in ADJ_ROW.finditer(open(d, encoding="utf-8").read())}


def recorded(path, sha=None):
    """This replacement is adjudicated -- file and commit both named."""
    base = os.path.basename(path)
    adj = adjudicated()
    if sha is None:
        return any(b == base for b, _s in adj)
    return (base, sha[:7]) in adj


def census():
    """[(path, sha, severity, cited-before count, recoverable, recorded)]."""
    out = []
    for path, sha, _a, _d, _ob, _oa in replacements():
        cites = citations(path, sha)
        before = [c for c, older in cites if older]
        sev = "CITED" if before else "UNCITED"
        out.append((path, sha[:7], sev, len(before), recoverable(path, sha),
                    recorded(path, sha)))
    return out


def unrecorded():
    """The rows a --check fails on: any replacement not yet adjudicated.

    NOT just the cited ones.  A replacement nothing happens to cite today can be
    cited tomorrow, and the citation will point at content that no longer
    answers to its name.  Adjudication is cheap; the rule is every one.
    """
    return [r for r in census() if not r[5]]


# ---------------------------------------------------------------------------

def report():
    reps = replacements()
    print("=" * 74)
    print("DID A WRITE DESTROY SOMETHING?")
    print("=" * 74)
    print()
    print("1. THE TEST IS TWO-PART, AND NEITHER HALF IS ENOUGH ALONE.")
    print("   (a) deletes more than it adds, or at least half the file")
    print("   (b) changes the file's own `name.py -- ...` identification line")
    print("   %d instruments tracked, %d replacements found."
          % (len(instruments()), len(reps)))
    print()
    if not reps:
        print("   None. Either the tree is clean or clause (b) missed one --")
        print("   see section 3 of the docstring for why that is possible.")
    for path, sha, add, dele, ob, oa in reps:
        print("   %s  %s  +%d -%d" % (path, sha[:7], add, dele))
        print("      was: %s" % ob[:62])
        print("      now: %s" % oa[:62])
    print()

    print("2. SEVERITY -- whether anything still pointed at the old content.")
    print("   %-34s %-8s %-8s %-6s %s"
          % ("file", "verdict", "cited", "recov", "recorded"))
    for path, sha, sev, n, rec, rc in census():
        print("   %-34s %-8s %-8d %-6s %s"
              % (path, sev, n, "yes" if rec else "NO", "yes" if rc else "NO"))
    print()
    pend = pending()
    print("3. THE PROSPECTIVE HALF -- the working tree against HEAD.")
    if not pend:
        print("   nothing uncommitted looks like a replacement.")
    for path, add, dele, hb, wb in pend:
        print("   %s  +%d -%d" % (path, add, dele))
        print("      HEAD: %s" % hb[:60])
        print("      disk: %s" % wb[:60])
    print()
    bad = unrecorded()
    print("4. VERDICT: %s"
          % ("no unrecorded replacement stands" if not bad
             else "%d UNRECORDED REPLACEMENT(S)" % len(bad)))
    for r in bad:
        print("   %s -- cited by %d file(s) written before it, and not in"
              % (r[0], r[3]))
        print("   DOCKET.md. Restore it or write it up.")
    print()
    print("5. REFUSED: to claim git loses anything -- every superseded byte is")
    print("   recoverable, and the danger is SILENT loss, a citation pointing")
    print("   at content that no longer answers to its name. To be a hook: this")
    print("   installs nothing. To judge a refactor: clause (b) is what keeps an")
    print("   honest rewrite out, and a replacement that preserves the")
    print("   identification line will not be caught.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    inst = instruments()
    chk("the tree is tracked", len(inst) > 50, True)
    # ASSERTED ON A FILE THAT HAS ALWAYS BEEN TRACKED, not on this one.  The
    # fixture used to name preserve.py and failed on its first run, because a
    # file is invisible to `git ls-files` until it is committed.  That failure
    # is what section 4 exists for; the fixture itself was just bootstrapping.
    chk("a long-tracked instrument is visible", HERE + "/mi.py" in inst, True)
    chk("and so is hlaw, which everything imports",
        HERE + "/hlaw.py" in inst, True)
    # the identification parser, on real content
    chk("it reads this file's own identification",
        (ident_of(open(__file__, encoding="utf-8").read()) or "").startswith(
            "DID A WRITE DESTROY SOMETHING?"), True)
    chk("it returns None on text with no identification line",
        ident_of("just some prose\nwith no marker\n"), None)
    chk("it does not match a bare filename mention",
        ident_of("see spectra.py for the argument\n"), None)
    # the known case
    reps = replacements()
    paths = [r[0] for r in reps]
    chk("the spectra.py replacement is found",
        HERE + "/spectra.py" in paths, True)
    sp = next(r for r in reps if r[0] == HERE + "/spectra.py")
    chk("it deleted more than it added", sp[3] > sp[2], True)
    chk("and the identification changed", sp[4] != sp[5], True)
    chk("the old one is the spectrum-of-a-charge-state file",
        "SPECTRUM of a charge state" in sp[4], True)
    chk("the new one is the channel index", "CHANNEL INDEX" in sp[5], True)
    chk("the superseded content is recoverable",
        recoverable(sp[0], sp[1]), True)
    chk("it was cited before the replacement",
        len([c for c, older in citations(sp[0], sp[1]) if older]) > 0, True)
    chk("and it is recorded in DOCKET.md", recorded(sp[0]), True)
    cen = census()
    chk("the census covers every replacement", len(cen), len(reps))
    chk("every replacement is recoverable",
        [r[0] for r in cen if not r[4]], [])
    # THE SELFTEST TESTS THE INSTRUMENT; `--check` REPORTS THE TREE.  Asserting
    # here that the tree is clean was a conflation of the two: it made a fixture
    # fail for a true finding.  What belongs here is that the instrument reports
    # the state it is in, and the state itself is section 2 of the report and
    # the exit code of --check.
    chk("the instrument reports a definite state",
        all(r[2] in ("CITED", "UNCITED") for r in cen), True)
    chk("and it found the case it was written for",
        any(r[0].endswith("spectra.py") and r[2] == "CITED" for r in cen), True)
    chk("every replacement is adjudicated",
        sorted(os.path.basename(r[0]) for r in unrecorded()), [])
    chk("the adjudication table names seven", len(adjudicated()), 7)
    chk("a filename alone is not adjudication -- the sha must match",
        recorded("x/spectra.py", "0000000"), False)
    # the prospective half
    pend = pending()
    chk("no uncommitted replacement is pending",
        [os.path.basename(p) for p, *_r in pend], [])
    chk("pending() reads the working tree, not history",
        isinstance(pend, list), True)
    print("preserve selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--check" in sys.argv:
        bad = unrecorded()
        pend = pending()
        for r in bad:
            print("UNRECORDED REPLACEMENT: %s (%s), cited by %d" % (r[0], r[1], r[3]))
        for path, add, dele, hb, wb in pend:
            print("UNCOMMITTED REPLACEMENT: %s  +%d -%d" % (path, add, dele))
            print("    HEAD says: %s" % hb[:60])
            print("    disk says: %s" % wb[:60])
        print("preserve --check: %s" % ("clean" if not (bad or pend) else "FAIL"))
        sys.exit(1 if (bad or pend) else 0)
    sys.exit(report())
