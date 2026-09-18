window.__mi = window.__mi || {}; window.__mi.index = {
 "meta": {
  "title": "The Method Index",
  "subtitle": "The Method 1.6 · every element on every axis of every index",
  "built": "2026-09-18T17:03:58+00:00",
  "commit": "ef7b325d5e5b",
  "generator": "tools/webindex.py over tools/populate.py",
  "names_note": "Element names are IUPAC labels for search only; they are not a corpus figure. The corpus carries symbols (register 1306)."
 },
 "sources": [
  {
   "file": "method/members/LW1-ground.py",
   "role": "observed ground configurations, Z = 1 to 108 (register 1306, NIST ASD 5.12)",
   "md5_recorded": "236975ac23aa29960d4f7c2a4d200cd6",
   "md5_measured": "236975ac23aa29960d4f7c2a4d200cd6",
   "bundle": "BUILD180_compendia",
   "ok": true
  },
  {
   "file": "method/members/tower-2.py",
   "role": "the tower above Λ₈",
   "md5_recorded": "c0bce27abe23ad939d297ac1022a01d7",
   "md5_measured": "c0bce27abe23ad939d297ac1022a01d7",
   "bundle": "BUILD180_compendia",
   "ok": true
  },
  {
   "file": "drive/The Method Materials/COORDINATES-2_13.csv",
   "role": "the spectra index: (Z, charge, ℓ, mult) → a channel",
   "md5_recorded": "906d08be19630b6f824ec0164de11773",
   "md5_measured": "906d08be19630b6f824ec0164de11773",
   "drive_modified": "2026-08-24T00:13:30.694Z",
   "ok": true
  }
 ],
 "status_legend": {
  "READ": "a measurement, taken from a member or the mirror",
  "PINNED": "the corpus defines it at the precision a program needs",
  "DERIVED": "arithmetic on a READ or PINNED quantity, nothing added",
  "RECOVERED": "not stated in any member, but recovered by measurement from the index's own computed column and consistent with what the registers say about it qualitatively",
  "RECONSTRUCTED": "the corpus states the object and its behaviour but not the form a program needs; reconstructed here, measured, and kept as such so a later ruling can move it"
 },
 "axes": [
  {
   "axis": "Z",
   "status": "READ",
   "source": "the ground-state atomic number, the input"
  },
  {
   "axis": "symbol",
   "status": "READ",
   "source": "NIST ASD 5.12 via LW1-ground.py (register 1306)"
  },
  {
   "axis": "configuration",
   "status": "READ",
   "source": "observed ground shells, cores expanded"
  },
  {
   "axis": "level",
   "status": "READ",
   "source": "observed ground level"
  },
  {
   "axis": "n",
   "status": "DERIVED",
   "source": "principal quantum number, per occupied subshell"
  },
  {
   "axis": "l",
   "status": "DERIVED",
   "source": "azimuthal quantum number, per occupied subshell"
  },
  {
   "axis": "occupancy",
   "status": "DERIVED",
   "source": "electrons in the subshell"
  },
  {
   "axis": "capacity",
   "status": "PINNED",
   "source": "2(2l+1), Pauli exclusion (section 7.1)"
  },
  {
   "axis": "n+l",
   "status": "DERIVED",
   "source": "the Madelung/Janet coordinate (register 1188)"
  },
  {
   "axis": "period",
   "status": "DERIVED",
   "source": "the drawn eighteen-column layout (section 6)"
  },
  {
   "axis": "group",
   "status": "DERIVED",
   "source": "the same layout; None where set aside"
  },
  {
   "axis": "block",
   "status": "DERIVED",
   "source": "l of the differentiating electron"
  },
  {
   "axis": "janet cell",
   "status": "DERIVED",
   "source": "(n+l, l) of the differentiating electron; E = 0"
  },
  {
   "axis": "charge",
   "status": "READ",
   "source": "spectroscopic stage; 1 is neutral"
  },
  {
   "axis": "Ne",
   "status": "DERIVED",
   "source": "electron count of the ion, Z - charge + 1"
  },
  {
   "axis": "p",
   "status": "PINNED",
   "source": "the core's orbital count at this l (register 1141)"
  },
  {
   "axis": "n0",
   "status": "RECONSTRUCTED",
   "source": "first entirely unoccupied n at this l; see n0_of"
  },
  {
   "axis": "B",
   "status": "PINNED",
   "source": "min(p, n0-l-1), the Pauli bound (register 1141)"
  },
  {
   "axis": "delta measured",
   "status": "READ",
   "source": "COORDINATES-2.13, grade measured/exact"
  },
  {
   "axis": "delta equation",
   "status": "PINNED",
   "source": "the channel equation, final form (register 1205)"
  },
  {
   "axis": "C(Z)",
   "status": "RECOVERED",
   "source": "the collapse coordinate, inverted out of COORDINATES-2.13's computed column (registers 1188-1190); see collapse_C"
  },
  {
   "axis": "witness",
   "status": "READ",
   "source": "COORDINATES-2.13"
  },
  {
   "axis": "bound",
   "status": "READ",
   "source": "COORDINATES-2.13"
  },
  {
   "axis": "Lambda_8 cell",
   "status": "RECONSTRUCTED",
   "source": "the ionisation ladder as transitions; see ionisation_cells"
  },
  {
   "axis": "caps",
   "status": "PINNED",
   "source": "section 7.4's (n,e,l,k,f) = (3,3,1,3,1)"
  }
 ],
 "caps": {
  "n": 3,
  "e": 3,
  "l": 1,
  "f": 1,
  "k": 3
 },
 "lambda_coords": [
  "n",
  "l",
  "k",
  "q",
  "e",
  "f",
  "g",
  "2S"
 ],
 "lambda_meaning": {
  "n": "source shell",
  "l": "source subshell",
  "k": "source occupancy",
  "q": "electrons removed",
  "e": "target shell",
  "f": "target subshell",
  "g": "target occupancy",
  "2S": "multiplicity"
 },
 "closure": {
  "index": "periodic table (period × group), section 6",
  "operator": "ℛ, the PINNED order operator of section 32.4.1 (tools/cypher.py)",
  "held": 90,
  "admitted": 126,
  "E": 36,
  "denied": [
   [
    1,
    2
   ],
   [
    1,
    3
   ],
   [
    1,
    4
   ],
   [
    1,
    5
   ],
   [
    1,
    6
   ],
   [
    1,
    7
   ],
   [
    1,
    8
   ],
   [
    1,
    9
   ],
   [
    1,
    10
   ],
   [
    1,
    11
   ],
   [
    1,
    12
   ],
   [
    1,
    13
   ],
   [
    1,
    14
   ],
   [
    1,
    15
   ],
   [
    1,
    16
   ],
   [
    1,
    17
   ],
   [
    2,
    3
   ],
   [
    2,
    4
   ],
   [
    2,
    5
   ],
   [
    2,
    6
   ],
   [
    2,
    7
   ],
   [
    2,
    8
   ],
   [
    2,
    9
   ],
   [
    2,
    10
   ],
   [
    2,
    11
   ],
   [
    2,
    12
   ],
   [
    3,
    3
   ],
   [
    3,
    4
   ],
   [
    3,
    5
   ],
   [
    3,
    6
   ],
   [
    3,
    7
   ],
   [
    3,
    8
   ],
   [
    3,
    9
   ],
   [
    3,
    10
   ],
   [
    3,
    11
   ],
   [
    3,
    12
   ]
  ],
  "set_aside": 28
 },
 "collapse": {
  "Z0": {
   "1": 5,
   "2": 21,
   "3": 57
  },
  "width": 8.0,
  "status": "RECOVERED",
  "form": "C(Z, ℓ) = clamp(0.5 + (Z − Z₀(ℓ)) / 8, 0, 1)"
 },
 "equation": {
  "A": 0.3772,
  "K": 0.4942,
  "H": 0.5415,
  "E0": 0.8297,
  "E1": 0.09,
  "form": [
   "delta = a p^e(Ne) Ne^k ln(c+1)/c                  where p > 0",
   "delta = h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c         where p = 0"
  ],
  "exponent": "e(Ne) = E0 - E1 ln Ne",
  "status": "PINNED",
  "source": "register 1205, final form"
 },
 "instruments": {
  "channel_delta": {
   "python": "def channel_delta(Z, charge, l, table=\"observed\"):\n    \"\"\"delta for a Rydberg channel, register 1205's standing form.\n\n        delta = a p^e(Ne) Ne^k ln(c+1)/c                  where p > 0\n        delta = h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c         where p = 0\n\n    Ne is the electron count of the ION and c its spectroscopic charge, so a\n    neutral atom is c = 1 and the core it presents is singly charged.\n\n    Register 5193 records that at Ne = 1 the (Ne-1)/Ne factor vanishes\n    identically for every charge and every C(Z), which is what makes a\n    one-electron ion return exactly zero -- the hydrogenic case, and not a\n    fitted one.\"\"\"\n    Ne = Z - charge + 1\n    c = charge\n    if Ne < 1 or c < 1:\n        return None\n    core = Ne - 1\n    p = core_p(core, l, table) if core >= 1 else 0\n    if p is None:\n        return None\n    charge_factor = math.log(c + 1) / c\n    if p > 0:\n        e = E0 - E1 * math.log(Ne)\n        return A_COEFF * (p ** e) * (Ne ** K_COEFF) * charge_factor\n    return (H_COEFF * collapse_C(Z, l) * ((Ne - 1) / Ne)\n            * (Ne ** K_COEFF) * charge_factor)\n",
   "file": "tools/populate.py",
   "line": 300,
   "status": "PINNED",
   "source": "the channel equation, final form (register 1205); its p = 0 branch carries the RECOVERED collapse ramp C(Z)"
  },
  "collapse_C": {
   "python": "def collapse_C(Z, l):\n    \"\"\"C(Z), the collapse coordinate across the Janet boundary.\n\n        C(Z, l) = clamp( 0.5 + (Z - Z0(l)) / 8, 0, 1 )\n\n    RECOVERED, not reconstructed. No member states the form: register 1190 says\n    only that it is \"read off the periodic table, not fitted -- one lookup\".\n    But COORDINATES-2.13's own computed column is generated by this equation,\n    so C can be INVERTED out of it, and it comes back exact:\n\n        l = 2:  C = 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000\n                at Z =  18,   19,    20,    21,    22,    23,    24,    25\n        l = 3:  the same eight values at Z = 54 to 61\n        l = 1:  the same eight values at Z =  2 to  9\n\n    A linear ramp eight wide, reaching exactly 0.5 at the Janet boundary and\n    saturating four beyond it. That is register 1189 in closed form -- \"the\n    collapse is a rapid transition, NOT A STEP\" -- and it is why Ca I nd is\n    0.908 at Z = 20, below the threshold: C(20, 2) = 0.375, already a third of\n    the way up the ramp. An indicator would have made it zero.\n\n    Above l = 3 there is no collapse and C is zero, which the index agrees\n    with: every l >= 4 channel inverts to C = 0 exactly.\"\"\"\n    z0 = COLLAPSE_Z.get(l)\n    if z0 is None:\n        return 0.0\n    return min(1.0, max(0.0, 0.5 + (Z - z0) / COLLAPSE_WIDTH))\n",
   "file": "tools/populate.py",
   "line": 271,
   "status": "RECOVERED",
   "source": "C(Z, l), the collapse coordinate, inverted out of COORDINATES-2.13's computed column (registers 1188 to 1190); no member states its form"
  },
  "pauli_bound": {
   "python": "def pauli_bound(Z, charge, l, config=None):\n    \"\"\"B = min(p, n0 - l - 1). Register 1141, Pauli 1925, Janet 1929.\"\"\"\n    core = Z - charge\n    if core < 1:\n        return 0\n    if config is not None:\n        occ = {(n, ll): o for n, ll, o in config}\n        p = sum(1 for n, ll, o in config if ll == l and o > 0)\n        n = l + 1\n        while occ.get((n, l), 0) > 0:\n            n += 1\n    else:\n        p = core_p(core, l)\n        n = n0_of(core, l)\n        if p is None or n is None:\n            return None\n    return max(0, min(p, n - l - 1))\n",
   "file": "tools/populate.py",
   "line": 234,
   "status": "PINNED",
   "source": "B = min(p, n0 - l - 1), the Pauli bound (register 1141)"
  },
  "core_p": {
   "python": "def core_p(core_Ne, l, table=\"observed\"):\n    \"\"\"p, the core's orbital count at this l, from the OBSERVED ground\n    configuration of the core (register 1306).\"\"\"\n    cfg = config_of(core_Ne, table)\n    if cfg is None:\n        return None\n    return sum(1 for _n, ll, o in cfg if ll == l and o > 0)\n",
   "file": "tools/populate.py",
   "line": 206,
   "status": "PINNED",
   "source": "p, the core's orbital count at this l, from the observed ground configuration of the core (registers 1141, 1306)"
  },
  "n0_of": {
   "python": "def n0_of(core_Ne, l, table=\"observed\"):\n    \"\"\"n0, the first Pauli-allowed n.\n\n    RECONSTRUCTED. Register 1141 states the bound and names its two terms; it\n    does not say whether a PARTIALLY filled subshell counts as allowed. Both\n    readings were measured against COORDINATES-2.13's own B column: \"first n\n    with room\" matches 87.0% of 102,871 rows, \"first ENTIRELY UNOCCUPIED n\"\n    matches 97.7%. He I ns settles it -- the core is 1s(1), the CSV gives B = 1,\n    and only the second reading returns 1.\"\"\"\n    cfg = config_of(core_Ne, table)\n    if cfg is None:\n        return None\n    occ = {(n, ll): o for n, ll, o in cfg}\n    n = l + 1\n    while occ.get((n, l), 0) > 0:\n        n += 1\n    return n\n",
   "file": "tools/populate.py",
   "line": 215,
   "status": "RECONSTRUCTED",
   "source": "n0, the first entirely unoccupied n at this l; register 1141 names the term but not the reading, and He I ns settles it"
  },
  "lambda_constraints": {
   "python": "def lambda_constraints(cell):\n    \"\"\"Section 7.1's seven constraints, four origins. PINNED.\"\"\"\n    n, l, k, q, e, f, g, S2 = cell\n    return [\n        (\"l <= n-1\", l <= n - 1, \"hydrogenic radial solution\"),\n        (\"k <= 2(2l+1)\", k <= 2 * (2 * l + 1), \"Pauli exclusion\"),\n        (\"q <= k\", q <= k, \"counting\"),\n        (\"f <= e-1\", f <= e - 1, \"hydrogenic radial solution\"),\n        (\"g <= 2(2f+1)\", g <= 2 * (2 * f + 1), \"Pauli exclusion\"),\n        (\"g <= q\", g <= q, \"counting\"),\n        (\"2S <= k\", S2 <= k, \"vector coupling (an envelope)\"),\n    ]\n",
   "file": "tools/populate.py",
   "line": 384,
   "status": "PINNED",
   "source": "section 7.1's seven constraints, four origins"
  },
  "caps_needed": {
   "python": "def caps_needed(cell):\n    n, l, k, q, e, f, g, _S2 = cell\n    return dict(n=n, e=e, l=l, f=f, k=k)\n",
   "file": "tools/populate.py",
   "line": 398,
   "status": "PINNED",
   "source": "the caps a Lambda_8 cell needs, read against section 7.4's (n, e, l, k, f) = (3, 3, 1, 3, 1); the cell it is applied to is the RECONSTRUCTED ionisation-ladder mapping and carries its own status"
  },
  "within_caps": {
   "python": "def within_caps(cell, caps=CAPS):\n    need = caps_needed(cell)\n    return {ax: need[ax] <= caps[ax] for ax in caps}\n",
   "file": "tools/populate.py",
   "line": 403,
   "status": "PINNED",
   "source": "section 7.4's standing caps; a cell outside them is reported OUTSIDE, never truncated"
  },
  "op_order": {
   "python": "def op_order(ix, opts):\n    \"\"\"R, §32.4.1. R(X) = {x in box : x_i <= phi_ij(x_j) for all i != j},\n    phi_ij(a) = max{y_i : y in X, y_j <= a}. Matches the seated instrument rclose.py.\"\"\"\n    if ix.d < 2:\n        return None, \"R needs at least two coordinates\"\n    X, D = ix.cells, ix.d\n    phi = {}\n    for i in range(D):\n        for j in range(D):\n            if i == j:\n                continue\n            for a in ix.alphabets[j]:\n                cand = [y[i] for y in X if y[j] <= a]\n                phi[(i, j, a)] = max(cand) if cand else None\n    out = set()\n    for x in ix.ambient():\n        good = True\n        for i in range(D):\n            for j in range(D):\n                if i == j:\n                    continue\n                p = phi[(i, j, x[j])]\n                if p is None or x[i] > p:\n                    good = False\n                    break\n            if not good:\n                break\n        if good:\n            out.add(x)\n    return out, \"staircase closure over the ambient product\"\n",
   "file": "tools/cypher.py",
   "line": 119,
   "status": "PINNED",
   "source": "R, the order operator of section 32.4.1; matches the seated instrument rclose.py"
  },
  "lowdin_construction": {
   "python": null,
   "file": "method/members/THE-LOWDIN-SOLUTION-2.md",
   "status": "READ",
   "held": false,
   "source": "the scalar-relativistic construction is not held; the paper's own statement, register 1706 and the SCF audit are shown in its place",
   "text": "Executed across the entire table with the inverse fine-structure constant c = 137.035999 as the only number supplied, the construction reproduces the observed filling order at all 107 elements for which ground configurations are known (Z = 2–108), locates the three genuine exceptions to the secondary rule exactly where nature has them and derives them from the physics of orbital collapse, proves that no g block exists anywhere below Z = 121, and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them.\n\nFinally, one physical constant is admitted, because the atom itself admits it: the speed of light, entering through the scalar-relativistic reduction of the Dirac equation as c = 137.035999 in Hartree atomic units.\n\n*(Relativistic clause.) The law is scalar-relativistic in an essential way: repeating the entire construction with c → ∞ changes the entrant channel at eleven elements, and inverts the underlying channel competition at thorium besides.\n\nRegister 1706: **ELEVEN ELEMENTS SEPARATE THE TABLE FROM ITS NON-RELATIVISTIC COUNTERFACTUAL.** *The identical walk at c → ∞ (Λ_cinf, 107 rows) disagrees with Λ_chain at Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — 4s for 3d at manganese and zinc, 5s for 4d at silver and cadmium, 5d for 4f across four lanthanides, 6s for 5d at mercury, the heavy actinides wrongly altogether. The relativistic walk scores 107/107, so all eleven are errors of the equation-without-light against nature; the thorium competition inverts besides, though its entrant survives by path.* **The wall chart is not a solution of the non-relativistic Schrödinger equation. Quarantine standing: Λ_cinf is contrast, never data.**\n\nr2-scf.out: 1706 / L9773 eleven elements listed: 11 | 1706's groups 2 (Mn, Zn) + 2 (Ag, Cd) + 4 lanthanides (Nd, Pm, Sm, Lu) + 1 (Hg) + 2 heavy actinides (Lr, Rf) = 11\n\nUNREPRODUCIBLE with that budget (record-carried, never withdrawn): 107/107 · 65/70/57/28 · +1.33 +1.24 +2.6 [2.57-2.73] +2.2 [1.92-3.32] +2.16 · >= 26x · the eleven · 0.058-0.264 · 0.083 · 2.6e-15 · 0.999992 · 1.000103 · +1.7e-7 · +6.1e-9 · 0.98 · 1.00 · Z = 91 sign · Dirac-Fock to 120"
  }
 },
 "relativistic": {
  "status": "READ",
  "c": 137,
  "statement": "Executed across the entire table with the inverse fine-structure constant c = 137.035999 as the only number supplied, the construction reproduces the observed filling order at all 107 elements for which ground configurations are known (Z = 2–108), locates the three genuine exceptions to the secondary rule exactly where nature has them and derives them from the physics of orbital collapse, proves that no g block exists anywhere below Z = 121, and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them.",
  "construction": "Finally, one physical constant is admitted, because the atom itself admits it: the speed of light, entering through the scalar-relativistic reduction of the Dirac equation as c = 137.035999 in Hartree atomic units.",
  "eleven": [
   {
    "symbol": "Mn",
    "Z": 25,
    "configuration": "[Ar]3d5 4s2",
    "entrant": "4s"
   },
   {
    "symbol": "Zn",
    "Z": 30,
    "configuration": "[Ar]3d10 4s2",
    "entrant": "4s"
   },
   {
    "symbol": "Ag",
    "Z": 47,
    "configuration": "[Kr]4d10 5s",
    "entrant": "5s"
   },
   {
    "symbol": "Cd",
    "Z": 48,
    "configuration": "[Kr]4d10 5s2",
    "entrant": "5s"
   },
   {
    "symbol": "Nd",
    "Z": 60,
    "configuration": "[Xe]4f4 6s2",
    "entrant": "4f"
   },
   {
    "symbol": "Pm",
    "Z": 61,
    "configuration": "[Xe]4f5 6s2",
    "entrant": "4f"
   },
   {
    "symbol": "Sm",
    "Z": 62,
    "configuration": "[Xe]4f6 6s2",
    "entrant": "4f"
   },
   {
    "symbol": "Lu",
    "Z": 71,
    "configuration": "[Xe]4f14 5d 6s2",
    "entrant": "5d"
   },
   {
    "symbol": "Hg",
    "Z": 80,
    "configuration": "[Xe]4f14 5d10 6s2",
    "entrant": "6s"
   },
   {
    "symbol": "Lr",
    "Z": 103,
    "configuration": "[Rn]5f14 7s2 7p",
    "entrant": "7p"
   },
   {
    "symbol": "Rf",
    "Z": 104,
    "configuration": "[Rn]5f14 6d2 7s2",
    "entrant": "6d"
   }
  ],
  "thorium": "*(Relativistic clause.) The law is scalar-relativistic in an essential way: repeating the entire construction with c → ∞ changes the entrant channel at eleven elements, and inverts the underlying channel competition at thorium besides.",
  "sources": {
   "paper": {
    "file": "method/members/THE-LOWDIN-SOLUTION-2.md",
    "eleven_line": 156,
    "construction_line": 27,
    "thorium_line": 45
   },
   "register": {
    "entry": 1706,
    "text": "**ELEVEN ELEMENTS SEPARATE THE TABLE FROM ITS NON-RELATIVISTIC COUNTERFACTUAL.** *The identical walk at c → ∞ (Λ_cinf, 107 rows) disagrees with Λ_chain at Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — 4s for 3d at manganese and zinc, 5s for 4d at silver and cadmium, 5d for 4f across four lanthanides, 6s for 5d at mercury, the heavy actinides wrongly altogether. The relativistic walk scores 107/107, so all eleven are errors of the equation-without-light against nature; the thorium competition inverts besides, though its entrant survives by path.* **The wall chart is not a solution of the non-relativistic Schrödinger equation. Quarantine standing: Λ_cinf is contrast, never data.**"
   },
   "scf_audit": {
    "file": "method/members/r2-scf.out",
    "count": "1706 / L9773 eleven elements listed: 11 | 1706's groups 2 (Mn, Zn) + 2 (Ag, Cd) + 4 lanthanides (Nd, Pm, Sm, Lu) + 1 (Hg) + 2 heavy actinides (Lr, Rf) = 11",
    "entrants": [
     {
      "symbol": "Mn",
      "Z": 25,
      "configuration": "[Ar]3d5 4s2",
      "entrant": "4s"
     },
     {
      "symbol": "Zn",
      "Z": 30,
      "configuration": "[Ar]3d10 4s2",
      "entrant": "4s"
     },
     {
      "symbol": "Ag",
      "Z": 47,
      "configuration": "[Kr]4d10 5s",
      "entrant": "5s"
     },
     {
      "symbol": "Cd",
      "Z": 48,
      "configuration": "[Kr]4d10 5s2",
      "entrant": "5s"
     },
     {
      "symbol": "Nd",
      "Z": 60,
      "configuration": "[Xe]4f4 6s2",
      "entrant": "4f"
     },
     {
      "symbol": "Pm",
      "Z": 61,
      "configuration": "[Xe]4f5 6s2",
      "entrant": "4f"
     },
     {
      "symbol": "Sm",
      "Z": 62,
      "configuration": "[Xe]4f6 6s2",
      "entrant": "4f"
     },
     {
      "symbol": "Lu",
      "Z": 71,
      "configuration": "[Xe]4f14 5d 6s2",
      "entrant": "5d"
     },
     {
      "symbol": "Hg",
      "Z": 80,
      "configuration": "[Xe]4f14 5d10 6s2",
      "entrant": "6s"
     },
     {
      "symbol": "Lr",
      "Z": 103,
      "configuration": "[Rn]5f14 7s2 7p",
      "entrant": "7p"
     },
     {
      "symbol": "Rf",
      "Z": 104,
      "configuration": "[Rn]5f14 6d2 7s2",
      "entrant": "6d"
     }
    ]
   }
  },
  "instrument": {
   "held": false,
   "note": "the scalar-relativistic construction and its c -> inf repetition are not held; the figures are record-carried",
   "readme_rows": [
    "| 1, 2, 4, 5, 6, 7, 8, 10 | PENDING BANK | LOWDIN-HANDOFF-103.tgz (sha256 05ea7bd5…, 1870 sealed files, root c6bcdd21) — the last sealed archive; awaiting upload to the Löwdin chat |",
    "| 9 (1707–1711) | PENDING BANK (packs 93–103) + NOT HELD (S104 restatement w104.py) | see note on S104 |",
    "| 11 six figures | NOT HELD as files unless M supplies S104 outputs | fig1–6.py and the PNGs were archived in pack104, never sealed (see note) |",
    "  the query itself is NOT HELD. The file's own fields are: ground shells as printed, ground level,"
   ],
   "budget": "UNREPRODUCIBLE with that budget (record-carried, never withdrawn): 107/107 · 65/70/57/28 · +1.33 +1.24 +2.6 [2.57-2.73] +2.2 [1.92-3.32] +2.16 · >= 26x · the eleven · 0.058-0.264 · 0.083 · 2.6e-15 · 0.999992 · 1.000103 · +1.7e-7 · +6.1e-9 · 0.98 · 1.00 · Z = 91 sign · Dirac-Fock to 120"
  }
 },
 "limits": {
  "status": {
   "note": "READ",
   "kind": "DERIVED"
  },
  "source": "COORDINATES-2.13, bound column",
  "rules": [
   {
    "kind": "ionisation-limit",
    "regex": "^limit [0-9.]+;",
    "meaning": "a series limit the csv prints for the channel (one electron outside a closed shell); the value is shown as printed, no unit added"
   },
   {
    "kind": "unresolved",
    "regex": "^series unresolved",
    "meaning": "the series is unresolved above the stated n in any published analysis"
   },
   {
    "kind": "nuclear",
    "regex": "^no (long-lived|primordial) isotope|^no nuclide synthesised",
    "meaning": "a nuclear limit: no long-lived or primordial isotope, or no nuclide synthesised"
   },
   {
    "kind": "term",
    "regex": "^not keyable",
    "meaning": "no single 2S+1 keys the channel (hole plus electron, or multi-valence)"
   },
   {
    "kind": "coupling",
    "regex": "^open-shell core",
    "meaning": "an open-shell core with the stated number of parents"
   },
   {
    "kind": "no-analysis",
    "regex": "^no analysis located|^none \\u2014 separable",
    "meaning": "no analysis located at this charge, or a separable series simply not yet measured; NOT a bound on existence, as the note says"
   },
   {
    "kind": "symmetry",
    "regex": "^derived by symmetry",
    "meaning": "delta = 0 by symmetry; no measurement required"
   },
   {
    "kind": "none",
    "regex": "^-$",
    "meaning": "the csv carries no note"
   }
  ],
  "kinds": [
   {
    "kind": "ionisation-limit",
    "count": 25
   },
   {
    "kind": "unresolved",
    "count": 28526
   },
   {
    "kind": "nuclear",
    "count": 27821
   },
   {
    "kind": "term",
    "count": 17626
   },
   {
    "kind": "coupling",
    "count": 26641
   },
   {
    "kind": "no-analysis",
    "count": 2931
   },
   {
    "kind": "symmetry",
    "count": 929
   },
   {
    "kind": "none",
    "count": 333
   }
  ],
  "notes": [
   {
    "note": "series unresolved above ng in any published analysis",
    "kind": "unresolved",
    "count": 28526
   },
   {
    "note": "no long-lived isotope",
    "kind": "nuclear",
    "count": 24312
   },
   {
    "note": "not keyable: no single 2S+1 (hole+electron or multi-valence)",
    "kind": "term",
    "count": 17626
   },
   {
    "note": "open-shell core, 16 parents",
    "kind": "coupling",
    "count": 11605
   },
   {
    "note": "open-shell core, 3 parents",
    "kind": "coupling",
    "count": 9756
   },
   {
    "note": "open-shell core, 119 parents",
    "kind": "coupling",
    "count": 5280
   },
   {
    "note": "no analysis located at this charge (NOT a bound on existence)",
    "kind": "no-analysis",
    "count": 2691
   },
   {
    "note": "no nuclide synthesised; theoretically admitted — Janet left-step, 8s(2) closes the eighth period at element 120",
    "kind": "nuclear",
    "count": 1760
   },
   {
    "note": "no nuclide synthesised; theoretically admitted — Janet left-step, 8s(1) opens element 119",
    "kind": "nuclear",
    "count": 1744
   },
   {
    "note": "derived by symmetry; no measurement required",
    "kind": "symmetry",
    "count": 929
   },
   {
    "note": "-",
    "kind": "none",
    "count": 333
   },
   {
    "note": "none — separable series, simply not yet measured",
    "kind": "no-analysis",
    "count": 240
   },
   {
    "note": "limit 41449.451; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 6
   },
   {
    "note": "no primordial isotope (R 1587)",
    "kind": "nuclear",
    "count": 5
   },
   {
    "note": "limit 31406.4677325; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 5
   },
   {
    "note": "limit 66928.04; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 3
   },
   {
    "note": "limit 49266.66; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 3
   },
   {
    "note": "limit 48278.48; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 2
   },
   {
    "note": "limit 48387.634; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 2
   },
   {
    "note": "limit 32848.872; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 2
   },
   {
    "note": "limit 46670.107; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 1
   },
   {
    "note": "limit 43762.6; one electron outside a closed shell",
    "kind": "ionisation-limit",
    "count": 1
   }
  ],
  "distinct_notes": 22,
  "unclassified": []
 },
 "figures": [
  {
   "file": "figures/FIG6relativisticvsnonrelativistic.png",
   "bytes": 110305,
   "md5": "7a328342a38f01358a160fc164047bf9",
   "md5_recorded": "7a328342a38f01358a160fc164047bf9",
   "ok": true,
   "archive": "drive/The Method Materials/The_Method_1_6_figures.zip",
   "caption": "Figure 5 of THE-LOWDIN-SOLUTION-2.md: the derived table at c = 137 against c -> inf",
   "status": "READ"
  }
 ],
 "fixtures": {
  "note": "computed at build with tools/populate.py's own functions, never typed in; a browser-side solver that cannot reproduce these must say so rather than print a result",
  "equation_report": {
   "grades": [
    "measured"
   ],
   "table": "observed",
   "channels": 358,
   "skipped": 0,
   "rms": 0.18094664873062427,
   "R2": 0.9655919926147233,
   "median_abs_error": 0.05871099417920789,
   "by_l": [
    {
     "l": 0,
     "n": 92,
     "rms": 0.1510484447616774
    },
    {
     "l": 1,
     "n": 81,
     "rms": 0.1956628448548384
    },
    {
     "l": 2,
     "n": 89,
     "rms": 0.17682026205474416
    },
    {
     "l": 3,
     "n": 59,
     "rms": 0.2515003802982241
    },
    {
     "l": 4,
     "n": 36,
     "rms": 0.013916158473755129
    },
    {
     "l": 5,
     "n": 1,
     "rms": 0.00013
    }
   ],
   "status": "PINNED",
   "note": "populate.equation_report over COORDINATES-2.13's measured rows; register 1205 records rms 0.1610, R2 0.9741 on a different sample of 284 channels, so the figures are not expected to match it exactly"
  },
  "closure": {
   "operator": "cypher.op_order, R (section 32.4.1)",
   "status": "PINNED",
   "periodic": {
    "held": 90,
    "admitted": 126,
    "E": 36,
    "index": "periodic table (period x group), section 6, the ninety main-table cells"
   },
   "janet": {
    "held": 19,
    "admitted": 19,
    "E": 0,
    "box": 32,
    "cells": [
     [
      1,
      0
     ],
     [
      2,
      0
     ],
     [
      3,
      0
     ],
     [
      3,
      1
     ],
     [
      4,
      0
     ],
     [
      4,
      1
     ],
     [
      5,
      0
     ],
     [
      5,
      1
     ],
     [
      5,
      2
     ],
     [
      6,
      0
     ],
     [
      6,
      1
     ],
     [
      6,
      2
     ],
     [
      7,
      0
     ],
     [
      7,
      1
     ],
     [
      7,
      2
     ],
     [
      7,
      3
     ],
     [
      8,
      1
     ],
     [
      8,
      2
     ],
     [
      8,
      3
     ]
    ],
    "index": "Janet (n+l x l): the distinct cells of the 108 elements LW1-ground.py carries"
   },
   "janet_cypher_fixture": {
    "held": 22,
    "admitted": 22,
    "E": 0,
    "box": 40,
    "index": "cypher.py's own Janet fixture, n = 1 to 7 and l < min(n, 4); its selftest records cells=22 box=40 E(order)=0. Not the elements' cells."
   }
  },
  "collapse_table": {
   "status": "RECOVERED",
   "form": "C(Z, l) = clamp(0.5 + (Z - Z0(l)) / 8, 0, 1)",
   "by_l": [
    {
     "l": 1,
     "Z0": 5,
     "rows": [
      {
       "Z": 1,
       "C": 0.0
      },
      {
       "Z": 2,
       "C": 0.125
      },
      {
       "Z": 3,
       "C": 0.25
      },
      {
       "Z": 4,
       "C": 0.375
      },
      {
       "Z": 5,
       "C": 0.5
      },
      {
       "Z": 6,
       "C": 0.625
      },
      {
       "Z": 7,
       "C": 0.75
      },
      {
       "Z": 8,
       "C": 0.875
      },
      {
       "Z": 9,
       "C": 1.0
      }
     ]
    },
    {
     "l": 2,
     "Z0": 21,
     "rows": [
      {
       "Z": 17,
       "C": 0.0
      },
      {
       "Z": 18,
       "C": 0.125
      },
      {
       "Z": 19,
       "C": 0.25
      },
      {
       "Z": 20,
       "C": 0.375
      },
      {
       "Z": 21,
       "C": 0.5
      },
      {
       "Z": 22,
       "C": 0.625
      },
      {
       "Z": 23,
       "C": 0.75
      },
      {
       "Z": 24,
       "C": 0.875
      },
      {
       "Z": 25,
       "C": 1.0
      }
     ]
    },
    {
     "l": 3,
     "Z0": 57,
     "rows": [
      {
       "Z": 53,
       "C": 0.0
      },
      {
       "Z": 54,
       "C": 0.125
      },
      {
       "Z": 55,
       "C": 0.25
      },
      {
       "Z": 56,
       "C": 0.375
      },
      {
       "Z": 57,
       "C": 0.5
      },
      {
       "Z": 58,
       "C": 0.625
      },
      {
       "Z": 59,
       "C": 0.75
      },
      {
       "Z": 60,
       "C": 0.875
      },
      {
       "Z": 61,
       "C": 1.0
      }
     ]
    }
   ]
  },
  "hydrogenic_zero": {
   "Z": 1,
   "charge": 1,
   "l": 0,
   "delta_equation": 0.0,
   "status": "PINNED",
   "source": "register 5193: at Ne = 1 the (Ne-1)/Ne factor vanishes identically"
  },
  "pauli": {
   "status": "PINNED",
   "source": "register 1141; populate.selftest's own pair",
   "rows": [
    {
     "label": "He I ns",
     "Z": 2,
     "charge": 1,
     "l": 0,
     "B": 1
    },
    {
     "label": "Be I ns",
     "Z": 4,
     "charge": 1,
     "l": 0,
     "B": 2
    }
   ]
  },
  "coefficient_roundtrip_sample": {
   "statuses": {
    "delta": "READ",
    "p": "PINNED",
    "Ne": "DERIVED",
    "C": "RECOVERED",
    "delta_equation": "PINNED"
   },
   "note": "the first 12 measured rows of COORDINATES-2.13 in (Z, charge, l, mult) order",
   "rows": [
    {
     "Z": 2,
     "charge": 1,
     "l": 0,
     "mult": 1,
     "delta": 0.1392,
     "p": 1,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.3682698534331113
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 0,
     "mult": 3,
     "delta": 0.2965,
     "p": 1,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.3682698534331113
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 1,
     "mult": 1,
     "delta": -0.0133,
     "p": 0,
     "Ne": 2,
     "C": 0.125,
     "delta_equation": 0.033042504910198466
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 2,
     "mult": 1,
     "delta": 0.0007,
     "p": 0,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.0
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 2,
     "mult": 3,
     "delta": 0.0014,
     "p": 0,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.0
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 3,
     "mult": 1,
     "delta": -0.001,
     "p": 0,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.0
    },
    {
     "Z": 2,
     "charge": 1,
     "l": 4,
     "mult": 1,
     "delta": -0.0014,
     "p": 0,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.0
    },
    {
     "Z": 3,
     "charge": 1,
     "l": 0,
     "mult": 2,
     "delta": 0.40455,
     "p": 1,
     "Ne": 3,
     "C": 0.0,
     "delta_equation": 0.44997715879258293
    },
    {
     "Z": 3,
     "charge": 1,
     "l": 1,
     "mult": 2,
     "delta": 0.0783,
     "p": 0,
     "Ne": 3,
     "C": 0.25,
     "delta_equation": 0.10766288064960394
    },
    {
     "Z": 3,
     "charge": 1,
     "l": 2,
     "mult": 2,
     "delta": 0.0021,
     "p": 0,
     "Ne": 3,
     "C": 0.0,
     "delta_equation": 0.0
    },
    {
     "Z": 3,
     "charge": 2,
     "l": 0,
     "mult": 1,
     "delta": 0.0744,
     "p": 1,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.2918469539187789
    },
    {
     "Z": 3,
     "charge": 2,
     "l": 0,
     "mult": 3,
     "delta": 0.1814,
     "p": 1,
     "Ne": 2,
     "C": 0.0,
     "delta_equation": 0.2918469539187789
    }
   ]
  }
 },
 "caveats": [
  {
   "id": "above-108",
   "text": "Elements above Z = 108 are not populated. LW1-ground.py stops at 108 because measurement does. COORDINATES-2.13 carries rows to Z = 120 and those are shown READ from the CSV with no configuration, equation or derived value behind them."
  },
  {
   "id": "b-aufbau",
   "text": "The spectra index's B column was built on a withdrawn configuration table (aufbau, patched by hand). Register 1306 corrected the configurations and COORDINATES-2.13 was never rebuilt on them. Where the observed table gives a different Pauli bound the site shows both and marks the disagreement."
  },
  {
   "id": "b-overloaded",
   "text": "25 measured rows carry a float in the B column: a dispersion of the median defect, not a bound. The site says 'B column is not a bound here' on those rows rather than comparing an integer against a spread."
  },
  {
   "id": "lambda8-mapping",
   "text": "A Λ₈ cell is a transition, so an element is not a cell. The mapping shown is the element's own ionisation ladder read off the observed configurations. Nothing in the store fixes this mapping; it is RECONSTRUCTED and a later ruling can move it."
  },
  {
   "id": "equation-domain",
   "text": "The channel equation is validated in its stated domain and extrapolated outside it. A residual on a channel outside that domain is not a finding against the equation."
  },
  {
   "id": "relativistic-not-held",
   "text": "The scalar-relativistic construction (Koelling–Harmon Hartree–Fock at c = 137) and its repetition at c → ∞ are not held: the Löwdin delivery records objects 1, 2, 4–8 and 10 as pending bank and object 11 as not held, because session 104 was never sealed. The eleven displaced elements are READ from THE-LOWDIN-SOLUTION-2.md and register 1706, record-carried and never withdrawn (r2-scf), and the site cannot recompute them."
  },
  {
   "id": "limit-kind",
   "text": "A limit kind is a classification of the csv's own bound note by the stated rule: the note is READ, the kind is DERIVED, and the rule is shown beside it. 'no analysis located' is, as the note itself says, not a bound on existence; a series limit is printed as the csv prints it, with no unit added."
  },
  {
   "id": "n0-reading",
   "text": "n₀'s reading is RECONSTRUCTED. Register 1141 names the terms of B = min(p, n₀ − ℓ − 1) but not whether a partially filled subshell counts; 'first entirely unoccupied n' matches the column at 97.7 % and He I settles it."
  }
 ],
 "totals": {
  "rows": 104832,
  "measured": 358,
  "exact": 929,
  "computed": 103545,
  "witnessed": 358,
  "populated": 108,
  "csv_only": 12
 },
 "layout": [
  {
   "Z": 1,
   "symbol": "H",
   "name": "Hydrogen",
   "period": 1,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    1,
    0
   ],
   "shells": "1s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 1,
    "channels": 8,
    "rows": 8,
    "measured": 0,
    "exact": 8,
    "computed": 0,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "symmetry": 8
   }
  },
  {
   "Z": 2,
   "symbol": "He",
   "name": "Helium",
   "period": 1,
   "group": 18,
   "block": "s",
   "set_aside": false,
   "janet": [
    1,
    0
   ],
   "shells": "1s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 2,
    "channels": 16,
    "rows": 24,
    "measured": 7,
    "exact": 8,
    "computed": 9,
    "witnessed": 7,
    "lambda8_steps": 1
   },
   "relativistic": false,
   "limits": {
    "none": 7,
    "term": 3,
    "unresolved": 6,
    "symmetry": 8
   }
  },
  {
   "Z": 3,
   "symbol": "Li",
   "name": "Lithium",
   "period": 2,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    2,
    0
   ],
   "shells": "1s2 2s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 3,
    "channels": 24,
    "rows": 32,
    "measured": 17,
    "exact": 3,
    "computed": 12,
    "witnessed": 17,
    "lambda8_steps": 2
   },
   "relativistic": false,
   "limits": {
    "none": 17,
    "no-analysis": 2,
    "unresolved": 9,
    "term": 1,
    "symmetry": 3
   }
  },
  {
   "Z": 4,
   "symbol": "Be",
   "name": "Beryllium",
   "period": 2,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    2,
    0
   ],
   "shells": "1s2 2s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 4,
    "channels": 32,
    "rows": 48,
    "measured": 24,
    "exact": 3,
    "computed": 21,
    "witnessed": 24,
    "lambda8_steps": 3
   },
   "relativistic": false,
   "limits": {
    "none": 24,
    "term": 6,
    "unresolved": 15,
    "symmetry": 3
   }
  },
  {
   "Z": 5,
   "symbol": "B",
   "name": "Boron",
   "period": 2,
   "group": 13,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p",
   "level": "2P*1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 5,
    "channels": 40,
    "rows": 56,
    "measured": 29,
    "exact": 3,
    "computed": 24,
    "witnessed": 29,
    "lambda8_steps": 4
   },
   "relativistic": false,
   "limits": {
    "no-analysis": 2,
    "ionisation-limit": 3,
    "unresolved": 18,
    "none": 26,
    "term": 4,
    "symmetry": 3
   }
  },
  {
   "Z": 6,
   "symbol": "C",
   "name": "Carbon",
   "period": 2,
   "group": 14,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p2",
   "level": "3P0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 6,
    "channels": 48,
    "rows": 72,
    "measured": 28,
    "exact": 8,
    "computed": 36,
    "witnessed": 28,
    "lambda8_steps": 5
   },
   "relativistic": false,
   "limits": {
    "none": 28,
    "term": 7,
    "unresolved": 24,
    "no-analysis": 5,
    "symmetry": 8
   }
  },
  {
   "Z": 7,
   "symbol": "N",
   "name": "Nitrogen",
   "period": 2,
   "group": 15,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p3",
   "level": "4S*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 7,
    "channels": 56,
    "rows": 88,
    "measured": 16,
    "exact": 8,
    "computed": 64,
    "witnessed": 16,
    "lambda8_steps": 6
   },
   "relativistic": false,
   "limits": {
    "none": 16,
    "coupling": 4,
    "unresolved": 30,
    "term": 25,
    "no-analysis": 5,
    "symmetry": 8
   }
  },
  {
   "Z": 8,
   "symbol": "O",
   "name": "Oxygen",
   "period": 2,
   "group": 16,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p4",
   "level": "3P2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 8,
    "channels": 64,
    "rows": 104,
    "measured": 10,
    "exact": 8,
    "computed": 86,
    "witnessed": 10,
    "lambda8_steps": 7
   },
   "relativistic": false,
   "limits": {
    "coupling": 20,
    "unresolved": 36,
    "none": 10,
    "term": 25,
    "no-analysis": 5,
    "symmetry": 8
   }
  },
  {
   "Z": 9,
   "symbol": "F",
   "name": "Fluorine",
   "period": 2,
   "group": 17,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p5",
   "level": "2P*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 9,
    "channels": 72,
    "rows": 120,
    "measured": 4,
    "exact": 8,
    "computed": 108,
    "witnessed": 4,
    "lambda8_steps": 8
   },
   "relativistic": false,
   "limits": {
    "none": 4,
    "coupling": 26,
    "unresolved": 42,
    "term": 30,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 10,
   "symbol": "Ne",
   "name": "Neon",
   "period": 2,
   "group": 18,
   "block": "p",
   "set_aside": false,
   "janet": [
    3,
    1
   ],
   "shells": "1s2 2s2 2p6",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 10,
    "channels": 80,
    "rows": 136,
    "measured": 7,
    "exact": 8,
    "computed": 121,
    "witnessed": 7,
    "lambda8_steps": 9
   },
   "relativistic": false,
   "limits": {
    "term": 39,
    "none": 7,
    "unresolved": 48,
    "coupling": 24,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 11,
   "symbol": "Na",
   "name": "Sodium",
   "period": 3,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    3,
    0
   ],
   "shells": "[Ne]3s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 11,
    "channels": 88,
    "rows": 144,
    "measured": 6,
    "exact": 8,
    "computed": 130,
    "witnessed": 6,
    "lambda8_steps": 10
   },
   "relativistic": false,
   "limits": {
    "ionisation-limit": 6,
    "unresolved": 50,
    "term": 40,
    "coupling": 30,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 12,
   "symbol": "Mg",
   "name": "Magnesium",
   "period": 3,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    3,
    0
   ],
   "shells": "[Ne]3s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 12,
    "channels": 96,
    "rows": 160,
    "measured": 13,
    "exact": 8,
    "computed": 139,
    "witnessed": 13,
    "lambda8_steps": 11
   },
   "relativistic": false,
   "limits": {
    "none": 13,
    "term": 42,
    "unresolved": 57,
    "coupling": 30,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 13,
   "symbol": "Al",
   "name": "Aluminium",
   "period": 3,
   "group": 13,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p",
   "level": "2P*1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 13,
    "channels": 104,
    "rows": 168,
    "measured": 16,
    "exact": 8,
    "computed": 144,
    "witnessed": 16,
    "lambda8_steps": 12
   },
   "relativistic": false,
   "limits": {
    "none": 14,
    "ionisation-limit": 2,
    "unresolved": 60,
    "term": 44,
    "coupling": 30,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 14,
   "symbol": "Si",
   "name": "Silicon",
   "period": 3,
   "group": 14,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p2",
   "level": "3P0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 14,
    "channels": 112,
    "rows": 184,
    "measured": 22,
    "exact": 8,
    "computed": 154,
    "witnessed": 22,
    "lambda8_steps": 13
   },
   "relativistic": false,
   "limits": {
    "term": 48,
    "none": 22,
    "unresolved": 66,
    "coupling": 30,
    "no-analysis": 10,
    "symmetry": 8
   }
  },
  {
   "Z": 15,
   "symbol": "P",
   "name": "Phosphorus",
   "period": 3,
   "group": 15,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p3",
   "level": "4S*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 15,
    "channels": 120,
    "rows": 200,
    "measured": 13,
    "exact": 8,
    "computed": 179,
    "witnessed": 13,
    "lambda8_steps": 14
   },
   "relativistic": false,
   "limits": {
    "coupling": 40,
    "unresolved": 72,
    "term": 51,
    "none": 13,
    "no-analysis": 16,
    "symmetry": 8
   }
  },
  {
   "Z": 16,
   "symbol": "S",
   "name": "Sulfur",
   "period": 3,
   "group": 16,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p4",
   "level": "3P2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 16,
    "channels": 128,
    "rows": 216,
    "measured": 17,
    "exact": 8,
    "computed": 191,
    "witnessed": 17,
    "lambda8_steps": 15
   },
   "relativistic": false,
   "limits": {
    "coupling": 50,
    "unresolved": 78,
    "term": 51,
    "none": 17,
    "no-analysis": 12,
    "symmetry": 8
   }
  },
  {
   "Z": 17,
   "symbol": "Cl",
   "name": "Chlorine",
   "period": 3,
   "group": 17,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p5",
   "level": "2P*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 17,
    "channels": 136,
    "rows": 232,
    "measured": 0,
    "exact": 8,
    "computed": 224,
    "witnessed": 0,
    "lambda8_steps": 16
   },
   "relativistic": false,
   "limits": {
    "coupling": 60,
    "unresolved": 84,
    "term": 60,
    "no-analysis": 20,
    "symmetry": 8
   }
  },
  {
   "Z": 18,
   "symbol": "Ar",
   "name": "Argon",
   "period": 3,
   "group": 18,
   "block": "p",
   "set_aside": false,
   "janet": [
    4,
    1
   ],
   "shells": "[Ne]3s2 3p6",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 18,
    "channels": 144,
    "rows": 248,
    "measured": 3,
    "exact": 8,
    "computed": 237,
    "witnessed": 3,
    "lambda8_steps": 17
   },
   "relativistic": false,
   "limits": {
    "term": 70,
    "unresolved": 90,
    "none": 3,
    "coupling": 57,
    "no-analysis": 20,
    "symmetry": 8
   }
  },
  {
   "Z": 19,
   "symbol": "K",
   "name": "Potassium",
   "period": 4,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    4,
    0
   ],
   "shells": "[Ar]4s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 19,
    "channels": 152,
    "rows": 256,
    "measured": 6,
    "exact": 8,
    "computed": 242,
    "witnessed": 6,
    "lambda8_steps": 18
   },
   "relativistic": false,
   "limits": {
    "none": 6,
    "no-analysis": 21,
    "unresolved": 93,
    "term": 70,
    "coupling": 58,
    "symmetry": 8
   }
  },
  {
   "Z": 20,
   "symbol": "Ca",
   "name": "Calcium",
   "period": 4,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    4,
    0
   ],
   "shells": "[Ar]4s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 20,
    "channels": 160,
    "rows": 272,
    "measured": 22,
    "exact": 8,
    "computed": 242,
    "witnessed": 22,
    "lambda8_steps": 19
   },
   "relativistic": false,
   "limits": {
    "none": 22,
    "term": 68,
    "unresolved": 99,
    "coupling": 57,
    "no-analysis": 18,
    "symmetry": 8
   }
  },
  {
   "Z": 21,
   "symbol": "Sc",
   "name": "Scandium",
   "period": 4,
   "group": 3,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d 4s2",
   "level": "2D3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 21,
    "channels": 168,
    "rows": 280,
    "measured": 6,
    "exact": 8,
    "computed": 266,
    "witnessed": 6,
    "lambda8_steps": 20
   },
   "relativistic": false,
   "limits": {
    "term": 84,
    "unresolved": 102,
    "none": 6,
    "coupling": 60,
    "no-analysis": 20,
    "symmetry": 8
   }
  },
  {
   "Z": 22,
   "symbol": "Ti",
   "name": "Titanium",
   "period": 4,
   "group": 4,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d2 4s2",
   "level": "3F2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 22,
    "channels": 176,
    "rows": 296,
    "measured": 14,
    "exact": 8,
    "computed": 274,
    "witnessed": 14,
    "lambda8_steps": 21
   },
   "relativistic": false,
   "limits": {
    "term": 85,
    "unresolved": 108,
    "none": 14,
    "no-analysis": 21,
    "coupling": 60,
    "symmetry": 8
   }
  },
  {
   "Z": 23,
   "symbol": "V",
   "name": "Vanadium",
   "period": 4,
   "group": 5,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d3 4s2",
   "level": "4F3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 23,
    "channels": 184,
    "rows": 312,
    "measured": 0,
    "exact": 8,
    "computed": 304,
    "witnessed": 0,
    "lambda8_steps": 22
   },
   "relativistic": false,
   "limits": {
    "coupling": 70,
    "unresolved": 114,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 24,
   "symbol": "Cr",
   "name": "Chromium",
   "period": 4,
   "group": 6,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d5 4s",
   "level": "7S3",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 24,
    "channels": 192,
    "rows": 328,
    "measured": 0,
    "exact": 8,
    "computed": 320,
    "witnessed": 0,
    "lambda8_steps": 23
   },
   "relativistic": false,
   "limits": {
    "coupling": 80,
    "unresolved": 120,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 25,
   "symbol": "Mn",
   "name": "Manganese",
   "period": 4,
   "group": 7,
   "block": "s",
   "set_aside": false,
   "janet": [
    4,
    0
   ],
   "shells": "[Ar]3d5 4s2",
   "level": "6S5/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 25,
    "channels": 200,
    "rows": 344,
    "measured": 0,
    "exact": 8,
    "computed": 336,
    "witnessed": 0,
    "lambda8_steps": 24
   },
   "relativistic": true,
   "limits": {
    "coupling": 90,
    "unresolved": 126,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 26,
   "symbol": "Fe",
   "name": "Iron",
   "period": 4,
   "group": 8,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d6 4s2",
   "level": "5D4",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 26,
    "channels": 208,
    "rows": 360,
    "measured": 11,
    "exact": 8,
    "computed": 341,
    "witnessed": 11,
    "lambda8_steps": 25
   },
   "relativistic": false,
   "limits": {
    "coupling": 100,
    "unresolved": 132,
    "term": 91,
    "no-analysis": 18,
    "none": 11,
    "symmetry": 8
   }
  },
  {
   "Z": 27,
   "symbol": "Co",
   "name": "Cobalt",
   "period": 4,
   "group": 9,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d7 4s2",
   "level": "4F9/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 27,
    "channels": 216,
    "rows": 376,
    "measured": 0,
    "exact": 8,
    "computed": 368,
    "witnessed": 0,
    "lambda8_steps": 26
   },
   "relativistic": false,
   "limits": {
    "coupling": 110,
    "unresolved": 138,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 28,
   "symbol": "Ni",
   "name": "Nickel",
   "period": 4,
   "group": 10,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d8 4s2",
   "level": "3F4",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 28,
    "channels": 224,
    "rows": 392,
    "measured": 0,
    "exact": 8,
    "computed": 384,
    "witnessed": 0,
    "lambda8_steps": 27
   },
   "relativistic": false,
   "limits": {
    "coupling": 120,
    "unresolved": 144,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 29,
   "symbol": "Cu",
   "name": "Copper",
   "period": 4,
   "group": 11,
   "block": "d",
   "set_aside": false,
   "janet": [
    5,
    2
   ],
   "shells": "[Ar]3d10 4s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 29,
    "channels": 232,
    "rows": 408,
    "measured": 0,
    "exact": 8,
    "computed": 400,
    "witnessed": 0,
    "lambda8_steps": 28
   },
   "relativistic": false,
   "limits": {
    "coupling": 130,
    "unresolved": 150,
    "term": 95,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 30,
   "symbol": "Zn",
   "name": "Zinc",
   "period": 4,
   "group": 12,
   "block": "s",
   "set_aside": false,
   "janet": [
    4,
    0
   ],
   "shells": "[Ar]3d10 4s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 30,
    "channels": 240,
    "rows": 424,
    "measured": 9,
    "exact": 8,
    "computed": 407,
    "witnessed": 9,
    "lambda8_steps": 29
   },
   "relativistic": true,
   "limits": {
    "term": 101,
    "none": 9,
    "unresolved": 156,
    "coupling": 125,
    "no-analysis": 25,
    "symmetry": 8
   }
  },
  {
   "Z": 31,
   "symbol": "Ga",
   "name": "Gallium",
   "period": 4,
   "group": 13,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p",
   "level": "2P*1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 31,
    "channels": 248,
    "rows": 432,
    "measured": 10,
    "exact": 8,
    "computed": 414,
    "witnessed": 10,
    "lambda8_steps": 30
   },
   "relativistic": false,
   "limits": {
    "none": 8,
    "ionisation-limit": 2,
    "no-analysis": 26,
    "unresolved": 159,
    "term": 99,
    "coupling": 130,
    "symmetry": 8
   }
  },
  {
   "Z": 32,
   "symbol": "Ge",
   "name": "Germanium",
   "period": 4,
   "group": 14,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p2",
   "level": "3P0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 32,
    "channels": 256,
    "rows": 448,
    "measured": 5,
    "exact": 8,
    "computed": 435,
    "witnessed": 5,
    "lambda8_steps": 31
   },
   "relativistic": false,
   "limits": {
    "term": 110,
    "unresolved": 165,
    "no-analysis": 30,
    "none": 5,
    "coupling": 130,
    "symmetry": 8
   }
  },
  {
   "Z": 33,
   "symbol": "As",
   "name": "Arsenic",
   "period": 4,
   "group": 15,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p3",
   "level": "4S*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 33,
    "channels": 264,
    "rows": 464,
    "measured": 0,
    "exact": 8,
    "computed": 456,
    "witnessed": 0,
    "lambda8_steps": 32
   },
   "relativistic": false,
   "limits": {
    "coupling": 140,
    "unresolved": 171,
    "term": 115,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 34,
   "symbol": "Se",
   "name": "Selenium",
   "period": 4,
   "group": 16,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p4",
   "level": "3P2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 34,
    "channels": 272,
    "rows": 480,
    "measured": 0,
    "exact": 8,
    "computed": 472,
    "witnessed": 0,
    "lambda8_steps": 33
   },
   "relativistic": false,
   "limits": {
    "coupling": 150,
    "unresolved": 177,
    "term": 115,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 35,
   "symbol": "Br",
   "name": "Bromine",
   "period": 4,
   "group": 17,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p5",
   "level": "2P*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 35,
    "channels": 280,
    "rows": 496,
    "measured": 0,
    "exact": 8,
    "computed": 488,
    "witnessed": 0,
    "lambda8_steps": 34
   },
   "relativistic": false,
   "limits": {
    "coupling": 160,
    "unresolved": 183,
    "term": 115,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 36,
   "symbol": "Kr",
   "name": "Krypton",
   "period": 4,
   "group": 18,
   "block": "p",
   "set_aside": false,
   "janet": [
    5,
    1
   ],
   "shells": "[Ar]3d10 4s2 4p6",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 36,
    "channels": 288,
    "rows": 512,
    "measured": 0,
    "exact": 8,
    "computed": 504,
    "witnessed": 0,
    "lambda8_steps": 35
   },
   "relativistic": false,
   "limits": {
    "term": 125,
    "unresolved": 189,
    "coupling": 160,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 37,
   "symbol": "Rb",
   "name": "Rubidium",
   "period": 5,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    5,
    0
   ],
   "shells": "[Kr]5s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 37,
    "channels": 296,
    "rows": 520,
    "measured": 0,
    "exact": 8,
    "computed": 512,
    "witnessed": 0,
    "lambda8_steps": 36
   },
   "relativistic": false,
   "limits": {
    "no-analysis": 35,
    "unresolved": 192,
    "term": 125,
    "coupling": 160,
    "symmetry": 8
   }
  },
  {
   "Z": 38,
   "symbol": "Sr",
   "name": "Strontium",
   "period": 5,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    5,
    0
   ],
   "shells": "[Kr]5s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 38,
    "channels": 304,
    "rows": 536,
    "measured": 5,
    "exact": 8,
    "computed": 523,
    "witnessed": 5,
    "lambda8_steps": 37
   },
   "relativistic": false,
   "limits": {
    "term": 135,
    "unresolved": 198,
    "none": 5,
    "coupling": 160,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 39,
   "symbol": "Y",
   "name": "Yttrium",
   "period": 5,
   "group": 3,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d 5s2",
   "level": "2D3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 39,
    "channels": 312,
    "rows": 544,
    "measured": 0,
    "exact": 8,
    "computed": 536,
    "witnessed": 0,
    "lambda8_steps": 38
   },
   "relativistic": false,
   "limits": {
    "term": 140,
    "unresolved": 201,
    "no-analysis": 35,
    "coupling": 160,
    "symmetry": 8
   }
  },
  {
   "Z": 40,
   "symbol": "Zr",
   "name": "Zirconium",
   "period": 5,
   "group": 4,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d2 5s2",
   "level": "3F2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 40,
    "channels": 320,
    "rows": 560,
    "measured": 0,
    "exact": 8,
    "computed": 552,
    "witnessed": 0,
    "lambda8_steps": 39
   },
   "relativistic": false,
   "limits": {
    "term": 150,
    "unresolved": 207,
    "no-analysis": 35,
    "coupling": 160,
    "symmetry": 8
   }
  },
  {
   "Z": 41,
   "symbol": "Nb",
   "name": "Niobium",
   "period": 5,
   "group": 5,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d4 5s",
   "level": "6D1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 41,
    "channels": 328,
    "rows": 576,
    "measured": 0,
    "exact": 8,
    "computed": 568,
    "witnessed": 0,
    "lambda8_steps": 40
   },
   "relativistic": false,
   "limits": {
    "coupling": 170,
    "unresolved": 213,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 42,
   "symbol": "Mo",
   "name": "Molybdenum",
   "period": 5,
   "group": 6,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d5 5s",
   "level": "7S3",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 42,
    "channels": 336,
    "rows": 592,
    "measured": 0,
    "exact": 8,
    "computed": 584,
    "witnessed": 0,
    "lambda8_steps": 41
   },
   "relativistic": false,
   "limits": {
    "coupling": 180,
    "unresolved": 219,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 43,
   "symbol": "Tc",
   "name": "Technetium",
   "period": 5,
   "group": 7,
   "block": "s",
   "set_aside": false,
   "janet": [
    5,
    0
   ],
   "shells": "[Kr]4d5 5s2",
   "level": "6S5/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 43,
    "channels": 344,
    "rows": 608,
    "measured": 0,
    "exact": 8,
    "computed": 600,
    "witnessed": 0,
    "lambda8_steps": 42
   },
   "relativistic": false,
   "limits": {
    "coupling": 190,
    "unresolved": 225,
    "term": 150,
    "nuclear": 5,
    "no-analysis": 30,
    "symmetry": 8
   }
  },
  {
   "Z": 44,
   "symbol": "Ru",
   "name": "Ruthenium",
   "period": 5,
   "group": 8,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d7 5s",
   "level": "5F5",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 44,
    "channels": 352,
    "rows": 624,
    "measured": 0,
    "exact": 8,
    "computed": 616,
    "witnessed": 0,
    "lambda8_steps": 43
   },
   "relativistic": false,
   "limits": {
    "coupling": 200,
    "unresolved": 231,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 45,
   "symbol": "Rh",
   "name": "Rhodium",
   "period": 5,
   "group": 9,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d8 5s",
   "level": "4F9/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 45,
    "channels": 360,
    "rows": 640,
    "measured": 0,
    "exact": 8,
    "computed": 632,
    "witnessed": 0,
    "lambda8_steps": 44
   },
   "relativistic": false,
   "limits": {
    "coupling": 210,
    "unresolved": 237,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 46,
   "symbol": "Pd",
   "name": "Palladium",
   "period": 5,
   "group": 10,
   "block": "d",
   "set_aside": false,
   "janet": [
    6,
    2
   ],
   "shells": "[Kr]4d10",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 46,
    "channels": 368,
    "rows": 656,
    "measured": 0,
    "exact": 8,
    "computed": 648,
    "witnessed": 0,
    "lambda8_steps": 45
   },
   "relativistic": false,
   "limits": {
    "coupling": 220,
    "unresolved": 243,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 47,
   "symbol": "Ag",
   "name": "Silver",
   "period": 5,
   "group": 11,
   "block": "s",
   "set_aside": false,
   "janet": [
    5,
    0
   ],
   "shells": "[Kr]4d10 5s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 47,
    "channels": 376,
    "rows": 672,
    "measured": 0,
    "exact": 8,
    "computed": 664,
    "witnessed": 0,
    "lambda8_steps": 46
   },
   "relativistic": true,
   "limits": {
    "coupling": 230,
    "unresolved": 249,
    "term": 150,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 48,
   "symbol": "Cd",
   "name": "Cadmium",
   "period": 5,
   "group": 12,
   "block": "s",
   "set_aside": false,
   "janet": [
    5,
    0
   ],
   "shells": "[Kr]4d10 5s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 48,
    "channels": 384,
    "rows": 688,
    "measured": 12,
    "exact": 8,
    "computed": 668,
    "witnessed": 12,
    "lambda8_steps": 47
   },
   "relativistic": true,
   "limits": {
    "none": 12,
    "term": 153,
    "unresolved": 255,
    "coupling": 225,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 49,
   "symbol": "In",
   "name": "Indium",
   "period": 5,
   "group": 13,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p",
   "level": "2P*1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 49,
    "channels": 392,
    "rows": 696,
    "measured": 1,
    "exact": 8,
    "computed": 687,
    "witnessed": 1,
    "lambda8_steps": 48
   },
   "relativistic": false,
   "limits": {
    "term": 164,
    "ionisation-limit": 1,
    "unresolved": 258,
    "coupling": 230,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 50,
   "symbol": "Sn",
   "name": "Tin",
   "period": 5,
   "group": 14,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p2",
   "level": "3P0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 50,
    "channels": 400,
    "rows": 712,
    "measured": 0,
    "exact": 8,
    "computed": 704,
    "witnessed": 0,
    "lambda8_steps": 49
   },
   "relativistic": false,
   "limits": {
    "term": 175,
    "unresolved": 264,
    "coupling": 230,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 51,
   "symbol": "Sb",
   "name": "Antimony",
   "period": 5,
   "group": 15,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p3",
   "level": "4S*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 51,
    "channels": 408,
    "rows": 728,
    "measured": 0,
    "exact": 8,
    "computed": 720,
    "witnessed": 0,
    "lambda8_steps": 50
   },
   "relativistic": false,
   "limits": {
    "coupling": 240,
    "unresolved": 270,
    "term": 175,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 52,
   "symbol": "Te",
   "name": "Tellurium",
   "period": 5,
   "group": 16,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p4",
   "level": "3P2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 52,
    "channels": 416,
    "rows": 744,
    "measured": 0,
    "exact": 8,
    "computed": 736,
    "witnessed": 0,
    "lambda8_steps": 51
   },
   "relativistic": false,
   "limits": {
    "coupling": 250,
    "unresolved": 276,
    "term": 175,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 53,
   "symbol": "I",
   "name": "Iodine",
   "period": 5,
   "group": 17,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p5",
   "level": "2P*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 53,
    "channels": 424,
    "rows": 760,
    "measured": 0,
    "exact": 8,
    "computed": 752,
    "witnessed": 0,
    "lambda8_steps": 52
   },
   "relativistic": false,
   "limits": {
    "coupling": 260,
    "unresolved": 282,
    "term": 175,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 54,
   "symbol": "Xe",
   "name": "Xenon",
   "period": 5,
   "group": 18,
   "block": "p",
   "set_aside": false,
   "janet": [
    6,
    1
   ],
   "shells": "[Cd]5p6",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 54,
    "channels": 432,
    "rows": 776,
    "measured": 0,
    "exact": 8,
    "computed": 768,
    "witnessed": 0,
    "lambda8_steps": 53
   },
   "relativistic": false,
   "limits": {
    "term": 185,
    "unresolved": 288,
    "coupling": 260,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 55,
   "symbol": "Cs",
   "name": "Caesium",
   "period": 6,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    6,
    0
   ],
   "shells": "[Xe]6s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 55,
    "channels": 440,
    "rows": 784,
    "measured": 5,
    "exact": 8,
    "computed": 771,
    "witnessed": 5,
    "lambda8_steps": 54
   },
   "relativistic": false,
   "limits": {
    "ionisation-limit": 5,
    "unresolved": 291,
    "term": 185,
    "coupling": 260,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 56,
   "symbol": "Ba",
   "name": "Barium",
   "period": 6,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    6,
    0
   ],
   "shells": "[Xe]6s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 56,
    "channels": 448,
    "rows": 800,
    "measured": 5,
    "exact": 8,
    "computed": 787,
    "witnessed": 5,
    "lambda8_steps": 55
   },
   "relativistic": false,
   "limits": {
    "term": 195,
    "unresolved": 297,
    "none": 5,
    "coupling": 260,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 57,
   "symbol": "La",
   "name": "Lanthanum",
   "period": 6,
   "group": 3,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]5d 6s2",
   "level": "2D3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 57,
    "channels": 456,
    "rows": 808,
    "measured": 0,
    "exact": 8,
    "computed": 800,
    "witnessed": 0,
    "lambda8_steps": 56
   },
   "relativistic": false,
   "limits": {
    "term": 205,
    "unresolved": 300,
    "coupling": 260,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 58,
   "symbol": "Ce",
   "name": "Cerium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f 5d 6s2",
   "level": "1G*4",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 58,
    "channels": 464,
    "rows": 824,
    "measured": 0,
    "exact": 8,
    "computed": 816,
    "witnessed": 0,
    "lambda8_steps": 57
   },
   "relativistic": false,
   "limits": {
    "term": 215,
    "unresolved": 306,
    "coupling": 260,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 59,
   "symbol": "Pr",
   "name": "Praseodymium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f3 6s2",
   "level": "4I*9/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 59,
    "channels": 472,
    "rows": 840,
    "measured": 0,
    "exact": 8,
    "computed": 832,
    "witnessed": 0,
    "lambda8_steps": 58
   },
   "relativistic": false,
   "limits": {
    "coupling": 270,
    "unresolved": 312,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 60,
   "symbol": "Nd",
   "name": "Neodymium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f4 6s2",
   "level": "5I4",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 60,
    "channels": 480,
    "rows": 856,
    "measured": 0,
    "exact": 8,
    "computed": 848,
    "witnessed": 0,
    "lambda8_steps": 59
   },
   "relativistic": true,
   "limits": {
    "coupling": 280,
    "unresolved": 318,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 61,
   "symbol": "Pm",
   "name": "Promethium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f5 6s2",
   "level": "6H*5/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 61,
    "channels": 488,
    "rows": 872,
    "measured": 0,
    "exact": 8,
    "computed": 864,
    "witnessed": 0,
    "lambda8_steps": 60
   },
   "relativistic": true,
   "limits": {
    "coupling": 290,
    "unresolved": 324,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 62,
   "symbol": "Sm",
   "name": "Samarium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f6 6s2",
   "level": "7F0",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 62,
    "channels": 496,
    "rows": 888,
    "measured": 0,
    "exact": 8,
    "computed": 880,
    "witnessed": 0,
    "lambda8_steps": 61
   },
   "relativistic": true,
   "limits": {
    "coupling": 300,
    "unresolved": 330,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 63,
   "symbol": "Eu",
   "name": "Europium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f7 6s2",
   "level": "8S*7/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 63,
    "channels": 504,
    "rows": 904,
    "measured": 0,
    "exact": 8,
    "computed": 896,
    "witnessed": 0,
    "lambda8_steps": 62
   },
   "relativistic": false,
   "limits": {
    "coupling": 310,
    "unresolved": 336,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 64,
   "symbol": "Gd",
   "name": "Gadolinium",
   "period": 6,
   "group": null,
   "block": "d",
   "set_aside": true,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f7 5d 6s2",
   "level": "9D*2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 64,
    "channels": 512,
    "rows": 920,
    "measured": 0,
    "exact": 8,
    "computed": 912,
    "witnessed": 0,
    "lambda8_steps": 63
   },
   "relativistic": false,
   "limits": {
    "coupling": 320,
    "unresolved": 342,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 65,
   "symbol": "Tb",
   "name": "Terbium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f9 6s2",
   "level": "6H*15/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 65,
    "channels": 520,
    "rows": 936,
    "measured": 0,
    "exact": 8,
    "computed": 928,
    "witnessed": 0,
    "lambda8_steps": 64
   },
   "relativistic": false,
   "limits": {
    "coupling": 330,
    "unresolved": 348,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 66,
   "symbol": "Dy",
   "name": "Dysprosium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f10 6s2",
   "level": "5I8",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 66,
    "channels": 528,
    "rows": 952,
    "measured": 0,
    "exact": 8,
    "computed": 944,
    "witnessed": 0,
    "lambda8_steps": 65
   },
   "relativistic": false,
   "limits": {
    "coupling": 340,
    "unresolved": 354,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 67,
   "symbol": "Ho",
   "name": "Holmium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f11 6s2",
   "level": "4I*15/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 67,
    "channels": 536,
    "rows": 968,
    "measured": 0,
    "exact": 8,
    "computed": 960,
    "witnessed": 0,
    "lambda8_steps": 66
   },
   "relativistic": false,
   "limits": {
    "coupling": 350,
    "unresolved": 360,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 68,
   "symbol": "Er",
   "name": "Erbium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f12 6s2",
   "level": "3H6",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 68,
    "channels": 544,
    "rows": 984,
    "measured": 0,
    "exact": 8,
    "computed": 976,
    "witnessed": 0,
    "lambda8_steps": 67
   },
   "relativistic": false,
   "limits": {
    "coupling": 360,
    "unresolved": 366,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 69,
   "symbol": "Tm",
   "name": "Thulium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f13 6s2",
   "level": "2F*7/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 69,
    "channels": 552,
    "rows": 1000,
    "measured": 0,
    "exact": 8,
    "computed": 992,
    "witnessed": 0,
    "lambda8_steps": 68
   },
   "relativistic": false,
   "limits": {
    "coupling": 370,
    "unresolved": 372,
    "term": 215,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 70,
   "symbol": "Yb",
   "name": "Ytterbium",
   "period": 6,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    7,
    3
   ],
   "shells": "[Xe]4f14 6s2",
   "level": "1S0",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 70,
    "channels": 560,
    "rows": 1016,
    "measured": 0,
    "exact": 8,
    "computed": 1008,
    "witnessed": 0,
    "lambda8_steps": 69
   },
   "relativistic": false,
   "limits": {
    "term": 225,
    "unresolved": 378,
    "coupling": 370,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 71,
   "symbol": "Lu",
   "name": "Lutetium",
   "period": 6,
   "group": null,
   "block": "d",
   "set_aside": true,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d 6s2",
   "level": "2D3/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 71,
    "channels": 568,
    "rows": 1024,
    "measured": 1,
    "exact": 8,
    "computed": 1015,
    "witnessed": 1,
    "lambda8_steps": 70
   },
   "relativistic": true,
   "limits": {
    "term": 229,
    "ionisation-limit": 1,
    "unresolved": 381,
    "coupling": 370,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 72,
   "symbol": "Hf",
   "name": "Hafnium",
   "period": 6,
   "group": 4,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d2 6s2",
   "level": "3F2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 72,
    "channels": 576,
    "rows": 1040,
    "measured": 0,
    "exact": 8,
    "computed": 1032,
    "witnessed": 0,
    "lambda8_steps": 71
   },
   "relativistic": false,
   "limits": {
    "term": 240,
    "unresolved": 387,
    "coupling": 370,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 73,
   "symbol": "Ta",
   "name": "Tantalum",
   "period": 6,
   "group": 5,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d3 6s2",
   "level": "4F3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 73,
    "channels": 584,
    "rows": 1056,
    "measured": 0,
    "exact": 8,
    "computed": 1048,
    "witnessed": 0,
    "lambda8_steps": 72
   },
   "relativistic": false,
   "limits": {
    "coupling": 380,
    "unresolved": 393,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 74,
   "symbol": "W",
   "name": "Tungsten",
   "period": 6,
   "group": 6,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d4 6s2",
   "level": "5D0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 74,
    "channels": 592,
    "rows": 1072,
    "measured": 0,
    "exact": 8,
    "computed": 1064,
    "witnessed": 0,
    "lambda8_steps": 73
   },
   "relativistic": false,
   "limits": {
    "coupling": 390,
    "unresolved": 399,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 75,
   "symbol": "Re",
   "name": "Rhenium",
   "period": 6,
   "group": 7,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d5 6s2",
   "level": "6S5/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 75,
    "channels": 600,
    "rows": 1088,
    "measured": 0,
    "exact": 8,
    "computed": 1080,
    "witnessed": 0,
    "lambda8_steps": 74
   },
   "relativistic": false,
   "limits": {
    "coupling": 400,
    "unresolved": 405,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 76,
   "symbol": "Os",
   "name": "Osmium",
   "period": 6,
   "group": 8,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d6 6s2",
   "level": "5D4",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 76,
    "channels": 608,
    "rows": 1104,
    "measured": 0,
    "exact": 8,
    "computed": 1096,
    "witnessed": 0,
    "lambda8_steps": 75
   },
   "relativistic": false,
   "limits": {
    "coupling": 410,
    "unresolved": 411,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 77,
   "symbol": "Ir",
   "name": "Iridium",
   "period": 6,
   "group": 9,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d7 6s2",
   "level": "4F9/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 77,
    "channels": 616,
    "rows": 1120,
    "measured": 0,
    "exact": 8,
    "computed": 1112,
    "witnessed": 0,
    "lambda8_steps": 76
   },
   "relativistic": false,
   "limits": {
    "coupling": 420,
    "unresolved": 417,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 78,
   "symbol": "Pt",
   "name": "Platinum",
   "period": 6,
   "group": 10,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d9 6s",
   "level": "3D3",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 78,
    "channels": 624,
    "rows": 1136,
    "measured": 0,
    "exact": 8,
    "computed": 1128,
    "witnessed": 0,
    "lambda8_steps": 77
   },
   "relativistic": false,
   "limits": {
    "coupling": 430,
    "unresolved": 423,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 79,
   "symbol": "Au",
   "name": "Gold",
   "period": 6,
   "group": 11,
   "block": "d",
   "set_aside": false,
   "janet": [
    7,
    2
   ],
   "shells": "[Xe]4f14 5d10 6s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 79,
    "channels": 632,
    "rows": 1152,
    "measured": 0,
    "exact": 8,
    "computed": 1144,
    "witnessed": 0,
    "lambda8_steps": 78
   },
   "relativistic": false,
   "limits": {
    "coupling": 440,
    "unresolved": 429,
    "term": 240,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 80,
   "symbol": "Hg",
   "name": "Mercury",
   "period": 6,
   "group": 12,
   "block": "s",
   "set_aside": false,
   "janet": [
    6,
    0
   ],
   "shells": "[Xe]4f14 5d10 6s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 80,
    "channels": 640,
    "rows": 1168,
    "measured": 5,
    "exact": 8,
    "computed": 1155,
    "witnessed": 5,
    "lambda8_steps": 79
   },
   "relativistic": true,
   "limits": {
    "term": 250,
    "unresolved": 435,
    "none": 5,
    "coupling": 435,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 81,
   "symbol": "Tl",
   "name": "Thallium",
   "period": 6,
   "group": 13,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p",
   "level": "2P*1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 81,
    "channels": 648,
    "rows": 1176,
    "measured": 3,
    "exact": 8,
    "computed": 1165,
    "witnessed": 3,
    "lambda8_steps": 80
   },
   "relativistic": false,
   "limits": {
    "ionisation-limit": 3,
    "term": 252,
    "unresolved": 438,
    "coupling": 440,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 82,
   "symbol": "Pb",
   "name": "Lead",
   "period": 6,
   "group": 14,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p2",
   "level": "(1/2,1/2)0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 82,
    "channels": 656,
    "rows": 1192,
    "measured": 0,
    "exact": 8,
    "computed": 1184,
    "witnessed": 0,
    "lambda8_steps": 81
   },
   "relativistic": false,
   "limits": {
    "term": 265,
    "unresolved": 444,
    "coupling": 440,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 83,
   "symbol": "Bi",
   "name": "Bismuth",
   "period": 6,
   "group": 15,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p3",
   "level": "4S*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 83,
    "channels": 664,
    "rows": 1208,
    "measured": 4,
    "exact": 8,
    "computed": 1196,
    "witnessed": 4,
    "lambda8_steps": 82
   },
   "relativistic": false,
   "limits": {
    "coupling": 450,
    "unresolved": 450,
    "term": 261,
    "none": 4,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 84,
   "symbol": "Po",
   "name": "Polonium",
   "period": 6,
   "group": 16,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p4",
   "level": "3P2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 84,
    "channels": 672,
    "rows": 1224,
    "measured": 0,
    "exact": 8,
    "computed": 1216,
    "witnessed": 0,
    "lambda8_steps": 83
   },
   "relativistic": false,
   "limits": {
    "coupling": 460,
    "unresolved": 456,
    "term": 265,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 85,
   "symbol": "At",
   "name": "Astatine",
   "period": 6,
   "group": 17,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p5",
   "level": "2P*3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 85,
    "channels": 680,
    "rows": 1240,
    "measured": 0,
    "exact": 8,
    "computed": 1232,
    "witnessed": 0,
    "lambda8_steps": 84
   },
   "relativistic": false,
   "limits": {
    "coupling": 470,
    "unresolved": 462,
    "term": 265,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 86,
   "symbol": "Rn",
   "name": "Radon",
   "period": 6,
   "group": 18,
   "block": "p",
   "set_aside": false,
   "janet": [
    7,
    1
   ],
   "shells": "[Hg]6p6",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 86,
    "channels": 688,
    "rows": 1256,
    "measured": 0,
    "exact": 8,
    "computed": 1248,
    "witnessed": 0,
    "lambda8_steps": 85
   },
   "relativistic": false,
   "limits": {
    "term": 275,
    "unresolved": 468,
    "coupling": 470,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 87,
   "symbol": "Fr",
   "name": "Francium",
   "period": 7,
   "group": 1,
   "block": "s",
   "set_aside": false,
   "janet": [
    7,
    0
   ],
   "shells": "[Rn]7s",
   "level": "2S1/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 87,
    "channels": 696,
    "rows": 1264,
    "measured": 2,
    "exact": 8,
    "computed": 1254,
    "witnessed": 2,
    "lambda8_steps": 86
   },
   "relativistic": false,
   "limits": {
    "ionisation-limit": 2,
    "term": 278,
    "unresolved": 471,
    "coupling": 470,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 88,
   "symbol": "Ra",
   "name": "Radium",
   "period": 7,
   "group": 2,
   "block": "s",
   "set_aside": false,
   "janet": [
    7,
    0
   ],
   "shells": "[Rn]7s2",
   "level": "1S0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 88,
    "channels": 704,
    "rows": 1280,
    "measured": 0,
    "exact": 8,
    "computed": 1272,
    "witnessed": 0,
    "lambda8_steps": 87
   },
   "relativistic": false,
   "limits": {
    "term": 290,
    "unresolved": 477,
    "coupling": 470,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 89,
   "symbol": "Ac",
   "name": "Actinium",
   "period": 7,
   "group": 3,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]6d 7s2",
   "level": "2D3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 89,
    "channels": 712,
    "rows": 1288,
    "measured": 0,
    "exact": 8,
    "computed": 1280,
    "witnessed": 0,
    "lambda8_steps": 88
   },
   "relativistic": false,
   "limits": {
    "term": 295,
    "unresolved": 480,
    "coupling": 470,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 90,
   "symbol": "Th",
   "name": "Thorium",
   "period": 7,
   "group": null,
   "block": "d",
   "set_aside": true,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]6d2 7s2",
   "level": "3F2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 90,
    "channels": 720,
    "rows": 1304,
    "measured": 0,
    "exact": 8,
    "computed": 1296,
    "witnessed": 0,
    "lambda8_steps": 89
   },
   "relativistic": false,
   "limits": {
    "term": 305,
    "unresolved": 486,
    "coupling": 470,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 91,
   "symbol": "Pa",
   "name": "Protactinium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f2 6d 7s2",
   "level": "4K11/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 91,
    "channels": 728,
    "rows": 1320,
    "measured": 0,
    "exact": 8,
    "computed": 1312,
    "witnessed": 0,
    "lambda8_steps": 90
   },
   "relativistic": false,
   "limits": {
    "coupling": 480,
    "unresolved": 492,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 92,
   "symbol": "U",
   "name": "Uranium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f3 6d 7s2",
   "level": "5L*6",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 92,
    "channels": 736,
    "rows": 1336,
    "measured": 0,
    "exact": 8,
    "computed": 1328,
    "witnessed": 0,
    "lambda8_steps": 91
   },
   "relativistic": false,
   "limits": {
    "coupling": 490,
    "unresolved": 498,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 93,
   "symbol": "Np",
   "name": "Neptunium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f4 6d 7s2",
   "level": "6L11/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 93,
    "channels": 744,
    "rows": 1352,
    "measured": 0,
    "exact": 8,
    "computed": 1344,
    "witnessed": 0,
    "lambda8_steps": 92
   },
   "relativistic": false,
   "limits": {
    "coupling": 500,
    "unresolved": 504,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 94,
   "symbol": "Pu",
   "name": "Plutonium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f6 7s2",
   "level": "7F0",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 94,
    "channels": 752,
    "rows": 1368,
    "measured": 0,
    "exact": 8,
    "computed": 1360,
    "witnessed": 0,
    "lambda8_steps": 93
   },
   "relativistic": false,
   "limits": {
    "coupling": 510,
    "unresolved": 510,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 95,
   "symbol": "Am",
   "name": "Americium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f7 7s2",
   "level": "8S*7/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 95,
    "channels": 760,
    "rows": 1384,
    "measured": 0,
    "exact": 8,
    "computed": 1376,
    "witnessed": 0,
    "lambda8_steps": 94
   },
   "relativistic": false,
   "limits": {
    "coupling": 520,
    "unresolved": 516,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 96,
   "symbol": "Cm",
   "name": "Curium",
   "period": 7,
   "group": null,
   "block": "d",
   "set_aside": true,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f7 6d 7s2",
   "level": "9D*2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 96,
    "channels": 768,
    "rows": 1400,
    "measured": 0,
    "exact": 8,
    "computed": 1392,
    "witnessed": 0,
    "lambda8_steps": 95
   },
   "relativistic": false,
   "limits": {
    "coupling": 530,
    "unresolved": 522,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 97,
   "symbol": "Bk",
   "name": "Berkelium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f9 7s2",
   "level": "6H*15/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 97,
    "channels": 776,
    "rows": 1416,
    "measured": 0,
    "exact": 8,
    "computed": 1408,
    "witnessed": 0,
    "lambda8_steps": 96
   },
   "relativistic": false,
   "limits": {
    "coupling": 540,
    "unresolved": 528,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 98,
   "symbol": "Cf",
   "name": "Californium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f10 7s2",
   "level": "5I8",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 98,
    "channels": 784,
    "rows": 1432,
    "measured": 0,
    "exact": 8,
    "computed": 1424,
    "witnessed": 0,
    "lambda8_steps": 97
   },
   "relativistic": false,
   "limits": {
    "coupling": 550,
    "unresolved": 534,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 99,
   "symbol": "Es",
   "name": "Einsteinium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f11 7s2",
   "level": "4I*15/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 99,
    "channels": 792,
    "rows": 1448,
    "measured": 0,
    "exact": 8,
    "computed": 1440,
    "witnessed": 0,
    "lambda8_steps": 98
   },
   "relativistic": false,
   "limits": {
    "coupling": 560,
    "unresolved": 540,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 100,
   "symbol": "Fm",
   "name": "Fermium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f12 7s2",
   "level": "3H6",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 100,
    "channels": 800,
    "rows": 1464,
    "measured": 0,
    "exact": 8,
    "computed": 1456,
    "witnessed": 0,
    "lambda8_steps": 99
   },
   "relativistic": false,
   "limits": {
    "coupling": 570,
    "unresolved": 546,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 101,
   "symbol": "Md",
   "name": "Mendelevium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f13 7s2",
   "level": "2F*7/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 101,
    "channels": 808,
    "rows": 1480,
    "measured": 0,
    "exact": 8,
    "computed": 1472,
    "witnessed": 0,
    "lambda8_steps": 100
   },
   "relativistic": false,
   "limits": {
    "coupling": 580,
    "unresolved": 552,
    "term": 305,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 102,
   "symbol": "No",
   "name": "Nobelium",
   "period": 7,
   "group": null,
   "block": "f",
   "set_aside": true,
   "janet": [
    8,
    3
   ],
   "shells": "[Rn]5f14 7s2",
   "level": "1S0",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 102,
    "channels": 816,
    "rows": 1496,
    "measured": 0,
    "exact": 8,
    "computed": 1488,
    "witnessed": 0,
    "lambda8_steps": 101
   },
   "relativistic": false,
   "limits": {
    "term": 315,
    "unresolved": 558,
    "coupling": 580,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 103,
   "symbol": "Lr",
   "name": "Lawrencium",
   "period": 7,
   "group": null,
   "block": "p",
   "set_aside": true,
   "janet": [
    8,
    1
   ],
   "shells": "[Rn]5f14 7s2 7p",
   "level": "2P*1/2",
   "held": false,
   "populated": true,
   "counts": {
    "ions": 103,
    "channels": 824,
    "rows": 1504,
    "measured": 0,
    "exact": 8,
    "computed": 1496,
    "witnessed": 0,
    "lambda8_steps": 102
   },
   "relativistic": true,
   "limits": {
    "term": 320,
    "unresolved": 561,
    "coupling": 580,
    "no-analysis": 35,
    "symmetry": 8
   }
  },
  {
   "Z": 104,
   "symbol": "Rf",
   "name": "Rutherfordium",
   "period": 7,
   "group": 4,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f14 6d2 7s2",
   "level": "3F2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 104,
    "channels": 832,
    "rows": 1520,
    "measured": 0,
    "exact": 8,
    "computed": 1512,
    "witnessed": 0,
    "lambda8_steps": 103
   },
   "relativistic": true,
   "limits": {
    "nuclear": 1512,
    "symmetry": 8
   }
  },
  {
   "Z": 105,
   "symbol": "Db",
   "name": "Dubnium",
   "period": 7,
   "group": 5,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f14 6d3 7s2",
   "level": "4F3/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 105,
    "channels": 840,
    "rows": 1536,
    "measured": 0,
    "exact": 8,
    "computed": 1528,
    "witnessed": 0,
    "lambda8_steps": 104
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1528,
    "symmetry": 8
   }
  },
  {
   "Z": 106,
   "symbol": "Sg",
   "name": "Seaborgium",
   "period": 7,
   "group": 6,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f14 6d4 7s2",
   "level": "0",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 106,
    "channels": 848,
    "rows": 1552,
    "measured": 0,
    "exact": 8,
    "computed": 1544,
    "witnessed": 0,
    "lambda8_steps": 105
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1544,
    "symmetry": 8
   }
  },
  {
   "Z": 107,
   "symbol": "Bh",
   "name": "Bohrium",
   "period": 7,
   "group": 7,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f14 6d5 7s2",
   "level": "5/2",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 107,
    "channels": 856,
    "rows": 1568,
    "measured": 0,
    "exact": 8,
    "computed": 1560,
    "witnessed": 0,
    "lambda8_steps": 106
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1560,
    "symmetry": 8
   }
  },
  {
   "Z": 108,
   "symbol": "Hs",
   "name": "Hassium",
   "period": 7,
   "group": 8,
   "block": "d",
   "set_aside": false,
   "janet": [
    8,
    2
   ],
   "shells": "[Rn]5f14 6d6 7s2",
   "level": "4",
   "held": true,
   "populated": true,
   "counts": {
    "ions": 108,
    "channels": 864,
    "rows": 1584,
    "measured": 0,
    "exact": 8,
    "computed": 1576,
    "witnessed": 0,
    "lambda8_steps": 107
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1576,
    "symmetry": 8
   }
  },
  {
   "Z": 109,
   "symbol": "Mt",
   "name": "Meitnerium",
   "period": 7,
   "group": 9,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 109,
    "channels": 872,
    "rows": 1600,
    "measured": 0,
    "exact": 8,
    "computed": 1592,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1592,
    "symmetry": 8
   }
  },
  {
   "Z": 110,
   "symbol": "Ds",
   "name": "Darmstadtium",
   "period": 7,
   "group": 10,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 110,
    "channels": 880,
    "rows": 1616,
    "measured": 0,
    "exact": 8,
    "computed": 1608,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1608,
    "symmetry": 8
   }
  },
  {
   "Z": 111,
   "symbol": "Rg",
   "name": "Roentgenium",
   "period": 7,
   "group": 11,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 111,
    "channels": 888,
    "rows": 1632,
    "measured": 0,
    "exact": 8,
    "computed": 1624,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1624,
    "symmetry": 8
   }
  },
  {
   "Z": 112,
   "symbol": "Cn",
   "name": "Copernicium",
   "period": 7,
   "group": 12,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 112,
    "channels": 896,
    "rows": 1648,
    "measured": 0,
    "exact": 8,
    "computed": 1640,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1640,
    "symmetry": 8
   }
  },
  {
   "Z": 113,
   "symbol": "Nh",
   "name": "Nihonium",
   "period": 7,
   "group": 13,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 113,
    "channels": 904,
    "rows": 1656,
    "measured": 0,
    "exact": 8,
    "computed": 1648,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1648,
    "symmetry": 8
   }
  },
  {
   "Z": 114,
   "symbol": "Fl",
   "name": "Flerovium",
   "period": 7,
   "group": 14,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 114,
    "channels": 912,
    "rows": 1672,
    "measured": 0,
    "exact": 8,
    "computed": 1664,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1664,
    "symmetry": 8
   }
  },
  {
   "Z": 115,
   "symbol": "Mc",
   "name": "Moscovium",
   "period": 7,
   "group": 15,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 115,
    "channels": 920,
    "rows": 1688,
    "measured": 0,
    "exact": 8,
    "computed": 1680,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1680,
    "symmetry": 8
   }
  },
  {
   "Z": 116,
   "symbol": "Lv",
   "name": "Livermorium",
   "period": 7,
   "group": 16,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 116,
    "channels": 928,
    "rows": 1704,
    "measured": 0,
    "exact": 8,
    "computed": 1696,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1696,
    "symmetry": 8
   }
  },
  {
   "Z": 117,
   "symbol": "Ts",
   "name": "Tennessine",
   "period": 7,
   "group": 17,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 117,
    "channels": 936,
    "rows": 1720,
    "measured": 0,
    "exact": 8,
    "computed": 1712,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1712,
    "symmetry": 8
   }
  },
  {
   "Z": 118,
   "symbol": "Og",
   "name": "Oganesson",
   "period": 7,
   "group": 18,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 118,
    "channels": 944,
    "rows": 1736,
    "measured": 0,
    "exact": 8,
    "computed": 1728,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1728,
    "symmetry": 8
   }
  },
  {
   "Z": 119,
   "symbol": "Uue",
   "name": "Ununennium",
   "period": 8,
   "group": 1,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 119,
    "channels": 952,
    "rows": 1744,
    "measured": 0,
    "exact": 0,
    "computed": 1744,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1744
   }
  },
  {
   "Z": 120,
   "symbol": "Ubn",
   "name": "Unbinilium",
   "period": 8,
   "group": 2,
   "block": null,
   "set_aside": false,
   "janet": null,
   "shells": null,
   "level": null,
   "held": null,
   "populated": false,
   "counts": {
    "ions": 120,
    "channels": 960,
    "rows": 1760,
    "measured": 0,
    "exact": 0,
    "computed": 1760,
    "witnessed": 0,
    "lambda8_steps": 0
   },
   "relativistic": false,
   "limits": {
    "nuclear": 1760
   }
  }
 ],
 "manifest": [
  {
   "Z": 1,
   "file": "elements/1.js",
   "bytes": 3900,
   "md5": "48abc3e7bbf329e603cbece0fe1c03b8",
   "payload_bytes": 3820,
   "payload_md5": "70d331d410a2c1c310a4d2968396ed75"
  },
  {
   "Z": 2,
   "file": "elements/2.js",
   "bytes": 9652,
   "md5": "c3fa31601737e5c9770887255a84571f",
   "payload_bytes": 9572,
   "payload_md5": "7c3a216e46e154f0ed664dd3f56f8929"
  },
  {
   "Z": 3,
   "file": "elements/3.js",
   "bytes": 13163,
   "md5": "48b8cbbe5d61b0e4ce65c0b92fcbcc11",
   "payload_bytes": 13083,
   "payload_md5": "7c381d521a2f9cab52f304122b8c18b4"
  },
  {
   "Z": 4,
   "file": "elements/4.js",
   "bytes": 18941,
   "md5": "03fc82111096a63a0829003f3f5d498d",
   "payload_bytes": 18861,
   "payload_md5": "66a1f6782c29ff23b6c6bb0c241e92f3"
  },
  {
   "Z": 5,
   "file": "elements/5.js",
   "bytes": 23142,
   "md5": "f2ab97e7eb096e834f3262c70065f975",
   "payload_bytes": 23062,
   "payload_md5": "056fb61e1854803c0b058ef29183a1df"
  },
  {
   "Z": 6,
   "file": "elements/6.js",
   "bytes": 28946,
   "md5": "049b4ef3e4353e0282afd17244228d0d",
   "payload_bytes": 28866,
   "payload_md5": "b71cbf6803543f12cec6fdf8eb84d7e5"
  },
  {
   "Z": 7,
   "file": "elements/7.js",
   "bytes": 35751,
   "md5": "7f7679e6d46aac23d056c976e817df0d",
   "payload_bytes": 35671,
   "payload_md5": "ea8e5fdd5f90bebe8aa7edb4988e48e5"
  },
  {
   "Z": 8,
   "file": "elements/8.js",
   "bytes": 41815,
   "md5": "6fbcb5aba5d75e185fc03c5e9222a42a",
   "payload_bytes": 41735,
   "payload_md5": "ae2dfe50957f4bd9db67a873b63c8558"
  },
  {
   "Z": 9,
   "file": "elements/9.js",
   "bytes": 48097,
   "md5": "20b0805fd71a117edcae81fb8bf98dfc",
   "payload_bytes": 48017,
   "payload_md5": "731f6603f995f0e6c0665071223878e3"
  },
  {
   "Z": 10,
   "file": "elements/10.js",
   "bytes": 54179,
   "md5": "1976177bd9c2b85dd29c6c668ff382c8",
   "payload_bytes": 54098,
   "payload_md5": "5ffe339491fa2bac7e5366752891d47d"
  },
  {
   "Z": 11,
   "file": "elements/11.js",
   "bytes": 59021,
   "md5": "b7a593e1b42ed258cd53ce445a0256e1",
   "payload_bytes": 58940,
   "payload_md5": "ef4aa00f0ad2234b898d700b891aa82d"
  },
  {
   "Z": 12,
   "file": "elements/12.js",
   "bytes": 64011,
   "md5": "845389f867aca26065323523db95938a",
   "payload_bytes": 63930,
   "payload_md5": "f1a73c2e1857f97de41e9f1411e4c225"
  },
  {
   "Z": 13,
   "file": "elements/13.js",
   "bytes": 68323,
   "md5": "5b688bb8589ec84d285b396fbae25138",
   "payload_bytes": 68242,
   "payload_md5": "2215eb6df0a9e8962beee78d8ab8b970"
  },
  {
   "Z": 14,
   "file": "elements/14.js",
   "bytes": 73924,
   "md5": "b7fd58a9d557bac1ce58b03243dd41cb",
   "payload_bytes": 73843,
   "payload_md5": "8943127f5e5fda7df2ed8e2980b58493"
  },
  {
   "Z": 15,
   "file": "elements/15.js",
   "bytes": 80333,
   "md5": "6eac1f11795e65a678f204964374b401",
   "payload_bytes": 80252,
   "payload_md5": "db6ebcdea6fc60ea98f136a36507afe5"
  },
  {
   "Z": 16,
   "file": "elements/16.js",
   "bytes": 86000,
   "md5": "5b60d1006c3330e3f971e6e4e61ad779",
   "payload_bytes": 85919,
   "payload_md5": "af962b109c812cb5118f9c8d040a8826"
  },
  {
   "Z": 17,
   "file": "elements/17.js",
   "bytes": 92912,
   "md5": "7acf075e8df287bc1b2ef64e81b7ed72",
   "payload_bytes": 92831,
   "payload_md5": "697fb2c5ae8268c62008ec587d3831ee"
  },
  {
   "Z": 18,
   "file": "elements/18.js",
   "bytes": 100030,
   "md5": "0a9f79ba7d0f2a5e4e26944a0f3b2026",
   "payload_bytes": 99949,
   "payload_md5": "7e7c97a58aec6ea5145e84cbc07d7de9"
  },
  {
   "Z": 19,
   "file": "elements/19.js",
   "bytes": 103953,
   "md5": "4841abe44822311343cf037889d4204a",
   "payload_bytes": 103872,
   "payload_md5": "acaa6e1c463f83bb3740877e5e5bfc9f"
  },
  {
   "Z": 20,
   "file": "elements/20.js",
   "bytes": 109345,
   "md5": "fe126e1a3019a8d8596b158d3f31b872",
   "payload_bytes": 109264,
   "payload_md5": "290061363362047022be52d599025889"
  },
  {
   "Z": 21,
   "file": "elements/21.js",
   "bytes": 114457,
   "md5": "a8c3efd38aff32e26b29029c697315f3",
   "payload_bytes": 114376,
   "payload_md5": "cbfea4d4146aef614ea6be47fd247a5f"
  },
  {
   "Z": 22,
   "file": "elements/22.js",
   "bytes": 120201,
   "md5": "c989acf644077fe33eff40a3e39113ab",
   "payload_bytes": 120120,
   "payload_md5": "a0c9ab687f810d6cafbcb625e67d02fd"
  },
  {
   "Z": 23,
   "file": "elements/23.js",
   "bytes": 127085,
   "md5": "f363783dc1b77bd34182553ced620082",
   "payload_bytes": 127004,
   "payload_md5": "6979b9e81deb51a7369490078d12450d"
  },
  {
   "Z": 24,
   "file": "elements/24.js",
   "bytes": 133079,
   "md5": "8dee14b2d34800f80cd31e7738b5556d",
   "payload_bytes": 132998,
   "payload_md5": "c4ce68fc51455bcd30045fca73bb1720"
  },
  {
   "Z": 25,
   "file": "elements/25.js",
   "bytes": 138972,
   "md5": "93685b7e4aee90365c5e3e129ab3a9ae",
   "payload_bytes": 138891,
   "payload_md5": "5bbb8b55b4b033372a021504cc3a5c8b"
  },
  {
   "Z": 26,
   "file": "elements/26.js",
   "bytes": 144410,
   "md5": "3e6def761040db629af3ae1bb24fee86",
   "payload_bytes": 144329,
   "payload_md5": "0a412f466aaf7eceae9c73cef6fcd146"
  },
  {
   "Z": 27,
   "file": "elements/27.js",
   "bytes": 150927,
   "md5": "83a8cc69bb2153545590f8d5ebd61f0e",
   "payload_bytes": 150846,
   "payload_md5": "f6e3fac3c18b89a03a85513e963499c8"
  },
  {
   "Z": 28,
   "file": "elements/28.js",
   "bytes": 156873,
   "md5": "2d272f6f62cf439d410aa42dc7407746",
   "payload_bytes": 156792,
   "payload_md5": "2b9cea9b8464a12e4b6ff258883a790d"
  },
  {
   "Z": 29,
   "file": "elements/29.js",
   "bytes": 162902,
   "md5": "738733c7ee1e9a73caf9c03423e4160a",
   "payload_bytes": 162821,
   "payload_md5": "246fe47ab6dd5c47c792d2e7fe985c88"
  },
  {
   "Z": 30,
   "file": "elements/30.js",
   "bytes": 168754,
   "md5": "4bffed7bf3763e8fc235570fb8e13b65",
   "payload_bytes": 168673,
   "payload_md5": "0ba209ee4a0a7819d628903f859a72c9"
  },
  {
   "Z": 31,
   "file": "elements/31.js",
   "bytes": 172935,
   "md5": "78d8fc449cd9d328e9eca183b1dc7a5b",
   "payload_bytes": 172854,
   "payload_md5": "ef2400bf5c2b8cb044c509a46b0fce22"
  },
  {
   "Z": 32,
   "file": "elements/32.js",
   "bytes": 179315,
   "md5": "e7859fa2ad281fb8a7a1ee64ac4c12d4",
   "payload_bytes": 179234,
   "payload_md5": "84a82e3f34aebce002d51261cde523ec"
  },
  {
   "Z": 33,
   "file": "elements/33.js",
   "bytes": 185587,
   "md5": "53d1f528462f0c822f12015fff282c1d",
   "payload_bytes": 185506,
   "payload_md5": "0831aebd448faa18dbbf08bb4492c450"
  },
  {
   "Z": 34,
   "file": "elements/34.js",
   "bytes": 191542,
   "md5": "147cffdb32830a25f8d76fc76d6b8d18",
   "payload_bytes": 191461,
   "payload_md5": "9fe368adb0fe2e0b84f6999f7e47e4af"
  },
  {
   "Z": 35,
   "file": "elements/35.js",
   "bytes": 197499,
   "md5": "38be16a7dbab90ea1a8830f16ec0c8b7",
   "payload_bytes": 197418,
   "payload_md5": "1be15b27a0eb979b0600d5d6b5205f89"
  },
  {
   "Z": 36,
   "file": "elements/36.js",
   "bytes": 203757,
   "md5": "abab26ceccdd578961fec31858509a1d",
   "payload_bytes": 203676,
   "payload_md5": "0870c287aceccc7e4b734bdf86cb56cd"
  },
  {
   "Z": 37,
   "file": "elements/37.js",
   "bytes": 207927,
   "md5": "66261678366b802f38ddd8738b5a6242",
   "payload_bytes": 207846,
   "payload_md5": "aa45bb697a0fe0389adba6f9828841b9"
  },
  {
   "Z": 38,
   "file": "elements/38.js",
   "bytes": 213947,
   "md5": "92c6eddec9a8fab4dfc21e221513be81",
   "payload_bytes": 213866,
   "payload_md5": "cc403847307a2841d22f79779474f94f"
  },
  {
   "Z": 39,
   "file": "elements/39.js",
   "bytes": 218482,
   "md5": "1921411b72ba7e689d2f721f079a58b7",
   "payload_bytes": 218401,
   "payload_md5": "ae2a9e2a1487bafbe7b5e2eca36ef83c"
  },
  {
   "Z": 40,
   "file": "elements/40.js",
   "bytes": 224725,
   "md5": "2b946aaffbac1c7b82d14ee1b2f820c1",
   "payload_bytes": 224644,
   "payload_md5": "461ed9c297b68a55b55679a255f463fe"
  },
  {
   "Z": 41,
   "file": "elements/41.js",
   "bytes": 230732,
   "md5": "71cf2b62d209740fd99870b92227dcaa",
   "payload_bytes": 230651,
   "payload_md5": "117e1db4d740af2e80778112b2cba37b"
  },
  {
   "Z": 42,
   "file": "elements/42.js",
   "bytes": 236723,
   "md5": "950302762bcbaf8d939733268a8f8c70",
   "payload_bytes": 236642,
   "payload_md5": "34030152e29bc0c5478cce1fa401b8a5"
  },
  {
   "Z": 43,
   "file": "elements/43.js",
   "bytes": 242577,
   "md5": "2890d5b1811404df232d454f42763ad3",
   "payload_bytes": 242496,
   "payload_md5": "629c62aa5fc88fcdd7bc3f53bd5ede84"
  },
  {
   "Z": 44,
   "file": "elements/44.js",
   "bytes": 248675,
   "md5": "e5580973ab3e6522026de38e90e5b1e6",
   "payload_bytes": 248594,
   "payload_md5": "c89b08a1fdaea92475370b36d020c21c"
  },
  {
   "Z": 45,
   "file": "elements/45.js",
   "bytes": 254629,
   "md5": "359fc35cef8424d8468bb0f8c652d8c2",
   "payload_bytes": 254548,
   "payload_md5": "326346fa97dfa0f632da55b984e899ba"
  },
  {
   "Z": 46,
   "file": "elements/46.js",
   "bytes": 260503,
   "md5": "ae4d934f4b1c6216c7b0ea3c11720cc6",
   "payload_bytes": 260422,
   "payload_md5": "f41313612404864de8f1f346562dd1b3"
  },
  {
   "Z": 47,
   "file": "elements/47.js",
   "bytes": 266527,
   "md5": "5fa9b4f0661106b1f2230adc7d756708",
   "payload_bytes": 266446,
   "payload_md5": "380c6bbb8c6e9867f6a06107d399ffc9"
  },
  {
   "Z": 48,
   "file": "elements/48.js",
   "bytes": 272213,
   "md5": "d41a1e1cd1dd9c6e3fccba0ff8edf5f0",
   "payload_bytes": 272132,
   "payload_md5": "94fafaad28806e9e84c7eabcf0946c21"
  },
  {
   "Z": 49,
   "file": "elements/49.js",
   "bytes": 277112,
   "md5": "1c267387c06ba7e0ad2a30ef0ecf75e9",
   "payload_bytes": 277031,
   "payload_md5": "49969b32e3fa125f69667a9665f0da16"
  },
  {
   "Z": 50,
   "file": "elements/50.js",
   "bytes": 283357,
   "md5": "7677ae77f6850c598fca098a41d03790",
   "payload_bytes": 283276,
   "payload_md5": "6ef4196baa6577c0820e6660ce668871"
  },
  {
   "Z": 51,
   "file": "elements/51.js",
   "bytes": 289285,
   "md5": "f022fd3a7550ad0893fdb1251908f07e",
   "payload_bytes": 289204,
   "payload_md5": "a1c52fc29849daf9cf356bcd697487ec"
  },
  {
   "Z": 52,
   "file": "elements/52.js",
   "bytes": 295252,
   "md5": "6e8e137e6ce74c4cba9a613bacb98093",
   "payload_bytes": 295171,
   "payload_md5": "640ffa97954318109824a2d2bcc08b2b"
  },
  {
   "Z": 53,
   "file": "elements/53.js",
   "bytes": 301191,
   "md5": "9c72f81e66efb7e9b40d0e9f9d75fb0b",
   "payload_bytes": 301110,
   "payload_md5": "c9681dd920c8553c698ae1d0dabfb0c0"
  },
  {
   "Z": 54,
   "file": "elements/54.js",
   "bytes": 310609,
   "md5": "9ce0e430f8d172660589a5f4c3c3ef76",
   "payload_bytes": 310528,
   "payload_md5": "039f59c002646b549507e3b3d63fc16f"
  },
  {
   "Z": 55,
   "file": "elements/55.js",
   "bytes": 315165,
   "md5": "a82b9102d3a2292970470df0ffb52872",
   "payload_bytes": 315084,
   "payload_md5": "a6e5e7fa27a42a160f340ffca24db33b"
  },
  {
   "Z": 56,
   "file": "elements/56.js",
   "bytes": 320895,
   "md5": "09a8708a24305e4a744c14637b0d1d1c",
   "payload_bytes": 320814,
   "payload_md5": "94d1a1c5d75dec0b3dbcf98535483efc"
  },
  {
   "Z": 57,
   "file": "elements/57.js",
   "bytes": 325332,
   "md5": "2893c2c0ae55da4a306b9770bb526487",
   "payload_bytes": 325251,
   "payload_md5": "1db6d6c2aa001dc5201ffb835efa4a07"
  },
  {
   "Z": 58,
   "file": "elements/58.js",
   "bytes": 331905,
   "md5": "4c32e667531614e8962296c6b87d31e7",
   "payload_bytes": 331824,
   "payload_md5": "e75cd13d69d8f968ffe59eeb4808fc20"
  },
  {
   "Z": 59,
   "file": "elements/59.js",
   "bytes": 337803,
   "md5": "9a6b2f3f2cf782550fcab15a2c3c43b2",
   "payload_bytes": 337722,
   "payload_md5": "8874638fddcaef05a8975c22a6aa0c2a"
  },
  {
   "Z": 60,
   "file": "elements/60.js",
   "bytes": 343917,
   "md5": "7df5ca8d047fadb48b1d6aff79edcf85",
   "payload_bytes": 343836,
   "payload_md5": "75a66acf1986de814f81ea2dd5bf76a9"
  },
  {
   "Z": 61,
   "file": "elements/61.js",
   "bytes": 349777,
   "md5": "c4072e8b4650275b2cf88803f6030676",
   "payload_bytes": 349696,
   "payload_md5": "80e99d5d4337c7ffd73cec71aa40c240"
  },
  {
   "Z": 62,
   "file": "elements/62.js",
   "bytes": 355826,
   "md5": "f44105d99f21ca7dddfacc3c41eb32cd",
   "payload_bytes": 355745,
   "payload_md5": "47ba2a6d726996d194f2fd98f7aa0538"
  },
  {
   "Z": 63,
   "file": "elements/63.js",
   "bytes": 361822,
   "md5": "cfbafe4f41c7e7f5787c26a7671e4df5",
   "payload_bytes": 361741,
   "payload_md5": "4fb1fdc194752f8764525b01106e17cd"
  },
  {
   "Z": 64,
   "file": "elements/64.js",
   "bytes": 368014,
   "md5": "03000e951b4424250c8ea681cc39ec8a",
   "payload_bytes": 367933,
   "payload_md5": "6897d84973a4b2fe1bc38d0ab7bf6fa7"
  },
  {
   "Z": 65,
   "file": "elements/65.js",
   "bytes": 373967,
   "md5": "dee93004b93774d69541298ce0ee0799",
   "payload_bytes": 373886,
   "payload_md5": "37635f08ed1c86ecaa2286c51d6ca3cb"
  },
  {
   "Z": 66,
   "file": "elements/66.js",
   "bytes": 380027,
   "md5": "acbc18b2eff59b156970967ad1183544",
   "payload_bytes": 379946,
   "payload_md5": "a49e6bc138b08485695b9205d61320b1"
  },
  {
   "Z": 67,
   "file": "elements/67.js",
   "bytes": 386021,
   "md5": "69c44f7239c0141742187ae9cd667c1c",
   "payload_bytes": 385940,
   "payload_md5": "a3510191aa1b65d0c25f626fb0d165b2"
  },
  {
   "Z": 68,
   "file": "elements/68.js",
   "bytes": 392018,
   "md5": "767ca305ca6056a58ebc4c67a085fef0",
   "payload_bytes": 391937,
   "payload_md5": "80c16f5b6492f8d84eb60da9005b8561"
  },
  {
   "Z": 69,
   "file": "elements/69.js",
   "bytes": 398104,
   "md5": "eb0a2aefb57cbfd8e344428e62713a90",
   "payload_bytes": 398023,
   "payload_md5": "0ad67256aca13dbfa2a6a9c30d8a184c"
  },
  {
   "Z": 70,
   "file": "elements/70.js",
   "bytes": 404427,
   "md5": "337a472e011dbbd394e3f13332787585",
   "payload_bytes": 404346,
   "payload_md5": "f17d7b31e8aa0794edb3a4f396f0d331"
  },
  {
   "Z": 71,
   "file": "elements/71.js",
   "bytes": 408723,
   "md5": "064e130b1223c43ec597b50d818f4dd0",
   "payload_bytes": 408642,
   "payload_md5": "f6a124a713ff13a7fbec47e793f4d67d"
  },
  {
   "Z": 72,
   "file": "elements/72.js",
   "bytes": 415074,
   "md5": "568f69042d55ae7d5faaa5e156f52c1f",
   "payload_bytes": 414993,
   "payload_md5": "dd96be07c603b7414686796cf5ef5026"
  },
  {
   "Z": 73,
   "file": "elements/73.js",
   "bytes": 421061,
   "md5": "556d135dfb6397d5275d33c2820d08c9",
   "payload_bytes": 420980,
   "payload_md5": "ae96bf49b6b576d8a19e91b9c2fd7b7b"
  },
  {
   "Z": 74,
   "file": "elements/74.js",
   "bytes": 427056,
   "md5": "7aeaf407128d15e6ec2e311cdc1f1365",
   "payload_bytes": 426975,
   "payload_md5": "d620b02b056cc54c2fc4bb83e3467b49"
  },
  {
   "Z": 75,
   "file": "elements/75.js",
   "bytes": 433069,
   "md5": "5af4fe5bbe92c135c1cb630736e0b12b",
   "payload_bytes": 432988,
   "payload_md5": "756cfc01329392522e60ba5f908db197"
  },
  {
   "Z": 76,
   "file": "elements/76.js",
   "bytes": 439104,
   "md5": "66d1a22c9937af54e64c862eb350839c",
   "payload_bytes": 439023,
   "payload_md5": "a865fb6a4cdba724a788f9e57ad5d701"
  },
  {
   "Z": 77,
   "file": "elements/77.js",
   "bytes": 445128,
   "md5": "4bd39026fc97aa1281b337f144d49ee5",
   "payload_bytes": 445047,
   "payload_md5": "9e3102761648aad31e18f6ad162bab33"
  },
  {
   "Z": 78,
   "file": "elements/78.js",
   "bytes": 451230,
   "md5": "2660f9a07269b7de0bbcfbcb2ddd2486",
   "payload_bytes": 451149,
   "payload_md5": "5a1828a2df0c85798bebb2ea52d965aa"
  },
  {
   "Z": 79,
   "file": "elements/79.js",
   "bytes": 457255,
   "md5": "8d600d9901969e0aacb4bb0e9538778c",
   "payload_bytes": 457174,
   "payload_md5": "9ed55efdd62610fd325f38aa3e3ca74d"
  },
  {
   "Z": 80,
   "file": "elements/80.js",
   "bytes": 463351,
   "md5": "d63ecdfee4c90403547960bcc6396f46",
   "payload_bytes": 463270,
   "payload_md5": "692d5940e95b63a3b0a0532deff23c8d"
  },
  {
   "Z": 81,
   "file": "elements/81.js",
   "bytes": 467945,
   "md5": "8c82f5558e44894239996245d474dca3",
   "payload_bytes": 467864,
   "payload_md5": "a33658ee4a1bc8912b46b01d23c6f1bd"
  },
  {
   "Z": 82,
   "file": "elements/82.js",
   "bytes": 474105,
   "md5": "fcb89d3e99f96b141e7511fdee91dd5a",
   "payload_bytes": 474024,
   "payload_md5": "a8184c0c5bd643d41c375430a6a99814"
  },
  {
   "Z": 83,
   "file": "elements/83.js",
   "bytes": 479892,
   "md5": "342a343b6cf5fa51bc8ad9c1945bb05d",
   "payload_bytes": 479811,
   "payload_md5": "81ccc2327eb5999d4187c02b1c05f684"
  },
  {
   "Z": 84,
   "file": "elements/84.js",
   "bytes": 486159,
   "md5": "2c9b432d741cf27700124efafeedc0eb",
   "payload_bytes": 486078,
   "payload_md5": "c02191470bed74d166cd7712a14c6082"
  },
  {
   "Z": 85,
   "file": "elements/85.js",
   "bytes": 492142,
   "md5": "e7bcc2d2501433439372b18885a31c56",
   "payload_bytes": 492061,
   "payload_md5": "bd5b2421077674e223ee1dda5c7eb5c2"
  },
  {
   "Z": 86,
   "file": "elements/86.js",
   "bytes": 498564,
   "md5": "364d4a51ec866f0e5e653f77df37c508",
   "payload_bytes": 498483,
   "payload_md5": "09348e1a0490ba496a0fb5ab35864f24"
  },
  {
   "Z": 87,
   "file": "elements/87.js",
   "bytes": 502900,
   "md5": "cafd37e473b215080209f14309578dae",
   "payload_bytes": 502819,
   "payload_md5": "56f6e5d7ea562591f7773736957b9720"
  },
  {
   "Z": 88,
   "file": "elements/88.js",
   "bytes": 509133,
   "md5": "09cb4381456082ba68ab55ec03e5ad48",
   "payload_bytes": 509052,
   "payload_md5": "2e680ea7420dffd4dba52915e85e51ef"
  },
  {
   "Z": 89,
   "file": "elements/89.js",
   "bytes": 513379,
   "md5": "4ddde4620079b2ba1a7519cbea3a9188",
   "payload_bytes": 513298,
   "payload_md5": "504eff2042aa8c744c91393919fcb265"
  },
  {
   "Z": 90,
   "file": "elements/90.js",
   "bytes": 519730,
   "md5": "719432622ebd412b50d6858620e1ce71",
   "payload_bytes": 519649,
   "payload_md5": "4729527a8be2e5c139eaa24041e5282c"
  },
  {
   "Z": 91,
   "file": "elements/91.js",
   "bytes": 525866,
   "md5": "db4b418dbd380910e993b21d537207ae",
   "payload_bytes": 525785,
   "payload_md5": "f5fbb6113236b11dfbdbca404b604145"
  },
  {
   "Z": 92,
   "file": "elements/92.js",
   "bytes": 531862,
   "md5": "7e9c782d81bd44134752e2a30b168ecb",
   "payload_bytes": 531781,
   "payload_md5": "fe612ff9cb45433d11ede7a8dba13a10"
  },
  {
   "Z": 93,
   "file": "elements/93.js",
   "bytes": 537977,
   "md5": "1f6e90992087778f82ad617f9bab3363",
   "payload_bytes": 537896,
   "payload_md5": "6069ed00da3b7375d64b99e7ed5f8a97"
  },
  {
   "Z": 94,
   "file": "elements/94.js",
   "bytes": 543799,
   "md5": "fee2a5a220e01097d4ac6aac630be201",
   "payload_bytes": 543718,
   "payload_md5": "becde5f7bfb5ebe54bb2e3634b8c4b42"
  },
  {
   "Z": 95,
   "file": "elements/95.js",
   "bytes": 549908,
   "md5": "9540240aa10018830d4300bf6ac1c6e2",
   "payload_bytes": 549827,
   "payload_md5": "2404998ecc606a1d74d14a61d06a42e0"
  },
  {
   "Z": 96,
   "file": "elements/96.js",
   "bytes": 555973,
   "md5": "70b32cac90aeba2b0f3afe825b14fa54",
   "payload_bytes": 555892,
   "payload_md5": "4dae9be027cabf889b110d6aff1bfe8a"
  },
  {
   "Z": 97,
   "file": "elements/97.js",
   "bytes": 561981,
   "md5": "b294035c760222c25a283d4cf4799086",
   "payload_bytes": 561900,
   "payload_md5": "3b0532b71a08878d9da7f43d2edbe488"
  },
  {
   "Z": 98,
   "file": "elements/98.js",
   "bytes": 567985,
   "md5": "e35a17b35dec328386cf4a6fa5bee7d2",
   "payload_bytes": 567904,
   "payload_md5": "e0ecd46912262dff48f169612b8a803e"
  },
  {
   "Z": 99,
   "file": "elements/99.js",
   "bytes": 573971,
   "md5": "ed0b09a39086924f93c30e4756cbc465",
   "payload_bytes": 573890,
   "payload_md5": "8b1603951375836f14d1c42910cf34f4"
  },
  {
   "Z": 100,
   "file": "elements/100.js",
   "bytes": 580059,
   "md5": "fa8a7cafd445a404281ea0ade29b0bef",
   "payload_bytes": 579977,
   "payload_md5": "f9aef58ec4a2704f966bb69d89ca334b"
  },
  {
   "Z": 101,
   "file": "elements/101.js",
   "bytes": 586100,
   "md5": "04e1f8ace8aaffcb0892f913bd7e3751",
   "payload_bytes": 586018,
   "payload_md5": "6656f6791f2b9cd4691f9d8e09617a8f"
  },
  {
   "Z": 102,
   "file": "elements/102.js",
   "bytes": 592532,
   "md5": "618c948475ce248f46602fbf81949c4f",
   "payload_bytes": 592450,
   "payload_md5": "4a68d7f559c04dc3b1ddb5b2914708ae"
  },
  {
   "Z": 103,
   "file": "elements/103.js",
   "bytes": 596814,
   "md5": "a0345d955dca372699983873073dfc89",
   "payload_bytes": 596732,
   "payload_md5": "e87a08879130e155a2d4153d5400a317"
  },
  {
   "Z": 104,
   "file": "elements/104.js",
   "bytes": 567730,
   "md5": "c6eb0dbd766a2647451cc7b1adab138e",
   "payload_bytes": 567648,
   "payload_md5": "ee8fc01f7cb05354d98a41add4817632"
  },
  {
   "Z": 105,
   "file": "elements/105.js",
   "bytes": 573555,
   "md5": "71c7714f72c0e94ba3756632e14f611b",
   "payload_bytes": 573473,
   "payload_md5": "ea4ed64fd7bdce3726c63fd206654d44"
  },
  {
   "Z": 106,
   "file": "elements/106.js",
   "bytes": 579402,
   "md5": "6253dbfb928736d7242e7e72959cfab2",
   "payload_bytes": 579320,
   "payload_md5": "e2c86e0e63ac5e1ba5a9097927e85afe"
  },
  {
   "Z": 107,
   "file": "elements/107.js",
   "bytes": 585203,
   "md5": "c5a180b090ece8220bbb891ce7f73ac5",
   "payload_bytes": 585121,
   "payload_md5": "8e13b45e6e05112661e5a4afd69a0d92"
  },
  {
   "Z": 108,
   "file": "elements/108.js",
   "bytes": 591005,
   "md5": "7a707d4b7b326623b243bb01c8f6bdbd",
   "payload_bytes": 590923,
   "payload_md5": "13a7f8b5a6f2dd5d88e628e06ce5a956"
  },
  {
   "Z": 109,
   "file": "elements/109.js",
   "bytes": 508748,
   "md5": "526b2e1f9db7d21e5266939cc90ec2d2",
   "payload_bytes": 508666,
   "payload_md5": "b8cf3b9dc03e095133b49a41fc15a393"
  },
  {
   "Z": 110,
   "file": "elements/110.js",
   "bytes": 513717,
   "md5": "8c1f1190adc51d86df5cc69a7c700264",
   "payload_bytes": 513635,
   "payload_md5": "ec5db7a00ce1239728d3cae52498e0a0"
  },
  {
   "Z": 111,
   "file": "elements/111.js",
   "bytes": 518676,
   "md5": "621152a82cd86cc0d59a470c400e797b",
   "payload_bytes": 518594,
   "payload_md5": "67a92c1d7601978892e571c6e1ac5e25"
  },
  {
   "Z": 112,
   "file": "elements/112.js",
   "bytes": 523696,
   "md5": "55ffcb1202ea320dad80fbc068b40bb2",
   "payload_bytes": 523614,
   "payload_md5": "af86d7e347d0666a8ecfad1f4275539c"
  },
  {
   "Z": 113,
   "file": "elements/113.js",
   "bytes": 526848,
   "md5": "f9028d78fef31ce38e8ce04c38c0e2b4",
   "payload_bytes": 526766,
   "payload_md5": "a797d6c5014664a931f33058c1c3eccc"
  },
  {
   "Z": 114,
   "file": "elements/114.js",
   "bytes": 531858,
   "md5": "f28b9a98a454cff8b8f38d61364fc771",
   "payload_bytes": 531776,
   "payload_md5": "216d70e2a68e2146c0af2083ece376cf"
  },
  {
   "Z": 115,
   "file": "elements/115.js",
   "bytes": 536855,
   "md5": "aa66a556af6e1fef88018e2cde7bea3a",
   "payload_bytes": 536773,
   "payload_md5": "1d0af06d065a911c3d7221de4f7f80e6"
  },
  {
   "Z": 116,
   "file": "elements/116.js",
   "bytes": 541792,
   "md5": "b11d55c6d1f29e07e9aceeb874cc9143",
   "payload_bytes": 541710,
   "payload_md5": "bd4d30fccf3b8109b5b0794ab697ff97"
  },
  {
   "Z": 117,
   "file": "elements/117.js",
   "bytes": 546791,
   "md5": "0cec903519b136e8ea0619d3595e0660",
   "payload_bytes": 546709,
   "payload_md5": "7dbead65fbf7c12062d854d40f84eac1"
  },
  {
   "Z": 118,
   "file": "elements/118.js",
   "bytes": 551785,
   "md5": "507ba17809c4e736da448dea7d7b5db6",
   "payload_bytes": 551703,
   "payload_md5": "e97d797aa6267b692faad780e414b4a8"
  },
  {
   "Z": 119,
   "file": "elements/119.js",
   "bytes": 673382,
   "md5": "279948916c98a15c280ee2a7253622d7",
   "payload_bytes": 673300,
   "payload_md5": "834750453af2118fc7f30a18285d7b6c"
  },
  {
   "Z": 120,
   "file": "elements/120.js",
   "bytes": 718174,
   "md5": "0dbe43c48cd96e087c885a83671565c9",
   "payload_bytes": 718092,
   "payload_md5": "c7b3105aeb57a2f6a62973c07de26614"
  }
 ],
 "protocol": {
  "index": "data/index.js sets window.__mi.index",
  "element": "data/elements/<Z>.js sets window.__mi.el[Z]",
  "why": "the page opens from a file:// URL on a phone, where fetch() of a local file is blocked and a <script src> is not",
  "encoding": "utf-8"
 }
};
