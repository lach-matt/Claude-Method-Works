#!/usr/bin/env python3
"""
faithful.py -- what a faithful copy's specification must carry (M-RULINGS items 86-88: the goal is a faithful copy;
the README -- "a software update patch presented as a README file telling position to what to construct with what it
has" -- is what crosses; M's order of work puts this link first).  READ where sources exist, deduced (M-DEDUCE),
computed where it can be.  Not seated; verified once, findings applied (HISTORY at the end; first written 'not
verified').  M's words are carried as hypotheses, never as results.

WHAT FOLLOWS THE WORK (each from the sections below)
  * A FAITHFUL CLASSICAL COPY NEEDS FAR LESS THAN ANY SNAPSHOT OF THE BODY.  The board's four counts (measure.py,
    imported) describe the body at an instant: 9.5e27 to 1.1e29 bits.  Much of what a snapshot fixes -- the positions
    of freely diffusing molecules -- the body itself scrambles within picoseconds (F3); a destination at body
    temperature supplies its own.  What the README must carry is what the destination cannot regenerate (F4).
  * THE IDENTITY-BEARING LAYER IS CLASSICAL, SO A CLASSICAL README LOSES NOTHING OF IT (F2), under Tegmark's
    identity-theory premise and the uncontested neuron-firing margin: decoherence in 1e-20 to 1e-19 s against
    dynamics of 1e-3 to 1e-1 s.  (His microtubule figure is disputed; that dispute is the boundary.)
  * ITS SIZE (F5): synapse wiring and strength, 30 to 41 bits per synapse, 5.5e9 bits per cubic millimetre of cortex at
    the 41-bit coding -- against the 1.4 petabytes (1.1e16 bits) the electron-microscope read of that cubic millimetre
    produced.  Scaled to a cortex (a named, unread volume) it is of order 1e15 bits: 3.5e12 to 4.0e13 times below the
    snapshot counts.  An order-of-magnitude estimate under H-WIRING-SUFFICES whose named inputs pull in opposite
    directions; neither a floor nor a ceiling is shown.  First written 'a floor of the identity layer'.
  * WHAT CROSSES NEEDS NO QUANTUM RESOURCES: no entanglement, no two-bits-per-qubit teleportation overhead, no years-long
    quantum memory (S1C-O6 goes silent on this path), and a classical README can wait without decohering.  Every
    channel shortfall the board prices in bits falls by the same factor as the count.
  * THE READ NEED NOT RESOLVE ATOMS FOR THAT LAYER (F6): synapses were read at ~30 nm sections -- a candidate narrowing
    of S1C-O1 under H-WIRING-SUFFICES.  The only read demonstrated at that resolution destroys the tissue.
  * NO-CLONING DOES NOT BIND A CLASSICAL COPY (F1): a classical encoding replicates perfectly ("if and only if a basis
    to which psi belongs is known" -- which a README meets), so the no-cloning theorem does not require destroying the
    original.  H-RETIRE-A's stated reason (item 32: "to satisfy the no-cloning clause") does not apply to a classical
    README, under H-IDENTITY-IN-DYNAMICS; other grounds are not examined -- a question for M, not a result.  First
    written 'physics no longer requires the original to be retired'.
  * IT BEARS ON TWO OPEN ITEMS.  H-WHICH-COUNT (S1B-O1): the README size is a fifth quantity, not one of the four
    counts; it singles none out, and M's ruling at item 33 ("Keep all four") stands.  Whether "the object's
    information" should be read, for a faithful copy, as the identity core is a question for M.  BULK3-O1 and
    crossing.py's D3 (classical or quantum?): F2 answers 'classical' for the identity layer, conditionally.
  * Boundary (item 82): a classical README cannot carry an unknown quantum state; the README shrinks only by what the
    builder already knows (F4); the body outside the cortex's wiring (cerebellum, subcortex, morphology, acquired body
    state) is unpriced (OPEN); and the copy is faithful at the instant of the read -- copy and original then diverge
    (Tegmark p.11: neural updates "may have to involve some classical randomness").

    python3 faithful.py              report
    python3 faithful.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL lines printed and not counted
    python3 faithful.py --json       the numbers as JSON

SOURCES READ (2026-10-06; routes: alphaXiv answer_pdf_queries on open arXiv copies, printed pages; Firecrawl scrape or
research index on open copies)
  Tegmark quant-ph/9907009v2 (alphaXiv): "the decoherence timescales (~10^-13 - 10^-20 seconds) are typically much
    shorter than the relevant dynamical timescales (~10^-3 - 10^-1 seconds)" (abstract, p.1); Table 1 (p.8): neuron
    with colliding ion or H2O 10^-20 s, nearby ion 10^-19 s, microtubule 10^-13 s; "fall squarely in the classical
    category, by a margin exceeding ten orders of magnitude" (p.8); if firing patterns correspond to perceptions,
    "consciousness itself cannot be of a quantum nature even if there is a yet undiscovered physical process in the
    brain with a very long decoherence time" (p.8); "we have tacitly assumed that consciousness is synonymous with
    certain brain processes" (p.11) -- carried as H-IDENTITY-IN-DYNAMICS.
  Hagan, Hameroff, Tuszynski quant-ph/0005025v1 (verifier-READ, p.1): recompute microtubule decoherence at 1e-5 to 1e-4 s
    (1e-2 to 1e-1 s with ordered water), and agree (p.2) that superpositions of firing are unlikely.  The microtubule
    margin is disputed; the firing margin is not.
  Scarani, Iblisdir, Gisin, Acin quant-ph/0511088v1 (alphaXiv): "No quantum operation exists that can duplicate
    perfectly an arbitrary quantum state" (p.3); "one cannot measure the state |psi> of a single quantum system"
    (p.3); replication "can be done perfectly and with probability 1 if and only if a basis to which psi belongs is
    known" (p.2); DNA's encoding "is classical ... it can be replicated perfectly" (p.2), with footnote 2: whether
    nature processes that information classically "is an open question"; in teleportation "the original has to be
    destroyed in the process" (p.30); Buzek-Hillery's optimal universal copier reaches fidelity 5/6 (p.4).
  Bartol et al., eLife 2015;4:e10778 (Firecrawl scrape, open): "a minimum of 26 distinguishable synaptic strengths,
    corresponding to storing 4.7 bits of information at each synapse"; titled "Nanoconnectomic upper bound on the
    variability of synaptic plasticity"; rat hippocampal CA1, spine-head size as the proxy for strength, excitatory
    spine synapses; the digest: "Additional measurements in the same and other brain regions are needed".
  Shapson-Coe et al., bioRxiv 10.1101/2021.05.29.446289v4 (Firecrawl scrape, open): "a 1 mm3 volume ... cut more than
    5000 slices at ~30 nm"; "57,216 cells, hundreds of millions of neurites and 133.7 million synaptic connections";
    "The 1.4 petabyte electron microscopy volume"; "Glia outnumbered neurons 2:1"; "incompleteness of the automated
    segmentation caused by split and merge errors" (abstract).  One temporal-lobe surgical sample.
  Azevedo et al., J. Comp. Neurol. 2009 (pmid 19226510; Firecrawl research index, abstract; verifier-READ via Europe
    PMC): "86.1 +/- 8.1 billion NeuN-positive cells ("neurons")"; "only 19% of all neurons located in the cerebral
    cortex".
  Nurk et al., Science 2022 (PMC9186530; verifier-READ abstract): "a complete 3.055 billion base pair (bp) sequence of a
    human genome, T2T-CHM13, that includes gapless assemblies for all chromosomes except Y".  First quoted from the
    research index's summary as "the first truly complete 3.055 billion base pair (bp) sequence", which the
    verifier did not find in the printed abstract.
  Holz, Heil, Sacco, PCCP 2 (2000) 4740, Table, as transcribed by O. Dietrich's compilation (Firecrawl scrape,
    dtrx.de/od/diff, Table 5): water self-diffusion D = 2.895 (35 C) and 3.222 (40 C) x 10^-9 m^2/s.  SECONDARY.

F1 [READ Scarani; computed]  A classical copy is possible and a quantum one is not.  The CNOT copier copies |0> and |1>
   exactly and fails on |+> (each output's fidelity with |+> is 1/2): computed -- this copier fails; that every
   copier fails is no-cloning, READ.  So the faithful copy M ruled for (item 87) is a copy of what is classical in the
   object.  A README fixes the basis, so its copy is perfect, and making it does not require destroying the original.
F2 [READ Tegmark; Hagan et al.]  What carries identity is classical at body temperature: neuron firing decoheres in
   1e-20 to 1e-19 s against dynamics of 1e-3 to 1e-1 s, so nothing of it is lost to a classical description -- under
   H-IDENTITY-IN-DYNAMICS and the uncontested firing margin.  First written 'nothing of them is lost', without the
   dispute.  The quantum remainder (single-molecule states, spins; microtubules if Hagan et al. are right) is not
   identity-bearing under Tegmark's p.8 argument; it is the boundary.
F3 [computed from READ D; H-BULK-WATER]  Freely diffusing positions are not carried.  Bulk water at 310.15 K has D =
   3.02e-9 m^2/s (Arrhenius interpolation of Holz's 35 and 40 C values); t = d^2/(6D) gives 5.5e-13 s for 1 A, and a
   spread of about 0.135 mm in one second.  (At 1 A and sub-picosecond times this is below the diffusive regime, and
   tissue water is slower than bulk water -- not READ -- so the figure is 'of order picoseconds'; the check asks
   'more than eight orders' below the fastest dynamics.)  So those positions are thermal microstate: a body-
   temperature destination supplies its own.  NOT covered: compartment concentrations (ion gradients, membrane
   potentials), which are macrostate the recipe must fix.  The board's thermal-entropy count (2.84e28 bits,
   CONDITIONAL) is the microstate information a body-temperature destination supplies for itself; it neither bounds
   nor is subtracted from the README.  First written 'the bulk of its atoms' (not READ) and 'the size of what the
   copy may leave out'.  CONTRAST: a solid-like D (illustrative 1e-20 m^2/s) holds a 1 A placement for 0.17 s.
F4 [deduced; computed illustration]  The README is the conditional description: what the destination cannot
   regenerate given what its builder already knows (H-REGENERABLE).  Computed: a megabyte generated by a known rule
   from a 32-byte seed is regenerated exactly from the seed; zlib cannot shrink that megabyte at all (CONTRAST: nor
   random data).  CONTROL: one flipped bit in the seed changes about half the output bits -- the exactness comes from
   the seed.  First written with the random-data arm labelled CONTROL; it cannot fail, so it is a CONTRAST.
F5 [READ; computed; CONDITIONAL]  The identity core, under H-WIRING-SUFFICES.  Listing each neuron's input synapses in
   order costs log2(86.1e9) = 36.3 bits per synapse for the partner plus log2(26) = 4.70 for the strength: 41.0 bits.
   Coding each neuron's inputs as an unordered set saves about log2(k/e) per synapse, with k = synapses per neuron
   (about 7,000, computed from Shapson-Coe's abstract: 133.7 million synapses over the third of 57,216 cells that are
   neurons): about 30 bits.  At 133.7 million synapses per mm^3 (H-DENSITY-TYPICAL) the 41-bit coding gives 5.49e9
   bits per mm^3 -- 2.0e6 times smaller than the 1.12e16-bit read that produced it.  For a cortex of H-GREY-VOLUME
   (5e5 mm^3, NAMED-NOT-READ) it is 2.7e15 bits.  The cerebral cortex holds only 19 % of the brain's neurons
   (Azevedo); the cerebellum and subcortical structures are outside the figure.  Directions: the address coding is an
   upper side; Bartol's 26 is "a minimum" (a lower side) and comes from rat CA1 (H-STRENGTH-TRANSFERS); the cortex-
   only scope and every omitted state (synapse position, morphology, glia, molecular and electrical state) are lower
   sides.  So: an order-of-magnitude estimate, neither floor nor ceiling.  The genome adds 1.22e10 bits for a diploid
   set (H-DIPLOID; CHM13 omits Y).
F6 [READ; deduced]  What the read must capture for that layer: synapses and their sizes, read at ~30 nm sections, not
   atoms -- a candidate narrowing of S1C-O1 for the identity layer, under H-WIRING-SUFFICES.  The read that exists
   (serial sectioning) destroys the tissue; a non-destructive read at that resolution is OPEN.
F7 [deduced]  What the README is: the identity core, the genome, and the recipe for everything the builder
   regenerates (H-REGENERABLE) -- including construction information that need not be identity-bearing (neuron
   morphology, axon routing), which could be comparable to the core in size and is OPEN unless the builder chooses
   the layout.

NAMED HYPOTHESES AND PREMISES
  H-IDENTITY-IN-DYNAMICS (Tegmark's premise, READ as his assumption, p.11): identity is carried by brain processes.
  H-WIRING-SUFFICES: those processes are fixed, for copying, by synaptic wiring and strengths (not READ as shown).
  H-ADDRESS-UNIFORM: each synapse's partner coded with log2 N bits, no wiring structure used (an upper side).
  H-STRENGTH-TRANSFERS: rat CA1's 26 strength levels are taken for human cortex.
  H-DENSITY-TYPICAL: Shapson-Coe's one temporal-lobe sample's synapse density is typical of cortex.
  H-GREY-VOLUME: 5e5 mm^3 of cortex (NAMED-NOT-READ).  Every whole-cortex figure is CONDITIONAL on it.
  H-BULK-WATER: tissue water is taken at bulk-water diffusion.
  H-REGENERABLE: the builder regenerates, from a recipe, every detail the README omits.  Load-bearing, not shown for
    a body; F4 shows only that a README's size is set by the builder's knowledge.
  H-DIPLOID: two haploid sets of the CHM13 length (no Y).
  M's: H-README, H-SAME-NEEDS-MATTER (what arrives is a copy), H-RETIRE-A (item 32; its reason examined in F1).

OPEN
  1. The brain outside the cortex (cerebellum, subcortex) and acquired body state (immune memory, scars, the
     microbiome, bone shape): not priced.
  2. A builder that regenerates a body from a recipe (H-REGENERABLE; with S1C-O2, placement); construction
     information (morphology, routing).
  3. A non-destructive read at synapse resolution.
  4. Whether H-WIRING-SUFFICES holds: what else of the brain's state identity needs (molecular, electrical).
  5. A READ whole-brain synapse total, in place of H-GREY-VOLUME and H-DENSITY-TYPICAL; human strength levels.

HISTORY (verifier, 2026-10-06; first-written claims kept above where they stood)
  'a floor of the identity layer' -> an estimate with inputs pulling both ways; Bartol's scope and the cortex-only
  scope named; the F4 random-data arm relabelled CONTRAST and a seed-flip CONTROL added; 'physics no longer requires
  the original to be retired' -> no-cloning no longer requires it; Tegmark's microtubule margin shown disputed (Hagan
  et al.); H-WHICH-COUNT and BULK3-O1 tied in; F3's regime, scope and the thermal count's meaning corrected; the Nurk
  quote replaced with the printed abstract; numbers matched to the printout (3.02e-9, 0.135 mm, 3.5e12 to 4.0e13).
"""
import hashlib
import json
import math
import os
import sys
import zlib
import contextlib
import io
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)

