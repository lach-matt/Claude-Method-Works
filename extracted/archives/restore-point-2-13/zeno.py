#!/usr/bin/env python3
"""zeno.py — bounded, checkpointed, resumable execution.

The prime directive: no operation runs unbounded. Every step declares a budget,
writes its result before the next begins, and is skipped on a rerun if it has
already succeeded. Work that exceeds its budget is halved and retried, so a step
that cannot finish whole finishes in pieces rather than not at all.

Three guarantees:
  (i)   nothing is lost to a timeout — the last completed step is on disk
  (ii)  a rerun costs only what has not yet succeeded
  (iii) a step that overruns reports its overrun rather than dying silently

Usage
    from zeno import step, halve, State
    with State("audits") as st:
        n = step(st, "lattice pairs", lambda: count_pairs(L), budget=120)
        for part in halve(cells, budget=90):   # splits until each part fits
            ...
"""
import json, os, time, math, hashlib, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".zeno")


class State:
    """A named, on-disk record of which steps have completed and what they returned."""

    def __init__(self, name, reset=False):
        self.name = name
        self.path = os.path.join(ROOT, f"{name}.json")
        os.makedirs(ROOT, exist_ok=True)
        if reset and os.path.exists(self.path):
            os.remove(self.path)
        self.done = {}
        if os.path.exists(self.path):
            try:
                self.done = json.load(open(self.path))
            except Exception:
                self.done = {}
        self.t0 = time.time()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.flush()
        return False

    def flush(self):
        tmp = self.path + ".tmp"
        json.dump(self.done, open(tmp, "w"))
        os.replace(tmp, self.path)          # atomic: never a half-written state

    def elapsed(self):
        return time.time() - self.t0


def _key(name, salt=""):
    return hashlib.sha256((name + "|" + salt).encode()).hexdigest()[:16]


def step(st, name, fn, budget=120, salt="", force=False):
    """Run fn() once. Skip it on a rerun if it has already succeeded.

    budget is a soft bound in seconds: exceeding it is recorded and reported,
    never suppressed, so a step that is quietly growing is visible before it
    becomes a timeout.
    """
    k = _key(name, salt)
    if not force and k in st.done and st.done[k].get("ok") and st.done[k].get("cached", True):
        rec = st.done[k]
        print(f"  · {name}: skipped, done in {rec['secs']:.1f}s", file=sys.stderr)
        return rec["value"]
    t = time.time()
    try:
        v = fn()
        ok, err = True, None
    except Exception as e:                   # a failed step is recorded, not lost
        v, ok, err = None, False, f"{type(e).__name__}: {e}"
    secs = time.time() - t
    # a result that cannot be serialised is still a completed step; record its shape,
    # and force a recompute next run rather than silently returning None (register 349)
    try:
        json.dumps(v); keep, cached = v, True
    except TypeError:
        keep, cached = f"<{type(v).__name__}, {len(v) if hasattr(v,'__len__') else '?'} items>", False
    st.done[k] = {"name": name, "ok": ok and cached, "secs": secs, "value": keep,
                  "error": err, "cached": cached}
    st.flush()
    mark = "ok " if ok else "FAIL"
    over = "  ** OVER BUDGET **" if secs > budget else ""
    print(f"  {mark} {name}: {secs:.1f}s{over}", file=sys.stderr)
    if err:
        print(f"       {err}", file=sys.stderr)
    return v


def halve(seq, budget=90, probe=64, work=None):
    """Yield slices of seq sized so each is expected to finish inside budget.

    Times a small probe, extrapolates, and halves until the projection fits.
    This is the Zeno part: the interval is divided until it is small enough to
    complete, rather than attempted whole and lost.
    """
    seq = list(seq)
    n = len(seq)
    if n == 0:
        return
    if work is None:
        size = n
    else:
        p = min(probe, n)
        t = time.time()
        work(seq[:p])
        per = max((time.time() - t) / p, 1e-9)
        size = max(1, int(budget / per))
        while size > 1 and size * per > budget:
            size //= 2
    for i in range(0, n, size):
        yield seq[i:i + size]


def report(st):
    d = list(st.done.values())
    ok = sum(1 for r in d if r["ok"])
    slow = [r for r in d if r["ok"] and r["secs"] > 30]
    print(f"\n  zeno: {ok}/{len(d)} steps complete, {st.elapsed():.1f}s this run", file=sys.stderr)
    if slow:
        print("  slowest steps — the ones that will time out first as the book grows:", file=sys.stderr)
        for r in sorted(slow, key=lambda r: -r["secs"])[:5]:
            print(f"    {r['secs']:6.1f}s  {r['name']}", file=sys.stderr)
    bad = [r for r in d if not r["ok"]]
    if bad:
        print("  failed steps, retained for retry:", file=sys.stderr)
        for r in bad:
            print(f"    {r['name']}: {r['error']}", file=sys.stderr)
    return len(bad)
