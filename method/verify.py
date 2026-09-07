#!/usr/bin/env python3
"""Verify method/ against itself: every member byte-exact, every bundle recovered.

Run from anywhere:  python3 method/verify.py
Exit 0 = VERIFY OK. Any mismatch is a hard failure and is reported, never repaired.

Two independent checks:
  1. Each member file matches its MEMBER-INDEX.tsv size and md5.
  2. Each member spliced back into its bundle at the recorded offset reproduces
     the bundle byte-for-byte, asserted by the bundle's own md5. This is what
     makes the extracted tree a faithful witness rather than a plausible copy.
"""
import csv, hashlib, pathlib, sys

H = pathlib.Path(__file__).resolve().parent
BUNDLES = {
    'main': 'The_Method_1_6_BUILD127_main_and_register.md',
    'comp': 'The_Method_1_6_BUILD274_compendia_papers_audits.md',
}
EXPECT_MD5 = {
    'main': 'dad1af971146d2979314fe622e1f7c9f',
    'comp': '814459facc579ca9f9e3a690fad39e01',
}

def md5(b): return hashlib.md5(b).hexdigest()

rows = list(csv.DictReader(open(H / 'MEMBER-INDEX.tsv', encoding='utf-8'), delimiter='\t'))
fail = []

for r in rows:
    p = H / 'members' / r['member']
    if not p.exists():
        fail.append(f"missing member {r['member']}"); continue
    body = p.read_bytes()
    if len(body) != int(r['bytes']) or md5(body) != r['md5']:
        fail.append(f"member {r['member']}: {len(body)} B / {md5(body)} != {r['bytes']} B / {r['md5']}")
print(f"members checked: {len(rows)}  mismatched: {len(fail)}")

for tag, fn in BUNDLES.items():
    raw = bytearray((H / fn).read_bytes())
    mine = [r for r in rows if r['bundle'] == tag]
    for r in mine:
        off, n = int(r['bundle_offset']), int(r['bytes'])
        raw[off:off + n] = (H / 'members' / r['member']).read_bytes()
    got = md5(bytes(raw))
    ok = got == EXPECT_MD5[tag]
    print(f"{tag:<20} {len(mine):>3} members spliced -> md5 {got} {'OK' if ok else 'MISMATCH (expected %s)' % EXPECT_MD5[tag]}")
    if not ok:
        fail.append(f"bundle {tag} not recovered")

if fail:
    print("\nVERIFY FAILED")
    for f in fail[:20]:
        print("  ", f)
    sys.exit(1)
print("\nVERIFY OK")
