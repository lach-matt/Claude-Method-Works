---
name: science-databases
description: "Routing table for scientific databases and literature sources from this container: which tool reaches each one (Firecrawl, TinyFish, Exa, alphaXiv, SciSpace, Consensus, Wiley, Wolfram, BigQuery, or direct HTTPS to the public GCS/S3 buckets), the exact URL pattern, a tested example, quotas, and which need a free key. Covers arXiv, INSPIRE, ADS, OpenAlex, Crossref, Semantic Scholar, zbMATH, OSTI, NTRS, SciPost, SCOAP3, Living Reviews, historical sources; OEIS, LMFDB, DLMF, nLab, Wolfram Functions, MaRDI, Metamath/Lean search; CODATA, NIST ASD, PDG, IAEA, NNDC; SIMBAD, VizieR, NED, Gaia, Exoplanet Archive, MAST, HEASARC, IRSA, Planck, LAMBDA, SDSS, DESI, JPL Horizons, GWOSC, GraceDB; Zenodo, Figshare, HEPData, CERN Open Data, Hugging Face, Kaggle. Use it before fetching any paper, constant or catalogue value, and whenever a READ (verbatim quote + page) is needed."
---

# science-databases: where each source is reachable from here

Quick lookup: `python3 .claude/skills/science-databases/dbroute.py <name>`. For example, `dbroute.py inspire`,
`dbroute.py gaia` or `dbroute.py --field astro`. It prints the tool, the URL pattern and the tested example from an
embedded table.

All of this comes from the tool sweep of 2026-10-09 (`research/warp-drive/toolsweep/toolsweep_result.json`).
Items flagged `excluded` there, and everything that depends on GitHub content, are left out.

## Ground rules

1. **From the container itself, the egress proxy refuses almost every science host** with a 403 on CONNECT. That
   includes arxiv.org, inspirehep.net, NIST, CDS, IPAC, MAST, GWOSC and more.
   - Do not try to route container traffic around it: no alternate hosts, no plain HTTP, no tunnels.
   - Python API clients such as `arxiv`, `astroquery`, `pyvo`, `ads`, `habanero` and `gwosc` all install fine,
     and all of them fail at the proxy.
2. **Three direct routes are allowed** and need no connector:
   - `https://storage.googleapis.com/arxiv-dataset/...`: every arXiv PDF, by version;
   - `https://openalex.s3.amazonaws.com/...`: the OpenAlex snapshot;
   - the **AWS Open Data astronomy buckets** at `https://<bucket>.s3.amazonaws.com/...`, read anonymously.
3. **Everything else goes through the session's MCP connectors**, which are separate services the user
   connected. Load each with ToolSearch (`select:<name>`) before the first call.
   - `mcp__Firecrawl__firecrawl_scrape` with `formats=["rawHtml"]` is the workhorse for JSON APIs. The JSON body
     comes back in `rawHtml`, so `json.loads` it.
   - `mcp__TinyFish__fetch_content` (`format="markdown"`, `links=False`, `image_links=False`,
     `page_metadata=False`) is the fallback. It is the primary route for TAP/ADQL services, the arXiv API and
     Semantic Scholar.
   - `mcp__Exa__web_fetch_exa` is best for HTML reference pages (DLMF, nLab, EoM, ProofWiki, Springer/LRR) and
     some plain JSON.
   - The built-in **WebFetch is broken here** (`getaddrinfo ENOTFOUND`). The built-in WebSearch works.
     `mcp__Parallel_Search__web_fetch` was often rate-limited (429).
4. **Large connector results** (above about 100k characters) are auto-saved to a file under
   `/root/.claude/projects/.../tool-results/`. Parse that file in Python; do not page it into context.
   This route moved the Planck PR3 TT spectrum (2,507 multipoles), the full GWTC catalogue and MPC `NEA.txt`.
5. **Connectors cannot send request headers.** APIs that authenticate by header stay unusable even with a free
   key: NASA ADS (Bearer token), Materials Project native (`X-API-KEY`), Semantic Scholar's keyed tier and Kaggle
   downloads. Keys passed in the query string do work: Springer Nature `api_key=`, NASA `api_key=DEMO_KEY`.

## READs: the board needs the source text itself

A READ is a **verbatim quote with its page (or equation) number, taken from the source text**. A summary, an
abstract, a search snippet or a model's paraphrase is never a READ.

