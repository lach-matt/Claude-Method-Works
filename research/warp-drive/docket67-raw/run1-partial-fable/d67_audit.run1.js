export const meta = {
  name: 'docket-67-foundations-audit',
  description: "DOCKET 67 (M-D65-3): audit every external result a refusal on the warp board rests on -- extract per owner, dedup, audit each at source with re-derivation and data-at-publication vs current, three adversarial lenses per audit, then compute what a non-STANDS grade reopens",
  phases: [ { title: 'Extract' }, { title: 'Merge' }, { title: 'Audit' }, { title: 'Verify' }, { title: 'Reopen' } ],
}
const ROOT = '/home/user/Claude-Method-Works'
const WD = ROOT + '/research/warp-drive'
const SP = '/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad'
const SCR = SP + '/d67'
const M_WORDS = "I didn't expect proving warp theory travel easy, but I'm starting suspect that some of the previously established math from outside art may be inaccurate or incomplete, or even wrong. My justification is that some previous physicists may have all lacked certain data"
const HOUSE = `
DOCKET 67 -- THE FOUNDATIONS AUDIT, on M's warp board (research/warp-drive/), opened on M's ruling M-D65-3 and run
now, after DOCKET 65 and before DOCKET 66. M's words, verbatim: "${M_WORDS}". The question put to M: "Should I open
a docket auditing the external results the board's refusals rest on (theorem / measurement / extrapolation;
hypotheses, the data each used, re-derived or machine-checked, graded STANDS / NARROWED / WRONG / DATA-DEPENDENT)?"
M's rules: everything accurate and true; every limitation a NAMED hypothesis; over-representation avoided BOTH ways
(never in M's favour either -- a misprint is a discrepancy, not a refutation; fluctuation.py is the tree's own
precedent: 'the discrepancies are recorded', nothing repaired, 'MUST NOT be quoted as errors in the journal version
until it is read'); nothing DECLARED -- nothing less than computed, measured or READ at source; evidence either way,
nothing presumed; a claim that cannot be checked here is OPEN, never flattened to STANDS or WRONG.
research/ is original work; the corpus under drive/ and method/ is never touched. DO NOT edit any file under
${WD} in this workflow: write only under ${SCR}/ (mkdir -p as needed). Never commit, push, stash or reset.
Tools: papers are READ at source through the alphaXiv MCP tools (load with ToolSearch 'select:mcp__alphaXiv__answer_pdf_queries,mcp__alphaXiv__get_paper_content,mcp__alphaXiv__discover_papers'):
answer_pdf_queries(paper=<arXiv id or title>, queries=[every question at once]) returns page text; get_paper_content(url, fullText=true)
returns the full text; discover_papers for later literature (2 calls per message). Pre-arXiv classics (Geroch 1967,
Tipler 1977, Birkhoff, Misner-Sharp 1964, Klinkhamer-Manton 1984, 't Hooft 1976) are read through an arXiv review
or a later paper that restates them exactly -- say which, and mark the classic NAMED-NOT-READ if only restated.
Machine checks: python3 with sympy; z3 via 'pip install z3-solver' if not present (pypi is on the proxy allowlist).
`
const OWNERS = ['certify', 'foliation', 'driven', 'drivensource', 'bounds', 'tolman', 'nonstatic', 'overturn', 'excite',
  'higgs', 'latticectc', 'noise', 'transit', 'formation', 'stockgate', 'linstab', 'massform', 'candidates', 'branelink',
  'warpfolder', 'hpscentre', 'fewsterteo', 'achievable', 'axial', 'spec', 'create', 'qeihps', 'phase1', 'concentric',
  'composite', 'seatindex', 'fluctuation', 'stability', 'stock', 'throatmass', 'wall', 'address', 'permute', 'anec',
  'anecscope', 'arrival', 'specthm', 'ledger']
