#!/usr/bin/env python3
"""regchat.py — the register chat's whole interface (R 1733).

    open     verify C4 · both gates · count · next free id · slip inbox
    ingest   validate slips · allocate ids in order · append · rebuild · re-gate
    close    seal the next bank · write the certificate · list what is owed

Built so a fresh chat spends its context on the work and not on rediscovering the
protocol. The rules it enforces are the ones the register already earned; each is
cited at the point it fires, so a refusal explains itself without a lookup.
"""
import os, re, subprocess, sys, shutil, hashlib, datetime, glob

DATA, GEN, OUT = "REGISTER-DATA.md", "REGISTER.md", "/mnt/user-data/outputs"
SLIPS, AUDITS, RT = "slips", "The_Method_1_6_audits.py", "roundtrip.py"
HEADING = re.compile(r"^ {0,3}(\d{3,4})([a-z]?)\. ", re.M)


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


def ids():
    return [m.group(1) + m.group(2) for m in HEADING.finditer(open(DATA, encoding="utf-8").read())]


def next_id():
    return max(int(re.match(r"\d+", i).group()) for i in ids()) + 1


def gates(label):
    """Both gates, cache cleared first — R 1709: a pass from cache is the old instrument's."""
    shutil.rmtree(".zeno", ignore_errors=True)
    a = "25/25" if "ALL TWENTY-FIVE PASS" in sh(f"python3 {AUDITS}") else "FAIL"
    r = sh(f"python3 {RT}").strip().splitlines()[-1] if os.path.exists(RT) else "?"
    print(f"  gates {label:<22} audits {a} · round-trip {r}")
    return a == "25/25" and r.startswith("6 of 6")


def pyc_guard(before):
    """R 1713 / R 1728: remove only what this run wrote; never the bank's own."""
    now = set(glob.glob("__pycache__/*.pyc"))
    for p in now - before:
        os.remove(p)
    if now - before:
        print(f"  bytecode written by this run and removed: {len(now - before)} (R 1713)")


def read_slip(p):
    txt = open(p, encoding="utf-8").read()
    d, body = {}, None
    for line in txt.split("\n"):
        m = re.match(r"^(SOURCE|ARTEFACT|TITLE):\s*(.*)$", line)
        if m and body is None:
            d[m.group(1)] = m.group(2).strip()
        elif line.strip() == "BODY:":
            body = []
        elif body is not None:
            body.append(line)
    d["BODY"] = "\n".join(body or []).strip()
    return d


def validate(p, d):
    """Every check capable of failing (§4.6). Refuse, never coerce (§2.9)."""
    bad = []
    for k in ("SOURCE", "ARTEFACT", "TITLE"):
        if not d.get(k):
            bad.append(f"missing {k}")
    if not d["BODY"]:
        bad.append("empty BODY")
    whole = d.get("TITLE", "") + "\n" + d["BODY"]
    if whole.count("**") % 2:
        bad.append("unbalanced bold markers (R 1565)")
    for line in whole.split("\n"):
        if HEADING.match(" " + line.lstrip()):
            bad.append(f"line reads as a false heading (R 1617, R 1730): {line.strip()[:40]}")
    if re.search(r"\bR ?1[0-9]{3}\b\.?\s*\*\*", whole) or re.match(r"\s*\d{3,4}\.", d["BODY"]):
        bad.append("slip claims its own id — ids are allocated here (R 1726)")
    return bad


def cmd_open():
    print("REGISTER CHAT — opening. Nothing is stated about the work until this prints.\n")
    files = int(sh("find . -type f | wc -l"))
    dirs = int(sh("find . -mindepth 1 -type d | wc -l"))
    print(f"  C4  {files} files · {dirs} dirs below root · {dirs + 1} archive dir entries (R 1726)")
    print(sh("python3 register_count.py").rstrip())
    ok = gates("at baseline")
    print(f"\n  NEXT FREE ID  R {next_id()}")
    s = sorted(x for x in glob.glob(f"{SLIPS}/*.md") if "TEMPLATE" not in x)
    print(f"  SLIPS WAITING {len(s)}")
    for p in s:
        d = read_slip(p)
        flag = "  [TRANSCRIPT-ONLY]" if d.get("ARTEFACT", "").upper().startswith("TRANSCRIPT") else ""
        print(f"    - {os.path.basename(p):<34} {d.get('TITLE','(no title)')[:46]}{flag}")
    print("\n  ready" if ok else "\n  GATES DID NOT PASS AT BASELINE — stop and report")


