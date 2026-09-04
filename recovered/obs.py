print("  IS EVERY UNFIXABLE CELL AN EXPECTATION VALUE?\n")
print("      test: for each closed index, name what the closure could NOT fix,")
print("      and ask whether it is ⟨Ψ|Ô|Ψ⟩ for some operator Ô.\n")
T=[("Λ","which transfers are admissible","the transfer q's SIZE",
    "⟨Ψ|Ĥ|Ψ⟩ difference","YES"),
   ("Λ_spectra","which channels exist","δ itself",
    "the phase shift = ⟨Ψ|V−V_C|Ψ⟩","YES"),
   ("Λ_law","which laws in which carrier","each law's coefficient",
    "varies by law","MIXED"),
   ("Λ_const","role × carrier of each constant","the constant's VALUE",
    "M, σ, h₀ — all amplitudes","YES"),
   ("Λ_var","body × role of each variable","δ, the single output",
    "the phase shift","YES"),
   ("Λ_ryd","order × ℓ × sign","δ₀ and δ₂",
    "Ritz coefficients = ⟨Ψ|r^-k|Ψ⟩ moments","YES"),
   ("Λ_charge","role × carrier × sign × regime","the decay RATE x",
    "screening = ⟨Ψ|1/r_ij|Ψ⟩ averaged","YES"),
   ("Λ_cross","Δn × ℓ_g","NOTHING — the value is (Δn)/(√pᵣ−√p_g)",
    "no operator: a node count","NO"),
   ("Λ_descent","c × regime","a(c)",
    "F⁰ and G² = ⟨Ψ|1/r₁₂|Ψ⟩","YES"),
   ("Λ_phys","source × domain","each parameter's magnitude",
    "mostly expectation values","YES"),
   ("Λ_amp","sequence × kind × ℓ","F_i and G_i themselves",
    "⟨Ψ|1/r₁₂|Ψ⟩ by definition","YES")]
print(f"      {'index':<12}{'the closure fixes':<34}{'it cannot fix':<32}{'observable?'}")
for a,b,c,d,e in T:
    print(f"      {a:<12}{b:<34}{c:<32}{e}")
print()
n=sum(1 for x in T if x[4]=="YES")
print(f"      {n} of {len(T)} unfixable quantities are expectation values.")
print(f"      1 is not: Λ_cross, whose value is a node count.")
print(f"      1 is mixed: Λ_law, which holds laws of both kinds.\n")
print("  AND THE EXCEPTION IS THE POINT\n")
print("      Λ_cross is the ONLY index whose unfixable cell is fixed anyway —")
print("      because (Δn)/(√pᵣ − √p_g) needs no measurement. it is counting.")
print()
print("      that is also the only index with NO statistics language.")
print("      the two facts are the same fact.\n")
print("  THE STATEMENT\n")
print("      an index closes when its cells are enumerable. what it cannot")
print("      supply is exactly what requires an operator — and the compendium's")
print("      own language test detects this: the statistics language is silent")
print("      precisely where no observation is needed.")
print()
print("      so the boundary the Löwdin work hit is not a limit of the method.")
print("      it is the boundary between the state space and the observable, and")
print("      the method located it by noticing which language fell silent.")
print()
print("  WHAT THIS PREDICTS\n")
print("      any future index whose unfixable cell is NOT an expectation value")
print("      should also lack a statistics language. that is falsifiable, and")
print("      Λ_cross is the only confirming instance we hold — one case.")