% Build the published Warp Shell metric once, then evaluate at several shift
% values.  Exact, because metricGet_WarpShellComoving sets g_tx = -S_warp(r)*vWarp
% on a metric that is otherwise diagonal: the shift enters linearly and nothing
% else in the build depends on it.
spaceScale = str2double(getenv('WF_SCALE'));
vlist      = str2num(getenv('WF_VLIST'));

R1 = 10; Rbuff = 0; R2 = 20; cartoonThickness = 5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, cartoonThickness]);
m = R2/(2*G)*c^2*(1/3);
sigma = 0; smoothFactor = 4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(cartoonThickness+1)/2, (2*(R2+10)*spaceScale+1)/2, ...
               (2*(R2+10)*spaceScale+1)/2, (cartoonThickness+1)/2].*gridScaling;

printf('SCALE %g   grid %dx%dx%d   dx = %.3f m   m = %.4e kg\n', ...
       spaceScale, gridSize(2), gridSize(3), gridSize(4), 1/spaceScale, m);
t0 = time();
Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, ...
                                  sigma, smoothFactor, 1.0, 1, gridScaling);
base_gtx = Met.tensor{1,2};
printf('  metric built  %.1f s\n\n', time()-t0);

printf('  %-8s %12s %10s %10s %12s %12s %12s %12s\n', ...
       'vWarp','rho_max','|f|/rho','|p|/rho','null','weak','strong','dominant');
for v = vlist
  Met.tensor{1,2} = base_gtx * v;
  Met.tensor{2,1} = Met.tensor{1,2};
  Ev = evalMetric(Met, 0, 1);
  T = Ev.energyTensorEulerian.tensor;
  sl = @(A) A(1, 4:end-3, 4:end-3, 3);
  rho = sl(T{1,1}); rmax = max(rho(:));
  f = max(abs([reshape(sl(T{1,2}),[],1); reshape(sl(T{1,3}),[],1); reshape(sl(T{1,4}),[],1)]));
  pk = max(abs([reshape(sl(T{2,2}),[],1); reshape(sl(T{3,3}),[],1); reshape(sl(T{4,4}),[],1)]));
  mn = zeros(1,4); k = 0;
  for nm = {'null','weak','strong','dominant'}
    k++; A = Ev.(nm{1})(1, 4:end-3, 4:end-3, 3); mn(k) = min(A(:));
  end
  printf('  %-8.4f %12.4e %10.4f %10.4f %12.3e %12.3e %12.3e %12.3e\n', ...
         v, rmax, f/rmax, pk/rmax, mn(1), mn(2), mn(3), mn(4));
  fflush(stdout);
end
printf('\n  (minima in J/m^3; compare against rho_max -- a fixed RATIO under grid\n');
printf('   refinement means physical, a falling one means truncation error)\n');
