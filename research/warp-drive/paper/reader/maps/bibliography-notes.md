# Bibliography notes for the reader's edition

Companion to `bibliography.md`, which is in the same directory. Checked on 2026-11-13. The scope is
`research/warp-drive/paper/RESPONSE-HL-5D.md`, called "the paper" below, together with its section 10 (lines 1908–2108)
and the 112 `.md` files of the supplement: 34 in `docket68/n1star/` and 78 in `docket68/n1star/proof5/`. Paths below
are relative to `research/warp-drive/`, and `docket68/n1star/` is left out of them.

## 1. How the entries were checked

- **The reference-lookup tools did not work here.** `verify_reference` and `lookup_reference` were loaded and
  called. Every call came back "unchecked" or "not found" because the proxy refuses both arXiv and OpenAlex
  (403, "Tunnel connection failed"). So no verdict in this file comes from those tools.
- The checks used these routes instead:
  - INSPIRE-HEP's API, through Firecrawl, with batched arXiv-id queries;
  - Crossref's API, through Firecrawl and TinyFish, with DOI filters and bibliographic queries;
  - the arXiv API, through TinyFish, for titles, versions, journal-refs and DOIs;
  - arXiv PDFs from the public `arxiv-dataset` GCS bucket, for:
    - the bibliographies of [Hin26], [Hin26a], [Hin26c], [Hin23c], [Hin23a], [Tou24] and [LR20];
    - checking [LR05] (1.3), [BGP] Cor. 3.2.4 and §1.2, and [CS06] Thm 2;
  - the DLMF front page;
  - the [AB26] URL.
- **What "verified" means.** Authors, title, venue, volume, pages, year and the DOI or arXiv id all agree with a
  Crossref, INSPIRE or arXiv record, or with the arXiv PDF itself.
- **What "corrected" means.** The printed value was wrong. The old and new values are given.
- **What "added" means.** The printed value was right but incomplete. Usually it lacked the journal version or the
  DOI.
- **Choices made for the clean list.**
  - Titles take the publisher's form, in sentence case.
  - arXiv versions are kept where the record names the version it read, because the proofs cite page and theorem
    numbers of that version.
  - Where a journal version exists, its theorem numbering may differ from the arXiv version's. This matters for
    [BH17] and [LR05].

## 2. Key census

- **Section 10 of the paper** has 47 entries.
- **Pattern keys in use.** 114 distinct keys of the form `[A-Za-z]+[0-9]{2}[a-z]?`, plus [DLMF], are used as citations
  in the paper (outside section 10) or in the supplement.
- **Bracket tokens that matched the pattern but are not citations**, and were excluded:
  - [A28] (`EQUALITY5-LAYER.md:1951`, a label);
  - [R10] to [R15] (`CONSTANTS5.md`, round labels);
  - [U10] and [U11] (`RWGAUGE5.md:339-340`, check labels);
  - [m13] (`CERTIFY-10L5-RESULT.md:2401`, a finding label).
- **Keys outside the pattern that the supplement also uses.** Each is in the list:
  - [SBG] (81 uses) and [0C] (32 uses);
  - [HJS] (31), [BGP] (47) and [RS1] (2);
  - [Hö83] (3) and [Hö85] (4), which the pattern misses because of the "ö".
- **Contents of `bibliography.md`:** 128 entries in all. That is 122 works plus 6 alias lines ("See [...]"), which
  keep the alternative keys working: [0C], [CTWG23], [HL17], [Ho85], [SBG] and [Sbi13].
- **Seven keys are new, proposed for works that are named but have no key:**
  - [Bur89], [CB69], [Isa68a] and [Isa68b] (section 6);
  - [Rie49], [HW13] and [Kat75] (section 7).

## 3. Keys used but missing from the paper's section 10

The paper itself uses **one key with no entry: [MP86]**, at `paper/RESPONSE-HL-5D.md:1154`. The supplement uses 68 more.
Each line below gives: the key, an example file:line, and where the full reference came from.

What "Source" means:
- **Supp** is the supplement's own reference text, at the file:line given.
- **Bib(X)** is the bibliography of source paper X, read from its arXiv PDF. The supplement borrows X's key.
- **Search** means Crossref, INSPIRE or arXiv, found by title or author.

