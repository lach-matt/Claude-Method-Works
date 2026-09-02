import re,sys,subprocess,os,pathlib
B='/home/claude/build/'
def esc_us(l):
    if l.startswith('```'): return l
    if l.startswith('    '): return l   # aligned display: left as code by displays()
    l=re.sub(r"(?<=[`)\]])'(?=\w)",'\u2019',l)   # apostrophe after a code span or bracket: not a smart-quote opener
    parts=re.split(r'(`[^`]*`)',l)
    return ''.join(p if p.startswith('`') else fix_stars(p.replace('_','\\_')) for p in parts)
def fix_stars(p):
    # mathematical stars that pandoc would read as emphasis
    p=re.sub(r', \*,', r', \\*,', p)                 # tuple wildcard (3,0,1,1,*,0,1,1)
    p=re.sub(r',\*,', r',\\*,', p)
    # star after a symbol and before an operator: w*/e*, dn*/dZ, p*−1, Z*², V* → 2 —
    # not the close of a one-letter italic like *h*/ν
    p=re.sub(r'(?<=[A-Za-z0-9])(?<!\*[A-Za-z])(?<!\*[A-Za-z][A-Za-z])\*(?=[/+−²|]| [→<>≪=≈])', r'\\*', p)
    p=re.sub(r'^(\*[^*].*[A-Za-z])\*\*$', r'\1\\**', p) # *… w** = italic ending on a starred symbol
    return p
odd=0
def fix_head(h):
    # headline is bold; a paired *x* inside stays italic, a lone * prints literally
    inner=h[2:-2]
    inner=re.sub(r'(?<![*\w])\*(?=\w)(.+?)(?<=\S)\*(?![*\w])',lambda m:'\x01'+m.group(1)+'\x01',inner)
    inner=inner.replace('*','\\*').replace('\x01','*')
    return '**'+inner+'**'
def balanced(t):
    open_=False
    for m in re.finditer(r'\*\*',t):
        i=m.start(); j=m.end()
        pre=t[i-1] if i else ' '; post=t[j] if j<len(t) else ' '
        opener=not post.isspace() and (pre.isspace() or pre in '(—-"\'')
        closer=not pre.isspace() and not opener
        if opener and open_: return False
        if closer and not open_: return False
        if opener: open_=True
        elif closer: open_=False
    return not open_
def split_close(body):
    import itertools
    sites=[m.start() for m in re.finditer(r'\* \*\*(?=[,.;:)\s\'\u2019])',body)]
    if not sites: return body
    sites=sites[:8]
    best=None
    for combo in itertools.product((0,1),repeat=len(sites)):
        t=body
        for pos,c in sorted(zip(sites,combo),reverse=True):
            t=t[:pos]+('**' if c==0 else '')+t[pos+4:]
        if balanced(re.sub(r'(?<!\*)\*(?!\*)','',t)): best=t; break
    return best if best is not None else re.sub(r'\* \*\*(?=[,.;:)\s\'\u2019])','**',body)
def fix_body(body):
    # the body is italic by style (EntryBody); only bold spans are kept as markup
    body=body.replace('\\*','\x02')                              # literal \* in the record is kept
    body=re.sub(r'(?<=\d[A-Z])\*\*(?=[)<\s])','\x02\x02',body)   # term symbols 2P**<3/2>, (2P**), 3P** J=0
    body=re.sub(r'(?<=\d)\*\*(?=/)','\x02\x02',body)              # 11**/21**
    body=split_close(body)                                    # **phrase* **, → **phrase**,  or dropped, by balance
    body=re.sub(r'\*\*([^*]+?)\*([.,;:]) \*\*',r'**\1**\2 **',body)  # **A*. **B → **A**. **B
    body=re.sub(r'(?<![*])\*(\w[^*]{0,400}?)\*\*(?=[,.;:)\s\'\u2019]|$)',r'*\1*',body)  # *iterate**, → *iterate*,
    # bold close mangled to a single star: **A, *b.* *C → **A, *b.** *C  (only when the bold is otherwise unclosed)
    def close_bold(m):
        seg=m.group(0)
        return re.sub(r'(\S)\* \*(?=\S)',r'\1** *',seg,count=1)
    if body.count('**')%2 and re.search(r'\*\*\s*$',body): body=re.sub(r'\*\*\s*$','',body)  # trailing orphan
    # merged italic close+open read as a bold opener: ". **X.* **Y" → ". *X.* **Y"
    body=re.sub(r'(?<=[.;:] )\*\*([^*]+?[.;:])\* \*\*',r'*\1* **',body)   # unconditional: a bold can't close on one star
    body=re.sub(r'^\*\*([^*]+?[.;:])\* \*\*',r'*\1* **',body)
    body=re.sub(r'(?<=[.;:])\*\s+\*\*\s*$',r'*',body)                    # ". ** " tail after an italic close
    if body.count('**')%2:
        body=re.sub(r'\*\*(?:(?!\*\*).)*$',close_bold,body)
    body=re.sub(r'\*{3,}',r'**',body)                        # *** → **
    body=re.sub(r'(?<!\*)\*(?!\*)','',body)                 # drop single italic marks
    body=re.sub(r'(?<![^\s])\*\*\s+\*\*(?![^\s])','',body)  # empty bold (free-standing only)
    body=re.sub(r'\*\* +(?=[,.;:)])','**',body)              # ** , → **,
    return body.strip().replace('\x02','\\*')
def nest_bold(t):
    # walk the ** tokens: emit only depth 0->1 and 1->0; inner bold is absorbed;
    # a closer with nothing open, or an opener never closed, prints literally
    out=[];last=0;depth=0;open_pos=None
    for m in re.finditer(r'\*\*',t):
        i=m.start(); j=m.end()
        pre=t[i-1] if i else ' '; post=t[j] if j<len(t) else ' '
        opener=not post.isspace() and (pre.isspace() or pre in '(—-"\'')
        out.append(t[last:i]); last=j
        if opener:
            if depth==0: open_pos=len(out); out.append('**')
            depth+=1
        else:
            if depth==0: pass                       # orphan closer: dropped
            elif depth==1: out.append('**'); depth=0
            else: depth-=1
    tail=t[last:]
    if depth>0 and open_pos is not None:
        # opener never closed: close at the end of its sentence
        m=re.search(r'[.!?](?=\s|$)',tail)
        if m: tail=tail[:m.end()]+'**'+tail[m.end():]
        else: out[open_pos]=''
    out.append(tail)
    return ''.join(out)
def fix_bodies(L):
    global odd
    out=[];n=0;inentry=False
    for l in L:
        if re.match(r'^### \d+',l): inentry=True; out.append(l); continue
        if l.startswith('#'): inentry=False
        if inentry and re.match(r'^\d+[a-z]?\. [^*]*\*\*( \*|\s*$)',l): l='**'+l   # sub-entry headline missing its opener
        if inentry and l.startswith('**'):
            m=re.match(r'^(\*\*.+?\*\*)(?=\*?\s|$)\*?\s*(.*)$',l)
            if m:
                head,body=m.group(1),m.group(2)
                codes=re.findall(r'`[^`]*`',body); body=re.sub(r'`[^`]*`',lambda x:'\x00',body)
                body=fix_body(body)
                if not balanced(body): odd+=1
                body=nest_bold(body)
                for c in codes: body=body.replace('\x00',c,1)
                head=fix_head(head)
                l=head+'\n\n::: {custom-style="EntryBody"}\n'+body+'\n:::\n' if body else head; n+=1
        out.append(l)
    print('bodies re-wrapped',n,'bodies with unbalanced bold (nest-resolved)',odd); return out
def _demark(b):
    # W-084 (chat 50). A block kept monospace is never parsed as markdown, so any bold markup inside
    # it prints as its own delimiters — main delivered 221 spans as literal **25**, **cells**, **Λ₉**.
    # PAIRED delimiters only, and only where the span holds no asterisk: the ~20 legitimate printed
    # stars in this volume are SINGLE (tuple wildcards, w*/e*, dn*/dZ) and are not touched. The block
    # keeps its column alignment because the substitution is length-reducing and symmetric.
    return re.sub(r'\*\*([^*\n]{1,60}?)\*\*', r'\1', b)
