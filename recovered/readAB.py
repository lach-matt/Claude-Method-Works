print("="*78)
print("READING A vs READING B — what each actually requires")
print("="*78)
print("""
READING A — a parallel occupied set inside the SAME lattice Λ.
  Λ_exc ⊆ Λ, cells reachable by excited configurations.
  Question: is Λ_exc an order ideal? all-or-nothing? how does it relate to Λ_g?
  STATUS: pursued. Result — Λ_exc = Λ_g under all three definitions tried.
  But those definitions all used the VALENCE cell only. There is a
  variant not yet tried: allow the excited valence electron to define a
  cell even when the resulting configuration is not any element's ground
  state, using HIGHER excitations (not just the lowest). Test below.

READING B — a DIFFERENT structure whose points are excited configurations.
  The obstruction I raised: an excited atom occupies several subshells at
  once, so it is not a point of Λ but a set of points.
  That obstruction is real but it does not block construction — it tells
  us the right object is a set-valued one. Two candidates:
    B1  occupancy VECTOR: v ∈ ℕ^25, one coordinate per (n,ℓ) column,
        with 0 ≤ v_(n,ℓ) ≤ 2(2ℓ+1) and Σ v = Z.
        This IS a product of chains — order structure guaranteed.
    B2  the configuration POSET: order configurations by "obtainable by
        promoting electrons upward", i.e. c ≤ c' iff c' is reachable from
        c by moving electrons to higher (n+ℓ). A different order entirely.
  Both are constructible. Test what each gives.
""")