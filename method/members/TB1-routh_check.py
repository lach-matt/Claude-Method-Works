# DELIVERY INSTRUMENT (new, thin). Object 7: the L4/L5 threshold was CITED in the record (Routh 1875), never computed.
# Routh's critical mass ratio: mu_1 = (1 - sqrt(1 - 4/27... )) closed form (9 - sqrt(69))/18.
import math
mu=(9-math.sqrt(69))/18
print(f"Routh mu_1 = (9-sqrt(69))/18 = {mu:.10f}; record prints 0.0385209; agree to 1e-7: {abs(mu-0.0385209)<1e-7}")