- [AN00] `ROUTES-OPEN.md:3035`. Supp `proof5/PART-III-G2-IOTA.md:409`, inline by name. Not in any Hintz bibliography.
- [An12] `N1STAR-PROOF.md:1891`. Supp, same line.
- [BVW15] `proof5/PART-III-G2-IOTA.md:471`. Bib(Hin26), Bib(Hin26c).
- [CBF06] `FAMILIES5-FULL.md:377`. Bib(Tou24).
- [CCRT07] `CERTIFY-10L5.md:11`. Supp `ROUTES-OPEN.md:635`.
- [CCTW16] `FAMILIES5.md:407`. Supp, same line, arXiv id only.
- [Chr11] `BEYOND5.md:114`. Supp `BEYOND5.md:160`.
- [COM81] `proof5/PART-III-C3-BOOSTDATA.md:210`. Bib(Hin26).
- [CP12] `FAMILIES5.md:316`. Supp `FAMILIES5.md:370`.
- [CS06] `FAMILIES5-AXIS.md:185`. Supp `FAMILIES5-VLASOV.md:92`, arXiv id only.
- [CTWG23] `FAMILIES5.md:408`. This is the same work as [CTG23] (section 5).
- [DHRT21] `ROUTES-OPEN.md:133`. Supp `ROUTES-OPEN.md:643`, no title given. Search, with Bib(Hin26).
- [dHUV15] `proof5/PART-II-A-SETUP.md:1126`. Bib(Hin26c).
- [Dya16] `N1STAR-LOG.md:4566`. Supp `proof5/PART-I-B-HIGHENERGY.md:2129`, which gives no pages. Bib(Hin26c).
- [DZ19] `N1STAR-LOG.md:4566`. Bib(Hin26), Bib(Hin26c).
- [Hig87] `proof5/PART-III-A2-HARMONICS.md:121`. Bib(Hin26).
- [Hin16] `proof5/PART-II-A-SETUP.md:1593`. Supp, same line, under its arXiv title. Bib(Hin26c).
- [Hin17] `N1STAR-PROOF.md:3846`. Bib(Hin26), Bib(Hin26a), Bib(Hin26c).
- [Hin22a] `proof5/PART-II-G2-DECAY.md:1327`. Bib(Hin26), Bib(Hin26c).
- [Hin23c] `N1STAR-LOG.md:3884`. Supp `proof5/PART-II-C-OPERATORS.md:849` and `ROUTES-OPEN.md:656`.
- [Hin24a] `N1STAR-LOG.md:1825`. Bib(Hin26), Bib(Hin26c).
- [Hin25a] `N1STAR-LOG.md:4554`. Bib(Hin26), Bib(Hin26a), Bib(Hin26c).
- [Hin25c] `proof5/PART-III-A-PREREQ.md:773`. Bib(Hin26).
- [Hin26b] `N1STAR-LOG.md:5097`. **This key has two meanings, and no single entry fits it** (section 5).
- [HL17] `N1STAR-LOG.md:841`. This is the same work as [HL18e] (section 5).
- [HL19] `FAMILIES5-FULL.md:414`. Supp, same line.
- [HL25] `FAMILIES5-AXIS.md:37`. Supp `FAMILIES5-FULL.md:422`.
- [Ho85] `N1STAR-LOG.md:5024`. This is an ASCII spelling of [Hö85] (section 5).
- [HPS77] `N1STAR-LOG.md:4543`. Supp `proof5/PART-II-B-DYNAMICS.md:736`.
- [Hua15] `N1STAR-LOG.md:328`. Supp `N1STAR-PROOF.md:1024`, arXiv id only. Search.
- [Hun15] `N1STAR-LOG.md:841`. Supp `ROUTES-OPEN.md:660`.
- [HV15] `proof5/PART-III-G-SPECTRAL.md:23`. Bib(Hin26): Haber–Vasy. The same key means another work elsewhere
  (section 5).
