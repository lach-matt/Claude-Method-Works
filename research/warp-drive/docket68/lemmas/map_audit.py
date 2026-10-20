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
  [456: M, "most of the warp theorem map is still stale.  Review ALL aspects of the map please."  Four more, so that
  what the review set right is held at every render.]
  A8 (computed) Every row's chip is phase2's audit (442): Passes, Re-derive with the items it waits on, Beyond 273, or
     Deferred -- and Computed · theorized for a passing row the register marks COMPUTED-THEORIZED (534); its row class
     agrees; every register row stands on the page.
  A9 (computed) Every station's colours are its rows': the head's dot the worse end, the strip's two tags each end's,
     the pills naming exactly the rows that do not pass at each end.
  A10 (computed) Outside the folds kept as record, every range of items opened at 441, 446 or 450 ends at the
     rulings' last item, the closed blocks the page names excepted (441-443, your bar; 450-452, the solver's three
     known solutions); every range of BOUNCE-RESEARCH sections opened at 11 ends at its last section.
  A11 (computed) No text of the build script stands on the page (a quote-plus-quote join, a format slot).
  A12 (computed) Every tally cell is coloured by its row's standing, and the counts the page states -- the tally's
     label, its key, the review panel -- are phase2's; the key's count of notes is the notes on the page.
  A13 (computed) The header's fold of rulings lists every item of the rulings file from 372 to the last.

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
PHASE2 = os.path.join(HERE, "phase2.py")
COL = {"ok": "green", "def": "def", "read": "amber", "open": "red"}
RANK = {"ok": 0, "def": 1, "read": 2, "open": 3}
LMCLS = {"ok": "", "read": " r", "open": " o", "def": " d"}
CLOSED = ((441, 443), (450, 452))


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


