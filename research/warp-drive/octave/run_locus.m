% Where does the NEC actually fail, and which component drives it?
% MEASURED.md finds the ceiling binds at |f|/rho = 0.327 while the (t,x) closed
% form allows 0.525.  This locates the failing point and prints the full Eulerian
% stress-energy there, so the discrepancy has a named cause instead of a guess.
spaceScale = str2double(getenv('WF_SCALE'));
vlist      = str2num(getenv('WF_VLIST'));

R1 = 10; Rbuff = 0; R2 = 20; cartoonThickness = 5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, cartoonThickness]);
m = R2/(2*G)*c^2*(1/3); sigma = 0; smoothFactor = 4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(cartoonThickness+1)/2, (2*(R2+10)*spaceScale+1)/2, ...
               (2*(R2+10)*spaceScale+1)/2, (cartoonThickness+1)/2].*gridScaling;
Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, ...
                                  sigma, smoothFactor, 1.0, 1, gridScaling);
base = Met.tensor{1,2};
cx = worldCenter(2)*spaceScale; cy = worldCenter(3)*spaceScale;

for v = vlist
  Met.tensor{1,2} = base*v; Met.tensor{2,1} = Met.tensor{1,2};
  Ev = evalMetric(Met, 0, 1);
  T = Ev.energyTensorEulerian.tensor;
  N = squeeze(Ev.null(1, 4:end-3, 4:end-3, 3));
  [mn, idx] = min(N(:));
  [ii, jj] = ind2sub(size(N), idx);
  I = ii + 3; J = jj + 3;                      % back to full-grid indices
  gv = @(a,b) T{a,b}(1, I, J, 3);
  rho = gv(1,1);
  x = (I - cx)/spaceScale; y = (J - cy)/spaceScale;
  r = sqrt(x^2 + y^2);
  printf('\n  vWarp = %.3f    null min = %+.4e  (%.4f rho)\n', v, mn, mn/rho);
  printf('    locus            x = %+7.2f  y = %+7.2f   r = %6.2f m\n', x, y, r);
  printf('    (shell spans r = %g..%g m; flux peaks near mid-shell r = %g)\n', R1, R2, (R1+R2)/2);
  printf('    energy density   rho     %+12.4e\n', rho);
  printf('    momentum         f_x     %+12.4e   %+8.4f rho\n', gv(1,2), gv(1,2)/rho);
  printf('                     f_y     %+12.4e   %+8.4f rho\n', gv(1,3), gv(1,3)/rho);
  printf('    pressures        p_x     %+12.4e   %+8.4f rho\n', gv(2,2), gv(2,2)/rho);
  printf('                     p_y     %+12.4e   %+8.4f rho\n', gv(3,3), gv(3,3)/rho);
  printf('                     p_z     %+12.4e   %+8.4f rho\n', gv(4,4), gv(4,4)/rho);
  printf('    shears           s_xy    %+12.4e   %+8.4f rho\n', gv(2,3), gv(2,3)/rho);
  printf('                     s_xz    %+12.4e   %+8.4f rho\n', gv(2,4), gv(2,4)/rho);
  printf('                     s_yz    %+12.4e   %+8.4f rho\n', gv(3,4), gv(3,4)/rho);
  % the (t,x) closed form of SHIFT-CEILING, evaluated AT THIS POINT
  printf('    closed form (t,x):  rho + p_x - 2|f_x| = %+.4e   -> %s\n', ...
         rho + gv(2,2) - 2*abs(gv(1,2)), ...
         merge(rho + gv(2,2) - 2*abs(gv(1,2)) < 0, 'predicts failure', 'predicts SAFE'));
  fflush(stdout);
end

% --- how null are the sampled vectors, in the actual metric? ---
printf('\n  METRIC AT THE LOCUS, and the nullity of the sampled vectors\n');
g = @(a,b) Met.tensor{a,b}(1, I, J, 3);
printf('    g_tt %+ .6f   g_tx %+ .6f   g_xx %+ .6f   g_yy %+ .6f\n', ...
       g(1,1), g(1,2), g(2,2), g(3,3));
worst = 0;
for th = linspace(0, 2*pi, 73)
  n = [cos(th), sin(th), 0];
  k = [1, n];
  s = 0;
  for a = 1:4
    for b = 1:4
      s = s + g(a,b)*k(a)*k(b);
    end
  end
  worst = max(worst, abs(s));
end
printf('    max |g_uv k^u k^v| over the sampled directions:  %.4f\n', worst);
printf('    (zero would mean the vectors are genuinely null in this metric)\n');