| route | gives | READ-grade? |
|---|---|---|
| GCS `arxiv-dataset` PDF → `sci run lit pdftotext -layout` / pymupdf (record the md5) | **full text, true page numbers** | **yes: the preferred route** |
| `arxiv.org/e-print/<id>` via Firecrawl rawHtml (single-file gzip sources) → TexSoup | **author's LaTeX source** (no page numbers; cite the equation label) | yes, for equations |
| `ar5iv.labs.arxiv.org/html/<id>` via Firecrawl rawHtml → `alttext="..."` | **exact LaTeX of every equation** | yes, for equations (section, not page) |
| `mcp__alphaXiv__answer_pdf_queries` | clean page text, page-located | yes, then confirm against the PDF |
| `mcp__Firecrawl__firecrawl_research_read_paper` | passages with exact LaTeX | usually; confirm the page against the PDF |
| `mcp__Wiley_Scholar_Gateway__search_wiley_fulltext` | full-text passages, Wiley/Hindawi only | passage yes; locate the page |
| Exa on `link.springer.com` (Living Reviews, OA Springer) | full HTML text | yes (section-located) |
| SCOAP3 JATS XML/PDF via TinyFish | full OA text: JHEP, PRD, EPJC, PLB, NPB | yes |
| NTRS `/downloads/*.txt`, Gutenberg `.tex`, de.wikisource, IA `_djvu.txt`, GDZ/IA page screenshots → tesseract | historical full text and page images | yes (OCR text needs proofreading against the image) |
| `alphaXiv get_paper_content` | full text with broken intra-word spacing ("spacetim e") | **no**: unsafe for quotes |
| arXiv API, INSPIRE, OpenAlex, Crossref, Semantic Scholar, zbMATH, ADS, DOAJ, Consensus, SciSpace | metadata, abstracts, citation graphs | **no**: use them to find papers, then READ the PDF |
| APS / IOP landing pages | abstract and metadata only (paywalled) | **no**. The free route is DOI → Unpaywall → arXiv id → GCS PDF |

## Literature

