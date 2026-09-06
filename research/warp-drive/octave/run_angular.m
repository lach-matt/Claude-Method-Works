% Angular dependence of the binding ratio.  The NEC failure was found on the
% TRANSVERSE axis; this asks how strongly the constraint varies with angle from
% the direction of motion, which is what says whether -- and which way -- to
% break sphericity.
spaceScale = str2double(getenv('WF_SCALE'));
v          = str2double(getenv('WF_V'));
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
Met = metricGet_ShapedShell(gridSize,wc,m,R1,R2,Rbuff,sigma,smoothFactor,v,1,gs,1.0);
Ev = evalMetric(Met,0,1); T = Ev.energyTensorEulerian.tensor;
cx = wc(2)*spaceScale; cy = wc(3)*spaceScale;
printf('ANGULAR PROFILE  vWarp = %.3f   (theta from +x, the direction of motion)\n', v);
printf('  %-10s %12s %12s %12s %10s\n','theta[deg]','max|f|/rho','at r [m]','min null','r(null)');
for th = [0 15 30 45 60 75 90]
  best=0; bestr=0; nmin=1e99; nr=0;
  for rr = (R1-2):0.25:(R2+2)
    x = rr*cosd(th); y = rr*sind(th);
    I = round(cx + x*spaceScale); J = round(cy + y*spaceScale);
    if I<4 || J<4 || I>gridSize(2)-3 || J>gridSize(3)-3, continue; end
    rho = T{1,1}(1,I,J,3);
    if rho < 1e39, continue; end
    f = sqrt(T{1,2}(1,I,J,3)^2 + T{1,3}(1,I,J,3)^2 + T{1,4}(1,I,J,3)^2);
    if f/rho > best, best = f/rho; bestr = rr; end
    nu = Ev.null(1,I,J,3);
    if nu < nmin, nmin = nu; nr = rr; end
  end
  printf('  %-10d %12.4f %12.2f %12.3e %10.2f\n', th, best, bestr, nmin, nr);
  fflush(stdout);
end
