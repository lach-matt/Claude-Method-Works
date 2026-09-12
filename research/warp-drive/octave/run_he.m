% TARGET 1, CLOSED PROPERLY: frame-independent Hawking-Ellis certification.
%
% Le (2602.18023) is right that a single-frame Eulerian contraction is not the
% test.  The correct one needs no observer scan at all:
%
%   1. T_ab in the orthonormal frame (doFrameTransfer, then lower with eta).
%   2. Raise one index with eta:  T^a_b = eta^ac T_cb  =  negate row 0.
%   3. Eigenvalues of that 4x4.  Complex pair  => HAWKING-ELLIS TYPE IV:
%      the stress-energy admits NO rest frame, and WEC/DEC fail automatically.
%      All real with one timelike eigenvector => TYPE I, diag(-rho,p1,p2,p3).
%   4. For Type I the conditions are EXACT ALGEBRA on the eigenvalues:
%         NEC  rho + p_i >= 0
%         WEC  rho >= 0  and NEC
%         DEC  rho - |p_i| >= 0
%         SEC  rho + sum p_i >= 0  and NEC
%      These hold for EVERY observer.  No sampling, no 40 directions.
%
% Reports the minimum SLACK of each condition per region, which is Le's own
% figure of merit, plus the Type-IV census.
spaceScale = str2double(getenv('WF_SCALE'));
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
Met = metricGet_WarpShellComoving(gridSize, wc, m, R1, R2, Rbuff, sigma, smoothFactor, 1.0, 1, gs);
base = Met.tensor{1,2};
N = gridSize(2); ctr=(N+1)/2;
[X,Y] = ndgrid((1:N)-ctr,(1:N)-ctr); Rm = sqrt(X.^2+Y.^2)/spaceScale;
inner = false(N,N); inner(5:end-4,5:end-4)=true;
eta = diag([-1 1 1 1]);

printf('SCALE %g   dx = %.3f m   (exact Hawking-Ellis, no observer sampling)\n', ...
       spaceScale, 1/spaceScale);
for v = [0 0.02 0.04]
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Tc = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tc, "Eulerian", 0);
  Tf = Tu.tensor; for i=2:4, Tf{1,i}=-Tf{1,i}; Tf{i,1}=-Tf{i,1}; end  % -> T_ab frame

  RHO = zeros(N,N); NEC = inf(N,N); WEC = inf(N,N); DEC = inf(N,N); SEC = inf(N,N);
  TYPE4 = false(N,N); LIVE = false(N,N);
  scale = 0;
  for i=1:N, for j=1:N
    scale = max(scale, abs(Tf{1,1}(1,i,j,3)));
  end, end
  thresh = 1e-8*scale;

  for i=1:N
    for j=1:N
      Tab = zeros(4,4);
      for a=1:4, for b=1:4, Tab(a,b) = Tf{a,b}(1,i,j,3); end, end
      if max(abs(Tab(:))) < thresh, continue; end       % vacuum: nothing to classify
      LIVE(i,j) = true;
      Tmix = Tab; Tmix(1,:) = -Tmix(1,:);               % T^a_b = eta^ac T_cb
      [V,D] = eig(Tmix);
      lam = diag(D);
      if max(abs(imag(lam))) > 1e-8*max(abs(real(lam)))
        TYPE4(i,j) = true; continue;                    % no rest frame exists
      end
      lam = real(lam); V = real(V);
      % the timelike eigenvector is the one with negative eta-norm
      nrm = zeros(4,1);
      for k=1:4, nrm(k) = V(:,k)'*eta*V(:,k); end
      [~, kt] = min(nrm);
      if nrm(kt) >= 0, TYPE4(i,j) = true; continue; end % no timelike eigenvector
      rho = -lam(kt);
      p = lam([1:kt-1 kt+1:4]);
      RHO(i,j) = rho;
      NEC(i,j) = min(rho + p);
      WEC(i,j) = min(rho, min(rho + p));
      DEC(i,j) = min(rho - abs(p));
      SEC(i,j) = min(rho + sum(p), min(rho + p));
    end
  end

  printf('\n  vWarp = %.3f\n', v);
  printf('  %-14s %11s %11s %11s %11s %7s %7s\n', ...
         'region','NEC slack','WEC slack','DEC slack','SEC slack','TypeIV','cells');
  for rg = {'bulk','transition','vacuum'}
    switch rg{1}
      case 'bulk',       msk = (Rm>10.5)&(Rm<19.5)&inner&LIVE;
      case 'transition', msk = (Rm>=19.5)&(Rm<=21.0)&inner&LIVE;
      case 'vacuum',     msk = (Rm>21.0)&inner&LIVE;
    end
    n4 = sum(sum(TYPE4 & msk)); nn = sum(msk(:));
    m1 = msk & ~TYPE4;
    if sum(m1(:))==0
      printf('  %-14s %11s %11s %11s %11s %7d %7d\n', rg{1},'-','-','-','-',n4,nn);
    else
      printf('  %-14s %11.3e %11.3e %11.3e %11.3e %7d %7d\n', rg{1}, ...
             min(NEC(m1)), min(WEC(m1)), min(DEC(m1)), min(SEC(m1)), n4, nn);
    end
  end
  fflush(stdout);
end