| source | route | URL pattern / call | tested example (2026-10-09) | notes |
|---|---|---|---|---|
| **arXiv PDFs (bulk)** | **direct HTTPS** | list: `https://storage.googleapis.com/storage/v1/b/arxiv-dataset/o?prefix=arxiv/arxiv/pdf/YYMM/YYMM.NNNNN&fields=items(name,size)`; get: `https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/YYMM/YYMM.NNNNNvN.pdf`; old ids: `arxiv/<arch>/pdf/YYMM/NNNNNNNvN.pdf` (e.g. `arxiv/hep-th/pdf/9906/9906064v1.pdf`) | `gr-qc/0009013v1.pdf`, 96,087 B, md5 ed8a162b…; p.8 "it violates all three energy conditions (weak, dominant and strong [3])" | current to about 2609.*; metadata dump `metadata-v5/arxiv-metadata-oai.json` is 4.5 GB |
| arXiv search API | TinyFish | `https://export.arxiv.org/api/query?search_query=ti:%22warp%20drive%22+AND+cat:gr-qc&max_results=20` | totalResults 120; 2401.15136v2, 2207.06458v1 | Firecrawl times out (60 s); about 30 s latency |
| arXiv OAI-PMH | TinyFish | `https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:<id>&metadataPrefix=arXiv` | gr-qc/0009013 → journal-ref CQG 11:L73, DOI | |
| arXiv abs / listing / PDF page | Exa (abs); Firecrawl (`parsers=["pdf"]`, list pages) | `https://arxiv.org/abs/<id>`; `https://arxiv.org/list/gr-qc/new` | abs text clean; list gr-qc/new: 76 entries | |
| arXiv LaTeX source | Firecrawl rawHtml | `https://arxiv.org/e-print/<id>` | hep-th/9906064 → `\documentstyle[12pt]{article}`, 16 equations via TexSoup | single-file gzip only; multi-file tarballs likely fail |
| ar5iv (equations) | Firecrawl rawHtml | `https://ar5iv.labs.arxiv.org/html/<id>` then `re.findall(r'alttext="([^"]*)"')` | `ds^{2}=e^{-2k|y|}\eta_{\mu\nu}dx^{\mu}dx^{\nu}+dy^{2}` | TinyFish strips alttext |
| alphaXiv | `mcp__alphaXiv__answer_pdf_queries`, `discover_papers` | `answer_pdf_queries(paper='gr-qc/9910076', queries=['Exact statement of Eq. (17)'])` | Shiromizu–Maeda–Sasaki eq. (17) verbatim | avoid `get_paper_content` for quotes |
| Firecrawl research index | `firecrawl_research_search_papers` / `read_paper` | `read_paper(paperId='arxiv:gr-qc/9910076', question=..., k=4)` | eqs. (18)–(19) in LaTeX | arXiv + PubMed/bioRxiv |
| **INSPIRE-HEP** | Firecrawl rawHtml (TinyFish also works) | `https://inspirehep.net/api/literature?q=refersto%3Aarxiv%3A<id>&size=25&fields=titles,arxiv_eprints,citation_count`; `&format=bibtex` | `t warp drive` → 78 hits | the best citation graph for hep-th/gr-qc |
| **NASA ADS** | **NEEDS-FREE-KEY, and unusable here** | `api.adsabs.harvard.edu/v1/search/query` | 401 "Missing Authorization in headers" | header token; connectors cannot send it. Use INSPIRE/OpenAlex/Crossref. Key: ui.adsabs.harvard.edu → Account → API Token (usable only from a machine with egress) |
| **OpenAlex API** | Firecrawl rawHtml | `https://api.openalex.org/works?search=<q>&per-page=50&select=id,doi,title,publication_year,cited_by_count`; `filter=cites:W…` | alcubierre warp drive → 676 works | now metered (cost_usd in meta) |
| **OpenAlex snapshot** | **direct HTTPS** | `https://openalex.s3.amazonaws.com/?list-type=2&prefix=data/jsonl/works/&delimiter=/`; files `data/jsonl/<entity>/updated_date=…/part_NNNN.gz` | release 2026-09-23; 476M works (659 GB) | bulk use only; mind disk |
| **Crossref** | Firecrawl rawHtml (Parallel also works) | `https://api.crossref.org/works/<DOI>`; `works?query=<q>&rows=20&select=DOI,title` | 10.1088/0264-9381/11/5/001: is-referenced-by 377 | |
| **Semantic Scholar** | TinyFish | `https://api.semanticscholar.org/graph/v1/paper/arXiv:<id>/citations?fields=title,year&limit=100` | warp drive search total 1137 | Firecrawl gets 429; the keyed tier uses a header (unusable) |
| **zbMATH Open** | Firecrawl rawHtml | `https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22Randall-Sundrum%22&results_per_page=10` (also `cc%3A83E15`) | 144 results; Garriga–Tanaka PRL 84, Zbl 0949.83019 | some records are license-restricted; formula search is not available |
| **OSTI.gov** | Firecrawl rawHtml (XML) | `https://www.osti.gov/api/v1/records?title=<q>&rows=20` | "Semiclassical instability of dynamical warp drives", PRD 79 124017 | `q=` is ignored; use `title=` |
| **NASA NTRS** | Firecrawl rawHtml | `https://ntrs.nasa.gov/api/citations/search?q=<q>&page.size=20`; full text `…/api/citations/<id>/downloads/<id>.txt` | "Warp Field Mechanics 101" full text | |
| **SciPost** | Firecrawl rawHtml | `https://scipost.org/api/publications/?format=json&search=<q>` | gravity → 190 | search matches broadly |
| **SCOAP3** (JHEP/PRD/EPJC/PLB/NPB OA) | TinyFish | `https://repo.scoap3.org/api/records/?q=<q>`, then fetch `_files[].file` (XML/PDF) the same way | 88,016 records; JATS ArticleTitle verbatim | phrase queries not honoured; Firecrawl times out |
| **Living Reviews in Relativity** | Exa | `https://link.springer.com/article/10.12942/lrr-YYYY-N` (`maxCharacters=200000`) | Maartens & Koyama lrr-2010-5 §1 verbatim | |
| Springer Nature OA API | **NEEDS-FREE-KEY** (works via Firecrawl once keyed) | `https://api.springernature.com/openaccess/json?q=title:%22<q>%22&api_key=KEY` | 401 without key | free key at dev.springernature.com; it goes in the URL, so the connector works |
| Unpaywall | Firecrawl rawHtml | `https://api.unpaywall.org/v2/<DOI>?email=<you>` | PRD 63 084013 → arxiv hep-th/0011176 | DOI → OA copy → GCS PDF |
| OpenCitations | Firecrawl rawHtml | `https://api.opencitations.net/index/v2/citations/doi:<DOI>` (or `citation-count`) | Alcubierre 1994: 401 | |
| DataCite, DOAJ, HAL, Europe PMC, PubMed, dblp, ORCID | Firecrawl rawHtml | `api.datacite.org/dois?query=`, `doaj.org/api/search/articles/<q>`, `api.archives-ouvertes.fr/search/?q=…&wt=json`, `www.ebi.ac.uk/europepmc/webservices/rest/search?…&format=json`, `eutils…/esearch.fcgi?…&retmode=json`, `dblp.org/search/publ/api?q=…&format=json`, `pub.orcid.org/v3.0/<ORCID>/works` | all returned 200 JSON | ROR goes via TinyFish (`api.ror.org/v2/organizations?query=`) |
| OpenAIRE Graph v1 | Exa | `https://api.openaire.eu/graph/v1/researchProducts?search=<q>&pageSize=10` | brane world → 4,442 | the legacy endpoint fails |
| INIS (IAEA), OSF Preprints | TinyFish | `https://inis.iaea.org/api/records?q=<q>`; `https://api.osf.io/v2/preprints/?filter[subjects]=…` | warp → 898 | |
| CERN Document Server | Firecrawl with `proxy="stealth"`, `waitFor=8000` | `https://cds.cern.ch/search?p=<q>&of=recjson&rg=10&ot=title,authors,files` | brane → CERN-TH-2026-169 | an Anubis bot wall blocks plain fetches |
| Google Scholar | Firecrawl markdown (occasional only) | `https://scholar.google.com/scholar?q=<q>` | Alcubierre 1994 "Cited by 1199" | no API; against Google's terms, so a cross-check only |
| APS / IOP landing pages | Firecrawl `formats=["summary"]` | `https://journals.aps.org/prd/abstract/<DOI>` | abstract and citation_pdf_url | metadata only |
| Semantic search | `mcp__Consensus__search`, `mcp__SciSpace__search-papers` | plain-language query | both found Shiromizu–Maeda–Sasaki and Maeda–Wands | Consensus: at most 3 calls at a time; cite with its numbered refs and include its sign-up line |
| Wiley full text | `mcp__Wiley_Scholar_Gateway__search_wiley_fulltext(query=..., topN=10)` | full natural-language question | Varieschi–Burstein 2013 eq. 15 T^00 verbatim | Wiley/Hindawi titles only |
| **Historical sources** | | | | |
| de.wikisource (Einstein 1915 …) | Firecrawl markdown | `https://de.wikisource.org/wiki/Die_Feldgleichungen_der_Gravitation` | full text, Sitzungsber. 1915 pp. 844–847 | equations flattened from MathML |
| Internet Archive | TinyFish (advancedsearch, `inside.php`); Firecrawl rawHtml (`_djvu.txt`); Firecrawl screenshot (page images) | `archive.org/advancedsearch.php?q=…&fl[]=identifier&output=json`; `archive.org/download/<ID>/<ID>_djvu.txt`; `archive.org/details/<ID>/page/n<LEAF>/mode/1up` (`waitFor=20000`) | Kaluza 1921, leaf 446, legible pp. 967–968 | OCR text has errors: proofread against the image (`sci run lit tesseract -l deu`) |
| GDZ Göttingen (Math. Ann. …) | Firecrawl rawHtml (METS); screenshot of the TIFY viewer (`waitFor=15000`) | `https://gdz.sub.uni-goettingen.de/mets/<PPN>.mets.xml` | Math. Ann. 79: 33 titles | viewer is JS-only |
| EuDML / Numdam / Gallica / HathiTrust | Firecrawl (EuDML record pages, Numdam OAI); TinyFish (Gallica SRU, HathiTrust bib API) | `eudml.org/doc/<id>`; `www.numdam.org/oai/?verb=ListRecords&metadataPrefix=oai_dc&set=AIHP`; `gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=dc.title%20all%20%22…%22`; `catalog.hathitrust.org/api/volumes/brief/oclc/<n>.json` | all returned records | HathiTrust full-text search is bot-blocked |
| Project Gutenberg / Open Library | Firecrawl rawHtml | `https://gutendex.com/books?search=<q>`; `https://openlibrary.org/search.json?q=<q>` | Einstein "Relativity" incl. a `.tex` format | |

