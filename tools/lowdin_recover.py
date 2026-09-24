#!/usr/bin/env python3
"""lowdin_recover.py -- recover the Löwdin project's own walk instrument from the chat export.

THE OBJECT.  The Löwdin project (100 conversations, LCP2 to LCP101 in drive/chats/, sessions
4 to 104) built the scalar-relativistic self-consistent-field chain that THE-LOWDIN-SOLUTION-2.md
§II.2 states and register 1701 witnesses: nlchain.py over hfc2.py's average-of-configuration
Hartree-Fock field with non-local exchange, the Koelling-Harmon kernel in t7c_kernel.py, three C
shooters, the convergence guard nlguard.py, the scorer nlcfg.py and the c -> inf drivers cinf.py and
cinf2.py.  The project sealed all of it in LOWDIN-HANDOFF-103.tgz (1,870 files), which was never
banked: LW1-README.md records objects 1, 2, 4-8 and 10 as PENDING BANK, and the site carried a
RECONSTRUCTION (tools/lowdin_walk.py) in its place.

THE ROUTE.  The archive's bytes are not in the export -- a file uploaded to a chat has no content
there -- but every runtime file was WRITTEN in a chat by a tool call, EDITED by tool calls, and
PRINTED back by `cat` and `sed -n` into tool results that the export carries verbatim.  This
instrument reads the export structurally and rebuilds each file two ways:

  (a) REPLAY   the file's whole edit history, in chat order: create_file bodies (the tool wrote
               them with a trailing newline: 79 of 86 sealed sha256 lines the sessions printed
               match only with it), str_replace edits, `cat > f <<EOF` heredocs, the in-place
               python patch scripts and `sed -i` commands the sessions ran, re-executed in a
               sandbox;
  (b) PRINTS   every window the sessions printed (`cat f`, `sed -n a,bp f`, `head -N f`), which
               the rebuilt text must reproduce line for line -- the witnesses.

A file is RECOVERED when its final text is a verbatim print or reproduces every print window taken
after its last edit; it is RECOVERED-REPLAYED when the replay carries it past the last print.  Where
the sessions printed a sealed sha256 manifest line for a file, the digest is checked; cinf.py's
matches.  Three files need a stated exception, each written where it is applied (SPECIAL below).
ground.py is the store's own LW1-ground.py (register 1306), which the sessions' prints of rt/ground.py
confirm.  eps0a_table.json is GENERATED here by the record's own generator over its ring integral and
checked against the six rows the session printed.

WHAT THIS IS NOT.  Not the sealed archive: its 1,870 files include run receipts, caches and
session documents this does not attempt; the runtime closure the chain needs is 27 files.  Not a
reconstruction: nothing here is rebuilt from a statement of behaviour.  And not a repair: where the
record's own instrument disagrees with the record's sealed rows (F61.1: the rows at Z <= 56 were
walked before the guard), the disagreement is reported, not smoothed.

Usage:
    python3 tools/lowdin_recover.py                 # regenerate lowdin/rt, LEDGER.tsv, WITNESS.tsv
    python3 tools/lowdin_recover.py --selftest      # the fixtures below, on the export alone
    python3 tools/lowdin_recover.py --verify        # regenerate in memory and compare with disk
    python3 tools/lowdin_recover.py --check-chain lowdin/chain/LAMBDA-CHAIN.jsonl
                                                    # a run against every sealed step the sessions printed
    python3 tools/lowdin_recover.py --runtime DIR   # a runnable copy: compile the shooters, generate the table

Running the recovered instrument (the record's own commands, from its README-HANDOFF files):
    cd DIR && SIC_NOCLAMP=1 SUBCELL=1 python3 nlchain.py 2 120       # Lambda_chain, appends nlchain.jsonl
    python3 pack59/cinf2.py canfail && python3 pack59/cinf2.py walk 2 108 OUT   # restart rows at c = 1e6
The sessions ran numpy 2.4.4 and Python 3.12; ring_zeta.py needs numpy's `trapezoid`.
"""

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATS = os.path.join(REPO, "drive", "chats")
OUT = os.path.join(REPO, "lowdin")
STORE_GROUND = os.path.join(REPO, "method", "members", "LW1-ground.py")

# the runtime closure of nlchain.py, measured by importing it (every local module it reaches)
RUNTIME = [
    "nlchain.py", "hfc2.py", "t7c_hfsr.py", "t7b_hf.py", "t7c_kernel.py", "t5_scf.py", "hfs.py",
    "hfs_pol.py", "hfs_sic.py", "step2_run.py", "rad.py", "tfd.py", "eigen_fix.py", "derive_P.py",
    "ground.py", "nlguard.py", "t7c_cuaudit.py", "cellcut.py", "lam1_zeta.py", "ring_zeta.py", "eps0a_table.py",
    "shoot.c", "shoot_sr.c", "shoot_x.c",
    # the drivers and the scorer the record ran over the chain
    "nlcfg.py", "cinf.py", "cinf2.py", "runsealed.py",
]
STD = {"numpy", "math", "sys", "os", "json", "time", "ctypes", "warnings", "io", "contextlib",
       "collections", "re", "hashlib", "subprocess", "itertools", "functools", "scipy", "random",
       "glob", "shutil", "argparse", "datetime", "importlib", "csv"}

