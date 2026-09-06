#!/usr/bin/env python3
"""f811.py -- SESSION 82, ITEM 5.  R81.7: PROPAGATE F81.1.

F81.1: the restart-to-stationarity ladder is NOT a descent.  At Z=89 cfg88+7p it RISES
0.022195 mHa.  R81.7's repair is PROPAGATION: find every instrument that assumes the
ladder descends, and correct it.  NO INSTRUMENT MAY ASSUME A SIGN.

DESIGN DECISIONS, DECLARED:

  D1  **THE DETECTOR IS STRUCTURAL, NOT LEXICAL.**  A file carries an S3 ladder if it
      BOTH re-seeds a solve from its own converged orbitals (`.P0 =`) AND accumulates
      successive total energies into a list (`append(float(E...))`).  Searching for the
      WORD 'ladder' is what let three different objects share one name in the first
      place, so the word is measured SEPARATELY (X3) and never used to decide scope.

  D2  **THE FAULT WITH TEETH IS THE TERMINATION TEST**, not the label.  A break on a
      SIGNED difference either never fires or fires at pass 1 on a rising ladder.  That
      is scored on its own (X2) and separately from naming (X5).

  D3  **NO SEALED FILE IS EDITED.**  pack80 and pack81 are sealed.  Sealed sites are
      REPORTED.  The forward repair is the lint gate plus the corrected vocabulary.

  D4  **CAN-FAILS RUN FIRST AND GATE.**  Two synthetic files are written to a scratch
      dir: one committing the one-sided break, one not.  The detector must flag exactly
      the first.  A detector that cannot fail is not measuring anything.

  D5  **THE PREDICTION SHA GATES EVERY RUN.**  Mismatch halts at rc=3.

CORRECTED VOCABULARY, CARRIED FORWARD (this is the repair R81.7 asks for):
      the quantity is the RESTART OFFSET, and it is SIGNED.
      its magnitude is a RESOLUTION.
      it is NOT a drop, NOT a descent, and NOT a distance to a basin floor.

usage:  python3 f811.py canfail     # D4, must pass before anything is scored
        python3 f811.py scan        # X1..X6, full tree
        python3 f811.py lint PATH   # X7, the forward gate.  rc=1 if any site offends.
"""
import os, re, sys, json, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRED = os.path.join(HERE, 'PREDICTION-S82-ITEM5-F811-PROPAGATION.md')
PSHA = os.path.join(HERE, 'PREDICTION-S82-ITEM5-F811-PROPAGATION.sha256')
OUT = os.path.join(HERE, 'f811.jsonl')

# ---- D5 ---------------------------------------------------------------------
def gate_sha():
    want = open(PSHA).read().split()[0]
    got = subprocess.run(['sha256sum', PRED], capture_output=True, text=True).stdout.split()[0]
    if want != got:
        print(f"HALT rc=3: prediction sha mismatch\n  filed {want}\n  now   {got}")
        sys.exit(3)

# ---- D1: the structural detector --------------------------------------------
RESEED = re.compile(r'\.P0\s*=')
ACCUM = re.compile(r'\.append\(\s*float\(\s*E')

def is_s3(src):
    """S3 == re-seeds from its own orbitals AND accumulates successive total energies."""
    return bool(RESEED.search(src)) and bool(ACCUM.search(src))

# ---- D2: the termination test ------------------------------------------------
# A line that decides stationarity from a difference of successive energies.
DIFFTEST = re.compile(r'(?:done|break|if)\b[^\n]*E2?\s*-\s*E\b|(?:done|break|if)\b[^\n]*'
                      r'ladder\[0\]\s*-\s*ladder\[-1\]|(?:done|break|if)\b[^\n]*'
                      r'ladder\[-1\]\s*-\s*ladder\[0\]')
HASABS = re.compile(r'\babs\s*\(')

def onesided(src):
    """Lines that test a successive-energy difference WITHOUT taking a magnitude."""
    bad = []
    for i, ln in enumerate(src.splitlines(), 1):
        s = ln.split('#')[0]
        if DIFFTEST.search(s) and not HASABS.search(s):
            bad.append((i, ln.strip()))
    return bad

# ---- D2/X5: naming -----------------------------------------------------------
NAMING = re.compile(r'\bdrop\w*|\bDROP\b|descend\w*|DESCEND\w*|basin floor|BASIN FLOOR',
                    re.IGNORECASE)

def naming_sites(src):
    out = []
    for i, ln in enumerate(src.splitlines(), 1):
        if NAMING.search(ln):
            out.append((i, ln.strip()[:110]))
    return out

# ---- X3: the naive regex, measured but never used to decide scope ------------
NAIVE = re.compile(r'\bladder\b', re.IGNORECASE)

def pyfiles(root):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith('.')]
        for f in sorted(fn):
            if f.endswith('.py'):
                yield os.path.join(dp, f)

def read(p):
    try:
        return open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''

# ---- D4 ----------------------------------------------------------------------
CF_BAD = '''
def stationarise(h, cfg, E):
    ladder = [float(E)]
    for k in range(12):
        Cls.P0 = h.P
        h2 = Cls(Z, cfg)
        E2, _, _, _ = h2.run2()
        ladder.append(float(E2))
        h = h2
        done = float(E2) - E < 1e-10
        E = float(E2)
        if done:
            break
    return h, float(E), ladder
'''

