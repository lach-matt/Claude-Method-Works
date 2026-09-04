# INTAKE — the incoming Gemini material

*Written at register 1614, before anything arrives, so the rules are set by the
protocol and not by what turns up.*

## The problem this file exists to prevent

The register's standing rule is **all data from source, never transcribe**
(registers 1187, 1541, and enforced at 1603 when a greedy regex read 289,119 as
9,119). A conversation with another model is **not a source**. It is a
secondary account, and its confident sentences look exactly like its uncertain
ones.

**So nothing from these conversations enters an artefact as data.** What they
can carry is:

| kind | what it is | what happens to it |
|---|---|---|
| **POINTER** | a paper, author, year, dataset, term of art | goes to the queue as a thing to FETCH from source |
| **CLAIM** | an assertion about physics or mathematics | goes to the board as a thing to TEST |
| **FRAME** | a way of seeing a problem, a reframing | usable immediately — a frame is not a fact |
| **NUMBER** | any figure, coefficient, energy, count | **REFUSED** unless traced to a primary source |

The fourth row is the one that will bite. A number recalled by a model is
indistinguishable in appearance from one read off a table, and this project
has already registered five sessions' worth of faults from exactly that
confusion — mine, not anyone else's.

## What I will do with each input

1. **Sort it** into the four kinds above, and say which is which before acting.
2. **Pointers** get a queue line each, with what would confirm them.
3. **Claims** get tested against what is already held, and the test is stated
   before it runs so it can fail.
4. **Frames** get applied and their consequences computed.
5. **Numbers** get held in `captures/GEMINI-UNVERIFIED.tsv`, marked
   `unverified`, and used for NOTHING until a primary source is reached.

## What I need alongside the material

For anything that should become data rather than a pointer:

- **the URL or DOI** the model was working from, if it named one
- **or M's own judgement** that a figure came from a source he has seen

Either is enough. Neither is required for pointers, claims or frames — those
can arrive as-is and be useful immediately.

## Where things will go

    captures/GEMINI-UNVERIFIED.tsv   numbers, held and unused
    QUEUE-LOG.md                     pointers, one line each
    BOARD.md                         claims to test
    REGISTER-DATA.md                 only what has been tested or fetched

## The one thing that will not happen

No input will be summarised into an artefact and then cited later as though
the artefact had established it. That is how a secondary account becomes a
primary one by attrition, and it is the failure mode this project's whole
provenance apparatus exists to prevent.