# SPECIAL: the three stated exceptions, each with its ground
SKIP_EVENTS = {
    # a create_file the session itself found not applied: its next call, `wc -l rt/t7b_hf.py`,
    # printed the 169-line file with the earlier header, and every later print agrees with the
    # earlier body plus its edits (LCP16 uses 59-60)
    "LCP16#59": "t7b_hf.py: create_file not applied in the session (wc -l at the next call shows the earlier file)",
}
# nlcfg.py: the session's own patch that rewrote the GATE dict from computed scores (LCP47#145) ran
# over the chain and cannot be replayed without it; the GATE block is taken from the print the next
# session made of it (LCP48, lines 186-200) and the last str_replace (LCP48#45) then applies to it.
# t7c_cuaudit.py: never written by a tool call (derived by `sed` from t7c_corrz.py, itself patched
# from t7c_corr.py); its text is the LCP23 print of all 135 lines, of which four exceed that print's
# 170-column cut, with lines 1-52 taken from the LCP24 print that was not cut; line 125's cut falls
# inside a trailing comment and is recorded as such.

PRINT_RX = re.compile(r"(?:^|&&|;|\|\|)\s*(cat|sed -n ['\"]?(\d+),(\d+)p['\"]?|head -(\d+))\s+([\w./-]+)(?:\s*2>/dev/null)?(\s*\|\s*head -(\d+))?(\s*\|\s*cut -c1-(\d+))?(\s*\|\s*head -(\d+))?(\s*\|)?")
MANIFEST_RX = re.compile(r"([0-9a-f]{64})  ([A-Za-z0-9_./-]*(?:rt/|pack\d+/)[A-Za-z0-9_./-]+)")
NAME_RX = re.compile(r"(?<![\w./-])([\w-]+\.(?:py|c|sh))(?![\w])")


# ------------------------------------------------------------------ the export

def chats():
    """[(title, path)] for the Löwdin project's conversations, LCP2..LCP101 in order."""
    idx = os.path.join(CHATS, "INDEX.tsv")
    out = []
    with open(idx, encoding="utf-8") as fh:
        next(fh)
        for ln in fh:
            p = ln.rstrip("\n").split("\t")
            if re.match(r"LCP\d+$", p[2]):
                out.append((p[2], os.path.join(CHATS, p[0])))
    return sorted(out, key=lambda x: int(x[0][3:]))


def walk_export(files):
    """One pass over the export: the ordered mutation events, the print windows, the sealed
    manifest lines.  files: the basenames of interest."""
    events, prints, manifest = [], [], {}
    fileset = set(files)
    for title, path in chats():
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        msgs = d["chat_messages"]
        uses, order, k = {}, [], 0
        for m in msgs:
            for c in m.get("content", []):
                if c.get("type") == "tool_use":
                    k += 1
                    uses[c["id"]] = (k, c)
                    order.append(c["id"])
        results = {}
        for m in msgs:
            for c in m.get("content", []):
                if c.get("type") == "tool_result":
                    txt = "".join(cc.get("text", "") for cc in (c.get("content") or []) if isinstance(cc, dict))
                    try:
                        j = json.loads(txt)
                        txt = j.get("stdout", "") + ("\n" + j["stderr"] if j.get("stderr") else "")
                    except Exception:
                        pass
                    results[c.get("tool_use_id")] = txt
        for uid in order:
            k, c = uses[uid]
            i = c.get("input", {})
            nm = c["name"]
            out = results.get(uid, "")
            for h, p in MANIFEST_RX.findall(out):
                manifest.setdefault(os.path.basename(p), {})[p] = h
            if nm in ("create_file", "str_replace"):
                b = os.path.basename(i.get("path", ""))
                if b in fileset:
                    events.append({"chat": title, "seq": k, "kind": nm, "file": b, "input": i})
            elif nm == "bash_tool":
                cmd = i.get("command", "")
                touched = sorted({t for t in NAME_RX.findall(cmd) if t in fileset})
                if touched and re.search(r"cat\s*>\s*|\.write\(|open\([^)]*['\"]w['\"]|sed\s+-i|python3\s+-\s*<<|sed\s+'[^']*'\s+[\w./-]+\s*>", cmd):
                    events.append({"chat": title, "seq": k, "kind": "bash", "touched": touched, "command": cmd})
                for mm in PRINT_RX.finditer(cmd):
                    f = os.path.basename(mm.group(5))
                    if f not in fileset:
                        continue
                    kind = mm.group(1)
                    if kind.startswith("sed"):
                        a, b = int(mm.group(2)), int(mm.group(3))
                    elif kind.startswith("head"):
                        a, b = 1, int(mm.group(4))
                    else:
                        a, b = 1, (int(mm.group(7)) if mm.group(7) else None)
                    cut = int(mm.group(9)) if mm.group(9) else None
                    if mm.group(12):          # piped on into a filter (grep, awk, ...): not a print of the file
                        continue
                    hd = mm.group(7) or mm.group(11)
                    if hd and not (kind == "cat" and mm.group(7)):
                        b = min(b if b else 10 ** 9, a + int(hd) - 1)
                    prints.append({"chat": title, "seq": k, "file": f, "a": a, "b": b, "cut": cut, "stdout": out, "command": cmd})
    return events, prints, manifest


# ------------------------------------------------------------------ the replay

