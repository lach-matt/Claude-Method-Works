for l in 1 2 3 4 5 6; do python3 v5c.py 89 core --l $l > v5c-89-core-l$l.log 2>&1; done
python3 v5c.py 89 ent --occ > v5c-89-ent-occ.log 2>&1
python3 v5c.py 89 run --occ > v5c-89-run-occ.log 2>&1
python3 v5d.py 89 ent > v5d-89-ent.log 2>&1; python3 v5d.py 89 run > v5d-89-run.log 2>&1
echo DONE89 > run89.done