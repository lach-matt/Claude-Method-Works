% ISOLATION TEST: can a bounded boosted region terminate in VACUUM?
% Strip everything else away.  Flat spatial slices, unit lapse, and a single
% compactly-supported shift bump -- no matter anywhere:
%     g_ij = delta_ij ,  alpha = 1 ,  beta^x = -v S(x,s)
% This is the axial-termination question with the torus removed.  If T here
% violates the energy conditions, then the taper CANNOT be supported by vacuum,
% and an open bore cannot carry a shift however the ring around it is built.
% The control is v = 0, which must give exactly Minkowski and exactly zero T.
RB=10; LX=8; WT=1.5; sc=1; half=30;
Nx=2*half*sc+1; ct=5; ctr=(Nx+1)/2; ctz=(ct+1)/2;
gridSize=[1,Nx,Nx,ct]; gs=[1/(1000*c),1/sc,1/sc,1/sc];
eta=diag([-1 1 1 1]);
printf('axial-termination isolation: vacuum, alpha=1, flat slices, shift bump only\n');
printf('boost cylinder r < %g, |x| < %g, taper width %g\n', RB, LX, WT);
for v = [0 0.02 0.04 0.10]
  Met.type="metric"; Met.index="covariant"; Met.coords="cartesian";
  Met.name="AxialTaper"; Met.scaling=gs; Met.date=date;
  for a=1:4, for b=1:4, Met.tensor{a,b}=zeros(gridSize); end, end
  for i=1:Nx, for j=1:Nx, for k=1:ct
    X=(i-ctr)/sc; Y=(j-ctr)/sc; Z=(k-ctz)/sc; Sr=sqrt(Y^2+Z^2);
    Sx = 0.5*(1-tanh((Sr-RB)/WT)) * 0.5*(1-tanh((abs(X)-LX)/WT));
    bx = -v*Sx;
    Met.tensor{1,1}(1,i,j,k) = -1 + bx^2;
    Met.tensor{1,2}(1,i,j,k) = bx;  Met.tensor{2,1}(1,i,j,k)=bx;
    Met.tensor{2,2}(1,i,j,k) = 1; Met.tensor{3,3}(1,i,j,k)=1; Met.tensor{4,4}(1,i,j,k)=1;
  end, end, end
  Tc = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tc, "Eulerian", 0);
  Tf = Tu.tensor; for i=2:4, Tf{1,i}=-Tf{1,i}; Tf{i,1}=-Tf{i,1}; end
  [XX,YY]=ndgrid(((1:Nx)-ctr)/sc,((1:Nx)-ctr)/sc); RR=abs(YY);
  inner=false(Nx,Nx); inner(5:end-4,5:end-4)=true;
  regBORE =(RR<RB-2)&(abs(XX)<LX-2)&inner;
  regMOUTH=(RR<RB-2)&(abs(XX)>=LX-2)&(abs(XX)<=LX+4)&inner;
  regWALL =(RR>=RB-2)&(RR<=RB+4)&(abs(XX)<LX-2)&inner;
  NEC=inf(Nx,Nx);DEC=inf(Nx,Nx);T4=false(Nx,Nx);LIVE=false(Nx,Nx);RHO=zeros(Nx,Nx);
  s0=0; for i=1:Nx, for j=1:Nx, s0=max(s0,abs(Tf{1,1}(1,i,j,ctz))); end, end
  th=max(1e-10*s0,1e-30);
  for i=1:Nx, for j=1:Nx
    Tab=zeros(4,4); for a=1:4, for b=1:4, Tab(a,b)=Tf{a,b}(1,i,j,ctz); end, end
    if max(abs(Tab(:)))<th, continue; end
    LIVE(i,j)=true; Tm=Tab; Tm(1,:)=-Tm(1,:);
    [V,D]=eig(Tm); lam=diag(D);
    if max(abs(imag(lam)))>1e-8*max(abs(real(lam))), T4(i,j)=true; continue; end
    lam=real(lam); V=real(V); nn=zeros(4,1);
    for q=1:4, nn(q)=V(:,q)'*eta*V(:,q); end
    [~,kt]=min(nn); if nn(kt)>=0, T4(i,j)=true; continue; end
    rho=-lam(kt); pp=lam([1:kt-1 kt+1:4]);
    RHO(i,j)=rho; NEC(i,j)=min(rho+pp); DEC(i,j)=min(rho-abs(pp));
  end, end
  printf('\n  v = %.3f%s   live cells %d, max|T00| %.3e\n', v, ...
         merge(v==0,'  <-- CONTROL: must be exactly vacuum',''), sum(LIVE(:)), s0);
  printf('  %-8s %13s %13s %13s %7s %6s\n','region','NEC','DEC','rho_min','TypeIV','cells');
  for rg={'BORE','MOUTH','WALL'}
    switch rg{1}
      case 'BORE', m=regBORE; case 'MOUTH', m=regMOUTH; otherwise, m=regWALL;
    end
    m=m&LIVE; n4=sum(sum(T4&m)); m1=m&~T4;
    if sum(m1(:))==0
      printf('  %-8s %13s %13s %13s %7d %6d\n', rg{1},'(vacuum)','-','-',n4,sum(m(:)));
    else
      printf('  %-8s %13.4e %13.4e %13.4e %7d %6d\n', rg{1}, ...
             min(NEC(m1)), min(DEC(m1)), min(RHO(m1)), n4, sum(m(:)));
    end
  end
  fflush(stdout);
end
