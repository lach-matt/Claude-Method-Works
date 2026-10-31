"""Census of III.B's inner radius r_0 = R_1/2 in proof5 Parts III-VII (BEYOND5 route (c), D363).

Every line of proof5/PART-{III,IV,V,VI,VII}*.md (Parts II, VIII and IX excluded; IX, the gauge comparison, is not
used by Theorem 0.2) that names r_0, the inner radius or
boundary, R_1/2, r_sharp, (5/8)R_1, (3/4)R_1 or, since D373, (3/8)R_1 is listed with a class:

  DEF    III.B's r_0 itself: its definition, the domain {|x| >= r_0}, the time functions built from it;
  VAL    the value R_1/2 enters a numerical inequality (the note says whether a smaller radius keeps it);
  SPC    used only through "{r = r_0} is spacelike, dr future timelike there, inside every horizon of the family
         and outside every inner horizon" (artificial boundary, vanishing inside the horizon, radial ODEs);
  CON    used through a constant chosen from it (delta_0, nu_0, R_nu, delta'_0, eps_X, weights);
  OTHER  another r_0: III.C''s exterior radius, the source's r_0 (= r_c), r_A at A = 0, notation.

The classes are read at the lines (python3 r0census5.py prints the windows with --show); nothing is proved here.
Writes ../BEYOND5-R0.tsv; --selftest checks the counts against the census as recorded in BEYOND5.md section 3.
"""
import re, glob, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
PAT = re.compile(r'r_0(?![0-9])|r_\{0\}|inner radius|inner boundary|\\t?frac12\s*R_1|R_1/2|r_\\sharp'
                 r'|\\frac58\s*R_1|\\frac34\s*R_1|\\frac38\s*R_1|3R_1/8')

OTHER_FILES = {'PART-III-C2-POLYHOM.md': "III.C''s exterior radius, r_0 large",
               'PART-III-C3-BOOSTDATA.md': "III.C''s exterior radius; r_1 = 2r_0",
               'PART-IV-EB.md': "Omega_ext,r_0 of III.C'", 'PART-IV3-NM.md': "Omega_ext,r_0 of III.C'",
               'PART-IV4-SLAB.md': "r_1 = 2r_0, r_0 large (III.C')",
               'PART-III-I-CONE.md': 'inner boundary of Omega_iota',
}
SPC_FILES = {'PART-III-D-GAUGEPOT.md': 'ODE on (r_0, r_h), r_0 < r_h', 'PART-III-D2-ZEROENERGY.md': '{r_0<r<r_h}',
             'PART-III-E-CONSTRAINT.md': 'vanishing inside the horizon, {|x| = c} spacelike',
             'PART-III-F3-MODES.md': 'modes on {r>r_0}; f<0 on (r_0-delta_0, r_h)',
             'PART-III-F4-ZERO.md': 'smooth on {r>r_0}',
             'PART-III-F5-PAIRINGS.md': 'zero on {r_0<|x|<r_h}', 'PART-III-H-AUGMENT.md': 'r >= r_0 > 0',
             'PART-III-H3-UNIFORM.md': 'compact subsets of {r>r_0}',
             'PART-III-I3-ALMOST.md': 'artificial boundary, spacelike',
             'PART-V-GLUING.md': None}
CON_FILES = {'PART-VI-DYN.md':
             "I.A's radii from the inner radius: r_0 = R_1/2, delta_0 = (r_h-R_1/2)/8, collar to 3R_1/8 (D373)",
             'PART-VI2-HORIZON.md': 'Psi_b the identity on {|x| <= 5R_1/8}; sup over [3R_1/8, r_h] finite',
             'PART-VI3-TRAPPING.md': "I.A's radii; domain {|x| >= 3R_1/8}"}