# ---------------------------------------------------------------------------------------------------- READ values
TEGMARK_TAU_DEC = (1e-20, 1e-13)        # s, p.1 and Table 1 p.8
TEGMARK_TAU_DYN = (1e-3, 1e-1)          # s, p.1
BARTOL_STRENGTHS = 26                   # eLife 2015
BARTOL_BITS = 4.7                       # as printed
AZEVEDO_NEURONS = 86.1e9                # abstract, +/- 8.1e9
SHAPSON_SYN_PER_MM3 = 133.7e6           # abstract, 1 mm^3
SHAPSON_SLICE_M = 30e-9                 # "~30 nm"
SHAPSON_CELLS = 57216                   # abstract
SHAPSON_GLIA_PER_NEURON = 2             # "Glia outnumbered neurons 2:1"
SHAPSON_BYTES = 1.4e15                  # "1.4 petabyte"
T2T_BP = 3.055e9                        # abstract (haploid CHM13)
HOLZ_D = {308.15: 2.895e-9, 313.15: 3.222e-9}   # m^2/s, SECONDARY transcription

# ---------------------------------------------------------------------------------------------------- named values
T_BODY = 310.15                         # K (37 C)
H_GREY_VOLUME_MM3 = 5e5                 # H-GREY-VOLUME, NAMED-NOT-READ, illustrative
D_SOLID_ILLUSTRATIVE = 1e-20            # m^2/s, the F3 contrast only


