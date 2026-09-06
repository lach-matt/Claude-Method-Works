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
S=open("The Method 1.5.md",encoding="utf-8").read()
RS=S.rindex("## 28. Withdrawals"); RE_=S.rindex("## 29.")
REG=S[RS:RE_]
PAT=re.compile(r"^ {0,3}((?:\d{3}, )*\d{3})\. ",re.M)
ms=list(PAT.finditer(REG))
ent=[]
for i,m in enumerate(ms):
    end=ms[i+1].start() if i+1<len(ms) else len(REG)
    n=int(re.findall(r"\d{3}",m.group(1))[-1])
    ent.append((n,m.group(1),REG[m.end():end].rstrip()))

# which entries does the BODY cite?
body=S[:RS]+S[RE_:]
cited=set()
for m in re.finditer(r"[Rr]egisters?\s+((?:\d{3}(?:\s*[–,-]\s*)?)+)",body):
    for g in re.findall(r"\d{3}",m.group(1)): cited.add(int(g))
    rng=re.findall(r"(\d{3})\s*[–-]\s*(\d{3})",m.group(1))
    for a,b in rng: cited.update(range(int(a),int(b)+1))

L=[];W=L.append
W("# THE METHOD 1.5 — THE REGISTER")
W("")
W(f"Generated from the book's source on {datetime.date.today().isoformat()}. "
  f"**{len(ent)} entries, {ent[0][0]} to {ent[-1][0]}.**")
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