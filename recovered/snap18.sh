#!/bin/bash
# snapshot: refuse to shrink
S=/home/claude/s18; mkdir -p $S
n_new=$(wc -l < t7b.jsonl); n_old=$( [ -f $S/t7b.jsonl ] && wc -l < $S/t7b.jsonl || echo 0)
[ "$n_new" -lt "$n_old" ] && { echo "REFUSE: $n_new < $n_old"; exit 1; }
cp t7b.jsonl t7b_hf.py t7b_run.py t7b_gate.py shoot_x.c $S/ && echo "snap ok rows=$n_new"