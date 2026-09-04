# DELIVERY INSTRUMENT (new, thin): prints the per-cap closure table for caps 3-12 that figs.py computed inline
# via `rows=[closure_test(c) for c in caps]` and printed as `print([(c,)+r for c,r in zip(caps,rows)])`.
# Same closure operator: audit.py::closure_test (min/max on the cell set) — NOT the book's tower-2.py.
import sys, time
src=open('audit.py').read().split('print("case')[0]; exec(src)
print("cap\tcells\tmeet_failures\tjoin_failures\ttwo_body_chain_failures\tseconds")
for cap in range(3,13):
    t=time.time(); n,mf,jf,tf=closure_test(cap); print(f"{cap}\t{n}\t{mf}\t{jf}\t{tf}\t{time.time()-t:.2f}")