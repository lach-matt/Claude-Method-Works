import re, sys, json
SRC="The_Method_1_6___The_Register-2.md"
# Ruling 27 + amendment. Tiers name WHY an entry leaves the subject-matter Register.
TIERS=[
("A-production", re.compile(r"pandoc|\.docx|\bdocx\b|typeset|markdown|markup|asterisk|flanking|smart quote|bold marker|italic|heading (level|tier)|\bfont\b|margin|page number|dot leader|column width|colWidths|contents (block|tier|lost)|alt line|\.zip\b|\.tar\b|bundle|split\.py|round-trip|roundtrip|build\.py|press(ed|es|ing)? (fault|leak|carri|hardcod|stamp|drop)|rendered? as (searchable|literal|run-on)|printed as (literal|run-on)", re.I)),
("B-session",    re.compile(r"handoff|\bsession\b|this chat|context (window|at 90)|DIGEST\.md|restore.point|Prime (Handoff|Zeno)|intake protocol|standing board|BRIDGE-|§H\.\d|the first turn|before a single file was read", re.I)),
("C-internal",   re.compile(r"\bstale\b|recount|re-count|entry count|citation count|load-bearing table|duplicated entries|unpaired bold|caption(s)? (written|read against|says|vs)|against (its|their) caption|locator|cross-reference(s)? (resolve|in the shipped|not two)|superseded (line|figure|count)|index regenerated|normalised to its own settled form", re.I)),
]
# Explicit overrides: subject matter that trips a pattern incidentally.
KEEP={364,294,379,1403,1411,1705,863,923,926,930,948,1176,1179,1275,1379,1407,1435,1437,1438,1450,1458,1460,1480,1493,1494,1495,1496,1610,1619,1655,1657,1660,1701,1702,1712,599,601,616,644,720,729,733,855,856,857,867,953,954,1174,523,491,585,1016,1584,1595,1658}
FORCE={1667,1668,1670,1676,1685,1697,1659,1614,1616,1631,1650,1698,1594,1000,1002,1725,1732,1743,1744,1745,1746,1747,1752,1753,1754,1756,1757,1759,1760,1764,1728,1735,1737,1741,1742,1149,1245,1248,1373,1386,1388,1564,1572,1680,1684,606,649,651,654,657,660,664,665,666,667,668,669,632,637,642,650,998,999,190,204,272,324,341,363,369,430,431,456,460,570,996,995,1358,1570,1617,1443,1477,1478,1565,1571,575,574,571,1537,1615}
parts=re.split(r"(?=\n### \d)", "\n"+open(SRC,encoding="utf-8").read())
out=[]
for p in parts:
    m=re.match(r"\n### ([\d, ]+)\n", p)
    if not m: out.append(("HEAD",None,p,None)); continue
    nums=[int(x) for x in re.findall(r"\d+", m.group(1))]
    trig=None
    for name,rx in TIERS:
        if rx.search(p): trig=name; break
    if any(n in FORCE for n in nums): trig=trig or "A-production"
    if any(n in KEEP for n in nums): trig=None
    out.append(("EX" if trig else "KEEP", nums, p, trig))
ex=[o for o in out if o[0]=="EX"]
print("EXCISE:",len(ex)," KEEP:",len([o for o in out if o[0]=='KEEP']))
if "--list" in sys.argv:
    for _,nums,p,t in ex:
        h=re.sub(r"\s+"," ",p.split("\n### ")[1].split("\n",1)[1] if "\n" in p else p)
        print("%-11s %-13s %s" % (",".join(map(str,nums)), t, h[:66]))
json.dump({"excise":[o[1] for o in ex]},open("excise_plan.json","w"))