- [HV16] `N1STAR-LOG.md:4566`. Bib(Hin26c). **The supplement's own text names the wrong work** (section 4).
- [HV18b] `N1STAR-PROOF.md:7128`. Bib(Hin26).
- [HV20] `N1STAR-PROOF.md:9205`. Bib(Hin26) and others.
- [HV24] `N1STAR-PROOF.md:7128`. Bib(Hin26).
- [HV26] `N1STAR-PROOF.md:7597`. Bib(Hin26), Bib(Hin26c).
- [IT20] `FAMILIES5-AXIS.md:328`. Supp `FAMILIES5-NONROUND.md:375`.
- [KK25] `ROUTES-OPEN.md:13`. Supp `ROUTES-OPEN.md:633`.
- [KS17] `N1STAR-LOG.md:841`. Supp `ROUTES-OPEN.md:640`.
- [Li25] `proof5/PART-II-G2-DECAY.md:1320`. Bib(Hin26c).
- [LR17] `ROUTES-OPEN.md:5357`. Bib(LR20), its reference [42].
- [LX24] `proof5/PART-II-G2-DECAY.md:1327`. Bib(Hin26c).
- [Mel93] `proof5/PART-III-A-PREREQ.md:773`. Bib(Hin26), Bib(Hin23a).
- [Mel94] `N1STAR-LOG.md:4566`. Bib(Hin26c).
- [Mel96] `proof5/PART-III-A-PREREQ.md:773`. Bib(Hin26).
- [Min19] `BEYOND5.md:116`. Supp `BEYOND5.md:163`.
- [MM10] `N1STAR-LOG.md:328`. Supp `N1STAR-PROOF.md:1023` and `:1068`.
- [MM87] `proof5/PART-II-F-IOTA.md:1524`. Supp `proof5/PART-II-F-IOTA.md:2735`.
- [Mos17] `FAMILIES5.md:732`. Supp, same line, arXiv id only.
- [MP11] `CERTIFY-10L5.md:12`. Supp `ROUTES-OPEN.md:637`.
- [MP86] `paper/RESPONSE-HL-5D.md:1154`. Supp `proof5/PART-III-B-FAMILY.md:554`.
- [Olv97] `N1STAR-PROOF.md:4139`. Bib(Hin26c).
- [RT12] `CERTIFY-10L5.md:12`. Supp `ROUTES-OPEN.md:639`.
- [Sbi13] `N1STAR-PROOF.md:1008`. This is the same work as [Sbi15] (section 5).
- [Sbi15] `BEYOND5.md:113`. Supp `BEYOND5.md:158`.
- [Sch10] `N1STAR-LOG.md:855`. A retired label for [Sch13], only mentioned as retired. No entry.
- [See64] `proof5/PART-IX-GAUGE.md:42`. Supp `proof5/PART-IX-GAUGE.md:405`.
- [Shu92] `N1STAR-PROOF.md:8169`. Bib(Hin26a), Bib(Hin26c).
- [SR89] `N1STAR-LOG.md:5051`. Supp `proof5/PART-II-G-NASHMOSER.md:517`. Bib(Hin26), Bib(Hin26c).
- [Tat13] `proof5/PART-II-G2-DECAY.md:1327`. Bib(Hin26), Bib(Hin26c).
- [Tay11] `N1STAR-PROOF.md:9238`. Bib(Hin23a): Taylor, PDE III.
- [Tay11a] `N1STAR-LOG.md:5096`. Bib(Hin26c): Taylor, PDE I.
- [Tou24] `FAMILIES5-AXIS.md:422`. Supp `FAMILIES5-FULL.md:429`.
- [Vas13] `N1STAR-LOG.md:2957`. Bib(Hin26), Bib(Hin26c).
- [Vas18] `N1STAR-LOG.md:2096`. Supp `proof5/PART-II-A2-STANDARD.md:836`.
- [Vas21b] `N1STAR-LOG.md:2095`. Bib(Hin26a), Bib(Hin26c).
- [VZ00] `proof5/PART-I-B-HIGHENERGY.md:238`. Bib(Hin26c).
- [Zwo12] `N1STAR-LOG.md:4566`. Bib(Hin26c).

