% TARGET 1: does a warp solution satisfying ALL FOUR energy conditions exist?
%
% Corrected diagnostic throughout.  getEnergyConditions lowers FRAME indices
% with the COORDINATE metric in the Null and Weak branches (lines 110, 131)
% while using Minkowski in Dominant and Strong (158, 201).  Two of four are
% right; here all four are computed with eta, consistently.
%
% Convergence is the proof step.  A negative value that scales away as dx->0 is
% truncation error.  One that does not is physics.
spaceScale = str2double(getenv('WF_SCALE'));
vlist      = str2num(getenv('WF_VLIST'));
NANG = 60; NTIME = 6;

R1=10; Rbuff=0; R2=20; ct=5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, ct]);
m = R2/(2*G)*c^2*(1/3); sigma=0; smoothFactor=4000;
gs = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
wc = [(ct+1)/2, (2*(R2+10)*spaceScale+1)/2, (2*(R2+10)*spaceScale+1)/2, (ct+1)/2].*gs;
Met = metricGet_WarpShellComoving(gridSize, wc, m, R1, R2, Rbuff, sigma, smoothFactor, 1.0, 1, gs);
base = Met.tensor{1,2};

N = gridSize(2); ctr=(N+1)/2;
[X,Y] = ndgrid((1:N)-ctr,(1:N)-ctr); Rm = sqrt(X.^2+Y.^2)/spaceScale;
shell = (Rm>10.5)&(Rm<19.5);
outside = (Rm>=19.5);

nullv = generateUniformField("nulllike", NANG, 1, 0);
timev = generateUniformField("timelike", NANG, NTIME, 0);

% eta-lower a frame-contravariant tensor: flip the 0i signs.
function Tc = etalower(Tu)
  Tc = Tu;
  for i = 2:4
    Tc{1,i} = -Tc{1,i};  Tc{i,1} = -Tc{i,1};
  end
end
function mn = contract_null(Tc, V, NA, sl)
  mn = Inf;
  for ii = 1:NA
    acc = 0;
    for mu=1:4, for nu=1:4
      acc = acc + Tc{mu,nu}*V(mu,ii)*V(nu,ii);
    end, end
    mn = min(mn, min(sl(acc)));
  end
end
function mn = contract_time(Tc, V, NA, NT, sl)
  mn = Inf;
  for jj = 1:NT
    for ii = 1:NA
      acc = 0;
      for mu=1:4, for nu=1:4
        acc = acc + Tc{mu,nu}*V(mu,ii,jj)*V(nu,ii,jj);
      end, end
      mn = min(mn, min(sl(acc)));
    end
  end
end

printf('SCALE %g   dx = %.4f m   grid %dx%d\n', spaceScale, 1/spaceScale, N, N);
printf('  %-7s %-8s %13s %13s %13s %13s\n','vWarp','region','NULL','WEAK','rho_min','SEC-ish');
for v = vlist
  Met.tensor{1,2}=base*v; Met.tensor{2,1}=Met.tensor{1,2};
  Tcoord = getEnergyTensor(Met,0);
  Tu = doFrameTransfer(Met, Tcoord, "Eulerian", 0);
  Tc = etalower(Tu.tensor);                       % frame, covariant -- the correct object
  rho = squeeze(Tu.tensor{1,1}(1,:,:,3));         % T^00 frame = energy density
  for rg = {'shell','outside'}
    msk = shell; if strcmp(rg{1},'outside'), msk = outside; end
    sl = @(A) reshape(subsref(squeeze(A(1,:,:,3)), substruct('()',{msk})),[],1);
    nn = contract_null(Tc, nullv, NANG, sl);
    ww = contract_time(Tc, timev, NANG, NTIME, sl);
    rr = min(rho(msk));
    % SEC proxy: rho + sum of principal pressures, in the frame
    tr = squeeze(Tc{2,2}(1,:,:,3)+Tc{3,3}(1,:,:,3)+Tc{4,4}(1,:,:,3));
    ss = min(rho(msk) + tr(msk));
    printf('  %-7.4f %-8s %13.5e %13.5e %13.5e %13.5e\n', v, rg{1}, nn, ww, rr, ss);
    fflush(stdout);
  end
end
