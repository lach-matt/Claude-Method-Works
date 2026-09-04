#!/usr/bin/env python3
"""bridge_transpose.py — turn the staged prose registers 1371-1433 into the
canonical REGISTER-DATA.md form.

Mechanical on purpose. Retyping 63 entries by hand is exactly the transcription
fault the register keeps recording, so the transformation is a program that can
be re-run and diffed.

Canonical form required by register_gen.py's parser:  ^ {0,3}NNNN\. <text>
Audit 12 MARKUP requires an even count of ** in every blank-line-separated block.

Corrections applied here are ONLY those forced by an entry's own enumeration.
Every one is listed in FORCED and printed on each run. Substantive figures that
need recomputation are left exactly as written and reported separately.
"""
import re, sys, textwrap, pathlib

SRC = pathlib.Path("/home/claude/rp/.bridge")
FILES = ["RAW-1371-1380.md", "RAW-1381-1390.md", "RAW-1391-1400.md",
         "RAW-1401-1410.md", "RAW-1411-1420.md", "RAW-1421-1430.md",
         "RAW-DELTA-1427-1433.md"]

# ---- corrections forced by the entry's own text -----------------------------
# (register, find, replace, why)
FORCED = [
 (1381, "six elements at two mass numbers each",
        "six elements at more than one mass number — five pairs and californium at three",
        "XRAY-KL3 carries Cf 251, 249 and 250; five of the six are pairs, Cf is not"),
 (1393, "H = HO − 2κℏω₀[l·s − μ(l² − ⟨l²⟩_N)]",
        "H = HO − κℏω₀[2 l·s + μ(l² − ⟨l²⟩_N)]",
        "the bracket as first written yields β = +2κμℏω₀, contradicting the entry's "
        "own β = −κμℏω; the corrected bracket reproduces both stated coefficients"),
 (1404, "six pair up as consecutive elements",
        "eight pair up as four consecutive pairs (corrected in transposition: the "
        "count of six was carried from register 1400, which lists three pairs, and "
        "was not updated when the lawrencium–rutherfordium pair was added)",
        "1404 enumerates four pairs, which is eight elements, not six"),
 (1421, "February's thirtieth and thirty-first plus the four thirty-day months' thirty-firsts",
        "February's twenty-ninth, thirtieth and thirty-first plus the four thirty-day "
        "months' thirty-firsts",
        "372 − 365 = 7; the list as first written names six"),
 (1430, "The other five pairs are one sense per shell",
        "The other four pairs are one sense per shell",
        "six pairs less the two named in 82–126 leaves four, which is what the "
        "entry's own enumeration lists"),
]

def load():
    ent = {}
    for fn in FILES:
        txt = (SRC / fn).read_text(encoding="utf-8")
        for m in re.finditer(r"^\*\*(\d{4}) — (.*?)$", txt, re.M):
            n = int(m.group(1))
            start = m.start()
            nxt = re.search(r"^\*\*\d{4} — ", txt[m.end():], re.M)
            body = txt[start: m.end() + (nxt.start() if nxt else len(txt))].strip()
            # the delta file is terser; the chunked files win on 1427-1430
            if n in ent and fn.startswith("RAW-DELTA"):
                continue
            ent[n] = body
    return ent

def head_and_rest(body):
    m = re.match(r"^\*\*(\d{4}) — (.*?)\*\*\s*(.*)$", body, re.S)
    n, head, rest = int(m.group(1)), m.group(2), m.group(3)
    return n, head, rest

def canon(n, head, rest):
    # heads in 165-1370 are capitalised declarative sentences
    h = head.strip()
    if not h.endswith((".", "!", "?", ":")):
        h += "."
    h = h.upper()
    para = re.sub(r"\s*\n\s*", " ", rest).strip()
    para = re.sub(r"[ \t]{2,}", " ", para)
    text = f"{n}. **{h}** {para}"
    wrapped = textwrap.wrap(text, width=97, initial_indent=" ",
                            subsequent_indent=" ", break_long_words=False,
                            break_on_hyphens=False)
    return "\n".join(wrapped)

def main():
    ent = load()
    want = set(range(1371, 1434))
    have = set(ent)
    if have != want:
        print("MISSING:", sorted(want - have), " EXTRA:", sorted(have - want))
        sys.exit(1)
    print(f"loaded {len(ent)} entries, {min(ent)}-{max(ent)}")

    applied = []
    for n, find, repl, why in FORCED:
        if find in ent[n]:
            ent[n] = ent[n].replace(find, repl)
            applied.append((n, why))
        else:
            print(f"  !! forced correction for {n} did not match — NOT applied")
            sys.exit(1)
    print("forced corrections applied:")
    for n, why in applied:
        print(f"  {n}: {why}")

    out, bad = [], []
    for n in sorted(ent):
        num, head, rest = head_and_rest(ent[n])
        block = canon(num, head, rest)
        if block.count("**") % 2:
            bad.append(num)
        out.append(block)
    if bad:
        print("ODD ** COUNT (audit 12 would fail):", bad); sys.exit(1)
    print("markup parity: all 63 blocks even")

    body = "\n\n" + "\n\n".join(out) + "\n"
    p = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
    p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n" + body,
                 encoding="utf-8")
    print("appended to REGISTER-DATA.md")

if __name__ == "__main__":
    main()
