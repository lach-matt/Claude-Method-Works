#!/usr/bin/env python3
"""dbroute.py -- print the tested route to a science database from this container.

    python3 dbroute.py inspire            # substring match on the name (case-insensitive)
    python3 dbroute.py --field astro      # literature | maths | constants | astro | gw | hubs
    python3 dbroute.py --list             # every entry, one line each

Table generated 2026-10-09 from research/warp-drive/toolsweep/toolsweep_result.json (statuses WORKS,
WORKS-VIA-CONNECTOR, NEEDS-FREE-KEY; excluded and GitHub-dependent items removed). Routing rules and READ
guidance live in SKILL.md beside this file. Stdlib only.
"""
import sys, textwrap

ROWS = [('OEIS (via Firecrawl)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  "oeis.org PROXY-403 directly; Firecrawl scrape with formats=['rawHtml'] returns the JSON body",
  "mcp__Firecrawl__firecrawl_scrape(url='https://oeis.org/search?q=<terms>&fmt=json', formats=['rawHtml'], "
  'maxAge=0)'),
 ('LMFDB API (via Firecrawl)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'www.lmfdb.org PROXY-403; Firecrawl returns the JSON',
  "firecrawl_scrape(url='https://www.lmfdb.org/api/<table>/?<field>=<v>&_format=json&_fields=...', "
  "formats=['rawHtml'])"),
 ('zbMATH Open API (via Firecrawl)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'api.zbmath.org PROXY-403; Firecrawl returns the JSON',
  "firecrawl_scrape(url='https://api.zbmath.org/v1/document/_search?search_string=<q>&results_per_page=5', "
  "formats=['rawHtml'])"),
 ('NIST DLMF (via Firecrawl)',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'dlmf.nist.gov PROXY-403; Firecrawl works',
  "firecrawl_scrape(url='https://dlmf.nist.gov/<sec>', formats=['rawHtml'])  # then extract <annotation "
  "encoding='application/x-tex'>"),
 ('TPTP problem library (via TinyFish)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'tptp.org PROXY-403; TinyFish fetch_content works',
  "mcp__TinyFish__fetch_content(urls=['https://tptp.org/cgi-bin/SeeTPTP?Category=Problems&Domain=<D>&File=<F>.p'], "
  "format='markdown')"),
 ('nLab (via Exa) and StackExchange API for physics.SE / MathOverflow (via Firecrawl)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  "ncatlab.org, api.stackexchange.com, mathoverflow.net PROXY-403; connectors work. Parallel web_fetch returned 'Too "
  "Many Requests' at the time",
  "firecrawl_scrape(url='https://api.stackexchange.com/2.3/search?intitle=<q>&site=mathoverflow&pagesize=5', "
  "formats=['rawHtml'])"),
 ('pdg 2026.0 (official PDG Python API, offline SQLite)',
  'constants',
  'WORKS',
  'pip in venv. pdg.lbl.gov and pdgapi.lbl.gov are blocked (403), so the bundled DB is the route.',
  "import pdg; api=pdg.connect(); p=api.get_particle_by_name('p'); p.mass, p.mass_error"),
 ('mendeleev 1.3.0 (offline periodic-table DB)',
  'constants',
  'WORKS',
  'pip in venv',
  "from mendeleev import element; element('H').ionenergies[1]"),
 ('GWOSC event API via Firecrawl connector',
  'gw',
  'WORKS-VIA-CONNECTOR',
  "mcp__Firecrawl__firecrawl_scrape with formats=['rawHtml'] on the JSON URL. Direct access is proxy 403.",
  "firecrawl_scrape(url='https://gwosc.org/eventapi/json/GWTC-1-confident/GW150914/v3/', formats=['rawHtml'], "
  'onlyMainContent=false)'),
 ('arXiv full PDF mirror on Google Cloud Storage (gs://arxiv-dataset, the Kaggle arXiv dataset)',
  'hubs',
  'WORKS',
  'direct HTTPS (storage.googleapis.com is not refused by the proxy); no key',
  'import urllib.request,json\n'
  "b='https://storage.googleapis.com'\n"
  "q=b+'/storage/v1/b/arxiv-dataset/o?prefix=arxiv/arxiv/pdf/2401/2401.15136&fields=items(name,size)'\n"
  "items=json.load(urllib.request.urlopen(q))['items']   # all versions\n"
  "urllib.request.urlretrieve(b+'/arxiv-dataset/'+items[-1]['name'],'paper.pdf')\n"
  '# old-style ids: prefix=arxiv/gr-qc/pdf/0009/0009013\n'
  '# then: python -I -c "import pymupdf;print(pymupdf.open(\'paper.pdf\')[0].get_text())"'),
 ('OpenAlex full snapshot on AWS S3 (s3://openalex)',
  'literature',
  'WORKS',
  'direct HTTPS (openalex.s3.amazonaws.com reachable); anonymous; no key',
  "curl -s 'https://openalex.s3.amazonaws.com/?list-type=2&prefix=data/jsonl/sources/&delimiter=/'\n"
  'curl -sO https://openalex.s3.amazonaws.com/data/jsonl/sources/updated_date=2026-02-09/part_0000.gz\n'
  'python3 -c "import gzip,json;[print(json.loads(l)[\'display_name\']) for l in '
  'gzip.open(\'part_0000.gz\',\'rt\')]"'),
 ('OEIS search JSON API (oeis.org/search?fmt=json)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED (proxy 403); via Firecrawl scrape (rawHtml)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://oeis.org/search?fmt=json&q=1,1,2,5,14,42,132', "
  "formats=['rawHtml'])  # then json.loads(result['rawHtml'])"),
 ('arXiv API (export.arxiv.org/api/query)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via TinyFish fetch_content works; Firecrawl timed out (60s); Parallel web_fetch fetch_error',
  "mcp__TinyFish__fetch_content(urls=['https://export.arxiv.org/api/query?search_query=ti:%22warp%20drive%22+AND+cat:gr-qc&max_results=20&sortBy=submittedDate'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('arXiv OAI-PMH (export.arxiv.org/oai2 -> oaipmh.arxiv.org/oai)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via TinyFish works',
  'TinyFish '
  "fetch_content(urls=['https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:gr-qc/0009013&metadataPrefix=arXiv'], "
  "format='markdown', ...)"),
 ('arXiv abs / PDF / listing pages (arxiv.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; Exa web_fetch_exa (abs), Firecrawl scrape (pdf with parsers, list/gr-qc/new); TinyFish returned '
  '400 on listing',
  "mcp__Firecrawl__firecrawl_scrape(url='https://arxiv.org/pdf/gr-qc/0009013', formats=['markdown'], "
  "parsers=['pdf'], pdfOptions={'maxPages':10})"),
 ('alphaXiv connector (get_paper_content, answer_pdf_queries, discover_papers)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'MCP connector (no key needed beyond the connected account)',
  "mcp__alphaXiv__answer_pdf_queries(paper='gr-qc/9910076', queries=['Exact statement of Eq. (17)'])  # prefer this "
  'over get_paper_content for verbatim text'),
 ('Firecrawl research index (firecrawl_research_search_papers / read_paper / inspect_paper)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'MCP connector',
  "mcp__Firecrawl__firecrawl_research_read_paper(paperId='arxiv:gr-qc/9910076', question='effective Einstein "
  "equation on the brane with projected Weyl term', k=4)"),
 ('INSPIRE-HEP REST API (inspirehep.net/api/literature)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl scrape rawHtml',
  "mcp__Firecrawl__firecrawl_scrape(url='https://inspirehep.net/api/literature?q=refersto%3Aarxiv%3Agr-qc%2F0009013&size=25&fields=titles,arxiv_eprints,citation_count', "
  "formats=['rawHtml'])"),
 ('OpenAlex REST API (api.openalex.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl scrape rawHtml (bulk: use the S3 snapshot item)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.openalex.org/works?filter=cites:W2090490735&per-page=50&select=id,doi,title,publication_year', "
  "formats=['rawHtml'])"),
 ('Crossref REST API (api.crossref.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl (rawHtml) and Parallel web_fetch (excerpt) both work',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.crossref.org/works/10.1088/0264-9381/11/5/001', "
  "formats=['rawHtml'])"),
 ('Semantic Scholar Graph API (api.semanticscholar.org/graph/v1)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; TinyFish works; Firecrawl got HTTP 429 (shared-IP rate limit). Free key available (header '
  'x-api-key - connectors here cannot send headers)',
  "mcp__TinyFish__fetch_content(urls=['https://api.semanticscholar.org/graph/v1/paper/arXiv:gr-qc/0009013/citations?fields=title,year&limit=100'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('NASA ADS API (api.adsabs.harvard.edu)',
  'astro',
  'NEEDS-FREE-KEY',
  'direct BLOCKED; via Firecrawl reaches the server but it requires an Authorization: Bearer header (free token from '
  'ui.adsabs.harvard.edu). None of the fetch connectors expose request headers, so even a free token cannot be used '
  'from this container.',
  "# Only usable from a machine with egress: curl -H 'Authorization: Bearer $ADS_TOKEN' "
  "'https://api.adsabs.harvard.edu/v1/search/query?q=title:%22warp+drive%22&fl=bibcode,title'\n"
  '# Here: use INSPIRE/OpenAlex/Crossref via Firecrawl instead'),
 ('zbMATH Open API (api.zbmath.org/v1)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl rawHtml',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.zbmath.org/v1/document/_search?search_string=cc%3A83E15%20ti%3Abrane&results_per_page=20', "
  "formats=['rawHtml'])"),
 ('LMFDB API (www.lmfdb.org/api)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl rawHtml',
  "mcp__Firecrawl__firecrawl_scrape(url='https://www.lmfdb.org/api/ec_curvedata/?_format=json&conductor=37&_fields=lmfdb_label,rank', "
  "formats=['rawHtml'])"),
 ('DLMF / MathWorld / nLab / Encyclopedia of Mathematics / ProofWiki (reference pages)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED (all five hosts 403; wolfram.com refused); via Exa web_fetch_exa',
  "mcp__Exa__web_fetch_exa(urls=['https://dlmf.nist.gov/15.2'], maxCharacters=20000)"),
 ('Stack Exchange API (Physics SE, MathOverflow, Math SE)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl rawHtml; anonymous quota 300/day (shared connector IP)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.stackexchange.com/2.3/search/advanced?q=Israel%20junction&site=physics&sort=votes&filter=withbody', "
  "formats=['rawHtml'])"),
 ('Wikipedia REST API (en.wikipedia.org/api/rest_v1)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl rawHtml',
  "mcp__Firecrawl__firecrawl_scrape(url='https://en.wikipedia.org/api/rest_v1/page/summary/Randall%E2%80%93Sundrum_model', "
  "formats=['rawHtml'])"),
 ('Wikidata SPARQL endpoint (query.wikidata.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl (GET with URL-encoded query)',
  "q=urllib.parse.quote('SELECT ?v WHERE {wd:Q2111 p:P1181/psv:P1181/wikibase:quantityAmount ?v}')\n"
  "mcp__Firecrawl__firecrawl_scrape(url='https://query.wikidata.org/sparql?format=json&query='+q, "
  "formats=['rawHtml'])"),
 ('Unpaywall API (api.unpaywall.org/v2)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl; needs only an email query param',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.unpaywall.org/v2/10.1103/PhysRevD.63.084013?email=you@example.org', "
  "formats=['rawHtml'])  # then fetch the arXiv id from the GCS mirror"),
 ('DataCite REST API (api.datacite.org)',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.datacite.org/dois?query=warp%20drive&page%5Bsize%5D=10', "
  "formats=['rawHtml'])"),
 ('DOAJ API (doaj.org/api)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://doaj.org/api/search/articles/bibjson.title%3A%22brane%22?pageSize=20', "
  "formats=['rawHtml'])"),
 ('Europe PMC REST API',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json', "
  "formats=['rawHtml'])"),
 ('PubMed E-utilities (eutils.ncbi.nlm.nih.gov)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json', "
  "formats=['rawHtml'])"),
 ('HAL API (api.archives-ouvertes.fr)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.archives-ouvertes.fr/search/?q=...&wt=json&fl=title_s,uri_s,fileMain_s', "
  "formats=['rawHtml'])"),
 ('Zenodo REST API (zenodo.org/api/records)',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://zenodo.org/api/records?q=title:%22brane%22&size=20', "
  "formats=['rawHtml'])"),
 ('Figshare API (api.figshare.com/v2)',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl GET only',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.figshare.com/v2/articles/34293318', formats=['rawHtml'])  # "
  'lookup by id only'),
 ('Internet Archive advancedsearch (archive.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://archive.org/advancedsearch.php?q=title%3A(gravitation)+AND+mediatype%3Atexts&fl%5B%5D=identifier&rows=50&output=json', "
  "formats=['rawHtml'])"),
 ('Project Gutenberg via Gutendex (gutendex.com)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; Firecrawl works (stealth proxy); TinyFish timed out',
  "mcp__Firecrawl__firecrawl_scrape(url='https://gutendex.com/books?search=riemann', formats=['rawHtml'])"),
 ('Open Library search API (openlibrary.org/search.json)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://openlibrary.org/search.json?q=wald+general+relativity&limit=5', "
  "formats=['rawHtml'])"),
 ('SciPost API (scipost.org/api/publications)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://scipost.org/api/publications/?format=json&search=brane', "
  "formats=['rawHtml'])"),
 ('OSTI.gov API (www.osti.gov/api/v1/records)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl (XML response)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://www.osti.gov/api/v1/records?title=brane&rows=20', "
  "formats=['rawHtml'])"),
 ('NASA Technical Reports Server API (ntrs.nasa.gov/api)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://ntrs.nasa.gov/api/citations/20110015936/downloads/20110015936.txt', "
  "formats=['rawHtml'])"),
 ('OpenCitations Index API v2 (api.opencitations.net)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.opencitations.net/index/v2/citations/doi:10.1088/0264-9381/11/5/001', "
  "formats=['rawHtml'])"),
 ('dblp search API (dblp.org/search/publ/api)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl',
  "mcp__Firecrawl__firecrawl_scrape(url='https://dblp.org/search/publ/api?q=numerical%20relativity&format=json&h=50', "
  "formats=['rawHtml'])"),
 ('ORCID public API (pub.orcid.org/v3.0) and ROR API (api.ror.org/v2)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; ORCID via Firecrawl, ROR via TinyFish',
  "mcp__Firecrawl__firecrawl_scrape(url='https://pub.orcid.org/v3.0/<ORCID>/works', formats=['rawHtml'])"),
 ('HEPData (www.hepdata.net)',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; Firecrawl works; TinyFish bot_blocked',
  "mcp__Firecrawl__firecrawl_scrape(url='https://www.hepdata.net/search/?q=...&format=json&size=10', "
  "formats=['rawHtml'])"),
 ('Google Scholar (scholar.google.com)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; one Firecrawl scrape returned a full results page',
  "mcp__Firecrawl__firecrawl_scrape(url='https://scholar.google.com/scholar?q=%22brane+world%22+Shiromizu', "
  "formats=['markdown'], onlyMainContent=True)"),
 ('Publisher landing pages: APS (journals.aps.org), IOP (iopscience.iop.org)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct BLOCKED; via Firecrawl (abstract/metadata only)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://journals.aps.org/prd/abstract/<DOI>', formats=['summary'])"),
 ('Springer Nature Open Access API (api.springernature.com)',
  'literature',
  'NEEDS-FREE-KEY',
  'direct BLOCKED; Firecrawl reaches server -> 401 without key',
  '# after registering at dev.springernature.com:\n'
  "mcp__Firecrawl__firecrawl_scrape(url='https://api.springernature.com/openaccess/json?q=title:%22warp%20drive%22&api_key=KEY', "
  "formats=['rawHtml'])"),
 ('Consensus connector (mcp__Consensus__search)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'MCP connector, free tier',
  "mcp__Consensus__search(query='Randall-Sundrum brane black hole solutions')"),
 ('SciSpace connector (mcp__SciSpace__search-papers)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'MCP connector',
  "mcp__SciSpace__search-papers(searchQuestion='How do brane-world corrections modify the Schwarzschild solution?')"),
 ('Wiley Scholar Gateway connector (search_wiley_fulltext)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'MCP connector',
  "mcp__Wiley_Scholar_Gateway__search_wiley_fulltext(query='...full natural-language question...', topN=10)"),
 ('NIST CODATA constants (allascii.txt)',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct HTTPS proxy 403; via Exa web_fetch_exa',
  "mcp__Exa__web_fetch_exa(urls=['https://physics.nist.gov/cuu/Constants/Table/allascii.txt'], "
  'maxCharacters=200000)  # offline equivalent: scipy.constants.physical_constants'),
 ('NIST Atomic Spectra Database (lines, ionisation energies)',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (Exa returned HTTP 500 on lines1.pl)',
  "mcp__TinyFish__fetch_content(urls=['https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=H-He&units=1&format=2&order=0&at_num_out=on&sp_name_out=on&ion_charge_out=on&el_name_out=on&e_out=0&unc_out=on&submit=Retrieve+Data'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('NIST Chemistry WebBook',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=1'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('NIST Atomic Weights and Isotopic Compositions',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Fe&ascii=ascii2&isotype=some'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('PDG REST API (pdgapi.lbl.gov) and PDG Listings site',
  'constants',
  'WORKS-VIA-CONNECTOR',
  "direct proxy 403 (pdg.lbl.gov, pdgapi.lbl.gov); via Exa (API JSON) and TinyFish (listings). The offline 'pdg' pip "
  'package is equivalent and needs no connector',
  "mcp__Exa__web_fetch_exa(urls=['https://pdgapi.lbl.gov/summaries/S008M'])"),
 ('HEPData',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  "direct proxy 403; Firecrawl with formats=['rawHtml'] returns the JSON (TinyFish reports bot_blocked; Exa "
  'CRAWL_UNKNOWN_ERROR)',
  "mcp__Firecrawl__firecrawl_scrape(url='https://www.hepdata.net/search/?q=higgs&format=json&size=5', "
  "formats=['rawHtml'], onlyMainContent=False)"),
 ('CERN Open Data API',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (files sit on root://eospublic, which no connector can fetch)',
  "mcp__TinyFish__fetch_content(urls=['https://opendata.cern.ch/api/records/?q=higgs&size=1'], format='markdown', "
  'links=False, image_links=False, page_metadata=False)'),
 ('INSPIRE-HEP API',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://inspirehep.net/api/literature?q=t%20randall%20sundrum&size=5&fields=titles,citation_count'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('SIMBAD TAP',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via Exa',
  "mcp__Exa__web_fetch_exa(urls=['https://simbad.cds.unistra.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&format=json&query=SELECT%20TOP%201%20main_id,ra,dec%20FROM%20basic%20WHERE%20main_id=%27M%20%2031%27'])"),
 ('VizieR (ASU-TSV) and CDS cdsarc catalogue files',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=I/239/hip_main&-out=HIP,Vmag,Plx&-out.max=3'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('CDS Sesame name resolver',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://cds.unistra.fr/cgi-bin/nph-sesame/-oxp/SNV?M31'], format='markdown', "
  'links=False, image_links=False, page_metadata=False)'),
 ('NED (NASA/IPAC Extragalactic Database)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://ned.ipac.caltech.edu/srs/ObjectLookup?name=M31'], format='markdown', "
  'links=False, image_links=False, page_metadata=False)'),
 ('NASA Exoplanet Archive TAP',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish with format=csv (Exa fails: CRAWL_UNEXPECTED_CONTENT_TYPE on json)',
  "mcp__TinyFish__fetch_content(urls=['https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+10+pl_name,pl_orbper+from+pscomppars&format=csv'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Gaia archive TAP (ESA)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT%20TOP%202%20source_id,parallax%20FROM%20gaiadr3.gaia_source%20WHERE%20parallax%3E700'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('ESA Sky TAP',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (Firecrawl answered once with a real TAP 400 for a bad table name, then failed '
  'with document_antibot)',
  "mcp__TinyFish__fetch_content(urls=['https://sky.esa.int/esasky-tap/tap/sync?request=doQuery&lang=adql&format=csv&query=SELECT%20TOP%205%20*%20FROM%20alerts.mv_v_gravitational_waves_fdw'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('MAST API (STScI)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (the returned markup is stripped, so values run together)',
  "mcp__TinyFish__fetch_content(urls=['https://mast.stsci.edu/api/v0/invoke?request=%7B%22service%22%3A%22Mast.Name.Lookup%22%2C%22params%22%3A%7B%22input%22%3A%22M31%22%7D%2C%22format%22%3A%22json%22%7D'], "
  "format='html', links=False, image_links=False, page_metadata=False)"),
 ('HEASARC Xamin TAP',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish. The server rejects FORMAT=csv; the default VOTable comes back base64-BINARY, '
  'which then needs decoding',
  "mcp__TinyFish__fetch_content(urls=['https://heasarc.gsfc.nasa.gov/xamin/vo/tap/sync?REQUEST=doQuery&LANG=ADQL&QUERY=SELECT%20TOP%202%20name,ra,dec%20FROM%20rosmaster'], "
  "format='html', links=False, image_links=False, page_metadata=False)"),
 ('IRSA TAP (IPAC)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://irsa.ipac.caltech.edu/TAP/sync?QUERY=SELECT+TOP+2+designation,ra,dec+FROM+fp_psc&FORMAT=csv'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Planck PR3 data via IRSA mirror (irsa.ipac.caltech.edu/data/Planck)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish. Large results auto-save to a tool-results file that numpy can parse',
  "mcp__TinyFish__fetch_content(urls=['https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)  # then np.loadtxt on the saved text"),
 ('LAMBDA (NASA CMB archive)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/wmap_tt_spectrum_9yr_v5.txt'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('SDSS SkyServer SQL (DR18)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?cmd=select%20top%202%20objid,ra,dec%20from%20photoobj&format=json'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('NOIRLab Astro Data Lab TAP (incl. DESI DR1) and DESI public listing',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403 (datalab.noirlab.edu, data.desi.lbl.gov); via TinyFish. The SPARCL endpoint I tried '
  '(/sparc/version/) returned 404',
  "mcp__TinyFish__fetch_content(urls=['https://datalab.noirlab.edu/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT%20TOP%202%20targetid,z,spectype%20FROM%20desi_dr1.zpix'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('ESO archive TAP and CADC TAP',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct not individually tested (all science hosts tested returned 403); via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://archive.eso.org/tap_obs/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT%20TOP%202%20target_name,instrument_name%20FROM%20ivoa.ObsCore'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('JPL Horizons API',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  'mcp__TinyFish__fetch_content(urls=["https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=\'499\'&OBJ_DATA=\'YES\'&MAKE_EPHEM=\'YES\'&EPHEM_TYPE=\'VECTORS\'&START_TIME=\'2026-01-01\'&STOP_TIME=\'2026-01-02\'&STEP_SIZE=\'1d\'"], '
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('JPL SBDB and Close-Approach (CAD) APIs',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via Exa (SBDB) and TinyFish (CAD)',
  "mcp__Exa__web_fetch_exa(urls=['https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=Ceres'])"),
 ('Minor Planet Center (MPCORB files)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (large result auto-saved to a tool-results file, parseable in bash)',
  "mcp__TinyFish__fetch_content(urls=['https://www.minorplanetcenter.net/iau/MPCORB/NEA.txt'], format='markdown', "
  'links=False, image_links=False, page_metadata=False)'),
 ('NASA api.nasa.gov (APOD, NeoWs) with DEMO_KEY',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (the key goes in the query string, so connectors can carry it)',
  "mcp__TinyFish__fetch_content(urls=['https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-10-01&end_date=2026-10-02&api_key=DEMO_KEY'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('GWOSC event API (gravitational-wave open science)',
  'gw',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish. The 651 KB JSON auto-saves to a file and parses in python',
  "mcp__TinyFish__fetch_content(urls=['https://gwosc.org/eventapi/json/GWTC/'], format='markdown', links=False, "
  "image_links=False, page_metadata=False)  # then json.load the saved tool-results file and read ['events']"),
 ('LIGO GraceDB public superevents API',
  'gw',
  'WORKS-VIA-CONNECTOR',
  'direct not individually tested; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://gracedb.ligo.org/api/superevents/?query=far%3C1e-10&count=5&format=json'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('IAEA LiveChart of Nuclides API',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via Exa',
  "mcp__Exa__web_fetch_exa(urls=['https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=135xe'])"),
 ('IAEA AMDC AME2020 atomic mass table',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403 (www-nds.iaea.org); via TinyFish. Offline alternative: radioactivedecay bundles AME2020',
  "mcp__TinyFish__fetch_content(urls=['https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt'], format='markdown', "
  'links=False, image_links=False, page_metadata=False)'),
 ('NNDC NuDat3 / ENSDF (BNL)',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=135XE&unc=nds'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('PubChem PUG REST',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/property/MolecularWeight/JSON'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Materials Project OPTIMADE endpoint (no key)',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://optimade.materialsproject.org/v1/structures?filter=chemical_formula_reduced=%22Si%22&page_limit=1'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Materials Project native API (api.materialsproject.org) / mp-api',
  'constants',
  'NEEDS-FREE-KEY',
  'direct proxy 403; via connector the API answers 401. The key goes in an X-API-KEY header, which none of the fetch '
  'connectors can send, so a free key does not help here',
  '# use the OPTIMADE row instead'),
 ('AFLOW AFLUX API',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://aflow.org/API/aflux/?species(Si),nspecies(1),$paging(1,1)'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Wolfram connector (WolframLanguageEvaluator / WolframAlpha) curated data',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'via mcp__Wolfram__WolframLanguageEvaluator (connected); direct api.wolframalpha.com is proxy 403',
  'mcp__Wolfram__WolframLanguageEvaluator(code=\'IsotopeData["Xenon135","HalfLife"]\')'),
 ('Hugging Face datasets API',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403 (huggingface_hub/datasets pip unusable); via TinyFish (Exa: CRAWL_UNEXPECTED_CONTENT_TYPE)',
  "mcp__TinyFish__fetch_content(urls=['https://huggingface.co/api/datasets?search=gravitational&limit=5'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Kaggle datasets API',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403 (kaggle CLI unusable); listing via TinyFish; download NEEDS-FREE-KEY plus header auth',
  "mcp__TinyFish__fetch_content(urls=['https://www.kaggle.com/api/v1/datasets/list?search=gravitational'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Zenodo REST API',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://zenodo.org/api/records?q=planck%20likelihood&size=3'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Google Dataset Search',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (HTML rendered to markdown)',
  "mcp__TinyFish__fetch_content(urls=['https://datasetsearch.research.google.com/search?query=brane%20world'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('data.nasa.gov (CKAN API)',
  'hubs',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish (the old Socrata /api/views path is replaced by CKAN /api/3/action)',
  "mcp__TinyFish__fetch_content(urls=['https://data.nasa.gov/api/3/action/package_search?q=exoplanet&rows=5'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('NOAA (SWPC space-weather JSON, NCEI search API)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'direct proxy 403; via TinyFish',
  "mcp__TinyFish__fetch_content(urls=['https://services.swpc.noaa.gov/json/planetary_k_index_1m.json'], "
  "format='markdown', links=False, image_links=False, page_metadata=False)"),
 ('Google BigQuery public datasets (connector)',
  'astro',
  'WORKS-VIA-CONNECTOR',
  'via mcp__Google_Cloud_BigQuery__* (connected). Only free metadata calls were made; SQL queries would bill the '
  "user's GCP project (1 TB/month free tier) and were not run",
  "mcp__Google_Cloud_BigQuery__list_table_ids(projectId='bigquery-public-data', "
  "datasetId='wise_all_sky_data_release')"),
 ('NASA ADS API',
  'astro',
  'NEEDS-FREE-KEY',
  'direct proxy 403; via connector the API answers 401. It needs a free token in an Authorization header, which the '
  'fetch connectors cannot send',
  '# use the INSPIRE-HEP row or the alphaXiv/Consensus connectors instead'),
 ('AWS Open Data astronomy buckets (unsigned S3)',
  'astro',
  'WORKS',
  'direct HTTPS to <bucket>.s3.amazonaws.com; boto3 with signature_version=UNSIGNED. arxiv.s3 is requester-pays '
  '(403).',
  'import boto3; from botocore import UNSIGNED; from botocore.config import Config; '
  "s3=boto3.client('s3',config=Config(signature_version=UNSIGNED),region_name='us-east-1'); "
  "s3.list_objects_v2(Bucket='stpubdata',Prefix='tess/public/',Delimiter='/') ; curl "
  "'https://nasa-lambda.s3.amazonaws.com/?list-type=2&prefix=wmap/'"),
 ('Google Cloud Storage public bucket arxiv-dataset (full arXiv PDF corpus)',
  'literature',
  'WORKS',
  'direct HTTPS storage.googleapis.com (JSON API and object GET)',
  'curl -s '
  "'https://storage.googleapis.com/storage/v1/b/arxiv-dataset/o?prefix=arxiv/arxiv/pdf/2509/2509.01234&maxResults=5' "
  '; curl -sO https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/2509/2509.01234v1.pdf'),
 ('xAct 1.3.0 (xTensor, xCoba, xPert) in the official Wolfram connector',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'via connector mcp__Wolfram__WolframLanguageEvaluator (stateless: re-download takes about 1 s per call). xact.es '
  'is 403 from this container directly.',
  'dir=CreateDirectory[]; f=FileNameJoin[{dir,"x.tgz"}]; '
  'URLDownload["http://www.xact.es/download/xAct_1.3.0.tgz",f]; ExtractArchive[f,dir]; PrependTo[$Path,dir]; '
  'Block[{Print=Null&},Quiet@Needs["xAct`xPerm`"]]; xAct`xPerm`$xpermQ=False; '
  'Block[{Print=Null&},Quiet@Needs["xAct`xCoba`"]]; ToExpression["DefManifold[M4,4,{a,b,c,d,e,f1}]; '
  'DefChart[sch,M4,{0,1,2,3},{t[],r[],th[],ph[]}]; DefMetric[-1,g[-a,-b],CD]; '
  'MetricInBasis[g,-sch,DiagonalMatrix[{...}]]; MetricCompute[g,sch,All]; '
  'Simplify@ToValues@TraceBasisDummy@ToBasis[sch]@RicciScalarCD[]"]   (use ToExpression so symbols parse after the '
  'package loads)'),
 ('Loogle, LeanSearch, Metamath, Mizar MML and Isabelle AFP via Firecrawl',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'via connector mcp__Firecrawl__firecrawl_scrape. Direct access is 403 for loogle.lean-lang.org, leansearch.net, '
  'isa-afp.org, mizar.uwb.edu.pl and us.metamath.org.',
  "firecrawl_scrape(url='https://loogle.lean-lang.org/json?q=Real.sqrt%2C%20%22mul_self%22', formats=['rawHtml'], "
  "maxAge=0) ; firecrawl_scrape(url='https://leansearch.net/?q=<words>', formats=['markdown'], waitFor=5000)"),
 ('gs://arxiv-dataset (arXiv bulk PDFs on Google Cloud Storage)',
  'literature',
  'WORKS',
  'storage.googleapis.com returns 200 directly; JSON listing API works',
  'curl -O https://storage.googleapis.com/arxiv-dataset/arxiv/hep-th/pdf/9906/9906064v1.pdf  (new IDs: '
  'arxiv/arxiv/pdf/YYMM/YYMM.NNNNNvN.pdf)'),
 ('ar5iv HTML (arXiv LaTeX alttext) via Firecrawl rawHtml',
  'literature',
  'WORKS-VIA-CONNECTOR',
  "ar5iv.labs.arxiv.org and arxiv.org return 403 directly. mcp__Firecrawl__firecrawl_scrape with formats ['rawHtml'] "
  'works. TinyFish format html strips alttext.',
  "firecrawl_scrape(url='https://ar5iv.labs.arxiv.org/html/hep-th/9906064', formats=['rawHtml']) then "
  're.findall(r\'alttext="([^"]*)"\', html)'),
 ('arXiv e-print LaTeX source via Firecrawl + TexSoup 0.3.3',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Firecrawl rawHtml on arxiv.org/e-print/<id> decompresses single-file gzip sources. TinyFish returns mangled '
  'binary. Multi-file tarballs untested (likely fail). TexSoup was pip-installed in a venv.',
  "firecrawl_scrape(url='https://arxiv.org/e-print/hep-th/9906064', formats=['rawHtml','html','markdown','links'])  "
  "# force file save; TexSoup(open(tex).read()).find_all('equation')"),
 ('SCOAP3 repository API (JHEP/PRD/EPJC/PLB/NPB OA full text)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'repo.scoap3.org and scoap3-prod-backend.s3.cern.ch return 403 directly. TinyFish fetch_content works; the '
  'Firecrawl scrape timed out after 60 s.',
  "mcp__TinyFish__fetch_content(urls=['https://repo.scoap3.org/api/records/?q=...']) then fetch _files[].file the "
  'same way'),
 ('Living Reviews in Relativity (link.springer.com) via Exa',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'link.springer.com returns 403 directly; mcp__Exa__web_fetch_exa works',
  "mcp__Exa__web_fetch_exa(urls=['https://link.springer.com/article/10.12942/lrr-2010-5'], maxCharacters=200000)"),
 ('CERN Document Server (recjson API)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  "Direct returns 403. TinyFish and basic Firecrawl get the Anubis bot wall ('Oh noes!'). Firecrawl with "
  "proxy='stealth' and waitFor=8000 passes.",
  "firecrawl_scrape(url='https://cds.cern.ch/search?p=brane&of=recjson&rg=2&ot=title,authors,files', "
  "formats=['rawHtml'], proxy='stealth', waitFor=8000)"),
 ('INIS (IAEA) InvenioRDM API',
  'constants',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; TinyFish works',
  "mcp__TinyFish__fetch_content(urls=['https://inis.iaea.org/api/records?q=warp'])"),
 ('OpenAIRE Graph API v1',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. The legacy /search/publications endpoint failed (TinyFish target_unreachable, Firecrawl '
  'timeout). The new /graph/v1/researchProducts endpoint works via Exa.',
  "mcp__Exa__web_fetch_exa(urls=['https://api.openaire.eu/graph/v1/researchProducts?search=brane%20world&pageSize=10'])"),
 ('OSF Preprints API',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; TinyFish works',
  "mcp__TinyFish__fetch_content(urls=['https://api.osf.io/v2/preprints/?filter[subjects]=...'])"),
 ('BASE (Bielefeld Academic Search Engine) API',
  'literature',
  'NEEDS-FREE-KEY',
  'Requires IP registration',
  'register IP with BASE, then '
  'api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&query=...'),
 ('Lens.org scholarly API',
  'literature',
  'NEEDS-FREE-KEY',
  "Needs a free token. The web UI via TinyFish shows only 'Verifying you are a valid user'.",
  'request token at lens.org, then POST api.lens.org/scholarly/search'),
 ('Dimensions',
  'literature',
  'NEEDS-FREE-KEY',
  'API needs an approved key; the web app is bot-blocked',
  'n/a without key'),
 ('de.wikisource (proofread German originals: Einstein 1915 etc.)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; Firecrawl (auto stealth) works',
  "firecrawl_scrape(url='https://de.wikisource.org/wiki/Die_Feldgleichungen_der_Gravitation', formats=['markdown'], "
  'onlyMainContent=True)'),
 ('Internet Archive (advancedsearch, djvu.txt, fulltext search-inside, page images)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'archive.org returns 403 directly. TinyFish works for the JSON APIs (advancedsearch, BookReader '
  'fulltext/inside.php); Firecrawl rawHtml works for multi-MB djvu.txt; Firecrawl screenshot of '
  '/details/<id>/page/nNNN/mode/1up with waitFor 20000 returns a page image hosted on storage.googleapis.com '
  '(reachable directly). Direct .jpg URLs give no screenshot.',
  'TinyFish: https://archive.org/advancedsearch.php?q=...&fl[]=identifier&output=json ; Firecrawl rawHtml: '
  'https://archive.org/download/ID/ID_djvu.txt ; Firecrawl screenshot: '
  'https://archive.org/details/ID/page/nLEAF/mode/1up?view=theater (waitFor 20000)'),
 ('GDZ Göttingen (Mathematische Annalen etc.)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  "Direct returns 403. Firecrawl rawHtml on /mets/<PPN>.mets.xml works; the HTML viewer is JS-only ('Wird geladen'), "
  'but a Firecrawl screenshot of the TIFY viewer (waitFor 15000) returns a legible page.',
  "firecrawl_scrape(url='https://gdz.sub.uni-goettingen.de/mets/PPN235181684_0079.mets.xml', formats=['rawHtml'])"),
 ('EuDML',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. Firecrawl works for record pages; the TinyFish search page returned 500.',
  "firecrawl_scrape(url='https://eudml.org/doc/<id>', formats=['markdown'])"),
 ('Numdam OAI-PMH',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; Firecrawl rawHtml works',
  "firecrawl_scrape(url='https://www.numdam.org/oai/?verb=ListRecords&metadataPrefix=oai_dc&set=AIHP', "
  "formats=['rawHtml'])"),
 ('HathiTrust Bibliographic API',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. TinyFish works for the bib API; full-text search (babel …/ls) is bot_blocked.',
  "mcp__TinyFish__fetch_content(urls=['https://catalog.hathitrust.org/api/volumes/brief/oclc/<n>.json'])"),
 ('Gallica SRU (BnF)',
  'literature',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; TinyFish works',
  "mcp__TinyFish__fetch_content(urls=['https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=dc.title%20all%20%22...%22'])"),
 ('Wolfram Functions Site',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. Firecrawl works with the ID-style URL (the path-style URL I guessed returned 404).',
  "firecrawl_scrape(url='https://functions.wolfram.com/07.23.02.0001.01', formats=['markdown'])"),
 ('CaltechAUTHORS (Bateman Manuscript Project volumes)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. Firecrawl on /api/records works (the /records HTML search path returned 404). The PDFs '
  'themselves were not fetched (54–71 MB each).',
  "firecrawl_scrape(url='https://authors.library.caltech.edu/api/records?q=%22Higher%20Transcendental%20Functions%22&size=3', "
  "formats=['rawHtml'])"),
 ('MaRDI portal (Wikibase API; SPARQL endpoint)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. TinyFish works for w/api.php wbsearchentities. query.portal.mardi4nfdi.de/sparql: TinyFish '
  'target_unreachable or 404, Firecrawl ERR_TUNNEL_CONNECTION_FAILED.',
  "mcp__TinyFish__fetch_content(urls=['https://portal.mardi4nfdi.de/w/api.php?action=wbsearchentities&search=...&language=en&format=json'])"),
 ('zbMATH Open API (+ formula search)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403. Firecrawl works for api.zbmath.org/v1/document/_search. The formulae page renders only the '
  'help UI (the search moved into structured search), so no hits were returned.',
  "firecrawl_scrape(url='https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22Randall-Sundrum%22&page=0&results_per_page=10', "
  "formats=['rawHtml'])"),
 ('ATNF psrcat web form via TinyFish',
  'gw',
  'WORKS-VIA-CONNECTOR',
  'TinyFish fetch_content on proc_form.php with ephemeris=short',
  "mcp__TinyFish__fetch_content(urls=['https://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?version=2.6.1&pulsar_names=J0737-3039A&ephemeris=short&submit_ephemeris=Get+Ephemeris&style=Long+with+last+digit+error&no_value=*&state=query'])"),
 ('VizieR B/psr (ATNF catalogue mirror) via TinyFish',
  'gw',
  'WORKS-VIA-CONNECTOR',
  'Direct returns 403; the TinyFish asu-tsv query works',
  "mcp__TinyFish__fetch_content(urls=['https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=B/psr/psr&PSRJ=J0737-3039A&-out=PSRJ,PB'])"),
 ('Magma Online Calculator (free, 120 s limit)',
  'maths',
  'WORKS-VIA-CONNECTOR',
  'magma.maths.usyd.edu.au returns 403 directly. mcp__TinyFish__run_web_automation types the code and submits. Ask '
  "for 'every line verbatim': the first run only returned the first line.",
  "run_web_automation(url='http://magma.maths.usyd.edu.au/calc/', goal='Clear the input box, type: <code>; click "
  "Submit; return EVERY output line verbatim', session_id=<uuid4>)  # may time out at 60 s; poll list_runs/get_run")]

def show(r):
    name, field, status, access, example = r
    print("== %s  [%s | %s]" % (name, field, status))
    print(textwrap.fill("route: " + access, 110, subsequent_indent="       "))
    print("example:")
    print(textwrap.indent(example, "    "))
    print()

def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    if argv[0] == "--list":
        for r in ROWS: print("%-11s %-20s %s" % (r[1], r[2], r[0]))
        return 0
    if argv[0] == "--field":
        hits = [r for r in ROWS if r[1] == (argv[1] if len(argv) > 1 else "")]
    else:
        q = " ".join(argv).lower()
        hits = [r for r in ROWS if q in r[0].lower() or q in r[3].lower()]
    for r in hits: show(r)
    if not hits:
        print("no entry for %r; try --list (and see SKILL.md 'Not available here')" % " ".join(argv)); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
