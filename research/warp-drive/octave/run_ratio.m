% Radial profiles of rho, |f| and the binding ratio |f|/rho along the transverse
% axis, for a given density shape.  This says where the constraint actually bites
% and therefore what shape rho should take -- instead of assuming it tracks |S''|.
spaceScale = str2double(getenv('WF_SCALE'));
delta      = str2double(getenv('WF_DELTA'));
v          = str2double(getenv('WF_V'));
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
Met = metricGet_ShapedShell(gridSize,wc,m,R1,R2,Rbuff,sigma,smoothFactor,v,1,gs,delta);
Ev = evalMetric(Met,0,1); T = Ev.energyTensorEulerian.tensor;
cx = wc(2)*spaceScale; cy = wc(3)*spaceScale;
J0 = round(cy);                                  % centre row
printf('RATIO PROFILE  delta = %.2f  vWarp = %.3f  (along +y, transverse)\n', delta, v);
printf('  %-7s %12s %12s %10s %12s\n','r [m]','rho','|f|','|f|/rho','null');
for jj = round(cy):round(cy + (R2+4)*spaceScale)
  r = (jj - cy)/spaceScale;
  if r < R1-2 || r > R2+2, continue; end
  I = round(cx);
  rho = T{1,1}(1,I,jj,3);
  fx  = T{1,2}(1,I,jj,3); fy = T{1,3}(1,I,jj,3);
  f   = sqrt(fx^2+fy^2);
  nu  = Ev.null(1,I,jj,3);
  if rho > 1e30
    printf('  %-7.2f %12.4e %12.4e %10.4f %12.3e\n', r, rho, f, f/rho, nu);
  end
end