def displays(L):
    # Indented blocks are the book's set-off material. A block with column alignment
    # (3+ internal spaces) or an 8+ indent is a typed table/equation and stays monospace;
    # every other indented block is prose and becomes a block quote so its markup
    # parses and its underscores escape.
    out=[];i=0;q=0;t2=0
    while i<len(L):
        if re.match(r'^ {2,3}\S',L[i]) and re.search(r'\S {3,}\S',L[i]):
            # a two-space aligned block is a typed table; markdown would join it into prose.
            j=i
            while j<len(L) and re.match(r'^ {2,3}\S',L[j]) and L[j].strip(): j+=1
            blk=L[i:j]
            runs=sum(1 for b in blk if re.search(r'\S {5,}\S',b) or len(re.findall(r'\S {3,}\S',b))>=2)
            if j-i>=2 and runs>=max(1,(j-i)//2):
                out.extend('    '+_demark(b[2:].rstrip()) for b in blk); t2+=1; i=j; continue
        if re.match(r'^ {4,}\S',L[i]):
            j=i
            while j<len(L) and re.match(r'^ {4,}\S',L[j]): j+=1
            blk=L[i:j]
            runs=any(re.search(r'\S {5,}\S',b) or len(re.findall(r'\S {3,}\S',b))>=2 for b in blk)
            prose=any((len(b.split())>=12 and not re.search(r'\S {3,}\S',b)) or re.match(r'^\s*\*\*[^*]+\*\*\s*$',b) for b in blk)
            aligned=runs or (blk[0].startswith(' '*8) and not prose)
            if aligned: out.extend(_demark(b) for b in blk)
            else: out.extend('> '+b.strip() for b in blk); q+=1
            i=j
        else: out.append(L[i]); i+=1
    print('display blocks quoted',q,'· two-space tables set',t2); return out
def cont_tables(L):
    # A pipe table split by a prose interjection continues with no header row, so pandoc
    # sets the continuation as literal text.
    # Re-head each such block with its parent table's header + separator. Guards: the
    # block must have >= 2 rows and >= 4 columns and match the last header's column
    # count, so lone math lines opening with | (e.g. determinants) stay text.
    out=[]; last=None; i=0
    n=0
    while i<len(L):
        if L[i].startswith('|'):
            j=i
            while j<len(L) and L[j].startswith('|'): j+=1
            blk=L[i:j]
            sep=len(blk)>1 and set(blk[1].replace('|','').replace(' ',''))<=set('-:') and '-' in blk[1]
            cols=blk[0].count('|')-1
            if sep:
                last=(blk[0],blk[1],cols)
            elif len(blk)>=2 and cols>=4 and last and last[2]==cols:
                if out and out[-1].strip(): out.append('')   # a table cannot interrupt a paragraph
                out.extend([last[0],last[1]]); n+=1
            out.extend(blk); i=j
        else:
            out.append(L[i]); i+=1
    if n: print('continuation tables re-headed',n)
    return out

# --- RULING 60 SWEEP: press-time only. Source files are never edited. ---
# The object replaces the script; the action only where no object exists.
# Rulings 42, 45, 46 (+ amendments 1-3), 60. Site list measured and classified in W-048.
SUBS = {
 'The_Method_1_6-2.md': [
  ('E(G), recomputed at build;',
   'E(G), recomputed;'),
  ("The harness is *zeno.py*, the state is *.zeno/*, and §2.20's requirement",
   "The work is segmented and its state is preserved, and §2.20's requirement"),
  ('requirement exists as a file rather than an intention: *The Method 1.6 audits.py* runs the whole set',
   'requirement is executed rather than intended: the whole set of twenty runs'),
  ('the uncorrected series the Spectra Compendium carried until Build 9.',
   'the uncorrected series the Spectra Compendium carried until the correction at register 1758.'),
  ("(generated by `register_gen.py` from this book's own source and",
   "(drawn from this book's own source and"),
  ('the source since Build 9, so it cannot be thinned by an edit here.',
   'the source, so it cannot be thinned by an edit here.'),
  ('Recomputed at this build (2026-08-24, `bookindex.py`), over the',
   'Recomputed on 2026-08-24, over the'),
  ('with zero failures (`rclose.py`).',
   'with zero failures (computed).'),
  ('rerun by `tb_audit.py`, 1756)',
   'rerun at register 1756)'),
  ('generated by* `spectra.py` *so it cannot drift,"',
   'generated so it cannot drift,"'),
  ('the table drifted from\n the script, and the script is owed a rebuild against the table.',
   'the table drifted, and that generation is retired: the table above is the source.'),
  ('Regenerated from the text on 2026-08-24 (`index_gen.py`):',
   'Regenerated from the text on 2026-08-24:'),
 ],
 'The_Method_1_6___The_Register-2.md': [
  ('| kind | entries (Build 16) | first reading | what it means |',
   '| kind | entries | first reading | what it means |'),
  ('*The Build 16 column is recomputed from this file by `kinds.py` over the 1,559 entry headings',
   '*The entries column is recomputed from this file over the 1,559 entry headings'),
  ('The first-reading column ( and earlier) was produced by patterns that were never printed',
   'The first-reading column was produced by patterns that were never printed'),
  ('Recomputed from this file by `register_cites.py` (2026-08-26).*',
   'Recomputed from this file (2026-08-26).*'),
  ('\nBuild 9, 2026-08-26. **1629 entries, 1 to 1786** (genesis 1\u201394, superseded 95\u2013164, mature record 165\u20131786).',
   '\n2026-08-26. **1629 entries, 1 to 1786** (genesis 1\u201394, superseded 95\u2013164, mature record 165\u20131786).'),
  ('The generator that once wrote it, `register_gen.py`, was retired at Build 9: entries from 1701 on',
   'The generator that once wrote it was retired: entries from 1701 on'),
  ('What is recomputed from this file at every press is stated where it is printed — the citation counts and the load-bearing table (`register_cites.py`, 1732), the kinds table below (`kinds.py`, 1756), and the entry form (`build.py`, 1744).',
   'What is recomputed from this file is stated where it is printed — the citation counts and the load-bearing table (register 1732), the kinds table below (register 1756), and the entry form (register 1744).'),
  # --- Ruling 46 Amendment 1 + Ruling 60: Register ENTRY BODIES (chat 36) ---
  ('**densities.py* AND *numbers-index.py*',
   '**the six densities* AND *the numbers index*'),
  ('*appendix_audit.py adds eight checks',
   '*Eight checks are added'),
  ('**`appendix_audit.py` FOUND ONE REAL FAULT AND THREE OF ITS OWN.**',
   '**THE EIGHT CHECKS FOUND ONE REAL FAULT AND THREE OF THEIR OWN.**'),
  ('*Generated by `indices.py`, four pages',
   '*Generated, four pages'),
  ('and `spectra.py` still read the book',
   'and the Compendium was still generated from the book'),
  ('*`channels.py` turns collected levels into channels',
   '*Collected levels are turned into channels'),
  ('**`channels.py` was never told it is hydrogenic**',
   '**the hydrogenic case was never distinguished**'),
  ('*`channels.py` splits a configuration string on a letter and divides; it is told nothing about what ℓ means.*',
   '*The defect is got by splitting a configuration string on a letter and dividing; what ℓ means never enters.*'),
  ('*Nothing in `channels.py` is told what ℓ means',
   '*Nothing behind the channel table is told what ℓ means'),
  ('`channel_verify.py` and `isoelectronic.py` regenerate all of it in two commands.',
   'all of it is regenerated in two commands.'),
  ('*Two patterns in `compendium_audit.py` counted',
   '*Two patterns counted'),
  ('*`channel_verify.py` asked whether two defects agreed',
   '*The check asked whether two defects agreed'),
  ('*`mathreg.py` held fifteen',
   '*a list held fifteen'),
  ('`MECHANISMS.md` fourteen — P.termsplit',
   'a second fourteen — P.termsplit'),
  ('an entry — and `QUEUE.md` still named the ten of register 720.',
   'an entry — and a third still named the ten of register 720.'),
  ('**`mech_audit.py` now compares the three and exits non-zero on disagreement.**',
   '**The three are now compared, and disagreement fails the build.**'),
  ('*`channels.py` groups by (core, orbital, term, J) with n absent from the key',
   '*Channels are grouped by (core, orbital, term, J) with n absent from the key'),
  ('**`channels.py` WROTE THE BRACKET COLUMN AS',
   '**THE BRACKET COLUMN WAS WRITTEN AS'),
  ('and `channels.py` supplies neither.*',
   'and neither was supplied.*'),
  (', and `power.py` cannot tell them apart from the counts alone.*',
   ', and the counts alone cannot tell them apart.*'),
  ('and it is a rewrite of `channels.py` rather than a collection.**',
   'and it is a rewrite of the channel table rather than a collection.**'),
  ('*— not a function in `mathverify.py`, not a function anywhere in the source tree.*',
   '*— not a check anywhere on record.*'),
  ('*`mathverify.py` defines sixteen functions and makes **103 rec() assertions',
   '*Sixteen checks are defined, making **103 assertions'),
  ('*`check_audit.py` classifies every field and can be run on any build.*',
   '*Every field is classified, and the classification can be recomputed on any build.*'),
  ('CHANNEL: `channels.py` USES R∞',
   'CHANNEL: THE CHANNEL TABLE USES R∞'),
  ('its absence from `channels.py` until today',
   'its absence from the channel table until today'),
  ('rewritten by every `channels.py` run.',
   'rewritten on every regeneration.'),
  ('`pjj.py` is register 818, `converge_selfsame.py` is 811, `coreblind_fill.py` is 845',
   'the P.jj evidence is register 818, the self-same convergence is 811, the core-blind filling is 845'),
  ('and `mathverify.py` touches 46.**',
   'and the verification touches 46.**'),
  ('and `mathverify.py` checks none of them.**',
   'and none of them is checked.**'),
  ('**`pverify.py` IS WRITTEN, AND ITS FIRST VERSION WAS WRONG',
   '**THE P-FAMILY VERIFICATION IS WRITTEN, AND ITS FIRST VERSION WAS WRONG'),
  ('**`pverify.py` DID WHAT IT WAS BUILT FOR.**',
   '**THE P-FAMILY VERIFICATION DID WHAT IT WAS BUILT FOR.**'),
  ('*No audit read `mathreg.py` as a GRAPH',
   '*No audit read the object list as a GRAPH'),
  ('so a `mathreg.py` that did not load reported ALL TWENTY-FIVE PASS.*',
   'so an object list that did not load reported ALL TWENTY-FIVE PASS.*'),
  ('*`register_gen.py` matched entry labels with',
   '*Entry labels were matched with'),
  ('Stored as `ground.py`.**',
   'Stored in the ground-configuration table.**'),
  ('Saved as domain_protocol.py.*',
   'Recorded as the domain protocol.*'),
  ('*Saved as chem_index.py.*',
   '*Recorded as the chemical index.*'),
  ("the same as ground.py's:",
   "the same as the ground-configuration table's:"),
  ('`contingency.py`, four questions:*',
   'The contingency test, four questions:*'),
  ('**`ladder_index.py` carried it for twenty-eight registers',
   '**the ladder index carried it for twenty-eight registers'),
  ('and `ladder_index2.py` is deleted — two scripts for one index',
   'and the duplicate index is deleted — two indexes for one object'),
  ('*`sixpair_screen.py`.*',
   '*Screened over the six pairs.*'),
  ('*`indices.py`* **computes** *its tower',
   '*The exact triangle* **computes** *its tower'),
  ("`mathreg.py`'s T.tower* **states**",
   'T.tower* **states**'),
  ('*`zeno.py` printed its checkpoint log to stdout while `indices.py` writes its artefact to stdout',
   '*The checkpoint log printed to stdout while the index writes its artefact to stdout'),
  ("And `roundtrip.py`'s normalisation is",
   'And the round-trip normalisation is'),
  ('*`balance.py`.*',
   '*Computed.*'),
  ('*`null_madelung.py`.*',
   '*Measured.*'),
  ('*`scorer.py`, a REBUILD',
   '*A REBUILD'),
  ('`xray_index.py`, `traj_index.py`, the captures',
   'the X-ray index, the trajectory index, the captures'),
  ("*`scorer.py` placed a using each step's OWN corridor — and a corridor is built by `brack.py` FROM the observed entrant",
   "*The scoring placed a using each step's OWN corridor — and a corridor is built FROM the observed entrant"),
  ('and `ground.py` matches all five exactly, so our table is faithful to the source.',
   'and the ground-configuration table matches all five exactly, so it is faithful to the source.'),
  ('`contingency.py` exists in this tree to catch exactly that',
   'The contingency test exists to catch exactly that'),
  ('and is now enforced in `belokolos_spectrum.py` with a comment saying why.',
   'and is now enforced in the ranking, with the reason recorded.'),
  ('Corrected to 0 in `a5c.py` and `merged_triples.py`.*',
   'Corrected to 0 in both counts.*'),
  ('**The counts move: a5c.py goes from six of thirty-five systems closing to FIVE',
   '**The counts move: the A5c systems go from six of thirty-five closing to FIVE'),
  ('merged_triples.py goes from three of forty-six to FOUR',
   'the merged triples go from three of forty-six to FOUR'),
  ('`contingency.py` has been in this tree since it was rebuilt this morning',
   'The contingency test has stood since it was rebuilt this morning'),
  ('preference: `indices.py` says',
   'preference: the composition table says'),
  ("`roundtrip.py`'s normalisation substituted",
   'the round-trip normalisation substituted'),
  ("Applying 1481's correction to `mathreg.py` broke the file twice in succession.",
   "Applying 1481's correction to the object list broke it twice in succession."),
  ('the three that depend on `mathreg.py` loading.',
   'the three that depend on the object list loading.'),
  ('Built as `vi_decorrelate.py`, seeded from vi_best',
   'Built as a decorrelation, seeded from vi_best'),
  ('while `vi_final.py` reports 79 under its own weights 4,1,3,3,1,1',
   'while the weighted count is 79 under weights 4,1,3,3,1,1'),
  ('same answer `sudoku_index.py` returned this morning',
   'same answer the sudoku index returned this morning'),
  ('exactly what `contingency.py` exists to catch, committed in the sentence',
   'exactly what the contingency test exists to catch, committed in the sentence'),
  ('The census in `The_Method_1_6_audits.py` matches phrases',
   'The census matches phrases'),
  ('eighteen ground configurations match `ground.py` exactly',
   'eighteen ground configurations match the ground-configuration table exactly'),
  ('and `ground.py` was written from the aufbau work',
   'and that table was written from the aufbau work'),
  ('`mathreg.py` states it as a RESULT:',
   'The record states it as a RESULT:'),
  ('Built `register_review.py` to find candidates on six mechanical failure modes',
   'Candidates were found on six mechanical failure modes'),
  ('three were not defined in `mathreg.py`.',
   'three were not defined in the object list.'),
  ('`appendix_audit.py` at 595, and seven more.',
   'the appendix checks at 595, and seven more.'),
  ('Built as `sudoku3.py`: three independent determinations of one cell',
   'Built as a three-way index: three independent determinations of one cell'),
  ('`coords.py` labelled every measured cell',
   'Every measured cell was labelled'),
  ('`coords.py` declares every cell above charge 10 improbable',
   'Every cell above charge 10 is declared improbable'),
  ("311 CELLS WERE INHERITED IN `aufbau.py`'s OWN measured() FUNCTION",
   "311 CELLS WERE INHERITED FROM THE AUFBAU WORK'S OWN MEASURED SET"),
  ('`scorer.py` reads the corridor for the CURRENT step',
   'the scoring reads the corridor for the CURRENT step'),
  ('while `brack.py` builds that corridor FROM the observed entrant',
   'while that corridor is built FROM the observed entrant'),
  ('**BUILT AS `trajectory.py`, WITH NOTHING ELSE CHANGED',
   '**BUILT AS A HELD-OUT TRAJECTORY, WITH NOTHING ELSE CHANGED'),
  ('read off `coords.py` rather than assumed',
   'read off the unbounded criterion rather than assumed'),
  ('Built as `termaxis.py` and tested',
   'Built as a term axis and tested'),
  ('and it is now written into `register_review.py`.',
   'and it is now written into the parity check.'),
  ('spectra.py held "101,328" hard-coded in six places and indices.py in one',
   'the spectra generation held "101,328" hard-coded in six places and the index in one'),
  ('mathreg.py and status.py quote 101,328 inside HISTORICAL statements',
   'two of them quote 101,328 inside HISTORICAL statements'),
  ('ONE IS FLAGGED AND NOT FIXED: spectra_F.py asserts that even and odd ranks balance',
   'ONE IS FLAGGED AND NOT FIXED: the rank-balance claim asserts that even and odd ranks balance'),
  ('Reading indices.py at source shows',
   'Reading the index at source shows'),
  ('spectra_F.py asserted even and odd ranks balance across 101,328 cells',
   'The rank-balance claim asserted even and odd ranks balance across 101,328 cells'),
  ('was caught by phase4.py failing its own check.*',
   'was caught by the staging failing its own check.*'),
  ("*`store_gen.py` recovers each stored series' members from the queue2 level tables",
   "*The derivation recovers each stored series' members from the queue2 level tables"),
  ('`store_gen.py` inherits the LIMIT ASSIGNMENT from the store',
   'The derivation inherits the LIMIT ASSIGNMENT from the store'),
  ('`store_gen.py` dropped the 68 before writing',
   'The derivation dropped the 68 before writing'),
  ('*`store_gen.py` rebuilt to implement the two rules already on record',
   '*The derivation rebuilt to implement the two rules already on record'),
  ('*`store_gen.py` gains `limits`, `assign_limit`, `top_member_E`',
   '*The derivation gains a limit set, a limit assignment and a top-member energy'),
  ('Implemented in `store_gen.py` as a FIFTH status',
   'Implemented as a FIFTH status'),
  ('*`store_gen.py` closes the VALUE derivation and inherits the series list from the authored store',
   '*The value derivation closes and the series list is inherited from the authored store'),
  ('Written into `spectra.py` — the generator, not the generated file',
   'Written into the generation — not the generated file'),
  ("`series_gen.py` built from store_gen's own readers",
   'The series construction was built from the same readers'),
  ('`dclose.py` was run on the table as printed',
   'The closure was computed on the table as printed'),
  ('as generated by `mathreg.py` on 2026-08-12',
   'as generated on 2026-08-12'),
  ('Both papers pressed with build.py (no entry-form fix',
   'Both papers pressed (no entry-form fix'),
  ('from a string in build.py that has not been advanced since chat 5',
   'from a string that has not been advanced since chat 5'),
  ('so the convention was found by test (`heii.py`): three limits',
   'so the convention was found by test: three limits'),
  ('(`fig_rerender.py`, data in `fig241_data.json`',
   '(data in `fig241_data.json`'),
  ('`appf.py` now reads the two compendium files and the Register beside the source and rewrites the census sentence',
   'the two compendium files and the Register are now read beside the source, rewriting the census sentence'),
  ("(bracket.py, that bank's register 796)",
   "(that bank's register 796)"),
  ("Run by `run489.py` over `spectra_raw` (92 tables), limits per row with channels.py's LIM as cross-check",
   "Run over `spectra_raw` (92 tables), limits per row with the channel table's LIM as cross-check"),
  ("recomputed by `spectra_count.py`, which now sums the bracket column. `run489.py`, `ruled_bracket.py`, RULING-TOLERANCE-489.md and the run's JSON go to BUILD-10;",
   'recomputed by summing the bracket column. The run, its ruled bracket, its tolerance ruling and its JSON are all retained;'),
  ('and `series_gen.py`, the T8-era selection generator whose header',
   'and the series construction, the T8-era selection whose header'),
  ('`store_gen.py`, which series_gen.py imports, is absent from MANIFEST and delivery',
   'The derivation it depends on is absent from MANIFEST and delivery'),
  ("and store_gen.py lives in restore-point-2_13's 708 files if it ever does.",
   "and it lives in restore-point-2_13's 708 files if it ever does."),
  ("standing in for channels.py's LIM per the MANIFEST's own note that it was extracted from it. `run489.py` exactly as sealed under ruling 26",
   "standing in for the channel table's LIM per the MANIFEST's own note that it was extracted from it, the run exactly as sealed under ruling 26"),
  ('the count paragraph recomputed by `spectra_count.py`: 1,577',
   'the count paragraph recomputed by summing the bracket column: 1,577'),
  ('The press stamps "Build 6" from a string',
   'The press stamps a build label from a string'),
  ('*It is now generated from the headings at build time and cannot disagree.*',
   '*It is now generated from the headings and cannot disagree.*'),
  ('Two are now recomputed at build; §32.1.4.1 names three more',
   'Two are now recomputed; §32.1.4.1 names three more'),
  ('E(G) now recomputes at build rather than printing a failure notice.',
   'E(G) now recomputes rather than printing a failure notice.'),
  ('**All six build-time readouts run for the first time',
   '**All six readouts run for the first time'),
  ("the artefact's numbers are computed at build time rather than typed",
   "the artefact's numbers are computed rather than typed"),
  ('Five of the six are now READ FROM THE FILE at build time (NCELL',
   'Five of the six are now READ FROM THE FILE (NCELL'),
  ('is read from the data companion at build and gated against it',
   'is read from the data companion and gated against it'),
  # --- RULING 62 SUBSTITUTION (chat 43): the Loewdin capture files point at Part VI. ---
  ('`XRAY-L3M5.tsv` is now held:',
   "The Lα₁ rows set out in the Spectra Compendium's § *The X-ray transition energies* are now held:"),
  ('`captures/XRAY-L3M4.tsv` is held, 78 rows Ca to Fm.',
   "The Lα₂ rows set out in the Spectra Compendium's § *The X-ray transition energies* are held, 78 rows Ca to Fm."),
  ('in writing `XRAY-L3M5.tsv` I COPIED',
   'in writing the Lα₁ rows I COPIED'),
  ('XRAY-L3M1.tsv at 88 rows (Ll), XRAY-L3M4.tsv at 78 (Lα2), XRAY-L3M5.tsv at 78 (Lα1), XRAY-L2M1.tsv at 88 (Lη) and XRAY-L2M4.tsv at 78 (Lβ1)',
   "Lℓ at 88 rows, Lα₂ at 78, Lα₁ at 78, Lη at 88 and Lβ₁ at 78 — the first three among the six transitions set out in the Spectra Compendium's § *The X-ray transition energies*, the last two held but not carried into that supply"),
  ('`XRAY-L1N2.tsv` (Lγ2, 67 rows) and `XRAY-L1N3.tsv` (Lγ3, 65 rows) are held',
   "The Lγ₂ rows (67) and the Lγ₃ rows (65), set out in the Spectra Compendium's § *The X-ray transition energies*, are held"),
  ('the six isotope anchors held in `XRAY-KL3.tsv`',
   "the six isotope anchors held in the Kα₁ rows set out in the Spectra Compendium's § *The X-ray transition energies*"),
  ('`captures/LADDER-K-Kr.tsv` is held: 495 rows',
   "The K–Kr ladder set out in the Spectra Compendium's Part VI § *The isoelectronic ladder* is held: 495 rows"),
  ('match `LADDER-K-Kr.tsv` — captured hours earlier',
   "match the K–Kr ladder set out in the Spectra Compendium's Part VI § *The isoelectronic ladder* — captured hours earlier"),
  ('agrees with the held `LADDER-K-Kr.tsv` to 4e-09 eV',
   "agrees with the held K–Kr ladder set out in the Spectra Compendium's Part VI § *The isoelectronic ladder* to 4e-09 eV"),
  ('CORRECTED AND HELD AS `captures/LEVELS-K-I.tsv`, with the corrected row flagged',
   'CORRECTED AND HELD AS a K I level table of its own, with the corrected row flagged'),
  ("form that produced `LADDER-K-Kr.tsv`'s 495 multi-charge rows",
   "form that produced the 495 multi-charge rows of the K–Kr ladder set out in the Spectra Compendium's Part VI § *The isoelectronic ladder*"),
  ('`LADDER-H-Ar-I-III.tsv` in the working root and 100+ level files in `spectra_raw/`',
   "the H–Ar ladder now set out in the Spectra Compendium's Part VI § *The isoelectronic ladder*, and 100+ level tables besides"),
  ('`LADDER-H-Ar-I-III.tsv` — 51 rows, hydrogen through argon at charges 0, +1 and +2 — SITS IN THE WORKING ROOT AND HAS ALL SESSION',
   "THE H–Ar LADDER — 51 rows, hydrogen through argon at charges 0, +1 and +2, set out in the Spectra Compendium's Part VI § *The isoelectronic ladder* — HAS BEEN HELD ALL SESSION"),
  ('Held as `captures/LEVELS-Fe-I.tsv` with the ionisation potential excluded',
   "Held as the Fe I level table set out in the Spectra Compendium's § *The two level tables*, with the ionisation potential excluded"),
  ('Held as `captures/LEVELS-Kr-I.tsv` with those two rows marked DISPUTED in the file',
   "Held as the Kr I level table set out in the Spectra Compendium's § *The two level tables*, with those two rows marked DISPUTED"),
  ('written into `captures/LEVELS-Kr-I.tsv` alongside both refuted values',
   "written into the Kr I level table set out in the Spectra Compendium's § *The two level tables*, alongside both refuted values"),
  ('Held as `captures/AME2020-A9.tsv` with the verification written into the file.',
   "Held as the A = 9 isobar chain set out in the Spectra Compendium's § *The nuclear supply*, with the verification written beside it."),
  ('But `AME2020-A9.tsv` is marked SUPERSEDED',
   "But the A = 9 isobar chain set out in the Spectra Compendium's § *The nuclear supply* is marked SUPERSEDED"),
  ('CAPTURED AS `RADII-actinide.tsv`: 23 rows covering',
   "CAPTURED AS the measured actinide radii set out in the Spectra Compendium's § *The nuclear supply*: 23 rows covering"),
  ('Held as `captures/RADII-Bk-Cf-PREDICTED.tsv`, labelled PREDICTED NOT MEASURED in its first line, so no later session can mistake it for a capture',
   "Held as the predicted berkelium and californium radii set out in the Spectra Compendium's § *The nuclear supply*, labelled PREDICTED NOT MEASURED in the first line, so no later session can mistake them for a capture"),
  ('Captured as `IE-neutral-all.tsv` and cross-checked',
   "Captured as the neutral first ionisation energies set out in the Spectra Compendium's § *The ionisation energies of the neutral atoms*, and cross-checked"),
  ('SIXTY-EIGHT CELLS CAPTURED as `QDEFECT-TOPbase.tsv` — exactly the charge-edge extension',
   "SIXTY-EIGHT CELLS CAPTURED, set out in the Spectra Compendium's § *The quantum defects of the light ladders* — exactly the charge-edge extension"),
  ("captures/NEUTRALS-STAGING.tsv holds 554 staged cells in the index's own schema",
   "the staged cells set out in the Spectra Compendium's § *The staged cells* hold 554 cells in the index's own schema"),
  ('R 1649 named `captures/NEUTRALS-STAGING.tsv` as the source of the 554',
   "R 1649 named the staged cells — set out in the Spectra Compendium's § *The staged cells* — as the source of the 554"),
  ('`spectra_raw` and `MEASUREMENTS.tsv` share NO species',
   'the queue2 level tables and the measurement store share NO species'),
  ("`phase4.py` READS `MEASUREMENTS.tsv`; nothing builds it. The chain queue2 → `captures/NEUTRALS-STAGING.tsv` → `MEASUREMENTS.tsv` survives ONLY AS DATA — neither step's code is in the bank, and `NEUTRALS-STAGING.tsv` is referenced nowhere in the tree but the register",
   "the measurement store is read but nothing builds it. The chain from the queue2 level tables through the staged cells to the measurement store survives ONLY AS DATA — neither step's code is in the bank, and the staged cells are named nowhere but the register. The staged cells are set out in the Spectra Compendium's § *The staged cells*; the measurement store is one of the two bodies that part records as not held"),
  ('MEASUREMENTS.tsv is the repair: many measurements to one cell',
   'The measurement store is the repair: many measurements to one cell'),
  ('keys are duplicated in MEASUREMENTS.tsv',
   'keys are duplicated in the measurement store'),
  ('MEASUREMENTS.tsv has carried it exactly in `term` and `parent`',
   'the measurement store has carried it exactly in its term and parent columns'),
  ('The `mult` column of MEASUREMENTS.tsv is hereby shown',
   'The mult column of the measurement store is hereby shown'),
  ('The authored MEASUREMENTS.tsv is NOT rewritten',
   'The authored measurement store is NOT rewritten'),
  ('The rows are recovered to `SPECTRA-DATA.tsv`, extracted once from the source that held them',
   'The rows are recovered to a store of their own, extracted once from the source that held them'),
  ('The held row in SPECTRA-DATA.tsv reads Ga I',
   'The held row in the published-values store reads Ga I'),
  # --- AMENDMENT 2 / RULING 61 (chat 44): the MECHANISMS.md sites point at Math Compendium P. ---
  ('*`MECHANISMS.md` holds*',
   '*The P family, set out in the Mathematical Compendium at § P. The spectral mechanisms, holds*'),
  ('**`MECHANISMS.md` GAINS P.polar',
   "**THE MATHEMATICAL COMPENDIUM'S P FAMILY GAINS P.polar"),
  ('*Their evidence lives in the analysis scripts and in `MECHANISMS.md`, which is not the same as a verifier that reruns on every build.*',
   '*Their evidence lives in the analysis and in the P family listing at § P. The spectral mechanisms of the Mathematical Compendium, which is not the same as a standing verifier.*'),
  # --- AMENDMENT 2 / RULING 61 (chat 45): Family A, the 'X.md holds it in full' pointers.
  #     Each entry already prints what the file is said to hold; 4749 repoints at register 1442.
  ('*A REBUILD — see PROVENANCE.md.*',
   '*A REBUILD — see register 1442.*'),   # L4749; runs after the scorer.py strip at the REBUILD-prefix pair
  (' — PROVENANCE.md holds the classification for every file in this tree.',
   '.'),   # L4765
  (' LOWDIN-LITERATURE.md holds the full record with attributions.',
   ''),   # L4793
  (' NU-AND-DELTA.md holds the comparison in full.',
   ''),   # L4825
  (' NU-DEACTIVATED.md holds the full classification.',
   ''),   # L4833
  ('`PROVENANCE.md` recorded Λ_xray as fully specified by registers 1378 and 1379',
   'Λ_xray was recorded as fully specified by registers 1378 and 1379'),   # L5419
  # --- AMENDMENT 2 / RULING 61 (chat 45): Family B, the trailing 'census on disk / evidence / raw in' lists. The counts are stated in the entry; the objects are named, the files are not.
  ('never appeared in MEASUREMENTS-DERIVED.tsv to be counted',
   'never appeared in the derived measurement store to be counted'),   # L5619
  (' Census on disk: T9-CENSUS.tsv, T9-RESIDUE.tsv, T9-TERMS.tsv.',
   ' The census, the residue and the term list were each kept.'),   # L5619
  (' Raw in `D-E-FINDINGS-RAW.txt`.',
   ''),   # L5643
  ('MEASUREMENTS-DERIVED.tsv gains six columns',
   'the derived measurement store gains six columns'),   # L5667
  (' Evidence: `T8-CENSUS.txt`, `T8-D1-RECORD.txt`, `MEASUREMENTS-DERIVED.v2.bak.tsv`.',
   ' Evidence: the census, the D1 record, and the pre-run copy of the derived store.'),   # L5667
  (' → 1,564 rows in `captures/READING-LIST-STAGING.tsv`; census in `captures/READING-LIST-CENSUS.txt`.',
   ' → 1,564 rows staged, and censused.'),   # L5687
  # --- AMENDMENT 2 / RULING 61 (chat 45): Families D, E and G. Each entry already prints what the file is said to hold; the object is named in place of the file.
  ('**`QUEUE.md` required this and it is done; all of it is regenerated in two commands.**',
   '**The queue required this and it is done.**'),   # L2121; runs after the channel_verify/isoelectronic strip
  ('RECONSTRUCTIONS held in HANDOFF.md from earlier sessions',
   'RECONSTRUCTIONS carried from earlier sessions'),   # L4609
  ('and DIGEST.md extended with what they hold',
   'and the digest extended with what they hold'),   # L5563
  (' DIGEST.md names them so the gap cannot close over quietly.',
   ' They are named here so the gap cannot close over quietly.'),   # L5563
  ('INDICES.md and SPECTRA.md carry the same mtime because they are generated in one pass',
   'the survey and the index carry the same timestamp because they are generated in one pass'),   # L5567
  # (fig241 'regenerated from the corrected table' handled by the fig_rerender.py pair above; dead duplicate removed, chat 52)
  # --- AMENDMENT 2 / RULING 61 (chat 45): Family C, the author's deliveries and the restore points. The sha256 provenance is kept; the archive filenames become the objects.
  ('`restore-point-1_9c.tar.gz` was cut while the tree was broken',
   'The 1_9c restore point was cut while the tree was broken'),   # L4913
  ('Building `captures/COORDINATES-jK.tsv` — the spectra index rebuilt on',
   'Rebuilding the spectra index on'),   # L5370
  ('delivered as RULING-TOLERANCE-489.md from The Method Löwdin project with spectra_levels_store.zip (sha256 08a6a78c, verified) and then restore-point-2_13.tar.gz itself',
   'delivered from The Method Löwdin project with a levels store (sha256 08a6a78c, verified) and then the 2_13 restore point itself'),   # L5851
  ('*`spectra_selection_and_levels.zip` (sha256 866b0368, cut from restore-point-2_13.tar.gz, sha 80577094, 708 files, on 2026-08-24) answers REQUEST-SPECTRA-DATA.md — this register',
   '*The selection and levels delivery (sha256 866b0368, cut from the 2_13 restore point, sha 80577094, 708 files, on 2026-08-24) answers the data request of this register'),   # L5855
  ("the run's JSON goes to the build as `run489_45.json`.",
   "the run's output goes to the build."),   # L5863
  (', and `LITERATURE.md` records it rather than choosing.',
   ', and it is recorded rather than resolved.'),
  ('*`LITERATURE.md` holds four confirmations',
   '*That standing record holds four confirmations'),
  ('*`LITERATURE.md` names the paper so',
   '*The paper is named here so'),
  ('*`LITERATURE.md` records every comparison attempted — ',
   '*Every comparison attempted is recorded — '),
  ('The best candidate is saved at vi_best.json with its full rule set and profile.',
   'The best candidate is kept with its full rule set and profile.'),
  ('Not knowing vi_best.json existed',
   'Not knowing the best candidate existed'),
  ('seeded from vi_best.json: distance 29',
   'seeded from the best candidate: distance 29'),
  ('the seventeen rules of `vi_best.json` applied',
   'the seventeen rules of the best candidate applied'),
  ('and `vi_best.json` holds it.',
   'and the best candidate holds it.'),
  ('`vi_best.json` already sits in the rare 0.9% region',
   'The best candidate already sits in the rare 0.9% region'),
  ("against vi_best's 25, though vi_best optimises all six columns",
   "against the best candidate's 25, though it optimises all six columns"),
  ('seeded from vi_best per register 591',
   'seeded from the best candidate per register 591'),
  ('*Saved as `vi_best2.json`.',
   '*Kept as the second candidate.'),
  ('— and `QD-CHECK.tsv`, the 37-element compilation from a paper this calculation never touched,',
   '— and the 37-element compilation of asymptotic quantum defects the Spectra Compendium checks against (§ *Published values the coordinates are checked against*), from a paper this calculation never touched,'),
  ('The levels exist and are recorded in `spectra_raw/ArII_highl.tsv`;',
   'The levels exist in the NIST Atomic Spectra Database, the source § *B.1 Sources* records for Ar II;'),
  ('*`spectra_raw/LiIII.tsv` recorded',
   '*The Li III series had recorded'),
  ('*Removed: `.zeno` and `__pycache__`, regenerated on every run; and `CHANNELS-NEW.tsv`, rewritten on every regeneration.',
   '*Removed: the cache and scratch directories, regenerated on every run; and the working copy of the channel table, rewritten on every regeneration.'),
  ('**`captures/READING-LIST.tsv` HOLDS FORTY-FOUR SPECIES',
   '**THE READING LIST HOLDS FORTY-FOUR SPECIES'),
  ('are held in `captures/URLS-SUPPLIED.md` with',
   'are held with'),
  ('**`captures/FETCH-PATHS.tsv` HOLDS ALL SIXTY-ONE',
   '**THE FETCH RECORD HOLDS ALL SIXTY-ONE'),
  ('*Written to `captures/FETCH-BATCHED.txt` beside the per-species `FETCH-PATHS.tsv`, so',
   '*Held in a batched form beside the per-species record, so'),
  ('Built as `captures/FETCH-QUEUE.tsv` with a TODO column',
   'Built as a queue with a TODO column'),
  ('in `captures/FETCH-QUEUE.tsv`, each with a TODO column',
   'in the queue, each with a TODO column'),
  ('**`captures/FETCH-QUEUE.tsv` carries the TODO column',
   '**THE QUEUE carries the TODO column'),
  ('*captures/QUEUE2-INVENTORY.tsv now tallies every capture',
   '*One inventory now tallies every capture'),
  ('and `CHANNELS-NEW.tsv` has carried a column reading',
   'and the channel table (§ *B.2 Channels*) has carried a column reading'),
  ('`The Method 1.6.pdf` was deleted',
   'The built PDF of the book was deleted'),
  ('SPECTRA.md failed its diff',
   'the Spectra Compendium failed its diff'),
  ('lambda-spectra-bound.html renders the (Z,charge) face as it is',
   'the (Z,charge) face was rendered as it is'),
  ('INDICES.md states Λ_spectra',
   'The Index of Indices states Λ_spectra'),
  ('SPECTRA.md and COORDINATES.tsv state',
   'The Spectra Compendium and COORDINATES.tsv state'),
  ('SPECTRA.md\'s "Janet collapse" section dates',
   "The Spectra Compendium's § *The Janet collapse* dates"),
  ('A DIGEST.md is written and banked',
   'A digest is written and banked'),
 ],
 'The_Method_1_6___Mathematical_Compendium-2.md': [
  # --- AMENDMENT 2 / RULING 61 (chat 45): VOLUME-SIDE sites. A reader meets these directly.
  ('the 17 rules of vi_best.json applied',
   'the violation index’s 17 rules applied'),   # L2188
  ('Generated from `mathreg.py` on 2026-08-12; the counts below were recounted',
   'Compiled 2026-08-12; the counts below were recounted'),
  ('`mathverify.py` makes **103 assertions naming 46 of these objects** and recomputes each stated value against the register',
   '**103 assertions name 46 of these objects** and recompute each stated value against the register'),
  ('`check_audit.py` classifies them on any build. Register 849.',
   'The check fields are classified at register 849.'),
  ('Rebuild with `python3 compendium.py > COMPENDIUM.md`. It reads the register, so it cannot',
   'This volume is drawn from the register, so it cannot'),
  ('*M §14.5.9 / twoheur.py; Karp 1972; Johnson 1974*',
   '*M §14.5.9; Karp 1972; Johnson 1974*'),
  ('*M §21.5.5 / allcons.py; Freuder 1978*',
   '*M §21.5.5; Freuder 1978*'),
  ('*protindex.py; Freuder 1978*',
   '*computed; Freuder 1978*'),
  ('*M §20 / stat_lang.py; Deming & Stephan 1940; Csiszar 1975*',
   '*M §20; Deming & Stephan 1940; Csiszar 1975*'),
  ('*close_L.py; Madelung 1936; NIST*',
   '*computed; Madelung 1936; NIST*'),
  ('while indices.py COMPUTES 22275, 64290',
   'while the exact triangle GIVES 22275, 64290'),
  ("The generated table in INDICES.md gives 0 with fraction 0.0000, indices.py says 'Λ₈ composes not at all — four source coordinates against three target', and K.window states the reason",
   'The composition table gives 0 with fraction 0.0000, Λ₈ composes not at all — four source coordinates against three target — and K.window states the reason'),
  ("not yet by `mathverify.py`; wiring them into the book's verifier is a build task, and until it is done",
   "not yet by this volume's own checks; that check is outstanding, and until it is done"),
  ("`ground.py`'s own edge of Z = 108 as the limit",
   "the ground-state table's own edge of Z = 108 as the limit"),
 ],
 'The_Method_1_6___The_Physics_Compendium-2.md': [
  # --- AMENDMENT 2 / RULING 61 (chat 45): VOLUME-SIDE sites. A reader meets these directly.
  ('those are in `MECHANISMS.md` and the Mathematical',
   'those are in the Mathematical'),   # L6
  ('the sixteen mechanisms in `MECHANISMS.md` describe how',
   'the sixteen mechanisms of the Mathematical Compendium’s § P. The spectral mechanisms describe how'),   # L66
  ('Generated from `mathreg.py` and `SPECTRA-DATA.tsv` on 2026-08-12.',
   'Compiled 2026-08-12.'),
  ('`channels.py` writes `bracket = "untested"` for every channel it builds, because running the bracketing method needs measured neighbours and a tolerance and the script supplies neither.',
   'The bracket reads `untested` for every channel built here, because running the bracketing method needs measured neighbours and a tolerance and neither was supplied.'),
 ],
 'The_Method_1_6___The_Index_of_Indices-2.md': [
  ('Generated on 2026-08-15 by `indices.py`.',
   'Compiled 2026-08-15.'),
  ('and it is what `domain_protocol.py` enforces.**',
   'and it is what the closure of the domain axis enforces.**'),
 ],
 'The_Method_1_6___Spectra_Compendium-2.md': [
  # --- AMENDMENT 2 / RULING 61 (chat 45): VOLUME-SIDE sites. A reader meets these directly.
  ('is in `LITERATURE.md`',
   'is in the main volume’s § References'),   # L1022
  ('*`MEASUREMENTS.tsv` and the rows recovered at register',
   '*The measurement store and the rows recovered at register'),   # L1080
  ('*Every figure in this table is read from* `COORDINATES-2.13` *at build by* `coords.py`*, which fails the press if one of them drifts from the file.*',
   '*Every figure in this table is read from the coordinate file set out in § The file, and each is checked against that file.*'),
  ('All bracket figures in this paragraph are recomputed from the table by `spectra_count.py`.',
   'All bracket figures in this paragraph are recomputed from the table above.'),
  ('It claimed the table could not drift from* `spectra.py`; *the table did drift, so* `spectra.py` *is retired: the table above is the source, and every count in the paragraph above it is taken from the table by* `spectra_count.py` * — 596,',
   'It claimed the table was generated and so could not drift; the table did drift, and that generation is retired: the table above is the source, and every count in the paragraph above it is taken from the table — 596,'),
  ('Counts below are read from `COORDINATES-2.13` at build time, not transcribed.*',
   'Counts below are read from the coordinate file set out in § The file, not transcribed.*'),
  ("The register's working entries name the capture files these bodies were held in; the volumes name the bodies. A reader who wants the sodium ladder is sent to §* The isoelectronic ladder*, not to a filename, and that is the whole of the difference.",
   'The register and the volumes both name the bodies. A reader who wants the sodium ladder is sent to §* The isoelectronic ladder*, not to a filename.'),
  ('* **19**, 527 and 1995, *JPCRD* **24**, 1803.\n## B.2 Channels',
   '* **19**, 527 and 1995, *JPCRD* **24**, 1803.\n\n## B.2 Channels'),
  ('onciled.* Registers 630–631; 1578; 1699–1700.\n## B.3 Flagged channels',
   'onciled.* Registers 630–631; 1578; 1699–1700.\n\n## B.3 Flagged channels'),
 ],
}

def sweep(src,t):
    n=0
    for a,b in SUBS.get(src,[]):
        assert t.count(a)==1, 'SWEEP ANCHOR %r in %s occurs %d times' % (a[:60],src,t.count(a))
        t=t.replace(a,b); n+=1
    if n: print('sweep:',src,n,'substitutions')
    return t

def build(src,out,title,strip_contents=False,toc_depth=2,fix_entries=False):
    t=open(B+src,encoding='utf-8').read()
    t=sweep(src,t)
    L=t.splitlines()
    # first H1 becomes the document title
    h1=[i for i,l in enumerate(L) if l.startswith('# ')]
    if h1 and h1[0]<5: L[h1[0]]=''   # a volume whose file opens with its title
    if strip_contents:
        # remove the book's literal contents block: lines between 'Contents' heading and next '## ' body heading
        s=[i for i,l in enumerate(L) if re.match(r'^\s*#{0,3}\s*(Contents|CONTENTS)\s*$',l)]
        if s:
            i=s[0]; parts=[k for k,l in enumerate(L) if k>i and re.match(r'^# PART 0',l)]
            j=parts[1] if len(parts)>1 else i+1
            L=L[:i]+L[j:]; print('contents block removed',i,j)
    if fix_entries:
        L=fix_bodies(L)
    L=cont_tables(L)
    L=displays(L)
    L=[re.sub(r'^!\[[^\]]*\]\((figures[^)]*)\)\s*$', r'![](\1)', l) for l in L]   # drop the image alt line: the caption paragraph carries the figure number
    L=[esc_us(l) for l in L]
    md='\n'.join(L)
    meta=f'---\ntitle: "{title}"\nauthor: "Matthew Lach"\ndate: "2026-08-26"\n---\n\n'
    open('tmp.md','w',encoding='utf-8').write(meta+md)
    cmd=['pandoc','tmp.md','-o',out,'--from','markdown+pipe_tables+smart']+(['--toc','--toc-depth',str(toc_depth)] if toc_depth else [])+['--resource-path',B,'--reference-doc','ref.docx']
    r=subprocess.run(cmd,capture_output=True,text=True); print(r.stderr[-1500:])
    shrink_wide_tables(out)
    titlepage_break(out)
    print(out,os.path.getsize(out))
def titlepage_break(docx):
    # INDEPENDENT TITLE PAGE (chat 52, ruling: "All compendia need an independent title page").
    # The break is placed BEFORE THE FIRST HEADING, not after the pandoc Date paragraph. This is the
    # original-input design ("the first heading becomes the title page", registers 272/456/1737): every
    # paragraph before the first heading is title-page matter and belongs on the title folio. For the
    # four compendia and the Register that is just the pandoc Title/Author/Date block. For the MAIN
    # volume the source additionally carries its own title block (The Method / the F expression / the
    # Lach Cylinder subtitle / author) which pandoc emits as body paragraphs BEFORE the first heading;
    # breaking after Date there split the metadata title onto its own page and left the book's real
    # title block on page 2 — a redundant double title page (chat 52 finding). Breaking before the
    # first heading keeps the whole title block, metadata and book title alike, on one title page for
    # all six volumes uniformly. Both anchors asserted (G0f): a first heading must exist and be unique
    # as the break site, and no title-block break may already be present; absent either, the press
    # stops rather than shipping a heading-less or double-broken volume.
    import zipfile,shutil,re
    tmp=docx+'.tp'
    with zipfile.ZipFile(docx) as zin:
        doc=zin.read('word/document.xml').decode('utf-8')
        names=zin.namelist()
    brk='<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    if brk in doc:
        raise SystemExit('titlepage_break: a page break already present at the title block in %s'%docx)
    # the first heading paragraph is the body boundary: match a <w:p> whose pStyle is Heading1/2/3
    hpat=re.compile(r'<w:p\b[^>]*>(?:(?!</w:p>).)*?<w:pStyle w:val="Heading[1-3]"\s*/>', re.S)
    m=hpat.search(doc)
    if not m:
        raise SystemExit('titlepage_break: no heading paragraph found to bound the title page in %s'%docx)
    # insert the break at the START of that first heading paragraph
    doc2=doc[:m.start()]+brk+doc[m.start():]
    assert doc2.count(brk)==1, 'titlepage_break: break not inserted exactly once'
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data=zin.read(item.filename)
            if item.filename=='word/document.xml': data=doc2.encode('utf-8')
            zout.writestr(item,data)
    shutil.move(tmp,docx)
    print('title page break inserted')
def shrink_wide_tables(docx,min_cols=8,sz=15):
    # wide tables (8+ columns) are set at 7.5pt so their rows do not wrap mid-word
    import zipfile,shutil
    tmp=docx+'.tmp'
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data=zin.read(item.filename)
            if item.filename=='word/document.xml':
                x=data.decode('utf-8'); n=0
                def fix(m):
                    nonlocal n
                    t=m.group(0)
                    first=re.search(r'<w:tr[ >].*?</w:tr>',t,re.S)
                    if not first or first.group(0).count('<w:tc>')+first.group(0).count('<w:tc ')<min_cols: return t
                    n+=1
                    t=re.sub(r'<w:r>(<w:rPr>)?',lambda k:'<w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/>'+('' if k.group(1) else '</w:rPr>'),t)
                    t=re.sub(r'<w:rPr><w:sz w:val="\d+"/><w:szCs w:val="\d+"/><w:rPr>',lambda k:k.group(0).replace('<w:rPr><w:rPr>','<w:rPr>').replace('/><w:rPr>','/>'),t)
                    # column widths proportional to each column's longest cell text
                    rows=re.findall(r'<w:tr[ >].*?</w:tr>',t,re.S); ncol=None; lens=[]; words=[]; num=[]
                    for ri,row in enumerate(rows):
                        cells=re.findall(r'<w:tc>.*?</w:tc>|<w:tc .*?</w:tc>',row,re.S)
                        if ncol is None: ncol=len(cells); lens=[[] for _ in range(ncol)]; words=[2]*ncol; num=[True]*ncol
                        for ci,c in enumerate(cells[:ncol]):
                            txt=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',c))
                            lens[ci].append(min(len(txt),28)); words[ci]=max(words[ci],max((len(w) for w in txt.split()),default=0))
                            if ri>0 and txt.strip() and not re.match(r'^[\d+\-\u2013.,%()/ ]*$',txt): num[ci]=False
                    def p90(v): v=sorted(v); return v[min(len(v)-1,int(len(v)*0.9))]
                    mx=[max(p90(v),w) for v,w in zip(lens,words)]
                    total=9360
                    for sz2 in (15,14,13,12):
                        sz=sz2                           # half-points: 7.5pt down to 6pt
                        cw=95*sz/15                                    # ~95 twips per character at 7.5pt
                        need=[m*cw+130 for m in mx]; floor=[w*cw+130 for w in words]
                        fixed=sum(n for n,k in zip(need,num) if k); flex=sum(n for n,k in zip(need,num) if not k)
                        scale=(total-fixed)/flex if fixed+flex>total and flex else 1.0
                        widths=[int(n if k else max(n*scale,f)) for n,k,f in zip(need,num,floor)]
                        if sum(widths)<=total: break
                    if sum(widths)>total: widths=[int(w*total/sum(widths)) for w in widths]
                    t=re.sub(r'<w:sz w:val="15"/><w:szCs w:val="15"/>','<w:sz w:val="%d"/><w:szCs w:val="%d"/>'%(sz,sz),t)
                    print('cols',mx,'numeric',sum(num),'sz',sz,'scale',round(scale,2),'sum',sum(widths))
                    grid=''.join('<w:gridCol w:w="%d"/>'%w for w in widths)
                    t=re.sub(r'<w:tblGrid>.*?</w:tblGrid>','<w:tblGrid>'+grid+'</w:tblGrid>',t,flags=re.S)
                    tblpr=('<w:tblPr><w:tblStyle w:val="Table"/><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="start"/>'
                           '<w:tblLayout w:type="fixed"/><w:tblCellMar><w:left w:w="40" w:type="dxa"/><w:right w:w="40" w:type="dxa"/></w:tblCellMar>'
                           '<w:tblLook w:firstRow="1" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0" w:val="0020"/></w:tblPr>')%total
                    t=re.sub(r'<w:tblPr>.*?</w:tblPr>',tblpr,t,count=1,flags=re.S)
                    def fixrow(rm):
                        wi=iter(widths)
                        return re.sub(r'<w:tcPr ?/>|<w:tcPr>.*?</w:tcPr>',lambda k:'<w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr>'%next(wi,400),rm.group(0),flags=re.S)
                    t=re.sub(r'<w:tr[ >].*?</w:tr>',fixrow,t,flags=re.S)
                    t=re.sub(r'<w:pPr>(<w:pStyle [^>]*/>)?',lambda k:'<w:pPr>'+(k.group(1) or '')+'<w:spacing w:before="0" w:after="0"/>',t)
                    return t
                x=re.sub(r'<w:tbl>.*?</w:tbl>',fix,x,flags=re.S)
                print('wide tables shrunk',n); data=x.encode('utf-8')
            zout.writestr(item,data)
    shutil.move(tmp,docx)
if __name__=='__main__':
    src,out,title=sys.argv[1:4]; kw=dict(strip_contents=('strip' in sys.argv),fix_entries=('fix' in sys.argv),toc_depth=int(sys.argv[-1]) if sys.argv[-1].isdigit() else 2)
    # ---- COORDS GATE (chat 19, W-013; scoped to Spectra by Ruling 65, chat 51, W-086). Closes SPEC-02.
    # A volume that CLAIMS its counts are read from the data companion at build time must prove it
    # at build time. The instrument is the SPECTRA one (usage: coords.py <spectra.md>) and can only
    # reconcile the Spectra Compendium's Part 0 table. W-079: since chat 24 the Register QUOTES Spectra's
    # build-time claim as subject matter, so the claim-trigger alone fired on the Register too, where
    # there is no Part 0 table, and aborted its press. Ruling 65 scopes the gate to the Spectra volume,
    # identified by its own H1 title — intrinsic, found by content not filename, and independent of the
    # Part 0 table, so a later break there still fires the gate and the instrument still exits loud (the
    # property the rejected 'require the read section' narrowing lacked, W-079).
    # A missing companion is a FAILURE, not a skip: absent the file the volume's claim is false.
    _t=open(src,encoding='utf-8').read()
    _is_spectra=bool(re.search(r'(?m)^# THE METHOD 1\.6 — SPECTRA COMPENDIUM$',_t))
    if _is_spectra and 'COORDINATES-2.13' in _t and re.search(r'read from[^.\n]{0,60}at build',_t):
        print('coords gate: this volume claims a build-time reading of COORDINATES-2.13 — verifying')
        _g=subprocess.run(['python3','coords.py',src]); print('coords gate: exit',_g.returncode)
        if _g.returncode!=0:
            sys.exit('BUILD ABORTED — coords.py gate FAILED on %s. The volume states its counts are '
                     'read from COORDINATES-2.13 at build time; they do not reconcile. Fix the '
                     'figures or withdraw the claim. No press was made.'%src)
    build(src,out,title,**kw)
    if 'pages' in sys.argv:   # print index: press, map headings to pages, rewrite Contents and Index, press again until the map is stable
        import os,hashlib
        outdir=os.path.dirname(out) or '.'; pdf=out[:-5]+'.pdf'; paged=src[:-3]+'.pages.md'; prev=None
        # SWEEP REACHES THE DELIVERED ARTEFACT (chat 49). index_pages.py reads the UNSWEPT source and
        # writes `paged`; build(paged) then looked SUBS up under the PAGED filename, which has no entry,
        # so every volume pressed with `pages` was delivered from unswept text. The first build IS swept
        # but is only the page-mapping pass and is overwritten. Measured in the object: main's own
        # anchors 'E(G), recomputed at build;' and 'zeno.py' both survived into main.pdf. Aliasing the
        # key makes the same pairs apply to the rebuild. sweep() still asserts each anchor exactly once,
        # so a pair that index_pages.py or appf.py has disturbed stops the press rather than passing.
        SUBS[paged]=SUBS.get(src,[])
        subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,out],capture_output=True)
        for k in range(3):
            subprocess.run(['python3','index_pages.py',src,pdf,paged,str(kw['toc_depth'])],check=True)
            # RULING 63 (chat 40) restores this call. Ruling 30's ground expired when Appendix F was
            # rebuilt on a new domain. appf.py recomputes the Register's SUBJECT-MATTER entry count,
            # gated at the front-matter boundary so editorial entries cannot enter it, and writes it
            # to the seventeen sites in main that state it. It asserts every anchor; a stale anchor
            # stops the press rather than passing silently.
            # VOLUME GATE (chat 49). Ruling 63's call sits in the GENERIC page loop, but appf.py is a
            # MAIN-volume instrument: it indexes from '# PART 0' and its --write asserts the fifteen
            # word-form sites plus two numeric anchors, all of which exist in main alone. Unconditional,
            # it raised IndexError on Math, Physics, IoI and Spectra and aborted four of the six presses.
            # The trigger is the CLAIM found by CONTENT, not the filename — W-013's coords-gate design,
            # so a rename cannot bypass it and a volume the instrument cannot read is never handed to it.
            # This narrows Ruling 63's call to the volume Ruling 63 names. It does not widen it.
            if '# PART 0' in open(paged,encoding='utf-8').read():
                subprocess.run(['python3','appf.py',paged,'--write'],check=True)
            h=hashlib.md5(open(paged,'rb').read()).hexdigest()
            if h==prev: print('page map stable after',k,'re-press(es)'); break
            prev=h; build(paged,out,title,**dict(kw,strip_contents=False,toc_depth=0))
            subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,out],capture_output=True)
        # POST-LOOP VERIFICATION (chat 16). The loop compares at the TOP of an iteration, so a press
        # that reaches its fixed point on the LAST build converges and never reports it. This re-derives
        # the map from the pressed PDF and states the result. It changes no output, only the report.
        chk=paged+'.chk'
        subprocess.run(['python3','index_pages.py',src,pdf,chk,str(kw['toc_depth'])],check=True)
        ok=open(chk,'rb').read()==open(paged,'rb').read()
        os.remove(chk)
        print('PAGE MAP CONVERGED' if ok else 'PAGE MAP NOT CONVERGED — another re-press needed')
