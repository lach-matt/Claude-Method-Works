% TARGET 1, done properly.  Three regions, kept apart:
%   SHELL  10.5 < r < 19.5   matter
%   VAC    20.5 < r < 26.0   vacuum exterior, away from BOTH boundaries
%   EDGE   outermost 4 cells  one-sided stencils; expected garbage, not physics
% In VAC the exact solution is Schwarzschild, so T = 0 identically and any
% nonzero value MUST converge away.  That is the test.
% Also measures the lapse and shift: transport, or no transport.
spaceScale = str2double(getenv('WF_SCALE'));
NANG = 40;
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
Met = metricGet_WarpShellComoving(gridSize, wc, m, R1, R2, Rbuff, sigma, smoothFactor, 1.0, 1, gs);
base = Met.tensor{1,2};
N = gridSize(2); ctr=(N+1)/2;
[X,Y] = ndgrid((1:N)-ctr,(1:N)-ctr); Rm = sqrt(X.^2+Y.^2)/spaceScale;
interior = false(N,N); interior(5:end-4,5:end-4) = true;    % drop 4 cells each side
shell = (Rm>10.5)&(Rm<19.5)&interior;
vac   = (Rm>20.5)&(Rm<26.0)&interior;
edge  = ~interior;
nullv = generateUniformField("nulllike", NANG, 1, 0);
printf('SCALE %g  dx=%.4f  cells: shell %d, vac %d, edge %d\n', ...
       spaceScale, 1/spaceScale, sum(shell(:)), sum(vac(:)), sum(edge(:)));
printf('  %-7s %-6s %14s %14s\n','vWarp','region','NULL','rho_min');
for v = [0 0.02 0.04]
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Tcoord = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tcoord, "Eulerian", 0);
  Tc = Tu.tensor; for i=2:4, Tc{1,i}=-Tc{1,i}; Tc{i,1}=-Tc{i,1}; end
  rho = squeeze(Tu.tensor{1,1}(1,:,:,3));
  best = Inf*ones(N,N);
  for ii=1:NANG
    acc = zeros(N,N);
    for mu=1:4, for nu=1:4
      acc = acc + squeeze(Tc{mu,nu}(1,:,:,3))*nullv(mu,ii)*nullv(nu,ii);
    end, end
    best = min(best,acc);
  end
  for rg = {'shell','vac','edge'}
    msk = shell; if strcmp(rg{1},'vac'), msk=vac; elseif strcmp(rg{1},'edge'), msk=edge; end
    printf('  %-7.4f %-6s %14.5e %14.5e\n', v, rg{1}, min(best(msk)), min(rho(msk)));
  end
  fflush(stdout);
end
% ---- transport ----
printf('\nTRANSPORT: lapse and shift on the +x axis (vWarp = 0.04)\n');
Met.tensor{1,2}=base*0.04; Met.tensor{2,1}=Met.tensor{1,2};
ginv = c4Inv(Met.tensor);
printf('  %8s %12s %12s %14s\n','r (m)','g_tx','alpha','-beta^x (c)');
for rr = [0 4 8 10 14 18 20 24 28]
  i = round(ctr + rr*spaceScale); j = round(ctr);
  if i > N, continue; end
  Gtt = ginv{1,1}(1,i,j,3); Gtx = ginv{1,2}(1,i,j,3);
  printf('  %8.1f %12.6f %14.6f %14.6f\n', rr, Met.tensor{1,2}(1,i,j,3), ...
         sqrt(-1/Gtt), Gtx/Gtt);
end
