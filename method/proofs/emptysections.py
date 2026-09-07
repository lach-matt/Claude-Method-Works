#!/usr/bin/env python3
"""emptysections.py — the nine heading-only sections: why they are empty, measured against the
original-input witness. Phase 0 ruling 3's evidence.

M, 7 September 2026: "why are they empty?"

THE ANSWER IS NOT PRODUCTION LOSS, AND IT IS ALREADY IN THE RECORD FOR SIX OF THE NINE.
`recovered/DEF-95B.md` (chat 95B) measured §14.5.2-§14.5.7 against the Prints & Proofs original
`The Method 1.6.md` -- 738,550 B, md5 49900cf41f818ab789bb90fc596ac977, the Ruling 56
ORIGINAL-INPUT WITNESS -- and found the six headings there with ZERO non-blank body lines:

  "§14.5.2-§14.5.7 are an AUTHORING GAP, not a production loss ... the text never existed at the
   input, so no print carries it. Do not re-derive this and do not search for an earlier print."

THIS EXTENDS THAT MEASUREMENT TO ALL NINE. Every one of §2.22, §14.5.2 through §14.5.7, §28.7.6 and
§28.9 is empty in the witness as well as in the live volume. Nothing was lost; nothing was ever
written. No build in the archive from BUILD9 to BUILD90 carries a body for any of them, and the
pressed PDF's contents put §14.5.2 through §14.5.6 all on one page, which is what consecutive empty
headings look like when they are typeset.

WHAT MAKES IT MATTER IS THE OTHER DIRECTION. The volumes cite these sections FIFTY-ONE times, and
the surrounding prose speaks of what they say: §14.5.8 opens "§14.5.7 measures the seed on scattered
shapes" and §14.5.9 opens "Everything §14.5.7 and §14.5.8 report about seed SIZES came from one
heuristic". §14.5.7 alone carries 23 citations, EIGHT OF THEM FROM THE REGISTER -- and Register
entries are append-only, so whoever writes that section writes it to what those eight already say,
not the other way round. That is chat 95B's order-of-work point and it still holds.

stdlib only.  --selftest asserts the witness reading and the citation load.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
METH = os.path.dirname(HERE)
MEM = os.path.join(METH, "members")
PP = os.path.join(METH, "PP_The_Method_1_6.md")
PP_MD5 = "49900cf41f818ab789bb90fc596ac977"
SECTIONS = ["2.22", "14.5.2", "14.5.3", "14.5.4", "14.5.5", "14.5.6", "14.5.7", "28.7.6", "28.9"]
VOLUMES = {"main": "The_Method_1_6-2.md", "reg": "The_Method_1_6___The_Register-2.md",
           "mc": "The_Method_1_6___Mathematical_Compendium-2.md",
           "pc": "The_Method_1_6___The_Physics_Compendium-2.md",
           "ioi": "The_Method_1_6___The_Index_of_Indices-2.md",
           "sc": "The_Method_1_6___Spectra_Compendium-2.md"}


def body(lines, sec):
    """(heading line, non-blank body lines before the next heading of any level)"""
    for i, l in enumerate(lines):
        if re.match(r"^#{2,6}\s+" + re.escape(sec) + r"\s", l):
            j, n = i + 1, 0
            while j < len(lines) and not re.match(r"^#{1,6}\s", lines[j]):
                if lines[j].strip():
                    n += 1
                j += 1
            return i + 1, n
    return None, None


def load(path):
    return open(path, encoding="utf-8", errors="replace").read().split("\n")


def citations():
    T = {k: load(os.path.join(MEM, v)) for k, v in VOLUMES.items()}
    out = {}
    for s in SECTIONS:
        rx = re.compile(r"§\s?" + re.escape(s) + r"(?![\d.])")
        per = {}
        for k, L in T.items():
            n = sum(1 for l in L if rx.search(l)
                    and not re.match(r"^#{1,6}\s+" + re.escape(s) + r"\s", l))
            if n:
                per[k] = n
        out[s] = per
    return out


def measure():
    pp, cur = load(PP), load(os.path.join(MEM, VOLUMES["main"]))
    cites = citations()
    rows = []
    for s in SECTIONS:
        a, b = body(pp, s); c, d = body(cur, s)
        rows.append(dict(sec=s, pp_line=a, pp_body=b, now_line=c, now_body=d,
                         cites=cites[s], total=sum(cites[s].values())))
    return rows


def report():
    rows = measure()
    print("The nine heading-only sections, against the original-input witness\n")
    print(f"  witness: PP_The_Method_1_6.md, md5 {PP_MD5} (Ruling 56)\n")
    print(f"  {'section':>9}{'witness L':>11}{'body':>6}{'live L':>9}{'body':>6}   citations")
    for r in rows:
        print(f"  {r['sec']:>9}{r['pp_line']:>11}{r['pp_body']:>6}{r['now_line']:>9}{r['now_body']:>6}"
              f"   {r['total']:>2}  {r['cites']}")
    tot = sum(r["total"] for r in rows)
    print(f"\n  EVERY ONE is empty in the witness as well as in the live volume. Nothing was lost;")
    print(f"  nothing was ever written. Chat 95B measured this for the six in §14.5 and said so:")
    print(f"  'an AUTHORING GAP, not a production loss ... the text never existed at the input.'")
    print(f"\n  And {tot} citations across the volumes resolve to a heading with nothing under it.")
    seven = [r for r in rows if r["sec"] == "14.5.7"][0]
    print(f"  §14.5.7 alone carries {seven['total']}, {seven['cites'].get('reg', 0)} of them from the Register — and Register")
    print("  entries are append-only, so that section must be written to what those entries")
    print("  already say, not the other way round.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    import hashlib
    eq("the witness is the Ruling 56 original input",
       hashlib.md5(open(PP, "rb").read()).hexdigest(), PP_MD5)
    rows = measure()
    eq("nine sections measured", len(rows), 9)
    eq("all nine are empty in the witness", [r["pp_body"] for r in rows], [0] * 9)
    eq("all nine are empty in the live volume", [r["now_body"] for r in rows], [0] * 9)
    eq("so not one of them was ever written",
       all(r["pp_body"] == 0 and r["now_body"] == 0 for r in rows), True)
    seven = [r for r in rows if r["sec"] == "14.5.7"][0]
    eq("§14.5.7 is the most-cited of the nine", seven["total"], 23)
    eq("and eight of its citations are the Register's", seven["cites"]["reg"], 8)
    eq("the nine carry 51 citations in all", sum(r["total"] for r in rows), 51)
    eq("every one of the nine is cited at least once",
       min(r["total"] for r in rows) >= 1, True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
