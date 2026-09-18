window.__mi = window.__mi || {}; window.__mi.index = {
 "meta": {
  "title": "The Method Index",
  "subtitle": "The Method 1.6 · every element on every axis of every index",
  "built": "2026-09-18T20:56:16+00:00",
  "commit": "e9b77f6fa390",
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
  "walk_integrate": {
   "python": "def integrate(field, l, eps, c, sign=1.0):\n    \"\"\"one shot at energy eps.  Returns (nodes, mismatch, p_match, norm_r, s_out, s_in,\n    p_out list, ok) -- or None when eps is not bracketed by the potential on the grid.\n    sign flips the relativistic term (the demonstrable failure mode); it is 1.0 in use.\"\"\"\n    g = field.grid\n    r, r2, V, dV, r2V = g.r, g.r2, field.V, field.dVdx, field.r2V\n    n = g.n\n    H = 2 * g.h\n    ll = l * (l + 1)\n    rel = c is not None\n    inv2c2 = 1.0 / (2 * c * c) if rel else 0.0\n\n    # coefficient arrays for this eps\n    A = [0.0] * n\n    B = [0.0] * n\n    if rel:\n        for i in range(n):\n            M = 1.0 + (eps - V[i]) * inv2c2\n            if M <= 0.0:\n                return None              # ε below −2c²: no such state\n            A[i] = -sign * dV[i] * inv2c2 / M\n            B[i] = ll + 2.0 * M * (r2V[i] - eps * r2[i])\n    else:\n        for i in range(n):\n            B[i] = ll + 2.0 * (r2V[i] - eps * r2[i])\n\n    # matching point: the outermost index where B < 0 (classically allowed), stepping by 2\n    m = -1\n    for i in range(n - 1, -1, -1):\n        if B[i] < 0.0:\n            m = i\n            break\n    if m < 4:\n        return None                      # eps below the potential everywhere: too low\n    if m >= n - 4:\n        return None                      # allowed region reaches the grid edge: too high\n    if m % 2:\n        m -= 1\n\n    # outward: the r^γ series at the nucleus\n    Z = field.Z\n    if rel:\n        g2 = ll + 1.0 - (Z / c) ** 2 * sign\n        gam = math.sqrt(g2) if g2 > 0 else 0.5\n    else:\n        gam = l + 1.0\n    p = 1.0\n    s = gam\n    pout = [0.0] * (m + 1)\n    pout[0] = p\n    nodes = 0\n    scale_shift = 0\n    for i in range(0, m, 2):\n        a0, b0 = A[i], B[i]\n        a1, b1 = A[i + 1], B[i + 1]\n        a2, b2 = A[i + 2], B[i + 2]\n        k1p = s\n        k1s = s + a0 * (s - p) + b0 * p\n        p1 = p + 0.5 * H * k1p\n        s1 = s + 0.5 * H * k1s\n        k2p = s1\n        k2s = s1 + a1 * (s1 - p1) + b1 * p1\n        p2 = p + 0.5 * H * k2p\n        s2 = s + 0.5 * H * k2s\n        k3p = s2\n        k3s = s2 + a1 * (s2 - p2) + b1 * p2\n        p3 = p + H * k3p\n        s3 = s + H * k3s\n        k4p = s3\n        k4s = s3 + a2 * (s3 - p3) + b2 * p3\n        pn = p + H / 6.0 * (k1p + 2 * k2p + 2 * k3p + k4p)\n        sn = s + H / 6.0 * (k1s + 2 * k2s + 2 * k3s + k4s)\n        if pn * p < 0.0:\n            nodes += 1\n        p, s = pn, sn\n        if abs(p) > 1e100:\n            p *= 1e-100\n            s *= 1e-100\n            pout = [v * 1e-100 for v in pout]\n        pout[i + 1] = 0.0                # midpoints are not carried\n        pout[i + 2] = p\n    p_out, s_out = p, s\n    # fill the midpoints of the outward solution by a second pass is unnecessary: the\n    # norm uses the even points only (Simpson on the coarse step H).\n\n    # inward: WKB tail from the last point\n    bN = B[n - 1]\n    p = 1e-30\n    s = -math.sqrt(bN) * p if bN > 0 else -p\n    pin = {}\n    pin[n - 1] = p\n    for i in range(n - 1, m, -2):\n        a0, b0 = A[i], B[i]\n        a1, b1 = A[i - 1], B[i - 1]\n        a2, b2 = A[i - 2], B[i - 2]\n        hh = -H\n        k1p = s\n        k1s = s + a0 * (s - p) + b0 * p\n        p1 = p + 0.5 * hh * k1p\n        s1 = s + 0.5 * hh * k1s\n        k2p = s1\n        k2s = s1 + a1 * (s1 - p1) + b1 * p1\n        p2 = p + 0.5 * hh * k2p\n        s2 = s + 0.5 * hh * k2s\n        k3p = s2\n        k3s = s2 + a1 * (s2 - p2) + b1 * p2\n        p3 = p + hh * k3p\n        s3 = s + hh * k3s\n        k4p = s3\n        k4s = s3 + a2 * (s3 - p3) + b2 * p3\n        p = p + hh / 6.0 * (k1p + 2 * k2p + 2 * k3p + k4p)\n        s = s + hh / 6.0 * (k1s + 2 * k2s + 2 * k3s + k4s)\n        if abs(p) > 1e100:\n            p *= 1e-100\n            s *= 1e-100\n            for k in pin:\n                pin[k] *= 1e-100\n        pin[i - 2] = p\n    p_in, s_in = p, s\n    if p_out == 0.0 or p_in == 0.0:\n        return None\n\n    # scale the inward branch onto the outward one at m\n    f = p_out / p_in\n    s_in *= f\n    for k in pin:\n        pin[k] *= f\n\n    # the full function on the coarse (even) points, and its norm ∫P² dr = ∫ p² r dx\n    P = [0.0] * n\n    for i in range(0, m + 1, 2):\n        P[i] = pout[i]\n    for i in range(m, n, 2):\n        P[i] = pin.get(i, 0.0)\n    f2 = [P[i] * P[i] * r[i] for i in range(0, n, 2)]\n    norm = integral(f2, H)\n    mismatch = (s_out - s_in) / r[m]     # (dP/dr)_out − (dP/dr)_in at the match, P(m) = p_out\n    # Hartree's correction: Δε = P(m) [P'_out − P'_in] / (2 ∫P² dr)\n    deps = p_out * mismatch / (2.0 * norm)\n    return nodes, deps, P, norm, m\n",
   "file": "tools/lowdin_walk.py",
   "line": 227,
   "status": "RECONSTRUCTED",
   "source": "one shot of the Koelling-Harmon radial pair in x = ln r, RK4 outward from the r^gamma series and inward from the WKB tail, matched at the outer turning point; the Hartree matching correction"
  },
  "walk_solve": {
   "python": "def solve(field, n, l, c, eps0=None, tol=1e-9, sign=1.0, maxit=80, trace=None):\n    \"\"\"the bound state (n, l) of the field: returns (eps, P_normalised) or None when the\n    grid holds no such bound state (eps ≥ 0).\"\"\"\n    target = n - l - 1\n    Z = field.Z\n    if eps0 is None:\n        eps = -0.5 * (Z / n) ** 2\n    else:\n        eps = eps0\n    if eps >= 0:\n        eps = -1e-3\n    lo, hi = None, 0.0                   # bounds: lo < eps_true < hi\n    floor = -4.0 * Z * Z - 10.0          # below the deepest level any field here holds\n    for it in range(maxit):\n        if eps < floor:\n            return None\n        res = integrate(field, l, eps, c, sign)\n        if trace:\n            trace(f\"      it {it:2d} eps {eps: .8f} lo {lo} hi {hi} -> \" +\n                  (\"none\" if res is None else f\"nodes {res[0]} deps {res[1]: .3e}\"))\n        if res is None:\n            # too low or too high?  decide by where the allowed region sits\n            g = field.grid\n            # if eps is above V at the grid edge the region reaches the edge -> too high\n            if eps > field.V[g.n - 1] + l * (l + 1) / (2 * g.r2[g.n - 1]):\n                hi = eps\n                eps = (lo + hi) / 2 if lo is not None else eps * 2.0 - 1e-6\n            else:\n                lo = eps\n                eps = (lo + hi) / 2\n            continue\n        nodes, deps, P, norm, m = res\n        if nodes > target:\n            hi = eps\n            eps = (lo + hi) / 2 if lo is not None else eps * 2.0 - 1e-6\n            continue\n        if nodes < target:\n            lo = eps\n            eps = (lo + hi) / 2\n            continue\n        # right node count: the sign of the correction tightens the bracket, and the\n        # Newton-like step is capped and kept inside it (the Hartree correction is\n        # first-order; from a distant start it overshoots past the node boundary)\n        if deps > 0:\n            lo = eps if lo is None else max(lo, eps)\n        else:\n            hi = min(hi, eps)\n        if abs(deps) > 0.5 * abs(eps):\n            deps = math.copysign(0.5 * abs(eps), deps)\n        new = eps + deps\n        if lo is not None and new <= lo:\n            new = (eps + lo) / 2\n        if new >= hi:\n            new = (eps + hi) / 2\n        if abs(new - eps) < tol * max(1.0, abs(eps)):\n            eps = new\n            res = integrate(field, l, eps, c, sign)\n            if res is None:\n                return None\n            nodes, deps, P, norm, m = res\n            if nodes != target:\n                return None\n            inv = 1.0 / math.sqrt(norm)\n            P = [v * inv for v in P]\n            # the integration carries the even points (RK4 steps of 2h); the odd points\n            # are filled by four-point Lagrange interpolation, fourth order like the rest\n            nn = len(P)\n            for i in range(1, nn - 1, 2):\n                if 3 <= i <= nn - 4:\n                    P[i] = (-P[i - 3] + 9 * P[i - 1] + 9 * P[i + 1] - P[i + 3]) / 16.0\n                else:\n                    P[i] = 0.5 * (P[i - 1] + P[i + 1])\n            return eps, P\n        eps = new\n        if eps >= 0:\n            return None\n    return None\n",
   "file": "tools/lowdin_walk.py",
   "line": 369,
   "status": "RECONSTRUCTED",
   "source": "the bound state (n, l): node count brackets, the correction refines"
  },
  "walk_potentials": {
   "python": "def potentials(grid, Z, N, D):\n    \"\"\"from D(x) = Σ q P² (= 4πr²ρ) return (V_cand, V_occ): the electronic part of the\n    field an ADDED electron sees (Hartree + local exchange; asymptote −(Z−N)/r with the\n    nucleus) and the part the OCCUPIED orbitals see (the same, Latter-tailed to\n    −(Z−N+1)/r).\"\"\"\n    r = grid.r\n    h = grid.h\n    n = grid.n\n    Q = cumint([D[i] * r[i] for i in range(n)], h)          # charge inside r\n    tail = cumint(D, h)                                     # ∫_0^x D dx'\n    total = tail[-1]\n    Vh = [Q[i] / r[i] + (total - tail[i]) for i in range(n)]\n    Vx = [-XC * (D[i] / (4 * math.pi * grid.r2[i])) ** (1.0 / 3.0) if D[i] > 0 else 0.0\n          for i in range(n)]\n    Vc = [Vh[i] + Vx[i] for i in range(n)]\n    lat = Z - N + 1                                         # Latter: V ≥ … in magnitude\n    Vo = [min(Vc[i], (Z - lat) / r[i]) for i in range(n)]   # total = Vo − Z/r ≤ −lat/r\n    return Vc, Vo\n",
   "file": "tools/lowdin_walk.py",
   "line": 455,
   "status": "RECONSTRUCTED",
   "source": "Hartree + Kohn-Sham local exchange from the density; Latter's tail for the occupied orbitals, none for the added electron"
  },
  "walk_scf": {
   "python": "def scf(grid, Z, cfg, c, Vstart=None, eps_start=None, mix=0.35, tol=1e-7, maxit=300,\n        log=None):\n    \"\"\"converge the field of the ion (Z, cfg).  Returns a dict with V_cand (electronic\n    part), orbitals {(n,l): (eps, P)}, iterations, converged flag, N.\"\"\"\n    N = sum(cfg.values())\n    n = grid.n\n    r = grid.r\n    if Vstart is None:\n        # a screened start: N−1 electrons at the Thomas–Fermi scale\n        a = 0.8853 / Z ** (1.0 / 3.0)\n        Vel = [max(N - 1, 0) * (1.0 - math.exp(-r[i] / a)) / r[i] for i in range(n)]\n    else:\n        Vel = list(Vstart)\n    eps = dict(eps_start or {})\n    orbs = {}\n    converged = False\n    it = 0\n    beta = mix\n    last_res = None\n    Vcand = Vel\n    for it in range(1, maxit + 1):\n        field = Field(grid, Z, Vel)\n        D = [0.0] * n\n        for nl, q in sorted(cfg.items()):\n            if q <= 0:\n                continue\n            sol = solve(field, nl[0], nl[1], c, eps.get(nl))\n            if sol is None:\n                sol = solve(field, nl[0], nl[1], c, None)\n            if sol is None:\n                raise RuntimeError(f\"Z={Z} cfg={cfg_str(cfg)}: no bound {ch_name(nl)}\")\n            e, P = sol\n            eps[nl] = e\n            orbs[nl] = (e, P)\n            for i in range(n):\n                D[i] += q * P[i] * P[i]\n        Vc, Vo = potentials(grid, Z, N, D)\n        res = max(abs(Vo[i] - Vel[i]) * r[i] for i in range(n))\n        if log:\n            log(f\"    scf it {it:3d}  residual {res:.3e}  beta {beta:.2f}\")\n        if res < tol:\n            converged = True\n            Vcand = Vc\n            break\n        if last_res is not None and res > last_res:\n            beta = max(0.05, beta * 0.5)\n        elif last_res is not None and res < 0.3 * last_res:\n            beta = min(0.6, beta * 1.25)\n        last_res = res\n        Vel = [(1 - beta) * Vel[i] + beta * Vo[i] for i in range(n)]\n        Vcand = Vc\n    return {\"Z\": Z, \"N\": N, \"cfg\": dict(cfg), \"V_cand\": Vcand, \"V_occ\": Vel,\n            \"orbitals\": orbs, \"eps\": eps, \"iterations\": it, \"converged\": converged,\n            \"D\": D}\n",
   "file": "tools/lowdin_walk.py",
   "line": 475,
   "status": "RECONSTRUCTED",
   "source": "the self-consistent field of the ion (Z, cfg), mixed to 1e-7"
  },
  "walk_frontier": {
   "python": "def frontier(cfg):\n    out = []\n    for n in range(1, N_MAX + 1):\n        for l in range(0, min(n, L_MAX + 1)):\n            if cfg.get((n, l), 0) < capacity((n, l)):\n                out.append((n, l))\n    return out\n",
   "file": "tools/lowdin_walk.py",
   "line": 531,
   "status": "RECONSTRUCTED",
   "source": "the unfilled (n, l) channels up to 8s and 8g"
  },
  "walk_scan": {
   "python": "def scan(grid, Z, state, c, eps_hint=None):\n    \"\"\"the candidate spectrum of one electron added to the frozen field: [(eps, (n,l))]\n    sorted deepest first.\"\"\"\n    field = Field(grid, Z, state[\"V_cand\"])\n    eps_hint = eps_hint or {}\n    spec = []\n    for nl in frontier(state[\"cfg\"]):\n        guess = eps_hint.get(nl)\n        if guess is None:\n            guess = -0.5 / nl[0] ** 2 * max(1.0, (Z - state[\"N\"])) ** 2\n            occ = state[\"eps\"].get(nl)\n            if occ is not None:\n                guess = occ * 0.7\n        sol = solve(field, nl[0], nl[1], c, guess)\n        if sol is None:\n            continue\n        spec.append((sol[0], nl))\n    spec.sort()\n    return spec\n",
   "file": "tools/lowdin_walk.py",
   "line": 540,
   "status": "RECONSTRUCTED",
   "source": "the candidate spectrum: one electron in each frontier channel of the frozen field, deepest first; the entrant is the first"
  },
  "walk_hf_operator": {
   "python": "def hf_operator(grid, pw, Z, orbs, cfg, a, Pa, occ_self):\n    \"\"\"V_loc (electronic part) and the exchange source X for channel a = (n, l) whose\n    current function is Pa; occ_self is the occupation the same-shell terms carry (q_a − 1\n    for an occupied orbital, q_a for an added electron in an open shell, 0 for an empty\n    channel).  orbs: {(n,l): P} of the occupied orbitals, cfg their occupations.\"\"\"\n    n = grid.n\n    r = grid.r\n    la = a[1]\n    Vel = [0.0] * n\n    X = [0.0] * n\n    for b, Pb in orbs.items():\n        qb = cfg[b]\n        if qb <= 0:\n            continue\n        if b == a:\n            continue\n        y0 = yk_over_r(grid, pw, Pb, Pb, 0)\n        for i in range(n):\n            Vel[i] += qb * y0[i]\n        lb = b[1]\n        for k in range(abs(la - lb), la + lb + 1, 2):\n            ak = a_k(la, k, lb)\n            if ak == 0.0:\n                continue\n            yk = yk_over_r(grid, pw, Pa, Pb, k)\n            f = 0.5 * qb * ak\n            for i in range(n):\n                X[i] += f * yk[i] * Pb[i]\n    if occ_self > 0:\n        Pself = orbs.get(a, Pa)\n        y0 = yk_over_r(grid, pw, Pself, Pself, 0)\n        for i in range(n):\n            Vel[i] += occ_self * y0[i]\n        fac = (2 * la + 1) / (4 * la + 1)\n        for k in range(2, 2 * la + 1, 2):\n            ak = a_k(la, k, la)\n            yk = yk_over_r(grid, pw, Pself, Pself, k)\n            f = occ_self * fac * ak\n            for i in range(n):\n                Vel[i] -= f * yk[i]\n    return Vel, X\n",
   "file": "tools/lowdin_walk.py",
   "line": 1010,
   "status": "RECONSTRUCTED",
   "source": "the Hartree-Fock operator of one channel: the local part (direct and same-shell average-of-configuration exchange) and the non-local exchange source from every other occupied orbital"
  },
  "walk_solve_inh": {
   "python": "def solve_inh(field, n, l, c, X, eps0, others=(), lam=(), tol=1e-8, maxit=60, trace=None, warm=None):\n    \"\"\"the orbital (n, l) of  (T + V_loc − ε)P = X + Σ_b λ_b P_b , normalised.  The source is\n    fixed, so the local problem's eigenvalue ε_pole (the homogeneous solve, whose node\n    count is reliable) is a pole of the solution's norm N(ε); the exchange operator is\n    positive, so the root lies below it, and there N falls from the pole, so N = 1 has one\n    root: bracketed in δ = ε_pole − ε and refined by a secant in ln N against ln δ.\n    Returns (eps, P, overlaps, multipliers): overlaps = [⟨P_b|P⟩ for b in others] of the\n    solution before its correction, and the multipliers λ_b + Δλ_b that make it orthogonal,\n    found by one exact Newton step at the root (one particular solution per partner); P is\n    the corrected, renormalised orbital.  Or None.  With no exchange source and no others it is the homogeneous solve.  The node\n    count is a diagnostic, not a bracket: a particular solution far from the pole carries\n    the nodes of its source.\"\"\"\n    g = field.grid\n    n_ = g.n\n    src = None\n    if X is not None and max(abs(v) for v in X) != 0.0:\n        src = list(X)\n    for Pb, lb in zip(others, lam):\n        if lb:\n            if src is None:\n                src = [0.0] * n_\n            for i in range(n_):\n                src[i] += lb * Pb[i]\n    if src is None:\n        sol = solve(field, n, l, c, eps0, tol=tol)\n        if sol is None:\n            return None\n        return sol[0], sol[1], [_dot(g, Pb, sol[1]) for Pb in others], list(lam)\n    hom = solve(field, n, l, c, (warm or {}).get(\"pole\", eps0))\n    if hom is None:\n        return None\n    e_pole = hom[0]\n    if warm is not None:\n        warm[\"pole\"] = e_pole\n    # the level below: the root must lie between it and the pole, or it is another state's\n    d_max = None\n    if n - 1 > l:\n        below = solve(field, n - 1, l, c, (warm or {}).get(\"below\"))\n        if below is not None:\n            if warm is not None:\n                warm[\"below\"] = below[0]\n            d_max = 0.999 * (e_pole - below[0])\n\n    def N_at(d):\n        res = shoot_multi(field, l, e_pole - d, c, [src])\n        if res is None:\n            return None\n        P = res[0][0]\n        N = _norm_even(g, P)\n        if not (N > 0.0) or N != N:\n            return None\n        return P, N\n\n    if warm is not None and warm.get(\"d\"):\n        d = warm[\"d\"]\n    else:\n        d = max(1e-6, 0.5 * (e_pole - eps0)) if (eps0 is not None and eps0 < e_pole) else max(1e-6, 1e-3 * abs(e_pole))\n    if d_max is not None and d > d_max:\n        d = 0.5 * d_max\n    res = N_at(d)\n    tries = 0\n    while res is None and tries < 20:\n        d *= 0.5\n        res = N_at(d)\n        tries += 1\n    if res is None:\n        return None\n    lo = hi = None\n    lnN = math.log(res[1])\n    if trace:\n        trace(f\"      inh pole {e_pole: .9f}  d0 {d:.3e} lnN {lnN: .3e}\")\n    best = None\n    if abs(lnN) < tol:\n        best = (d, res)\n    else:\n        # a warm start sits near the root: bracket by small factors first\n        grow = 1.25 if (warm is not None and warm.get(\"d\")) else 2.0\n        if lnN > 0:\n            lo = (d, lnN)\n            for _ in range(60):\n                d *= grow\n                if d_max is not None and d >= d_max:\n                    d = d_max\n                res = N_at(d)\n                if res is None:\n                    return None\n                lnN = math.log(res[1])\n                if trace:\n                    trace(f\"      inh grow  d {d:.3e} lnN {lnN: .3e}\")\n                if lnN < 0:\n                    hi = (d, lnN)\n                    break\n                lo = (d, lnN)\n                if d_max is not None and d >= d_max:\n                    break                # no root above the level below: another state's\n            if hi is None:\n                return None\n        else:\n            hi = (d, lnN)\n            for _ in range(60):\n                d /= grow\n                res = N_at(d)\n                if res is None:\n                    return None\n                lnN = math.log(res[1])\n                if trace:\n                    trace(f\"      inh shrink d {d:.3e} lnN {lnN: .3e}\")\n                if lnN > 0:\n                    lo = (d, lnN)\n                    break\n                hi = (d, lnN)\n            if lo is None:\n                return None\n        near = None\n        for it in range(maxit):\n            la, lb = math.log(lo[0]), math.log(hi[0])\n            t = lo[1] / (lo[1] - hi[1])\n            ld = la + t * (lb - la)\n            if not (la < ld < lb) or it % 4 == 3:\n                ld = 0.5 * (la + lb)\n            d = math.exp(ld)\n            res = N_at(d)\n            if res is None:\n                return None\n            lnN = math.log(res[1])\n            if trace:\n                trace(f\"      inh it {it:2d} d {d:.6e} eps {e_pole - d: .9f} lnN {lnN: .3e}\")\n            if abs(lnN) < tol:\n                best = (d, res)\n                break\n            if near is None or abs(lnN) < near[0]:\n                near = (abs(lnN), d, res)\n            if lnN > 0:\n                lo = (d, lnN)\n            else:\n                hi = (d, lnN)\n        if best is None:\n            if near is not None and near[0] < 1e-5:\n                best = (near[1], near[2])\n            else:\n                return None\n    d, res = best\n    P, N = res\n    inv = 1.0 / math.sqrt(N)\n    P = [v * inv for v in P]\n    eps = e_pole - d\n    if warm is not None:\n        warm[\"d\"] = d\n    ovl = [_dot_even(g, Pb, P) for Pb in others]\n    new_lam = list(lam)\n    if others:\n        # the multipliers that make THIS solution orthogonal, by one Newton step at the\n        # root: with v_b = (H_loc − ε)^{-1} P_b,  ⟨b'|P + Σ Δλ_b v_b⟩ = 0  is linear in Δλ\n        # and exact; the corrected P is renormalised (a second-order change)\n        res_v = shoot_multi(field, l, eps, c, list(others))\n        if res_v is not None:\n            vs = res_v[0]\n            nb = len(others)\n            Mx = [[_dot_even(g, others[bp], vs[b]) for b in range(nb)] for bp in range(nb)]\n            dl = _solve_small(Mx, [-o for o in ovl])\n            if dl is not None and all(abs(x) < 1e3 for x in dl):\n                for b in range(nb):\n                    vb = vs[b]\n                    x = dl[b]\n                    for i in range(0, g.n, 2):\n                        P[i] += x * vb[i]\n                N2 = _norm_even(g, P)\n                inv2 = 1.0 / math.sqrt(N2)\n                P = [v * inv2 for v in P]\n                new_lam = [lb + x for lb, x in zip(lam, dl)]\n    P = _fill_odd(P)\n    return eps, P, ovl, new_lam\n",
   "file": "tools/lowdin_walk.py",
   "line": 836,
   "status": "RECONSTRUCTED",
   "source": "the orbital of the inhomogeneous equation, its energy fixed by the norm condition below the local pole, its multipliers by one Newton step to orthogonality"
  },
  "walk_scf_hf": {
   "python": "def scf_hf(grid, Z, cfg, c, start, mix=0.7, tol=1e-7, maxit=150, log=None):\n    \"\"\"converge the Hartree–Fock field of the ion (Z, cfg) from the local-exchange state\n    `start`.\n\n    Orbitals of one ℓ are coupled by off-diagonal multipliers.  Each equation carries its\n    own, λ_ab: the equation is solved with them as a fixed source, and at the root one\n    exact Newton step (one particular solution per partner) moves them to the values that\n    make the solution orthogonal, so at convergence every equation holds exactly with an\n    orthonormal set.  What that leaves free is the rotation angle of each coupled pair\n    within its own span, and the variational condition q_a ε_ab = q_b ε_ba fixes it (Froese\n    Fischer's rotation analysis): after every sweep each pair takes a Newton step toward\n    the angle at which the average-of-configuration energy is stationary, with the exact\n    gradient 2(q_a⟨b|F_a|a⟩ − q_b⟨a|F_b|b⟩) from the state's orbitals and the curvature\n    from the energy at three angles (its one-electron part non-relativistic; the field's\n    operators stay Koelling–Harmon).  Nothing is Schmidt-orthogonalised: a Schmidt step\n    after mixing admits fixed points where the solved orbital differs from the stored one\n    by a multiple of its partner, and the equations then hold only up to that residual.\n    A pair of CLOSED shells carries no multiplier and no rotation: the energy is invariant\n    under their rotation, and only the canonical pair (the eigenfunctions of the one Fock\n    operator) carries the orbital energies the record compares.  The field is converged\n    when the orbitals, the eigenvalues, every overlap and every angle are still.  Returns\n    a state dict like scf()'s, with orbitals {(n,l): (eps, P)}; the field is the\n    orbitals.\"\"\"\n    N = sum(cfg.values())\n    pw = Powers(grid)\n    orbs = {nl: list(P) for nl, (e, P) in start[\"orbitals\"].items() if cfg.get(nl, 0) > 0}\n    eps = {nl: e for nl, (e, P) in start[\"orbitals\"].items() if cfg.get(nl, 0) > 0}\n    order = sorted(orbs, key=lambda k: (k[1], k[0]))\n\n    def coupled(a, b):\n        return a != b and a[1] == b[1] and not (cfg[a] == capacity(a) and cfg[b] == capacity(b))\n\n    pairs = [(a, b) for i, a in enumerate(order) for b in order[i + 1:] if coupled(a, b)]\n    lam_of = {a: {} for a in order}\n    rot = {}\n    warm = {a: {} for a in order}\n    converged = False\n    it = 0\n    beta = mix\n    last = None\n    d_rot = 0.0\n    o_max = 0.0\n    for it in range(1, maxit + 1):\n        de_max = 0.0\n        dp_max = 0.0\n        o_max = 0.0\n        for a in order:\n            qa = cfg[a]\n            others = [b for b in order if coupled(a, b)]\n            Vel, X = hf_operator(grid, pw, Z, orbs, cfg, a, orbs[a], qa - 1)\n            field = Field(grid, Z, Vel)\n            lam = [lam_of[a].get(b, 0.0) for b in others]\n            sol = solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam, warm=warm[a])\n            if sol is None:\n                warm[a] = {}\n                sol = solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam)\n            if sol is None:\n                if log:\n                    solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam, trace=log)\n                raise RuntimeError(f\"HF Z={Z} cfg={cfg_str(cfg)}: no solution for {ch_name(a)} at iteration {it} (eps {eps[a]})\")\n            e_new, P_new, ovl, new_lam = sol\n            for b, lb in zip(others, new_lam):\n                lam_of[a][b] = lb\n            o_max = max([o_max] + [abs(o) for o in ovl])\n            P_mix = [(1 - beta) * orbs[a][i] + beta * P_new[i] for i in range(grid.n)]\n            nrm = math.sqrt(_dot(grid, P_mix, P_mix))\n            P_mix = [v / nrm for v in P_mix]\n            dp = math.sqrt(_dot(grid, [P_mix[i] - orbs[a][i] for i in range(grid.n)],\n                                [P_mix[i] - orbs[a][i] for i in range(grid.n)]))\n            de_max = max(de_max, abs(e_new - eps[a]) / max(1.0, abs(e_new)))\n            dp_max = max(dp_max, dp)\n            orbs[a] = P_mix\n            eps[a] = e_new\n        # the rotation step: within each coupled pair's span the energy must be\n        # stationary; the exact gradient from the state, the curvature from the energy\n        d_rot = 0.0\n        for (a, b) in pairs:\n            if not HF_ROTATE:\n                break\n            g = pair_gradient(grid, pw, Z, orbs, cfg, a, b, eps, c)\n            mem = rot.get((a, b))\n            H = mem[1] if (mem is not None and it % 3 != 1) else pair_curvature(grid, pw, Z, orbs, cfg, a, b)\n            theta = rotate_pair(grid, pw, Z, orbs, cfg, a, b, g, H)\n            d_rot = max(d_rot, abs(theta))\n            rot[(a, b)] = (theta, H)\n        res = max(de_max, dp_max)\n        if log:\n            log(f\"    hf it {it:3d}  d_eps {de_max:.2e}  d_P {dp_max:.2e}  d_rot {d_rot:.2e}  ovl {o_max:.1e}  beta {beta:.2f}  \"\n                + \" \".join(f\"{ch_name(a)}:{eps[a]:.6f}\" for a in order))\n        if res < tol and d_rot < 1e-6 and o_max < 1e-6:\n            converged = True\n            break\n        if last is not None and res > 1.5 * last:\n            beta = max(0.3, beta * 0.7)\n        elif last is not None and res < 0.5 * last:\n            beta = min(0.9, beta * 1.1)\n        last = res\n    return {\"Z\": Z, \"N\": N, \"cfg\": dict(cfg), \"orbitals\": {a: (eps[a], orbs[a]) for a in order},\n            \"eps\": dict(eps), \"iterations\": it, \"converged\": converged, \"field\": \"hf\",\n            \"orbs\": orbs, \"pw\": pw, \"lam\": {ch_name(a): {ch_name(b): v for b, v in d.items()} for a, d in lam_of.items()},\n            \"d_rot\": d_rot, \"overlap\": o_max,\n            \"note\": \"\" if converged else f\"hf not converged in {it} sweeps: residual {last:.1e}, angle {d_rot:.1e}, overlap {o_max:.1e}\"}\n",
   "file": "tools/lowdin_walk.py",
   "line": 1242,
   "status": "RECONSTRUCTED",
   "source": "the Hartree-Fock field of the ion: per-equation multipliers and the pair rotation at which the energy is stationary"
  },
  "walk_scan_hf": {
   "python": "def scan_hf(grid, Z, state, c, lx_spec=None, log=None):\n    \"\"\"the candidate spectrum in the frozen Hartree–Fock field: one electron in each\n    frontier channel, its own exchange with every occupied orbital iterated to\n    self-consistency and its multipliers against the occupied orbitals of its ℓ iterated to\n    orthogonality (the occupied orbitals do not respond, so the equation is the projected\n    one and its multipliers are its own, moved by the Newton step of solve_inh until the\n    overlaps vanish).  Deepest first.\"\"\"\n    cfg = state[\"cfg\"]\n    orbs = state[\"orbs\"]\n    pw = state[\"pw\"]\n    hint = {nl: e for e, nl in (lx_spec or [])}\n    spec = []\n    for nl in frontier(cfg):\n        occ_self = cfg.get(nl, 0)\n        others = [b for b in orbs if b != nl and b[1] == nl[1]]\n        Pothers = [orbs[b] for b in others]\n        guess_e = hint.get(nl, state[\"eps\"].get(nl))\n        Pc = orbs.get(nl)\n        if Pc is None:\n            Vel0, _X0 = hf_operator(grid, pw, Z, orbs, cfg, nl, [0.0] * grid.n, 0)\n            f0 = Field(grid, Z, Vel0)\n            h0 = solve(f0, nl[0], nl[1], c, guess_e)\n            if h0 is None:\n                continue\n            guess_e, Pc = h0\n            if others:\n                Pc = _orthogonalise(grid, Pc, Pothers)\n        lam = [0.0] * len(others)\n        e_prev = None\n        ok = False\n        wm = {}\n        for k in range(60):\n            Vel, X = hf_operator(grid, pw, Z, orbs, cfg, nl, Pc, occ_self)\n            field = Field(grid, Z, Vel)\n            sol = solve_inh(field, nl[0], nl[1], c, X, guess_e, Pothers, lam, warm=wm)\n            if sol is None:\n                wm = {}\n                sol = solve_inh(field, nl[0], nl[1], c, X, guess_e, Pothers, lam)\n            if sol is None:\n                break\n            e_new, P_new, ovl, lam = sol\n            Pn = [0.5 * Pc[i] + 0.5 * P_new[i] for i in range(grid.n)] if e_prev is not None else P_new\n            nrm = math.sqrt(_dot(grid, Pn, Pn))\n            Pc = [v / nrm for v in Pn]\n            guess_e = e_new\n            if e_prev is not None and abs(e_new - e_prev) < 1e-9 * max(1.0, abs(e_new)) \\\n                    and max([abs(o) for o in ovl] or [0.0]) < 1e-7:\n                ok = True\n                break\n            e_prev = e_new\n        if e_prev is not None and guess_e < 0:\n            spec.append((guess_e, nl))\n            if log and not ok:\n                log(f\"    scan: {ch_name(nl)} not settled after 60 rounds\")\n    spec.sort()\n    return spec\n",
   "file": "tools/lowdin_walk.py",
   "line": 1346,
   "status": "RECONSTRUCTED",
   "source": "the candidate spectrum in the frozen Hartree-Fock field, each candidate's own exchange and multipliers iterated"
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
  },
  "walk": {
   "status": "RECONSTRUCTED",
   "instrument": "tools/lowdin_walk.py",
   "table": {
    "file": "LOWDIN-WALK.tsv",
    "bytes": 101340,
    "md5": "29fbb6405650b731e04a25b0b32cd51e",
    "rows": 238
   },
   "primary": "lx",
   "field": "Koelling-Harmon scalar-relativistic radial equation in a local-exchange (Kohn-Sham, V_x = -(3 rho/pi)^(1/3)) self-consistent field with Latter's tail: the Hartree-Fock-Slater construction, not the record's Hartree-Fock",
   "not_reproduced": "the record's non-local exchange; its collapse criterion; its correlation clause; its Z = 91 two-branch diagnostic",
   "fields": {
    "lx": {
     "field": "lx",
     "name": "Koelling-Harmon scalar-relativistic radial equation in a local-exchange (Kohn-Sham, V_x = -(3 rho/pi)^(1/3)) self-consistent field with Latter's tail: the Hartree-Fock-Slater construction, not the record's Hartree-Fock",
     "not_reproduced": "the record's non-local exchange; its collapse criterion; its correlation clause; its Z = 91 two-branch diagnostic",
     "entrants": [
      {
       "Z": 2,
       "symbol": "He",
       "c137": "1s",
       "cinf": "1s",
       "margin_c137": 1.13394831,
       "margin_cinf": 1.13390294,
       "displaced": false
      },
      {
       "Z": 3,
       "symbol": "Li",
       "c137": "2s",
       "cinf": "2s",
       "margin_c137": 0.07271971,
       "margin_cinf": 0.07269298,
       "displaced": false
      },
      {
       "Z": 4,
       "symbol": "Be",
       "c137": "2s",
       "cinf": "2s",
       "margin_c137": 0.13951638,
       "margin_cinf": 0.13941582,
       "displaced": false
      },
      {
       "Z": 5,
       "symbol": "B",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.32771191,
       "margin_cinf": 0.32781676,
       "displaced": false
      },
      {
       "Z": 6,
       "symbol": "C",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.45246834,
       "margin_cinf": 0.45265599,
       "displaced": false
      },
      {
       "Z": 7,
       "symbol": "N",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.57709058,
       "margin_cinf": 0.57738236,
       "displaced": false
      },
      {
       "Z": 8,
       "symbol": "O",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.70439978,
       "margin_cinf": 0.70482323,
       "displaced": false
      },
      {
       "Z": 9,
       "symbol": "F",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.83566261,
       "margin_cinf": 0.8362486,
       "displaced": false
      },
      {
       "Z": 10,
       "symbol": "Ne",
       "c137": "2p",
       "cinf": "2p",
       "margin_c137": 0.97146949,
       "margin_cinf": 0.97225154,
       "displaced": false
      },
      {
       "Z": 11,
       "symbol": "Na",
       "c137": "3s",
       "cinf": "3s",
       "margin_c137": 0.11069328,
       "margin_cinf": 0.11020783,
       "displaced": false
      },
      {
       "Z": 12,
       "symbol": "Mg",
       "c137": "3s",
       "cinf": "3s",
       "margin_c137": 0.15614253,
       "margin_cinf": 0.15532214,
       "displaced": false
      },
      {
       "Z": 13,
       "symbol": "Al",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.18699368,
       "margin_cinf": 0.18751574,
       "displaced": false
      },
      {
       "Z": 14,
       "symbol": "Si",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.26206871,
       "margin_cinf": 0.26279785,
       "displaced": false
      },
      {
       "Z": 15,
       "symbol": "P",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.34186874,
       "margin_cinf": 0.34275944,
       "displaced": false
      },
      {
       "Z": 16,
       "symbol": "S",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.42476429,
       "margin_cinf": 0.4258143,
       "displaced": false
      },
      {
       "Z": 17,
       "symbol": "Cl",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.51084732,
       "margin_cinf": 0.51206181,
       "displaced": false
      },
      {
       "Z": 18,
       "symbol": "Ar",
       "c137": "3p",
       "cinf": "3p",
       "margin_c137": 0.60030039,
       "margin_cinf": 0.60168329,
       "displaced": false
      },
      {
       "Z": 19,
       "symbol": "K",
       "c137": "4s",
       "cinf": "4s",
       "margin_c137": 0.08501865,
       "margin_cinf": 0.08214046,
       "displaced": false
      },
      {
       "Z": 20,
       "symbol": "Ca",
       "c137": "4s",
       "cinf": "4s",
       "margin_c137": 0.02722139,
       "margin_cinf": 0.02157626,
       "displaced": false
      },
      {
       "Z": 21,
       "symbol": "Sc",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.25256387,
       "margin_cinf": 0.25986696,
       "displaced": false
      },
      {
       "Z": 22,
       "symbol": "Ti",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.30643274,
       "margin_cinf": 0.31448372,
       "displaced": false
      },
      {
       "Z": 23,
       "symbol": "V",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.35576853,
       "margin_cinf": 0.36475614,
       "displaced": false
      },
      {
       "Z": 24,
       "symbol": "Cr",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.40222727,
       "margin_cinf": 0.41227912,
       "displaced": false
      },
      {
       "Z": 25,
       "symbol": "Mn",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.4466174,
       "margin_cinf": 0.45784223,
       "displaced": false
      },
      {
       "Z": 26,
       "symbol": "Fe",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.48940838,
       "margin_cinf": 0.50190759,
       "displaced": false
      },
      {
       "Z": 27,
       "symbol": "Co",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.53090397,
       "margin_cinf": 0.54477539,
       "displaced": false
      },
      {
       "Z": 28,
       "symbol": "Ni",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.57131188,
       "margin_cinf": 0.58665368,
       "displaced": false
      },
      {
       "Z": 29,
       "symbol": "Cu",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.61078286,
       "margin_cinf": 0.62769586,
       "displaced": false
      },
      {
       "Z": 30,
       "symbol": "Zn",
       "c137": "3d",
       "cinf": "3d",
       "margin_c137": 0.64943218,
       "margin_cinf": 0.66801488,
       "displaced": false
      },
      {
       "Z": 31,
       "symbol": "Ga",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.18923114,
       "margin_cinf": 0.19099953,
       "displaced": false
      },
      {
       "Z": 32,
       "symbol": "Ge",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.24699881,
       "margin_cinf": 0.24963301,
       "displaced": false
      },
      {
       "Z": 33,
       "symbol": "As",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.31006958,
       "margin_cinf": 0.31308032,
       "displaced": false
      },
      {
       "Z": 34,
       "symbol": "Se",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.374441,
       "margin_cinf": 0.37774556,
       "displaced": false
      },
      {
       "Z": 35,
       "symbol": "Br",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.44008207,
       "margin_cinf": 0.44365688,
       "displaced": false
      },
      {
       "Z": 36,
       "symbol": "Kr",
       "c137": "4p",
       "cinf": "4p",
       "margin_c137": 0.50725359,
       "margin_cinf": 0.5110798,
       "displaced": false
      },
      {
       "Z": 37,
       "symbol": "Rb",
       "c137": "5s",
       "cinf": "5s",
       "margin_c137": 0.08574849,
       "margin_cinf": 0.07690085,
       "displaced": false
      },
      {
       "Z": 38,
       "symbol": "Sr",
       "c137": "5s",
       "cinf": "5s",
       "margin_c137": 0.06223826,
       "margin_cinf": 0.04775689,
       "displaced": false
      },
      {
       "Z": 39,
       "symbol": "Y",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.13406907,
       "margin_cinf": 0.14948669,
       "displaced": false
      },
      {
       "Z": 40,
       "symbol": "Zr",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.18864697,
       "margin_cinf": 0.20555757,
       "displaced": false
      },
      {
       "Z": 41,
       "symbol": "Nb",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.24063408,
       "margin_cinf": 0.25934186,
       "displaced": false
      },
      {
       "Z": 42,
       "symbol": "Mo",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.29169653,
       "margin_cinf": 0.31235959,
       "displaced": false
      },
      {
       "Z": 43,
       "symbol": "Tc",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.34243385,
       "margin_cinf": 0.36517488,
       "displaced": false
      },
      {
       "Z": 44,
       "symbol": "Ru",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.39311948,
       "margin_cinf": 0.41805136,
       "displaced": false
      },
      {
       "Z": 45,
       "symbol": "Rh",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.44389768,
       "margin_cinf": 0.47113178,
       "displaced": false
      },
      {
       "Z": 46,
       "symbol": "Pd",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.49484864,
       "margin_cinf": 0.52449725,
       "displaced": false
      },
      {
       "Z": 47,
       "symbol": "Ag",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.54602173,
       "margin_cinf": 0.57820065,
       "displaced": false
      },
      {
       "Z": 48,
       "symbol": "Cd",
       "c137": "4d",
       "cinf": "4d",
       "margin_c137": 0.5974453,
       "margin_cinf": 0.63227257,
       "displaced": false
      },
      {
       "Z": 49,
       "symbol": "In",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.17422662,
       "margin_cinf": 0.17792747,
       "displaced": false
      },
      {
       "Z": 50,
       "symbol": "Sn",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.2202816,
       "margin_cinf": 0.22565264,
       "displaced": false
      },
      {
       "Z": 51,
       "symbol": "Sb",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.27053465,
       "margin_cinf": 0.27654622,
       "displaced": false
      },
      {
       "Z": 52,
       "symbol": "Te",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.32132842,
       "margin_cinf": 0.32780917,
       "displaced": false
      },
      {
       "Z": 53,
       "symbol": "I",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.37258928,
       "margin_cinf": 0.37949654,
       "displaced": false
      },
      {
       "Z": 54,
       "symbol": "Xe",
       "c137": "5p",
       "cinf": "5p",
       "margin_c137": 0.42455445,
       "margin_cinf": 0.4318585,
       "displaced": false
      },
      {
       "Z": 55,
       "symbol": "Cs",
       "c137": "6s",
       "cinf": "6s",
       "margin_c137": 0.0487688,
       "margin_cinf": 0.02908518,
       "displaced": false
      },
      {
       "Z": 56,
       "symbol": "Ba",
       "c137": "6s",
       "cinf": "5d",
       "margin_c137": 0.0248226,
       "margin_cinf": 0.00366088,
       "displaced": true
      },
      {
       "Z": 57,
       "symbol": "La",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.08977633,
       "margin_cinf": 0.1663153,
       "displaced": false
      },
      {
       "Z": 58,
       "symbol": "Ce",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.1285128,
       "margin_cinf": 0.20729222,
       "displaced": false
      },
      {
       "Z": 59,
       "symbol": "Pr",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.16125681,
       "margin_cinf": 0.24311218,
       "displaced": false
      },
      {
       "Z": 60,
       "symbol": "Nd",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.18949479,
       "margin_cinf": 0.27495586,
       "displaced": false
      },
      {
       "Z": 61,
       "symbol": "Pm",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.21410963,
       "margin_cinf": 0.30356865,
       "displaced": false
      },
      {
       "Z": 62,
       "symbol": "Sm",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.23568564,
       "margin_cinf": 0.32945591,
       "displaced": false
      },
      {
       "Z": 63,
       "symbol": "Eu",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.25463588,
       "margin_cinf": 0.3529869,
       "displaced": false
      },
      {
       "Z": 64,
       "symbol": "Gd",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.27126881,
       "margin_cinf": 0.37444073,
       "displaced": false
      },
      {
       "Z": 65,
       "symbol": "Tb",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.2858233,
       "margin_cinf": 0.39403677,
       "displaced": false
      },
      {
       "Z": 66,
       "symbol": "Dy",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.29848938,
       "margin_cinf": 0.4119511,
       "displaced": false
      },
      {
       "Z": 67,
       "symbol": "Ho",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.30942215,
       "margin_cinf": 0.42786616,
       "displaced": false
      },
      {
       "Z": 68,
       "symbol": "Er",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.3187521,
       "margin_cinf": 0.43777555,
       "displaced": false
      },
      {
       "Z": 69,
       "symbol": "Tm",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.32658821,
       "margin_cinf": 0.44624273,
       "displaced": false
      },
      {
       "Z": 70,
       "symbol": "Yb",
       "c137": "4f",
       "cinf": "4f",
       "margin_c137": 0.33302558,
       "margin_cinf": 0.45337041,
       "displaced": false
      },
      {
       "Z": 71,
       "symbol": "Lu",
       "c137": "5d",
       "cinf": "6s",
       "margin_c137": 0.09956176,
       "margin_cinf": 0.02138542,
       "displaced": true
      },
      {
       "Z": 72,
       "symbol": "Hf",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.14508006,
       "margin_cinf": 0.19107801,
       "displaced": false
      },
      {
       "Z": 73,
       "symbol": "Ta",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.18873486,
       "margin_cinf": 0.23904386,
       "displaced": false
      },
      {
       "Z": 74,
       "symbol": "W",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.23184969,
       "margin_cinf": 0.28653696,
       "displaced": false
      },
      {
       "Z": 75,
       "symbol": "Re",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.27489827,
       "margin_cinf": 0.33402148,
       "displaced": false
      },
      {
       "Z": 76,
       "symbol": "Os",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.31808181,
       "margin_cinf": 0.38171096,
       "displaced": false
      },
      {
       "Z": 77,
       "symbol": "Ir",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.36150033,
       "margin_cinf": 0.42971975,
       "displaced": false
      },
      {
       "Z": 78,
       "symbol": "Pt",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.40520783,
       "margin_cinf": 0.47811573,
       "displaced": false
      },
      {
       "Z": 79,
       "symbol": "Au",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.44923505,
       "margin_cinf": 0.5269423,
       "displaced": false
      },
      {
       "Z": 80,
       "symbol": "Hg",
       "c137": "5d",
       "cinf": "5d",
       "margin_c137": 0.4935998,
       "margin_cinf": 0.57622696,
       "displaced": false
      },
      {
       "Z": 81,
       "symbol": "Tl",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.16213529,
       "margin_cinf": 0.17307262,
       "displaced": false
      },
      {
       "Z": 82,
       "symbol": "Pb",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.19975613,
       "margin_cinf": 0.21558549,
       "displaced": false
      },
      {
       "Z": 83,
       "symbol": "Bi",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.24329494,
       "margin_cinf": 0.26090524,
       "displaced": false
      },
      {
       "Z": 84,
       "symbol": "Po",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.28725644,
       "margin_cinf": 0.30618315,
       "displaced": false
      },
      {
       "Z": 85,
       "symbol": "At",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.33126482,
       "margin_cinf": 0.35142201,
       "displaced": false
      },
      {
       "Z": 86,
       "symbol": "Rn",
       "c137": "6p",
       "cinf": "6p",
       "margin_c137": 0.37550568,
       "margin_cinf": 0.39685416,
       "displaced": false
      },
      {
       "Z": 87,
       "symbol": "Fr",
       "c137": "7s",
       "cinf": "7s",
       "margin_c137": 0.07128084,
       "margin_cinf": 0.0210456,
       "displaced": false
      },
      {
       "Z": 88,
       "symbol": "Ra",
       "c137": "7s",
       "cinf": "6d",
       "margin_c137": 0.06211879,
       "margin_cinf": 0.00668457,
       "displaced": true
      },
      {
       "Z": 89,
       "symbol": "Ac",
       "c137": "6d",
       "cinf": "5f",
       "margin_c137": 0.05553556,
       "margin_cinf": 0.08089383,
       "displaced": true
      },
      {
       "Z": 90,
       "symbol": "Th",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.0613636,
       "margin_cinf": 0.13397204,
       "displaced": false
      },
      {
       "Z": 91,
       "symbol": "Pa",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.10903334,
       "margin_cinf": 0.18464212,
       "displaced": false
      },
      {
       "Z": 92,
       "symbol": "U",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.15423692,
       "margin_cinf": 0.23367542,
       "displaced": false
      },
      {
       "Z": 93,
       "symbol": "Np",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.19761097,
       "margin_cinf": 0.28147777,
       "displaced": false
      },
      {
       "Z": 94,
       "symbol": "Pu",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.23950085,
       "margin_cinf": 0.32829416,
       "displaced": false
      },
      {
       "Z": 95,
       "symbol": "Am",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.28011752,
       "margin_cinf": 0.37428504,
       "displaced": false
      },
      {
       "Z": 96,
       "symbol": "Cm",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.31959833,
       "margin_cinf": 0.41956192,
       "displaced": false
      },
      {
       "Z": 97,
       "symbol": "Bk",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.35803847,
       "margin_cinf": 0.46420754,
       "displaced": false
      },
      {
       "Z": 98,
       "symbol": "Cf",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.39550524,
       "margin_cinf": 0.50828154,
       "displaced": false
      },
      {
       "Z": 99,
       "symbol": "Es",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.43204756,
       "margin_cinf": 0.55183139,
       "displaced": false
      },
      {
       "Z": 100,
       "symbol": "Fm",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.46770051,
       "margin_cinf": 0.59489413,
       "displaced": false
      },
      {
       "Z": 101,
       "symbol": "Md",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.50249176,
       "margin_cinf": 0.63749947,
       "displaced": false
      },
      {
       "Z": 102,
       "symbol": "No",
       "c137": "5f",
       "cinf": "5f",
       "margin_c137": 0.5364391,
       "margin_cinf": 0.67967147,
       "displaced": false
      },
      {
       "Z": 103,
       "symbol": "Lr",
       "c137": "5f",
       "cinf": "6d",
       "margin_c137": 0.56955611,
       "margin_cinf": 0.01349532,
       "displaced": true
      },
      {
       "Z": 104,
       "symbol": "Rf",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.117501,
       "margin_cinf": 0.04617956,
       "displaced": false
      },
      {
       "Z": 105,
       "symbol": "Db",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.15430371,
       "margin_cinf": 0.07846424,
       "displaced": false
      },
      {
       "Z": 106,
       "symbol": "Sg",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.19018129,
       "margin_cinf": 0.11091521,
       "displaced": false
      },
      {
       "Z": 107,
       "symbol": "Bh",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.22570242,
       "margin_cinf": 0.14374659,
       "displaced": false
      },
      {
       "Z": 108,
       "symbol": "Hs",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.26111736,
       "margin_cinf": 0.17704325,
       "displaced": false
      },
      {
       "Z": 109,
       "symbol": "Mt",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.2965495,
       "margin_cinf": 0.21083927,
       "displaced": false
      },
      {
       "Z": 110,
       "symbol": "Ds",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.33206276,
       "margin_cinf": 0.24514611,
       "displaced": false
      },
      {
       "Z": 111,
       "symbol": "Rg",
       "c137": "6d",
       "cinf": "6d",
       "margin_c137": 0.36769017,
       "margin_cinf": 0.27996639,
       "displaced": false
      },
      {
       "Z": 112,
       "symbol": "Cn",
       "c137": "6d",
       "cinf": "7s",
       "margin_c137": 0.40344841,
       "margin_cinf": 0.15991313,
       "displaced": true
      },
      {
       "Z": 113,
       "symbol": "Nh",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.13272835,
       "margin_cinf": 0.16384594,
       "displaced": false
      },
      {
       "Z": 114,
       "symbol": "Fl",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.15895619,
       "margin_cinf": 0.20182501,
       "displaced": false
      },
      {
       "Z": 115,
       "symbol": "Mc",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.19339546,
       "margin_cinf": 0.2418,
       "displaced": false
      },
      {
       "Z": 116,
       "symbol": "Lv",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.22817626,
       "margin_cinf": 0.28145921,
       "displaced": false
      },
      {
       "Z": 117,
       "symbol": "Ts",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.26259136,
       "margin_cinf": 0.32083452,
       "displaced": false
      },
      {
       "Z": 118,
       "symbol": "Og",
       "c137": "7p",
       "cinf": "7p",
       "margin_c137": 0.29674094,
       "margin_cinf": 0.36014508,
       "displaced": false
      },
      {
       "Z": 119,
       "symbol": "Uue",
       "c137": "8s",
       "cinf": "8s",
       "margin_c137": 0.11497651,
       "margin_cinf": 3.532e-05,
       "displaced": false
      },
      {
       "Z": 120,
       "symbol": "Ubn",
       "c137": "8s",
       "cinf": "6f",
       "margin_c137": 0.12307422,
       "margin_cinf": 0.09095094,
       "displaced": true
      }
     ]
    }
   },
   "c": {
    "c137": 137.035999,
    "cinf": null
   },
   "grid": {
    "r_min": 9.999999999999994e-08,
    "r_max": 299.43709108793183,
    "h": 0.005,
    "points": 4365
   },
   "summary": {
    "status": "RECONSTRUCTED",
    "rows": 238,
    "settings": {
     "lx:137.035999": {
      "field": "lx",
      "field_name": "local exchange (Kohn–Sham) with Latter's tail: Hartree–Fock–Slater",
      "c": "137.035999",
      "rows": 119,
      "Z_first": 2,
      "Z_last": 120,
      "not_converged": [],
      "openings": [
       {
        "channel": "1s",
        "Z": 2
       },
       {
        "channel": "2s",
        "Z": 3
       },
       {
        "channel": "2p",
        "Z": 5
       },
       {
        "channel": "3s",
        "Z": 11
       },
       {
        "channel": "3p",
        "Z": 13
       },
       {
        "channel": "4s",
        "Z": 19
       },
       {
        "channel": "3d",
        "Z": 21
       },
       {
        "channel": "4p",
        "Z": 31
       },
       {
        "channel": "5s",
        "Z": 37
       },
       {
        "channel": "4d",
        "Z": 39
       },
       {
        "channel": "5p",
        "Z": 49
       },
       {
        "channel": "6s",
        "Z": 55
       },
       {
        "channel": "4f",
        "Z": 57
       },
       {
        "channel": "5d",
        "Z": 71
       },
       {
        "channel": "6p",
        "Z": 81
       },
       {
        "channel": "7s",
        "Z": 87
       },
       {
        "channel": "6d",
        "Z": 89
       },
       {
        "channel": "5f",
        "Z": 90
       },
       {
        "channel": "7p",
        "Z": 113
       },
       {
        "channel": "8s",
        "Z": 119
       }
      ],
      "openings_observed": [
       {
        "channel": "1s",
        "Z": 1
       },
       {
        "channel": "2s",
        "Z": 3
       },
       {
        "channel": "2p",
        "Z": 5
       },
       {
        "channel": "3s",
        "Z": 11
       },
       {
        "channel": "3p",
        "Z": 13
       },
       {
        "channel": "4s",
        "Z": 19
       },
       {
        "channel": "3d",
        "Z": 21
       },
       {
        "channel": "4p",
        "Z": 31
       },
       {
        "channel": "5s",
        "Z": 37
       },
       {
        "channel": "4d",
        "Z": 39
       },
       {
        "channel": "5p",
        "Z": 49
       },
       {
        "channel": "6s",
        "Z": 55
       },
       {
        "channel": "5d",
        "Z": 57
       },
       {
        "channel": "4f",
        "Z": 58
       },
       {
        "channel": "6p",
        "Z": 81
       },
       {
        "channel": "7s",
        "Z": 87
       },
       {
        "channel": "6d",
        "Z": 89
       },
       {
        "channel": "5f",
        "Z": 91
       },
       {
        "channel": "7p",
        "Z": 103
       }
      ],
      "same_order": false,
      "openings_displaced": [
       {
        "channel": "1s",
        "Z": 2,
        "observed_Z": 1
       },
       {
        "channel": "4f",
        "Z": 57,
        "observed_Z": 58
       },
       {
        "channel": "5d",
        "Z": 71,
        "observed_Z": 57
       },
       {
        "channel": "5f",
        "Z": 90,
        "observed_Z": 91
       },
       {
        "channel": "7p",
        "Z": 113,
        "observed_Z": 103
       }
      ],
      "clause1_violations": [],
      "clause2_exceptions": [
       "6d@89 before 5f@90"
      ],
      "scored": 107,
      "agree": 96,
      "disagree": [
       {
        "symbol": "Mn",
        "Z": 25,
        "entrant": "3d",
        "observed_gain": "4s"
       },
       {
        "symbol": "Zn",
        "Z": 30,
        "entrant": "3d",
        "observed_gain": "4s"
       },
       {
        "symbol": "Tc",
        "Z": 43,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "Ag",
        "Z": 47,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "Cd",
        "Z": 48,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "La",
        "Z": 57,
        "entrant": "4f",
        "observed_gain": "5d"
       },
       {
        "symbol": "Gd",
        "Z": 64,
        "entrant": "4f",
        "observed_gain": "5d"
       },
       {
        "symbol": "Hg",
        "Z": 80,
        "entrant": "5d",
        "observed_gain": "6s"
       },
       {
        "symbol": "Th",
        "Z": 90,
        "entrant": "5f",
        "observed_gain": "6d"
       },
       {
        "symbol": "Cm",
        "Z": 96,
        "entrant": "5f",
        "observed_gain": "6d"
       },
       {
        "symbol": "Lr",
        "Z": 103,
        "entrant": "5f",
        "observed_gain": "7p"
       }
      ],
      "cfg_identical": 84,
      "g_pins": [
       {
        "channel": "5g",
        "offered": 119,
        "max_dev": 0.00041835999999999957
       },
       {
        "channel": "6g",
        "offered": 119,
        "max_dev": 0.0003672811111111122
       },
       {
        "channel": "7g",
        "offered": 119,
        "max_dev": 0.00027486836734694035
       },
       {
        "channel": "8g",
        "offered": 119,
        "max_dev": 0.00020172000000000072
       }
      ],
      "smallest_margins": [
       {
        "symbol": "Ba",
        "Z": 56,
        "entrant": "6s",
        "runner_up": "5d",
        "margin": 0.0248226
       },
       {
        "symbol": "Ca",
        "Z": 20,
        "entrant": "4s",
        "runner_up": "3d",
        "margin": 0.02722139
       },
       {
        "symbol": "Cs",
        "Z": 55,
        "entrant": "6s",
        "runner_up": "5d",
        "margin": 0.0487688
       },
       {
        "symbol": "Ac",
        "Z": 89,
        "entrant": "6d",
        "runner_up": "5f",
        "margin": 0.05553556
       },
       {
        "symbol": "Th",
        "Z": 90,
        "entrant": "5f",
        "runner_up": "6d",
        "margin": 0.0613636
       }
      ]
     },
     "lx:inf": {
      "field": "lx",
      "field_name": "local exchange (Kohn–Sham) with Latter's tail: Hartree–Fock–Slater",
      "c": "inf",
      "rows": 119,
      "Z_first": 2,
      "Z_last": 120,
      "not_converged": [],
      "openings": [
       {
        "channel": "1s",
        "Z": 2
       },
       {
        "channel": "2s",
        "Z": 3
       },
       {
        "channel": "2p",
        "Z": 5
       },
       {
        "channel": "3s",
        "Z": 11
       },
       {
        "channel": "3p",
        "Z": 13
       },
       {
        "channel": "4s",
        "Z": 19
       },
       {
        "channel": "3d",
        "Z": 21
       },
       {
        "channel": "4p",
        "Z": 31
       },
       {
        "channel": "5s",
        "Z": 37
       },
       {
        "channel": "4d",
        "Z": 39
       },
       {
        "channel": "5p",
        "Z": 49
       },
       {
        "channel": "6s",
        "Z": 55
       },
       {
        "channel": "5d",
        "Z": 56
       },
       {
        "channel": "4f",
        "Z": 57
       },
       {
        "channel": "6p",
        "Z": 81
       },
       {
        "channel": "7s",
        "Z": 87
       },
       {
        "channel": "6d",
        "Z": 88
       },
       {
        "channel": "5f",
        "Z": 89
       },
       {
        "channel": "7p",
        "Z": 113
       },
       {
        "channel": "8s",
        "Z": 119
       },
       {
        "channel": "6f",
        "Z": 120
       }
      ],
      "openings_observed": [
       {
        "channel": "1s",
        "Z": 1
       },
       {
        "channel": "2s",
        "Z": 3
       },
       {
        "channel": "2p",
        "Z": 5
       },
       {
        "channel": "3s",
        "Z": 11
       },
       {
        "channel": "3p",
        "Z": 13
       },
       {
        "channel": "4s",
        "Z": 19
       },
       {
        "channel": "3d",
        "Z": 21
       },
       {
        "channel": "4p",
        "Z": 31
       },
       {
        "channel": "5s",
        "Z": 37
       },
       {
        "channel": "4d",
        "Z": 39
       },
       {
        "channel": "5p",
        "Z": 49
       },
       {
        "channel": "6s",
        "Z": 55
       },
       {
        "channel": "5d",
        "Z": 57
       },
       {
        "channel": "4f",
        "Z": 58
       },
       {
        "channel": "6p",
        "Z": 81
       },
       {
        "channel": "7s",
        "Z": 87
       },
       {
        "channel": "6d",
        "Z": 89
       },
       {
        "channel": "5f",
        "Z": 91
       },
       {
        "channel": "7p",
        "Z": 103
       }
      ],
      "same_order": true,
      "openings_displaced": [
       {
        "channel": "1s",
        "Z": 2,
        "observed_Z": 1
       },
       {
        "channel": "5d",
        "Z": 56,
        "observed_Z": 57
       },
       {
        "channel": "4f",
        "Z": 57,
        "observed_Z": 58
       },
       {
        "channel": "6d",
        "Z": 88,
        "observed_Z": 89
       },
       {
        "channel": "5f",
        "Z": 89,
        "observed_Z": 91
       },
       {
        "channel": "7p",
        "Z": 113,
        "observed_Z": 103
       }
      ],
      "clause1_violations": [],
      "clause2_exceptions": [
       "5d@56 before 4f@57",
       "6d@88 before 5f@89"
      ],
      "scored": 107,
      "agree": 92,
      "disagree": [
       {
        "symbol": "Mn",
        "Z": 25,
        "entrant": "3d",
        "observed_gain": "4s"
       },
       {
        "symbol": "Zn",
        "Z": 30,
        "entrant": "3d",
        "observed_gain": "4s"
       },
       {
        "symbol": "Tc",
        "Z": 43,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "Ag",
        "Z": 47,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "Cd",
        "Z": 48,
        "entrant": "4d",
        "observed_gain": "5s"
       },
       {
        "symbol": "Ba",
        "Z": 56,
        "entrant": "5d",
        "observed_gain": "6s"
       },
       {
        "symbol": "La",
        "Z": 57,
        "entrant": "4f",
        "observed_gain": "5d"
       },
       {
        "symbol": "Gd",
        "Z": 64,
        "entrant": "4f",
        "observed_gain": "5d"
       },
       {
        "symbol": "Lu",
        "Z": 71,
        "entrant": "6s",
        "observed_gain": "5d"
       },
       {
        "symbol": "Hg",
        "Z": 80,
        "entrant": "5d",
        "observed_gain": "6s"
       },
       {
        "symbol": "Ra",
        "Z": 88,
        "entrant": "6d",
        "observed_gain": "7s"
       },
       {
        "symbol": "Ac",
        "Z": 89,
        "entrant": "5f",
        "observed_gain": "6d"
       },
       {
        "symbol": "Th",
        "Z": 90,
        "entrant": "5f",
        "observed_gain": "6d"
       },
       {
        "symbol": "Cm",
        "Z": 96,
        "entrant": "5f",
        "observed_gain": "6d"
       },
       {
        "symbol": "Lr",
        "Z": 103,
        "entrant": "6d",
        "observed_gain": "7p"
       }
      ],
      "cfg_identical": 61,
      "g_pins": [
       {
        "channel": "5g",
        "offered": 119,
        "max_dev": 0.20896583000000002
       },
       {
        "channel": "6g",
        "offered": 119,
        "max_dev": 0.007059461111111113
       },
       {
        "channel": "7g",
        "offered": 119,
        "max_dev": 0.00447856836734694
       },
       {
        "channel": "8g",
        "offered": 119,
        "max_dev": 0.0029645599999999998
       }
      ],
      "smallest_margins": [
       {
        "symbol": "Uue",
        "Z": 119,
        "entrant": "8s",
        "runner_up": "7d",
        "margin": 3.532e-05
       },
       {
        "symbol": "Ba",
        "Z": 56,
        "entrant": "5d",
        "runner_up": "6s",
        "margin": 0.00366088
       },
       {
        "symbol": "Ra",
        "Z": 88,
        "entrant": "6d",
        "runner_up": "7s",
        "margin": 0.00668457
       },
       {
        "symbol": "Lr",
        "Z": 103,
        "entrant": "6d",
        "runner_up": "7s",
        "margin": 0.01349532
       },
       {
        "symbol": "Fr",
        "Z": 87,
        "entrant": "7s",
        "runner_up": "6d",
        "margin": 0.0210456
       }
      ]
     }
    },
    "compare": {
     "field": "lx",
     "field_name": "local exchange (Kohn–Sham) with Latter's tail: Hartree–Fock–Slater",
     "Z_first": 2,
     "Z_last": 120,
     "rows": 119,
     "displaced": [
      {
       "symbol": "Ba",
       "Z": 56,
       "entrant_c137": "6s",
       "entrant_cinf": "5d"
      },
      {
       "symbol": "Lu",
       "Z": 71,
       "entrant_c137": "5d",
       "entrant_cinf": "6s"
      },
      {
       "symbol": "Ra",
       "Z": 88,
       "entrant_c137": "7s",
       "entrant_cinf": "6d"
      },
      {
       "symbol": "Ac",
       "Z": 89,
       "entrant_c137": "6d",
       "entrant_cinf": "5f"
      },
      {
       "symbol": "Lr",
       "Z": 103,
       "entrant_c137": "5f",
       "entrant_cinf": "6d"
      },
      {
       "symbol": "Cn",
       "Z": 112,
       "entrant_c137": "6d",
       "entrant_cinf": "7s"
      },
      {
       "symbol": "Ubn",
       "Z": 120,
       "entrant_c137": "8s",
       "entrant_cinf": "6f"
      }
     ],
     "eleven_1706": [
      "Mn",
      "Zn",
      "Ag",
      "Cd",
      "Nd",
      "Pm",
      "Sm",
      "Lu",
      "Hg",
      "Lr",
      "Rf"
     ],
     "in_eleven": [
      "Lu",
      "Lr"
     ],
     "not_in_eleven": [
      "Ba",
      "Ra",
      "Ac",
      "Cn",
      "Ubn"
     ],
     "eleven_not_displaced": [
      "Mn",
      "Zn",
      "Ag",
      "Cd",
      "Nd",
      "Pm",
      "Sm",
      "Hg",
      "Rf"
     ],
     "thorium": {
      "entrant_c137": "5f",
      "entrant_cinf": "5f",
      "identical": true,
      "top3_c137": [
       "5f:-0.40022777",
       "6d:-0.33886416",
       "7p:-0.20647270"
      ],
      "top3_cinf": [
       "5f:-0.44422213",
       "6d:-0.31025009",
       "7s:-0.27264593"
      ]
     },
     "named_rows": [
      {
       "symbol": "Mn",
       "Z": 25,
       "top3_c137": [
        "3d:-0.74138426",
        "4p:-0.29476685",
        "5s:-0.12289774"
       ],
       "top3_cinf": [
        "3d:-0.75313672",
        "4p:-0.29529450",
        "5s:-0.12235490"
       ]
      },
      {
       "symbol": "Zn",
       "Z": 30,
       "top3_c137": [
        "3d:-0.96938076",
        "4p:-0.31994857",
        "5s:-0.13260640"
       ],
       "top3_cinf": [
        "3d:-0.98864532",
        "4p:-0.32063045",
        "5s:-0.13167224"
       ]
      },
      {
       "symbol": "Ag",
       "Z": 47,
       "top3_c137": [
        "4d:-0.83970830",
        "5p:-0.29368657",
        "6s:-0.12375895"
       ],
       "top3_cinf": [
        "4d:-0.87291006",
        "5p:-0.29470942",
        "6s:-0.12164596"
       ]
      },
      {
       "symbol": "Cd",
       "Z": 48,
       "top3_c137": [
        "4d:-0.89489438",
        "5p:-0.29744908",
        "6s:-0.12520239"
       ],
       "top3_cinf": [
        "4d:-0.93088284",
        "5p:-0.29861027",
        "6s:-0.12296056"
       ]
      },
      {
       "symbol": "Nd",
       "Z": 60,
       "top3_c137": [
        "4f:-0.54541758",
        "5d:-0.35592279",
        "6p:-0.21538466"
       ],
       "top3_cinf": [
        "4f:-0.59909892",
        "5d:-0.32414306",
        "6s:-0.29469865"
       ]
      },
      {
       "symbol": "Lu",
       "Z": 71,
       "top3_c137": [
        "5d:-0.32766324",
        "6p:-0.22810148",
        "7s:-0.11012868"
       ],
       "top3_cinf": [
        "6s:-0.33305956",
        "5d:-0.31167414",
        "6p:-0.21030286"
       ]
      },
      {
       "symbol": "Hg",
       "Z": 80,
       "top3_c137": [
        "5d:-0.78203740",
        "6p:-0.28843761",
        "7s:-0.12772538"
       ],
       "top3_cinf": [
        "5d:-0.86744204",
        "6p:-0.29121508",
        "7s:-0.12031657"
       ]
      },
      {
       "symbol": "Th",
       "Z": 90,
       "top3_c137": [
        "5f:-0.40022777",
        "6d:-0.33886416",
        "7p:-0.20647270"
       ],
       "top3_cinf": [
        "5f:-0.44422213",
        "6d:-0.31025009",
        "7s:-0.27264593"
       ]
      },
      {
       "symbol": "Lr",
       "Z": 103,
       "top3_c137": [
        "5f:-0.91382663",
        "6d:-0.34427052",
        "7p:-0.22296478"
       ],
       "top3_cinf": [
        "6d:-0.32046755",
        "7s:-0.30697223",
        "7p:-0.19872732"
       ]
      },
      {
       "symbol": "Rf",
       "Z": 104,
       "top3_c137": [
        "6d:-0.34125784",
        "7p:-0.22375684",
        "8s:-0.11797506"
       ],
       "top3_cinf": [
        "6d:-0.37265496",
        "7s:-0.32647540",
        "7p:-0.20944955"
       ]
      }
     ]
    },
    "fields": {
     "lx": {
      "field": "lx",
      "field_name": "local exchange (Kohn–Sham) with Latter's tail: Hartree–Fock–Slater",
      "Z_first": 2,
      "Z_last": 120,
      "rows": 119,
      "displaced": [
       {
        "symbol": "Ba",
        "Z": 56,
        "entrant_c137": "6s",
        "entrant_cinf": "5d"
       },
       {
        "symbol": "Lu",
        "Z": 71,
        "entrant_c137": "5d",
        "entrant_cinf": "6s"
       },
       {
        "symbol": "Ra",
        "Z": 88,
        "entrant_c137": "7s",
        "entrant_cinf": "6d"
       },
       {
        "symbol": "Ac",
        "Z": 89,
        "entrant_c137": "6d",
        "entrant_cinf": "5f"
       },
       {
        "symbol": "Lr",
        "Z": 103,
        "entrant_c137": "5f",
        "entrant_cinf": "6d"
       },
       {
        "symbol": "Cn",
        "Z": 112,
        "entrant_c137": "6d",
        "entrant_cinf": "7s"
       },
       {
        "symbol": "Ubn",
        "Z": 120,
        "entrant_c137": "8s",
        "entrant_cinf": "6f"
       }
      ],
      "eleven_1706": [
       "Mn",
       "Zn",
       "Ag",
       "Cd",
       "Nd",
       "Pm",
       "Sm",
       "Lu",
       "Hg",
       "Lr",
       "Rf"
      ],
      "in_eleven": [
       "Lu",
       "Lr"
      ],
      "not_in_eleven": [
       "Ba",
       "Ra",
       "Ac",
       "Cn",
       "Ubn"
      ],
      "eleven_not_displaced": [
       "Mn",
       "Zn",
       "Ag",
       "Cd",
       "Nd",
       "Pm",
       "Sm",
       "Hg",
       "Rf"
      ],
      "thorium": {
       "entrant_c137": "5f",
       "entrant_cinf": "5f",
       "identical": true,
       "top3_c137": [
        "5f:-0.40022777",
        "6d:-0.33886416",
        "7p:-0.20647270"
       ],
       "top3_cinf": [
        "5f:-0.44422213",
        "6d:-0.31025009",
        "7s:-0.27264593"
       ]
      },
      "named_rows": [
       {
        "symbol": "Mn",
        "Z": 25,
        "top3_c137": [
         "3d:-0.74138426",
         "4p:-0.29476685",
         "5s:-0.12289774"
        ],
        "top3_cinf": [
         "3d:-0.75313672",
         "4p:-0.29529450",
         "5s:-0.12235490"
        ]
       },
       {
        "symbol": "Zn",
        "Z": 30,
        "top3_c137": [
         "3d:-0.96938076",
         "4p:-0.31994857",
         "5s:-0.13260640"
        ],
        "top3_cinf": [
         "3d:-0.98864532",
         "4p:-0.32063045",
         "5s:-0.13167224"
        ]
       },
       {
        "symbol": "Ag",
        "Z": 47,
        "top3_c137": [
         "4d:-0.83970830",
         "5p:-0.29368657",
         "6s:-0.12375895"
        ],
        "top3_cinf": [
         "4d:-0.87291006",
         "5p:-0.29470942",
         "6s:-0.12164596"
        ]
       },
       {
        "symbol": "Cd",
        "Z": 48,
        "top3_c137": [
         "4d:-0.89489438",
         "5p:-0.29744908",
         "6s:-0.12520239"
        ],
        "top3_cinf": [
         "4d:-0.93088284",
         "5p:-0.29861027",
         "6s:-0.12296056"
        ]
       },
       {
        "symbol": "Nd",
        "Z": 60,
        "top3_c137": [
         "4f:-0.54541758",
         "5d:-0.35592279",
         "6p:-0.21538466"
        ],
        "top3_cinf": [
         "4f:-0.59909892",
         "5d:-0.32414306",
         "6s:-0.29469865"
        ]
       },
       {
        "symbol": "Lu",
        "Z": 71,
        "top3_c137": [
         "5d:-0.32766324",
         "6p:-0.22810148",
         "7s:-0.11012868"
        ],
        "top3_cinf": [
         "6s:-0.33305956",
         "5d:-0.31167414",
         "6p:-0.21030286"
        ]
       },
       {
        "symbol": "Hg",
        "Z": 80,
        "top3_c137": [
         "5d:-0.78203740",
         "6p:-0.28843761",
         "7s:-0.12772538"
        ],
        "top3_cinf": [
         "5d:-0.86744204",
         "6p:-0.29121508",
         "7s:-0.12031657"
        ]
       },
       {
        "symbol": "Th",
        "Z": 90,
        "top3_c137": [
         "5f:-0.40022777",
         "6d:-0.33886416",
         "7p:-0.20647270"
        ],
        "top3_cinf": [
         "5f:-0.44422213",
         "6d:-0.31025009",
         "7s:-0.27264593"
        ]
       },
       {
        "symbol": "Lr",
        "Z": 103,
        "top3_c137": [
         "5f:-0.91382663",
         "6d:-0.34427052",
         "7p:-0.22296478"
        ],
        "top3_cinf": [
         "6d:-0.32046755",
         "7s:-0.30697223",
         "7p:-0.19872732"
        ]
       },
       {
        "symbol": "Rf",
        "Z": 104,
        "top3_c137": [
         "6d:-0.34125784",
         "7p:-0.22375684",
         "8s:-0.11797506"
        ],
        "top3_cinf": [
         "6d:-0.37265496",
         "7s:-0.32647540",
         "7p:-0.20944955"
        ]
       }
      ]
     }
    },
    "primary_field": "lx"
   },
   "entrants": [
    {
     "Z": 2,
     "symbol": "He",
     "c137": "1s",
     "cinf": "1s",
     "margin_c137": 1.13394831,
     "margin_cinf": 1.13390294,
     "displaced": false
    },
    {
     "Z": 3,
     "symbol": "Li",
     "c137": "2s",
     "cinf": "2s",
     "margin_c137": 0.07271971,
     "margin_cinf": 0.07269298,
     "displaced": false
    },
    {
     "Z": 4,
     "symbol": "Be",
     "c137": "2s",
     "cinf": "2s",
     "margin_c137": 0.13951638,
     "margin_cinf": 0.13941582,
     "displaced": false
    },
    {
     "Z": 5,
     "symbol": "B",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.32771191,
     "margin_cinf": 0.32781676,
     "displaced": false
    },
    {
     "Z": 6,
     "symbol": "C",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.45246834,
     "margin_cinf": 0.45265599,
     "displaced": false
    },
    {
     "Z": 7,
     "symbol": "N",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.57709058,
     "margin_cinf": 0.57738236,
     "displaced": false
    },
    {
     "Z": 8,
     "symbol": "O",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.70439978,
     "margin_cinf": 0.70482323,
     "displaced": false
    },
    {
     "Z": 9,
     "symbol": "F",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.83566261,
     "margin_cinf": 0.8362486,
     "displaced": false
    },
    {
     "Z": 10,
     "symbol": "Ne",
     "c137": "2p",
     "cinf": "2p",
     "margin_c137": 0.97146949,
     "margin_cinf": 0.97225154,
     "displaced": false
    },
    {
     "Z": 11,
     "symbol": "Na",
     "c137": "3s",
     "cinf": "3s",
     "margin_c137": 0.11069328,
     "margin_cinf": 0.11020783,
     "displaced": false
    },
    {
     "Z": 12,
     "symbol": "Mg",
     "c137": "3s",
     "cinf": "3s",
     "margin_c137": 0.15614253,
     "margin_cinf": 0.15532214,
     "displaced": false
    },
    {
     "Z": 13,
     "symbol": "Al",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.18699368,
     "margin_cinf": 0.18751574,
     "displaced": false
    },
    {
     "Z": 14,
     "symbol": "Si",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.26206871,
     "margin_cinf": 0.26279785,
     "displaced": false
    },
    {
     "Z": 15,
     "symbol": "P",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.34186874,
     "margin_cinf": 0.34275944,
     "displaced": false
    },
    {
     "Z": 16,
     "symbol": "S",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.42476429,
     "margin_cinf": 0.4258143,
     "displaced": false
    },
    {
     "Z": 17,
     "symbol": "Cl",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.51084732,
     "margin_cinf": 0.51206181,
     "displaced": false
    },
    {
     "Z": 18,
     "symbol": "Ar",
     "c137": "3p",
     "cinf": "3p",
     "margin_c137": 0.60030039,
     "margin_cinf": 0.60168329,
     "displaced": false
    },
    {
     "Z": 19,
     "symbol": "K",
     "c137": "4s",
     "cinf": "4s",
     "margin_c137": 0.08501865,
     "margin_cinf": 0.08214046,
     "displaced": false
    },
    {
     "Z": 20,
     "symbol": "Ca",
     "c137": "4s",
     "cinf": "4s",
     "margin_c137": 0.02722139,
     "margin_cinf": 0.02157626,
     "displaced": false
    },
    {
     "Z": 21,
     "symbol": "Sc",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.25256387,
     "margin_cinf": 0.25986696,
     "displaced": false
    },
    {
     "Z": 22,
     "symbol": "Ti",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.30643274,
     "margin_cinf": 0.31448372,
     "displaced": false
    },
    {
     "Z": 23,
     "symbol": "V",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.35576853,
     "margin_cinf": 0.36475614,
     "displaced": false
    },
    {
     "Z": 24,
     "symbol": "Cr",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.40222727,
     "margin_cinf": 0.41227912,
     "displaced": false
    },
    {
     "Z": 25,
     "symbol": "Mn",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.4466174,
     "margin_cinf": 0.45784223,
     "displaced": false
    },
    {
     "Z": 26,
     "symbol": "Fe",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.48940838,
     "margin_cinf": 0.50190759,
     "displaced": false
    },
    {
     "Z": 27,
     "symbol": "Co",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.53090397,
     "margin_cinf": 0.54477539,
     "displaced": false
    },
    {
     "Z": 28,
     "symbol": "Ni",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.57131188,
     "margin_cinf": 0.58665368,
     "displaced": false
    },
    {
     "Z": 29,
     "symbol": "Cu",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.61078286,
     "margin_cinf": 0.62769586,
     "displaced": false
    },
    {
     "Z": 30,
     "symbol": "Zn",
     "c137": "3d",
     "cinf": "3d",
     "margin_c137": 0.64943218,
     "margin_cinf": 0.66801488,
     "displaced": false
    },
    {
     "Z": 31,
     "symbol": "Ga",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.18923114,
     "margin_cinf": 0.19099953,
     "displaced": false
    },
    {
     "Z": 32,
     "symbol": "Ge",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.24699881,
     "margin_cinf": 0.24963301,
     "displaced": false
    },
    {
     "Z": 33,
     "symbol": "As",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.31006958,
     "margin_cinf": 0.31308032,
     "displaced": false
    },
    {
     "Z": 34,
     "symbol": "Se",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.374441,
     "margin_cinf": 0.37774556,
     "displaced": false
    },
    {
     "Z": 35,
     "symbol": "Br",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.44008207,
     "margin_cinf": 0.44365688,
     "displaced": false
    },
    {
     "Z": 36,
     "symbol": "Kr",
     "c137": "4p",
     "cinf": "4p",
     "margin_c137": 0.50725359,
     "margin_cinf": 0.5110798,
     "displaced": false
    },
    {
     "Z": 37,
     "symbol": "Rb",
     "c137": "5s",
     "cinf": "5s",
     "margin_c137": 0.08574849,
     "margin_cinf": 0.07690085,
     "displaced": false
    },
    {
     "Z": 38,
     "symbol": "Sr",
     "c137": "5s",
     "cinf": "5s",
     "margin_c137": 0.06223826,
     "margin_cinf": 0.04775689,
     "displaced": false
    },
    {
     "Z": 39,
     "symbol": "Y",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.13406907,
     "margin_cinf": 0.14948669,
     "displaced": false
    },
    {
     "Z": 40,
     "symbol": "Zr",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.18864697,
     "margin_cinf": 0.20555757,
     "displaced": false
    },
    {
     "Z": 41,
     "symbol": "Nb",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.24063408,
     "margin_cinf": 0.25934186,
     "displaced": false
    },
    {
     "Z": 42,
     "symbol": "Mo",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.29169653,
     "margin_cinf": 0.31235959,
     "displaced": false
    },
    {
     "Z": 43,
     "symbol": "Tc",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.34243385,
     "margin_cinf": 0.36517488,
     "displaced": false
    },
    {
     "Z": 44,
     "symbol": "Ru",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.39311948,
     "margin_cinf": 0.41805136,
     "displaced": false
    },
    {
     "Z": 45,
     "symbol": "Rh",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.44389768,
     "margin_cinf": 0.47113178,
     "displaced": false
    },
    {
     "Z": 46,
     "symbol": "Pd",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.49484864,
     "margin_cinf": 0.52449725,
     "displaced": false
    },
    {
     "Z": 47,
     "symbol": "Ag",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.54602173,
     "margin_cinf": 0.57820065,
     "displaced": false
    },
    {
     "Z": 48,
     "symbol": "Cd",
     "c137": "4d",
     "cinf": "4d",
     "margin_c137": 0.5974453,
     "margin_cinf": 0.63227257,
     "displaced": false
    },
    {
     "Z": 49,
     "symbol": "In",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.17422662,
     "margin_cinf": 0.17792747,
     "displaced": false
    },
    {
     "Z": 50,
     "symbol": "Sn",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.2202816,
     "margin_cinf": 0.22565264,
     "displaced": false
    },
    {
     "Z": 51,
     "symbol": "Sb",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.27053465,
     "margin_cinf": 0.27654622,
     "displaced": false
    },
    {
     "Z": 52,
     "symbol": "Te",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.32132842,
     "margin_cinf": 0.32780917,
     "displaced": false
    },
    {
     "Z": 53,
     "symbol": "I",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.37258928,
     "margin_cinf": 0.37949654,
     "displaced": false
    },
    {
     "Z": 54,
     "symbol": "Xe",
     "c137": "5p",
     "cinf": "5p",
     "margin_c137": 0.42455445,
     "margin_cinf": 0.4318585,
     "displaced": false
    },
    {
     "Z": 55,
     "symbol": "Cs",
     "c137": "6s",
     "cinf": "6s",
     "margin_c137": 0.0487688,
     "margin_cinf": 0.02908518,
     "displaced": false
    },
    {
     "Z": 56,
     "symbol": "Ba",
     "c137": "6s",
     "cinf": "5d",
     "margin_c137": 0.0248226,
     "margin_cinf": 0.00366088,
     "displaced": true
    },
    {
     "Z": 57,
     "symbol": "La",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.08977633,
     "margin_cinf": 0.1663153,
     "displaced": false
    },
    {
     "Z": 58,
     "symbol": "Ce",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.1285128,
     "margin_cinf": 0.20729222,
     "displaced": false
    },
    {
     "Z": 59,
     "symbol": "Pr",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.16125681,
     "margin_cinf": 0.24311218,
     "displaced": false
    },
    {
     "Z": 60,
     "symbol": "Nd",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.18949479,
     "margin_cinf": 0.27495586,
     "displaced": false
    },
    {
     "Z": 61,
     "symbol": "Pm",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.21410963,
     "margin_cinf": 0.30356865,
     "displaced": false
    },
    {
     "Z": 62,
     "symbol": "Sm",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.23568564,
     "margin_cinf": 0.32945591,
     "displaced": false
    },
    {
     "Z": 63,
     "symbol": "Eu",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.25463588,
     "margin_cinf": 0.3529869,
     "displaced": false
    },
    {
     "Z": 64,
     "symbol": "Gd",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.27126881,
     "margin_cinf": 0.37444073,
     "displaced": false
    },
    {
     "Z": 65,
     "symbol": "Tb",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.2858233,
     "margin_cinf": 0.39403677,
     "displaced": false
    },
    {
     "Z": 66,
     "symbol": "Dy",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.29848938,
     "margin_cinf": 0.4119511,
     "displaced": false
    },
    {
     "Z": 67,
     "symbol": "Ho",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.30942215,
     "margin_cinf": 0.42786616,
     "displaced": false
    },
    {
     "Z": 68,
     "symbol": "Er",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.3187521,
     "margin_cinf": 0.43777555,
     "displaced": false
    },
    {
     "Z": 69,
     "symbol": "Tm",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.32658821,
     "margin_cinf": 0.44624273,
     "displaced": false
    },
    {
     "Z": 70,
     "symbol": "Yb",
     "c137": "4f",
     "cinf": "4f",
     "margin_c137": 0.33302558,
     "margin_cinf": 0.45337041,
     "displaced": false
    },
    {
     "Z": 71,
     "symbol": "Lu",
     "c137": "5d",
     "cinf": "6s",
     "margin_c137": 0.09956176,
     "margin_cinf": 0.02138542,
     "displaced": true
    },
    {
     "Z": 72,
     "symbol": "Hf",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.14508006,
     "margin_cinf": 0.19107801,
     "displaced": false
    },
    {
     "Z": 73,
     "symbol": "Ta",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.18873486,
     "margin_cinf": 0.23904386,
     "displaced": false
    },
    {
     "Z": 74,
     "symbol": "W",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.23184969,
     "margin_cinf": 0.28653696,
     "displaced": false
    },
    {
     "Z": 75,
     "symbol": "Re",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.27489827,
     "margin_cinf": 0.33402148,
     "displaced": false
    },
    {
     "Z": 76,
     "symbol": "Os",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.31808181,
     "margin_cinf": 0.38171096,
     "displaced": false
    },
    {
     "Z": 77,
     "symbol": "Ir",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.36150033,
     "margin_cinf": 0.42971975,
     "displaced": false
    },
    {
     "Z": 78,
     "symbol": "Pt",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.40520783,
     "margin_cinf": 0.47811573,
     "displaced": false
    },
    {
     "Z": 79,
     "symbol": "Au",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.44923505,
     "margin_cinf": 0.5269423,
     "displaced": false
    },
    {
     "Z": 80,
     "symbol": "Hg",
     "c137": "5d",
     "cinf": "5d",
     "margin_c137": 0.4935998,
     "margin_cinf": 0.57622696,
     "displaced": false
    },
    {
     "Z": 81,
     "symbol": "Tl",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.16213529,
     "margin_cinf": 0.17307262,
     "displaced": false
    },
    {
     "Z": 82,
     "symbol": "Pb",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.19975613,
     "margin_cinf": 0.21558549,
     "displaced": false
    },
    {
     "Z": 83,
     "symbol": "Bi",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.24329494,
     "margin_cinf": 0.26090524,
     "displaced": false
    },
    {
     "Z": 84,
     "symbol": "Po",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.28725644,
     "margin_cinf": 0.30618315,
     "displaced": false
    },
    {
     "Z": 85,
     "symbol": "At",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.33126482,
     "margin_cinf": 0.35142201,
     "displaced": false
    },
    {
     "Z": 86,
     "symbol": "Rn",
     "c137": "6p",
     "cinf": "6p",
     "margin_c137": 0.37550568,
     "margin_cinf": 0.39685416,
     "displaced": false
    },
    {
     "Z": 87,
     "symbol": "Fr",
     "c137": "7s",
     "cinf": "7s",
     "margin_c137": 0.07128084,
     "margin_cinf": 0.0210456,
     "displaced": false
    },
    {
     "Z": 88,
     "symbol": "Ra",
     "c137": "7s",
     "cinf": "6d",
     "margin_c137": 0.06211879,
     "margin_cinf": 0.00668457,
     "displaced": true
    },
    {
     "Z": 89,
     "symbol": "Ac",
     "c137": "6d",
     "cinf": "5f",
     "margin_c137": 0.05553556,
     "margin_cinf": 0.08089383,
     "displaced": true
    },
    {
     "Z": 90,
     "symbol": "Th",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.0613636,
     "margin_cinf": 0.13397204,
     "displaced": false
    },
    {
     "Z": 91,
     "symbol": "Pa",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.10903334,
     "margin_cinf": 0.18464212,
     "displaced": false
    },
    {
     "Z": 92,
     "symbol": "U",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.15423692,
     "margin_cinf": 0.23367542,
     "displaced": false
    },
    {
     "Z": 93,
     "symbol": "Np",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.19761097,
     "margin_cinf": 0.28147777,
     "displaced": false
    },
    {
     "Z": 94,
     "symbol": "Pu",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.23950085,
     "margin_cinf": 0.32829416,
     "displaced": false
    },
    {
     "Z": 95,
     "symbol": "Am",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.28011752,
     "margin_cinf": 0.37428504,
     "displaced": false
    },
    {
     "Z": 96,
     "symbol": "Cm",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.31959833,
     "margin_cinf": 0.41956192,
     "displaced": false
    },
    {
     "Z": 97,
     "symbol": "Bk",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.35803847,
     "margin_cinf": 0.46420754,
     "displaced": false
    },
    {
     "Z": 98,
     "symbol": "Cf",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.39550524,
     "margin_cinf": 0.50828154,
     "displaced": false
    },
    {
     "Z": 99,
     "symbol": "Es",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.43204756,
     "margin_cinf": 0.55183139,
     "displaced": false
    },
    {
     "Z": 100,
     "symbol": "Fm",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.46770051,
     "margin_cinf": 0.59489413,
     "displaced": false
    },
    {
     "Z": 101,
     "symbol": "Md",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.50249176,
     "margin_cinf": 0.63749947,
     "displaced": false
    },
    {
     "Z": 102,
     "symbol": "No",
     "c137": "5f",
     "cinf": "5f",
     "margin_c137": 0.5364391,
     "margin_cinf": 0.67967147,
     "displaced": false
    },
    {
     "Z": 103,
     "symbol": "Lr",
     "c137": "5f",
     "cinf": "6d",
     "margin_c137": 0.56955611,
     "margin_cinf": 0.01349532,
     "displaced": true
    },
    {
     "Z": 104,
     "symbol": "Rf",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.117501,
     "margin_cinf": 0.04617956,
     "displaced": false
    },
    {
     "Z": 105,
     "symbol": "Db",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.15430371,
     "margin_cinf": 0.07846424,
     "displaced": false
    },
    {
     "Z": 106,
     "symbol": "Sg",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.19018129,
     "margin_cinf": 0.11091521,
     "displaced": false
    },
    {
     "Z": 107,
     "symbol": "Bh",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.22570242,
     "margin_cinf": 0.14374659,
     "displaced": false
    },
    {
     "Z": 108,
     "symbol": "Hs",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.26111736,
     "margin_cinf": 0.17704325,
     "displaced": false
    },
    {
     "Z": 109,
     "symbol": "Mt",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.2965495,
     "margin_cinf": 0.21083927,
     "displaced": false
    },
    {
     "Z": 110,
     "symbol": "Ds",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.33206276,
     "margin_cinf": 0.24514611,
     "displaced": false
    },
    {
     "Z": 111,
     "symbol": "Rg",
     "c137": "6d",
     "cinf": "6d",
     "margin_c137": 0.36769017,
     "margin_cinf": 0.27996639,
     "displaced": false
    },
    {
     "Z": 112,
     "symbol": "Cn",
     "c137": "6d",
     "cinf": "7s",
     "margin_c137": 0.40344841,
     "margin_cinf": 0.15991313,
     "displaced": true
    },
    {
     "Z": 113,
     "symbol": "Nh",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.13272835,
     "margin_cinf": 0.16384594,
     "displaced": false
    },
    {
     "Z": 114,
     "symbol": "Fl",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.15895619,
     "margin_cinf": 0.20182501,
     "displaced": false
    },
    {
     "Z": 115,
     "symbol": "Mc",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.19339546,
     "margin_cinf": 0.2418,
     "displaced": false
    },
    {
     "Z": 116,
     "symbol": "Lv",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.22817626,
     "margin_cinf": 0.28145921,
     "displaced": false
    },
    {
     "Z": 117,
     "symbol": "Ts",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.26259136,
     "margin_cinf": 0.32083452,
     "displaced": false
    },
    {
     "Z": 118,
     "symbol": "Og",
     "c137": "7p",
     "cinf": "7p",
     "margin_c137": 0.29674094,
     "margin_cinf": 0.36014508,
     "displaced": false
    },
    {
     "Z": 119,
     "symbol": "Uue",
     "c137": "8s",
     "cinf": "8s",
     "margin_c137": 0.11497651,
     "margin_cinf": 3.532e-05,
     "displaced": false
    },
    {
     "Z": 120,
     "symbol": "Ubn",
     "c137": "8s",
     "cinf": "6f",
     "margin_c137": 0.12307422,
     "margin_cinf": 0.09095094,
     "displaced": true
    }
   ]
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
   "id": "walk-reconstructed",
   "text": "The walk shown beside the record is a RECONSTRUCTION (tools/lowdin_walk.py over LOWDIN-WALK.tsv): the record's construction rebuilt from its statement and run in two fields, a local-exchange one and the record's own average-of-configuration Hartree–Fock with non-local exchange, neither of them the record's code, which never arrived. Where it agrees with the record that is a measurement; where it disagrees that is a measurement too. It is never the record's number, and the record's Λ_chain and Λ_cinf stay unheld."
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": false,
   "walk_lx_displaced": false,
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
   "walk_displaced": true,
   "walk_lx_displaced": true,
   "limits": {
    "nuclear": 1760
   }
  }
 ],
 "manifest": [
  {
   "Z": 1,
   "file": "elements/1.js",
   "bytes": 3912,
   "md5": "3cb6a36cd2e84c84a45ef5d1c68a4f31",
   "payload_bytes": 3832,
   "payload_md5": "bca5cba3621e034e2007adb8863b3474"
  },
  {
   "Z": 2,
   "file": "elements/2.js",
   "bytes": 12171,
   "md5": "4b39ca2e0f20b193649adbb0ccb6a022",
   "payload_bytes": 12091,
   "payload_md5": "8956036e0a8286dd36c5ebfe0db68055"
  },
  {
   "Z": 3,
   "file": "elements/3.js",
   "bytes": 15625,
   "md5": "fffdd96361dd744787b17f5547e6f51e",
   "payload_bytes": 15545,
   "payload_md5": "3f356c6de692f8582cc26fbac5cb17d3"
  },
  {
   "Z": 4,
   "file": "elements/4.js",
   "bytes": 21405,
   "md5": "098df9e24dadba72175be1b0aba365cb",
   "payload_bytes": 21325,
   "payload_md5": "b6da033528ce96fe3eb84d1eb3cbe7f1"
  },
  {
   "Z": 5,
   "file": "elements/5.js",
   "bytes": 25545,
   "md5": "6f04a11c1d5dac3e7854e3c0d7ab3590",
   "payload_bytes": 25465,
   "payload_md5": "1b020bc4082e641a4da191d573dd1d55"
  },
  {
   "Z": 6,
   "file": "elements/6.js",
   "bytes": 31359,
   "md5": "e8436749ff35edd0fe31d58e09faf8d9",
   "payload_bytes": 31279,
   "payload_md5": "70c5351e193d12ce3f2d487784158c67"
  },
  {
   "Z": 7,
   "file": "elements/7.js",
   "bytes": 38162,
   "md5": "a4e4e02424b1877ac2f13e7eebc80da4",
   "payload_bytes": 38082,
   "payload_md5": "7abff1f936a3dfd010eefb15561ffc29"
  },
  {
   "Z": 8,
   "file": "elements/8.js",
   "bytes": 44224,
   "md5": "6dabffcfe951e8df6a26c9e62f480924",
   "payload_bytes": 44144,
   "payload_md5": "6211315fdd1902b8181d07f13db47d61"
  },
  {
   "Z": 9,
   "file": "elements/9.js",
   "bytes": 50507,
   "md5": "c0ffede48d9b3f60d26ccf5d0dc45884",
   "payload_bytes": 50427,
   "payload_md5": "5a2579d05275d7f955b9517ca41df9cb"
  },
  {
   "Z": 10,
   "file": "elements/10.js",
   "bytes": 56592,
   "md5": "545442359007da7b34f9bf5c6f121359",
   "payload_bytes": 56511,
   "payload_md5": "7d45a861440c1c197de94a0f892cd8df"
  },
  {
   "Z": 11,
   "file": "elements/11.js",
   "bytes": 61371,
   "md5": "afbff6a5b23a3a565569330e1689b100",
   "payload_bytes": 61290,
   "payload_md5": "1be015ecb8e3baa9070a9db358e03021"
  },
  {
   "Z": 12,
   "file": "elements/12.js",
   "bytes": 66366,
   "md5": "419f1ed30c6f653e41219cd4e4e40381",
   "payload_bytes": 66285,
   "payload_md5": "4d15d58e11b5831058adb483c63bbb82"
  },
  {
   "Z": 13,
   "file": "elements/13.js",
   "bytes": 70616,
   "md5": "e87051d7ac78ca8df12ffe8b0a501617",
   "payload_bytes": 70535,
   "payload_md5": "14165162d659731e765a86fa72aced98"
  },
  {
   "Z": 14,
   "file": "elements/14.js",
   "bytes": 76221,
   "md5": "e060c417e5653b9c5f00dbc1b44dc041",
   "payload_bytes": 76140,
   "payload_md5": "0f74121a4f96b5da1c4a0f1abc2efa34"
  },
  {
   "Z": 15,
   "file": "elements/15.js",
   "bytes": 82626,
   "md5": "b46de12050f276c0a83ee62d88d651e7",
   "payload_bytes": 82545,
   "payload_md5": "3bcdfd4264ce5677f52634c7d94c350c"
  },
  {
   "Z": 16,
   "file": "elements/16.js",
   "bytes": 88298,
   "md5": "60e13944213aa5c56c63a5da2e94bf8a",
   "payload_bytes": 88217,
   "payload_md5": "23af53a3837cc0487806067ea90ccb7c"
  },
  {
   "Z": 17,
   "file": "elements/17.js",
   "bytes": 95211,
   "md5": "9f6ec98e386ecd487a9bb87e91d5ae3e",
   "payload_bytes": 95130,
   "payload_md5": "c5216d702d663d01ed204dd2d8830364"
  },
  {
   "Z": 18,
   "file": "elements/18.js",
   "bytes": 102323,
   "md5": "27de7c2284c380bb1ca600684b9fd466",
   "payload_bytes": 102242,
   "payload_md5": "16d88b2333002207b29c08f5a6b0b449"
  },
  {
   "Z": 19,
   "file": "elements/19.js",
   "bytes": 106185,
   "md5": "8971097216a71324f3f1fcb646f57614",
   "payload_bytes": 106104,
   "payload_md5": "db60262794ec02043ebfb18110026bbd"
  },
  {
   "Z": 20,
   "file": "elements/20.js",
   "bytes": 111584,
   "md5": "f3d08152f9a4aebbffd7d0d1182ede38",
   "payload_bytes": 111503,
   "payload_md5": "b1a94e8bfc3fc47d1b24394d439c6074"
  },
  {
   "Z": 21,
   "file": "elements/21.js",
   "bytes": 116633,
   "md5": "a32b77082f0564a952c3393a09a4efb6",
   "payload_bytes": 116552,
   "payload_md5": "c82fc260fb8a87de86285217f92f8ba1"
  },
  {
   "Z": 22,
   "file": "elements/22.js",
   "bytes": 122383,
   "md5": "48f5ca33d75f1fac29bca33aa6aa5d34",
   "payload_bytes": 122302,
   "payload_md5": "5ea738ab656359d66c25d9fff88d77a8"
  },
  {
   "Z": 23,
   "file": "elements/23.js",
   "bytes": 129262,
   "md5": "92d9f133bfbc853ce1f983184dfb1d15",
   "payload_bytes": 129181,
   "payload_md5": "c801c19f65eb829faa75b6d63f747605"
  },
  {
   "Z": 24,
   "file": "elements/24.js",
   "bytes": 135265,
   "md5": "39acaa9dafabdfad75464123273c8597",
   "payload_bytes": 135184,
   "payload_md5": "ea051d8b6669d7cb532e228219de50d7"
  },
  {
   "Z": 25,
   "file": "elements/25.js",
   "bytes": 141145,
   "md5": "36a2d0f66ef6fe4f23d34c4290da575a",
   "payload_bytes": 141064,
   "payload_md5": "309fd58327d3c83ccd337c977d03083a"
  },
  {
   "Z": 26,
   "file": "elements/26.js",
   "bytes": 146588,
   "md5": "fb135645e36a1e278a468ea27263d504",
   "payload_bytes": 146507,
   "payload_md5": "eee2f94aac45490cb067fc1f1a61d914"
  },
  {
   "Z": 27,
   "file": "elements/27.js",
   "bytes": 153107,
   "md5": "5189f3cf326a2ed93eb4c1c4c9fb8751",
   "payload_bytes": 153026,
   "payload_md5": "8b7b230ee398144ff92bbfbca0335c81"
  },
  {
   "Z": 28,
   "file": "elements/28.js",
   "bytes": 159053,
   "md5": "f94a63125e21f2bffac06cf724a672cd",
   "payload_bytes": 158972,
   "payload_md5": "8a84d367cd502dafef2954aad797ad5e"
  },
  {
   "Z": 29,
   "file": "elements/29.js",
   "bytes": 165082,
   "md5": "66a148253f44bffbb607aed4c26f4e4a",
   "payload_bytes": 165001,
   "payload_md5": "195bff560c33498144d365e4d21ce210"
  },
  {
   "Z": 30,
   "file": "elements/30.js",
   "bytes": 170935,
   "md5": "f3cb77252f9f426d27d9e174f64aa885",
   "payload_bytes": 170854,
   "payload_md5": "8e0d8ab03e3b8b8af1114cc47aa75254"
  },
  {
   "Z": 31,
   "file": "elements/31.js",
   "bytes": 175053,
   "md5": "3a2f8ac3a87ffce77672bfefd3a4f648",
   "payload_bytes": 174972,
   "payload_md5": "e096ddccb92f34280617d66a12a3435e"
  },
  {
   "Z": 32,
   "file": "elements/32.js",
   "bytes": 181438,
   "md5": "5c9add8790c115dd9f666471e536a198",
   "payload_bytes": 181357,
   "payload_md5": "0f38b27b665fb363750f4a7816996900"
  },
  {
   "Z": 33,
   "file": "elements/33.js",
   "bytes": 187710,
   "md5": "e89968cbbc209c3d43fab2e0c3171580",
   "payload_bytes": 187629,
   "payload_md5": "e87d70c3013d5e57552bb0c271f0a54d"
  },
  {
   "Z": 34,
   "file": "elements/34.js",
   "bytes": 193666,
   "md5": "36d1ff1930bbd12eaf23a881e542e76e",
   "payload_bytes": 193585,
   "payload_md5": "7c9394707833fa0437193e3ef28ac2e5"
  },
  {
   "Z": 35,
   "file": "elements/35.js",
   "bytes": 199622,
   "md5": "efb555bb1f1895f9ab14a40a8892fac3",
   "payload_bytes": 199541,
   "payload_md5": "83b84de8d4d0908aa6fb2bc4d0ffa978"
  },
  {
   "Z": 36,
   "file": "elements/36.js",
   "bytes": 205880,
   "md5": "99cbb15f8ae2be540122375ad58a417e",
   "payload_bytes": 205799,
   "payload_md5": "0f7cbaff380ebfef1071597eb6a948d8"
  },
  {
   "Z": 37,
   "file": "elements/37.js",
   "bytes": 209987,
   "md5": "6cccdcba8f1230d6d8d41d6781fb91b4",
   "payload_bytes": 209906,
   "payload_md5": "0e173f1624bddd0063645860910757e5"
  },
  {
   "Z": 38,
   "file": "elements/38.js",
   "bytes": 216015,
   "md5": "4dd162650701f1e77f6d97eed7315496",
   "payload_bytes": 215934,
   "payload_md5": "91cbd488cdb74a2318b1a1ae81182a3d"
  },
  {
   "Z": 39,
   "file": "elements/39.js",
   "bytes": 220478,
   "md5": "3d32d6df85e83f1848e9c47c684630da",
   "payload_bytes": 220397,
   "payload_md5": "7fbc55e8054a7542596f0188a269e540"
  },
  {
   "Z": 40,
   "file": "elements/40.js",
   "bytes": 226738,
   "md5": "f79fbb20f80a7ea5be85ba5a845c5383",
   "payload_bytes": 226657,
   "payload_md5": "e176f11249e6de1611863ea18647f21a"
  },
  {
   "Z": 41,
   "file": "elements/41.js",
   "bytes": 232740,
   "md5": "f5d398431f407a95510bc80b71cbca24",
   "payload_bytes": 232659,
   "payload_md5": "e184c516d7a699cf6279c6ec1ceb5ea8"
  },
  {
   "Z": 42,
   "file": "elements/42.js",
   "bytes": 238734,
   "md5": "c52fb028f07276ca99258d3cbb0ba98b",
   "payload_bytes": 238653,
   "payload_md5": "e9f6ddd7dd6ce31fd5d6fdd260969121"
  },
  {
   "Z": 43,
   "file": "elements/43.js",
   "bytes": 244580,
   "md5": "f1e80ff0c78f9df45d329774097175e9",
   "payload_bytes": 244499,
   "payload_md5": "6b8f9d5f541d344b59842226b01dd960"
  },
  {
   "Z": 44,
   "file": "elements/44.js",
   "bytes": 250685,
   "md5": "0f6ccc1fbe833f78dbe1c9d000265493",
   "payload_bytes": 250604,
   "payload_md5": "82d0def4aca46058bf642402e7c1ae33"
  },
  {
   "Z": 45,
   "file": "elements/45.js",
   "bytes": 256636,
   "md5": "cf9035f0e7e498515d82e4e236c560d8",
   "payload_bytes": 256555,
   "payload_md5": "4e2956714076821f84d7a60e7e836a18"
  },
  {
   "Z": 46,
   "file": "elements/46.js",
   "bytes": 262514,
   "md5": "3344f19fea7e9c416b9d575c2cae5030",
   "payload_bytes": 262433,
   "payload_md5": "54813e7aafbd6022e326871f844a2f94"
  },
  {
   "Z": 47,
   "file": "elements/47.js",
   "bytes": 268533,
   "md5": "85e4acd39a0f896984a1eaf710a2aefd",
   "payload_bytes": 268452,
   "payload_md5": "4f7fbcd4bf737dcd96540bd4c727a04b"
  },
  {
   "Z": 48,
   "file": "elements/48.js",
   "bytes": 274221,
   "md5": "c035d0c3b257a82987a8ea5baddd1a30",
   "payload_bytes": 274140,
   "payload_md5": "5e9ce014b2571cdedd604d6c701ee8c6"
  },
  {
   "Z": 49,
   "file": "elements/49.js",
   "bytes": 279061,
   "md5": "8d5dc4314b9710a588c2976e3e6aee20",
   "payload_bytes": 278980,
   "payload_md5": "8b69c4d9b1467b7ad02abc0546f2da4e"
  },
  {
   "Z": 50,
   "file": "elements/50.js",
   "bytes": 285308,
   "md5": "b51434edb7d14ce435420ec16da40043",
   "payload_bytes": 285227,
   "payload_md5": "909c9ac04bdff95c4a1608ac34204e15"
  },
  {
   "Z": 51,
   "file": "elements/51.js",
   "bytes": 291239,
   "md5": "d1ae1b9af5e9a870e1050f87be21359c",
   "payload_bytes": 291158,
   "payload_md5": "4d2ed7ccfd808d7966364c15821594d4"
  },
  {
   "Z": 52,
   "file": "elements/52.js",
   "bytes": 297207,
   "md5": "d99f68ea46128f5b94c4e1f6e77e84d8",
   "payload_bytes": 297126,
   "payload_md5": "acc02a2126c30890b7577f68ecd10a2d"
  },
  {
   "Z": 53,
   "file": "elements/53.js",
   "bytes": 303146,
   "md5": "e043d674ff3b8586baf228b20875cbdd",
   "payload_bytes": 303065,
   "payload_md5": "dd97705b422cea13709e1b32353260d6"
  },
  {
   "Z": 54,
   "file": "elements/54.js",
   "bytes": 312564,
   "md5": "934eac560805c4a006b71134a88cc8b9",
   "payload_bytes": 312483,
   "payload_md5": "67e728668534698de169b4ec91467751"
  },
  {
   "Z": 55,
   "file": "elements/55.js",
   "bytes": 317053,
   "md5": "54afbb14510978fb56f2ac814f137920",
   "payload_bytes": 316972,
   "payload_md5": "34951d80a82b5e5ceda1afce62691fdd"
  },
  {
   "Z": 56,
   "file": "elements/56.js",
   "bytes": 322790,
   "md5": "2465d21842f77c0f14b6243f11178ab5",
   "payload_bytes": 322709,
   "payload_md5": "e81f952791cc2e5436bce3fadc1c63c0"
  },
  {
   "Z": 57,
   "file": "elements/57.js",
   "bytes": 327194,
   "md5": "b41acd68eab5cb376eefb6b3f029281f",
   "payload_bytes": 327113,
   "payload_md5": "45568c92360e4b6e849736ac9683395a"
  },
  {
   "Z": 58,
   "file": "elements/58.js",
   "bytes": 333777,
   "md5": "1167d8cedd14783c1cd56b64502879bc",
   "payload_bytes": 333696,
   "payload_md5": "a0c8a7b1478ae69693200086a51ff213"
  },
  {
   "Z": 59,
   "file": "elements/59.js",
   "bytes": 339681,
   "md5": "d2c221a070b35ab7d5e17d72fe4e846c",
   "payload_bytes": 339600,
   "payload_md5": "5aa165514386c543bf59afeb223950fc"
  },
  {
   "Z": 60,
   "file": "elements/60.js",
   "bytes": 345792,
   "md5": "fae73d2b77fe0538242df1512e325076",
   "payload_bytes": 345711,
   "payload_md5": "ec50b1e86361b1727a0c63e458d67da5"
  },
  {
   "Z": 61,
   "file": "elements/61.js",
   "bytes": 351649,
   "md5": "a913fc65892770a1231285d13c1482c3",
   "payload_bytes": 351568,
   "payload_md5": "0fdd497adafeedc061009dcd381eeab6"
  },
  {
   "Z": 62,
   "file": "elements/62.js",
   "bytes": 357698,
   "md5": "39d597fd01f415be2128b427271d32bf",
   "payload_bytes": 357617,
   "payload_md5": "87e0104bb42701649b660be0725d325a"
  },
  {
   "Z": 63,
   "file": "elements/63.js",
   "bytes": 363695,
   "md5": "07ea52985e8264069e07c7eb0d54aa0e",
   "payload_bytes": 363614,
   "payload_md5": "3533157ed6285e682d67edaf9d847030"
  },
  {
   "Z": 64,
   "file": "elements/64.js",
   "bytes": 369891,
   "md5": "88539b88a9a5b578ee4c79286d7f237e",
   "payload_bytes": 369810,
   "payload_md5": "71b60c2e6b99c115ba8933f62fe2de1e"
  },
  {
   "Z": 65,
   "file": "elements/65.js",
   "bytes": 375837,
   "md5": "b7099a9a88140550ced59c44c41ad8b6",
   "payload_bytes": 375756,
   "payload_md5": "5ce9b1b31dee5cb64a8dab1512ae651c"
  },
  {
   "Z": 66,
   "file": "elements/66.js",
   "bytes": 381903,
   "md5": "55843331df0b431d38781aee01e11753",
   "payload_bytes": 381822,
   "payload_md5": "68eab734278ab44bdc9e058b291ef002"
  },
  {
   "Z": 67,
   "file": "elements/67.js",
   "bytes": 387895,
   "md5": "23be020ed1f22a131f55d3f95e923dee",
   "payload_bytes": 387814,
   "payload_md5": "c895eb6ee464697c661c45d98f7078e3"
  },
  {
   "Z": 68,
   "file": "elements/68.js",
   "bytes": 393896,
   "md5": "f9e94be435aeb57d0c7c564d3cb57733",
   "payload_bytes": 393815,
   "payload_md5": "bc136f5cb5766728f440418bdc4ad1a1"
  },
  {
   "Z": 69,
   "file": "elements/69.js",
   "bytes": 399978,
   "md5": "e9711e19be8817ed93fccef1fd53c90d",
   "payload_bytes": 399897,
   "payload_md5": "4dbaf9f553be270f9d1b7b3d9681098f"
  },
  {
   "Z": 70,
   "file": "elements/70.js",
   "bytes": 406306,
   "md5": "b8a7d4dec1f39d6424276659fd0fb7f1",
   "payload_bytes": 406225,
   "payload_md5": "e25d6604611cefb50c900dff525be486"
  },
  {
   "Z": 71,
   "file": "elements/71.js",
   "bytes": 410534,
   "md5": "337df05b3de1d181f6d6f87cce96af78",
   "payload_bytes": 410453,
   "payload_md5": "37d6d3b20cd375f7aedfa1466fac0582"
  },
  {
   "Z": 72,
   "file": "elements/72.js",
   "bytes": 416856,
   "md5": "2a957f4d72184b0d53b97bef2eb2d1c7",
   "payload_bytes": 416775,
   "payload_md5": "ca8094d770ec8e677787ed0fbf784852"
  },
  {
   "Z": 73,
   "file": "elements/73.js",
   "bytes": 422845,
   "md5": "24b30e8bac8209fe11418a0f668529e6",
   "payload_bytes": 422764,
   "payload_md5": "b54dfe7f96e0b9f04aff07a6e1c9c887"
  },
  {
   "Z": 74,
   "file": "elements/74.js",
   "bytes": 428840,
   "md5": "a6ecc9ceea1effc17ce4de22fd554b72",
   "payload_bytes": 428759,
   "payload_md5": "f767028772b81c3825e82b28c8b98308"
  },
  {
   "Z": 75,
   "file": "elements/75.js",
   "bytes": 434853,
   "md5": "2e3db0e1ef4a1e86a193d6910a9c7678",
   "payload_bytes": 434772,
   "payload_md5": "157088e9ee73eddb05abf2805acbd8ef"
  },
  {
   "Z": 76,
   "file": "elements/76.js",
   "bytes": 440882,
   "md5": "11fb1409798af5555e04462e7b235705",
   "payload_bytes": 440801,
   "payload_md5": "19ddbcf0e39c8a177ced7852958c70a0"
  },
  {
   "Z": 77,
   "file": "elements/77.js",
   "bytes": 446911,
   "md5": "a50ac444b2370573edc2416dc84ea91d",
   "payload_bytes": 446830,
   "payload_md5": "28198e7edc78fe371d0a0531b647e1e1"
  },
  {
   "Z": 78,
   "file": "elements/78.js",
   "bytes": 453017,
   "md5": "ad6bcdd6a0edf0662020021167491837",
   "payload_bytes": 452936,
   "payload_md5": "3653e9cf0a057f23e38635a1e6006331"
  },
  {
   "Z": 79,
   "file": "elements/79.js",
   "bytes": 459036,
   "md5": "8a19220efa3110e8ea41c6a599eb9513",
   "payload_bytes": 458955,
   "payload_md5": "43850efd757523535e60c9f4b85003fd"
  },
  {
   "Z": 80,
   "file": "elements/80.js",
   "bytes": 465128,
   "md5": "7c3812488123396241ee36909ba0274f",
   "payload_bytes": 465047,
   "payload_md5": "7a6eba061232d327b2ed9bc87e5bac67"
  },
  {
   "Z": 81,
   "file": "elements/81.js",
   "bytes": 469659,
   "md5": "f5d627568f2c59c2f876fe92c314cecf",
   "payload_bytes": 469578,
   "payload_md5": "802cb3d49492296fc7682446c1bb188c"
  },
  {
   "Z": 82,
   "file": "elements/82.js",
   "bytes": 475830,
   "md5": "ca855388084391f0be6002d7c8ed9623",
   "payload_bytes": 475749,
   "payload_md5": "e514d1416f1f9154725b852fcec9beff"
  },
  {
   "Z": 83,
   "file": "elements/83.js",
   "bytes": 481619,
   "md5": "50f1b44199f6cc3ab42e3323f2a0defa",
   "payload_bytes": 481538,
   "payload_md5": "36ed6b4668b80999d849545c93c479e5"
  },
  {
   "Z": 84,
   "file": "elements/84.js",
   "bytes": 487885,
   "md5": "010ac8065598e27dcc66ce0f571472bc",
   "payload_bytes": 487804,
   "payload_md5": "640918adc1cb7a06e8c95904c0d2c866"
  },
  {
   "Z": 85,
   "file": "elements/85.js",
   "bytes": 493870,
   "md5": "7ce157e7bac33aa752713d7ebcdfec34",
   "payload_bytes": 493789,
   "payload_md5": "e4896a57730bfe668b57f50c43ef1259"
  },
  {
   "Z": 86,
   "file": "elements/86.js",
   "bytes": 500289,
   "md5": "8fa76c7abe3beb1ef0ef5e3c8f6371cf",
   "payload_bytes": 500208,
   "payload_md5": "768b37e056a0bfa55acc55ba21d42941"
  },
  {
   "Z": 87,
   "file": "elements/87.js",
   "bytes": 504557,
   "md5": "93f1a4ed153da54b9125e163346490fc",
   "payload_bytes": 504476,
   "payload_md5": "62901838b69732c90745726796dc42f6"
  },
  {
   "Z": 88,
   "file": "elements/88.js",
   "bytes": 510803,
   "md5": "608f7c1637f85be8323aba8e504e0173",
   "payload_bytes": 510722,
   "payload_md5": "769e774b3a0aa54a54b803f80202d226"
  },
  {
   "Z": 89,
   "file": "elements/89.js",
   "bytes": 515017,
   "md5": "e9532789afc8db23d3c8f4487eeb0dac",
   "payload_bytes": 514936,
   "payload_md5": "be24ae26b7577d8a9edfd7f6e5feadc1"
  },
  {
   "Z": 90,
   "file": "elements/90.js",
   "bytes": 521374,
   "md5": "7d381b74da4586e23c33c0bba16b96ab",
   "payload_bytes": 521293,
   "payload_md5": "4c8562dc74da947a917fc025b3dd7d18"
  },
  {
   "Z": 91,
   "file": "elements/91.js",
   "bytes": 527520,
   "md5": "c38e7a76991e1bbe4ca803c039e2b6da",
   "payload_bytes": 527439,
   "payload_md5": "deec16fdb2281e3cb02a9fd701f49284"
  },
  {
   "Z": 92,
   "file": "elements/92.js",
   "bytes": 533514,
   "md5": "f47bd546ef6e5b51f78450cbb9c76c82",
   "payload_bytes": 533433,
   "payload_md5": "b268dc256b6c45e70189e9a29b2a54aa"
  },
  {
   "Z": 93,
   "file": "elements/93.js",
   "bytes": 539626,
   "md5": "da4abf75baf4ef495d8e2cfbc77ea37e",
   "payload_bytes": 539545,
   "payload_md5": "9f63a23590bc5472ac17002b0c5eca7a"
  },
  {
   "Z": 94,
   "file": "elements/94.js",
   "bytes": 545452,
   "md5": "c35eeecbb11fb54699a6444462221ef6",
   "payload_bytes": 545371,
   "payload_md5": "4b35ca5df799f84a0b2167df0e2d300d"
  },
  {
   "Z": 95,
   "file": "elements/95.js",
   "bytes": 551560,
   "md5": "863d46365aa8aa89fbb504d773e8b2e4",
   "payload_bytes": 551479,
   "payload_md5": "959af38c0a8fcb6f8aebc7599c7143a1"
  },
  {
   "Z": 96,
   "file": "elements/96.js",
   "bytes": 557626,
   "md5": "787e01e90c15597f318bcd0a6dd088d2",
   "payload_bytes": 557545,
   "payload_md5": "20cfeedfba22139c5a985428120c97a3"
  },
  {
   "Z": 97,
   "file": "elements/97.js",
   "bytes": 563634,
   "md5": "5355ec3028773aa6a5588b589d4e0416",
   "payload_bytes": 563553,
   "payload_md5": "925ce899de0c443ef51ffbb587a985aa"
  },
  {
   "Z": 98,
   "file": "elements/98.js",
   "bytes": 569635,
   "md5": "22adc6a376f02a169fb3e49a5ce310e0",
   "payload_bytes": 569554,
   "payload_md5": "46df754acfcf9ffef167fc50a55cdc0c"
  },
  {
   "Z": 99,
   "file": "elements/99.js",
   "bytes": 575623,
   "md5": "03df62c8e3c8cfda96ef257e2b3f3ea9",
   "payload_bytes": 575542,
   "payload_md5": "97b98b5c20413182a851d464f14991db"
  },
  {
   "Z": 100,
   "file": "elements/100.js",
   "bytes": 581718,
   "md5": "d2e05c539bbfb1bc1c9dc238ad992983",
   "payload_bytes": 581636,
   "payload_md5": "baca20cd877c030e69dd83c29790d627"
  },
  {
   "Z": 101,
   "file": "elements/101.js",
   "bytes": 587752,
   "md5": "de60c82be4d35d173d862594b3896a4c",
   "payload_bytes": 587670,
   "payload_md5": "d31940573a4d069398d44f0d389764c0"
  },
  {
   "Z": 102,
   "file": "elements/102.js",
   "bytes": 594184,
   "md5": "ba120633ffcae11cdaa7b73f4a0f3d42",
   "payload_bytes": 594102,
   "payload_md5": "d7f334a0b3b5cdf8fc38499ba831019f"
  },
  {
   "Z": 103,
   "file": "elements/103.js",
   "bytes": 598436,
   "md5": "d5bf78ebecf202a1d2594a5352cbd5ef",
   "payload_bytes": 598354,
   "payload_md5": "8705fb24619275d50b5e174d2faad4ae"
  },
  {
   "Z": 104,
   "file": "elements/104.js",
   "bytes": 569317,
   "md5": "f4c6736f10ca15bbffcdc0a718cff215",
   "payload_bytes": 569235,
   "payload_md5": "e1123dd69d5d4925a04979954851b07f"
  },
  {
   "Z": 105,
   "file": "elements/105.js",
   "bytes": 575146,
   "md5": "5baa30dae50738e7bf33df5f5f472f16",
   "payload_bytes": 575064,
   "payload_md5": "89b62d5d069a7a9e3fd3be7728e5356a"
  },
  {
   "Z": 106,
   "file": "elements/106.js",
   "bytes": 580989,
   "md5": "117be7d17fbe7c8e8abd3673b73c6ba1",
   "payload_bytes": 580907,
   "payload_md5": "1da6710f8fd883dbf81801ab8e3437f5"
  },
  {
   "Z": 107,
   "file": "elements/107.js",
   "bytes": 586790,
   "md5": "563c8fe8e67eeb486b3f5fe4a9f4bd9a",
   "payload_bytes": 586708,
   "payload_md5": "1f4bf4d5235f85fcc509cc5870b9849e"
  },
  {
   "Z": 108,
   "file": "elements/108.js",
   "bytes": 592595,
   "md5": "fc9a60e8ca4d447d44190e5abf4bbc11",
   "payload_bytes": 592513,
   "payload_md5": "8f3392528fe84196a8c13d3a75bf81e1"
  },
  {
   "Z": 109,
   "file": "elements/109.js",
   "bytes": 510324,
   "md5": "ceaaf6810ce1dc26342daf3439fe5c3b",
   "payload_bytes": 510242,
   "payload_md5": "e7a04d4afbcae8f3f742dec7342eeddd"
  },
  {
   "Z": 110,
   "file": "elements/110.js",
   "bytes": 515301,
   "md5": "6c00a1c1254f41d69baa9fa13120423d",
   "payload_bytes": 515219,
   "payload_md5": "5d0777f7ad8be809c21d1bdad608d2fc"
  },
  {
   "Z": 111,
   "file": "elements/111.js",
   "bytes": 520263,
   "md5": "6cf9672c5fcac8dd7f214cd61d106926",
   "payload_bytes": 520181,
   "payload_md5": "38ebdc043d2e4247494b81b54b8ff813"
  },
  {
   "Z": 112,
   "file": "elements/112.js",
   "bytes": 525247,
   "md5": "f70b8d8992eb65a45e0ee7ef9cdf37af",
   "payload_bytes": 525165,
   "payload_md5": "f393576314130d31686b38336a38847b"
  },
  {
   "Z": 113,
   "file": "elements/113.js",
   "bytes": 528338,
   "md5": "ba4270fb5fd02c9937568ce4412f9fba",
   "payload_bytes": 528256,
   "payload_md5": "010a35cf2a1e4b0b2092a3444bf5d529"
  },
  {
   "Z": 114,
   "file": "elements/114.js",
   "bytes": 533353,
   "md5": "dccad32ddfab12d970e3a2989836182e",
   "payload_bytes": 533271,
   "payload_md5": "9895f28a46ee34e22625f177b9f8a802"
  },
  {
   "Z": 115,
   "file": "elements/115.js",
   "bytes": 538349,
   "md5": "6065618cd5ee612deed2142539a311d3",
   "payload_bytes": 538267,
   "payload_md5": "331ffead0f81c7763b0d09effc8027bf"
  },
  {
   "Z": 116,
   "file": "elements/116.js",
   "bytes": 543283,
   "md5": "c139fc3f8f8c7f3bb8d65c3cfadaa91f",
   "payload_bytes": 543201,
   "payload_md5": "f7507de1e7f8e001f04dbd47fb78ca98"
  },
  {
   "Z": 117,
   "file": "elements/117.js",
   "bytes": 548286,
   "md5": "ccdfeeb27353c6df78a95c5f45d9177d",
   "payload_bytes": 548204,
   "payload_md5": "ac34183d02cbdfb41ee7e7b118ad197c"
  },
  {
   "Z": 118,
   "file": "elements/118.js",
   "bytes": 553277,
   "md5": "7c78b39d7d618944452c24bb882882c3",
   "payload_bytes": 553195,
   "payload_md5": "98bc4be459019dfa723ff4d69e63ec39"
  },
  {
   "Z": 119,
   "file": "elements/119.js",
   "bytes": 674813,
   "md5": "c477f65ebf72f78e1fb443d299b6017d",
   "payload_bytes": 674731,
   "payload_md5": "80f869237e7361d614bb49f182eaf4ea"
  },
  {
   "Z": 120,
   "file": "elements/120.js",
   "bytes": 719612,
   "md5": "eeebcee8a72dfa26188dc30cc8b1360b",
   "payload_bytes": 719530,
   "payload_md5": "3287c8b090f4a38390bb33cbcc53bbe8"
  }
 ],
 "protocol": {
  "index": "data/index.js sets window.__mi.index",
  "element": "data/elements/<Z>.js sets window.__mi.el[Z]",
  "why": "the page opens from a file:// URL on a phone, where fetch() of a local file is blocked and a <script src> is not",
  "encoding": "utf-8"
 }
};
