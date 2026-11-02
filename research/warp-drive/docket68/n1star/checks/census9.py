#!/usr/bin/env python3
"""census9.py -- computations behind three of the paper's statements (RESPONSE-HL-5D.md sections 8.5 and 9).

  C23 (computed, a text census) Paper section 8.5 (lines 1012-1014): "every other conclusion drawn at the point inherits
      from this, is free of h, improves as h falls, or, like simplicity, fails at most on a countable set of h". Every
      line of N1STAR-PROOF.md section 10 that names the parameter point (gam_C = 10^6, h = 10^-6, (v, e_C) = (1/2,
      1/102400)) -- 'at the point', 'the record's point', 'the point's', 'at its point', 'at that point', 'Proposition
      10.9's point', 'point of Proposition 10.9 / 10.2x', 'gam_C = 10^6', 'h = 10^-6' -- is listed in SITES below with
      its class in section 10.54, as proof5/checks/gammac5.py lists its constants: a, b, c, d, e (10.54 (a)-(e); the
      anchor, the words by which 10.54 names it, must occur in 10.54's text), b-lead (not in (b)'s enumeration but
      under its lead sentence "Every conclusion the record drew from Proposition 10.9 at the point": the site's
      subsection names Proposition 10.9), or x (no conclusion at the parameter point: a point of S^3, a statement for
      every parameter, 10.54 itself, a setting). A hit no entry matches is UNLISTED and the check fails; so does an
      entry no hit matches (a stale list). Which class a site is in is a reading, recorded in SITES; that every hit is
      read and every anchor is in 10.54 is computed. Control: a planted line 'At the record's point the planted
      quantity Q is positive.' in section 10 is reported unlisted.
  C29 (computed, a text census) Paper section 9 (lines 1346-1347): "reduced to finitely many weights chosen under
      inequalities, six elementary losses given closed forms". The write-out is LOSS-D.md: section 2's table of the
      losses explicit in the weights (its rows counted and listed), section 2's "Not in closed form" list and section
      2b's items carrying each of them (each must be six, the same six, and each 2b item must give a closed form: a
      displayed (2.k) or l' = 2[l_I] + 10 + sup d), and section 4's E1'a list of the weights (finite; each must stand
      in a clause of sections 2b-3 with <, <=, >, >= or 'in', or, for the beta's, at the line II.G2:834 cited for
      them; the E_+ bound is the order (3 + eps_+)- of PART-III-J-PARAM.md:60, so it is checked through eps_+). 2b's
      free choices are printed beside them. Control: a planted item '7. **Planted.**' in section 2b makes the count 7.
  C27 (exact, sympy) Paper section 9 (lines 1421-1424): BEYOND5.md Propositions 6.1-6.2 and Lemma 6.3 at the lowered
      inner radius r_flat = (1/2) min(R_1, r_q(mu_end)), R_1 = mu_end^(1/2), r_q = (72^(1/2) mu_end l5^2)^(1/4). For
      the background after the shell, Tangherlini of mass mu_end in Kerr-Schild form (BEYOND5 section 1 and
      Proposition 6.2's proof: g = -f dt^2 + 2 (1 - f) dt dr + (2 - f) dr^2 + r^2 dOmega_3^2, f = 1 - mu/r^2), the
      inverse metric is computed: g^rr = f, and g^-1(dt - dr, dt - dr) = -4 mu/r^2 (t_* slices spacelike for r > 0).
      Then exactly: f(r_flat) <= -3 < 0 for every mu_end > 0 (r_flat^2 <= mu_end/4), so {r = r_flat} is spacelike, dr
      timelike; and at the record's values (l5 = 1; mu_end = (227/192) mu0, the lambda -> 0 gain (2/9)(105/128) mu0 of
      BEYOND5 section 1, mu0 = 100 and 1000) f(r_flat) < 0, r_flat < r_q < r_h = mu_end^(1/2), and (1.1) mu_end <=
      16 72^(1/2) holds at the first seed and fails at the second (where r_flat = r_q/2). Control: r_0 = 2 r_h, above
      the horizon, where f = 3/4 > 0.
      Beside it the program runs checks/r0census5.py --selftest on a copy of its file (the original writes
      ../BEYOND5-R0.tsv; the copy writes into a scratch directory) and prints its output lines; that census is not
      part of C27's verdict.

Labels: C23 computed (text census; the classes a reading); C29 computed (text census); C27 computed (exact, sympy).

Run: python3 checks/census9.py   (a few seconds)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(HERE, "..", "..", "paper", "RESPONSE-HL-5D.md")


def read(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()


def paper_has(*phrases):
    t = re.sub(r"\s+", " ", open(PAPER, encoding="utf-8").read())
    return all(p in t for p in phrases)


# ---------------------------------------------------------------- C23 the point's conclusions against 10.54

PAT = re.compile(r"at the point(?!s)|record's point|the point's|at its point|point of (?:Proposition 10\.9|10\.2\d)|"
                 r"10\.9's point|at that point|gam_C = 10\^6|h = 10\^-6", re.I)
LEAD = "Every conclusion the record drew from Proposition 10.9 at the point"
# (subsection, words of the line, class, anchor in 10.54 or the reason it is out of scope)
SITES = [
    ("10.12", "Both strips are clear at the point", "a", "[-100, 19/10]"),
    ("10.13", "Proposition 10.9's point (1/2, 1/102400, 10^-6) is admissible", "c", "10.13's Lemmas 3.3-3.8"),
    ("10.14", "checks its conditions at the point of Pr", "c", "the e-bound of his Lemma 4.4"),
    ("10.14", "At the point of Proposition 10.9 its conditions", "c", "the e-bound of his Lemma 4.4"),
    ("10.14", "Theorem 4.9's at h = 10^-6", "a", "Theorem 4.9"),
    ("10.14", "so that h = 10^-6 is not", "d", "below the h_0 of his Theorems 5.2 and 6.2"),
    ("10.21", "1/2 + vartheta_H+ = -4995.33... at h = 10^-6", "e", "10.79"),
    ("10.21", "and at h = 10^-6, the one point at which the roots are", "a", "10.21(e)"),
    ("10.21", "so for C_0 <= 98 at that point", "a", "10.21(e)"),
    ("10.22", "the invertibility of (2) at h = 10^-6", "a", "10.22"),
    ("10.23", "at its point for C_0 <= 100", "a", "10.23"),
    ("10.23", "C_0 <= 100, at that point", "a", "10.23"),
    ("10.23", "real part >= 2 at that point, 2, 3 and 1", "a", "10.23"),
    ("10.23", "and at h = 10^-6 provided that lies below", "a", "10.23"),
    ("10.23", "the roots at Proposition 10.9's point and their counts", "a", "10.23"),
    ("10.24", "Proposition 10.9, at the point and for every l", "b", "10.24(a)'s gap"),
    ("10.24", "(1.000003 at l <= 12 at the", "b", "1.000003"),
    ("10.24", "closest pair at the point being at s1", "b", "the last two free of h"),
    ("10.24", "(b) (Lemma 8.5) At the point", "b-lead", "Lemma 8.5"),
    ("10.24", "10^-7 at the point (iv)", "b", "the last two free of h"),
    ("10.24", "gam_Ups small, at the point.", "b-lead", "Proposition 8.6"),
    ("10.24", "for every l at Proposition 10.9's point", "b", "10.24(a)'s gap"),
    ("10.24", "Lemma 8.5 is computed at the point", "b-lead", "Lemma 8.5"),
    ("10.24", "Proposition 8.6 is deduced on readings, at that point", "b-lead", "Proposition 8.6"),
    ("10.25", "at the point of 10.24 in particular", "x", "stated for every admissible parameter"),
    ("10.25", "Proposition 10.9's point and for gam_Ups small, on the readings", "b-lead", "Proposition 8.6"),
    ("10.25", "alone, at Proposition 10.9's point for small gam_Ups", "b-lead", "Proposition 8.6"),
    ("10.27", "at that point, and so at every point", "x", "a point of S^3, not the parameter point"),
    ("10.27", "at Proposition 10.9's point with gam_Ups small, L-hat(sigma)", "b-lead", "Proposition 8.8"),
    ("10.27", "which Proposition 10.9's h = 10^-6 must lie", "d", "below the h_0 of his Theorems 5.2 and 6.2"),
    ("10.31", "the one point h = 10^-6 of Proposition 10.9", "a", "10.21(e)"),
    ("10.33", "the harmonics at the point of 10.27", "x", "a point of S^3 (10.27's sin chi = 3/5)"),
    ("10.34", "l = 2, 3, at Proposition 10.9's poin", "d", "Simplicity (10.52(i))"),
    ("10.34", "computed for l <= 12 at the point (section 10.24)", "d", "Simplicity (10.52(i))"),
    ("10.37", "(iv) (the record's point: gam_C = 10^6", "b", "10.37"),
    ("10.37", "At gam_C = 10^6 the method fails", "b", "10.37"),
    ("10.37", "smooth determinant at the record's point", "b", "10.37"),
    ("10.37", "lam < 1 + eps_ind -- at the record's point", "b", "10.37"),
    ("10.37", "Hence at the record's point, on the readings of (c)", "b", "10.37"),
    ("10.37", "is a pure resonance of L-bar at the record's point", "b", "10.37"),
    ("10.37", "on a further reading, at the record's point", "b", "10.37"),
    ("10.38", "sbar5.py's S-bar at the point", "c", "10.38"),
    ("10.44", "gam_C, at the record's", "c", "(10.44)"),
    ("10.44", "nonzero at the point (P3)", "c", "(10.44)"),
    ("10.46", "499996.6171875 at the point", "c", "the I+ gap's upper end"),
    ("10.46", "K4 is exact at the point", "b", "(10.46)"),
    ("10.48", "record's point (gam_Ups = 1/100)", "c", "the I+ gap's upper end"),
    ("10.52", "10.24 computed the indicial roots of L at the record's point", "d", "10.52"),
    ("10.52", "**Proposition 10.43 (computed).** At the record's point", "d", "10.52"),
    ("10.52", "Lemma 8.4 holds in five dimensions at the point", "d", "10.52"),
    ("10.52", "nothing proved beyond Lemma 8.4 at the point", "d", "10.52"),
    ("10.54", "(b) (what inherits)", "x", "10.54 itself"),
    ("10.54", "The point's numbers themselves", "x", "10.54 itself"),
    ("10.54", "being the point's (10.52; D129)", "x", "10.54 itself"),
    ("10.54", "B5 is discharged", "x", "10.54 itself"),
    ("10.71", "A property holds at one point", "x", "a setting: 10.70's kind-C steps, no conclusion"),
    ("10.75", "(10.24 (iv)), at the record's point", "b-lead", "Lemma 8.5"),
    ("10.75", "the record's point", "c", "The quantities proportional to gam_C"),   # (xxv): gam_Ups, (1-e)(1-v)gam_C
    ("10.79", "### 10.79", "e", "10.79"),
    ("10.79", "At h = 10^-6, vartheta_H+ = -4995.83", "e", "10.79"),
    ("10.79", "so at h = 10^-6 and at", "e", "10.79"),
    ("10.79", "vartheta_H+ at h = 10^-6 is -4995.44", "e", "10.79"),
]


def c23(control=False):
    L = read("N1STAR-PROOF.md").split("\n")
    a = next(i for i, l in enumerate(L) if l.startswith("## 10."))
    b = next(i for i, l in enumerate(L) if l.startswith("## 11."))
    if control:
        L = L[:b] + ["At the record's point the planted quantity Q is positive."] + L[b:]
    subs, sec, hits = {}, None, []
    for i in range(a, b + (1 if control else 0)):
        if L[i].startswith("### 10."):
            sec = L[i].split()[1]
        subs.setdefault(sec, []).append(L[i])
        if PAT.search(L[i]):
            hits.append((i + 1, sec, L[i]))
    t54 = re.sub(r"\s+", " ", "\n".join(subs["10.54"]))
    used, unlisted, cls = set(), [], {}
    for n, sec, line in hits:
        m = [k for k, (s, key, c, x) in enumerate(SITES) if s == sec and key in line and k not in used]
        if len(m) == 0:
            unlisted.append((n, sec, line.strip()[:100]))
            continue
        k = m[0]
        used.add(k)
        s, key, c, x = SITES[k]
        if c in "abcde":
            ok = x in t54
        elif c == "b-lead":
            ok = LEAD in t54 and "Proposition 10.9" in "\n".join(subs[sec])
        else:
            ok = c == "x"
        if not ok:
            unlisted.append((n, sec, "anchor not in 10.54: %s" % x))
        cls[c] = cls.get(c, 0) + 1
    stale = [SITES[k][:2] for k in range(len(SITES)) if k not in used]
    if not control:
        lead = sorted({(SITES[k][0], SITES[k][3]) for k in used if SITES[k][2] == "b-lead"})
        print("  C23: %d lines of section 10 name the point, in %d subsections; by class %s; unlisted %s; stale "
              "entries %s" % (len(hits), len({h[1] for h in hits}), dict(sorted(cls.items())), unlisted or "none",
                              stale or "none"), flush=True)
        print("  C23: under (b)'s lead sentence only, not its enumeration: %s" % lead, flush=True)
    else:
        print("  C23 control: unlisted %s" % unlisted, flush=True)
    phrase = paper_has("every other conclusion drawn at the point inherits from this, is free of h, improves as h "
                       "falls, or, like simplicity, fails at most on a countable set of h")
    return phrase and not unlisted and not stale


# ---------------------------------------------------------------- C29 the losses and weights of LOSS-D

INEQ = re.compile(r"<|≤|>|≥|∈")
WEIGHTS = {"ε_ind": r"ε_ind", "ε_K": r"ε_K", "ε_+": r"ε_\+", "ε": r"ε(?![_'′\w])", "ℓ_I": r"ℓ_I(?!\^)",
           "a_I": r"a_I", "ℓ_I^max": r"ℓ_I\^max", "the E_+ bound": None, "the β's at each use": None}


def section(t, head, nxt):
    i = t.index(head)
    return t[i:t.index(nxt, i + len(head))]


def c29(control=False):
    t = read("LOSS-D.md")
    if control:
        t = t.replace("**What this closes.**", "7. **Planted.** loses 3, (2.6).\n\n**What this closes.**", 1)
    s2 = section(t, "## 2. The elementary losses", "## 2b.")
    s2b = section(t, "## 2b.", "## 3.")
    s3 = section(t, "## 3.", "## 4.")
    s4 = section(t, "## 4.", "## 5.")
    table = [r for r in s2.split("\n") if r.startswith("| ") and not r.startswith("| loss ")]
    notcf = re.findall(r"^(\d)\. (.+?)[(:]", s2.split("**Not in closed form.**")[1], re.M)
    items = re.split(r"^(?=\d\. \*\*)", s2b.split("**What this closes.**")[0], flags=re.M)[1:]
    names = [re.match(r"\d\. \*\*(.+?)\.?\*\*", it).group(1) for it in items]
    closed = [bool(re.search(r"\(2\.\d\)", it) or "2⌈ℓ_I⌉ + 10 + sup d" in it) for it in items]
    same = len(notcf) == len(names) and all(a.replace("'s ", " ").split()[:3] == n.split()[:3]
                                                    for (_, a), n in zip(notcf, names))
    print("  C29: section 2's table: %d losses explicit in the weights: %s" %
          (len(table), "; ".join(r.split("|")[1].strip() for r in table)), flush=True)
    print("  C29: not in closed form (section 2): %d; carried in 2b: %d (%s); each a closed form: %s; same six: %s" %
          (len(notcf), len(items), "; ".join(names), closed, same), flush=True)
    wl = re.sub(r"\s+", " ", s4).split("Choose numbers for ")[1].split(", from the")[0]
    wl = [w.strip() for w in re.split(r", | and ", wl)]
    wblock = re.sub(r"\s+", " ", s3.split("**Weights.**")[1].split("None of")[0])
    near = lambda sym, txt: re.search(r"[<≤>≥∈][^;<≤>≥∈]{0,25}%s|%s[^;<≤>≥∈]{0,25}[<≤>≥∈]" % (sym, sym), txt)
    found = {}
    for w in wl:
        if WEIGHTS.get(w, "?") == "?":
            found[w] = None
        elif w == "the β's at each use":
            g2 = open(os.path.join(HERE, "proof5", "PART-II-G2-DECAY.md"), encoding="utf-8").read().split("\n")
            k = g2[833].find(r"\beta'_I<\min(\beta_I")
            found[w] = "II.G2:834 " + g2[833][k:k + 40] if k >= 0 else None
        elif w == "the E_+ bound":
            j = open(os.path.join(HERE, "proof5", "PART-III-J-PARAM.md"), encoding="utf-8").read().split("\n")
            m = near(WEIGHTS["ε_+"], wblock)
            found[w] = ("J-PARAM:60 order (3 + eps_+)-, with eps_+: " + m.group(0)) if (
                r"(\mathcal E_+,(3+\epsilon_+)-)" in j[59] and m) else None
        else:
            m = near(WEIGHTS[w], wblock)
            where = "section 3:"
            if not m:
                m, where = near(WEIGHTS[w], re.sub(r"\s+", " ", s2b)), "section 2b:"
            found[w] = (where + " " + m.group(0)) if m else None
    for w in wl:
        print("    weight %-22s %s" % (w, found[w] or "NO INEQUALITY FOUND"), flush=True)
    free = re.sub(r"\s+", " ", s2b).split("free choices still to be made: ")[1].split(".")[0]
    print("  C29: %d weights (E1'a), each with an inequality: %s; 2b's free choices: %s; loop counts (section 3): %d"
          % (len(wl), all(found.values()), free, len(re.findall(r"^- ", s3.split("**Counts.**")[1].split("**The")[0],
                                                              re.M))), flush=True)
    phrase = paper_has("finitely many weights chosen under inequalities, six elementary losses given closed forms")
    return (phrase and len(notcf) == 6 and len(items) == 6 and all(closed) and same and len(wl) < 20
            and all(found.values()))


# ---------------------------------------------------------------- C27 r = r_0 spacelike inside the horizon

def c27(control=False):
    t, r, mu, l5, th, p1, p2 = sp.symbols("t r mu l5 theta phi1 phi2", positive=True)
    f = 1 - mu/r**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -f, 1 - f, 1 - f, 2 - f
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2*sp.sin(th)**2, r**2*sp.sin(th)**2*sp.sin(p1)**2
    gi = g.inv()
    dt, dr = sp.Matrix([1, 0, 0, 0, 0]), sp.Matrix([0, 1, 0, 0, 0])
    q = lambda x, y: sp.simplify((x.T*gi*y)[0, 0])
    ok = sp.simplify(q(dr, dr) - f) == 0 and sp.simplify(q(dt - dr, dt - dr) + 4*mu/r**2) == 0
    R1, rq = sp.sqrt(mu), (sp.sqrt(72)*mu*l5**2)**sp.Rational(1, 4)
    rflat = sp.Min(R1, rq)/2
    r0 = 2*sp.sqrt(mu) if control else rflat
    # every mu > 0: f increases in r and r_flat <= R_1/2, so f(r_flat) <= f(R_1/2) = -3
    gen = sp.diff(f, r).is_positive is True and sp.simplify(f.subs(r, R1/2)) == -3
    if control:
        gen = bool(sp.simplify(f.subs(r, r0)) < 0)
    rows, allneg = [], True
    for mu0 in (100, 1000):
        me = sp.Rational(227, 192)*mu0
        assert sp.Rational(2, 9)*sp.Rational(105, 128) == sp.Rational(35, 192)
        sub = {mu: me, l5: 1}
        rv = r0.subs(sub)
        fv = sp.nsimplify(f.subs(r, rv).subs(sub))
        neg = bool(sp.simplify(fv) < 0)
        inside = bool(rv < rq.subs(sub)) and bool(rq.subs(sub) < sp.sqrt(me))
        c11 = bool(me <= 16*sp.sqrt(72))
        rows.append("mu0 = %d: mu_end = %s, r_0 = %s = %.6g, f(r_0) = %.6g (< 0: %s), r_0 < r_q < r_h: %s, (1.1): %s"
                    % (mu0, me, rv, float(rv), float(fv), neg, inside, c11))
        allneg &= neg and (inside or control)
        ok &= c11 == (mu0 == 100)
    if not control:
        print("  C27: g^rr = f = 1 - mu/r^2 and g^-1(dt - dr, dt - dr) = -4 mu/r^2 computed: %s; f(R_1/2) = -3, "
              "f increasing in r, so f(r_flat) <= -3 for every mu_end > 0: %s" % (ok, gen), flush=True)
        for x in rows:
            print("    " + x, flush=True)
    else:
        print("  C27 control (r_0 = 2 r_h): " + "; ".join(rows), flush=True)
    phrase = paper_has("lowered below r_q(μ_end) = (√72 μ_end l5²)^(1/4)")
    return phrase and ok and gen and allneg


def r0census():
    tmp = tempfile.mkdtemp()
    os.makedirs(os.path.join(tmp, "checks"))
    shutil.copy(os.path.join(HERE, "checks", "r0census5.py"), os.path.join(tmp, "checks"))
    os.symlink(os.path.join(HERE, "proof5"), os.path.join(tmp, "proof5"))
    p = subprocess.run([sys.executable, os.path.join(tmp, "checks", "r0census5.py"), "--selftest"],
                       capture_output=True, text=True)
    for x in p.stdout.strip().split("\n"):
        print("  r0census5.py --selftest: " + x, flush=True)
    print("  r0census5.py exit %d" % p.returncode, flush=True)
    shutil.rmtree(tmp)


CHECKS = [("C23", c23), ("C29", c29), ("C27", c27)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    r0census()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
