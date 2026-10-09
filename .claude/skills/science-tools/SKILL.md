---
name: science-tools
description: "Install and run the board's local science toolchain through one script, `sci`. Covers GR tensor algebra (EinsteinPy, GraviPy, pytearcat, OGRePy, Maxima ctensor, Cadabra2, REDUCE excalc, SageManifolds), CAS work (PARI/GP, FORM, GiNaC), provers (cvc5, z3, Metamath set.mm, SPASS, QEPCAD-B, Lean 4 core, Coq), ODE/PDE numerics (py-pde, findiff, diffrax/jax, pygro, SumOfSquares, Dedalus), offline physical data (PDG, CODATA via astropy/scipy, mendeleev, radioactivedecay, xraydb), CAMB/CLASS, GW codes (lalsuite, qnm, pykerr, pybhpt), PDF/OCR tools for verbatim READs, and a relocated TeX Live. Use it when a derivation, check or number needs a real engine, or when you need to cross-check a result in a second engine."
---

# science-tools: the `sci` toolchain

```
.claude/skills/science-tools/sci list                  # groups, contents, what is installed
.claude/skills/science-tools/sci install gr cas        # idempotent; also: default, all; --force to redo
.claude/skills/science-tools/sci run cas maxima --very-quiet --batch=f.mac </dev/null
.claude/skills/science-tools/sci run gr python my_metric.py
.claude/skills/science-tools/sci check                 # one small known-answer computation per installed group
.claude/skills/science-tools/sci env tex               # print the environment; `source` it in another shell
.claude/skills/science-tools/sci dryrun numerics       # what pip WOULD change in the system python (it never does)
.claude/skills/science-tools/sci du | sci remove <group> | sci clean
```

Everything goes under **`SCI_ROOT`** (default `/root/sci`), never into the repository. The script refuses a
`SCI_ROOT` inside the repo or in a system or user-site path. Layout:
- `venv/<group>/`: pip venvs;
- `deb/<group>/`: extracted Ubuntu debs;
- `opt/reduce/`, `conda/envs/<group>/`;
- `bin/<group>/`: wrapper scripts, callable by absolute path from anywhere;
- `env/<group>.sh`, `state/` (stamps, `pip freeze`, deb md5 lists, dry-run reports) and `logs/`.

## Routes used, and only these

- **PyPI**: pip into a venv, always with `PYTHONNOUSERSITE=1` and no cache. The script never uses `--user`, and
  it never touches the system Python (`/usr/local/lib/python3.11`) or `~/.local`.
  Before each pip group, `sci install` runs a `pip --dry-run` in a throwaway `--system-site-packages` probe venv.
  It reports whether numpy 2.4.6, scipy 1.17.1, sympy 1.14 or mpmath 1.3 *would* change in the system python.
  The report is in `state/<group>.dryrun`. Every group checked so far reports "unchanged".
- **Ubuntu archive** (archive.ubuntu.com and security.ubuntu.com over HTTPS), using a private apt state in
  `SCI_ROOT/apt`.
  - The dependency set comes from a simulated `apt-get -s install`, which prints a plan and installs nothing.
  - The packages are then fetched with `apt-get download` and unpacked with `dpkg-deb -x` into
    `deb/<group>`.
  - The script never runs a real `apt-get install` or `dpkg -i`, and never changes the system dpkg database.
- **conda-forge** (`conda.anaconda.org`) via micromamba, which is itself fetched from conda-forge. The package
  cache is deleted after every env is created.
- **SourceForge**: REDUCE's freestanding build, with its md5 pinned.
- **Nothing from GitHub** or any GitHub-content mirror. See the excluded list at the end.

## Groups and verification status

**VERIFIED** means `sci install <group>` ran from an empty `SCI_ROOT` on 2026-10-09, and `sci check <group>` then
passed. The one-line results are the check's own output. **NOT YET VERIFIED** means the install code is written but
was not run end to end here. Run `sci install <g> && sci check <g>` before relying on it, and fix the group if it
fails.

