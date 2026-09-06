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
        heads.append(re.sub(r"\s+"," ",m.group(2)).strip())
    # the contents itself occupies the front pages; skip them when searching
    first_body=0
    for i,pg in enumerate(pages):
        if "PART I" in pg and "PART II" in pg: first_body=i
    out={}
    for h in heads:
        key=re.sub(r"\s+"," ",h).strip()
        probe=key[:52]
        for i in range(first_body+1,len(pages)):
            if probe and probe in re.sub(r"\s+"," ",pages[i]):
                out[key]=str(i)      # pdftotext page 0 is the cover; i is 1-based display
                break
    return out,len(heads)
with State("pagemap") as st:
    out,n=step(st,"map every heading to its page",run,budget=600)
with open("PAGEMAP.tsv","w",encoding="utf-8") as f:
    for k,v in out.items(): f.write(f"{k}\t{v}\n")
print(f"  {len(out)} of {n} headings located")