def register_status():
    """[item 534] each row's register status, so a COMPUTED-THEORIZED row is chipped as such"""
    spec = importlib.util.spec_from_file_location("ma_wt2", THEOREM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {row[1].split()[0]: row[2] for row in mod.LEMMAS_NOW}


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


def phase2_audit():
    spec = importlib.util.spec_from_file_location("ma_p2", PHASE2)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.audit()


def klass(aud, rid):
    """phase2's standing of a row: ok passes, read waits on a reading, open rests on 273 or is OPEN on its own claim
    (item 489: FACE2s, FACE2 and the rows on them, SOURCEs and SOURCE, R1), def deferred; [534] a COMPUTED-THEORIZED
    row passes (ok)"""
    w = aud[rid]
    if not w:
        return "ok"
    if any("own claim (OPEN)" in x for x in w):
        return "open"
    if rid.startswith("SOURCE") and any("OPEN" in x for x in w):
        return "def"
    return "open" if any("273" in x for x in w) else "read"


def waits(aud, rid):
    """the item numbers a row waits on, 273 first"""
    out = {m.group(1) for m in (re.match(r"(\d+)", x) for x in aud[rid]) if m}
    return sorted(out, key=lambda n: (n != "273", int(n)))


def chip(aud, rid, status=None):
    k = klass(aud, rid)
    if k == "ok" and (status or {}).get(rid) == "COMPUTED-THEORIZED":     # [item 534] M: 'label them as computed'
        return k, "Computed · theorized"
    if k == "ok" and (status or {}).get(rid) == "PROVED on QB":           # [item 542] M: 'PROVED on QB'
        return k, "Passes · on QB"
    if k == "open" and any("own claim (OPEN)" in x for x in aud[rid]):
        return k, "Open"
    return k, {"ok": "Passes", "def": "Deferred", "open": "Beyond · 273"}.get(k) or \
        "Re-derive · " + ", ".join(waits(aud, rid))


def end_of(ids, rid):
    if rid.endswith("s") and rid[:-1] in ids:
        return "small"
    return "large" if rid + "s" in ids else "both"


def worst(aud, rows):
    ks = [klass(aud, r) for r in rows]
    if ks and all(k == "def" for k in ks):
        return "def"
    return max(ks, key=lambda k: RANK[k]) if ks else "ok"


def unfolded(page):
    """the page less its folds kept as record (details.was-note)"""
    return re.sub(r'<details class="was-note">.*?</details>', "", page, flags=re.S)


def body_text(page):
    """the page less its header (title, lede, meta and the fold of rulings), tags stripped, entities resolved"""
    h0 = page.index("<header")
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
    aud = phase2_audit()
    rst = register_status()
    rows = re.findall(r'<li class="(lm[^"]*)"><span class="chip (\w+)">([^<]*)</span><div class="what"><b>([^<]+)</b>',
                      page)
    bad = []
    for cls, ck, txt, rid in rows:
        rid = html.unescape(rid)
        k, want = chip(aud, rid, rst) if rid in aud else (None, None)
        if (ck, html.unescape(txt)) != (k, want) or cls not in ("lm shared", "lm" + LMCLS.get(k, "?")):
            bad.append(rid)
    on_page = {html.unescape(r[3]) for r in rows}
    r = bool(rows) and not bad and on_page == set(ids) == set(aud)
    ok.append(r); say("A8 %d row chips against phase2's audit of %d rows: %s%s" % (
        len(rows), len(aud), r, (" (wrong %s)" % bad[:6]) if bad else ""))
    bad = []
    for sid, body in re.findall(r'<article class="station" id="(\w+)">(.*?)</article>', page, re.S):
        rids = [html.unescape(x) for x in re.findall(r'<div class="what"><b>([^<]+)</b>', body)]
        sm = [x for x in rids if end_of(ids, x) in ("small", "both")]
        lg = [x for x in rids if end_of(ids, x) in ("large", "both")]
        ks, kl = worst(aud, sm), worst(aud, lg)
        dot = re.search(r'<div class="head"><div class="dot (\w+)">', body)
        stop = re.search(r'<div class="stop"><a href="#%s"><div class="dot \w+">.*?<div class="v (\w+)">[^<]*</div>'
                         r'<div class="lp (\w+)">' % sid, page)
        pills = re.findall(r'<span class="verdict (\w+)">([^<·]+)·([^<]*)</span>', body)
        named = {"small": set(), "large": set()}
        cols = {"small": set(), "large": set()}
        for col, who, txt in pills:
            for e in (("small", "large") if who.strip() == "Both ends" else
                      ("small",) if who.strip() == "Small end" else ("large",)):
                cols[e].add(col)
                named[e] |= set(re.findall(r"([A-Za-z0-9′']+) \(", txt))
        need = {e: {x for x in grp if klass(aud, x) in ("read", "open")} for e, grp in (("small", sm), ("large", lg))}
        good = (dot and dot.group(1) == COL[max((ks, kl), key=lambda k: RANK[k])] and stop and
                (stop.group(1), stop.group(2)) == (COL[ks], COL[kl]) and cols == {"small": {COL[ks]}, "large": {COL[kl]}}
                and named == need)
        if not good:
            bad.append(sid)
    r = not bad
    ok.append(r); say("A9 every station's dot, strip tags and pills from its rows' standing: %s%s" % (
        r, (" (wrong %s)" % bad) if bad else ""))
    live = unfolded(page)
    stale = [m.group(0) for m in re.finditer(r"(?<![\d.,])(441|446|450)[–-](\d{3})(?!\d)", live)
             if int(m.group(2)) != n and (int(m.group(1)), int(m.group(2))) not in CLOSED]
    stale += [m.group(0) for m in re.finditer(r"sections 11[–-](\d+)", live) if int(m.group(1)) != ls]
    r = not stale
    ok.append(r); say("A10 every open range of items ends at %d, of sections at %d: %s%s" % (
        n, ls, r, (" (stale %s)" % stale[:6]) if stale else ""))
    text = html.unescape(re.sub(r"<style.*?</style>|<script.*?</script>", "", page, flags=re.S))
    leak = re.findall(r"' \+ |\+ A \+|%[ds]\b|\\n", re.sub(r"<[^>]+>", " ", text))
    r = not leak
    ok.append(r); say("A11 no build-script text on the page: %s%s" % (r, (" (%s)" % leak[:4]) if leak else ""))
    cellk = {"c-ok": "ok", "c-read": "read", "c-open": "open", "c-def": "def"}
    wrong = [html.unescape(t) for c, t in re.findall(r'<span class="cell ([\w-]+)" title="([^"]+)"></span>', page)
             if html.unescape(t) not in aud or cellk.get(c) != klass(aud, html.unescape(t))]
    cnt = {k: sum(klass(aud, x) == k for x in aud) for k in ("ok", "read", "open", "def")}
    label = "%d pass, %d wait on a reading" % (cnt["ok"], cnt["read"])
    key = dict(re.findall(r'<li><span class="sw (c-\w+)"></span><b>(\d+)</b>', page))
    notes = len(re.findall(r'<div class="left since">', page))
    key_since = re.search(r'<span class="sw since"></span><b>(\d+)</b>', page)
    good = (not wrong and page.count(label) >= 2 and
            {cellk[k]: int(v) for k, v in key.items() if k in cellk} == cnt and
            key_since is not None and int(key_since.group(1)) == notes)
    ok.append(good); say("A12 tally cells coloured by standing, the counts %s and %d notes as the audit and page give: %s%s"
                         % (cnt, notes, good, (" (cells wrong %s)" % wrong[:4]) if wrong else ""))
    fold = re.search(r"<summary>Every ruling since item (\d+), in order</summary>(.*?)</details>", page, re.S)
    gap = ["no fold"]
    if fold:
        lo, cited = int(fold.group(1)), set()
        for a, b in re.findall(r"(?<![\d.,])(\d{3})(?:[–-](\d{3}))?(?!\d)", fold.group(2)):
            cited |= set(range(int(a), int(b or a) + 1))
        items = {int(m) for m in re.findall(r"^(\d{1,4})\. \*\*", open(RULINGS, encoding="utf-8").read(), re.M)}
        gap = sorted(k for k in items if lo <= k <= n and k not in cited)
    r = not gap
    ok.append(r); say("A13 the fold of rulings lists every item to %d: %s%s" % (n, r, (" (missing %s)" % gap[:8]) if gap else ""))
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
        # [483: every row but SOURCE passes, so the mutants turn a passing row's marks the other way]
        # [542: O1a's chip reads "Passes · on QB", so the mutant matches the chip whatever its words]
        "chip_open": re.sub(r'<span class="chip ok">[^<]*</span><div class="what"><b>O1a</b>',
                            '<span class="chip open">Beyond · 273</span><div class="what"><b>O1a</b>', page, count=1),
        "dot_red": re.sub(r'(<article class="station" id="crossing">\s*<div class="head"><div class="dot )green',
                          r"\1red", page, count=1),
        "stale_range": page.replace("446–%d" % n, "446–%d" % (n - 1), 1),
        "leak": page.replace("</h2>", " register' + A + 's</h2>", 1),
        "tally_recolour": page.replace('<span class="cell c-ok" title="M1"></span>', '<span class="cell c-open" title="M1"></span>', 1),
        "fold_gap": page.replace("(437); the delivery", "; the delivery", 1),
        "key_count": re.sub(r'<span class="sw c-ok"></span><b>(\d+)</b>',
                            lambda m_: '<span class="sw c-ok"></span><b>%d</b>' % (int(m_.group(1)) + 1), page, count=1),
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