const EXTRACT_SCHEMA = { type: 'object', properties: {
  owner: { type: 'string' }, exists: { type: 'boolean' },
  results: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string', description: 'arXiv id if any (e.g. gr-qc/9406053, 1208.5399), else a short slug like geroch-1967-topology-change' },
    name: { type: 'string' }, kind: { type: 'string', enum: ['theorem', 'bound', 'measurement', 'computation', 'extrapolation', 'definition'] },
    statement_as_used: { type: 'string', description: "quoted from the owner, with file:line" },
    hypotheses_as_used: { type: 'array', items: { type: 'string' } },
    status_word: { type: 'string', description: "the owner's own word: READ / CITED / NAMED-NOT-READ / RECORD PIN / none" },
    rests_on_it: { type: 'array', items: { type: 'string' }, description: 'ledger row ids / specthm class ids / facts names whose verdict USES it (not merely cites it)' },
    context_only: { type: 'boolean', description: 'true if the owner only cites it and no verdict rests on it' },
    data_used: { type: 'array', items: { type: 'string' }, description: 'numerical inputs the result depends on, as the owner records them (e.g. m_h = 125.13 GeV READ)' },
    where: { type: 'string' } },
    required: ['key', 'name', 'kind', 'statement_as_used', 'hypotheses_as_used', 'status_word', 'rests_on_it', 'context_only', 'where'] } } },
  required: ['owner', 'exists', 'results'] }
phase('Extract')
log(`extracting external results from ${OWNERS.length} owners`)
const extracted = await parallel(OWNERS.map(o => () => agent(HOUSE + `
YOUR STAGE: EXTRACT, owner ${o}.py in ${WD} (if the file does not exist, return exists=false and no results). Read the
whole file. List EVERY external result -- a theorem, bound, measured datum, published computation or extrapolation
from OUTSIDE this tree -- that this owner uses, quoting the statement AS THE OWNER STATES IT (file:line) and the
hypotheses as used, the owner's own status word, and which verdicts REST on it (ledger rows this owner holds -- run
'python3 -c "import ledger; ..."' to see which rows name ${o} in their owner column -- and specthm classes/facts if
specthm's facts() or escapes name this owner). Mark context_only=true where no verdict uses it. Include the numerical
data each result depends on as the owner records it. Do not skip a result because it looks standard (Birkhoff,
Raychaudhuri, the positive-energy theorem, the no-communication theorem, Bekenstein's bound all count). Nothing
graded here -- this stage only lists.`, { label: 'extract:' + o, phase: 'Extract', effort: 'medium', schema: EXTRACT_SCHEMA })))
const all = extracted.filter(Boolean).flatMap(e => e.exists ? e.results.map(r => ({ ...r, owner: e.owner })) : [])
const missing = extracted.filter(Boolean).filter(e => !e.exists).map(e => e.owner)
if (missing.length) log(`owners not found (skipped): ${missing.join(', ')}`)
log(`${all.length} result occurrences across ${extracted.filter(Boolean).length} owners`)
// plain-code dedup by key (arXiv id or slug), keeping every occurrence's provenance
const byKey = {}
for (const r of all) { const k = r.key.trim().toLowerCase().replace(/^arxiv:/, ''); (byKey[k] = byKey[k] || []).push(r) }
const groups = Object.entries(byKey).map(([key, occ]) => ({ key, occurrences: occ }))
log(`${groups.length} distinct keys before the merge`)
phase('Merge')
// the merge agent sees only a compact roster (key, names, owners, kinds); plain code applies its fold map
const uniq = xs => Array.from(new Set(xs.filter(Boolean)))
const roster = groups.map(g => ({ key: g.key, names: uniq(g.occurrences.map(o => o.name)).slice(0, 4),
  kinds: uniq(g.occurrences.map(o => o.kind)), owners: uniq(g.occurrences.map(o => o.owner)),
  any_verdict_rests: g.occurrences.some(o => !o.context_only) }))
const MERGE_SCHEMA = { type: 'object', properties: {
  folds: { type: 'array', items: { type: 'object', properties: { into: { type: 'string' }, from: { type: 'array', items: { type: 'string' } }, why: { type: 'string' } }, required: ['into', 'from', 'why'] } },
  splits: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, note: { type: 'string' } }, required: ['key', 'note'] }, description: 'keys that hold two distinct results under one id (e.g. Borde theorem vs Borde escapes) -- noted, audited as one with the note' } },
  required: ['folds', 'splits'] }
