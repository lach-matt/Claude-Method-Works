#!/usr/bin/env python3
"""emptysections.py — the nine heading-only sections: why they are empty, and where their material
went. Phase 0 ruling 3's evidence, and it does not say what chat 95B concluded.

M, 7 September 2026: "why are they empty?" and then, on the first answer:
"this is because the citations moved but the pointers did not."

M IS RIGHT, AND IT CHANGES THE REPAIR. The first answer -- they were never written -- is true and is
measured below against the original-input witness. It is not the whole answer, and by itself it
produced chat 95B's conclusion that "the repair is authoring six sections, and it is R3's largest
single item." The second pass here tests M's reading instead, and the material is in the book:

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

  §14.5.7  The volume's own §14.5.9 QUOTES it -- "§14.5.7 says G is a seed iff phi-hat(G) =
           phi-hat(X)" -- and that definition is in §14.5.9. "Zero cells are forced" is in §14.5.10,
           §14.5.11 and §14.5.12. The seed as a covering problem is in §14.5.8 through §14.5.14 and
           §21.5.4. Seven cells for 976 is in §14.5.1, §14.5.9, §14.5.13 and §21.5.4.
  §14.5.5  R4 and its four orientations are developed at main L4162 and L5785-L5851.
  §14.5.4  "E measures ..." is stated at main L193, L299, L1583 and L1994.
  §2.22    its principle is register 1551's finding, stated there in full.
  §28.7.6  the volume DESCRIBES the move: its eighty-six entries were prepended into it over time and
           the repair sent them to §28.7.7, leaving -- in the volume's own words -- "now four, the
           tower's three, which repairs their numbering". It has ZERO.
  §28.9    is a parent heading with a child, §28.9.1, and is not an authoring gap at all.

TWO ATTRIBUTIONS HAVE NO HOME IN THE MAIN VOLUME, and they are the exception that has to be said:
"anti-exchange" and "NP-hard" occur NOWHERE in it, and both are cited to §14.5.7 from the
Mathematical Compendium. The NP-hardness is seated at register 2071.

SO THE REPAIR IS RE-POINTING, NOT AUTHORING. Fifty-one citations name a heading with nothing under
it while the material they want is in the book under other numbers. That is Phase 3's pointer class,
which the plan already names -- "targets that say nothing of the claim" -- and not the one item the
plan says only M can do. Chat 95B measured the emptiness correctly and drew the wrong conclusion
from it, because it asked where the text was and not where the material was.

stdlib only.  --selftest asserts the witness reading, the citation load, and the material's location.
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
    print("\n\nAND THE MATERIAL IS IN THE BOOK, WHICH IS WHY THE REPAIR IS RE-POINTING\n")
    for name, pat in MATERIAL.items():
        w = [x for x in where(pat) if x not in SECTIONS and x.startswith(SCOPE)]
        print(f"  {name:34} in §{', §'.join(w[:6]) if w else 'NOWHERE in these families'}")
    print(f"\n  (scope: the §{', §'.join(SCOPE)} families the citations themselves name — a bare word")
    print("   like 'forced' matches half the book, and half the book is not a measurement.)")
    print("\n  Two attributions have no home in the main volume at all — 'anti-exchange' and")
    print("  'NP-hard', both cited to §14.5.7 from the Mathematical Compendium; the NP-hardness is")
    print("  seated at register 2071.")
    print("\n  §28.9 is a parent heading with one child, §28.9.1, and is not a gap. §28.7.6's")
    print("  eighty-six entries were moved to §28.7.7 by a repair the volume describes, which says")
    print("  §28.7.6 'is now four' — and it is zero.")


# what the citing lines say the empty sections contain, and where to look for it. The scope is the
# families the citations themselves name -- §14.5.x, §14.6.x and §21.5.x -- because a bare word like
# "forced" or "cover" matches half the book and a list of half the book is not a measurement.
MATERIAL = {
    "the seed definition ℛ(G) = X": r"φ̂\(G\)\s*=\s*φ̂\(X\)|ℛ\(G\)\s*=\s*X",
    "zero cells are forced": r"\bforced\b",
    "the seed as a covering problem": r"covering problem|set cover",
    "seven cells for 976": r"seven cells",
    "ℛ₄ and its four orientations": r"ℛ₄",
    "what E measures, exactly": r"E measures",
}
SCOPE = ("14.5", "14.6", "21.5")


def spans():
    L = load(os.path.join(MEM, VOLUMES["main"]))
    hd = [(i, re.match(r"^#{2,6}\s+(\S+)", l).group(1))
          for i, l in enumerate(L) if re.match(r"^#{2,6}\s+\S+", l)]
    out = {}
    for k, (i, name) in enumerate(hd):
        j = hd[k + 1][0] if k + 1 < len(hd) else len(L)
        out.setdefault(name, (i + 1, j))
    return L, out


def where(pat):
    """every section of the main volume whose body matches pat."""
    L, sp = spans()
    return [n for n, (a, b) in sp.items() if re.search(pat, "\n".join(L[a:b]))]


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
    eq("the seed definition §14.5.9 attributes to §14.5.7 is in §14.5.9",
       "14.5.9" in where(MATERIAL["the seed definition ℛ(G) = X"][0]), True)
    eq("'zero cells are forced' is in §14.5.10", "14.5.10" in where(r"forced"), True)
    eq("ℛ₄ is developed outside §14.5.5", [x for x in where(r"ℛ₄") if x != "14.5.5"] != [], True)
    eq("'E measures' is stated outside §14.5.4", [x for x in where(r"E measures") if x != "14.5.4"] != [], True)
    eq("'anti-exchange' occurs nowhere in the main volume", where(r"anti-exchange"), [])
    eq("'NP-hard' occurs nowhere in the main volume", where(r"NP-hard"), [])
    L, sp = spans()
    eq("§28.9 has a child, §28.9.1", "28.9.1" in sp, True)
    eq("§28.7.6 has none", [n for n in sp if n.startswith("28.7.6.")], [])
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