## Mathematics

| source | route | URL pattern / call | tested example | notes |
|---|---|---|---|---|
| **OEIS** | Firecrawl rawHtml | `https://oeis.org/search?fmt=json&q=1,1,2,5,14,42,132` (add `maxAge=0`) | A000108 Catalan numbers | about 178k characters; query narrowly. The raw GitHub data mirror is excluded |
| **LMFDB** | Firecrawl rawHtml | `https://www.lmfdb.org/api/<table>/?<field>=<v>&_format=json&_fields=...` | `ec_curvedata` 37.a1: rank 1, conductor 37, ainvs [0,0,1,-1,0] | `_limit` ignored (100 rows; page with `_offset`) |
| **DLMF** | Exa (text) or Firecrawl rawHtml (TeX annotations) | `https://dlmf.nist.gov/<chap>.<sec>` | 10.2.1 Bessel equation in TeX | for exact quotes extract `<annotation encoding="application/x-tex">` |
| **nLab**, Encyclopedia of Mathematics, ProofWiki, MathWorld | Exa | `https://ncatlab.org/nlab/show/<Page>` etc. | Kaluza-Klein mechanism page | MathWorld equations are images (come back empty) |
| **Wolfram Functions** | Firecrawl markdown | ID-style URL `https://functions.wolfram.com/07.23.02.0001.01` | 2F1 series definition | path-style URLs 404 |
| **MaRDI portal** | TinyFish | `https://portal.mardi4nfdi.de/w/api.php?action=wbsearchentities&search=<q>&language=en&format=json` | Riemann zeta function → Q-ids | SPARQL endpoint unreachable through every connector |
| **Metamath / Lean / Mizar / AFP search** | Firecrawl | Loogle `https://loogle.lean-lang.org/json?q=Real.sqrt%2C%20%22mul_self%22` (rawHtml); LeanSearch `https://leansearch.net/?q=<words>` (markdown, `waitFor=5000`); Metamath `us.metamath.org/mpeuni/<thm>.html`; Mizar `mizar.uwb.edu.pl/version/current/html/<art>.html` | Loogle: 388 declarations; Metamath sqrt2irr | lemma *search* only; Mathlib cannot be installed here. Local Metamath set.mm: `sci install provers` |
| Stack Exchange (Physics SE, MathOverflow) | Firecrawl rawHtml | `https://api.stackexchange.com/2.3/search/advanced?q=<q>&site=physics&sort=votes&filter=withbody` | quota 300/day | the shared connector IP shares that quota |
| TPTP | TinyFish | `https://tptp.org/cgi-bin/SeeTPTP?Category=Problems&Domain=<D>&File=<F>.p` | SET001-1.p full file | |
| CaltechAUTHORS (Bateman volumes) | Firecrawl rawHtml | `https://authors.library.caltech.edu/api/records?q=%22Higher%20Transcendental%20Functions%22` | 3 volumes, open | PDFs are 37–71 MB |
| Wolfram (CAS, xAct) | `mcp__Wolfram__WolframLanguageEvaluator` | stateless: load and compute in one call. xAct from `www.xact.es`; set ``xAct`xPerm`$xpermQ=False`` before xCoba | xAct Schwarzschild RicciScalar = 0 in 5.7 s | label "computed (Wolfram 15.0.1, connector)". FeynCalc is excluded (GitHub download) |
| Magma online calculator | `mcp__TinyFish__run_web_automation` | `http://magma.maths.usyd.edu.au/calc/`; ask for every output line verbatim | Cole's factorisation of 2^67−1 | 120 s limit; may time out at 60 s, so poll `get_run` |