| group | status | what it gives | measured size |
|---|---|---|---|
| `gr` | **VERIFIED** | EinsteinPy, GraviPy, pytearcat (py3.11 venv); OGRePy (py3.13 venv, command `ogrepy-python`) | 1217 MB |
| `cas` | **VERIFIED** | Maxima 5.46 + ctensor/itensor, Cadabra2 2.4.5.4, PARI/GP 2.15.4, FORM 4.3 (`form`, `tform`), GiNaC `ginsh`, REDUCE 2026-03 (`reduce` = `redpsl`) with EXCALC/Redlog | 376 MB |
| `provers` | **VERIFIED** | cvc5 1.4.2 + z3 5.1 (venv), Metamath 0.195 + set.mm, SPASS 3.9, QEPCAD-B 1.74 (+ Singular 4.3.2) | 243 MB |
| `numerics` | **VERIFIED** | py-pde, findiff, diffrax + jax (CPU), pygro, SumOfSquares (PICOS + cvxopt), scipy, matplotlib | 1096 MB |
| `data` | NOT YET VERIFIED | pdg (PDG 2026 sqlite), particle, mendeleev, periodictable, radioactivedecay, xraydb, astropy, matplotlib | ~0.4 GB est. |
| `cosmo` | NOT YET VERIFIED | CAMB (wheel), CLASS/classy (sdist compiled with the system gcc, about 80 s) | ~0.3 GB est. |
| `gw` | NOT YET VERIFIED | lalsuite, qnm, pykerr, pybhpt | ~0.6 GB est. |
| `lit` | NOT YET VERIFIED (debs prototyped) | poppler `pdftotext`/`pdftoppm`, tesseract 5.3.4 (eng, deu), pdfplumber, pypdf, pymupdf, pylatexenc, bibtexparser, TexSoup | ~0.2 GB est. |
| `tex` | NOT YET VERIFIED (relocation prototyped) | TeX Live 2023 from debs: latex-base/recommended/extra, pictures (TikZ), fonts-recommended, science (physics, siunitx), publishers (revtex4-2) | ~0.5 GB est. |
| `sage` | NOT YET VERIFIED | passagemath-symbolics + passagemath-maxima: SageManifolds and Sage's symbolic ring | ~1.6 GB est. |
| `dedalus` | NOT YET VERIFIED | Dedalus 3 from a conda-forge env with FFTW/MPI (command `dedalus-python`) | ~0.9 GB est. |
| `lean` | NOT YET VERIFIED | Lean 4 core from conda-forge `lean4` (Mathlib is excluded) | ~3.5 GB est. |
| `coq` | NOT YET VERIFIED | Coq 8.18 + Interval, Coquelicot, Flocq (Ubuntu debs; private `findlib.conf`, `COQLIB`) | ~1.2 GB est. |

**Verified check output (2026-10-09):**
- `gr`:
  - EinsteinPy, GraviPy, pytearcat and OGRePy each gave the 5D Randall–Sundrum Ricci scalar R = −20k²;
  - EinsteinPy gave the Schwarzschild Ricci tensor as 0.
- `cas`:
  - Maxima ctensor gave RS5 R = −20k²;
  - Cadabra2 gave Schwarzschild `R_{a b} = 0`;
  - gp gave `lindep([Pi^2,zeta(2),1]) = [1, -6, 0]~`;
  - FORM gave Tr(γ^μγ^νγ^ργ^σ) = 4(δδ − δδ + δδ);
  - ginsh gave the series of √(1−2M/r) correctly;
  - REDUCE excalc gave RS5 R = −20k².
- `provers`:
  - cvc5 gave x² = 2, x > 0 as sat, with an algebraic-number model;
  - z3 gave the AM-GM refutation as unsat;
  - Metamath verified set.mm `2p2e4 |- ( 2 + 2 ) = 4`;
  - SPASS found a proof of transitivity;
  - QEPCAD gave (∃x)[x² + bx + c = 0] ⇔ `4 c - b^2 <= 0`.
- `numerics`:
  - findiff gave max|f''+sin| = 8.2e-5;
  - diffrax gave x(10) = −0.839071529041 against cos 10 = −0.839071529076;
  - py-pde gave the heat equation u(π/2,1) = 0.367548 against e⁻¹;
  - pygro gave the Alcubierre bubble-centre geodesic x = v_s t to 8.9e-16;
  - SumOfSquares found (x² + y² + 1)·Motzkin SOS-feasible (status optimal).

**What was prototyped but not run through `sci`.** On 2026-10-09 the same deb routes were exercised by hand:
- `lit`: pdftotext reproduced a generated PDF verbatim, and tesseract OCR'd a `pdftoppm` render of it correctly
  (one `|`→`l` slip).
- `tex`: the relocated pdflatex compiled amsmath + TikZ + hyperref in 1.2 s. That needed three things:
  - a private `texmf.cnf`;
  - `updmap-sys` run on Debian's fontmap snippets, with `PERL5LIB` set to `tlpkg`;
  - real `ls-R` files, because the shipped ones are dangling symlinks into `/var/lib/texmf`.

`install_tex` encodes exactly these steps, but it has not been run as a whole.

**Disk.** The four verified groups take about 3.0 GB in `/root/sci`, and that is what is installed now. The default
set (`sci install default`, which is everything except sage, lean, coq and dedalus) is estimated at about 5 GB.
Install the heavy optional groups only when needed, and `sci remove` them afterwards.

## Gotchas the script handles, and ones you must handle

- **Maxima** waits forever on stdin if a sign question comes up. Always `assume(...)` the signs, and always run with
  `--batch=f.mac </dev/null`. The wrapper cannot add the redirect for you.
- **Cadabra2** is a Python 3.12 module. The `cadabra2` wrapper runs it under the `cas312` venv, which has sympy.
  `cadabra-python` gives you that interpreter with `cadabra2` importable.