Keys outside the pattern:
- [0C] `INVERSE5-SIX.md:115`. Supp `proof5/PART-II-F-IOTA.md:2724`. This is the same work as [Hin23e].
- [BGP] `BEYOND5-R0-PROOF.md:472`. Supp `proof5/PART-II-F-IOTA.md:2729`.
- [HJS] `N1STAR-LOG.md:4603`. Supp `proof5/PART-I-B-HIGHENERGY.md:2126`, which gives no title. Search.
- [Hö83] `proof5/PART-II-F-IOTA.md:2058`. Supp `proof5/PART-II-F-IOTA.md:2742`.
- [Hö85] `proof5/PART-II-F-IOTA.md:30`. Supp `proof5/PART-II-F-IOTA.md:2744`.
- [RS1] `proof5/PART-I-C-LOWENERGY.md:122`. Supp `proof5/PART-I-C-LOWENERGY.md:1508`.
- [SBG] `CONSTANTS5.md:1492`. Supp `proof5/PART-II-A-SETUP.md:11`. This is the same work as [Hin26d].

## 4. Verification results

### 4.1 The paper's 47 entries

**All 47 were verified.**

**Corrected: 4 substantive errors.**
- **[LR05]: the title and arXiv id belong to different papers.**
  - Old: *Global existence for the Einstein vacuum equations in wave coordinates*, arXiv:math/0411109v2.
  - Finding: that title belongs to arXiv:math/0312479, which appeared as Comm. Math. Phys. 256 (2005) 43–110. The
    arXiv id belongs to a different paper.
  - Which one was read: the record's quotation is "g^{αβ}∂_α∂_β g_μν = F_μν(g)(∂g, ∂g)" (`N1STAR-PROOF.md:1087`). It
    is (1.3) on p. 2 of math/0411109v2, which was checked against the PDF. The (1.3) of math/0312479 is a different
    model system.
  - New: *The global stability of Minkowski space-time in harmonic gauge*, Ann. of Math. (2) 171 (2010) 1401–1477,
    doi:10.4007/annals.2010.171.1401.
  - The key stays [LR05], although the work dates from 2004–2010.
- **[BH17]: wrong title.**
  - Old: *Multiplication in Sobolev spaces, revisited*. That title belongs to arXiv:1512.07379.
  - New: *Sobolev–Slobodeckij spaces on compact manifolds, revisited*, the title of arXiv:1704.07930, plus Mathematics
    10 (2022) 522, doi:10.3390/math10030522.
  - The supplement had already made this repair at D623 (`N1STAR-PROOF.md:1058`). The paper had not.
  - The theorem numbers 7.21, 7.26 and 9.14 refer to the arXiv text.
- **[CTG23]: title.** Old "...in higher dimensions". New "...in higher dimension", as on arXiv and INSPIRE.
- **[DS23]: truncated title.**
  - Old: *Strongly hyperbolic quasilinear systems revisited*.
  - New: the full title, adding "..., with applications to relativistic fluid dynamics", plus Asymptot. Anal. 140
    (2024) 281–302, doi:10.3233/ASY-241919.
  - The author order Disconzi, Shao is confirmed by Crossref. INSPIRE lists the two the other way round.

**Corrected: 3 minor title forms, now as the publisher prints them.**
- [KI03b]: "generalised" becomes "generalized".
- [Hol08]: "decay-rates" becomes "decay rates".
- [Sch13]: "higher dimensional" becomes "higher-dimensional".

**Added: journal versions the paper lacked (21 entries).**
- [AG22]: Commun. Pure Appl. Anal. 22 (2023) 2960–2999, doi:10.3934/cpaa.2023095.
- [AHW24]: J. Eur. Math. Soc. 28 (2026) 3919–3981, doi:10.4171/jems/1544.
- [AO14]: J. Differential Equations 256 (2014) 2023–2078.
- [BH17]: Mathematics 10 (2022) 522 (see above).
- [CD03]: Mém. Soc. Math. Fr. (N.S.) 94 (2003), doi:10.24033/msmf.407.
- [CLY03b]: J. High Energy Phys. 2003(12) 041.
- [CYDL03]: Phys. Rev. D 68 (2003) 061503.
- [DR08]: Clay Math. Proc. 17 (2013) 97–205.
- [DS23]: Asymptot. Anal. 140 (2024) 281–302 (see above).
- [ER08]: Living Rev. Relativ. 11 (2008) 6.
- [GO13]: Comm. Partial Differential Equations 39 (2014) 1128–1157.
- [HKW18]: Ann. PDE 6 (2020) 7.
- [HL21]: Pure Appl. Math. Q. 20 (2024) 1541–1600.
- [HL24]: Class. Quantum Grav. 41 (2024) 143002.
- [Hol08]: Adv. Theor. Math. Phys. 14 (2010) 1245–1372.
- [KI03]: Prog. Theor. Phys. 110 (2003) 701–722.
- [KI03b]: Prog. Theor. Phys. 111 (2004) 29–73.
- [LR05]: Ann. of Math. 171 (2010) 1401–1477 (see above).
- [LY22]: Math. Nachr. 297 (2024) 811–832.
- [SY21]: Math. Nachr. 297 (2024) 1407–1443.
- [TTS09]: J. Math. Phys. 51 (2010) 062502.

