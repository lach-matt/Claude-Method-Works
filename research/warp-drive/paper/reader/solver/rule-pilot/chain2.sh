#!/bin/bash
cd /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/srule
while pgrep -f chain.sh > /dev/null; do sleep 5; done
nice -n 19 g++ -O2 -march=native -fopenmp -std=c++17 -DUSE_QD -DFXL=6 -I/home/user/Claude-Method-Works/research/warp-drive/paper/reader/solver -o fxpilot2_q6 fxpilot2.cpp > build2.log 2>&1
echo "built $(date)" > chain2.log
OMP_NUM_THREADS=1 nice -n 19 ./fxpilot2_q6 p1_M160.cfg 100 0 > run2_M160.out 2> run2_M160.err
echo "M160 long done $(date)" >> chain2.log