- **FORM**: only `form` and `tform` are installed. `parform` would pull in OpenMPI.
- **REDUCE**: use `reduce` (`redpsl`). `redcsl` needs X11's `libXft`, which is not installed.
- **QEPCAD** needs `$qe` and a `default.qepcadrc` that points at the private Singular. The wrapper sets both;
  without them QEPCAD hangs.
- **pytearcat** calls Jupyter's `display()`. Shim it first with `builtins.display = lambda *a, **k: None`.
- **OGRePy** needs Python ≥ 3.13, so it gets its own venv. It prints notebook banners and checks PyPI on import.
- **EinsteinPy** returns float coefficients in the Einstein tensor (`6.0*k**2`). `nsimplify` before an exact
  comparison.
- **mendeleev, radioactivedecay and pandas** need `python-dateutil` inside the venv when run under `python -I`.
  The `data` group installs it explicitly.
- **pygro**: start a geodesic slightly off a symmetry axis, because exactly r = 0 gives NaN.
- **jax**: set `jax.config.update('jax_enable_x64', True)` for precision work.
- **qnm** writes a cache. The `gw` env points `XDG_CACHE_HOME` at `SCI_ROOT/cache`, not `~/.cache`.
- **Dedalus** must run with `OMP_NUM_THREADS=1` (`dedalus-python` sets it).
- **Lean** comes without Mathlib. Core Lean (`Nat`, `omega`, `simp`, `decide`) only.
- **Python 3.12 members**: ten seated members in `method/` need `python3.12`, not the bare `python3`. That is
  unrelated to `sci`, so do not "fix" them with a venv.
- **Constants**: take CODATA 2022 from scipy.constants or `astropy.constants.codata2022`, and particle values from
  `pdg` (GeV). Never use `unyt`, whose G is from CODATA 2014. The Wolfram connector's electron mass is less
  precise than CODATA 2022.

## Labelling results (the board's rules)

- A tool result is labelled **computed (<tool> <version>)**, for example "computed (Maxima 5.46 ctensor)" or
  "computed (CAMB 2.0.4)". Never write it as "verified" or "derived" without the tool name.
- **A result that carries weight is cross-checked in a second, independent engine.** Name both: "computed
  (Maxima ctensor); cross-checked (Cadabra2)". Useful independent pairs:
  - curvature: Maxima ctensor, REDUCE excalc, Cadabra2, EinsteinPy/GraviPy (both SymPy-based, so one engine
    family), SageManifolds, and xAct in the Wolfram connector;
  - series and integrals: Maxima, PARI/GP, GiNaC, SymPy, Wolfram (connector);
  - Boltzmann spectra: CAMB against CLASS;
  - QNMs: qnm against pykerr;
  - proofs: z3 against cvc5, QEPCAD against Redlog.
- Engines that share code are not independent. EinsteinPy, GraviPy, pytearcat and OGRePy all sit on SymPy, and
  Mathics3 delegates to SymPy too.
- An unevaluated return, a timeout or a `FAIL` line is not a result. Say so.
- A **READ** (a verbatim quote with a page number) comes from the source text, never from a tool's paraphrase. The
  `lit` tools extract text, and the `science-databases` skill says where full text can be fetched.

## Persistence

The container is ephemeral, and `SCI_ROOT` disappears with it. `sci install` re-creates any group from the network
in about 1–8 minutes; numerics and gr are the slow ones, mostly from downloads. To have a set ready at each session
start, add a line like this to the environment's setup script:

```
SCI_ROOT=/root/sci /home/user/Claude-Method-Works/.claude/skills/science-tools/sci install gr cas provers
```

Check free disk space first: the shared disk had about 19 GB free at the end of this session.

## Not available here (needs GitHub, which this environment's network policy blocks)

These were found by the tool sweep but depend on GitHub content: github.com, codeload, raw/media/release-asset
githubusercontent hosts, `git clone` of github.com, cdn.jsdelivr.net/gh, or proxy.golang.org used for non-Go
code. They are excluded, and no workaround is offered:
- Mathlib4 (and elan, lean-interact, LeanDojo);
- CLASS built from a Go-proxy zip, hi_class, MGCAMB, EFTCAMB. Use pip `classy`/`camb` instead;
- ore_algebra from a Go-proxy zip;
- the OEIS raw data mirror;
- sxs (the SXS catalogue);
- BlackHawk and BlackMax GitHub forks;
- SpECTRE;
- Tarski;
- WarpFactory (source read through a GitHub reader);
- cobaya likelihood data from GitHub (Planck native data, the DESI BAO and Pantheon+ repos);
- FeynCalc downloaded from GitHub inside the Wolfram kernel.

Also not available, for other reasons: Isabelle, Vampire and Prover9 (no allowed channel); E prover (crashes);
yices and dReal (missing native libraries); PySR (the Julia download is blocked); Ubuntu's Macaulay2 (hard-coded
paths); pycbc (it would downgrade numpy and scipy, so if it is ever needed it gets its own venv); gwpy/gwosc
strain downloads and astroquery (their hosts are refused; see `science-databases` for connector routes).