CF_GOOD = CF_BAD.replace('done = float(E2) - E < 1e-10',
                         'done = abs(float(E2) - E) < 1e-10')

def canfail():
    gate_sha()
    print("=== D4 CAN-FAILS, RUN FIRST AND GATING =============================")
    ok = True
    d = tempfile.mkdtemp()
    pb, pg = os.path.join(d, 'bad.py'), os.path.join(d, 'good.py')
    open(pb, 'w').write(CF_BAD)
    open(pg, 'w').write(CF_GOOD)

    for tag, p, want_s3, want_bad in (('CF1 one-sided break', pb, True, 1),
                                      ('CF2 magnitude break', pg, True, 0)):
        src = read(p)
        s3, bad = is_s3(src), onesided(src)
        good = (s3 == want_s3) and (len(bad) == want_bad)
        ok &= good
        print(f"  {tag:24s} S3={s3!s:5s} one-sided={len(bad)}  "
              f"{'PASS' if good else '**FAIL**'}")

    # CF3: the detector must NOT claim an S3 ladder in a file that only says the word.
    pw = os.path.join(d, 'word.py')
    open(pw, 'w').write("LADDER = [(0.4, 100), (0.2, 600)]  # the rung ladder, sense S1\n")
    s3 = is_s3(read(pw))
    good = (s3 is False) and bool(NAIVE.search(read(pw)))
    ok &= good
    print(f"  {'CF3 word-only, sense S1':24s} S3={s3!s:5s} naive-match=True  "
          f"{'PASS' if good else '**FAIL**'}")

    print(f"\n  CAN-FAIL VERDICT: {'PASS -- both directions reachable' if ok else '**FAIL**'}")
    if not ok:
        sys.exit(4)

# ---- the scan ----------------------------------------------------------------
def scan():
    gate_sha()
    print("=== F81.1 PROPAGATION SCAN, FULL TREE ==============================")
    s3f, naive, onesided_all, naming_all, consumers = [], [], [], {}, []
    n = 0
    for p in pyfiles(ROOT):
        rel = os.path.relpath(p, ROOT)
        if rel.startswith('pack82/f811'):
            continue                      # the scanner does not scan itself
        src = read(p)
        n += 1
        if NAIVE.search(src):
            naive.append(rel)
        if is_s3(src):
            s3f.append(rel)
            for ln, txt in onesided(src):
                onesided_all.append((rel, ln, txt))
            sites = naming_sites(src)
            if sites:
                naming_all[rel] = sites
        if 'drop_mHa' in src:
            consumers.append(rel)
    ext = [f for f in consumers if f not in s3f]

    print(f"  .py files scanned            : {n}")
    print(f"  X1  S3 ladders (STRUCTURAL)  : {len(s3f)}")
    for f in s3f:
        print(f"        {f}")
    pre80 = [f for f in s3f if not re.search(r'pack8[0-2]/', f)]
    print(f"      of which pre-s80          : {len(pre80)} {pre80 if pre80 else ''}")
    print(f"  X2  one-sided break tests    : {len(onesided_all)}")
    for f, ln, txt in onesided_all:
        print(f"        {f}:{ln}  {txt}")
    print(f"  X3  naive 'ladder' matches   : {len(naive)} files "
          f"(over-match = {len(naive) - len(s3f)})")
    print(f"  X4  external drop_mHa users  : {len(ext)} {ext if ext else ''}")
    ns = sum(len(v) for v in naming_all.values())
    print(f"  X5  naming sites in S3 files : {ns}")
    for f, v in naming_all.items():
        print(f"        {f}: {len(v)} site(s)")

    json.dump(dict(files=n, s3=s3f, pre_s80=pre80,
                   onesided=[dict(f=a, line=b, src=c) for a, b, c in onesided_all],
                   naive=naive, naive_overmatch=len(naive) - len(s3f),
                   external_drop_consumers=ext,
                   naming={k: v for k, v in naming_all.items()},
                   naming_total=ns),
              open(OUT, 'w'), indent=1)
    print(f"\n  receipts -> {os.path.relpath(OUT, ROOT)}")

# ---- X7: the forward lint gate ----------------------------------------------
def lint(path):
    """rc=1 if PATH commits F81.1: a one-sided stationarity test, or a signed restart
    offset carrying a name that asserts a direction."""
    src = read(path)
    if not is_s3(src):
        print(f"LINT {path}: no S3 ladder. NOT APPLICABLE. rc=0")
        return 0
    bad, names = onesided(src), naming_sites(src)
    for ln, txt in bad:
        print(f"  **F81.1 TEETH** {path}:{ln}  one-sided stationarity test: {txt}")
    for ln, txt in names:
        print(f"  **F81.1 NAMING** {path}:{ln}  a signed offset named as a direction: {txt}")
    rc = 1 if (bad or names) else 0
    print(f"LINT {path}: teeth={len(bad)} naming={len(names)} rc={rc}")
    return rc

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == 'canfail':
        canfail()
    elif a[0] == 'scan':
        canfail(); print(); scan()
    elif a[0] == 'lint':
        sys.exit(lint(a[1]))
    else:
        print(__doc__)
