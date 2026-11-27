#!/bin/bash
cd /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/srule
while pgrep -f "fxpilot_q6 p1.cfg" > /dev/null; do sleep 5; done
echo "chain start $(date)" > chain.log
nice -n 19 python3 /home/user/Claude-Method-Works/research/warp-drive/paper/reader/solver/consts.py 16 24 160 c_16_24_160.bin >> chain.log 2>&1
echo "consts done $(date)" >> chain.log
OMP_NUM_THREADS=1 nice -n 19 ./fxpilot_q6 p1_M160.cfg 45 0 > run_M160.out 2> run_M160.err
echo "M160 done $(date)" >> chain.log
OMP_NUM_THREADS=1 nice -n 19 ./pconv_q p1.cfg c_12_18_80.bin 12 18 /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/bsolv/s2A_dd/c_16_24_80.bin 16 24 c_20_30_80.bin 20 30 c_24_36_80.bin 24 36 > pconv.out 2> pconv.err
echo "pconv done $(date)" >> chain.log
