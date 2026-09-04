#!/usr/bin/env python3
"""register_gen.py -- the register as its own compendium.

Chapter 28 is 226,588 characters, a quarter of the book, and 468 entries. By the
criterion that the book holds main points, unidentified elements and
unprecedented formulations, the register is none of those — it is the RECORD.

But it is also what makes every claim checkable, so it does not vanish: it moves
to REGISTER.md, generated from the source, and the book keeps only the entries a
chapter actually cites.

Rebuild:  python3 register_gen.py > REGISTER.md
"""
import re, sys, datetime
# Chapter 28 was THINNED in the reconstruction, so reading it regenerated the
# compendium from the reduced set and lost 215 entries. The full record now
# lives in REGISTER-DATA.md, which chapter 28 is a selection FROM rather than
# a source for (register 654).
S=open("The Method 1.6.md",encoding="utf-8").read()
RS=S.rindex("## 28. Withdrawals"); RE_=S.rindex("## 29.")
# the archive holds everything ever written; chapter 28 holds the selection PLUS
# any entry written since the archive was cut. The compendium is their union, so
# a new entry cannot be lost by living only in the book (register 657).
_ARC=open("REGISTER-DATA.md",encoding="utf-8").read()
_CH=S[RS:RE_]
# Register 1244: this pattern was \d{3} exactly, so every entry from 1000 onward
# — four digits — was silently dropped. 243 entries, a quarter of the record,
# absent from the compendium since entry 1000 was written.
_P=re.compile(r"^ {0,3}((?:\d{3,4}, )*\d{3,4})\. ",re.M)
def _ents(t):
    ms=list(_P.finditer(t)); out=[]
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(t)
        seg=t[m.start():end]
        h=re.search(r"\n### ",seg)
        if h: seg=seg[:h.start()]+"\n\n"
        out.append((m.group(1),seg))
    return out
_have={k for k,_ in _ents(_ARC)}
_new=[(k,t) for k,t in _ents(_CH) if k not in _have]
REG=_ARC+"".join(t for _,t in _new)
if _new:
    open("REGISTER-DATA.md","w",encoding="utf-8").write(REG)
PAT=re.compile(r"^ {0,3}((?:\d{3,4}, )*\d{3,4})\. ",re.M)
ms=list(PAT.finditer(REG))
ent=[]
for i,m in enumerate(ms):
    end=ms[i+1].start() if i+1<len(ms) else len(REG)
    # a grouped label like "305, 361." must sort by its FIRST number, which is
    # where the entry sits in the sequence (register 650)
    n=int(re.findall(r"\d{3,4}",m.group(1))[0])
    ent.append((n,m.group(1),REG[m.end():end].rstrip()))

# which entries does the BODY cite?
body=S[:RS]+S[RE_:]
cited=set()
for m in re.finditer(r"[Rr]egisters?\s+((?:\d{3,4}(?:\s*[–,-]\s*)?)+)",body):
    for g in re.findall(r"\d{3,4}",m.group(1)): cited.add(int(g))
    rng=re.findall(r"(\d{3,4})\s*[–-]\s*(\d{3,4})",m.group(1))
    for a,b in rng: cited.update(range(int(a),int(b)+1))

L=[];W=L.append
W("# THE METHOD 1.6 — THE REGISTER")

# ---------------------------------------------------------------- front matter
# Register 1243. The register was 1,032 entries with no way in. A reader could
# check any claim and could not find one. This front matter is generated from the
# entries themselves, so it cannot drift from them.
from collections import Counter as _C, defaultdict as _dd
_ENT = re.findall(r"^\s{0,3}(\d{3,4})\.\s(.*?)(?=\n\s{0,3}\d{3,4}\.\s|\Z)",
                  open("REGISTER-DATA.md", encoding="utf-8").read(), re.M | re.S)
_KIND = [
 ("a fault of mine", r"\bI (?:wrote|applied|read|reported|assumed|missed|used|fitted|"
                     r"claimed|took|swallowed|never)\b|my (?:own|error|fault|regex|"
                     r"reading|check)|a fault of mine|MY OWN"),
 ("a withdrawal",    r"\bWITHDRAW|withdrawn|superseded|retracted|reversed"),
 ("a correction",    r"\bCORRECT|corrected|repaired|the fix|\bwrong\b"),
 ("prior art",       r"PRIOR ART|prior art|already published|Edl[eé]n|Seaton|Racah|Birkhoff"),
 ("a new protocol",  r"\bprotocol\b|audit \d|now checks|part of the seal"),
 ("an open question",r"\bunresolved\b|cannot (?:be )?test|remains open"),
 ("a measurement",   r"\brms\b|R²|\bmedian\b|\d+ of \d+|\bp = \d"),
]
_tal = _C(); _first = {}
for _n, _b in _ENT:
    _got = False
    for _k, _p in _KIND:
        if re.search(_p, _b, re.I):
            _tal[_k] += 1; _first.setdefault(_k, int(_n)); _got = True
    if not _got: _tal["a finding"] += 1