def replay(events, files, log, seed=None):
    """Rebuild each file in a sandbox by re-executing its edit history.  Returns {file: text}.
    seed: {file: (text, (chat_no, seq))} -- a text known at that point; the file's earlier events are skipped."""
    sb = tempfile.mkdtemp(prefix="lowdin-replay-")
    need = set(files)
    seed = seed or {}
    for f, (t, _at) in seed.items():
        with open(os.path.join(sb, f), "w") as fh:
            fh.write(t)
    if os.path.exists(STORE_GROUND):
        shutil.copy(STORE_GROUND, os.path.join(sb, "ground.py"))
    created, changed = {}, {}

    def snapshot():
        return {f: hashlib.sha256(open(os.path.join(sb, f), "rb").read()).hexdigest() for f in need if os.path.exists(os.path.join(sb, f))}
    before = snapshot()
    for e in events:
        tag = "%s#%d" % (e["chat"], e["seq"])
        at = (int(e["chat"][3:]), e["seq"])
        if any(f in seed and at <= seed[f][1] for f in ([e["file"]] if "file" in e else e["touched"])):
            continue
        if tag in SKIP_EVENTS:
            log.append((tag, "SKIPPED", e.get("file", ""), SKIP_EVENTS[tag]))
            continue
        if e["kind"] == "create_file":
            body = e["input"].get("file_text", "")
            if not body.endswith("\n"):
                body += "\n"
            with open(os.path.join(sb, e["file"]), "w") as fh:
                fh.write(body)
            created.setdefault(e["file"], tag)
            log.append((tag, "create", e["file"], str(len(body))))
        elif e["kind"] == "str_replace":
            p = os.path.join(sb, e["file"])
            if not os.path.exists(p):
                continue
            s = open(p).read()
            old, new = e["input"]["old_str"], e["input"]["new_str"]
            n = s.count(old)
            if n == 1:
                open(p, "w").write(s.replace(old, new))
                log.append((tag, "str_replace", e["file"], "ok"))
            else:
                log.append((tag, "str_replace", e["file"], "NOT APPLIED (count=%d)" % n))
        else:
            cmd = e["command"]
            touched = [f for f in e["touched"] if f in need]
            for m in re.finditer(r"cat\s*>\s*([\w./-]+)\s*<<\s*'?(\w+)'?\n(.*?)\n\2(?:\n|$)", cmd, flags=re.S):
                b = os.path.basename(m.group(1))
                if b in need:
                    open(os.path.join(sb, b), "w").write(m.group(3) + "\n")
                    created.setdefault(b, tag)
                    log.append((tag, "heredoc", b, str(len(m.group(3)))))
            for m in re.finditer(r"python3\s+-\s*<<\s*'?(\w+)'?\n(.*?)\n\1(?:\n|$)", cmd, flags=re.S):
                script = m.group(2)
                if not any(re.search(r"(?<![\w./-])" + re.escape(b) + r"(?![\w])", script) for b in touched):
                    continue
                if not re.search(r"\.write\(|open\([^)]*['\"]w['\"]", script):
                    continue
                script2 = re.sub(r"/home/claude/[\w./-]*/(?:rt|pack\d+|code|fixed|work\d*)/", sb + "/", script)
                script2 = re.sub(r"/home/claude/[\w./-]*/", sb + "/", script2)
                r = subprocess.run([sys.executable, "-"], input=script2, capture_output=True, text=True, cwd=sb, timeout=120)
                log.append((tag, "pyscript", ",".join(touched), "rc=%d %s" % (r.returncode, (r.stderr.strip().splitlines() or [""])[-1][:80])))
            for m in re.finditer(r"sed\s+-i\s+((?:'[^']*'|\"[^\"]*\"|\S+))\s+([\w./-]+)", cmd):
                b = os.path.basename(m.group(2))
                if b in need and os.path.exists(os.path.join(sb, b)):
                    r = subprocess.run("sed -i %s %s" % (m.group(1), b), shell=True, capture_output=True, text=True, cwd=sb)
                    log.append((tag, "sed-i", b, "rc=%d" % r.returncode))
            for m in re.finditer(r"sed\s+('(?:[^'\\]|\\.)*')\s+([\w./-]+)\s*>\s*([\w./-]+)", cmd):
                a, b = os.path.basename(m.group(2)), os.path.basename(m.group(3))
                if a in need and b in need and os.path.exists(os.path.join(sb, a)):
                    r = subprocess.run("sed %s %s > %s" % (m.group(1), a, b), shell=True, capture_output=True, text=True, cwd=sb)
                    created.setdefault(b, tag)
                    log.append((tag, "sed>", a + "->" + b, "rc=%d" % r.returncode))
        after = snapshot()
        for f in need:
            if after.get(f) != before.get(f):
                changed[f] = tag
        before = after
    texts = {}
    for f in files:
        p = os.path.join(sb, f)
        if os.path.exists(p):
            texts[f] = open(p).read()
    shutil.rmtree(sb, ignore_errors=True)
    return texts, created, changed


# ------------------------------------------------------------------ the prints

def window_text(pr):
    """The lines a print window shows, or None when the block cannot be isolated."""
    out = pr["stdout"]
    f = pr["file"]
    marker = "=== %s ===\n" % f
    if marker in out:
        block = out.split(marker, 1)[1]
        block = re.split(r"\n=== [^\n]* ===\n", block, 1)[0]
        return block.split("\n")
    lone = re.fullmatch(r"\s*(?:cd [\w./-]+ && )?cat\s+[\w./-]*%s\s*(?:\|\s*head -\d+)?\s*" % re.escape(f), pr["command"])
    if lone:
        return out.rstrip("\n").split("\n")
    return None


def witnessed(text, pr):
    """(matched, total): how many lines of the window the text reproduces, and whether the
    window is found contiguously in the print."""
    lines = text.split("\n")
    a, b = pr["a"], pr["b"] or len(lines)
    win = lines[a - 1:b]
    if pr["cut"]:
        win = [l[:pr["cut"]] for l in win]
    contiguous = "\n".join(win) in pr["stdout"]
    have = set(pr["stdout"].split("\n"))
    return contiguous, sum(1 for l in win if l in have), len(win)


