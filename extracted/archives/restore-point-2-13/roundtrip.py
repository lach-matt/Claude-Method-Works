#!/usr/bin/env python3
"""roundtrip.py — four questions asked before a generated artefact is trusted.

Register 1389. The protocol exists because three artefacts were called generated
while carrying a hand-authored region their generator never wrote, and every
rebuild silently discarded it (registers 1373, 1386, 1388). The build exited 0
and the file looked complete; only a diff of the regeneration against the held
copy could see it.

    DECLARE   does the generator declare every region it does not write?
    ISOLATE   never regenerate over the held copy.
    DIFF      byte-identical once the build date is normalised.
    REFUSE    does it write nothing rather than a partial file?

Question 2 is not caution but a recorded consequence: running an in-place
generator as a test destroyed the artefact it was testing (register 1388). Every
generator here is run in a scratch copy of the tree, whatever its write mode.

NORMALISATION, register 1433. Only the build date is substituted. The two
progress-line regexes this file once carried are RETIRED, not kept as a safety
net: they accommodated zeno writing its log to stdout, and the defect they
accommodated is now fixed at source. A workaround that succeeds hides the defect
it accommodates; retiring it is how you find out whether the repair took.
"""
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# artefact, generator, write mode, declared hand-authored tail (None if fully generated)
ARTEFACTS = [
    ("COMPENDIUM.md", "compendium.py",  "stdout",   "COMPENDIUM-TAIL.md"),
    ("INDICES.md",    "indices.py",     "stdout",   "INDICES-TAIL.md"),
    ("PHYSICS.md",    "physics.py",     "in-place", "PHYSICS-TAIL.md"),
    ("SPECTRA.md",    "spectra.py",     "stdout",   None),
    ("REGISTER.md",   "register_gen.py","stdout",   None),
    # R 1655's lesson applied to a TSV: roundtrip covered five markdown artefacts
    # and no TSV, which is how the value store sat outside C3 and could not be
    # shown not to have drifted (R 1674). MEASUREMENTS.tsv is the authored input
    # the generator does not write, so it stands where a hand-authored tail
    # stands for the markdown artefacts: DECLARE names it, REFUSE removes it.
    ("MEASUREMENTS-DERIVED.tsv", "store_gen.py", "in-place", "MEASUREMENTS.tsv"),
]

DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


BUILD = re.compile(r"(Generated[^\n]{0,60}?on )(\d{4}-\d{2}-\d{2})")


def NORM(held, gen):
    """Adopt the held copy's BUILD date — and only that.

    FIXED after a failure of this gate on itself: the previous version
    substituted the held copy's first date into EVERY date-shaped string in the
    generated text, so a legitimate date INSIDE the content — a dated correction
    note in mathreg.py — was silently rewritten and the diff failed. A
    normalisation that reaches into content is not a normalisation; it is a
    corruption that happens to be invisible when the content carries no dates."""
    h = BUILD.search(held)
    if not h:
        return (held, gen)
    return (held, BUILD.sub(lambda m: m.group(1) + h.group(2), gen))


def scratch_tree():
    """ISOLATE — a full copy, so no generator can reach the held artefacts."""
    d = tempfile.mkdtemp(prefix="roundtrip.")
    for f in os.listdir(HERE):
        p = os.path.join(HERE, f)
        if os.path.isfile(p):
            shutil.copy2(p, d)
        elif os.path.isdir(p) and f not in (".zeno", "__pycache__"):
            shutil.copytree(p, os.path.join(d, f), dirs_exist_ok=True)
    return d


def regenerate(d, gen, artefact, mode):
    r = subprocess.run([sys.executable, gen], cwd=d, capture_output=True,
                       text=True, timeout=1800)
    if r.returncode != 0:
        return None, f"generator exited {r.returncode}"
    if mode == "stdout":
        return r.stdout, None
    p = os.path.join(d, artefact)
    return (open(p, encoding="utf-8").read(), None) if os.path.exists(p) else (None, "no artefact written")


def declares(gen, tail):
    """DECLARE — the generator names the region it does not write."""
    if tail is None:
        return True, "fully generated, nothing to declare"
    src = open(os.path.join(HERE, gen), encoding="utf-8").read()
    return (tail in src), ("declares " + tail if tail in src else "DOES NOT declare " + tail)


def refuses(d, gen, artefact, tail, mode):
    """REFUSE — with the tail removed, write nothing rather than a partial file."""
    if tail is None:
        return True, "no tail — not applicable"
    tp = os.path.join(d, tail)
    ap = os.path.join(d, artefact)
    before = open(ap, "rb").read() if os.path.exists(ap) else None
    os.remove(tp)
    r = subprocess.run([sys.executable, gen], cwd=d, capture_output=True,
                       text=True, timeout=1800)
    after = open(ap, "rb").read() if os.path.exists(ap) else None
    if mode == "in-place":
        ok = r.returncode != 0 and before == after
        why = f"exit {r.returncode}, artefact {'unchanged' if before == after else 'MUTATED'}"
    else:
        # a stdout writer producing a short file is harmless; it must still not
        # emit a truncated artefact silently
        ok = r.returncode != 0 or len(r.stdout) == 0
        why = f"exit {r.returncode}, {len(r.stdout)} bytes to stdout"
    return ok, why


def main():
    passed = 0
    print("=== ROUND-TRIP: DECLARE · ISOLATE · DIFF · REFUSE ===")
    for artefact, gen, mode, tail in ARTEFACTS:
        d = scratch_tree()                                   # ISOLATE
        try:
            held = open(os.path.join(HERE, artefact), encoding="utf-8").read()
            dec, dwhy = declares(gen, tail)
            out, err = regenerate(d, gen, artefact, mode)
            if out is None:
                print(f"  {artefact:15s} FAIL  {err}")
                continue
            h, g = NORM(held, out)
            diff = (h == g)
            ref, rwhy = refuses(d, gen, artefact, tail, mode)
            ok = dec and diff and ref
            passed += ok
            mark = "PASS" if ok else "FAIL"
            print(f"  {artefact:15s} {mark}  declare={dec} diff={diff} refuse={ref}")
            if not ok:
                if not dec:  print(f"       DECLARE: {dwhy}")
                if not diff: print(f"       DIFF: held {len(h)} vs generated {len(g)} after date normalisation")
                if not ref:  print(f"       REFUSE: {rwhy}")
        finally:
            shutil.rmtree(d, ignore_errors=True)
    print(f"\n{passed} of {len(ARTEFACTS)} round-trip")
    sys.exit(0 if passed == len(ARTEFACTS) else 1)


if __name__ == "__main__":
    main()
