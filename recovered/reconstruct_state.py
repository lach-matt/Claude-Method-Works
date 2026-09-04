#!/usr/bin/env python3
"""reconstruct_state.py -- the reconstruction's state, under zeno.

Register 633: the reconstruction edits ran outside State/step. They are file
surgery rather than computation, but §2.20 says nothing runs unbounded, and a
250,000-character rewrite qualifies. This records where it stands, checkpointed.
"""
import re, os
from zeno import State, step
def run():
    s=open("The Method 1.5.md",encoding="utf-8").read()
    o=open("/tmp/orig.md",encoding="utf-8").read() if os.path.exists("/tmp/orig.md") else s
    RS=s.rindex("## 28. Withdrawals"); RE_=s.rindex("## 29.")
    ent=[int(x) for x in re.findall(r"^ {0,3}(\d{3})\. ",s[RS:RE_],re.M)]
    oRS=o.rindex("## 28. Withdrawals"); oRE=o.rindex("## 29.")
    oent=[int(x) for x in re.findall(r"^ {0,3}(\d{3})\. ",o[oRS:oRE],re.M)]
    aB=s.rindex("# Appendix B"); bB=s.rindex("# Appendix C")
    oaB=o.rindex("# Appendix B"); obB=o.rindex("# Appendix C")
    return dict(before=len(o), after=len(s), saved=len(o)-len(s),
                reg_before=len(o[oRS:oRE]), reg_after=len(s[RS:RE_]),
                ent_before=len(oent), ent_after=len(ent),
                appB_before=obB-oaB, appB_after=bB-aB,
                ascending=ent==sorted(ent), lo=min(ent), hi=max(ent))
with State("reconstruct_state") as st:
    R=step(st,"reconstruction state",run,budget=120)
print(f"  {'':<26}{'before':>10}{'after':>10}{'saved':>10}")
print(f"  {'whole book':<26}{R['before']:>10,}{R['after']:>10,}{R['saved']:>10,}")
print(f"  {'chapter 28':<26}{R['reg_before']:>10,}{R['reg_after']:>10,}{R['reg_before']-R['reg_after']:>10,}")
print(f"  {'appendix B':<26}{R['appB_before']:>10,}{R['appB_after']:>10,}{R['appB_before']-R['appB_after']:>10,}")
print(f"\n  register entries {R['ent_after']} of {R['ent_before']}   "
      f"{R['lo']}–{R['hi']}   ascending {R['ascending']}")