def full_prints(prints, f, text):
    """The chats in which the whole file was printed verbatim and equals text."""
    out = []
    n = text.rstrip("\n").count("\n") + 1
    for pr in prints:
        if pr["file"] != f or pr["a"] != 1 or pr["cut"] or (pr["b"] is not None and pr["b"] < n):
            continue
        if text.rstrip("\n") in pr["stdout"]:
            out.append("%s#%d" % (pr["chat"], pr["seq"]))
    return out


# ------------------------------------------------------------------ assembly

def assemble(log=print):
    files = RUNTIME
    events, prints, manifest = walk_export(files)
    rlog = []
    texts, created, last_edit = replay(events, files, rlog)   # the last event that changed each file's bytes
    final, ledger, witness = {}, [], []
    by_file = {}
    for pr in prints:
        by_file.setdefault(pr["file"], []).append(pr)

    def latest_full_print(f):
        cands = []
        for pr in by_file.get(f, []):
            if pr["a"] != 1 or pr["cut"]:
                continue
            wt = window_text(pr)
            if wt is None:
                continue
            n = pr["b"]
            if n is not None and n < len(wt):
                continue
            cands.append((int(pr["chat"][3:]), pr["seq"], "\n".join(wt).rstrip("\n") + "\n", pr))
        return max(cands, key=lambda x: (x[0], x[1])) if cands else None

    for f in files:
        method, note, text = None, "", None
        if f == "ground.py":
            text = open(STORE_GROUND).read()
            method = "STORE-MEMBER"
            note = "method/members/LW1-ground.py, register 1306; the sessions' prints of rt/ground.py agree"
        elif f == "t7c_cuaudit.py":
            p23 = [p for p in by_file.get(f, []) if p["chat"] == "LCP23" and p["a"] == 1 and p["b"] == 134]
            p24 = [p for p in by_file.get(f, []) if p["chat"] == "LCP24" and p["a"] == 1 and p["b"] == 52]
            if p23 and p24:
                a = p23[0]["stdout"].split("\n")
                b = p24[0]["stdout"].rstrip("\n").split("\n")
                lines = b[:52] + a[52:]
                while lines and lines[-1] == "":
                    lines.pop()
                comp = "\n".join(lines) + "\n"
                cut = [i + 1 for i, l in enumerate(a) if len(l) >= 170]
                at = (24, 10 ** 6)
                later = [e for e in events if (int(e["chat"][3:]), e["seq"]) > at and ("t7c_cuaudit.py" in (e.get("touched") or [e.get("file")]))]
                rl = []
                t2, _c, _ch = replay(later, ["t7c_cuaudit.py", "t7c_corrz.py"], rl, seed={"t7c_cuaudit.py": (comp, at), "t7c_corrz.py": (comp, at)})
                text = t2.get("t7c_cuaudit.py", comp)
                method = "PRINT-COMPOSITE+REPLAY"
                note = ("LCP23 print of 135 lines at a 170-column cut (lines %s cut) with lines 1-52 from the uncut LCP24 print, then the "
                        "session-28 patch (LCP26#31, the cell-cut branch) replayed over it; line 125's cut falls inside a trailing comment; "
                        "windows printed at sessions 30 and 71 show a further edit (the older v_gb removed) that no tool call in the export "
                        "records -- the module serves hfc2's correlation potential, which the chain never calls (CORR=False)" % cut)
        elif f == "nlcfg.py":
            rep = texts.get(f)
            p48 = [p for p in by_file.get(f, []) if p["chat"] == "LCP48" and p["a"] == 186]
            ev = [e for e in events if e["chat"] == "LCP48" and e["seq"] == 45]
            if rep and p48 and ev:
                gate = re.search(r"GATE = dict\(.*?str_mismatch=\[\]\)", p48[0]["stdout"], flags=re.S)
                cur = re.search(r"GATE = dict\(.*?str_mismatch=\[\]\)", rep, flags=re.S)
                if gate and cur:
                    t = rep.replace(cur.group(0), gate.group(0))
                    old, new = ev[0]["input"]["old_str"], ev[0]["input"]["new_str"]
                    if t.count(old) == 1:
                        text = t.replace(old, new)
                        method = "REPLAY+PRINT-REPAIR"
                        note = "the GATE block rewritten by LCP47#145 over the chain is taken from the LCP48 print (lines 186-200); LCP48#45 then applies"
                        last_edit[f] = "LCP48#45"
        if text is None:
            lp = latest_full_print(f)
            rep = texts.get(f)
            if lp and rep and lp[2] == rep:
                text, method, note = rep, "REPLAY=PRINT", "the replayed text equals the latest full print (%s#%d)" % (lp[3]["chat"], lp[3]["seq"])
            elif lp and (rep is None or int(lp[0]) >= int((last_edit.get(f, "LCP0#0")).split("#")[0][3:])):
                text, method = lp[2], "PRINT"
                note = "the latest full print (%s#%d)%s" % (lp[3]["chat"], lp[3]["seq"], "" if rep is None else "; the replay differs: %d vs %d bytes" % (len(rep), len(lp[2])))
            elif rep is not None:
                text, method, note = rep, "REPLAY", "no full print after the last edit; the replayed history stands on its windows"
        if text is None:
            ledger.append({"file": f, "status": "NOT RECOVERED", "method": "", "note": "no creation and no full print in the export"})
            continue
        final[f] = text
        # witnesses: every window printed at or after the last edit (or all, for print-built files)
        wins = by_file.get(f, [])
        le = last_edit.get(f, "LCP0#0")
        le_chat, le_seq = int(le.split("#")[0][3:]), int(le.split("#")[1])
        after = [p for p in wins if (int(p["chat"][3:]), p["seq"]) >= (le_chat, le_seq)]
        matched = total = 0
        for pr in after:
            contiguous, m, n = witnessed(text, pr)
            witness.append({"file": f, "chat": pr["chat"], "seq": pr["seq"], "lines": "%d-%s" % (pr["a"], pr["b"] or "end"), "cut": pr["cut"] or "",
                            "contiguous": "yes" if contiguous else "no", "lines_found": "%d/%d" % (m, n)})
            matched += (1 if contiguous or m == n else 0)
            total += 1
        fulls = full_prints(prints, f, text)
        sha = hashlib.sha256(text.encode()).hexdigest()
        sealed = manifest.get(f, {})
        sealed_verdict = ""
        if sealed:
            sealed_verdict = "; ".join("%s %s" % (p, "MATCH" if h == sha else "differs") for p, h in sorted(sealed.items()))
        status = "RECOVERED" if (fulls or (total and matched == total)) else ("RECOVERED-REPLAYED" if method.startswith("REPLAY") else "RECOVERED-PARTIAL")
        if f == "t7c_cuaudit.py":
            status = "RECOVERED-PARTIAL"
        if f == "ground.py":
            status = "STORE"
        ledger.append({"file": f, "bytes": len(text.encode()), "sha256": sha, "method": method, "created": created.get(f, ""), "last_edit": last_edit.get(f, ""),
                       "windows_after_last_edit": "%d/%d" % (matched, total), "full_prints_equal": ",".join(fulls), "sealed_sha256": sealed_verdict,
                       "status": status, "note": note})
    return final, ledger, witness, rlog, manifest


