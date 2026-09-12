% Measure the NEC ceiling as a function of horizon fill fraction.
% fill = r_s/R1 = 2Gm/(c^2 R1).  With R2 = 2 R1 and Warp Factory's own
% parameterisation m = R2 c^2/(2G) * factor, we have r_s = R2*factor = R1*fill,
% so factor = fill/2.
spaceScale = str2double(getenv('WF_SCALE'));
fills      = str2num(getenv('WF_FILLS'));
vlist      = str2num(getenv('WF_VLIST'));

R1 = 10; Rbuff = 0; R2 = 20; cartoonThickness = 5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, cartoonThickness]);
sigma = 0; smoothFactor = 4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(cartoonThickness+1)/2, (2*(R2+10)*spaceScale+1)/2, ...
               (2*(R2+10)*spaceScale+1)/2, (cartoonThickness+1)/2].*gridScaling;

printf('FILL SWEEP  scale %g  dx %.3f m  grid %dx%dx%d\n\n', ...
       spaceScale, 1/spaceScale, gridSize(2), gridSize(3), gridSize(4));
printf('  %-7s %11s %11s %9s %9s %11s\n', ...
       'fill','m [kg]','rho_max','floor/rho','k=f/rho/v','v_crit');
fflush(stdout);

for fl = fills
  factor = fl/2;
  m = R2/(2*G)*c^2*factor;
  Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, ...
                                    sigma, smoothFactor, 1.0, 1, gridScaling);
  base = Met.tensor{1,2};
  vs = []; mins = []; rmax = 0; floorv = 0; kk = [];
  for v = vlist
    Met.tensor{1,2} = base * v; Met.tensor{2,1} = Met.tensor{1,2};
    Ev = evalMetric(Met, 0, 1);
    T = Ev.energyTensorEulerian.tensor;
    sl = @(A) A(1, 4:end-3, 4:end-3, 3);
    rho = sl(T{1,1}); rm = max(rho(:));
    f = max(abs([reshape(sl(T{1,2}),[],1); reshape(sl(T{1,3}),[],1); reshape(sl(T{1,4}),[],1)]));
    A = Ev.null(1, 4:end-3, 4:end-3, 3); mn = min(A(:));
    if v == 0, floorv = mn; rmax = rm; else kk(end+1) = (f/rm)/v; end
    vs(end+1) = v; mins(end+1) = mn;
  end
  % least-squares zero over points clearly above the floor
  sel = abs(mins) > 10*abs(floorv);
  vc = NaN;
  if sum(sel) >= 2
    x = vs(sel); y = mins(sel); n = numel(x);
    b = (n*sum(x.*y) - sum(x)*sum(y)) / (n*sum(x.^2) - sum(x)^2);
    a = (sum(y) - b*sum(x))/n;
    vc = -a/b;
  end
  printf('  %-7.3f %11.4e %11.4e %9.2e %9.3f %11.5f\n', ...
         fl, m, rmax, abs(floorv)/rmax, mean(kk), vc);
  fflush(stdout);
end
