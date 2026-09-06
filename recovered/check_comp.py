data = open("BUILD60_compendia.md",encoding="utf-8").read()
def c(s): return data.count(s)
checks = [
 # HANDOFF-9 set (=1 each)
 ("order dimension of Λ₈ is 7", 1),
 ("Dilworth partition of all 976 cells into 122 chains", 1),
 ("fifteen coordinate-support patterns", 1),
 ("riding monotonicity upward", 1),
 ("### W-090", 1),
 ("### W-091", 1),
 ("### `S.gen`", 1),
 ("### `K.bracket`", 1),
 ("## THE PRIOR-ART CHAIN", 1),
 ("ω(N(x)) ≤ 8, the coordinate count — proved and tight", 1),
 ("five equivalent forms, all equal to ∏_i(|x_i−y_i|+1)", 1),
 ("the maximum local up-degree is 7", 1),
 ("μ_Λ(x,y) = μ_arith(N(x),N(y)) if and only if the interval", 1),
 ("exactly the product of the six edge lifts in tree order", 1),
 ("1.0000 in every stratum for all five shared-coordinate pairs", 1),
 # CHANGED set
 ("`K.decay` `K.markov` `L.voidfrac`", 0),
 ("`K.decay` `K.markov` `L.box` `L.voidfrac`", 1),
 ("Chebyshev's sum inequality", 2),
 # BUILD59 content discriminators (=1)
 ("116,138 distinct boxes, zero discrepancies", 1),
 ("width 1 if and only if it is a forest", 1),
 ("the tree count is 280, the true count 240", 1),
 ("the accepted set is equal as a set to the image", 1),
 ("no bit is forced by more than 3 others", 1),
 ("0.7446 % of the space it is written in", 1),
 # Grade objects (=1 each)
 ("### `L.omega`", 1),
 ("### `L.occ`", 1),
 ("### `L.metric`", 1),
 ("### `L.mobius`", 1),
 ("### `L.voidfrac`", 1),
 ("### `L.box`", 1),
 ("### `L.bits`", 1),
 ("### `L.circuit`", 1),
 # NEW chat-59 discriminators headings =1
 ("### The language combinations", 1),
 ("### The detachable leaf", 1),
 ("### Why a closed expression exists", 1),
 ("### The alternating specialisation", 1),
 ("### Palindromic rank polynomial ⟺ self-dual", 1),
 # Old headings =0
 ("### `L.comb`", 0),
 ("### `L.Fm1`", 0),
 ("### `L.pal`", 0),
 ("F(-1) counts the difference", 0),
 # Residuals
 ("`L.Fm1`", 2),
 ("`L.pal`", 1),
]
allpass=True
for name,exp in checks:
    got=c(name)
    ok=got==exp
    allpass&=ok
    print(f"{'PASS' if ok else 'FAIL'}  [{name[:55]}]: got {got} exp {exp}")
print("\nCOMPENDIA ALL PASS" if allpass else "\nCOMPENDIA HAS FAILURES")