def cmd_ingest():
    s = sorted(x for x in glob.glob(f"{SLIPS}/*.md") if "TEMPLATE" not in x)
    if not s:
        print("no slips to ingest"); return
    parsed, refused = [], []
    for p in s:
        d = read_slip(p)
        bad = validate(p, d)
        (refused if bad else parsed).append((p, d, bad))
    for p, d, bad in refused:
        print(f"  REFUSED {os.path.basename(p)}")
        for b in bad:
            print(f"      {b}")
    if refused:
        print("\n  Nothing appended. Refusal is a finding, not a failure (§2.9).")
        return
    before = set(glob.glob("__pycache__/*.pyc"))
    shutil.copy(DATA, f"/home/claude/{DATA}.PRE-{next_id()}.bak.md")
    n = next_id()
    with open(DATA, "a", encoding="utf-8") as f:
        for p, d, _ in parsed:
            f.write(f"\n {n}. **{d['TITLE']}** {d['BODY']}\n")
            print(f"  R {n}  <- {os.path.basename(p)}  [{d['SOURCE']}]")
            n += 1
    sh(f"python3 register_gen.py > {GEN}")           # the redirect, always (R 1700)
    rc = subprocess.run("python3 register_count.py", shell=True, capture_output=True, text=True)
    print(rc.stdout.rstrip())
    if rc.returncode:
        print("  DUPLICATE ID — the append is bad; restore the .bak and re-run")
        return
    gates("after ingest")
    pyc_guard(before)
    for p, _, _ in parsed:
        os.rename(p, p + ".done")
    print(f"  {len(parsed)} slip(s) ingested and marked .done")


def cmd_close():
    before = set(glob.glob("__pycache__/*.pyc"))
    ok = gates("at close")
    pyc_guard(before)
    m = re.search(r"restore-point-2_(\d+)", sh("ls /mnt/user-data/uploads") + sh("ls /home/claude"))
    nxt = f"restore-point-2_{int(m.group(1)) + 1 if m else 16}.tar.gz"
    sh(f"tar czf /home/claude/{nxt} .")
    h = hashlib.sha256(open(f"/home/claude/{nxt}", "rb").read()).hexdigest()
    files = int(sh("find . -type f | wc -l")); dirs = int(sh("find . -mindepth 1 -type d | wc -l"))
    cnt = sh("python3 register_count.py")
    owed = [l.rstrip() for l in open("OWED.md", encoding="utf-8")] if os.path.exists("OWED.md") else []
    cert = [f"# CERTIFICATE — register session, {datetime.date.today()}", "",
            f"**Bank out:** `{nxt}`  sha256 `{h}`", "",
            f"**C4:** {files} files · {dirs} dirs below root · {files + dirs + 1} archive entries", "",
            "```", cnt.rstrip(), "```", "",
            f"**Gates at close:** {'25/25 · 6/6' if ok else 'DID NOT PASS — see above'}", "",
            "## Owed, carried not decided", *(owed or ["- (none recorded in OWED.md)"])]
    open("/home/claude/CERTIFICATE-REGISTER.md", "w", encoding="utf-8").write("\n".join(cert) + "\n")
    os.makedirs(OUT, exist_ok=True)
    for f in (f"/home/claude/{nxt}", "/home/claude/CERTIFICATE-REGISTER.md"):
        shutil.copy(f, OUT)
    print(f"  sealed {nxt} · sha256 {h[:16]}… · certificate written")
    print("  present both from /mnt/user-data/outputs and hand off")


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "open"
    {"open": cmd_open, "ingest": cmd_ingest, "close": cmd_close}.get(c, cmd_open)()