## Constants, atomic and nuclear data

Offline first: `sci install data` gives the same numbers with no connector.
- CODATA 2022: `scipy.constants` and `astropy.constants.codata2022`;
- PDG 2026: `pdg`, which reports GeV;
- `particle`, which reports MeV;
- `mendeleev`, which has NIST ionisation energies;
- `radioactivedecay`: ICRP-107, AME2020 and NUBASE2020;
- `xraydb`.

| source | route | URL pattern | tested example | notes |
|---|---|---|---|---|
| **CODATA** (NIST allascii) | Exa | `https://physics.nist.gov/cuu/Constants/Table/allascii.txt` (`maxCharacters=200000`) | 2022 adjustment, atomic mass constant 1.660 539 068 92e-27 kg | offline: `scipy.constants.physical_constants` |
| **NIST ASD** (levels, lines, IEs) | TinyFish | `https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=H-He&units=1&format=2&order=0&at_num_out=on&sp_name_out=on&ion_charge_out=on&el_name_out=on&e_out=0&unc_out=on&submit=Retrieve+Data`; lines: `…/ASD/lines1.pl?…` | H I 13.598434599702(12) eV; Hα 656.270970 nm | Exa returns 500 on lines1.pl |
| NIST atomic weights / isotopes | TinyFish | `https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Fe&ascii=ascii2&isotype=some` | 56Fe 55.93493633(49) | |
| NIST Chemistry WebBook | TinyFish | `https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=1` | water ΔfH°gas −241.826 kJ/mol | |
| **PDG** | offline `pdg` package; Exa (REST API); TinyFish (Listings) | `https://pdgapi.lbl.gov/summaries/S008M` | π± mass 139.5703909836813 MeV (2026) | |
| **IAEA LiveChart** (ENSDF) | Exa | `https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=135xe` | Xe-135 t½ 9.14 h | |
| IAEA AMDC AME2020 | TinyFish | `https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt` | 308k-character table (auto-saved file) | offline: `radioactivedecay` bundles AME2020 |
| **NNDC NuDat3 / ENSDF** | TinyFish | `https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=135XE&unc=nds` | adopted levels, Q(β−)=1165 keV | KAERI is blocked by its own firewall |
| Wolfram curated data | `mcp__Wolfram__WolframLanguageEvaluator` | `IsotopeData["Xenon135","HalfLife"]`, `ElementData`, `PlanetData` | Xe-135 9.14 h | electron mass 0.51099892 MeV is **less precise than CODATA 2022**; do not use it for constants |
| PubChem, Materials Project OPTIMADE, AFLOW | TinyFish | `pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/<n>/property/MolecularWeight/JSON`; `optimade.materialsproject.org/v1/structures?filter=…`; `aflow.org/API/aflux/?species(Si),…` | all returned data | MP's native API is NEEDS-FREE-KEY and the key is a header, so it cannot be used: use OPTIMADE |

