eV=1.602176634e-19; Q=17.59e6*eV
print('  WHAT 1 MW OF PROTON BEAM ACTUALLY MAKES')
for Ep,lab in [(590e6,'PSI HIPA, 590 MeV'),(800e6,'LANSCE-class, 800 MeV'),(3e9,'3 GeV, J-PARC-class')]:
    Np = 1e6/(Ep*eV)
    for y,ylab in [(0.05,'0.05 pi-/p'),(0.1,'0.1 pi-/p'),(0.3,'0.3 pi-/p')]:
        if ylab=='0.1 pi-/p':
            print('     %-24s %.3g protons/s  x %-12s = %.3g pi-/s' % (lab,Np,ylab,Np*y))
print()
print('  THE REQUIREMENT')
for P,lab in [(1e3,'1 kW'),(1e6,'1 MW'),(1e9,'1 GW')]:
    R=P/(300*Q)
    print('     %-6s fusion at N=300 needs %.3g mu/s' % (lab,R))
print()
print('  SO WHERE IS THE 1e5?')
print('     E_mu = 5 GeV means: 1 MW of beam -> %.3g mu/s' % (1e6/(5e9*eV)))
print('     which is exactly the 1 MW fusion requirement (1.2e15 /s).')
print('     the papers table is SELF-CONSISTENT: 1 MW beam -> 1 MW fusion, Q ~ 1.')
print()
print('     the 1e10 /s at facilities is a DIFFERENT quantity:')
print('        it is muons DELIVERED TO A BEAMLINE, not muons produced.')
print('        implied cost per delivered muon at 1.4 MW / 1e10 /s:')
print('        %.3g J = %.0f GeV per muon  -- %.0fx worse than the 5 GeV figure.'
      % (1.4e6/1e10, 1.4e6/1e10/eV/1e9, (1.4e6/1e10/eV/1e9)/5))
print()
print('  WHY BEAMLINES THROW AWAY 175x')
LOSS=[('production target thickness','only a few % of protons interact usefully'),
      ('capture solid angle','pions emitted into 4pi; horn/solenoid captures a fraction'),
      ('momentum bite','beamlines select dp/p ~ few %, discarding the rest of the spectrum'),
      ('emittance selection','precision experiments need small phase space; muCF does not'),
      ('decay acceptance','only pions decaying inside the channel with the right kinematics'),
      ('stopping fraction','surface muons are chosen for shallow stopping, not for count')]
for a,b in LOSS: print('     %-28s %s' % (a,b))
print()
print('  WHAT muCF NEEDS THAT A PHYSICS BEAMLINE DOES NOT')
print('     %-26s %-22s %s' % ('quantity','physics beamline','muCF reactor'))
ROWS=[('momentum spread','dp/p ~ 1-3%','anything that stops in the fuel'),
      ('emittance','small, for tracking','irrelevant'),
      ('polarisation','often required','helps sticking, not required'),
      ('beam spot','mm, defined','the whole fuel volume'),
      ('pulse structure','defined','continuous preferred'),
      ('backgrounds','minimised','irrelevant - the target is the detector')]
for r in ROWS: print('     %-26s %-22s %s' % r)
print()
print('  THE FLUX GAP, RESTATED')
print('     it is NOT: not enough beam power. 1 MW exists.')
print('     it is NOT: not enough pion production. ~1e15/s at 1 MW.')
print('     it IS   : no machine collects and stops a large fraction of what is produced,')
print('               because no machine has ever been built to want that.')
print()
print('     the 175x between 5 GeV/muon (design accounting) and 875 GeV/muon (delivered)')
print('     is the collection chain, and it is the SAME six stages as the energy gap.')
print('     -> the two gaps are one chain read at two thresholds, as suspected,')
print('        and the operative number is neither 1.28x nor 1e5 but ~175x.')