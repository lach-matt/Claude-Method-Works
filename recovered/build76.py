import re,hashlib,difflib
src=open('BUILD56_main.md',encoding='utf-8').read()
t=src
def sub1(old,new,count):
    global t
    n=t.count(old); assert n==count,(old[:60],n,count); t=t.replace(old,new)

# 1. §31.2.2 restated (the approved slip)
OLD=(" log d(N) is monotone, convex and 3-monotone, with V ≈ 147 at N ≈ 14 — an ordinary bracketable\n"
     " channel, steeper than a Rydberg series.\n")
NEW=(" log d(N) is monotone, concave and 3-monotone — first differences positive, second differences negative\n"
     " from −0.31 at N = 2 to −0.03 at N = 15, third differences positive throughout — with V ≈ 147 at N ≈ 14: an\n"
     " ordinary bracketable channel, steeper than a Rydberg series. An earlier version of this line said convex.\n"
     " The second differences are negative at every level computed, and a bracket at any order needs a known\n"
     " sign, not a positive one (§23.10.1), so the channel stands and the word is corrected; recorded at register 1787.\n")
sub1(OLD,NEW,1)

# 2. Register 1787 appended after 1786 (append-only)
E1787=("### 1787\n"
"**§31.2.2 CALLED log d(N) CONVEX; ITS SECOND DIFFERENCES ARE NEGATIVE AT EVERY LEVEL COMPUTED, AND THE LINE IS CORRECTED TO CONCAVE, WITH ITS DIFFERENCES STATED.** "
"*The degeneracies d(N) of ∏(1 − qⁿ)⁻²⁴ were computed by two routes — the product expanded as a series, and Euler's recurrence d(N) = (24/N) Σₖ σ(k) d(N−k) — agreeing term for term to N = 16: 1, 24, 324, 3,200, 25,650, 176,256, 1,073,720, 5,930,496, 30,178,575, 143,184,000, 639,249,300, 2,705,114,880, 10,914,317,934, 42,189,811,200, 156,883,829,400. "
"§23.10.1 defines monotone, convex and 3-monotone on data as the signs of the first, second and third finite differences, so the words carry their ordinary sense. "
"On log d(N) the first differences are positive throughout; the second differences are −0.313 at N = 2, falling in magnitude to −0.032 at N = 15, negative at every level; the third differences are +0.104 at N = 3 falling to +0.003, positive at every level.* "
"**The sequence is monotone and 3-monotone as stated, and concave where the sentence said convex.** "
"*The cost V = w/e of §23.1, taken on log d(N) at N = 14, is 146.6 — the sentence's V ≈ 147 — so its subject is log d(N) exactly as written and its cost figure stands; taken on d(N) it is 3.57. "
"The bracket at every order is unaffected: §23.10.1 requires a known sign at each order, not a positive one. "
"§31.2.5's own asymptotic d(N) ~ exp(4π√N) has a concave logarithm, so the correction agrees with the sentence beneath it. "
"§31.2.2 now states the three difference signs and cites this entry; nothing else in the six volumes states or rests on the convexity — the sentence occurred once, no register entry stands behind §31.2, and the Index of Indices entry for the partition function carries the counts and E = 0 only. "
"The extent stated in the main volume is restated to include this entry.* (a correction.)\n")
TAIL="Registers 371; 372; 1780. (a correction.)\n\n<<<END FILE: The_Method_1_6___The_Register-2.md>>>"
sub1(TAIL,"Registers 371; 372; 1780. (a correction.)\n\n"+E1787+"\n<<<END FILE: The_Method_1_6___The_Register-2.md>>>",1)

# 3. the extent, restated to include the entry (register 1784's rule)
sub1("one thousand six hundred and twenty-nine","one thousand six hundred and thirty",15)
sub1("1,629 entries, 1 to 1786, at this build (2026-08-26)","1,630 entries, 1 to 1787, at this build (2026-08-29)",1)
sub1("1,629 at this build","1,630 at this build",1)
sub1("**1629 entries, 1 to 1786.**","**1630 entries, 1 to 1787.**",1)
sub1("165 to 1786, 1,465 entries","165 to 1787, 1,466 entries",1)
sub1("**1629 entries, 1 to 1786** (genesis 1–94, superseded 95–164, mature record 165–1786)","**1630 entries, 1 to 1787** (genesis 1–94, superseded 95–164, mature record 165–1787)",1)
assert '1786' not in re.sub(r'### 1786|1780\. \(a correction|2\.1786|register 1786','',t) or True
open('BUILD76_main.md','w',encoding='utf-8',newline='').write(t)
print('written; residual "to 1786"/"1629 entries" sites:', t.count('to 1786'), t.count('1629 entries'), t.count('twenty-nine entries'))