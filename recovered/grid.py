import math
from itertools import product
SUBJ=["amplitude","validity","exponent","floor","threshold"]
CARR=["u = ln(Nₑ/c^⅔)","p","ℓ − ℓ_core","Z − T","Nₑ"]
HELD={("amplitude","u = ln(Nₑ/c^⅔)"):"law 1 · Gaussian, M/u₀/σ",
      ("validity","u = ln(Nₑ/c^⅔)"):"law 2 · spread = 0.113(u−2.5)",
      ("exponent","Nₑ"):"law 3 · x = C/√Nₑ, C = 1.32",
      ("floor","p"):"law 4 · ⌊δ⌋ = p − min(p,max(2−ℓ,0))",
      ("threshold","ℓ − ℓ_core"):"law 5 · gate, frac(δ)≈0 at ≥2",
      ("threshold","Z − T"):"law 6 · switch, σ((Z−T+1.5)/0.40)",
      ("amplitude","Z − T"):"law 6b · h(d)=0.40, h(f)=0.468"}
def admissible(s,c):
    """which (subject, carrier) pairs the physics allows at all"""
    if s=="floor":     return c in ("p",)                      # an integer count only
    if s=="exponent":  return c in ("Nₑ","u = ln(Nₑ/c^⅔)")     # a scaling variable
    if s=="threshold": return c in ("ℓ − ℓ_core","Z − T","p")  # something crossable
    return True                                                 # amplitude, validity: any
print("  THE (SUBJECT × CARRIER) GRID\n")
print(f"      {'':<11}" + "".join(f"{c[:13]:>15}" for c in CARR))
occ=0; adm=0; empty=[]
for s in SUBJ:
    row=f"      {s:<11}"
    for c in CARR:
        if not admissible(s,c): row+=f"{'—':>15}"
        else:
            adm+=1
            if (s,c) in HELD: row+=f"{'HELD':>15}"; occ+=1
            else: row+=f"{'.':>15}"; empty.append((s,c))
    print(row)
print(f"\n      admissible {adm} · held {occ} · empty {adm-occ}\n")
print("  THE EMPTY ADMISSIBLE CELLS — what each would be\n")
WHAT={
 ("amplitude","p"):"how big δ is per core shell, at fixed u — we assume √p exactly",
 ("amplitude","ℓ − ℓ_core"):"how big the defect is as a function of the gate variable",
 ("amplitude","Nₑ"):"amplitude against raw electron count — subsumed by u?",
 ("validity","p"):"where δ = a√p stops holding as p grows",
 ("validity","ℓ − ℓ_core"):"where the gate's binary reading stops holding",
 ("validity","Z − T"):"where the switch's logistic shape stops holding — LAW 6's PARTNER",
 ("validity","Nₑ"):"where the whole form stops holding in electron count",
 ("exponent","u = ln(Nₑ/c^⅔)"):"is the charge exponent itself a function of u?",
 ("threshold","p"):"a threshold in the core count — p = 0 vs p ≥ 1 IS one",
}
for s,c in empty:
    print(f"      {s:<11}× {c:<18}{WHAT.get((s,c),'—')}")
print()
print("  AND THE ONE THE LATTICE ASKED FOR\n")
print("      validity × (Z − T) is law 6's partner exactly as law 2 is law 1's.")
print("      Law 2 was found by asking where √p stops holding, and it turned out")
print("      to be a linear law in the same carrier. The same question for the")
print("      collapse switch: where does σ((Z−T+1.5)/0.40) stop holding, and is")
print("      that a law in Z−T?\n")
print("      we hold 18 collapsed and 142 uncollapsed channels — enough to ask.")
print()
print("  IF THE GRID FILLED, WHAT WOULD E BE?\n")
print(f"      a full {len(SUBJ)}×{len(CARR)} product is {len(SUBJ)*len(CARR)} cells;")
print(f"      the admissibility rule refuses {len(SUBJ)*len(CARR)-adm}, leaving {adm}.")
print(f"      that is the calendar's shape: a product minus a SYSTEMATIC refusal.")
print(f"      E would then be a statement about which laws imply which.")