const merged = await agent(HOUSE + `
YOUR STAGE: MERGE. Below is a roster of ${roster.length} keys of extracted external results (${all.length} occurrences),
grouped by exact key. Return the FOLD MAP: groups that are the SAME external result under different keys (a slug
and its arXiv id; 'Fewster-Roman QEI' and gr-qc/0209036; the same theorem cited from two papers -- fold INTO the
primary source's key). Do NOT fold distinct results that merely share a paper (Borde's theorem and Borde's three
escapes are two results; if one key already holds two, list it under splits with a note). Fold nothing you are not
sure of: two keys left separate cost one extra audit; two results folded wrongly lose one. Read the owners' files
under ${WD} where a name is ambiguous.
ROSTER:
` + JSON.stringify(roster), { label: 'merge', phase: 'Merge', effort: 'high', schema: MERGE_SCHEMA })
const into = {}
for (const f of (merged ? merged.folds : [])) for (const k of f.from) into[k.toLowerCase()] = f.into.toLowerCase()
const folded = {}
for (const g of groups) { const k = into[g.key] || g.key; (folded[k] = folded[k] || []).push(...g.occurrences) }
const splitNote = {}
for (const s of (merged ? merged.splits : [])) splitNote[s.key.toLowerCase()] = s.note
const canonicalAll = Object.entries(folded).map(([key, occ]) => ({
  key, name: uniq(occ.map(o => o.name))[0], names: uniq(occ.map(o => o.name)), kind: uniq(occ.map(o => o.kind))[0],
  merged_keys: uniq(occ.map(o => o.key.toLowerCase())).filter(k => k !== key),
  statements_as_used: occ.map(o => ({ owner: o.owner, where: o.where, statement: o.statement_as_used, hypotheses: o.hypotheses_as_used, status_word: o.status_word })),
  rests_on_it: uniq(occ.flatMap(o => o.rests_on_it)), owners: uniq(occ.map(o => o.owner)),
  data_used: uniq(occ.flatMap(o => o.data_used || [])), context_only: occ.every(o => o.context_only),
  split_note: splitNote[key] || '' }))
const canonical = canonicalAll.filter(c => !c.context_only)
const droppedContext = canonicalAll.filter(c => c.context_only).map(c => c.key)
log(`${canonical.length} canonical external results to audit (${merged ? merged.folds.length : 0} folds applied); ${droppedContext.length} context-only dropped: ${droppedContext.join(', ')}`)
phase('Audit')
const AUDIT_SCHEMA = { type: 'object', properties: {
  key: { type: 'string' }, name: { type: 'string' },
  source: { type: 'object', properties: { located: { type: 'string' }, read_status: { type: 'string', enum: ['READ', 'READ-VIA-RESTATEMENT', 'NAMED-NOT-READ'] }, via: { type: 'string' } }, required: ['located', 'read_status', 'via'] },
  published_statement: { type: 'string' }, published_hypotheses: { type: 'array', items: { type: 'string' } },
  hypothesis_drift: { type: 'array', items: { type: 'string' }, description: 'each hypothesis the tree drops, adds or weakens relative to the source, with the site' },
  data_at_publication: { type: 'array', items: { type: 'object', properties: { quantity: { type: 'string' }, value_then: { type: 'string' }, value_now: { type: 'string' }, source_now: { type: 'string' }, moves_conclusion: { type: 'string' } }, required: ['quantity', 'value_then', 'value_now', 'source_now', 'moves_conclusion'] } },
  rederivation: { type: 'object', properties: { method: { type: 'string', enum: ['sympy', 'z3', 'numeric', 'by-hand-checked-numerically', 'none-possible'] }, script_path: { type: 'string' }, outcome: { type: 'string' }, agrees_with_source: { type: 'string', enum: ['yes', 'no', 'partly', 'not-run'] } }, required: ['method', 'script_path', 'outcome', 'agrees_with_source'] },
  later_literature: { type: 'array', items: { type: 'object', properties: { ref: { type: 'string' }, effect: { type: 'string', enum: ['confirms', 'narrows', 'contradicts', 'extends', 'contested'] }, what: { type: 'string' }, read_status: { type: 'string' } }, required: ['ref', 'effect', 'what', 'read_status'] } },
  lacked_data: { type: 'string', description: "M's hypothesis tested for this result: what data the authors had, what came later, and whether it changes the conclusion -- evidence either way" },
  grade: { type: 'string', enum: ['STANDS', 'NARROWED', 'WRONG', 'DATA-DEPENDENT', 'OPEN'] },
  grade_evidence: { type: 'string' }, what_would_change_the_grade: { type: 'string' },
  reverify_command: { type: 'string' }, report_path: { type: 'string' } },
  required: ['key', 'name', 'source', 'published_statement', 'published_hypotheses', 'hypothesis_drift', 'data_at_publication', 'rederivation', 'later_literature', 'lacked_data', 'grade', 'grade_evidence', 'what_would_change_the_grade', 'reverify_command', 'report_path'] }