**Added: DOIs or missing pages.**
- DOIs: [HL18], [HL18e], [Tou23a], [Tou23b], [Hin21], [Hin23a], [Hin23e] and [Rac16].
- [IK03]: the page "901" becomes "901–919", and the DOI is added.
- [HHV21]: the DOI is added, and so is the correction in Invent. Math. 236 (2024) 477–481,
  doi:10.1007/s00222-024-01240-w.
- [Sch13]: the issue, pages and DOI are added.
- [DLMF]: the editors are added. The release, 1.2.8 of 2026-09-15, was confirmed on dlmf.nist.gov.

**Verified as printed, with no journal version found as of 2026-11-13.**
- [Hin23b], [Hin23d], [Hin24b], [Hin26], [Hin26a], [Hin26c]: the Crossref author search for P. Hintz since 2023
  finds none of them.
- [Hun19], [LR20], [CTG23] and [Wu26].
- [AB26] has no arXiv id or DOI. The arXiv search returns 0 results. The URL is live, and the title and the authors,
  Levent Alpöge and Tristan Buckmaster, match the PDF.

### 4.2 The added entries (the 63 works in section 3, and the 5 outside the pattern)

**Verified by Crossref (DOI, volume and pages):**
- AN00, BVW15, CBF06 (doi:10.1088/0264-9381/23/20/015), CCRT07, COM81, CP12, CS06, dHUV15;
- Dya16, DZ19, Hig87, Hin16, Hin17, Hin22a, Hin25a, Hin25c;
- HV15, HV16, HV18b, HV20, HV26, HPS77, Hun15, IT20;
- Li25, LR17, LX24, Mel93, Min19, MM87, MP11, MP86;
- Olv97, RT12, Sbi15, See64, Tat13, Tay11, Tay11a, Tou24;
- Vas13, Vas18, Vas21b, VZ00, Zwo12, BGP, KS17 (the 2020 book).

**Verified, with something missing:**
- [CCTW16]: Crossref gives no volume. Dissertationes Math. 515 is from memory and is not printed.
- [HL19]: Ann. Sci. Éc. Norm. Supér. (4), published 2024-04-02, doi:10.24033/asens.2577. Crossref gives no volume or
  pages.
- [MM10]: Crossref gives no volume. "(5) 11 (2012)" is from memory. The pages 857–874 and the DOI are verified.

**Verified on arXiv only, with no journal version found:**
- An12, Chr11, DHRT21, Hin23c, Hin24a, HL25, Hua15 (SSRN copy 2026, no journal), HV24, KK25, Mos17, HJS.
- [Mos17]: its companion paper is Anal. PDE 13 (2020), but that is a different paper.

**Changes from the supplement's own reference text:**
- [Dya16]: "Ann. Inst. Fourier 66 (2016)" becomes 66 (2016) 55–82.
- [MP86]: "Ann. Phys. 172 (1986)" becomes 172 (1986) 304–347.
- [MM87]: "J. Funct. Anal. 75 (1987)" becomes 75 (1987) 260–310.
- [CS06]: arXiv id only; J. Differential Geom. 73 (2006) 185–217 is added.
- [Hin16]: the arXiv title "Global well-posedness of quasilinear wave equations..." (`proof5/PART-II-A-SETUP.md:1593`)
  becomes the published title "Global analysis of quasilinear wave equations on asymptotically de Sitter spaces", Ann.
  Inst. Fourier 66 (2016) 1285–1408.
