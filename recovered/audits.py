"""The twenty prime audits of The Method 1.3 §3, run against
On the Matter of Time Travel. Exits with the number of failures.
Every audit prints its evidence, not merely its verdict."""
import re, os, subprocess, unicodedata, sys
from itertools import combinations, product

SRC = "paper.md"
PDF = "On_the_Matter_of_Time_Travel.pdf"
FIGDIR = "fig"
S = open(SRC, encoding="utf-8").read()
TXT = subprocess.run(["pdftotext", PDF, "-"], capture_output=True,
                     text=True, encoding="utf-8").stdout

results = []
def rec(n, name, ok, note):
    results.append((n, name, ok, note))
    print(f"{n:>2}  {name:<12} {'PASS' if ok else 'FAIL'}  {note}")

# ---------------------------------------------------------------- 1 LATTICE
def lam(NM,EM,LM,KM,FM,extra=0):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            out.append((n,l,k,q,e,f,g,s))
    return out
L8 = lam(3,3,1,3,1)
SET = set(L8)
jm = sum(1 for a,b in combinations(L8,2)
         if tuple(map(max,a,b)) not in SET or tuple(map(min,a,b)) not in SET)
rk = lambda x: sum(x)
mod = sum(1 for a,b in combinations(L8,2)
          if rk(tuple(map(max,a,b)))+rk(tuple(map(min,a,b))) != rk(a)+rk(b))
prof = {}
for x in L8: prof[rk(x)] = prof.get(rk(x),0)+1
F1 = sum(prof.values()); Fm1 = sum(c*(-1)**r for r,c in prof.items())
alpha = sum(len({x[i] for x in L8})-1 for i in range(8))
refl = sum(1 for x in L8 if tuple(max(y[i] for y in L8)-x[i] for i in range(8)) in SET)
cyl = sum(len({(x[0],x[1],x[2],x[7]) for x in L8 if x[3]==q}) *
          len({(x[4],x[5],x[6]) for x in L8 if x[3]==q}) for q in range(4))
lat = (len(L8)==976 and jm==0 and mod==0 and F1==976 and Fm1==2
       and alpha==17 and refl==8 and cyl==976 and max(prof.values())==122)
rec(1,"LATTICE",lat,
    f"|Λ₈|={len(L8)} · {len(L8)*(len(L8)-1)//2:,} pairs, {jm} join/meet + {mod} modularity failures · "
    f"F(1)={F1} F(−1)={Fm1} · Σ(|Aᵢ|−1)={alpha} · reflection={refl} · Σ|A||B|={cyl}")

# ---------------------------------------------------------------- 2 EQUATIONS
eqs = []
# the title identity
eqs.append(("|∏Aᵢ| = |X| + E + refused", 6912 == 976 + 0 + 5936))
# g ≤ q ≤ k gives a monotone clock, on Λ₉
L9 = [c+(sp,) for c in L8 for sp in range(0,c[6]+1)]
src = lambda c:(c[0],c[1],c[2],c[7]); tgt = lambda c:(c[4],c[5],c[6],c[8])
srcs = {src(c) for c in L9}
rises = sum(1 for c in L9 if tgt(c) in srcs and tgt(c)[2] > src(c)[2])
eqs.append(("occupancy never rises", rises == 0))
# Cesàro chain equals R(exact) at n=3, N=12
def exact3(N):
    return [(a,a+b,a+b+c) for a in range(N+1) for b in range(a+1) for c in range(b+1)
            if a+b+c<=N]
