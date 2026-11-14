#!/bin/bash
# SessionStart (cloud sessions only) -- item 401: restore the Lean 4 connection each session.
#   sci install lean         Lean 4 core from conda-forge (~3.5 GB; skipped when already installed)
#   sci install lean4skills  the lean4 skill of cameronfreer/lean4-skills, linked into ~/.claude/skills,
#                            with its helper runtime (the one GitHub-sourced group; see the sci header)
# Then the two groups' environments go into $CLAUDE_ENV_FILE, so every shell has lean, lake and LEAN4_*.
# Idempotent; synchronous, so the tools are there before the session's first turn.
set -euo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
SCI="$CLAUDE_PROJECT_DIR/.claude/skills/science-tools/sci"
"$SCI" install lean lean4skills >&2
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  # The env file persists for the whole session and the hook fires on every startup, resume, clear and compact,
  # so append a group's block only if it is not there yet (209 duplicate blocks once overflowed bash's argument limit).
  for g in lean lean4skills; do
    grep -qF "group '$g'" "$CLAUDE_ENV_FILE" 2>/dev/null || cat "${SCI_ROOT:-/root/sci}/env/$g.sh" >> "$CLAUDE_ENV_FILE"
  done
fi
