# DOCKET 67 shards (fresh run on M's ruling "Start the workflow over"; Opus 5.5)
Extraction + merge: wf_b2052d90-b95 (pass A, stopped after extract/merge; 832 occurrences, 431 canonical, 165 context-only)
canonical.json rebuilt from that journal with the script's own rules; shards interleaved canonical[i::12].
shard task    run id
0  wp86trkkr  wf_45789490-3e4
1  wz63197o9  wf_1ebde2d4-a80
2  w2bmovuog  wf_d8bd2f29-877
3  wk2732wac  wf_5f7ea9cb-c55
4  w23y71x6h  wf_69570ec5-b93
5  w25ufa10t  wf_7d6a3043-164
6  wxxjzycr7  wf_17b80fe0-f4d
7  woxzcb39r  wf_0aa179d7-231
8  wof3sz7jv  wf_a012a1bd-f69
9  wrxfmoq5i  wf_787976b6-09a
10 wqof4sy03  wf_3254d88c-8b2
11 wr5wdgppc  wf_8c794de6-2ca
After all 12: collect each shard's audits (journal result, mode 'S'), then run mode 'B' with canonical [] and
prior_nonstands = every non-STANDS final grade with its rests_on_it from canonical.json -> the reopen.

Round 1 (11:5x-16:00 UTC): every shard stopped on the session limit (reset 16:30 UTC) after ~25 audits each; no
verifier ran. Round 2 resumed 16:33 UTC with the same run ids (cached audits replay):
tasks 0 w840223fw, 1 wd2lz43hd, 2 wlekyy1kv, 3 wmotyyq11, 4 wewnt2xl3, 5 wiz25n0pq, 6 w9zzeowcd, 7 wvxuz5isn,
8 weznakm6v, 9 wg8wmaelf, 10 wrqm308zy, 11 wecbjwm2s.
Unverified round-1 audit tally (audits/*.json, includes duplicates of the earlier stopped pass A):
STANDS 100, NARROWED 192, DATA-DEPENDENT 7, WRONG 1, OPEN 25.

Round 2 (16:33-17:35 UTC Sep 26): stopped on the WEEKLY limit (resets Oct 2 06:00 UTC).
Collected (round2_collected.json): 412 of 431 audited, 19 missing; 12 verifier results total.
Unverified grades: NARROWED 248, STANDS 120, OPEN 33, DATA-DEPENDENT 7, WRONG 4.
Resume after Oct 2 06:00 UTC with the same 12 run ids (cache replays the 412 audits).

Round 3 (2026-09-27, M: "Test subagents first"): a probe agent returned; shards 0-3 resumed from cache with
their run ids (tasks wius0utlb, wfc97uyel, wqbpqhqih, weejxoxl0); shards 4-11 held until these show no limit.
Round 3 cont.: shards 0-3 progressing without a limit (journals ~460 -> ~580 lines by 17:26 UTC); shards 4-7 resumed
(tasks wc9s4zx0g, wgjejs5y6, wh2tccicb, wzt78b8s2). Shards 8-11 held.
Re-audits on M-retrieved sources: 22 results in reaudit/ (one auditor each); three verifiers launched on them
(refute, re-derive, data/source identity) -> reaudit/_verify_{refute,rederive,data}.json.