LEDGER_COLS = ["file", "bytes", "sha256", "method", "created", "last_edit", "windows_after_last_edit", "full_prints_equal", "sealed_sha256", "status", "note"]
WITNESS_COLS = ["file", "chat", "seq", "lines", "cut", "contiguous", "lines_found"]


def write_tree(final, ledger, witness, out=OUT):
    rt = os.path.join(out, "rt")
    os.makedirs(rt, exist_ok=True)
    for f, t in final.items():
        with open(os.path.join(rt, f), "w") as fh:
            fh.write(t)
    with open(os.path.join(out, "LEDGER.tsv"), "w") as fh:
        fh.write("\t".join(LEDGER_COLS) + "\n")
        for r in ledger:
            fh.write("\t".join(str(r.get(c, "")) for c in LEDGER_COLS) + "\n")
    with open(os.path.join(out, "WITNESS.tsv"), "w") as fh:
        fh.write("\t".join(WITNESS_COLS) + "\n")
        for r in witness:
            fh.write("\t".join(str(r.get(c, "")) for c in WITNESS_COLS) + "\n")


def make_runtime(final, dst):
    """A runnable copy: the files, the three shooters compiled, the table generated by the
    record's generator, and the drivers where the record kept them (pack52/, pack53/, pack59/)."""
    rt = os.path.join(dst, "rt")
    os.makedirs(rt, exist_ok=True)
    for f, t in final.items():
        with open(os.path.join(rt, f), "w") as fh:
            fh.write(t)
    for pk, f in (("pack52", "cinf.py"), ("pack53", "runsealed.py"), ("pack59", "cinf2.py")):
        os.makedirs(os.path.join(dst, pk), exist_ok=True)
        shutil.copy(os.path.join(rt, f), os.path.join(dst, pk, f))
    for k in ("shoot", "shoot_sr", "shoot_x"):
        r = subprocess.run(["gcc", "-O2", "-shared", "-fPIC", "-o", "lib%s.so" % k, "%s.c" % k], cwd=rt, capture_output=True, text=True)
        if r.returncode:
            raise SystemExit("kernel compile failed: %s\n%s" % (k, r.stderr))
    r = subprocess.run([sys.executable, "eps0a_table.py"], cwd=rt, capture_output=True, text=True, timeout=900)
    if r.returncode:
        raise SystemExit("eps0a_table.py failed (numpy with `trapezoid` is needed):\n" + r.stderr[-800:])
    return rt, r.stdout


# ------------------------------------------------------------------ the chain check

ARROW_RX = re.compile(r"->\s*Z=(\d+)\s+entrant\s+(\S+)\s+D\s+(\S+)\s+margin\s+(\S+)\s+rec\s+(\S+)\s+ok\s+(\S+)")


def sealed_steps():
    """Every chain step the sessions printed (`-> Z=.. entrant .. D .. margin .. rec .. ok ..`)
    and every full row printed as JSON, by Z, with the chat that printed it."""
    steps, rows = {}, {}
    for title, path in chats():
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        for m in d["chat_messages"]:
            for c in m.get("content", []):
                if c.get("type") != "tool_result":
                    continue
                txt = "".join(cc.get("text", "") for cc in (c.get("content") or []) if isinstance(cc, dict))
                try:
                    j = json.loads(txt)
                    txt = j.get("stdout", "") + "\n" + j.get("stderr", "")
                except Exception:
                    pass
                for mm in ARROW_RX.finditer(txt):
                    steps.setdefault(int(mm.group(1)), []).append((title,) + mm.groups()[1:])
                if '"ent_nl"' in txt:
                    for o in _json_objects(txt):
                        if isinstance(o, dict) and "Z" in o and "ent_nl" in o and o.get("mode") in ("chain", "guarded s47", None) and "clight" not in o:
                            rows.setdefault(o["Z"], []).append((title, o))
    return steps, rows