## Astronomy, cosmology and gravitational waves

TAP services: send ADQL as `sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=<url-encoded>` through TinyFish.

| source | route | URL pattern | tested example | notes |
|---|---|---|---|---|
| **SIMBAD** | Exa | `https://simbad.cds.unistra.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&format=json&query=SELECT TOP 1 main_id,ra,dec,otype FROM basic WHERE main_id='M  31'` | M 31: 10.6847, 41.2688, AGN | |
| **VizieR** / CDS files / Sesame | TinyFish | `https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=I/239/hip_main&-out=HIP,Vmag,Plx&-out.max=3`; `cdsarc.cds.unistra.fr/ftp/<cat>/ReadMe`; `cds.unistra.fr/cgi-bin/nph-sesame/-oxp/SNV?M31` | Hipparcos rows | |
| **NED** | TinyFish | `https://ned.ipac.caltech.edu/srs/ObjectLookup?name=M31` | z = −0.000991 | |
| **Gaia** (ESA TAP) | TinyFish | `https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT TOP 2 source_id,parallax FROM gaiadr3.gaia_source WHERE parallax>700` | Proxima Cen 768.07 mas | Gaia DR3 files are also in the AWS buckets |
| **NASA Exoplanet Archive** | TinyFish, `format=csv` | `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+10+pl_name,pl_orbper+from+pscomppars&format=csv` | Kepler-1513 b … | Exa fails on JSON; exoplanet.eu is down |
| **MAST** | TinyFish (`format="html"`); AWS bucket `stpubdata` for files | `https://mast.stsci.edu/api/v0/invoke?request=<url-encoded JSON>` | M31 name lookup | the TinyFish markup is stripped, so values run together |
| **HEASARC** | TinyFish (Xamin TAP); AWS bucket `nasa-heasarc` | `https://heasarc.gsfc.nasa.gov/xamin/vo/tap/sync?REQUEST=doQuery&LANG=ADQL&QUERY=…` | ROSAT rows | no CSV; the VOTable is base64 BINARY, so decode it |
| **IRSA** (2MASS, WISE, Spitzer) | TinyFish; AWS buckets `nasa-irsa-*`, `ipac-irsa-ztf` | `https://irsa.ipac.caltech.edu/TAP/sync?QUERY=SELECT+TOP+2+designation,ra,dec+FROM+fp_psc&FORMAT=csv` | 2MASS PSC rows | |
| **Planck** (PR3 via the IRSA mirror) | TinyFish | `https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-full_R3.01.txt` | 2,507 multipoles, peak ℓ = 232 (auto-saved, `np.loadtxt`) | PLA (pla.esac.esa.int) data downloads unverified |
| **LAMBDA** | TinyFish; AWS bucket `nasa-lambda` | `https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/wmap_tt_spectrum_9yr_v5.txt` | WMAP 9-yr TT | |
| **SDSS** SkyServer DR18 | TinyFish | `https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?cmd=<SQL>&format=json` | photoobj rows | |
| **DESI** (DR1 via NOIRLab Data Lab) | TinyFish | `https://datalab.noirlab.edu/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT TOP 2 targetid,z,spectype FROM desi_dr1.zpix`; listing `data.desi.lbl.gov/public/dr1/` | z = 0.2727 GALAXY | SPARCL endpoint 404 |
| ESO / CADC TAP, ESA Sky | TinyFish | `archive.eso.org/tap_obs/sync?…`; `ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/argus/sync?…`; `sky.esa.int/esasky-tap/tap/sync?…` | ObsCore rows | |
| **JPL Horizons** / SBDB / CAD | TinyFish (Horizons, CAD); Exa (SBDB) | `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='499'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='VECTORS'&START_TIME='2026-01-01'&STOP_TIME='2026-01-02'&STEP_SIZE='1d'`; `ssd-api.jpl.nasa.gov/sbdb.api?sstr=Ceres` | Mars GM 42828.375662 km³/s² | offline ephemeris: de421 + jplephem (pip) |
| Minor Planet Center | TinyFish | `https://www.minorplanetcenter.net/iau/MPCORB/NEA.txt` | 42,702 lines (auto-saved) | |
| NASA open APIs | TinyFish with `api_key=DEMO_KEY` in the URL | `https://api.nasa.gov/neo/rest/v1/feed?start_date=…&end_date=…&api_key=DEMO_KEY` | 11 NEOs | DEMO_KEY is rate-limited; a free personal key from api.nasa.gov also goes in the URL |
| **GWOSC** (event catalogue) | TinyFish (full catalogue); Firecrawl rawHtml (single event) | `https://gwosc.org/eventapi/json/GWTC/`; `https://gwosc.org/eventapi/json/GWTC-1-confident/GW150914/v3/` | 391 event-versions to GWTC-5.0; GW150914 m1 35.6, m2 30.6 M☉, 440 Mpc | bulk strain (HDF5/GWF) is not practical |
| **GraceDB** (public superevents) | TinyFish | `https://gracedb.ligo.org/api/superevents/?query=far%3C1e-10&count=5&format=json` | 117 rows; S251117dq | |
| ATNF pulsar catalogue | TinyFish | `https://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?version=2.6.1&pulsar_names=J0737-3039A&ephemeris=short&submit_ephemeris=Get+Ephemeris&style=Long+with+last+digit+error&no_value=*&state=query` | J0737-3039A OMDOT 16.8995 deg/yr, PBDOT −1.252e-12 | VizieR B/psr lacks OMDOT/PBDOT |
| **AWS Open Data astro buckets** | **direct HTTPS** (anonymous) | `https://<bucket>.s3.amazonaws.com/?list-type=2&prefix=<p>&delimiter=/`, objects at `https://<bucket>.s3.amazonaws.com/<key>`; buckets: `stpubdata` (TESS/HST/JWST/Kepler/GALEX/PanSTARRS), `nasa-heasarc`, `nasa-irsa-wise`, `nasa-irsa-euclid-q1`, `nasa-irsa-spherex`, `ipac-irsa-ztf`, `nasa-lambda` | TESS, HST/COS, Chandra, WISE, Euclid Q1, SPHEREx, ZTF and WMAP FITS opened with astropy | arxiv.s3 is requester-pays (403) |
| **BigQuery public datasets** | `mcp__Google_Cloud_BigQuery__*` | `list_table_ids(projectId='bigquery-public-data', datasetId='wise_all_sky_data_release')`; also `blackhole_database`, `noaa_goes16`, `moon_phases` | metadata calls only | **SQL bills the user's GCP project** (1 TB/month free). Ask before running queries |
| NOAA SWPC / NCEI | TinyFish | `https://services.swpc.noaa.gov/json/planetary_k_index_1m.json` | Kp index | |

