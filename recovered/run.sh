#!/bin/bash
# run.sh -- PRIME CONTINUITY DIRECTIVE clause 3. The ONLY admissible launcher for anything
# that computes. Detaches the job so a tool-call timeout cannot orphan a running process
# invisibly, writes a receipt, and appends to SESSION-LEDGER.tsv.
#
#   bash run.sh TAG "command"     launch, return immediately with the receipt path
#   bash run.sh --poll TAG        state of that job: RUNNING / DONE rc=N, plus log tail
#   bash run.sh --list            every job this session, newest last
#
# A lost tool result is then recovered by READING, never by recalling.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
LED="$D/SESSION-LEDGER.tsv"
REC="$D/receipts"; mkdir -p "$REC"
[ -f "$LED" ] || printf 'started\ttag\trc\tended\tcommand\n' > "$LED"

case "${1:-}" in
  --list)
    cat "$LED"; exit 0 ;;
  --poll)
    T="${2:?tag}"; R="$REC/$T"
    [ -d "$R" ] || { echo "NO SUCH JOB: $T"; exit 1; }
    if [ -f "$R/rc" ]; then
      echo "DONE  $T  rc=$(cat "$R/rc")  started $(cat "$R/started")  ended $(cat "$R/ended")"
    else
      P=$(cat "$R/pid" 2>/dev/null)
      if kill -0 "$P" 2>/dev/null; then echo "RUNNING  $T  pid=$P  started $(cat "$R/started")"
      else echo "VANISHED  $T  pid=$P  -- no rc file and no process. Read the log."; fi
    fi
    echo "--- log tail ---"; tail -n "${3:-15}" "$R/log" 2>/dev/null
    exit 0 ;;
esac

T="${1:?usage: run.sh TAG \"command\"}"; shift
CMD="$*"
R="$REC/$T"; mkdir -p "$R"
date -Is > "$R/started"; printf '%s\n' "$CMD" > "$R/cmd"
setsid bash -c '
  cd "$1"; shift; R="$1"; shift
  ( eval "$@" ) > "$R/log" 2>&1
  echo $? > "$R/rc"; date -Is > "$R/ended"
  printf "%s\t%s\t%s\t%s\t%s\n" "$(cat "$R/started")" "$(basename "$R")" "$(cat "$R/rc")" \
    "$(cat "$R/ended")" "$(cat "$R/cmd")" >> "'"$LED"'"
' _ "$D" "$R" "$CMD" < /dev/null > /dev/null 2>&1 &
echo $! > "$R/pid"
sleep 1
echo "LAUNCHED $T  pid=$(cat "$R/pid")  receipt=$R"
echo "poll with:  bash run.sh --poll $T"
