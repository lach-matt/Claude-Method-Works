# RUNG-5 TEST, on-hand data only.  Criterion: a = 1, nu = n* = n - delta, with delta read at the
# one-electron ion of nuclear charge Z over the closed core (R 1304's charge dependence),
# entrant = least n* among Pauli-admissible subshells (excluding those the Z-1 config fills).
# Sources: R 1258 (Kr core), Spectra Compendium rows (Sc III, Ca II, K I, Ba II), DIAGONAL/FACET5 (Cs I, Fr I).
data = {
 # species: (core, Z of step it decides, observed entrant, full subshells at Z-1 among candidates, {subshell:(n,delta)})
 'K I':   ('Ar',19,'4s',[],        {'4s':(4,2.191),'4p':(4,1.727),'3d':(3,0.246)}),
 'Ca II': ('Ar',20,'4s',[],        {'4s':(4,1.8338),'3d':(3,0.6341)}),          # Ca II np not on hand
 'Sc III':('Ar',21,'3d',['4s'],    {'4s':(4,1.5848),'4p':(4,1.2861),'3d':(3,0.6538),'4f':(4,0.0450)}),
 'Rb I':  ('Kr',37,'5s',[],        {'5s':(5,3.1357),'5p':(5,2.6566),'4d':(4,1.3307),'4f':(4,0.0143)}),
 'Sr II': ('Kr',38,'5s',[],        {'5s':(5,2.7115),'5p':(5,2.3636),'4d':(4,1.4592),'4f':(4,0.0610)}),
 'Y III': ('Kr',39,'4d',['5s'],    {'5s':(5,2.4462),'5p':(5,2.1216),'4d':(4,1.3965),'4f':(4,0.1466)}),
 'Cs I':  ('Xe',55,'6s',[],        {'6s':(6,4.051),'6p':(6,3.593),'5d':(5,2.466),'4f':(4,0.033)}),
 'Ba II': ('Xe',56,'6s',[],        {'6s':(6,3.598),'6p':(6,3.241),'5d':(5,2.415),'4f':(4,0.756)}),
 'Fr I':  ('Rn',87,'7s',[],        {'7s':(7,5.07221),'7p':(7,4.59521),'6d':(6,3.42371)}),
}
hits=0;n=0
for sp,(core,Z,obs,full,d) in data.items():
    ns={k:nn-dl for k,(nn,dl) in d.items() if k not in full}
    pred=min(ns,key=ns.get); n+=1; hits+= pred==obs
    print(f"{sp:7s} {core} core  Z={Z:3d}  n*: " + "  ".join(f"{k} {v:.3f}" for k,v in sorted(ns.items(),key=lambda x:x[1])) + f"   -> {pred}  obs {obs}  {'HIT' if pred==obs else 'MISS'}")
print(f"\n{hits}/{n} on hand.  Untestable on hand (ions absent from record): La III (Z57, 5d vs 4f), Ce IV (58), Ac III (89), Th IV (90); Ra II (88, also facet 4).")
# What R 1457 refuted, for contrast: neutral-core Cs I delta applied at La (Z=57): 6s full
ns={'6p':6-3.593,'5d':5-2.466,'4f':4-0.033}; print("R 1457's object (Cs I delta at La, 6s full):", min(ns,key=ns.get), "-> not 5d; that refutation stands and is a different object")