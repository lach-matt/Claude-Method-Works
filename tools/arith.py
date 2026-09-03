#!/usr/bin/env python3
"""tools/arith.py -- the arithmetic audit of The Method 1.6, run as a program.

The standing method (DOCKET.md section 2) requires, at every section read:

    "Check the arithmetic of every ratio and percentage; never round with
     round() -- Decimal.quantize, convention named."

This is that sweep run as a class over whole members instead of one section at
a time. It extracts the arithmetic the volumes state *about themselves* -- a
fraction bound to a percentage, a signed additive expression, a binomial pair
count, a stated complement, a percentage of a base -- recomputes each in
Decimal, and reports a verdict per claim.

Stdlib only, Python 3.9+. No dependencies, so an audit can run it from any tree.

Three things it refuses to do:

  1. It never rounds with round(). Every comparison is Decimal.quantize at the
     precision the text itself states, under a named convention, and the
     convention is printed with the verdict.

  2. It never reports DISAGREE for a co-located pair. A fraction and a
     percentage on one line are not a claim unless the text binds them. An
     unbound pair is NOT-BOUND -- an assertion, not a result. This is the
     regex-artefact discipline of the C7/C9 precedents.

  3. It never picks the rounding convention for you. A claim that agrees under
     one convention and fails under another is ROUNDING-SENSITIVE, reported as
     such rather than resolved: an exact tie is a finding about the text, which
     owes its convention a name.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
from decimal import (
    Decimal,
    InvalidOperation,
    localcontext,
    ROUND_DOWN,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_MEMBERS = os.path.join(REPO, "method", "members")

# ---------------------------------------------------------------------------
# Rosters are data. Which members are reader-facing is a matter of record, not
# of this program's opinion; name one and it audits that.
# ---------------------------------------------------------------------------

VOLUMES = [
    "The_Method_1_6-2.md",
    "The_Method_1_6___The_Register-2.md",
    "The_Method_1_6___Mathematical_Compendium-2.md",
    "The_Method_1_6___The_Physics_Compendium-2.md",
    "The_Method_1_6___The_Index_of_Indices-2.md",
    "The_Method_1_6___Spectra_Compendium-2.md",
]

PAPERS = [
    "THE-LOWDIN-SOLUTION-2.md",
    "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md",
]

AUDITS = [
    "MAIN_AUDIT.md",
    "MATH_AUDIT.md",
    "PHYS_AUDIT.md",
    "REGISTER_AUDIT.md",
    "IOI_SPEC_AUDIT.md",
]

ROSTERS = {
    "volumes": VOLUMES,
    "papers": PAPERS,
    "audits": AUDITS,
    "reader-facing": VOLUMES + PAPERS,
    "all": VOLUMES + PAPERS + AUDITS,
}

SHORT = {
    "The_Method_1_6-2.md": "main",
    "The_Method_1_6___The_Register-2.md": "reg",
    "The_Method_1_6___Mathematical_Compendium-2.md": "mc",
    "The_Method_1_6___The_Physics_Compendium-2.md": "pc",
    "The_Method_1_6___The_Index_of_Indices-2.md": "ioi",
    "The_Method_1_6___Spectra_Compendium-2.md": "sc",
    "THE-LOWDIN-SOLUTION-2.md": "lw",
    "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md": "tb",
}

# ---------------------------------------------------------------------------
# Rounding conventions, named
# ---------------------------------------------------------------------------

CONVENTIONS = {
    "HALF_UP": ROUND_HALF_UP,
    "HALF_EVEN": ROUND_HALF_EVEN,
    "HALF_DOWN": ROUND_HALF_DOWN,
    "DOWN": ROUND_DOWN,
    "UP": ROUND_UP,
}

# The two standard half-conventions. A claim that separates them is sitting on
# an exact tie, and the text owes its convention a name.
DEFAULT_CONVENTIONS = ("HALF_UP", "HALF_EVEN")

AGREE = "AGREE"
DISAGREE = "DISAGREE"
SENSITIVE = "ROUNDING-SENSITIVE"
WITHIN = "WITHIN-INPUT-PRECISION"
NOT_BOUND = "NOT-BOUND"
UNCHECKABLE = "UNCHECKABLE"

VERDICTS = (AGREE, WITHIN, DISAGREE, SENSITIVE, NOT_BOUND, UNCHECKABLE)

# Verdicts that are results about the text rather than notes about the sweep.
FINDINGS = (DISAGREE, SENSITIVE)

MINUS = "−"  # U+2212, the corpus's minus sign. The em dash is punctuation.


class Claim:
    """One arithmetic claim the text makes about itself."""

    __slots__ = ("cls", "member", "line", "text", "stated", "computed",
                 "verdict", "binder", "note")

    def __init__(self, cls, member, line, text, stated, computed, verdict,
                 binder="", note=""):
        self.cls = cls
        self.member = member
        self.line = line
        self.text = text
        self.stated = stated
        self.computed = computed
        self.verdict = verdict
        self.binder = binder
        self.note = note

    def asdict(self):
        return {
            "class": self.cls,
            "member": self.member,
            "short": SHORT.get(self.member, self.member),
            "line": self.line,
            "text": self.text,
            "stated": self.stated,
            "computed": self.computed,
            "verdict": self.verdict,
            "binder": self.binder,
            "note": self.note,
        }


# ---------------------------------------------------------------------------
# Numbers
# ---------------------------------------------------------------------------

def _n(s):
    """A corpus number to a Decimal. Thousands separators and U+2212 minus."""
    return Decimal(s.replace(",", "").replace(MINUS, "-").strip())


def _dp(stated_str):
    """The decimal places the text itself states. This fixes the precision of
    the comparison: a value printed to 1 dp is not a claim about the 2nd."""
    return len(stated_str.split(".")[1]) if "." in stated_str else 0


def _exact(fn):
    with localcontext() as ctx:
        ctx.prec = 50
        return fn()


def _verdict(exact, stated_str, conventions):
    """Compare an exact Decimal against a stated value at the stated precision,
    under every named convention. Returns (verdict, computed_str, note)."""
    try:
        stated = Decimal(stated_str.replace(",", ""))
    except InvalidOperation:
        return UNCHECKABLE, "", "stated value does not parse"

    dp = _dp(stated_str)
    q = Decimal(1).scaleb(-dp)

    agreeing, failing = [], []
    for name in conventions:
        with localcontext() as ctx:
            ctx.prec = 50
            got = exact.quantize(q, rounding=CONVENTIONS[name])
        (agreeing if got == stated else failing).append(name)

    # Show the computed value with two more places than the text states, so a
    # near miss reads as a near miss and a tie reads as a tie.
    with localcontext() as ctx:
        ctx.prec = 50
        shown = exact.quantize(Decimal(1).scaleb(-(dp + 2)),
                               rounding=ROUND_HALF_EVEN)
    computed = format(shown.normalize() if shown == shown.to_integral_value()
                      else shown, "f")

    if not failing:
        return AGREE, computed, "convention-independent at %d dp" % dp
    if not agreeing:
        return DISAGREE, computed, "under every convention: %s" % ", ".join(conventions)
    return (SENSITIVE, computed,
            "agrees under %s, fails under %s -- an exact tie; the text owes "
            "its convention a name" % (", ".join(agreeing), ", ".join(failing)))


# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# A number may carry thousands separators but may not END in one: without the
# closing \d, "5 of 28," matches with the sentence's comma glued on.
INT = r"\d(?:[\d,]*\d)?"
NUM = INT + r"(?:\.\d+)?"

# "146 of 163" or "84/99". Counts, so integers on both sides.
FRAC = r"(?P<a>" + INT + r")(?:\s+of\s+|\s*/\s*)(?P<b>" + INT + r")"

# At most three lowercase-ish words may stand between the fraction and the
# percentage -- "556 of 1,664 cells valued, 33%". A digit or any punctuation in
# between breaks the binding.
TAIL = r"(?P<tail>(?:\s+[A-Za-z][A-Za-z-]*){0,3})"
PCT = r"(?P<p>\d+(?:\.\d+)?)\s?%"

RE_FRAC = re.compile(FRAC)
RE_PCT = re.compile(PCT)

# Strong binders assert the identity; the comma merely apposes it.
RE_BOUND_EQ = re.compile(FRAC + TAIL + r"\s*(?P<sep>=)\s*" + PCT)
RE_BOUND_PAREN = re.compile(FRAC + TAIL + r"\s*\(\s*" + PCT + r"\s*\)")
RE_BOUND_REV = re.compile(PCT + r"\s*\(\s*" + FRAC + r"\s*\)")
RE_BOUND_COMMA = re.compile(FRAC + TAIL + r"\s*(?P<sep>,)\s*" + PCT)

STRONG_BINDERS = (("=", RE_BOUND_EQ), ("(...)", RE_BOUND_PAREN),
                  ("%(...)", RE_BOUND_REV))
WEAK_BINDERS = ((",", RE_BOUND_COMMA),)

# A term may be a product: "12*10 + 20*6". An expression is a signed sum of
# terms, and a *chain* of expressions joined by "=" asserts that all of them
# are equal -- which is how the volumes actually write arithmetic:
#
#   |L| = S_q |A(q)| x |B(q)| = 33*5 + 33*10 + 23*15 + 8*17
#                             = 165 + 330 + 345 + 136 = 976
#
# Pairing only the first "=" with what follows it reads the second expression
# as a scalar total and invents two defects where the text has none.
TERM = NUM + r"(?:\s*[·×*]\s*" + NUM + r")*"
EXPR = TERM + r"(?:\s*[+\-" + MINUS + r"]\s*" + TERM + r")*"
# The trailing (?![A-Za-z]) is why "the degree sum 12*10 + 20*6 + 30*4 = 360
# = 2E" closes on 360 and not on the 2 of "2E". A digit glued to a letter is a
# variable; reading it as a value manufactures a defect where the text says
# "the arithmetic is sound throughout" -- and is right.
RE_EQ = re.compile(
    r"(?<![\d.,\w])(?P<chain>" + EXPR
    + r"(?:\s*=\s*" + EXPR + r")+)(?![\d,]*\d)(?![A-Za-z])"
)
RE_HAS_OP = re.compile(r"[+\-" + MINUS + r"·×*]")

RE_CHOOSE = re.compile(
    r"C\(\s*(?P<n>\d+)\s*,\s*(?P<k>\d+)\s*\)"
    r"(?:\s*[·×*]\s*(?P<f>" + INT + r"))?"
    r"\s*=\s*(?P<m>" + INT + r")\b(?![A-Za-z])"
)

RE_FAIL = re.compile(
    # "fail at 23%" states a rate, not a count of failures, so "at" is not a
    # preposition this reads and no candidate may be a percentage.
    r"fail(?:s|ed)?\s+(?:on|for|in)\s+(?P<f1>" + INT + r")\b(?!\s*%)"
    r"|\b(?P<f2>" + INT + r")\b(?!\s*%)\s+(?:\w+\s+)?fail(?:s|ed)?\b",
    re.I,
)

RE_PCT_OF = re.compile(
    PCT + r"\s+of\s+(?P<b>" + INT + r")\s*(?:is|=|,)\s*(?P<r>" + INT + r")\b"
)


def _squash(s):
    return re.sub(r"\s+", " ", s).strip()


RE_DANGLING = re.compile(r"[+\-" + MINUS + r"=×·*]\s*$")


def logical_lines(text, max_join=4):
    """Physical lines, with a wrapped expression joined to its continuation.

    DOCKET.md section 2: a construction that wraps is read on the
    whitespace-normalised join. A line ending in a dangling arithmetic
    operator is continued by the next non-blank line, which is why

        ... and 248,305 +
        248,305 - 495,515 = 1,095, as reported.

    is one claim -- correct inclusion-exclusion -- and not a false one.
    Nothing else is joined. Joining two adjacent table rows would fabricate
    arithmetic the text never states, so only a dangling operator licenses it.

    Yields (starting physical line number, joined text).
    """
    raw = text.split("\n")
    out = []
    i = 0
    while i < len(raw):
        start = i
        buf = raw[i].rstrip()
        while (RE_DANGLING.search(buf) and i + 1 < len(raw)
               and raw[i + 1].strip() and (i - start) < max_join):
            i += 1
            buf = buf + " " + raw[i].strip()
        out.append((start + 1, buf))
        i += 1
    return out


def _fmt(v):
    v = v.normalize()
    return format(v, "f")


# ---------------------------------------------------------------------------
# Finders. Each yields Claims for one line.
# ---------------------------------------------------------------------------

def find_fraction_pct(member, lineno, line, conventions, strict):
    binders = list(STRONG_BINDERS)
    if not strict:
        binders += list(WEAK_BINDERS)

    bound_spans = []
    for name, rx in binders:
        for m in rx.finditer(line):
            a, b, p = _n(m.group("a")), _n(m.group("b")), m.group("p")
            bound_spans.append(m.span())
            if b == 0:
                yield Claim("FRACTION-PCT", member, lineno, _squash(m.group(0)),
                            p + "%", "", UNCHECKABLE, name,
                            "denominator is zero")
                continue
            exact = _exact(lambda: a / b * 100)
            verdict, computed, note = _verdict(exact, p, conventions)
            if a > b:
                note = (note + "; " if note else "") + \
                    "numerator exceeds denominator -- read the site"
            yield Claim("FRACTION-PCT", member, lineno, _squash(m.group(0)),
                        p + "%", computed + "%", verdict, name, note)

    # Refusal 2: a fraction co-located with a percentage but not bound to it is
    # not a claim. Report it as NOT-BOUND so the site can be read by eye, and
    # never as a disagreement.
    if not RE_PCT.search(line):
        return
    for m in RE_FRAC.finditer(line):
        if any(s <= m.start() and m.end() <= e for s, e in bound_spans):
            continue
        pcts = [x.group(0) for x in RE_PCT.finditer(line)]
        yield Claim("FRACTION-PCT", member, lineno, _squash(m.group(0)),
                    "; ".join(pcts[:3]), "", NOT_BOUND, "",
                    "percentage on the line is not bound to this fraction")


def _lit_interval(tok):
    """A literal's value as an interval. A count is exact; a decimal printed to
    d places stands for anything within half an ulp of itself."""
    v = _n(tok)
    if "." in tok:
        half = Decimal(1).scaleb(-_dp(tok)) / 2
        return v - half, v + half
    return v, v


def _prod_interval(term):
    ivs = [_lit_interval(x) for x in re.split(r"\s*[·×*]\s*", term.strip())]
    lo, hi = ivs[0]
    for a, b in ivs[1:]:
        c = [lo * a, lo * b, hi * a, hi * b]
        lo, hi = min(c), max(c)
    return lo, hi


def _eval_interval(expr):
    parts = re.split(r"\s*([+\-" + MINUS + r"])\s*", expr)
    lo, hi = _prod_interval(parts[0])
    i = 1
    while i + 1 < len(parts):
        op, term = parts[i], parts[i + 1]
        a, b = _prod_interval(term)
        lo, hi = (lo + a, hi + b) if op == "+" else (lo - b, hi - a)
        i += 2
    return lo, hi


def _soften(verdict, note, expr, stated_str):
    """A disagreement smaller than the operands' own printed precision is not a
    defect -- it is the operands' rounding, and saying otherwise would fault the
    text for arithmetic it never claimed. MC's

        1.0838 x 1.0854 x 1.1212 x 1.0522 x 1.0125 x 1.0022 = 1.4081

    is stated "to four decimals" from factors printed to four; the product of
    the printed factors is 1.408218, but the product of what they stand for
    lies in an interval that covers 1.4081. Integer operands are exact, so a
    count-only expression is never softened."""
    if verdict != DISAGREE or "." not in expr:
        return verdict, note
    try:
        lo, hi = _exact(lambda: _eval_interval(expr))
    except (InvalidOperation, IndexError):
        return verdict, note
    try:
        stated = Decimal(stated_str.replace(",", ""))
    except InvalidOperation:
        return verdict, note
    half = Decimal(1).scaleb(-_dp(stated_str)) / 2
    if lo - half <= stated <= hi + half:
        q = Decimal(1).scaleb(-(_dp(stated_str) + 2))
        with localcontext() as ctx:
            ctx.prec = 50
            shown = (lo.quantize(q, rounding=ROUND_DOWN),
                     hi.quantize(q, rounding=ROUND_UP))
        return WITHIN, ("the operands are printed to their own precision, so "
                        "the value lies in [%s, %s]; that interval covers the "
                        "stated %s" % (_fmt(shown[0]), _fmt(shown[1]),
                                       stated_str))
    return verdict, note


def _prod(term):
    vals = [_n(x) for x in re.split(r"\s*[·×*]\s*", term.strip())]
    out = vals[0]
    for v in vals[1:]:
        out *= v
    return out


def _eval_additive(expr):
    parts = re.split(r"\s*([+\-" + MINUS + r"])\s*", expr)
    total = _prod(parts[0])
    i = 1
    while i + 1 < len(parts):
        op, term = parts[i], parts[i + 1]
        v = _prod(term)
        total = total + v if op == "+" else total - v
        i += 2
    return total


def find_equation(member, lineno, line, conventions, strict):
    for m in RE_EQ.finditer(line):
        chain = m.group("chain")
        parts = [p.strip() for p in chain.split("=") if p.strip()]
        if len(parts) < 2:
            continue
        # Two bare numbers joined by "=" are a label or an assignment, not
        # arithmetic. At least one side must actually compute something.
        if not any(RE_HAS_OP.search(p) for p in parts):
            continue
        try:
            vals = [_exact(lambda q=q: _eval_additive(q)) for q in parts]
        except (InvalidOperation, IndexError):
            continue

        closing = parts[-1]
        if not RE_HAS_OP.search(closing):
            # The chain closes on a bare stated total: compare the computed
            # value against it at the precision the text states.
            verdict, computed, note = _verdict(vals[0], closing, conventions)
            verdict, note = _soften(verdict, note, parts[0], closing)
            if len(parts) > 2 and len(set(vals[:-1])) > 1:
                verdict = DISAGREE
                note = "the chain's own members disagree"
        else:
            # Every member is an expression; the claim is that they are equal.
            verdict = AGREE if len(set(vals)) == 1 else DISAGREE
            computed = _fmt(vals[0])
            note = "exact equality; no rounding is involved"

        if len(parts) > 2:
            note = (note + "; " if note else "") + "chain of %d: %s" % (
                len(parts), " = ".join(_fmt(v) for v in vals))

        yield Claim("EQUATION", member, lineno, _squash(m.group(0)),
                    closing, computed, verdict, "=", note)


def find_choose(member, lineno, line, conventions, strict):
    for m in RE_CHOOSE.finditer(line):
        n, k = int(m.group("n")), int(m.group("k"))
        if k > n:
            yield Claim("CHOOSE", member, lineno, _squash(m.group(0)),
                        m.group("m"), "0", UNCHECKABLE, "=",
                        "k exceeds n")
            continue
        exact = Decimal(math.comb(n, k))
        factor = m.group("f")
        if factor:
            exact *= _n(factor)
        verdict, computed, note = _verdict(exact, m.group("m"), conventions)
        yield Claim("CHOOSE", member, lineno, _squash(m.group(0)),
                    m.group("m"), computed, verdict, "=", note)


def find_complement(member, lineno, line, conventions, strict):
    fracs = list(RE_FRAC.finditer(line))
    if len(fracs) != 1:
        return  # ambiguous: which fraction does the failure count complement?
    # The failure count must FOLLOW the fraction it complements. A table row
    # reading "D=0   failed, found, repaired -- 39 claims, now 60 of 63" puts a
    # zero and the word "failed" before the fraction; they are not a claim.
    end = fracs[0].end()
    fails = [m for m in RE_FAIL.finditer(line) if m.start() >= end]
    if not fails:
        return
    a, b = _n(fracs[0].group("a")), _n(fracs[0].group("b"))
    if a > b:
        return
    stated = fails[0].group("f1") or fails[0].group("f2")
    exact = b - a
    verdict, computed, note = _verdict(exact, stated, conventions)
    yield Claim("COMPLEMENT", member, lineno,
                _squash(fracs[0].group(0) + " ... " + fails[0].group(0)),
                stated, computed, verdict, "fail",
                (note + "; " if note else "") + "complement of %s of %s"
                % (fracs[0].group("a"), fracs[0].group("b")))


def find_pct_of(member, lineno, line, conventions, strict):
    for m in RE_PCT_OF.finditer(line):
        p, b = Decimal(m.group("p")), _n(m.group("b"))
        exact = _exact(lambda: p / 100 * b)
        verdict, computed, note = _verdict(exact, m.group("r"), conventions)
        yield Claim("PCT-OF", member, lineno, _squash(m.group(0)),
                    m.group("r"), computed, verdict, "is/=", note)


FINDERS = {
    "FRACTION-PCT": find_fraction_pct,
    "EQUATION": find_equation,
    "CHOOSE": find_choose,
    "COMPLEMENT": find_complement,
    "PCT-OF": find_pct_of,
}


# ---------------------------------------------------------------------------
# The sweep
# ---------------------------------------------------------------------------

def audit_text(member, text, conventions=DEFAULT_CONVENTIONS, strict=False,
               classes=None):
    classes = classes or list(FINDERS)
    out = []
    for lineno, line in logical_lines(text):
        low = line.lower()
        if "%" not in line and "=" not in line and "fail" not in low:
            continue  # nothing in this file's claim classes can fire
        for cls in classes:
            out.extend(FINDERS[cls](member, lineno, line, conventions, strict))
    return out


def audit_member(members_dir, member, **kw):
    path = os.path.join(members_dir, member)
    with open(path, encoding="utf-8") as fh:
        return audit_text(member, fh.read(), **kw)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(claims, conventions, only=None, quiet_not_bound=True, width=96):
    order = {v: i for i, v in enumerate(VERDICTS)}
    shown = [c for c in claims if not only or c.verdict in only]
    if quiet_not_bound and not only:
        shown = [c for c in shown if c.verdict != NOT_BOUND]
    shown.sort(key=lambda c: (order.get(c.verdict, 9), c.member, c.line))

    print("conventions: %s   (Decimal.quantize; round() is never used)"
          % ", ".join(conventions))
    print()
    for c in shown:
        site = "%s:%d" % (SHORT.get(c.member, c.member), c.line)
        head = "%-14s %-13s %-24s" % (site, c.cls, c.verdict)
        print(head + _squash(c.text)[:width])
        detail = "  stated %s" % c.stated
        if c.computed:
            detail += "   computed %s" % c.computed
        if c.binder:
            detail += "   bound by '%s'" % c.binder
        print(" " * 14 + detail)
        if c.note:
            print(" " * 16 + c.note)
        print()

    tally = {}
    for c in claims:
        tally[c.verdict] = tally.get(c.verdict, 0) + 1
    print("-" * 72)
    print("  ".join("%s %d" % (v, tally.get(v, 0)) for v in VERDICTS
                    if tally.get(v)))
    findings = sum(tally.get(v, 0) for v in FINDINGS)
    print("%d claim%s checked, %d finding%s"
          % (len(claims), "" if len(claims) == 1 else "s",
             findings, "" if findings == 1 else "s"))
    return findings


# ---------------------------------------------------------------------------
# Self-test. The fixtures are the corpus's own recorded arithmetic, addressed by
# the text of the site rather than by line number so a rebuild cannot move them.
# Failures are reported, never tuned away.
# ---------------------------------------------------------------------------

SYNTHETIC = [
    # (line, class, expected verdict, expected computed prefix)
    ("146 of 163 = 92%", "FRACTION-PCT", DISAGREE, "89.5"),
    ("52 of 52 = 100%", "FRACTION-PCT", AGREE, "100"),
    ("71/80 = 89%", "FRACTION-PCT", AGREE, "88.75"),
    ("84/99 = 85%", "FRACTION-PCT", AGREE, "84.8"),
    # An exact tie at the stated precision: 12.5 is 13 under HALF_UP and 12
    # under HALF_EVEN. The convention decides, so the text owes it a name.
    ("1 of 8 = 13%", "FRACTION-PCT", SENSITIVE, "12.5"),
    ("311 of 311 measured channels. As an equality it is right 57%",
     "FRACTION-PCT", NOT_BOUND, ""),
    ("0 of 0 = 50%", "FRACTION-PCT", UNCHECKABLE, ""),
    ("V-E+F = 62" + MINUS + "180+120 = 2", "EQUATION", AGREE, "2"),
    ("165 + 330 + 345 + 136 = 976", "EQUATION", AGREE, "976"),
    ("12·10 + 20·6 = 240", "EQUATION", AGREE, "240"),
    # A chain: every member must equal every other.
    ("|L| = 33·5 + 33·10 + 23·15 + 8·17 = 165 + 330 + 345 + 136 = 976",
     "EQUATION", AGREE, "976"),
    ("|A| × |B| × |q| = 33 × 17 × 4 = 2,244 against 976", "EQUATION",
     AGREE, "2244"),
    ("2 + 2 = 5", "EQUATION", DISAGREE, "4"),
    ("C(5,2) = 10 combinations", "CHOOSE", AGREE, "10"),
    ("C(6,2) = 15 exist", "CHOOSE", AGREE, "15"),
    ("C(120,2) = 7,140", "CHOOSE", AGREE, "7140"),
    ("C(9,2)·4 = 144", "CHOOSE", AGREE, "144"),
    ("C(5,2) = 11", "CHOOSE", DISAGREE, "10"),
    ("546 of 789 interior cells pass. It fails on 243 cells", "COMPLEMENT",
     AGREE, "243"),
    ("held for 318 of 407 channels and failed for 89", "COMPLEMENT",
     AGREE, "89"),
    ("20% of 264 is 53", "PCT-OF", AGREE, "52.8"),
    # Operands printed to four decimals: the product of what they stand for
    # covers the stated value, so this is not a defect.
    ("1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022 = 1.4081",
     "EQUATION", WITHIN, "1.408218"),
    # Integer operands are exact, so the same shape is NOT softened.
    ("33 × 5 = 166", "EQUATION", DISAGREE, "165"),
    # The chain must close on 360, not on the 2 of "2E".
    ("the degree sum 12·10 + 20·6 + 30·4 = 360 = 2E", "EQUATION", AGREE, "360"),
    # A failure rate is not a failure count.
    ("114 of 129 consistent, interval 82-93%; heavy elements fail at 23% "
     "against light at 8%", "FRACTION-PCT", NOT_BOUND, ""),
]

# Sites that must yield NO claim. Each one is a construction that a looser
# reading turns into a defect the text does not contain.
NEGATIVE = [
    # A table row: the zero and the word "failed" both precede the fraction.
    ("\u2145=0        failed, found, repaired \u2014 39 claims, now 60 of 63",
     "COMPLEMENT"),
    # An assignment is not arithmetic.
    ("n = 3", "EQUATION"),
    ("the cap is k = 3 and f = 1", "EQUATION"),
    # "fail at 23%" is a rate; there is no complement claim here.
    ("114 of 129 consistent on raw levels, interval 82-93%; heavy elements "
     "fail at 23% against light at 8%", "COMPLEMENT"),
]

# Fixtures that must be read across a line wrap, through audit_text.
WRAPPED = [
    ("    248,305 with h11 >= 140 \u00b7 495,515 with at least one \u00b7 and 248,305 +\n"
     "    248,305 \u2212 495,515 = 1,095, as reported.",
     "EQUATION", AGREE, "1095"),
]

# Sites in the live members. Addressed by the matched text, not by line
# number, so a rebuild cannot move a fixture out from under the self-test.
CORPUS = [
    # Repaired under R3 (item 153-01, Register 1800): the site read 92% against its own
    # count and now reads 90%. The SYNTHETIC fixture keeps the defective form, so the
    # DISAGREE path is still exercised on a literal.
    ("mc", "FRACTION-PCT", "146 of 163 = 90%", AGREE),
    ("mc", "FRACTION-PCT", "52 of 52 = 100%", AGREE),
    ("reg", "FRACTION-PCT", "1,169 of 1,654 = 70.7%", AGREE),
    ("reg", "FRACTION-PCT", "84/99 = 85%", AGREE),
    ("reg", "FRACTION-PCT", "71/80 = 89%", AGREE),
    ("reg", "CHOOSE", "C(120,2) = 7,140", AGREE),
    ("mc", "EQUATION",
     "33\u00b75 + 33\u00b710 + 23\u00b715 + 8\u00b717 = 165 + 330 + 345 + 136 = 976",
     AGREE),
    ("mc", "EQUATION", "33 × 17 × 4 = 2,244", AGREE),
    ("mc", "EQUATION",
     "1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022 = 1.4081", WITHIN),
    ("reg", "EQUATION", "12·10 + 20·6 + 30·4 = 360", AGREE),
    ("main", "EQUATION", "248,305 + 248,305 − 495,515 = 1,095", AGREE),
    ("reg", "COMPLEMENT", "318 of 407 ... failed for 89", AGREE),
]


def selftest(members_dir):
    fails = []
    checked = 0

    for line, cls, want_verdict, want_computed in SYNTHETIC:
        got = [c for c in FINDERS[cls]("synthetic", 1, line,
                                       DEFAULT_CONVENTIONS, False)]
        got = [c for c in got if c.verdict == want_verdict] or got
        checked += 1
        if not got:
            fails.append("no %s claim found in %r" % (cls, line))
            continue
        c = got[0]
        if c.verdict != want_verdict:
            fails.append("%r: verdict %s, expected %s"
                         % (line, c.verdict, want_verdict))
        elif want_computed and not c.computed.lstrip("-").startswith(want_computed):
            fails.append("%r: computed %s, expected ~%s"
                         % (line, c.computed, want_computed))

    for line, cls in NEGATIVE:
        got = list(FINDERS[cls]("synthetic", 1, line, DEFAULT_CONVENTIONS, False))
        got = [c for c in got if c.verdict != NOT_BOUND]
        checked += 1
        if got:
            fails.append("%r should yield no %s claim, got %s %s"
                         % (line, cls, got[0].verdict, got[0].text))

    for text, cls, want_verdict, want_computed in WRAPPED:
        got = [c for c in audit_text("synthetic", text) if c.cls == cls]
        checked += 1
        if not got:
            fails.append("no %s claim across the wrap in %r" % (cls, text))
        elif got[0].verdict != want_verdict:
            fails.append("wrapped %r: verdict %s, expected %s"
                         % (got[0].text, got[0].verdict, want_verdict))
        elif not got[0].computed.startswith(want_computed):
            fails.append("wrapped %r: computed %s, expected ~%s"
                         % (got[0].text, got[0].computed, want_computed))

    long_to_short = {v: k for k, v in SHORT.items()}
    by_member = {}
    for short, cls, text, want in CORPUS:
        member = long_to_short[short]
        if member not in by_member:
            by_member[member] = audit_member(members_dir, member)
        hits = [c for c in by_member[member]
                if c.cls == cls and c.text == text]
        checked += 1
        if not hits:
            fails.append("%s: %r not found in %s" % (cls, text, short))
        elif hits[0].verdict != want:
            fails.append("%s %r in %s: verdict %s, expected %s"
                         % (cls, text, short, hits[0].verdict, want))

    print("fixtures checked: %d  failed: %d" % (checked, len(fails)))
    for f in fails:
        print("  FAIL " + f)
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED")
    return 0 if not fails else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="The arithmetic audit of The Method 1.6, run as a program.")
    ap.add_argument("--members", default=DEFAULT_MEMBERS,
                    help="the members directory (default: method/members)")
    ap.add_argument("--member", action="append", default=[],
                    help="audit this member; repeatable")
    ap.add_argument("--roster", help="audit a named roster of members")
    ap.add_argument("--list-rosters", action="store_true")
    ap.add_argument("--class", dest="classes", action="append", default=[],
                    choices=sorted(FINDERS), help="restrict to this claim class")
    ap.add_argument("--conventions", default=",".join(DEFAULT_CONVENTIONS),
                    help="comma-separated rounding conventions: "
                         + ", ".join(sorted(CONVENTIONS)))
    ap.add_argument("--strict-binding", action="store_true",
                    help="require '=' or parentheses; do not accept a comma")
    ap.add_argument("--only", help="report only these verdicts, comma-separated")
    ap.add_argument("--all-verdicts", action="store_true",
                    help="include NOT-BOUND sites in the report")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.list_rosters:
        for name, members in sorted(ROSTERS.items()):
            print("%-14s %d members" % (name, len(members)))
            for m in members:
                print("    %-6s %s" % (SHORT.get(m, ""), m))
        return 0

    if args.selftest:
        return selftest(args.members)

    conventions = [c.strip().upper() for c in args.conventions.split(",") if c.strip()]
    for c in conventions:
        if c not in CONVENTIONS:
            ap.error("unknown convention %r; choose from %s"
                     % (c, ", ".join(sorted(CONVENTIONS))))

    members = list(args.member)
    if args.roster:
        if args.roster not in ROSTERS:
            ap.error("unknown roster %r; --list-rosters shows them" % args.roster)
        members += ROSTERS[args.roster]
    if not members:
        ap.error("name a member with --member or a roster with --roster")

    claims = []
    for m in members:
        path = os.path.join(args.members, m)
        if not os.path.exists(path):
            print("missing member: %s" % path, file=sys.stderr)
            return 2
        claims.extend(audit_member(args.members, m, conventions=conventions,
                                   strict=args.strict_binding,
                                   classes=args.classes or None))

    only = None
    if args.only:
        only = [v.strip().upper() for v in args.only.split(",")]
        for v in only:
            if v not in VERDICTS:
                ap.error("unknown verdict %r" % v)

    if args.json:
        json.dump({"conventions": conventions,
                   "members": members,
                   "claims": [c.asdict() for c in claims
                              if not only or c.verdict in only]},
                  sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    report(claims, conventions, only=only,
           quiet_not_bound=not args.all_verdicts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