## Data hubs

| source | route | URL pattern | tested example | notes |
|---|---|---|---|---|
| **Zenodo** | Firecrawl rawHtml or TinyFish | `https://zenodo.org/api/records?q=<q>&size=10` | "CMB lensing likelihood data: ACT, SPT-3G, and Planck" | many recent "warp drive" uploads are unrefereed |
| **Figshare** | Firecrawl rawHtml, lookup by id only | `https://api.figshare.com/v2/articles/<id>` | search via GET ignored | search needs POST, so it is not available |
| **HEPData** | Firecrawl rawHtml (`onlyMainContent=False`) | `https://www.hepdata.net/search/?q=<q>&format=json&size=10`; tables `…/download/table/<ins>/<Table>/csv` | higgs → 515 | TinyFish is bot-blocked |
| **CERN Open Data** | TinyFish | `https://opendata.cern.ch/api/records/?q=<q>&size=5` | recid 5209 "Higgs to two photons from 2011" | files on `root://eospublic` cannot be fetched |
| **Hugging Face** datasets | TinyFish | `https://huggingface.co/api/datasets?search=<q>&limit=5` | physics datasets list | listing only; `huggingface_hub` is blocked |
| **Kaggle** | TinyFish (listing) | `https://www.kaggle.com/api/v1/datasets/list?search=<q>` | "The Gravitational Waves Discovery Data" | download is NEEDS-FREE-KEY plus a header, so not usable here |
| Google Dataset Search, data.nasa.gov (CKAN) | TinyFish | `datasetsearch.research.google.com/search?query=<q>`; `data.nasa.gov/api/3/action/package_search?q=<q>&rows=5` | GWTC-3 on zenodo; 15 exoplanet packages | |