- **[HV16]: the supplement names the wrong work** (`proof5/PART-I-B-HIGHENERGY.md:2127`).
  - It gives "Non-trapping estimates near normally hyperbolic trapping, Math. Res. Lett. (2014)".
  - The key comes from [Hin26c]'s bibliography, where [HV16] is Hintz–Vasy, *Global analysis of quasilinear wave
    equations on asymptotically Kerr–de Sitter spaces*, IMRN 2016, 5355–5426.
  - [Hin26c]'s own text cites "[HV16, Theorem 4.7]", the theorem the supplement follows.
  - **Corrected to the IMRN paper.**
- [Hin23c]: the title differs between files.
  - The supplement (`proof5/PART-II-C-OPERATORS.md:849`) and Hintz's later bibliographies call it "Linear waves on
    non-stationary asymptotically flat spacetimes. I".
  - arXiv:2302.14647 has only v1, and both its listing and its PDF read "Linear waves on asymptotically flat
    spacetimes. I".
  - The arXiv title is used.
- [KS17]: arXiv:1711.07597 (2017) appeared as a book in 2020, doi:10.1515/9780691218526. The series number 210 is as
  in Bib(Hin26) and Bib(Hin23c). Crossref gives no series.
- [DHRT21]: the title is taken from arXiv. Bib(Hin26) prints a different title ("...the Schwarzschild solution to
  gravitational perturbations").
- [IT20]: Crossref has "quasi-linear" in the title. The arXiv version has "quasilinear".

**Errors in the source bibliographies, not followed here:**
- [Mel93]: the DOI in Bib(Hin26), Bib(Hin26a), Bib(Hin26c) and Bib(Hin23c), 10.1016/0377-0257(93)80040-i, resolves to
  the subject index of J. Non-Newtonian Fluid Mech. vol. 50. The correct DOI is 10.1201/9781439864609.
- [HV20]: Bib(Hin26) prints issue 6(2). Crossref gives 6(1), article 2.
- [Hin23e]: Bib(Hin26c) prints volume 3. The correct volume is 5, as the paper has it.

**Not verifiable with the tools available.** Each is taken from Hintz's bibliographies, consistent across them, and
was not read by the record:
- [Mel94]: the Sanda proceedings, Dekker LN Pure Appl. Math. 161 (1994) 85–130;
- [Mel96]: an unpublished manuscript at math.mit.edu;
- [Shu92]: Astérisque 207 (1992) 35–108;
- [SR89]: Enseign. Math. (2) 35 (1989) 217–226. A Crossref search found no record.

**Partly verified:**
- [Hö83] and [Hö85]: Crossref holds only later printings, the 1998 reprint of I and the 2007 Classics edition of III.
  The 1983 and 1985 Grundlehren data (vols. 256 and 274) are standard and were not checked by a tool.
- [RS1]: Crossref confirms Academic Press, 1972, through chapter records.

## 5. Keys with two meanings, and works with two keys

**[Hin26b] has two meanings in the supplement.** It is always a key borrowed from a source's bibliography. Hintz's three
papers number one another differently.
- **It means our [Hin26c]**, taken from [Hin26a]'s list, at:
  - `N1STAR-PROOF.md:4427`, 9387 and 9414 (Theorem 9.38, Corollary 9.43 and Proposition 9.40).
- **It means our [Hin26]**, taken from [Hin26c]'s list, at:
  - `N1STAR-PROOF.md:6472`, which states this itself, and 6494, a quotation of [Hin26c] Remark 5.14;
  - `proof5/PART-II-G2-DECAY.md:25`, 1038, 1151, 1282 and 1322 (Lemmas 2.12 and 2.23, Fuchsian ODE integration). The
    PDF confirms that [Hin26] Lemma 2.12 is "Integration of a Fuchsian ODE";
  - `N1STAR-LOG.md:5097` and `ROUTES-OPEN.md:2617`.
- In [Hin26]'s own list, [Hin26b] is a third work: *Horizons of some asymptotically stationary space-times*, Duke Math.
  J. 175 (2026) 1345–1361. The supplement does not use it.
- **Recommendation:** rewrite all 12 sites with the edition's keys. `bibliography.md` deliberately has no [Hin26b]
  entry.

**[Hin23b] has two meanings.** It means our [Hin23b] (Gluing I) everywhere except `proof5/PART-II-G-NASHMOSER.md:523`.
- There, "[Hin23b] ... Lemma 3.33" is [Hin26c]'s key for *Exterior stability of Minkowski space*, which is our
  [Hin23a]. The same lemma is cited as "[Hin23a] Lemma 3.33" in `proof5/PART-IV2-TAME.md:225`.
- **Recommendation:** rekey that one site to [Hin23a].

**Keys that differ between the sources, with no conflict in the supplement as far as checked:**
- [HV15]: Haber–Vasy in Bib(Hin26). Hintz–Vasy, Anal. PDE 8 (2015), in Bib(Hin26a), Bib(Hin26c) and Bib(Hin23c). The
  supplement uses it only through [Hin26] (`proof5/PART-III-G-SPECTRAL.md:23`, 29 and 951), so it means Haber–Vasy.
- [Hin23a]: in Bib(Hin26c) it is the 0-calculus paper. The supplement renamed that to [0C].
- [Hin26c]: in Bib(Hin26c) it is the scaled bounded geometry paper (renamed [SBG]), and in Bib(Hin26a) it is our
  [Hin26]. The supplement's quotations from [Hin26] use our sense (`N1STAR-PROOF.md:6467`).
- [Tay11] and [Tay11a] are different works: PDE III from [Hin23a]'s list, and PDE I from [Hin26c]'s. Bib(Hin26c) calls
  PDE III [Tay11b]. Both keys are kept.

**Works with two keys.** Each alias stays in `bibliography.md` as a "See" line. Collapsing them in the text is
recommended.

| Kept key | Alternative key | Where the alternative is used |
|---|---|---|
| [CTG23] | [CTWG23] | `FAMILIES5.md:408` and 7 more uses |
| [HL18e] | [HL17] | `N1STAR-LOG.md:841`, `ROUTES-OPEN.md:280` and `:662` (5 uses) |
| [Sbi15] | [Sbi13] | `N1STAR-PROOF.md:1008`: the same arXiv:1309.7591 |
| [Hin26d] | [SBG] | 81 uses, chiefly in `proof5/PART-II-A*.md`; `proof5/PART-II-A-SETUP.md:11` states the identity |
| [Hin23e] | [0C] | 32 uses, chiefly in `proof5/PART-II-F-IOTA.md`; line 26 states the identity |
| [Hö85] | [Ho85] | `N1STAR-LOG.md:5024` |
| [Sch13] | [Sch10] | Retired at D47; mentioned only as retired (`N1STAR-LOG.md:855`, `:884`, `ROUTES-OPEN.md:664`) |

## 6. Uncited entries, entries cited only in the working logs, and works named without a key

**[HL18e] is not cited in the paper's text.**
- The paper keeps it only to tell it apart from [HL18].
- The supplement cites it as [HL17], 5 times, in `N1STAR-LOG.md` and `ROUTES-OPEN.md` only.
- **Recommendation:** keep the entry under [HL18e] and rekey [HL17] to [HL18e]. If the edition leaves out the two log
  files, drop the entry, or keep it with one clause saying it is listed to tell it apart from [HL18].

**Keys used only in the working logs** (`N1STAR-LOG.md` and `ROUTES-OPEN.md`):
- [AN00], [DHRT21], [HL17], [Ho85], [Hun15], [KK25], [KS17], [LR17] and [Sch10].
- If the logs are not printed:
  - [AN00] stays cited, because `proof5/PART-III-G2-IOTA.md:409` names the work inline. **Recommendation:** replace
    that inline citation with [AN00].
  - [Ho85] stays cited through [Hö85].
  - **[DHRT21], [Hun15], [KK25], [KS17] and [LR17] become uncited and should be dropped.**

**Works named in the paper without a key.** The paper names Burnett and Isaacson at lines 57, 64, 238 and 735. Its
section 10 bullet (line 2102) names Burnett 1989, Isaacson 1968 and Choquet-Bruhat 1969.
- All four were verified by Crossref, and the identifiers the paper prints match.
- They are added under the proposed keys [Bur89], [Isa68a], [Isa68b] and [CB69].
- **Recommendation:** cite them by key where they are named. If not, remove the four entries.

**Other works the supplement names without a key, deliberately not added:**
- the unkeyed rows of the sourcing table at `N1STAR-PROOF.md:1008-1020`: Bahouri–Chemin arXiv:math/0304390, Rendall
  arXiv:gr-qc/0505133, and lecture notes by Holzegel and Luk;
- "Riesz-Schauder" (`GAUGEDECAY5.md:4891`, 4903 and 5206). This is F. Riesz's standard theory. The analytic Fredholm
  theorem used beside it is [RS1] Thm VI.14.

## 7. The items the coordinator asked for (each verified, with the lines that cite it)

1. **[BGP] Corollary 3.2.4**, at `GAUGEDECAY5.md:1088`. [BGP] Theorem 3.2.11 is also cited, at `GAUGEDECAY5.md:3151`
   and 3154.
   - Bär, Ginoux and Pfäffle, *Wave equations on Lorentzian manifolds and quantization*, Eur. Math. Soc. (2007),
     doi:10.4171/037, arXiv:0806.1036v1.
   - Corollary 3.2.4 (uniqueness for the Cauchy problem with vanishing data) was found in the arXiv text.
   - The record cites the book's page numbers (`proof5/PART-IX-GAUGE.md:88`).
2. **[CS06] Theorem 2**, at `FAMILIES5-VLASOV.md:92`, which has the quotation, and at 270 and 283 (Proposition L′).
   Also at `FAMILIES5-AXIS.md:185`.
   - Corvino and Schoen, J. Differential Geom. 73 (2006) 185–217, doi:10.4310/jdg/1146169910.
   - Theorem 2 was found in arXiv:gr-qc/0301071v1.
3. **Riesz's Green function for the 4+1 wave equation**, in `GAUGEDECAY5.md` Lemma R7.2 at line 3322. It is
   used again as "Riesz's interior coefficient" at lines 3939, 3984, 4614, 5386, 5905, 6462 and 7016.
   - **The original:** the new key [Rie49], M. Riesz, *L'intégrale de Riemann–Liouville et le problème de Cauchy*,
     Acta Math. 81 (1949) 1–222, doi:10.1007/BF02395016 (Crossref).
   - **A textbook statement:** [BGP] §1.2, Definition 1.2.1 and Proposition 1.2.4 (3) and (7), where R₊(2) is the
     advanced fundamental solution of □.
   - **The constant agrees with the lemma.** In spacetime dimension n = 5, BGP's constant is C(2,5) = −1/(4π²). So
     R₊(2) = −(4π²)⁻¹ (t² − r²)^(−3/2) inside the future cone, which is exactly the lemma's E₄ (computed here). The
     edition can cite "[BGP] Prop. 1.2.4, after [Rie49]".
4. **Hollands–Wald**, at `FAMILIES5-R8.md:7`, 43, 91 and 341–346 (R8.7).
   - The new key [HW13]: S. Hollands, R. M. Wald, *Stability of black holes and black branes*, Comm. Math. Phys. 321
     (2013) 629–680, doi:10.1007/s00220-012-1638-1, arXiv:1201.0463 (Crossref and INSPIRE).
   - The record says the identification of E with their canonical energy "is standard, but it is not READ here and
     nothing here uses it".
   - So the edition should cite it only as a remark.
5. **The Vlasov literature.**
   - At `FAMILIES5-FULL.md:403-453`, every work already has a verified entry:
     - [HL18] (line 405), [HL19] (414), [HL25] (422) and [Tou24] (429);
     - [Tou23a] and [Tou23b] (438–439, by arXiv id) and [LR20] (441).
   - In section 1 of `FAMILIES5-VLASOV.md`, the works are:
     - [HL25] (69), [Rac16] (86), [CS06] (92) and [CD03] (98), all already in the list;
     - Kato 1975 (104, also 52 and 358), which is the one new entry.
   - The new key [Kat75]: T. Kato, *The Cauchy problem for quasi-linear symmetric hyperbolic systems*, Arch. Ration.
     Mech. Anal. 58 (1975) 181–205, doi:10.1007/BF00280740 (Crossref). The record notes it was "not read at source",
     and proves its own Theorem K instead.
   - [IT20], cited with Theorem K (`FAMILIES5-VLASOV.md:327`), is in the list.
   - The "textbook elliptic regularity theorem" (`FAMILIES5-VLASOV.md:52-53`) is not named, so it gets no entry. The
     needed Lemma E is proved in the file.