_cite = _C()
for _n, _b in _ENT:
    for _m in re.finditer(r"[Rr]egisters? (\d{3,4})", _b): _cite[int(_m.group(1))] += 1

W("")
W("## How to read this register")
W("")
W(f"**{len(ent)} entries, {min(n for n,_,_ in ent)} to "
  f"{max(int(x) for _,l,_ in ent for x in re.findall(chr(92)+chr(100)+chr(123)+chr(51)+chr(44)+chr(52)+chr(125), l))}.** "
  "Each is written at a fixed density and stands "
  "alone. *The register is the working record the five compendia are distilled from: "
  "it argues, it reverses itself, and it keeps the reversals. The compendia answer; "
  "this is where the answers were got.*")
W("")
W("**An entry is cited by a chapter, by a compendium object, or by another entry. "
  "Nothing here is decorative — an entry exists because something rests on it.**")
W("")
W("### What the entries are")
W("")
W("| kind | entries | what it means |")
W("|---|---|---|")
_MEAN = {
 "a finding": "something established that was not known before the entry",
 "a measurement": "a number, with what it was measured on",
 "a correction": "something written wrong and put right, with both states kept",
 "prior art": "a result found to be published, with the source",
 "an open question": "something the work cannot currently settle, and why",
 "a withdrawal": "a claim removed, with the reason",
 "a new protocol": "a rule earned by a failure, so the failure cannot recur",
 "a fault of mine": "an error by the assistant, recorded as such",
}
for _k, _v in _tal.most_common():
    W(f"| **{_k}** | {_v} | {_MEAN.get(_k, '')} |")
W("")
W("*The kinds overlap: a correction is usually also a measurement, and a withdrawal "
  "usually cites prior art. The counts are of entries matching each pattern, not a "
  "partition.*")
W("")
W("### The load-bearing entries")
W("")
W(f"**{len(_cite)} entries are cited by other entries.** Those cited most are the "
  "ones the rest of the record leans on:")
W("")
W("| entry | cited | what it established |")
W("|---|---|---|")
_WHAT = {
 784: "a fault invisible to every audit, because audits check consistency and not provenance",
 679: "the residual is structured, so it is a measurement and not a rounding",
 802: "monotonicity is directionally right and not universal",
 868: "R∞ used where the reduced-mass Rydberg is correct — a systematic in every channel",
 675: "what stops the collection is truncation, not missing species",
 727: "the three-member rule relaxed where the limit is published",
 782: "a verification column set equal to its own denominator — passing by construction",
 341: "two chapter ones; continuous numbering, 1,183 edits",
 287: "the density protocol for register entries",
 387: "what a bracket can and cannot say",
}
for _r, _c in _cite.most_common(10):
    W(f"| **{_r}** | {_c}× | {_WHAT.get(_r, '—')} |")
W("")
W("### Where the corrections came from")
W("")
W("**A fault is only half an entry; what resolved it is the other half.** *Of the "
  "corrections recorded here, the resolutions fall into four kinds:*")
W("")
W("| resolution | example |")
W("|---|---|")
W("| **a published result** | R∞ → R_M is Bohr 1913, made after Fowler objected that "
  "the Pickering series did not fit (registers 868, 1241) |")
W("| **a measurement the work already held** | the multiplicity constraint was proved "
  "at register 1139 and not carried into the operator until 1178 |")
W("| **an audit written after the fact** | the dependency cycle Q.delta → Q.exch → "
  "Q.delta, caught only when audit 24 was written (registers 1208, 1225) |")
W("| **the person's correction** | pushing back where the assistant stopped looking "
  "too early — recorded wherever it happened |")
W("")
W("---")
W("")

W("")
W(f"Generated from the book's source on {datetime.date.today().isoformat()}. "
  f"**{len(ent)} entries, {min(n for n,_,_ in ent)} to "
  f"{max(int(x) for _,l,_ in ent for x in re.findall(chr(92)+chr(100)+chr(123)+chr(51)+chr(44)+chr(52)+chr(125), l))}.**")
W("")
W("Every correction, withdrawal and finding in the order it happened. **The book cites entries where")
W("they carry an argument; the complete record lives here.** Rebuild with `python3 register_gen.py >")
W("REGISTER.md` — it reads the source, so it cannot drift.")
W("")
W(f"**{len(cited & {e[0] for e in ent})} entries are cited somewhere in the book's chapters.** The rest")
W("are the record of how the work went, which is the material §4's mechanisms were built from.")
W("")
W("---")
W("")
for n,lbl,txt in ent:
    tag = " · **cited**" if n in cited else ""
    W(f"### {lbl}{tag}")
    W("")
    W(re.sub(r"\n\s+"," ",txt).strip())
    W("")
print("\n".join(L))
