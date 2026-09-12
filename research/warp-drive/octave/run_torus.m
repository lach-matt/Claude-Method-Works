% THE OPEN GATE, certified.  Source-first toroidal slice from tsolve.py:
%   gamma_ij = psi^4 delta_ij   (exact solution of the Hamiltonian constraint)
%   alpha    = (2-psi)/psi      (Brill-Lindquist lapse; exact for Schwarzschild)
%   beta^x   = -v S(x,s)        boosted cylinder inside the bore
% ADM assembly:  g_tt = -alpha^2 + psi^4 (beta^x)^2 ,  g_tx = psi^4 beta^x
% Then Warp Factory computes T, and the EXACT Hawking-Ellis certifier from
% TARGET-1 grades it.  vWarp = 0 is the CONTROL: if the bare torus violates,
% the construction is invalid and nothing downstream counts.
psi2 = load('psi.dat'); gg = load('grid.dat');
xlo=gg(1); xhi=gg(2); slo=gg(3); shi=gg(4); Np=gg(5);
xs = linspace(xlo,xhi,Np); ss = linspace(slo,shi,Np);
R0=15; A=5; RB=R0-A;             % major, minor, bore radius
LX=8; WT=1.5;                    % axial half-length and taper width of the boost
sc=1; half=30;
Nx=2*half*sc+1; ct=5;
gridSize=[1,Nx,Nx,ct];
gs=[1/(1000*c), 1/sc, 1/sc, 1/sc];
ctr=(Nx+1)/2; ctz=(ct+1)/2;
eta=diag([-1 1 1 1]);
printf('open-gate certification: R0=%g a=%g bore=%g, boost cylinder r<%g |x|<%g\n',R0,A,RB,RB,LX);

for v = [0 0.02 0.04]
  Met.type="metric"; Met.index="covariant"; Met.coords="cartesian"; Met.name="OpenGate"; Met.scaling=gs; Met.date=date;
  for a=1:4, for b=1:4, Met.tensor{a,b}=zeros(gridSize); end, end
  for i=1:Nx
    for j=1:Nx
      for k=1:ct
        X=(i-ctr)/sc; Y=(j-ctr)/sc; Z=(k-ctz)/sc;
        Sr=sqrt(Y^2+Z^2);
        p = interp2(ss, xs, psi2, min(max(Sr,slo),shi), min(max(X,xlo),xhi), 'linear');
        if isnan(p), p=1.0; end
        al=(2-p)/p; p4=p^4;
        Sx = 0.5*(1-tanh((Sr-RB)/WT)) * 0.5*(1-tanh((abs(X)-LX)/WT));
        bx = -v*Sx;
        Met.tensor{1,1}(1,i,j,k) = -al^2 + p4*bx^2;
        Met.tensor{1,2}(1,i,j,k) = p4*bx;   Met.tensor{2,1}(1,i,j,k)=p4*bx;
        Met.tensor{2,2}(1,i,j,k) = p4;
        Met.tensor{3,3}(1,i,j,k) = p4;
        Met.tensor{4,4}(1,i,j,k) = p4;
      end
    end
  end
  Tc = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tc, "Eulerian", 0);
  Tf = Tu.tensor; for i=2:4, Tf{1,i}=-Tf{1,i}; Tf{i,1}=-Tf{i,1}; end

  [XX,YY]=ndgrid(((1:Nx)-ctr)/sc,((1:Nx)-ctr)/sc);
  RR=abs(YY); DR=sqrt((RR-R0).^2+XX.^2);
  inner=false(Nx,Nx); inner(5:end-4,5:end-4)=true;
  regRING  = (DR<A+1) & inner;
  regBORE  = (RR<RB-1) & (abs(XX)<LX-2) & inner;
  regMOUTH = (RR<RB-1) & (abs(XX)>=LX-2) & (abs(XX)<=LX+4) & inner;
  regFAR   = ~(regRING|regBORE|regMOUTH) & inner;

  NEC=inf(Nx,Nx); DEC=inf(Nx,Nx); WEC=inf(Nx,Nx); T4=false(Nx,Nx); LIVE=false(Nx,Nx);
  sc0=0; for i=1:Nx, for j=1:Nx, sc0=max(sc0,abs(Tf{1,1}(1,i,j,ctz))); end, end
  th=1e-10*sc0;
  for i=1:Nx
    for j=1:Nx
      Tab=zeros(4,4);
      for a=1:4, for b=1:4, Tab(a,b)=Tf{a,b}(1,i,j,ctz); end, end
      if max(abs(Tab(:)))<th, continue; end
      LIVE(i,j)=true;
      Tm=Tab; Tm(1,:)=-Tm(1,:);
      [V,D]=eig(Tm); lam=diag(D);
      if max(abs(imag(lam)))>1e-8*max(abs(real(lam))), T4(i,j)=true; continue; end
      lam=real(lam); V=real(V);
      nn=zeros(4,1); for q=1:4, nn(q)=V(:,q)'*eta*V(:,q); end
      [~,kt]=min(nn);
      if nn(kt)>=0, T4(i,j)=true; continue; end
      rho=-lam(kt); pp=lam([1:kt-1 kt+1:4]);
      NEC(i,j)=min(rho+pp); WEC(i,j)=min(rho,min(rho+pp)); DEC(i,j)=min(rho-abs(pp));
    end
  end
  printf('\n  vWarp = %.3f%s\n', v, merge(v==0,'   <-- CONTROL',''));
  printf('  %-8s %13s %13s %13s %7s %7s\n','region','NEC','WEC','DEC','TypeIV','cells');
  for rg={'RING','BORE','MOUTH','FAR'}
    switch rg{1}
      case 'RING', m=regRING; case 'BORE', m=regBORE;
      case 'MOUTH', m=regMOUTH; otherwise, m=regFAR;
    end
    m=m&LIVE; n4=sum(sum(T4&m)); m1=m&~T4;
    if sum(m1(:))==0
      printf('  %-8s %13s %13s %13s %7d %7d\n', rg{1},'(vacuum)','-','-',n4,sum(m(:)));
    else
      printf('  %-8s %13.4e %13.4e %13.4e %7d %7d\n', rg{1}, ...
             min(NEC(m1)), min(WEC(m1)), min(DEC(m1)), n4, sum(m(:)));
    end
  end
  fflush(stdout);
end
