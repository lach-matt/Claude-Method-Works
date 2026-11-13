#!/usr/bin/env python3
"""equiv.py -- does a cleaned program compute what its original computes?

The code appendix carries each program cleaned (no repository paths, no process words) and renamed by its
computation number. Cleaning may touch comments, names and the wording of printed lines, never the mathematics. This
harness runs the original and the cleaned copy on the same arguments and compares what they print at two levels:

  STRICT   the outputs agree line by line after normalising paths, the two program names and timing lines;
  NUMERIC  the sequence of numbers and verdict words (PASS, FAIL, OK, True, False, refuted, verified) agrees.

A pair is EQUIVALENT when the exit codes agree and NUMERIC agrees; STRICT is reported beside it. Any other outcome
is a failure, and the cleaned copy is not used.

    python3 equiv.py ORIGINAL.py CLEANED.py [-- ARGS ...]     compare one pair (timeout: --timeout SECONDS)
    python3 equiv.py --table PAIRS.tsv --out EQUIVALENCE.tsv  compare every row: key, original, cleaned, args
    python3 equiv.py --selftest                               controls: a changed number must be caught

Each program runs with its own directory as the working directory, under the interpreter running this harness.
"""
import os, re, subprocess, sys, tempfile, time, hashlib

TIMING = re.compile(r"(?i)\b(elapsed|took|time|runtime|wall|seconds?)\b.*\d|\d+(\.\d+)?\s*(s|sec|ms|min)\b\s*$")
PATH = re.compile(r"(?:[A-Za-z]:)?(?:/[\w.\-]+)+/?|\b[\w\-]+/[\w./\-]+")
NUM = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
VERDICT = re.compile(r"\b(PASS|FAIL|OK|True|False|refuted|verified|passes|fails)\b")


def run(path, args, timeout):
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, os.path.basename(path)] + args, cwd=os.path.dirname(os.path.abspath(path)),
                           capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr, time.time() - t0
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT", time.time() - t0


def normalise(text, names):
    out = []
    for ln in text.splitlines():
        if TIMING.search(ln):
            continue
        for n in names:
            ln = ln.replace(n, "<prog>")
        ln = PATH.sub("<path>", ln).rstrip()
        if ln:
            out.append(ln)
    return out


def numeric(lines):
    seq = []
    for ln in lines:
        for m in re.finditer(NUM.pattern + "|" + VERDICT.pattern, ln):
            seq.append(m.group(0))
    return seq


def compare(orig, clean, args, timeout):
    names = sorted({os.path.splitext(os.path.basename(orig))[0], os.path.splitext(os.path.basename(clean))[0]},
                   key=len, reverse=True)
    c1, o1, t1 = run(orig, args, timeout)
    c2, o2, t2 = run(clean, args, timeout)
    n1, n2 = normalise(o1, names), normalise(o2, names)
    strict = n1 == n2
    num = numeric(n1) == numeric(n2)
    ok = c1 is not None and c1 == c2 and num
    h = hashlib.md5("\n".join(numeric(n1)).encode()).hexdigest()[:12]
    return {"status": "EQUIVALENT" if ok else ("TIMEOUT" if c1 is None or c2 is None else "DIFFERENT"),
            "strict": strict, "numeric": num, "exit": (c1, c2), "secs": (round(t1, 1), round(t2, 1)),
            "numbers": len(numeric(n1)), "digest": h, "diff": first_diff(n1, n2)}


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return "line %d: %r | %r" % (i + 1, x[:60], y[:60])
    return "" if len(a) == len(b) else "length %d vs %d" % (len(a), len(b))


def selftest():
    d = tempfile.mkdtemp()
    a = os.path.join(d, "orig_prog.py")
    b = os.path.join(d, "C001.py")
    c = os.path.join(d, "C002.py")
    open(a, "w").write("import sys\nprint('docket path /x/y/z.out: residual 3.01e-4 PASS')\nprint('elapsed 2.5 s')\n")
    open(b, "w").write("print('residual 3.01e-4 PASS')\nprint('elapsed 9.9 s')\n")
    open(c, "w").write("print('residual 3.02e-4 PASS')\n")
    r1 = compare(a, b, [], 60)
    r2 = compare(a, c, [], 60)
    ok = r1["status"] == "EQUIVALENT" and r2["status"] == "DIFFERENT"
    print("same mathematics, reworded:", r1["status"], "| changed number:", r2["status"])
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    a = sys.argv[1:]
    if "--selftest" in a:
        return selftest()
    timeout = 3600
    if "--timeout" in a:
        i = a.index("--timeout"); timeout = float(a[i + 1]); del a[i:i + 2]
    if "--table" in a:
        tab = a[a.index("--table") + 1]
        out = a[a.index("--out") + 1]
        rows = [r.rstrip("\n").split("\t") for r in open(tab, encoding="utf-8") if r.strip() and not r.startswith("#")]
        bad = 0
        with open(out, "w", encoding="utf-8") as f:
            f.write("key\tstatus\tstrict\tnumeric\texit_orig\texit_clean\tsecs_orig\tsecs_clean\tnumbers\tdigest\tdiff\n")
            for r in rows:
                key, orig, clean = r[0], r[1], r[2]
                args = r[3].split() if len(r) > 3 and r[3] else []
                x = compare(orig, clean, args, timeout)
                bad += x["status"] != "EQUIVALENT"
                f.write("\t".join(map(str, [key, x["status"], x["strict"], x["numeric"], x["exit"][0], x["exit"][1],
                                            x["secs"][0], x["secs"][1], x["numbers"], x["digest"], x["diff"]])) + "\n")
                f.flush()
                print(key, x["status"], x["diff"])
        return 1 if bad else 0
    if "--" in a:
        i = a.index("--"); args = a[i + 1:]; a = a[:i]
    else:
        args = []
    x = compare(a[0], a[1], args, timeout)
    print(x)
    return 0 if x["status"] == "EQUIVALENT" else 1


if __name__ == "__main__":
    sys.exit(main())
