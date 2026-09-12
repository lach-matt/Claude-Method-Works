% Localised NEC: does the corrected (frame) NEC depend on the shift at all?
% Reports the minimum over the SHELL INTERIOR only (10 < r < 20 m), away from
% the grid-boundary truncation error that dominates the global minimum.
spaceScale = 2; vlist = [0 0.02 0.03 0.04 0.06 0.10 0.15 0.20];
NANG = 60;
R1 = 10; Rbuff = 0; R2 = 20; cartoonThickness = 5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, cartoonThickness]);
m = R2/(2*G)*c^2*(1/3); sigma = 0; smoothFactor = 4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(cartoonThickness+1)/2, (2*(R2+10)*spaceScale+1)/2, ...
               (2*(R2+10)*spaceScale+1)/2, (cartoonThickness+1)/2].*gridScaling;
Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, ...
                                  sigma, smoothFactor, 1.0, 1, gridScaling);
base_gtx = Met.tensor{1,2};
nvec = generateUniformField("nulllike", NANG, 1, 0);

% radius map on the z-midplane slice
N = gridSize(2); ctr = (N+1)/2;
[X,Y] = ndgrid((1:N)-ctr, (1:N)-ctr);
Rm = sqrt(X.^2 + Y.^2)/spaceScale;
inshell = (Rm > 10.5) & (Rm < 19.5);
printf('shell-interior cells: %d   (dx = %.2f m, %d dirs)\n\n', sum(inshell(:)), 1/spaceScale, NANG);
printf('  %-7s %14s %14s %14s %12s\n','vWarp','FRAME_shell','SHIP_shell','T0x_max','r@min');
for v = vlist
  Met.tensor{1,2} = base_gtx*v;  Met.tensor{2,1} = Met.tensor{1,2};
  Tc = getEnergyTensor(Met, 0);
  Tu = doFrameTransfer(Met, Tc, "Eulerian", 0);
  Tf = Tu.tensor;
  t0x = max(abs(reshape(squeeze(Tf{1,2}(1,:,:,3)),[],1)));
  for i = 2:4, Tf{1,i} = -Tf{1,i}; Tf{i,1} = -Tf{i,1}; end
  best = Inf*ones(N,N);
  for ii = 1:NANG
    acc = zeros(N,N);
    for mu = 1:4
      for nu = 1:4
        acc = acc + squeeze(Tf{mu,nu}(1,:,:,3))*nvec(mu,ii)*nvec(nu,ii);
      end
    end
    best = min(best, acc);
  end
  bs = best; bs(~inshell) = Inf;
  [mv, idx] = min(bs(:));
  ship = getEnergyConditions(Tc, Met, "Null", NANG, 1, 0, 0);
  sh = squeeze(ship(1,:,:,3)); sh(~inshell) = Inf; msh = min(sh(:));
  printf('  %-7.3f %14.5e %14.5e %14.4e %12.2f\n', v, mv, msh, t0x, Rm(idx));
  fflush(stdout);
end