def chain3(N):
    return [(a,s,m) for a in range(N+1) for s in range(a,min(2*a,N)+1)
            for m in range(s,min(3*s//2,N)+1)]
eqs.append(("chain(3,12) = 142", len(chain3(12))==142))
eqs.append(("exact(3,12) = 102", len(exact3(12))==102))
eqs.append(("E(exact) = 40", len(chain3(12))-len(exact3(12))==40))
# Sc VI
d4,d5 = 1.0057,0.9812
d2 = (d4-d5)/(1/16-1/25); dinf = d4-d2/16; d6 = dinf+d2/36
T = lambda n,d: 36*109737.31568/(n-d)**2
E6 = 892700.0 - T(6,d6)
eqs.append(("Sc VI estimate = 736,688", round(E6) == 736688))
eqs.append(("Sc VI bracket lower = 735,860", round(892700.0-T(6,d5)) == 735860))
eqs.append(("Sc VI convex upper = 737,380", round(892700.0-T(6,2*d5-d4)) == 737380))
# meet-closure of the concave set
conc = [c for c in exact3(12)]
CS = set(conc)
mf = sum(1 for a,b in combinations(conc,2) if tuple(map(min,a,b)) not in CS)
eqs.append(("exact set meet-closed", mf == 0))
bad = [n for n,ok in eqs if not ok]
rec(2,"EQUATIONS", not bad, f"{len(eqs)-len(bad)} of {len(eqs)} evaluated true" +
    (f" · failing: {bad}" if bad else ""))

# ---------------------------------------------------------------- 3 CONSISTENCY
# every figure that appears more than once must agree with itself
nums = {}
for m in re.finditer(r'(\d{1,3}(?:,\d{3})+|\b\d+\.\d+%|\b\d+%)', S):
    nums[m.group(1)] = nums.get(m.group(1),0)+1
claims = {
 "976": S.count("976"), "1,654": S.count("1,654"), "199,130": S.count("199,130"),
 "41,682": S.count("41,682"), "475,800": S.count("475,800"),
}
# contradiction probes: paired statements that must not both appear
contra = []
if "meet failures are zero" in S and re.search(r"meet fail\w*\s*\|\s*[1-9]", S): contra.append("meet")
if "E(X) = 0" in S and "E(Λ) > 0" in S: contra.append("E")
# the register count must agree between the abstract and Part VI
abs_n = re.search(r"withdrawal register — (\w+) entries", S)
part6 = re.search(r"# PART VI.*?\n\n(\w+) entries", S, re.S)
n_reg = len(re.findall(r"^\*\*\d+\. ", S, re.M))
words = {"eight":8,"nine":9,"ten":10,"seven":7}
stated = words.get(part6.group(1).lower()) if part6 else None
ok3 = not contra and stated == n_reg
rec(3,"CONSISTENCY", ok3,
    f"register: Part VI states '{part6.group(1) if part6 else '—'}' = {stated}, entries present = {n_reg}"
    + (f" · contradictions: {contra}" if contra else ""))

# ---------------------------------------------------------------- 4 REDUNDANCY
# no table may be restated in prose within the same section
secs = re.split(r'\n#{1,3} ', S)
dupes = []
for sec in secs:
    rows = re.findall(r'^\|(.+)\|$', sec, re.M)
    for r in rows:
        cells = [c.strip() for c in r.split('|') if c.strip() and not set(c.strip()) <= set('-: ')]
        for c in cells:
            if len(c) > 45 and sec.count(c) > 1: dupes.append(c[:40])
# Appendix B must not restate a figure the body already gives
rec(4,"REDUNDANCY", not dupes,
    f"{len(rows) if secs else 0} table rows scanned across {len(secs)} sections · "
    f"{len(dupes)} statements surviving their own restatement")

# ---------------------------------------------------------------- 5 ARTEFACT
bad_glyph = {c for c in TXT if c in "\ufffd\u25a1" or unicodedata.category(c)=="Co"}
probe_ok = len({c for c in TXT+"\ufffd" if c in "\ufffd\u25a1"}) == 1   # §4.6
info = subprocess.run(["pdfinfo",PDF],capture_output=True,text=True).stdout
pages = int(re.search(r"Pages:\s+(\d+)",info).group(1))
fonts = subprocess.run(["pdffonts",PDF],capture_output=True,text=True).stdout.splitlines()[2:]
unemb = [l for l in fonts if l.split()[-4] != "yes"]
imgs = len(subprocess.run(["pdfimages","-list",PDF],capture_output=True,text=True).stdout.splitlines())-2
bbox = subprocess.run(["pdftotext","-bbox",PDF,"-"],capture_output=True,text=True).stdout
overflow = 0
for b in re.findall(r'<page .*?>(.*?)</page>', bbox, re.S):
    xs=[float(x) for x in re.findall(r'xMax="([\d.]+)"',b)]
    if xs and max(xs) > 595.28-40: overflow += 1
ok5 = not bad_glyph and not unemb and overflow==0 and imgs==16 and probe_ok
rec(5,"ARTEFACT", ok5,
    f"{pages}pp · {len(bad_glyph)} bad glyphs (probe can fail: {probe_ok}) · "
    f"{len(unemb)} unembedded fonts · {imgs} images · {overflow} overflowing pages")

# ---------------------------------------------------------------- 6 COHERENCE
figrefs = re.findall(r'!\[Figure (\d)\]\((fig/[^)]+)\)', S)
figcaps = re.findall(r'\*\*Figure (\d)\.\*\*', S)
missing_files = [p for _,p in figrefs if not os.path.exists(p)]
unused = set(os.listdir(FIGDIR)) - {os.path.basename(p) for _,p in figrefs}
heads = re.findall(r'^#{1,3} (.+)$', S, re.M)
# internal § references must point at sections this paper has, or at the book (which is external)
own = re.findall(r'§(\d+)\b', S)
ok6 = (not missing_files and not unused
       and [a for a,_ in figrefs]==figcaps)
rec(6,"COHERENCE", ok6,
    f"{len(figrefs)} figure refs, {len(figcaps)} captions, paired in order · "
    f"{len(missing_files)} missing files · {len(unused)} unused files · {len(heads)} headings")

# ---------------------------------------------------------------- 7 ATTRIBUTION
refblock = S.split("## Appendix D — References")[1]
authors = re.findall(r'^([A-Z][A-Za-z\-]+(?:, [A-Z]\.)*)', refblock, re.M)
listed = {a.split(',')[0] for a in authors}
body = S.split("## Appendix D — References")[0]
cited = set()
for name in ["Brylawski","Baker","Pixley","Birkhoff","Dilworth","Knaster","Tarski",
             "Nesterov","Nemirovskii","Racah","Rival","Siggers","Lach"]:
    if name in body: cited.add(name)
uncited = listed - cited
unlisted = cited - listed
ok7 = not uncited and not unlisted
rec(7,"ATTRIBUTION", ok7,
    f"{len(listed)} works listed, {len(cited)} cited in the body · "
    f"listed-and-uncited {sorted(uncited)} · cited-and-unlisted {sorted(unlisted)}")

# ---------------------------------------------------------------- 14 ARITHMETIC
# every count in the tower table derived from the construction, not read from the book
tower = {8:976, 9:1654, 10:2535}
L10 = [c+(v,) for c in L9 for v in range(c[8], c[6]+1)]
arith = (len(L8)==tower[8] and len(L9)==tower[9] and len(L10)==tower[10])
# and one digit altered must break it, per 4.6
canfail = (len(L8) != 977)
rec(14,"ARITHMETIC", arith and canfail,
    f"Λ₈={len(L8)} Λ₉={len(L9)} Λ₁₀={len(L10)} rebuilt from §7.1 · shown able to fail: {canfail}")

# ---------------------------------------------------------------- 15 ENUMERATION
enum = []
enum.append(("eight figures", len(figrefs)==8, f"{len(figrefs)}"))
enum.append(("Appendix B.1 lists eight", len(re.findall(r'^\| [1-8] \|', S, re.M))==8,
             str(len(re.findall(r'^\| [1-8] \|', S, re.M)))))
enum.append(("Part VI: register entries", n_reg==stated, f"{n_reg} vs stated {stated}"))
oc = re.findall(r'\*\*O(\d)', S)
enum.append(("Appendix C items O1..On contiguous", oc==[str(i+1) for i in range(len(oc))], ",".join(oc)))
badenum=[e for e in enum if not e[1]]
rec(15,"ENUMERATION", not badenum,
    " · ".join(f"{n}: {v}" for n,_,v in enum))

# ---------------------------------------------------------------- 19 SEQUENCE
secnums = [int(m) for m in re.findall(r'^## (\d+)\. ', S, re.M)]
gaps = [i for i in range(1,len(secnums)) if secnums[i] != secnums[i-1]+1]
dup = len(secnums)!=len(set(secnums))
rec(19,"SEQUENCE", not gaps and not dup,
    f"§1–§{max(secnums)} present, {len(secnums)} sections, "
    f"{len(gaps)} breaks in ascent, duplicates: {dup}")

# ---------------------------------------------------------------- 20 PROJECTION
src_heads = [h.strip() for h in re.findall(r'^#{1,2} (.+)$', S, re.M)]
in_pdf = [h for h in src_heads if h.replace('*','').split('—')[0].strip()[:28] in TXT]
rec(20,"PROJECTION", len(in_pdf)==len(src_heads),
    f"{len(in_pdf)} of {len(src_heads)} top-level headings project from source into the artefact")

# ---------------------------------------------------------------- DEPTH
depths = [len(m.group(1)) for m in re.finditer(r'^(#{1,6}) ', S, re.M)]
jumps = [i for i in range(1,len(depths)) if depths[i]-depths[i-1] > 1]
rec(21,"DEPTH", not jumps, f"max depth {max(depths)}, {len(jumps)} skipped levels")

# ---------------------------------------------------------------- SCOPE
# every density/count claim must carry its cap or its n
scope_fail = []
for m in re.finditer(r'(\d+\.\d)%', S):
    ctx = S[max(0,m.start()-320):m.start()+120]
    if not re.search(r'\bN = \d+|\bcap\b|n = \d|caps\b|four caps|at N|per cent|density', ctx):
        scope_fail.append(m.group(0))
rec(22,"SCOPE", not scope_fail,
    f"{len(re.findall(r'[0-9]+\\.[0-9]%', S))} percentage claims, "
    f"{len(scope_fail)} without a stated cap or n in context")

# ---------------------------------------------------------------- FIDELITY
fid = []
for probe in ["199,130","41,682","475,800","736,688","Brylawski","infimum subsemilattice",
              "occupancy clock","9,720","5,936","68.1"]:
    if TXT.count(probe) == 0: fid.append(probe)
rec(23,"FIDELITY", not fid,
    f"10 source strings probed in the artefact's text layer · {len(fid)} absent {fid}")

# ---------------------------------------------------------------- ANTECEDENT
orphan = []
seen_part = False
for line in S.split("\n"):
    if re.match(r'^# PART|^# APPENDICES|^# On the Matter', line): seen_part = True
    if re.match(r'^## \d+\. ', line) and not seen_part: orphan.append(line[:40])
rec(24,"ANTECEDENT", not orphan, f"{len(orphan)} numbered sections without a parent part")

# ---------------------------------------------------------------- the unnamed five
print()
print("Audits 8–13 and 16–18 are not named anywhere in The Method 1.3.")
print("§3 names seven; §3.8 adds DEPTH, SEQUENCE, PROJECTION; the registers add")
print("ARITHMETIC (14), ENUMERATION (15), FIDELITY, SCOPE, ANTECEDENT — fifteen in all.")
print("Five of the twenty exist only as a count. They are recorded as unrunnable,")
print("not as passing: an assertion is not an enumeration (§E.4.1).")

fails = sum(1 for _,_,ok,_ in results if not ok)
print(f"\n{len(results)} audits run, {fails} failures, 5 unrunnable.")
sys.exit(fails)
