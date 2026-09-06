"""AUDIT 25 -- GROUNDING. Does a named external source use this coordinate as a term?
Audit 22 compares a rung to a theorem's meaning of the same word. If NO source names
the term, the pair never enters audit 22's table and the coordinate is invisible to it."""
from collections import Counter
IDX={
 'V1 laws (15)':[
  ('X_exp','Colladay-Kostelecky; Buniy; Hartman','grounded'),
  ('X_spon','Arkani-Hamed et al; Cheng et al','grounded'),
  ('Sc','Tsirelson; Bell; CHSH','grounded'),
  ('IC','Pawlowski et al','grounded'),
  ('U_open','Banks-Susskind-Peskin; Nikolic','grounded'),
  ('U_ghost','Ostrogradsky; Sbisa','grounded'),
  ('NEC_pt','Buniy-Hsu-Murray; Ford-Roman','grounded'),
  ('NEC_ach','Graham-Olum; Wall','grounded'),
  ('L_dyn','Weinberg; Polchinski','grounded'),
  ('L_kin','Abrams-Lloyd','grounded'),
  ('SD_obs','Soulas; Sorkin','grounded'),
  ('SD_field','Burgoyne; Luders-Zumino','grounded'),
  ('DNc','Wootters-Zurek; Dieks','grounded'),
  ('DNd','Rastegin; Bennett et al','grounded'),
  ('EOM','Ostrogradsky; Creminelli et al','grounded')],
 'Lambda (13)':[
  ('n','Condon-Shortley','grounded'),('l','Condon-Shortley','grounded'),
  ('k','Condon-Shortley','grounded'),
  ('q','NONE LOCATED','UNGROUNDED'),
  ('e','as n','grounded'),('f','as l','grounded'),('g','as k','grounded'),
  ('2S','Condon-Shortley','grounded'),("2S'",'Condon-Shortley','grounded'),
  ('2J','Condon-Shortley','grounded'),
  ('2K','NIST / IVOA jK coupling','grounded'),
  ('v','Racah','grounded'),
  ('L','Racah (used, not indexed)','grounded but ABSENT')],
 'V3 geometry (5)':[
  ('FLAT','Hawking-Ellis; Penrose','grounded'),('CONN','standard topology','grounded'),
  ('HYP','Hawking-Ellis','grounded'),('GEN','Hawking-Ellis singularity theorems','grounded'),
  ('ASYM','Hawking-Ellis','grounded')],
 'V6 solution (4)':[
  ('SC','Graham-Olum; the semiclassical Einstein equation','grounded'),
  ('HAD','Hadamard condition, standard','grounded'),
  ('ACH','Graham-Olum; standard causal structure','grounded'),
  ('REG','no sharp definition located','WEAK')],
 'null surface (6)':[
  ('THETA','Raychaudhuri; Ashtekar NEH','grounded'),
  ('SIGMA','Raychaudhuri','grounded'),
  ('STAT','Killing horizon, standard','grounded'),
  ('COMP','geodesic completeness, standard','grounded'),
  ('ACH','standard','grounded'),('TOP','Ashtekar NEH (S^2 x R)','grounded')],
 'charger index (6)':[
  ('TRIG','MINE','UNGROUNDED'),('CUR','MINE','UNGROUNDED'),('JUR','MINE','UNGROUNDED'),
  ('VOC','MINE','UNGROUNDED'),('V1','MINE','UNGROUNDED'),('FIRE','MINE','UNGROUNDED')],
 'axis index (7)':[
  ('rungs','MINE','UNGROUNDED'),('exposure','MINE','UNGROUNDED'),('lattice','MINE','UNGROUNDED'),
  ('conflation','MINE','UNGROUNDED'),('measured','MINE','UNGROUNDED'),
  ('in-deg','MINE','UNGROUNDED'),('out-deg','MINE','UNGROUNDED')],
 'measure index (2)':[
  ('FAITH','order theory: a faithful map','grounded'),
  ('CARD','standard','grounded')],
 'audit index (4)':[
  ('LEFT','MINE','UNGROUNDED'),('RIGHT','MINE','UNGROUNDED'),
  ('AUTO','MINE','UNGROUNDED'),('OUT','MINE','UNGROUNDED')],
}
print('  AUDIT 25 -- GROUNDING')
print()
print('  %-22s %6s %10s %12s %s' % ('index','terms','grounded','ungrounded','verdict'))
tot=Counter(); META=[]
for k,v in IDX.items():
    g=sum(1 for _,_,s in v if s.startswith('grounded'))
    u=sum(1 for _,_,s in v if s=='UNGROUNDED')
    w=sum(1 for _,_,s in v if s=='WEAK')
    tot['g']+=g; tot['u']+=u; tot['w']+=w
    verdict='fully grounded' if u==0 and w==0 else ('ENTIRELY UNGROUNDED' if u==len(v) else 'mixed')
    if u==len(v): META.append(k)
    print('  %-22s %6d %10d %12d %s' % (k,len(v),g,u,verdict))
print()
print('  totals: %d grounded, %d ungrounded, %d weak, of %d terms'
      % (tot['g'],tot['u'],tot['w'],tot['g']+tot['u']+tot['w']))
print()
print('  ENTIRELY UNGROUNDED INDICES')
for m in META: print('     %s' % m)
print()
print('  AND THEIR MEASURED BEHAVIOUR')
B={'charger index (6)':(6,192,3.1,25,'open, E uninformative'),
   'axis index (7)':(9,5184,0.17,499,'open, E uninformative'),
   'audit index (4)':(5,24,20.8,5,'open, E uninformative')}
print('  %-22s %6s %8s %9s %6s %s' % ('index','cells','box','density','E','verdict'))
for k in META:
    c,b,d,e,v=B[k]; print('  %-22s %6d %8d %8.2f%% %6d %s' % (k,c,b,d,e,v))
print()
print('  THE CORRELATION')
print('     every entirely-ungrounded index is OPEN and below the density threshold.')
print('     every fully-grounded index built here is CLOSED: V3, V6, null surface.')
print('     V1 and Lambda are grounded and open/closed respectively - so grounding does')
print('     NOT determine closure. but the three meta-indices are the only ones that are')
print('     both ungrounded and uninformative, and they are the ones whose coordinates')
print('     I chose with nothing external to answer to.')
print()
print('  WHY AUDIT 22 CANNOT SEE THIS')
print('     audit 22 pairs a coordinate with a theorem that NAMES it.')
print('     an ungrounded coordinate is named by no theorem, so it generates no pair.')
print('     it passes audit 22 by being absent from it.')
print('     -> 17 of the %d terms here are invisible to audit 22 entirely.' % (tot['g']+tot['u']+tot['w']))