const VERDICT = { type: 'object', properties: { lens: { type: 'string' }, refuted: { type: 'boolean' }, proposed_grade: { type: 'string', enum: ['STANDS', 'NARROWED', 'WRONG', 'DATA-DEPENDENT', 'OPEN'] }, reason: { type: 'string' }, commands_run: { type: 'array', items: { type: 'string' } } }, required: ['lens', 'refuted', 'proposed_grade', 'reason', 'commands_run'] }
const LENSES = [
  ['refute', `LENS: REFUTE THE GRADE. Try to refute the audit's grade in EITHER direction: a STANDS that a hypothesis
drift or a moved datum undermines; a NARROWED/WRONG/DATA-DEPENDENT that rests on a misreading, a misprint, a
restatement rather than the source, or a computation the auditor got wrong. Read the source yourself (alphaXiv).`],
  ['rederive', `LENS: RE-RUN THE RE-DERIVATION. Run the audit's script_path yourself (copy to your own scratch dir
first); check its encoding against the published statement (is what it checks the theorem, or a toy of it?); run
the vacuity guard (does the check pass with the hypotheses negated?). If method is none-possible, say whether a
finite check was in fact possible and try one.`],
  ['data', `LENS: THE DATA CLAIM. Check every data_at_publication row and the lacked_data answer at source (PDG
reviews on arXiv, the paper's own numbers): are value_then and value_now right, and does moves_conclusion follow?
Is M's hypothesis for THIS result answered with evidence either way, not presumed?`],
]
const audited = await pipeline(canonical,
  (r, item, i) => agent(HOUSE + `
YOUR STAGE: AUDIT one external result (${i + 1} of ${canonical.length}). THE RESULT AS THE TREE USES IT:
` + JSON.stringify(r) + `
Do, in order: (1) LOCATE and READ the source at alphaXiv (batch every question into one answer_pdf_queries call:
exact statement, every hypothesis, the data/inputs used, the year and what was known then); for a classic with no
arXiv copy, read the exact restatement in a later arXiv paper or review and mark READ-VIA-RESTATEMENT. (2) Quote
the PUBLISHED statement and hypotheses; list every HYPOTHESIS DRIFT between the source and the tree's use (dropped,
added, weakened), each with the owner's file:line. (3) DATA: every numerical input the result's conclusion depends
on -- the value the authors used and the current value (PDG 2024/2025 review on arXiv, or the measurement paper),
with whether the move changes the conclusion (compute it if it is a formula). (4) RE-DERIVE or MACHINE-CHECK what
is finite or closed-form: write ${SCR}/rederive/${r.key.replace(/[^A-Za-z0-9._-]/g, '_')}.py (sympy/z3/numeric),
run it, record the outcome; if genuinely nothing is checkable, say exactly why. (5) LATER LITERATURE: one
discover_papers call for work that narrows, contradicts or extends it; read what matters. (6) M's hypothesis for
THIS result: what data the authors lacked, and whether having it changes the conclusion -- evidence either way.
(7) GRADE: STANDS (statement and hypotheses as used, re-derivation agrees, no moved datum moves the conclusion);
NARROWED (holds on a smaller class than the tree uses, or a hypothesis the tree drops); WRONG (a refuting
counterexample or a computed contradiction, SHOWN here -- a misprint is a discrepancy, not WRONG); DATA-DEPENDENT
(the conclusion moves with a datum that has moved or is contested); OPEN (not readable or not checkable here).
Every grade carries its evidence and a reverify_command. Write the full report to
${SCR}/audits/${r.key.replace(/[^A-Za-z0-9._-]/g, '_')}.json and return it.`,
    { label: 'audit:' + r.key, phase: 'Audit', effort: 'high', schema: AUDIT_SCHEMA }),
  (a, item) => a ? parallel(LENSES.map(([k, p]) => () => agent(HOUSE + `
YOU ARE AN ADVERSARIAL VERIFIER of one audit. Make NO edits under ${WD}; write only under ${SCR}/verify/${k}/.
THE RESULT AS THE TREE USES IT: ` + JSON.stringify(item) + `
THE AUDIT: ` + JSON.stringify(a) + `
` + p + ` Default to refuted=true only with a stated reason; propose the grade the evidence supports.`,
    { label: 'verify:' + k + ':' + item.key, phase: 'Verify', effort: 'high', schema: VERDICT }))).then(vs => {
      const votes = vs.filter(Boolean)
      const refutes = votes.filter(v => v.refuted)
      const agreed = refutes.length <= 1
      const grades = votes.map(v => v.proposed_grade)
      const final = agreed ? a.grade : (grades.every(g => g === grades[0]) ? grades[0] : 'OPEN')
      return { ...a, verifiers: votes, agreed, final_grade: final, disputed: !agreed }
    }) : null)