## Free keys (and whether they help here)

| service | how the user gets one | usable from here? |
|---|---|---|
| NASA ADS | ui.adsabs.harvard.edu → log in → Account → Settings → API Token | **no**: Bearer header; use INSPIRE/OpenAlex/Crossref |
| Springer Nature OA API | register at dev.springernature.com → Applications → key | **yes**: `api_key=` goes in the URL (Firecrawl) |
| Materials Project | materialsproject.org → log in → Dashboard → API key | **no**: `X-API-KEY` header; use OPTIMADE (no key) |
| Lens.org | lens.org → account → request Scholarly API access | **no**: token header and POST |
| Semantic Scholar | semanticscholar.org/product/api → request key | not needed (the unauthenticated tier works via TinyFish); the key is a header |
| BASE | register the client IP with Bielefeld University Library | **no**: the connector egress IPs vary |
| NASA api.nasa.gov | api.nasa.gov → sign up (instant) | **yes**: `api_key=` in the URL (DEMO_KEY works for light use) |
| Kaggle | kaggle.com → Settings → Create API token | listing works without one; downloads need header auth (**no**) |

## Not available here

- **GitHub-content routes**, which are excluded:
  - the OEIS raw data mirror;
  - WarpFactory sources read through a GitHub reader;
  - FeynCalc downloaded from GitHub inside the Wolfram kernel;
  - cobaya likelihood data (Planck native data, DESI BAO and Pantheon+ repos);
  - SXS catalogue data;
  - anything else through raw/media/codeload githubusercontent, `git clone` of github.com, or the Go proxy.
- **Blocked on every route tried:** CORE, IA Scholar / fatcat, Elicit (paid plan), the Papers with Code API
  (retired), CiteSeerX, Approach0, the MaRDI SPARQL endpoint, KAERI, OQMD (502), exoplanet.eu (503), the Einstein
  Papers Project (now paywalled), SageCell/CoCalc and the Inverse Symbolic Calculator. For constant recognition,
  use local `mpmath.identify` or PARI `lindep`.
- **Remote compute services** are not a database route. Use the local engines (`science-tools`) or the Wolfram
  connector.
