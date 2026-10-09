---
name: mathematica
description: "Evaluate Wolfram Language (Mathematica syntax): symbolic algebra, series, integrals, ODEs, exact simplification. Runs locally through Mathics3, an open-source Wolfram Language interpreter (a subset of Mathematica, not Mathematica itself), or through the official Wolfram connector (connected; Wolfram 15.0.1). Trigger: /mathematica, or when a derivation is best checked in Wolfram Language."
---

# /mathematica

Three routes to the Wolfram Language. They differ in what they can do, and **a result must say which route
produced it.**

## 1. Local, available now: Mathics3 (`wl`)

Mathics3 is a free, open-source interpreter for the Wolfram Language, built on SymPy and mpmath. It installs from
pypi, which the egress proxy allows. It covers much of core Mathematica: `Series`, `Integrate`, `D`, `DSolve`,
`Solve`, `Simplify`, `N[..., 30]`. It is **not** Mathematica, and some functions are missing or return unevaluated.

```
.claude/skills/mathematica/wl 'Series[1/((1 - 2 m/r)^2/(1 - 3 m/(2 r))), {m, 0, 1}]' 'N[Zeta[3], 30]'
.claude/skills/mathematica/wl -f derivation.wl      # use Print[] inside the file
WL_TIMEOUT=1200 .claude/skills/mathematica/wl '...' # default timeout 600 s
```

Each argument is evaluated and printed on its own line. The wrapper installs `mathics3` and `requests` on first use.

**Quirks the wrapper already handles:**
- only the first `-c` is run;
- `-script` prints nothing;
- an open stdin hangs the process.

If you call `mathics` directly, close stdin (`</dev/null`) and put everything in one `-c`.

**Labelling (the board's rules).**
- A Mathics3 result is **computed (Mathics3)**, never "Mathematica".
- Where a result carries weight, cross-check it in SymPy or numerically. Mathics3 delegates much of its algebra to
  SymPy, so the two are not fully independent; an exact numeric check is the stronger control.
- An unevaluated return is not a result. Say so, and fall back to SymPy.

**Checked on first install (2026-10-09).** Each of these came back correct:
- `Integrate[1/(2 (2 r - 3)^2), {r, 2, Infinity}]` gave `1/4`, eq. (17)'s ∫ρ = m/4 (SIM1 S5);
- `D[Log[F/H], r]` for eq. (17) simplified to `-1/(6 - 7 r + 2 r^2)`, SIM1 S4's −1/((r−2)(2r−3));
- `Series` of 1/H gave `1 + 5 m/(2 r)`;
- `DSolve`, `Solve` and `N[Zeta[3], 30]` were also checked.

## 2. Real Wolfram Language: the official Wolfram connector (connected 2026-10-09)

This is Wolfram's own kernel, running remotely. It needs no sign-in. Load its tools with ToolSearch:
- `mcp__Wolfram__WolframLanguageEvaluator`: evaluates Wolfram Language code. The kernel is stateless, so put
  definitions and results in one call. The default time limit is 60 s.
- `mcp__Wolfram__WolframAlpha`: natural-language queries, for constants, data and entities.
- `mcp__Wolfram__WolframContext`: semantic search over Wolfram documentation.

**Label its results** "computed (Wolfram 15.0.1, connector)". Prefer this route to Mathics3 whenever a result carries
weight, or when Mathics3 lacks a function. Mathics3 stays the offline route, and an independent cross-check, since the
two engines share no code.

**Checked on connection (2026-10-09).** `$Version` returned "15.0.1 for Linux x86 (64-bit) (July 2, 2026)". These
agreed with Mathics3 and SymPy:
- 1/H to first order gave 1 + 5m/(2r);
- d ln(F/H)/dr gave 1/(−6 + 7r − 2r²);
- ∫ gave 1/4;
- the warp null-energy expression for AdS₄-sliced AdS₅ gave 0.

## 3. A local Wolfram Engine: blocked here

The free Wolfram Engine for developers would give a full local kernel. In this environment it is blocked twice over:
- the egress proxy refuses `wolfram.com`, `account.wolfram.com` and `wolframcloud.com` (403, checked 2026-10-09);
- the engine needs activation with a Wolfram ID.

**To enable it,** add those hosts under the environment's Network access (Allowed domains). Then install and activate
the engine in the environment's setup script, which runs at each session start. The download is several GB.

## Persistence

The cloud container is ephemeral, so pip installs vanish with it. `wl` reinstalls Mathics3 on first use, which takes
about 30 s. To skip that, add `pip install mathics3 requests` to the environment's setup script.