LINES = {  # (file, line): (class, note)
    ('PART-III-B-FAMILY.md', 102): ('OTHER', 'r_A at A = 0'), ('PART-III-B-FAMILY.md', 117): ('OTHER', 'r_A at A = 0'),
    ('PART-III-B-FAMILY.md', 157): ('VAL',
        'B: |x|^2 >= R_1^2/4 > 2||A||^2; a smaller r needs eps_param < r/(sqrt2 R_1)'),
    ('PART-III-B-FAMILY.md', 158): ('VAL', 'as 157'), ('PART-III-B-FAMILY.md', 159): ('VAL', 'as 157'),
    ('PART-III-B-FAMILY.md', 244): ('VAL',
        'psi(2R_1) = 2R_1 - r_0 >= 3R_1/2: holds for every smaller r_0'),
    ('PART-III-B-FAMILY.md', 161): ('SPC', 'horizon inside {|x| > r_0}'),
    ('PART-III-H2-ADMISS.md', 380): ('CON', 'delta_1'), ('PART-III-H2-ADMISS.md', 381): ('CON', 'r_Gamma > r_2 > r_0'),
    ('PART-III-H2-ADMISS.md', 398): ('CON', 'bounded factors'),
    ('PART-III-H2-ADMISS.md', 402): ('CON', 'weight integral'),
    ('PART-III-H2-ADMISS.md', 421): ('CON', '<x> <= C r'),
    ('PART-III-K-NONLINEAR.md', 43): ('DEF', 'psi_IVP = psi on [r_0, 5R_1]'),
    ('PART-III-K-NONLINEAR.md', 44): ('DEF', ''),
    ('PART-III-K-NONLINEAR.md', 84): ('CON', 'nu_0 = min(1/4, r_0/8)'), ('PART-III-K-NONLINEAR.md', 86): ('CON', ''),
    ('PART-III-K-NONLINEAR.md', 103): ('CON', 'R_nu = (r_0+R)/2'),
    ('PART-III-K-NONLINEAR.md', 134): ('OTHER', "III.C'''s exterior radius, stated"),
    ('PART-III-K-NONLINEAR.md', 135): ('OTHER', 'as 134'),
    ('PART-III-K-NONLINEAR.md', 559): ('CON', 'nu vanishes near r_0'),
    ('PART-IV5-CDMODES.md', 35): ('OTHER', "the source's r_0 = r_c"), ('PART-IV5-CDMODES.md', 36): ('OTHER', 'as 35'),
    ('PART-IV5-CDMODES.md', 186): ('SPC', 'continuity on [r_sharp, inf)'),
    ('PART-IV5-CDMODES.md', 209): ('SPC', 'supported at the inner boundary'),
    ('PART-IV6-SOLV.md', 23): ('OTHER', "the source's r_0 = r_c"), ('PART-IV6-SOLV.md', 314): ('OTHER', 'r_c for r_0'),
    ('PART-IV6-SOLV.md', 317): ('OTHER', 'r_c for r_0'),
    ('PART-VI3-TRAPPING.md', 374): ('VAL', 'r_0-delta_0 = 7R_1/16 < 5R_1/8 (D373); at r_0^A = r, delta_0 <= R_1/16'),
    ('PART-VII-ASSEMBLY.md', 88): ('CON', '(0.2) on {r_0 <= r <= R\'}'),
}
for i in (192, 428, 532, 533, 679, 680, 882, 884):
    LINES[('PART-IV6-SOLV.md', i)] = ('VAL', 'Lemma 0.5 (6) = record 10.14 (ii), checked on [r_h/2, oo) only; '
                                            'holds on (0, r_h) by the inner piece (D366)')
for i in range(142, 157):
    LINES[('PART-VII-ASSEMBLY.md', i)] = ('CON', "Lemma 1.2: a' = q_0 - delta'_0 < r_0/2, delta'_0 in (0, q_0) free")


def classify(f, i):
    if (f, i) in LINES: return LINES[(f, i)]
    if f in OTHER_FILES: return 'OTHER', OTHER_FILES[f]
    if f in SPC_FILES: return 'SPC', SPC_FILES[f] or 'domain {|x| >= r_0}'
    if f in CON_FILES: return 'CON', CON_FILES[f]
    if f == 'PART-III-B-FAMILY.md' or f == 'PART-VII-ASSEMBLY.md': return 'DEF', ''
    if f == 'PART-III-H2-ADMISS.md': return 'SPC', 'X = {r >= r_0}, extendible at r = r_0; Seeley into {r > r_0/2}'
    if f == 'PART-III-K-NONLINEAR.md': return 'SPC', 'inner boundary spacelike, dr future timelike'
    if f == 'PART-IV6-SOLV.md': return 'SPC', "r_sharp: only dr future timelike on [r_sharp, 3R_1/4] used (IV'''''5)"
    return '?', ''


def census():
    rows = []
    fs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(P5, 'PART-*.md')))
    for f in fs:
        if not re.match(r'PART-(III|IV|V|VI|VII)[-0-9]', f): continue
        for i, l in enumerate(open(os.path.join(P5, f), encoding='utf-8'), 1):
            if PAT.search(l):
                c, n = classify(f, i)
                rows.append((f, i, c, n, l.strip()))
    return rows


def main():
    rows = census()
    if '--show' in sys.argv:
        for f, i, c, n, l in rows: print(f, i, c, '|', l[:150])
        return
    with open(os.path.join(HERE, '..', 'BEYOND5-R0.tsv'), 'w', encoding='utf-8') as o:
        o.write('file\tline\tclass\tnote\n')
        for f, i, c, n, l in rows: o.write('%s\t%d\t%s\t%s\n' % (f, i, c, n))
    cnt = collections.Counter(r[2] for r in rows)
    nf = len({r[0] for r in rows})
    print('lines', len(rows), 'files', nf, dict(sorted(cnt.items())))
    if '--selftest' in sys.argv:
        ok = cnt.get('?', 0) == 0 and cnt == EXPECT and nf == EXPECT_FILES
        print('selftest', 'ok' if ok else 'FAIL'); sys.exit(0 if ok else 1)


EXPECT = collections.Counter({'CON': 60, 'DEF': 19, 'OTHER': 108, 'SPC': 120, 'VAL': 13})
EXPECT_FILES = 25

if __name__ == '__main__':
    main()
