#!/usr/bin/env python3
"""assemble.py -- build PAPER.md from chapters/*.md (STYLE.md section 4).

Order: chapters/ files sorted by name (NN-key.md). Headings:
    # Part. Title {#part:key}            -> # Part I. Title
    ## Title {#ch:key}                    -> ## 7. Title              (chapters numbered 1, 2, ...)
    ## Appendix. Title {#app:key}         -> ## Appendix A. Title
    ### Title {#sec:key}                  -> ### 7.3 Title            (every ### in a chapter is numbered)
    **Theorem {#thm:key}**                -> **Theorem 7.4**          (thm/lem/prop/cor/def/rem share one counter)
    display line ending {#eq:key}         -> ... (7.12)               (equations: own counter per chapter)
    [[thm:key]] [[eq:key]] [[ch:key]] [[sec:key]] [[app:key]] [[part:key]]  -> Theorem 7.4, (7.12), Chapter 7, ...
    [[C:key]]                             -> Computation C17          (numbered by first citation in reading order)
Appendix A (computations) is built from computations/<key>.md, one entry per cited key, in number order; the
assembler fails if a cited key has no entry. A file chapters/NN-front.md carries the title block, unnumbered.

    python3 assemble.py            write PAPER.md and computations/NUMBERS.tsv
    python3 assemble.py --check    resolve everything, report problems, write nothing
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIND_WORD = {"thm": "Theorem", "lem": "Lemma", "prop": "Proposition", "cor": "Corollary", "def": "Definition",
             "rem": "Remark"}
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"]
PART_RX = re.compile(r"^# Part\. (.*?)\s*\{#part:([a-z0-9\-]+)\}\s*$")
CH_RX = re.compile(r"^## (?!Appendix\.)(.*?)\s*\{#ch:([a-z0-9\-]+)\}\s*$")
APP_RX = re.compile(r"^## Appendix\. (.*?)\s*\{#app:([a-z0-9\-]+)\}\s*$")
SEC_RX = re.compile(r"^### (.*?)(?:\s*\{#sec:([a-z0-9\-]+)\})?\s*$")
RES_RX = re.compile(r"\*\*(Theorem|Lemma|Proposition|Corollary|Definition|Remark) \{#(thm|lem|prop|cor|def|rem):"
                    r"([a-z0-9\-]+)\}\*\*")
EQ_RX = re.compile(r"\s*\{#eq:([a-z0-9\-]+)\}\s*$")
REF_RX = re.compile(r"\[\[(thm|lem|prop|cor|def|rem|eq|ch|sec|app|part|C):([a-z0-9][a-z0-9_\-]*)\]\]")


def load():
    d = os.path.join(HERE, "chapters")
    files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
    return [(f, open(os.path.join(d, f), encoding="utf-8").read().split("\n")) for f in files]


def number(chapters):
    labels, problems = {}, []
    out = []
    part_n = ch_n = app_n = 0
    cur = None          # current chapter number string ("7" or "A")
    sec_n = res_n = eq_n = 0

    def put(key, text, where):
        if key in labels:
            problems.append("label %s defined twice (%s)" % (key, where))
        labels[key] = text

    for fname, lines in chapters:
        new = []
        for i, ln in enumerate(lines, 1):
            where = "%s:%d" % (fname, i)
            m = PART_RX.match(ln)
            if m:
                part_n += 1
                put("part:" + m.group(2), "Part " + ROMAN[part_n - 1], where)
                new.append("# Part %s. %s" % (ROMAN[part_n - 1], m.group(1)))
                continue
            m = APP_RX.match(ln)
            if m:
                app_n += 1
                cur = chr(ord("A") + app_n - 1)
                sec_n = res_n = eq_n = 0
                put("app:" + m.group(2), "Appendix " + cur, where)
                new.append("## Appendix %s. %s" % (cur, m.group(1)))
                continue
            m = CH_RX.match(ln)
            if m:
                ch_n += 1
                cur = str(ch_n)
                sec_n = res_n = eq_n = 0
                put("ch:" + m.group(2), "Chapter " + cur, where)
                new.append("## %s. %s" % (cur, m.group(1)))
                continue
            m = SEC_RX.match(ln)
            if m and cur is not None:
                sec_n += 1
                if m.group(2):
                    put("sec:" + m.group(2), "Section %s.%d" % (cur, sec_n), where)
                new.append("### %s.%d %s" % (cur, sec_n, m.group(1)))
                continue

            def res(mm):
                nonlocal res_n
                res_n += 1
                put(mm.group(2) + ":" + mm.group(3), "%s %s.%d" % (mm.group(1), cur, res_n), where)
                return "**%s %s.%d**" % (mm.group(1), cur, res_n)
            if RES_RX.search(ln):
                if cur is None:
                    problems.append("result outside any chapter at " + where)
                ln = RES_RX.sub(res, ln)
            m = EQ_RX.search(ln)
            if m:
                eq_n += 1
                tag = "(%s.%d)" % (cur, eq_n)
                put("eq:" + m.group(1), tag, where)
                ln = EQ_RX.sub("    " + tag, ln)
            new.append(ln)
        out.append((fname, new))
    return out, labels, problems


def resolve(numbered, labels):
    problems, cnum, order = [], {}, []

    def ref(mm, where):
        kind, key = mm.group(1), mm.group(2)
        if kind == "C":
            if key not in cnum:
                cnum[key] = len(cnum) + 1
                order.append(key)
            return "Computation C%d" % cnum[key]
        k = kind + ":" + key
        if k not in labels:
            problems.append("undefined reference %s at %s" % (k, where))
            return "[[%s]]" % k
        return labels[k]
    final = []
    for fname, lines in numbered:
        for i, ln in enumerate(lines, 1):
            final.append(REF_RX.sub(lambda mm: ref(mm, "%s:%d" % (fname, i)), ln))
    return final, cnum, order, problems


def appendix_a(order, cnum):
    d = os.path.join(HERE, "computations")
    body, problems = [], []
    for key in order:
        p = os.path.join(d, key + ".md")
        if not os.path.isfile(p):
            problems.append("computation %s (C%d) has no entry in computations/" % (key, cnum[key]))
            continue
        text = open(p, encoding="utf-8").read().strip()
        body.append("**Computation C%d.** %s\n" % (cnum[key], text))
    return body, problems


def main():
    check = "--check" in sys.argv
    numbered, labels, p1 = number(load())
    final, cnum, order, p2 = resolve(numbered, labels)
    body, p3 = appendix_a(order, cnum)
    text = "\n".join(final)
    if "{{APPENDIX-A}}" in text:
        text = text.replace("{{APPENDIX-A}}", "\n".join(body))
    elif order:
        p3.append("no {{APPENDIX-A}} placeholder for the %d computation entries" % len(order))
    problems = p1 + p2 + p3
    for p in problems:
        print("PROBLEM:", p)
    print("labels %d, computations cited %d, problems %d" % (len(labels), len(order), len(problems)))
    if not check:
        open(os.path.join(HERE, "PAPER.md"), "w", encoding="utf-8").write(text.rstrip("\n") + "\n")
        os.makedirs(os.path.join(HERE, "computations"), exist_ok=True)
        with open(os.path.join(HERE, "computations", "NUMBERS.tsv"), "w", encoding="utf-8") as f:
            f.write("number\tkey\n")
            for k in order:
                f.write("C%d\t%s\n" % (cnum[k], k))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
