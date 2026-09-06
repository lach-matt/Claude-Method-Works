r 68 && g 68 'python3 nlwalk_hf.py 71 | tail -1'
r 69 && g 69 'python3 nlwalk_hfc.py 21 | tail -1'
r 70 && g 70 'CLIGHT=1e6 OUT=nlwalk_sr_gate.jsonl python3 nlwalk_sr.py 21 | tail -1'
r 71 && g 71 'python3 nlwalk_sr.py 21 | tail -1'