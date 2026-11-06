"""r9text5.py -- SETTLE-GLAM5 round 9: the file's own text, checked (the round-8 reader's m1 and nit 8).

  T1 (text, exact) the rounds 1-7 region of SETTLE-GLAM5.md (up to "## Round 8") has, word for word and in order, the
     words of the round-7 file (git 54c8634, md5 8235b0a9), once the [R8] and [R9] notes are removed (bracket-matched)
     and the two R7 notes that round 8 moved to their paragraphs' ends ("[R7 (nit): on Omega, Theorem P's (P-iv)" and
     "[R7 (minor 2): not \"every condition computed\"") are compared as notes, each equal word for word. A word
     multiset would not see a passage moved; the sequence does (the round-8 reader's m1).
  T1' control: round 8's misplacement re-created in memory (the R7 note's last words moved into the paragraph above it)
     fails T1.
  T2 (text) no line opens a block inside a paragraph: after its indent no line begins with "- ", "+ ", "* ", ">" or a
     number followed by "." or ")" unless it is an intended list item, a line at column 0 beginning "- " or "N. " whose
     previous line is blank, a list item or a list item's indented continuation, or a label ending in ".**", "*", ":"
     or ".*" (a list that interrupts a paragraph by design); lines in code blocks and indented code are skipped.
  T2' control: the round-7 state of the same note (its continuation line beginning "- g_b0^-1|_op") is flagged.
  T3 every line of SETTLE-GLAM5.md is within 121 characters.
Labels: text checks, exact.

    python3 checks/r9text5.py     (a few seconds)
"""
import hashlib
import os
import re
import subprocess
import sys

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ROOT))))
GIT_R7, MD5_R7 = "54c8634", "8235b0a90a1185603b3b2aca39378014"
PATH = "research/warp-drive/docket68/n1star/SETTLE-GLAM5.md"


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def strip_notes(t, tags=("[R8", "[R9")):
    out, i, removed = [], 0, []
    while True:
        js = [j for j in (t.find(tag, i) for tag in tags) if j >= 0]
        if not js:
            out.append(t[i:])
            break
        j = min(js)
        out.append(t[i:j])
        d, k = 0, j
        while True:
            if t[k] == "[":
                d += 1
            elif t[k] == "]":
                d -= 1
                if d == 0:
                    break
            k += 1
        removed.append(t[j:k + 1])
        out.append(" ")
        i = k + 1
    return "".join(out), removed


MOVED = ["[R7 (nit): on Omega, Theorem P's (P-iv)", "[R7 (minor 2): not \"every condition computed\""]


def cut_moved(t):
    got = []
    for head in MOVED:
        j = t.index(head)
        d, k = 0, j
        while True:
            if t[k] == "[":
                d += 1
            elif t[k] == "]":
                d -= 1
                if d == 0:
                    break
            k += 1
        got.append(t[j:k + 1].split())
        t = t[:j] + " " + t[k + 1:]
    return t, got


def word_sequence(old, new):
    o = old[:old.index("## Round 8")] if "## Round 8" in old else old
    n = new[:new.index("## Round 8")]
    n2, notes = strip_notes(n)
    o3, mo = cut_moved(o)
    n3, mn = cut_moved(n2)
    return o3.split() == n3.split() and mo == mn, len(o3.split()), len(n3.split()), len(notes)


MARK = re.compile(r"^([-+*] |>|\d+[.)](\s|$))")


def md_flags(text):
    L = text.split("\n")
    flags, fence = [], False
    for i, l in enumerate(L):
        if l.startswith("```"):
            fence = not fence
            continue
        if fence or l.startswith("    ") or i == 0 or not L[i - 1].strip():
            continue
        body = l.lstrip(" ")
        if not MARK.match(body):
            continue
        prev = L[i - 1]
        intended = (l == body and (l.startswith("- ") or re.match(r"^\d+\. ", l))
                    and (prev.startswith("- ") or re.match(r"^\d+\. ", prev) or prev.startswith("  ")
                         or prev.rstrip().endswith((".**", ":", ".*", "*"))))
        if not intended:
            flags.append((i + 1, l[:60]))
    return flags


R7NOTE_TAIL = "In (iv), continuity holds on every interval on which"


def main():
    new = open(os.path.join(ROOT, "SETTLE-GLAM5.md")).read()
    old = subprocess.run(["git", "-C", REPO, "show", f"{GIT_R7}:{PATH}"], capture_output=True, text=True).stdout
    md5 = hashlib.md5(old.encode()).hexdigest()
    print("T1  the rounds 1-7 region against the round-7 file, word by word")
    ok, no, nn, k = word_sequence(old, new)
    check("T1 git 54c8634's file (md5 8235b0a9) and the current one, [R8]/[R9] notes removed and the two moved R7 notes "
          "compared as notes: the same words in the same order", ok and md5 == MD5_R7,
          f"md5 {md5[:8]}; {no} and {nn} words; {k} notes removed")
    # control: re-create round 8's misplacement in memory
    i = new.index(R7NOTE_TAIL)
    tail = "|g^-1 - g_b0^-1|_op < 7/25, with R7-A's cut; Step 6's openness at sigma* is R7-A.]"
    j = new.index(tail, i)
    bad = new[:j] + new[j + len(tail):]
    p = bad.rfind("which is therefore at most C lam^2 rho^-9.", 0, i)
    bad = bad[:p] + "which is therefore at most C lam^2 rho^-9. - g_b0^-1|_op < 7/25, with R7-A's cut; Step 6's " \
        "openness at sigma* is R7-A.]" + bad[p + len("which is therefore at most C lam^2 rho^-9."):]
    okc, _, _, _ = word_sequence(old, bad)
    check("T1' control: round 8's misplacement re-created in memory fails T1", not okc)
    print("T2  no line opens a block inside a paragraph")
    fl = md_flags(new)
    check("T2 every line that begins with a block marker is an intended list item", not fl, str(fl[:5]))
    r7 = new.replace(R7NOTE_TAIL + "\n|g^-1 - g_b0^-1|_op", R7NOTE_TAIL + " |g^-1\n- g_b0^-1|_op", 1)
    check("T2' control: the round-7 state of that note (a continuation line beginning '- g_b0^-1|_op') is flagged",
          len(md_flags(r7)) == 1 and r7 != new, str(md_flags(r7)[:2]))
    print("T3  line lengths")
    long_ = [(n_ + 1, len(l)) for n_, l in enumerate(new.split("\n")) if len(l) > 121]
    check("T3 every line within 121 characters", not long_, str(long_[:5]))
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
