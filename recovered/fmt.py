import sys,ast
for l in sys.stdin:
    if l.startswith('{'):
        d=ast.literal_eval(l); print(' '.join(f"{k}={d[k]}" for k in d if k not in ('kind','it','sec','el')))
    else: print(l.strip()[:120])