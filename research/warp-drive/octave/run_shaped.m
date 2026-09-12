spaceScale = str2double(getenv('WF_SCALE'));
vlist      = str2num(getenv('WF_VLIST'));
delta      = str2double(getenv('WF_DELTA'));
R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
printf('SHAPED SHELL  delta = %.3f  (1 = uniform, 0 = mass tracks |S''''|)\n', delta);
Met = metricGet_ShapedShell(gridSize,wc,m,R1,R2,Rbuff,sigma,smoothFactor,1.0,1,gs,delta);
base = Met.tensor{1,2};
printf('  %-8s %12s %10s %10s %12s\n','vWarp','rho_max','|f|/rho','|p|/rho','null');
for v = vlist
  Met.tensor{1,2} = base*v; Met.tensor{2,1} = Met.tensor{1,2};
  Ev = evalMetric(Met,0,1); T = Ev.energyTensorEulerian.tensor;
  sl = @(A) A(1,4:end-3,4:end-3,3);
  rho = sl(T{1,1}); rm = max(rho(:));
  f = max(abs([reshape(sl(T{1,2}),[],1);reshape(sl(T{1,3}),[],1);reshape(sl(T{1,4}),[],1)]));
  pk = max(abs([reshape(sl(T{2,2}),[],1);reshape(sl(T{3,3}),[],1);reshape(sl(T{4,4}),[],1)]));
  A = Ev.null(1,4:end-3,4:end-3,3);
  printf('  %-8.4f %12.4e %10.4f %10.4f %12.3e\n', v, rm, f/rm, pk/rm, min(A(:)));
  fflush(stdout);
end
