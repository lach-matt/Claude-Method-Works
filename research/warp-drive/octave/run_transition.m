% Did TARGET-1 mask out the region where the failure actually lives?
% Le (arXiv:2605.25417) finds the EC failure localized at the smooth
% source-vacuum transition, not in the bulk.  TARGET-1 sampled
% shell 10.5-19.5 and vac 20.5-26.0 -- and EXCLUDED 19.5-20.5.
% Here the transition is resolved in fine radial bins, at two resolutions.
% A physical failure converges to a finite negative value; a stencil
% artefact converges to zero.  That is the discriminator.
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
inner = false(N,N); inner(5:end-4,5:end-4) = true;   % drop the true grid edge
nullv = generateUniformField("nulllike", NANG, 1, 0);

printf('SCALE %g   dx = %.3f m\n', spaceScale, 1/spaceScale);
for v = [0 0.04]
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Tc = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tc, "Eulerian", 0);
  Tf = Tu.tensor; for i=2:4, Tf{1,i}=-Tf{1,i}; Tf{i,1}=-Tf{i,1}; end
  rho = squeeze(Tu.tensor{1,1}(1,:,:,3));
  best = Inf*ones(N,N);
  for ii=1:NANG
    acc = zeros(N,N);
    for mu=1:4, for nu=1:4
      acc = acc + squeeze(Tf{mu,nu}(1,:,:,3))*nullv(mu,ii)*nullv(nu,ii);
    end, end
    best = min(best,acc);
  end
  printf('\n  vWarp = %.3f   radial bins across the transition\n', v);
  printf('  %-14s %14s %14s %8s\n','band (m)','NULL min','rho min','cells');
  edges = [16 18 19 19.5 20 20.5 21 22 24 27];
  for k = 1:numel(edges)-1
    msk = (Rm>=edges(k)) & (Rm<edges(k+1)) & inner;
    if sum(msk(:)) == 0, continue; end
    printf('  %5.1f - %-6.1f %14.5e %14.5e %8d\n', edges(k), edges(k+1), ...
           min(best(msk)), min(rho(msk)), sum(msk(:)));
  end
  fflush(stdout);
end
