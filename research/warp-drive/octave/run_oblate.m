spaceScale=str2double(getenv('WF_SCALE')); vlist=str2num(getenv('WF_VLIST'));
ecc=str2double(getenv('WF_ECC'));
R1=10; Rbuff=0; R2=20; ct=5;
gridSize=ceil([1,2*(R2+10+ecc*R2)*spaceScale,2*(R2+10+ecc*R2)*spaceScale,ct]);
m=R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs=[1/(1000*c),1/spaceScale,1/spaceScale,1/spaceScale];
wc=[(ct+1)/2,(gridSize(2)+1)/2,(gridSize(3)+1)/2,(ct+1)/2].*gs;
printf('OBLATE SHELL  ecc = %.2f   grid %dx%d\n', ecc, gridSize(2), gridSize(3));
Met=metricGet_OblateShell(gridSize,wc,m,R1,R2,Rbuff,sigma,smoothFactor,1.0,1,gs,ecc);
base=Met.tensor{1,2};
printf('  %-8s %12s %10s %12s %12s\n','vWarp','rho_max','|f|/rho','null','strong');
for v=vlist
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Ev=evalMetric(Met,0,1); T=Ev.energyTensorEulerian.tensor;
  sl=@(A) A(1,4:end-3,4:end-3,3);
  rho=sl(T{1,1}); rm=max(rho(:));
  f=max(abs([reshape(sl(T{1,2}),[],1);reshape(sl(T{1,3}),[],1);reshape(sl(T{1,4}),[],1)]));
  A1=Ev.null(1,4:end-3,4:end-3,3); A2=Ev.strong(1,4:end-3,4:end-3,3);
  printf('  %-8.4f %12.4e %10.4f %12.3e %12.3e\n',v,rm,f/rm,min(A1(:)),min(A2(:)));
  fflush(stdout);
end