const done = audited.filter(Boolean)
const tally = {}
for (const a of done) tally[a.final_grade] = (tally[a.final_grade] || 0) + 1
log(`audits: ${done.length}; grades ${JSON.stringify(tally)}; disputed ${done.filter(a => a.disputed).length}`)
phase('Reopen')
const REOPEN_SCHEMA = { type: 'object', properties: { reopens: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, final_grade: { type: 'string' }, verdicts_resting: { type: 'array', items: { type: 'string' } },
  classes_reopened: { type: 'array', items: { type: 'string' } }, how_computed: { type: 'string' } },
  required: ['key', 'final_grade', 'verdicts_resting', 'classes_reopened', 'how_computed'] } },
  summary_path: { type: 'string' } }, required: ['reopens', 'summary_path'] }
const nonstands = done.filter(a => a.final_grade !== 'STANDS')
const reopen = nonstands.length ? await agent(HOUSE + `
YOUR STAGE: REOPEN. For each audited result whose final grade is not STANDS (below), COMPUTE -- never type -- what
its failing would reopen: ask specthm (python3 -c 'import specthm; ...' -- escapes(), _reopen(), facts(), the
classes' verdicts and their unsat cores) and ledger (which rows' verdicts rest on it, from the extract's
rests_on_it) which classes and rows fall back to OPEN if the fact that rests on this result is dropped; for a
result that is not a specthm fact, say so and name the ledger rows only. Write the summary, with the commands, to
${SCR}/reopen.json.
NON-STANDS RESULTS: ` + JSON.stringify(nonstands.map(a => ({ key: a.key, name: a.name, final_grade: a.final_grade, grade_evidence: a.grade_evidence, rests_on_it: (canonical.find(c => c.key === a.key) || {}).rests_on_it })))
, { label: 'reopen', phase: 'Reopen', effort: 'high', schema: REOPEN_SCHEMA }) : { reopens: [], summary_path: '' }
return { owners_missing: missing, occurrences: all.length, canonical: canonical.length, dropped_context_only: droppedContext, folds: merged ? merged.folds : [], tally, audits: done, reopen }
