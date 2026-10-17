#!/usr/bin/env python3
"""map_audit.py -- item 455: the full map page is current before every render.  M: "please make sure the full map page
is being updated in full each time you render it for me."  Carried as M-MAP-IN-FULL: every render updates the whole
page -- its rows, stages, findings and questions -- to the current record, not its header line alone.  This instrument
is run before each publish of chainmap.html; a render that fails it is not published.  Labels: computed (each check
reads the page against the record).  Worked in the conversation; not verified; not seated.  2026-10-17.

  A0 (read) M's words: 455.
  A1 (computed) The header names the last item of the rulings file.
  A2 (computed) Every item from 441 to the last is cited in the page's body, outside the header and its fold of
     rulings: the body says what each item did, not the header alone.
  A3 (computed) Every instrument the theorem's selftest runs from item 441 on (warptheorem.py T1) is named on the page.
  A4 (computed) The tally holds one cell per row of the register (LEMMAS_NOW), each titled by its row.
  A5 (computed) The footer counts the register's rows.
  A6 (computed) The page cites BOUNCE-RESEARCH.md through its last section.
  A7 (computed) The page's elements nest.

python3 map_audit.py [--selftest | --mutants]
"""
import html
import html.parser
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MAP = os.path.join(D68, "chainmap.html")
THEOREM = os.path.join(D68, "warptheorem.py")
BOUNCE = os.path.join(HERE, "BOUNCE-RESEARCH.md")
WORDS = ("please make sure the full map page is being updated in full each time you render it for me",)
FIRST = 441


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def last_item():
    return max(int(m) for m in re.findall(r"^(\d{1,4})\. \*\*", open(RULINGS, encoding="utf-8").read(), re.M))


def register_ids():
    spec = importlib.util.spec_from_file_location("ma_wt", THEOREM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [row[1].split()[0] for row in mod.LEMMAS_NOW]


def t1_since(first=FIRST):
    """T1's lemma files from the '# item NNN' comment numbered >= first onward"""
    src = open(THEOREM, encoding="utf-8").read()
    i = src.index("def lemma_selftests")
    j = src.index("_load(os.path.join(HERE, \"lemmas\", f)", i)
    block = src[i:j]
    out, on = [], False
    for line in block.splitlines():
        m = re.match(r"\s*# items? (\d+)", line)
        if m:
            on = on or int(m.group(1)) >= first
        if on:
            out += re.findall(r'"([a-z0-9_]+\.py)"', line)
    return out


def body_text(page):
    """the page less its header block (meta and its fold), tags stripped, entities resolved"""
    h0 = page.index('<div class="meta">')
    h1 = page.index("</header>", h0)
    rest = page[:h0] + page[h1:]
    return html.unescape(re.sub(r"<[^>]+>", " ", rest))


def last_section():
    return max(int(m) for m in re.findall(r"^## (\d+)\.", open(BOUNCE, encoding="utf-8").read(), re.M))


class _Nest(html.parser.HTMLParser):
    VOID = ("br", "link", "meta", "img", "hr", "input", "wbr")

    def __init__(self):
        super().__init__()
        self.st, self.err = [], 0

    def handle_starttag(self, t, a):
        if t not in self.VOID:
            self.st.append(t)

    def handle_endtag(self, t):
        if self.st and self.st[-1] == t:
            self.st.pop()
        else:
            self.err += 1


def audit(page, quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    n = last_item()
    r = ("rulings through item %d " % n) in page
    ok.append(r); say("A1 the header names item %d, the rulings' last: %s" % (n, r))
    body = body_text(page)
    missing = [k for k in range(FIRST, n + 1) if not re.search(r"(?<![\d.,])%d(?![\d])" % k, body)]
    r = not missing
    ok.append(r); say("A2 every item %d-%d cited in the body: %s%s" % (FIRST, n, r, (" (missing %s)" % missing)
                                                                    if missing else ""))
    t1 = t1_since()
    absent = [f for f in t1 if f[:-3] not in page]
    r = bool(t1) and not absent
    ok.append(r); say("A3 the %d instruments T1 runs since %d all named: %s%s" % (len(t1), FIRST, r,
                                                                             (" (absent %s)" % absent) if absent else ""))
    ids = register_ids()
    cells = [html.unescape(t) for t in re.findall(r'<span class="cell [^"]+" title="([^"]+)"></span>', page)]
    r = sorted(cells) == sorted(ids)
    ok.append(r); say("A4 the tally: %d cells against %d register rows, titled alike: %s" % (len(cells), len(ids), r))
    r = ("LEMMAS_NOW, %d rows;" % len(ids)) in page
    ok.append(r); say("A5 the footer counts %d rows: %s" % (len(ids), r))
    ls = last_section()
    r = bool(re.search(r"sections? \d+[–-]%d\b|§%d\b|section %d\b" % (ls, ls, ls), page))
    ok.append(r); say("A6 BOUNCE-RESEARCH cited through section %d: %s" % (ls, r))
    p = _Nest()
    p.feed(page)
    r = p.err == 0 and not p.st
    ok.append(r); say("A7 the elements nest: %s" % r)
    return ok


def selftest(quiet=False, page=None):
    say = (lambda *a: None) if quiet else print
    r0 = words()
    say("A0 words: %s" % r0)
    ok = [r0] + audit(page if page is not None else open(MAP, encoding="utf-8").read(), quiet)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    page = open(MAP, encoding="utf-8").read()
    n = last_item()
    cases = {
        "stale_header": page.replace("rulings through item %d " % n, "rulings through item %d " % (n - 1), 1),
        "header_only": re.sub(r"(?<![\d.,])%d(?![\d])" % n, "", page[:page.index("</header>")]) and
        (page[:page.index("</header>")] + re.sub(r"(?<![\d.,])%d(?![\d])" % n, "",
                                                page[page.index("</header>"):])),
        "drop_cell": re.sub(r'<span class="cell [^"]+" title="[^"]+"></span>', "", page, count=1),
        "drop_instrument": page.replace("corridor_p1", "corridor_pX"),
        "unclosed": page.replace("</section>", "", 1),
    }
    caught = 0
    for k, v in cases.items():
        bad = not selftest(quiet=True, page=v)
        caught += bad
        print("mutant %-16s %s" % (k, "caught" if bad else "MISSED"))
    print("%d/%d caught" % (caught, len(cases)))
    return caught == len(cases)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