def _measure():
    """The board's four snapshot counts, imported from measure.py (never retyped)."""
    spec = importlib.util.spec_from_file_location("d68_measure_faithful", os.path.join(D68, "measure.py"))
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
            ob = m.object_bits()
    finally:
        sys.path[:] = saved
    return {"species": ob["species_sequence_bits"], "grid_1A": ob["grid"][1e-10]["bits"],
            "grid_0p1A": ob["grid"][1e-11]["bits"], "thermal": ob["thermo_bits"], "atoms": ob["atoms"]}


# ---------------------------------------------------------------------------------------------------- F1
def copier_fidelities():
    """The CNOT copier |psi>|0> -> CNOT: fidelity of each output qubit with |psi>, for |0>, |1> and |+>."""
    def cnot(state):                     # state: dict over (a, b) in {0,1}^2
        return {(a, b ^ a): amp for (a, b), amp in state.items()}

    def reduced_fidelity(state, psi, which):
        # rho of one qubit; fidelity <psi|rho|psi> for a pure target psi = (c0, c1)
        rho = [[0j, 0j], [0j, 0j]]
        for (a, b), amp in state.items():
            for (a2, b2), amp2 in state.items():
                if which == 0 and b == b2:
                    rho[a][a2] += amp * amp2.conjugate()
                if which == 1 and a == a2:
                    rho[b][b2] += amp * amp2.conjugate()
        c = psi
        return sum((c[i].conjugate() * rho[i][j] * c[j]) for i in range(2) for j in range(2)).real

    out = {}
    s = 1 / math.sqrt(2)
    for name, psi in (("0", (1 + 0j, 0j)), ("1", (0j, 1 + 0j)), ("+", (s + 0j, s + 0j))):
        state = {(0, 0): psi[0], (1, 0): psi[1]}
        st = cnot(state)
        out[name] = (reduced_fidelity(st, psi, 0), reduced_fidelity(st, psi, 1))
    return out


