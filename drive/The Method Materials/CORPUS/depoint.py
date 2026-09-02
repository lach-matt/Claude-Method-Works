#!/usr/bin/env python3
"""depoint.py — Ruling 29: remove pointers to excised Register entries.

A pointer is an EXPLICIT number naming an entry that no longer has a heading in
the Register. A RANGE (registers a-b) names a span, not an entry, and is left
alone even when an excised number falls inside it.

Clause content is kept; only the pointer token and its connective are removed.
Prose coherence is swept later, in one pass, by author's ruling.

  python3 depoint.py           dry run, prints before/after
  python3 depoint.py --write   apply, after writing .prepoint backups
"""
import re, sys, json, collections

FILES = {
    "MAIN":     "The_Method_1_6-2.md",
    "REGISTER": "The_Method_1_6___The_Register-2.md",
    "MATH":     "The_Method_1_6___Mathematical_Compendium-2.md",
    "PHYS":     "The_Method_1_6___The_Physics_Compendium-2.md",
    "SPECTRA":  "The_Method_1_6___Spectra_Compendium-2.md",
    "IOI":      "The_Method_1_6___The_Index_of_Indices-2.md",
    "LOWDIN":   "THE-LOWDIN-SOLUTION-2.md",
    "TB":       "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md",
}
REG = FILES["REGISTER"]

NUMLIST = r'(?:\d{3,4}(?:\s*[\u2013-]\s*\d{3,4})?)(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[\u2013-]\s*\d{3,4})?)*'
RNG = re.compile(r'(?i)\b(registers?)\s+(' + NUMLIST + r')')
RR  = re.compile(r'\b(R)\s(' + NUMLIST + r')')
# connective immediately before a pointer phrase, removed with it
LEAD = re.compile(r'(?:\s+(?:at|in|of|see|from|by|per|and|since|as))?\s*$', re.I)


def live_numbers():
    txt = open(REG, encoding="utf-8").read()
    out = set()
    for h in re.findall(r"^### ([\d,\s]+?)\s*$", txt, re.M):
        for p in h.split(","):
            if p.strip().isdigit():
                out.add(int(p.strip()))
    return out


def tidy(s):
    s = s.replace("( )", "").replace("()", "")
    s = re.sub(r"\(\s*[,;]?\s*\)", "", s)
    s = re.sub(r"[,;]\s*\)", ")", s)
    s = re.sub(r"\(\s*[,;]\s*", "(", s)
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    s = re.sub(r"(?<!\.)\.\s*\.(?!\.)", ".", s)
    s = re.sub(r"([,;])\s*\1+", r"\1", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.rstrip() if s.strip() else s


def rebuild(word, parts, keep):
    """keep = list of part strings that survive; word is 'register(s)' or 'R'."""
    if not keep:
        return None
    if word.upper() == "R":
        head = "R "
    else:
        multi = len(keep) > 1 or any(("\u2013" in k or re.match(r'\d+\s*-\s*\d+$', k)) for k in keep)
        head = ("Registers " if word[0].isupper() else "registers ") if multi else \
               ("Register " if word[0].isupper() else "register ")
    if len(keep) == 1:
        body = keep[0]
    else:
        body = ", ".join(keep[:-1]) + " and " + keep[-1]
    return head + body


def process(line, dead, own):
    """Return (newline, n_pointers_removed)."""
    removed = 0
    for pat in (RNG, RR):
        while True:
            hit = None
            for m in pat.finditer(line):
                parts = [p.strip() for p in re.split(r'\s*(?:,|and|/|;)\s*', m.group(2))]
                singles = [p for p in parts if p.isdigit()]
                bad = [p for p in singles
                       if int(p) in dead and not (own and int(p) in own)]
                if bad:
                    hit = (m, parts, bad)
                    break
            if not hit:
                break
            m, parts, bad = hit
            keep = [p for p in parts if p not in bad]
            new = rebuild(m.group(1), parts, keep)
            if new is None:
                pre = line[:m.start()]
                cut = LEAD.search(pre)
                pre = pre[:cut.start()] if cut and cut.start() > 0 else pre
                line = tidy(pre + line[m.end():])
            else:
                line = line[:m.start()] + new + line[m.end():]
            removed += len(bad)
    return line, removed


def main(write=False):
    dead_seen = collections.Counter()
    total = 0
    samples = []
    for tag, fn in FILES.items():
        dead = None  # recomputed per file below
        break
    dead = None
    live = live_numbers()
    for tag, fn in FILES.items():
        lines = open(fn, encoding="utf-8").read().split("\n")
        own = None
        changed = 0
        for i, s in enumerate(lines):
            if tag == "REGISTER":
                m = re.match(r"^### ([\d,\s]+?)\s*$", s)
                if m:
                    own = {int(x.strip()) for x in m.group(1).split(",") if x.strip().isdigit()}
                    continue
            # dead = any cited number with no heading
            cited = set()
            for pat in (RNG, RR):
                for mm in pat.finditer(s):
                    for p in re.split(r'\s*(?:,|and|/|;)\s*', mm.group(2)):
                        if p.strip().isdigit():
                            cited.add(int(p.strip()))
            deadhere = {n for n in cited if n not in live}
            if not deadhere:
                continue
            new, n = process(s, deadhere, own if tag == "REGISTER" else None)
            if n:
                if len(samples) < 14:
                    samples.append((tag, i + 1, s.strip()[:0], s, new))
                for d in deadhere:
                    dead_seen[d] += 0
                lines[i] = new
                changed += n
                total += n
        if changed:
            print(f"{tag:<9} pointers removed: {changed}")
            if write:
                open(fn + ".prepoint", "w", encoding="utf-8").write(
                    open(fn, encoding="utf-8").read())
                open(fn, "w", encoding="utf-8").write("\n".join(lines))
    print("TOTAL POINTERS REMOVED:", total)
    if not write:
        print("\n--- sample before/after ---")
        for tag, ln, _, a, b in samples:
            print(f"\n[{tag}:{ln}]")
            print("  -", a.strip()[:190])
            print("  +", b.strip()[:190])
    return total


if __name__ == "__main__":
    main("--write" in sys.argv)