def _json_objects(text):
    i = 0
    while True:
        i = text.find("{", i)
        if i < 0:
            return
        depth, j = 0, i
        while j < len(text):
            ch = text[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        chunk = text[i:j + 1]
        if '"ent_nl"' in chunk:
            try:
                yield json.loads(chunk)
            except Exception:
                pass
        i = j + 1 if j > i else i + 1


CHECK_COLS = ["Z", "entrant", "verdict", "detail"]


def check_chain(path, log=print, tsv=None):
    """Compare a run of nlchain.py against every sealed step and row the sessions printed.
    The sealed rows at Z <= 56 predate the guard (F61.1), so a margin that differs there while
    the entrant and its depth agree is the record's own finding, not a failure of the run."""
    steps, rows = sealed_steps()
    run = {}
    with open(path) as fh:
        for ln in fh:
            r = json.loads(ln)
            run[r["Z"]] = r
    verdicts = {"exact+order": 0, "exact": 0, "entrant+depth (margin differs: F61.1)": 0, "entrant only": 0, "DIFFERS": 0, "unwitnessed": 0}
    out = []
    for Z in sorted(run):
        r = run[Z]
        cands = [s for s in steps.get(Z, [])]
        full = [o for _t, o in rows.get(Z, [])]
        if not cands and not full:
            verdicts["unwitnessed"] += 1
            out.append((Z, r["ent"], "unwitnessed", ""))
            continue
        best = None
        for t, e, D, mg, rec, ok in cands:
            if e == r["ent"] and abs(float(D) - r["D_ent"]) < 1e-9 and abs(float(mg) - r["margin"]) < 1e-9:
                best = ("exact", t)
                break
        # a row the sessions printed whole (chain or guarded mode) is compared in full: the order list
        # of every channel's depth to five decimals, and the refused set
        for o in full:
            if o.get("mode") not in ("chain", "guarded s47"):
                continue
            od = o.get("D_ent", o["order"][0][1] if o.get("order") else None)
            if od is None:
                continue
            if o["ent"] == r["ent"] and abs(od - r["D_ent"]) < 1e-9 and abs(o["margin"] - r["margin"]) < 1e-9 \
               and [[c, round(v, 5)] for c, v in o["order"]] == [[c, round(v, 5)] for c, v in r["order"]] \
               and sorted(o.get("fail", {})) == sorted(r.get("fail", {})):
                best = ("exact+order", "the full printed row: every channel's depth and the refused set")
                break
        if best is None:
            for o in full:
                od = o.get("D_ent", o["order"][0][1] if o.get("order") else None)
                if od is not None and o["ent"] == r["ent"] and abs(od - r["D_ent"]) < 1e-9 and abs(o["margin"] - r["margin"]) < 1e-9:
                    best = ("exact", "row")
                    break
        if best is None:
            for t, e, D, mg, rec, ok in cands:
                if e == r["ent"] and abs(float(D) - r["D_ent"]) < 1e-9:
                    best = ("entrant+depth (margin differs: F61.1)" if Z <= 56 else "DIFFERS", "%s: sealed margin %s, run %s" % (t, mg, r["margin"]))
                    break
        if best is None:
            ents = {e for _t, e, *_ in cands} | {o["ent"] for o in full}
            best = ("entrant only" if r["ent"] in ents else "DIFFERS", "sealed %s" % sorted(ents))
        verdicts[best[0]] += 1
        out.append((Z, r["ent"], best[0], best[1]))
    for Z, e, v, d in out:
        log("  Z=%3d %-3s %-38s %s" % (Z, e, v, d))
    log("  rows %d: %s" % (len(run), ", ".join("%s %d" % kv for kv in verdicts.items())))
    if tsv:
        with open(tsv, "w") as fh:
            fh.write("\t".join(CHECK_COLS) + "\n")
            for Z, e, v, d in out:
                fh.write("%d\t%s\t%s\t%s\n" % (Z, e, v, d))
    return verdicts, out


# ------------------------------------------------------------------ collecting the runs

RUN_SPECS = {
    # key: (file, instrument, command, what, kind)
    "chain": ("LAMBDA-CHAIN.jsonl", "nlchain.py", "SIC_NOCLAMP=1 SUBCELL=1 python3 nlchain.py 2 120",
              "the chain on its own configuration at every step, Z = 2 to 120: the record's Lambda_chain re-derived by the record's instrument", "record"),
    "restart137": ("LAMBDA-CINF-SEALED.jsonl", "cinf.py via runsealed.py", "python3 pack53/runsealed.py pack52/cinf.py walk 2 108 OUT",
                   "the table the paper compared against, re-derived as sealed: restart rows from the observed configuration; the record's fault F59.3 "
                   "established that this driver's c never reached the field, so it runs at c = 137.035999 and its clight label is false", "record"),
    "restart_cinf": ("LAMBDA-CINF2.jsonl", "cinf2.py", "python3 pack59/cinf2.py canfail && python3 pack59/cinf2.py walk 2 108 OUT",
                     "restart rows at a genuine c = 1e6 by the record's F59.3 remedy; the record ran 13 of these rows (the exposed set), the other 94 are run here", "extension"),
    "chain_cinf": ("LAMBDA-CINF-CHAIN.jsonl", "nlchain.py after cinf2.patch", "python3 cinf_chain.py 2 120 (cinf2.patch(1e6), then nlchain.main)",
                   "the chain at a genuine c = 1e6: the identical walk with the constant removed, which the paper describes and the record never ran chained", "extension"),
}


def collect(pairs, out=OUT):
    """Copy the runs' output tables into lowdin/chain with RUNS.tsv and CHECK.tsv."""
    import platform
    try:
        import numpy
        npv = numpy.__version__
    except Exception:
        npv = "absent"
    cd = os.path.join(out, "chain")
    os.makedirs(cd, exist_ok=True)
    rows = []
    for key, src in pairs:
        fn, inst, cmd, what, kind = RUN_SPECS[key]
        blob = open(src, "rb").read()
        with open(os.path.join(cd, fn), "wb") as fh:
            fh.write(blob)
        n = sum(1 for ln in blob.decode().splitlines() if ln.strip())
        zs = [json.loads(ln)["Z"] for ln in blob.decode().splitlines() if ln.strip()]
        rows.append({"key": key, "file": fn, "instrument": inst, "command": cmd, "rows": n, "Z_range": "%d-%d" % (min(zs), max(zs)) if zs else "",
                     "md5": hashlib.md5(blob).hexdigest(), "python": platform.python_version(), "numpy": npv, "kind": kind, "what": what,
                     "status": "RECOVERED" if kind == "record" else "RECOVERED (a run the record did not make)"})
    cols = ["key", "file", "instrument", "command", "rows", "Z_range", "md5", "python", "numpy", "kind", "status", "what"]
    with open(os.path.join(cd, "RUNS.tsv"), "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in cols) + "\n")
    ch = os.path.join(cd, "LAMBDA-CHAIN.jsonl")
    if os.path.exists(ch):
        check_chain(ch, log=lambda *a: None, tsv=os.path.join(cd, "CHECK.tsv"))
    return rows


SCORE_RX = re.compile(r"CONFIG score (\d+)/(\d+)\s+STEP \(`ok`\) score (\d+)/(\d+)")
FAIL_RX = re.compile(r"^\s*(config|step)\s+failures\s*:\s*\[([^\]]*)\]", re.M)


def score_runs(out=OUT, keys=("chain", "chain_cinf")):
    """Run the record's own scorer, nlcfg.py, over each chain-mode table in lowdin/chain and
    write SCORE.tsv: nlcfg reads nlchain.jsonl beside itself, so each table is copied under that
    name into a runtime built from lowdin/rt (shooters compiled, the table generated), and `show`
    is parsed.
    The scorer's GATE dict is the last session's pin on the c = 137.035999 chain (73/107, 96/107)
    and is not consulted; `show` prints both scores and both failure lists for any table."""
    import subprocess, tempfile
    cd = os.path.join(out, "chain")
    rt = os.path.join(out, "rt")
    rows = []
    for key in keys:
        fn = RUN_SPECS[key][0]
        src = os.path.join(cd, fn)
        if not os.path.exists(src):
            continue
        with tempfile.TemporaryDirectory(prefix="lowdin-score-") as td:
            # nlcfg imports nlchain, which loads the compiled shooters and the generated table, so
            # the sandbox is a full runtime built from the seated tree (the same route as --runtime)
            final = {f: open(os.path.join(rt, f)).read() for f in sorted(os.listdir(rt)) if f.endswith((".py", ".c"))}
            sandbox, _ = make_runtime(final, td)
            shutil.copy(src, os.path.join(sandbox, "nlchain.jsonl"))
            p = subprocess.run([sys.executable, "nlcfg.py", "show"], cwd=sandbox, capture_output=True, text=True, timeout=900)
        m = SCORE_RX.search(p.stdout)
        if p.returncode != 0 or not m:
            raise RuntimeError("nlcfg.py show failed on %s: %s" % (fn, (p.stderr or p.stdout)[-400:]))
        fails = {k: [int(x) for x in v.split(",") if x.strip()] for k, v in FAIL_RX.findall(p.stdout)}
        rows.append({"key": key, "file": fn, "scorer": "nlcfg.py show", "config_score": "%s/%s" % (m.group(1), m.group(2)),
                     "step_score": "%s/%s" % (m.group(3), m.group(4)),
                     "config_failures": " ".join(map(str, fails.get("config", []))), "step_failures": " ".join(map(str, fails.get("step", []))),
                     "status": "RECOVERED" if RUN_SPECS[key][4] == "record" else "RECOVERED (a run the record did not make)",
                     "what": "the record's scorer over this table: the chain's configuration against the observed one at each Z <= 108 (CONFIG), "
                             "and its entrant against the observed gain (STEP); the scorer's own GATE pins the c = 137.035999 chain and is not consulted"})
    cols = ["key", "file", "scorer", "config_score", "step_score", "config_failures", "step_failures", "status", "what"]
    with open(os.path.join(cd, "SCORE.tsv"), "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in cols) + "\n")
    return rows


# ------------------------------------------------------------------ selftest

def selftest():
    fail = 0
    print("lowdin_recover.py --selftest   fixtures: the export's own prints and sealed digests")
    print()

    def chk(name, got, want):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print("  [%s] %-78s %s" % ("ok" if ok else "FAIL", name, "" if ok else "got %r want %r" % (got, want)))

    final, ledger, witness, rlog, manifest = assemble(log=lambda *a: None)
    L = {r["file"]: r for r in ledger}
    chk("the runtime closure is recovered in full", sorted(f for f in RUNTIME if f in final), sorted(RUNTIME))
    chk("cinf.py hashes to the sealed manifest line the session printed (pack52/cinf.py)", L["cinf.py"]["sealed_sha256"], "pack52/cinf.py MATCH")
    chk("nlchain.py: three sessions printed it whole and all three equal the recovered text", len(L["nlchain.py"]["full_prints_equal"].split(",")) >= 3, True)
    chk("t7c_kernel.py and hfc2.py: printed whole in more than one session, all equal", (len(L["t7c_kernel.py"]["full_prints_equal"].split(",")) >= 2, len(L["hfc2.py"]["full_prints_equal"].split(",")) >= 3), (True, True))
    chk("every window printed after a file's last edit is reproduced, t7c_cuaudit.py the stated exception", [r["file"] for r in ledger if r.get("windows_after_last_edit", "0/0") != "0/0" and r["windows_after_last_edit"].split("/")[0] != r["windows_after_last_edit"].split("/")[1]], ["t7c_cuaudit.py"])
    chk("statuses: no file NOT RECOVERED; t7c_cuaudit.py the one RECOVERED-PARTIAL", ([r["file"] for r in ledger if r["status"] == "NOT RECOVERED"], [r["file"] for r in ledger if r["status"] == "RECOVERED-PARTIAL"]), ([], ["t7c_cuaudit.py"]))
    chk("t7c_cuaudit.py carries the session-28 cell-cut branch and the S30/S71 windows that the composite can reproduce", ("from cellcut import SUBCELL as _SUBCELL" in final["t7c_cuaudit.py"], L["t7c_cuaudit.py"]["windows_after_last_edit"]), (True, L["t7c_cuaudit.py"]["windows_after_last_edit"]))
    chk("t7b_hf.py: the rewrite the session found unapplied is skipped, and the field module carries _ceff", "_ceff" in final["t7b_hf.py"] and "Froese Fischer" in final["t7b_hf.py"][:400], True)
    chk("nlcfg.py: the GATE the last session pinned, 73/107 configurations and 96/107 steps", ("cfg_score=(73, 107), ok_score=(96, 107)" in final["nlcfg.py"]), True)
    chk("ring_zeta.py carries the trapezoid name numpy 2.4 requires, as the session patched it", "np.trapezoid" in final["ring_zeta.py"] and "np.trapz" not in final["ring_zeta.py"], True)
    chk("shoot_sr.c: the session's print and the sed derivation from shoot.c agree", L["shoot_sr.c"]["status"] in ("RECOVERED", "RECOVERED-REPLAYED"), True)
    chk("ground.py is the store's member", L["ground.py"]["method"], "STORE-MEMBER")
    chk("the sealed steps: 112 of the 119 Z values have a printed step", len(sealed_steps()[0]), 112)
    events, prints, manifest = walk_export(["nlchain.py"])
    early = [e for e in events if int(e["chat"][3:]) <= 45]
    t40, _c, _l = replay(early, ["nlchain.py"], [])
    chk("nlchain.py replayed to session 48 (before its s47 edits) hashes to the sealed pack40 manifest line",
        hashlib.sha256(t40.get("nlchain.py", "").encode()).hexdigest(), manifest.get("nlchain.py", {}).get("pack40/nlchain.py"))
    print()
    print("  %d failure(s)" % fail if fail else "  all fixtures pass")
    return fail


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true", help="regenerate in memory and compare with lowdin/rt")
    ap.add_argument("--check-chain", metavar="JSONL", help="compare a chain run against the sealed steps the sessions printed")
    ap.add_argument("--check-out", metavar="TSV", help="with --check-chain: also write the verdicts as a table")
    ap.add_argument("--runtime", metavar="DIR", help="write a runnable copy (compiles the shooters, generates the table)")
    ap.add_argument("--collect", nargs="+", metavar="KEY=JSONL", help="copy run outputs into lowdin/chain with RUNS.tsv and CHECK.tsv; keys: " + ", ".join(RUN_SPECS))
    ap.add_argument("--score", action="store_true", help="run the record's scorer nlcfg.py over the chain-mode tables in lowdin/chain; writes SCORE.tsv")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if a.check_chain:
        v, _ = check_chain(a.check_chain, tsv=a.check_out)
        return 1 if v["DIFFERS"] else 0
    final, ledger, witness, rlog, manifest = assemble()
    if a.verify:
        rt = os.path.join(a.out, "rt")
        drift = [f for f, t in final.items() if not os.path.exists(os.path.join(rt, f)) or open(os.path.join(rt, f)).read() != t]
        print("verify: %d files, %d differ%s" % (len(final), len(drift), (": " + ", ".join(drift)) if drift else ""))
        return 1 if drift else 0
    if a.collect:
        rows = collect([tuple(x.split("=", 1)) for x in a.collect], a.out)
        for r in rows:
            print("  %-13s %-26s %4d rows  Z %-8s md5 %s" % (r["key"], r["file"], r["rows"], r["Z_range"], r["md5"][:12]))
        return 0
    if a.score:
        for r in score_runs(a.out):
            print("  %-11s %-24s CONFIG %-8s STEP %-8s step failures: %s" % (r["key"], r["file"], r["config_score"], r["step_score"], r["step_failures"]))
        return 0
    if a.runtime:
        rt, out = make_runtime(final, a.runtime)
        print("runtime written to %s; eps0a_table.py:\n%s" % (rt, out[-600:]))
        return 0
    write_tree(final, ledger, witness, a.out)
    for r in ledger:
        print("  %-16s %-22s %-20s %7s  windows %-6s full-prints %-24s %s" % (r["file"], r["status"], r["method"], r.get("bytes", ""), r.get("windows_after_last_edit", ""), r.get("full_prints_equal", "")[:24], r.get("sealed_sha256", "")))
    print("wrote %s: %d files, LEDGER.tsv, WITNESS.tsv (%d windows)" % (a.out, len(final), len(witness)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