# ---------------------------------------------------------------------------------------------------- F3
def water_D(T=T_BODY):
    """Arrhenius interpolation of Holz's 35 and 40 C values (log D linear in 1/T)."""
    (T1, D1), (T2, D2) = sorted(HOLZ_D.items())
    slope = (math.log(D2) - math.log(D1)) / (1 / T2 - 1 / T1)
    return math.exp(math.log(D1) + slope * (1 / T - 1 / T1))


def forget_time(d=1e-10, D=None):
    """Mean time to diffuse a distance d in three dimensions, t = d^2/(6D)."""
    D = water_D() if D is None else D
    return d * d / (6 * D)


def spread(t=1.0, D=None):
    D = water_D() if D is None else D
    return math.sqrt(6 * D * t)


# ---------------------------------------------------------------------------------------------------- F4
def readme_demo(n_bytes=1 << 20, seed=b"faithful.py README seed, 32 byte"):
    """A megabyte generated by a known rule (SHA-256 in counter mode) from a short seed: the README is the seed;
    the builder that knows the rule regenerates the data exactly.  CONTROL: data with no known rule (os.urandom),
    whose best general README (zlib, level 9) is no smaller than the data."""
    def generate(s, n):
        out, i = bytearray(), 0
        while len(out) < n:
            out += hashlib.sha256(s + i.to_bytes(8, "big")).digest()
            i += 1
        return bytes(out[:n])
    data = generate(seed, n_bytes)
    rebuilt = generate(seed, n_bytes)
    flipped = generate(bytes([seed[0] ^ 1]) + seed[1:], n_bytes)
    differ = sum(bin(a ^ b).count("1") for a, b in zip(data, flipped)) / (8 * n_bytes)
    rand = os.urandom(n_bytes)
    return {"seed_bytes": len(seed), "data_bytes": len(data), "exact": rebuilt == data, "flip_differ": differ,
            "zlib_of_rule_data": len(zlib.compress(data, 9)) / len(data),
            "zlib_of_random": len(zlib.compress(rand, 9)) / len(rand)}


