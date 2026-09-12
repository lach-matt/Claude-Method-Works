% Attribution: where did the published 0.0218 c ceiling come from?
% Same shipped NEC, three slices:
%   PUB   = 1,4:end-3,4:end-3,3    -- the slice run_sweep.m used (published)
%   SHELL = 10.5 < r < 19.5        -- shell interior only
%   BOX   = PUB minus the shell    -- everything else in that slice
spaceScale = 2; vlist = [0 0.015 0.020 0.0218 0.025 0.030 0.035 0.040 0.045];
NANG = 60;
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gridScaling;
Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, sigma, smoothFactor, 1.0, 1, gridScaling);
base = Met.tensor{1,2};
N = gridSize(2); ctr=(N+1)/2;
[X,Y] = ndgrid((1:N)-ctr,(1:N)-ctr); Rm = sqrt(X.^2+Y.^2)/spaceScale;
pub = false(N,N); pub(4:end-3,4:end-3) = true;
shell = (Rm>10.5)&(Rm<19.5);
printf('  %-7s %14s %14s %14s %10s\n','vWarp','PUB','SHELL','PUB\\SHELL','r@PUBmin');
for v = vlist
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Tc = getEnergyTensor(Met,0);
  A = squeeze(getEnergyConditions(Tc,Met,"Null",NANG,1,0,0)(1,:,:,3));
  p=A; p(~pub)=Inf; [mp,ip]=min(p(:));
  s=A; s(~shell)=Inf; ms=min(s(:));
  o=A; o(~(pub&~shell))=Inf; mo=min(o(:));
  printf('  %-7.4f %14.5e %14.5e %14.5e %10.2f\n', v, mp, ms, mo, Rm(ip));
  fflush(stdout);
end
