#!/usr/bin/env python3
"""pagemap.py -- pass one: where each heading lands.

Register 665. The contents had no page numbers because a page number does not
exist until the document is laid out. This extracts heading→page from a built
PDF and writes PAGEMAP.tsv, which the press reads on the next pass.
"""
import re, subprocess, sys
from zeno import State, step
def run():
    L=subprocess.run(["pdftotext","-layout","/mnt/user-data/outputs/The Method 1.6.pdf","-"],
                     capture_output=True,text=True).stdout
    pages=L.split("\f")
    s=open("The Method 1.6.md",encoding="utf-8").read()
    j=s.index("## References",s.index("Contents"))
    heads=[]
    for m in re.finditer(r"^(#{1,3}) (\S[^\n]*)$",s[j:],re.M):
        _h=m.group(2)
        _h=re.sub(r"\*\*|\*|`","",_h)          # the render strips emphasis marks
        heads.append(re.sub(r"\s+"," ",_h).strip())
    # the contents itself occupies the front pages; skip them when searching
    # a contents page is one where many lines ARE heading titles. Density of
    # numbered lines failed: the last contents page is mostly end-matter entries,
    # which carry no section number (register 665).
    titles={re.sub(r"\s+"," ",h).strip() for h in heads}
    first_body=0
    for i,pg in enumerate(pages):
        flat=[re.sub(r"\s+"," ",l).strip() for l in pg.split("\n") if l.strip()]
        flat=[l for l in flat if not re.match(r"^The Method — The Lach Cylinder", l)
              and not re.fullmatch(r"\d{1,4}", l)]
        # a contents line now ends with its own page number, so it no longer
        # matches the bare title (register 666)
        hits=sum(1 for l in flat if re.sub(r"\s+\d{1,4}$","",l) in titles)
        # the contents can spill a page holding only two entries, so a page that is
        # ENTIRELY heading titles counts however few it has
        if hits>=8 or (flat and hits>=2 and hits==len(flat)): first_body=i
    out={}
    for h in heads:
        key=re.sub(r"\s+"," ",h).strip()
        probe=key[:40]
        # a heading begins a line; a bare word matched mid-paragraph gave
        # "References" on page 12 (register 665)
        pat=re.compile(r"^\s{0,6}"+re.escape(probe[:34]), re.M)
        # a short title like "Index" or "References" occurs mid-book as a word, so
        # end-matter headings are searched from the BACK
        rng=range(len(pages)-1,first_body,-1) if len(key)<14 else range(first_body+1,len(pages))
        for i in rng:
            flat="\n".join(re.sub(r"\s+"," ",l) for l in pages[i].split("\n"))
            if probe and pat.search(flat):
                out[key]=str(i)
                break
    return out,len(heads)
with State("pagemap") as st:
    out,n=step(st,"map every heading to its page",run,budget=600)
with open("PAGEMAP.tsv","w",encoding="utf-8") as f:
    for k,v in out.items(): f.write(f"{k}\t{v}\n")
print(f"  {len(out)} of {n} headings located")