# ---------------------------------------------------------------------------------------------------- F5
def identity_core(volume_mm3=H_GREY_VOLUME_MM3):
    addr = math.log2(AZEVEDO_NEURONS)
    strength = math.log2(BARTOL_STRENGTHS)
    per_syn = addr + strength
    neurons_sample = SHAPSON_CELLS / (1 + SHAPSON_GLIA_PER_NEURON)
    k = SHAPSON_SYN_PER_MM3 / neurons_sample
    # an unordered set of k partners among N: log2 C(N, k) bits per neuron, exactly (lgamma)
    lgC = (math.lgamma(AZEVEDO_NEURONS + 1) - math.lgamma(k + 1) - math.lgamma(AZEVEDO_NEURONS - k + 1)) / math.log(2)
    per_syn_unordered = lgC / k + strength
    per_mm3 = SHAPSON_SYN_PER_MM3 * per_syn
    raw_bits_mm3 = SHAPSON_BYTES * 8
    genome = 2 * T2T_BP * 2            # 2 bits per base, diploid (H-DIPLOID)
    return {"addr_bits": addr, "strength_bits": strength, "per_synapse_bits": per_syn, "per_mm3_bits": per_mm3,
            "synapses_per_neuron": k, "per_synapse_bits_unordered": per_syn_unordered,
            "raw_read_bits_mm3": raw_bits_mm3, "raw_over_readme": raw_bits_mm3 / per_mm3,
            "total_bits": per_mm3 * volume_mm3, "volume_mm3": volume_mm3, "genome_bits": genome}


