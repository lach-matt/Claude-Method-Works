data = open("BUILD56_main.md",encoding="utf-8").read()
lines = data.split("\n")
def c(s): return data.count(s)
def cl(s): return sum(1 for ln in lines if ln==s)
checks = [
 ("order dimension exactly **7**", c("order dimension exactly **7**"), 1),
 ("omega(N(x)) <= 8, the coordinate count", c("ω(N(x)) ≤ 8, the coordinate count"), 1),
 ("an order of dimension seven", c("an order of dimension seven"), 1),
 ("line ### 1 (genesis)", cl("### 1"), 1),
 ("2S' <= v <= g, parity", c("2S′ ≤ v ≤ g, parity"), 0),
 ("IoI 46,740", c("46,740"), 1),
 ("IoI 0.6592", c("0.6592"), 1),
 ("IoI 127,070", c("127,070"), 1),
 ("IoI 0.6381", c("0.6381"), 1),
]
allpass=True
for name,got,exp in checks:
    ok = got==exp
    allpass &= ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got} expected {exp}")
print("MAIN ALL PASS" if allpass else "MAIN HAS FAILURES")