def compute():
    m = _measure()
    ic = identity_core()
    D = water_D()
    return {"copier": copier_fidelities(),
            "decoherence_margin": TEGMARK_TAU_DYN[0] / TEGMARK_TAU_DEC[1],
            "water_D_310K": D, "forget_1A_s": forget_time(), "spread_1s_m": spread(),
            "forget_1A_solid_s": forget_time(D=D_SOLID_ILLUSTRATIVE),
            "holz_endpoints": {T: water_D(T) for T in HOLZ_D},
            "readme": readme_demo(), "identity": ic, "snapshot": m,
            "snapshot_over_core": m["species"] / ic["total_bits"],
            "snapshot_over_core_max": m["grid_0p1A"] / ic["total_bits"]}


def report():
    d = compute()
    ic, m = d["identity"], d["snapshot"]
    print("faithful.py -- what a faithful copy's specification must carry (M items 86-88; not verified; not seated)\n")
    print("F1 copier fidelities (each output with the input): |0> %s, |1> %s, |+> %s" % tuple(
        "(%.2f, %.2f)" % d["copier"][k] for k in ("0", "1", "+")))
    print("F2 decoherence margin (Tegmark): dynamics / decoherence >= %.0e" % d["decoherence_margin"])
    print("F3 water at 310 K: D = %.3e m^2/s; forgets 1 A in %.2e s; spreads %.2e m in 1 s" % (
        d["water_D_310K"], d["forget_1A_s"], d["spread_1s_m"]))
    r = d["readme"]
    print("F4 README demo: %d-byte seed regenerates %d bytes exactly (%s); one flipped seed bit changes %.4f of the "
          "output bits; zlib of that data %.4f, of random %.4f" % (
              r["seed_bytes"], r["data_bytes"], r["exact"], r["flip_differ"], r["zlib_of_rule_data"],
              r["zlib_of_random"]))
    print("F5 identity core: %.2f + %.2f = %.2f bits per synapse; %.3e bits per mm^3 (raw read %.3e, %.2e times "
          "larger); cortex of %.0e mm^3 (H-GREY-VOLUME): %.2e bits; genome (diploid) %.3e bits" % (
              ic["addr_bits"], ic["strength_bits"], ic["per_synapse_bits"], ic["per_mm3_bits"],
              ic["raw_read_bits_mm3"], ic["raw_over_readme"], ic["volume_mm3"], ic["total_bits"], ic["genome_bits"]))
    print("   unordered-set coding (k = %.0f synapses per neuron): %.1f bits per synapse" % (
        ic["synapses_per_neuron"], ic["per_synapse_bits_unordered"]))
    print("   the board's snapshot counts (measure.py): species %.2e, grid 1 A %.2e, grid 0.1 A %.2e, thermal %.2e "
          "bits; snapshot / identity core = %.2e to %.2e" % (m["species"], m["grid_1A"], m["grid_0p1A"], m["thermal"],
                                                             d["snapshot_over_core"], d["snapshot_over_core_max"]))
    print("F6 the read: sections of %.0f nm (Shapson-Coe)" % (SHAPSON_SLICE_M * 1e9))


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    d = compute()
    cp = d["copier"]
    chk("F1: the CNOT copier copies the classical states exactly (|0>: %.3f, %.3f; |1>: %.3f, %.3f)" % (
        cp["0"] + cp["1"]), all(abs(f - 1) < 1e-12 for f in cp["0"] + cp["1"]))
    chk("F1: on the superposition |+> each output's fidelity is %.3f, %.3f -- the copy fails (no-cloning), and the "
        "fidelity test can see a failure" % cp["+"], all(abs(f - 0.5) < 1e-12 for f in cp["+"]), ctl=True)
    t = d["forget_1A_s"]
    chk("F3: water at 310 K (D = %.3e m^2/s, from READ values) is of order %.2e s for a 1 A placement (H-BULK-WATER), more than eight "
        "orders below the fastest brain dynamics (%.0e s)" % (d["water_D_310K"], t, TEGMARK_TAU_DYN[0]),
        t * 1e8 < TEGMARK_TAU_DYN[0] and 2.9e-9 < d["water_D_310K"] < 3.2e-9)
    chk("F3: a solid-like D (illustrative %.0e m^2/s) holds the same placement %.2e s -- positions that would have to "
        "be carried" % (D_SOLID_ILLUSTRATIVE, d["forget_1A_solid_s"]),
        d["forget_1A_solid_s"] > TEGMARK_TAU_DYN[1], contrast=True)
    r = d["readme"]
    chk("F4: a %d-byte README regenerates %d bytes exactly for a builder that knows the rule (%s), though zlib cannot "
        "shrink that data (%.4f): the README's size is set by the builder's knowledge" % (
            r["seed_bytes"], r["data_bytes"], r["exact"], r["zlib_of_rule_data"]),
        r["exact"] and r["zlib_of_rule_data"] > 0.99)
    chk("F4: one flipped bit in the seed changes %.4f of the output bits -- the exactness comes from the seed, not "
        "from determinism alone" % r["flip_differ"], 0.45 < r["flip_differ"] < 0.55, ctl=True)
    chk("F4: for data with no rule the builder knows, the best general README (zlib) is no smaller than the data "
        "(%.4f)" % r["zlib_of_random"], r["zlib_of_random"] > 0.99, contrast=True)
    ic = d["identity"]
    chk("F5: log2 of Bartol's 26 strengths is %.3f, the 4.7 bits per synapse they print" % ic["strength_bits"],
        abs(ic["strength_bits"] - BARTOL_BITS) < 0.01)
    chk("F5: the identity core is %.3e bits per mm^3, %.2e times smaller than the %.3e-bit read of the same volume" % (
        ic["per_mm3_bits"], ic["raw_over_readme"], ic["raw_read_bits_mm3"]), ic["raw_over_readme"] > 1e6)
    chk("F5: coding each neuron's inputs as an unordered set (k = %.0f, computed from Shapson-Coe) gives %.1f bits per "
        "synapse, below the ordered coding's %.1f: the range is 30 to 41" % (
            ic["synapses_per_neuron"], ic["per_synapse_bits_unordered"], ic["per_synapse_bits"]),
        28 < ic["per_synapse_bits_unordered"] < 32 < ic["per_synapse_bits"])
    chk("F5: with H-GREY-VOLUME the core (%.2e bits) sits %.2e to %.2e times below the board's snapshot counts "
        "(imported from measure.py) -- CONDITIONAL, an order-of-magnitude estimate" % (
            ic["total_bits"], d["snapshot_over_core"], d["snapshot_over_core_max"]),
        d["snapshot_over_core"] > 1e10 and d["snapshot"]["species"] < d["snapshot"]["grid_1A"])
    structural.append("F2: Tegmark's margin, dynamics / decoherence >= %.0e (arithmetic on READ values)" %
                      d["decoherence_margin"])
    structural.append("F3: the Arrhenius interpolation returns Holz's endpoints: %s" % ", ".join(
        "%.3e" % v for v in d["holz_endpoints"].values()))
    structural.append("F5: the genome (diploid, 2 bits per base) is %.3e bits, %.1e of the core" % (
        ic["genome_bits"], ic["genome_bits"] / ic["total_bits"]))
    structural.append("F5: water spreads %.2e m in one second at 310 K" % d["spread_1s_m"])
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("faithful.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
