% NEC computed three ways on one stress-energy tensor.
%
% Warp Factory's null path does:
%   (1) T_mn  (coordinate, covariant)
%   (2) M'*T*M  ->  T_ab  (orthonormal Eulerian frame, covariant)      [M'*g*M = eta]
%   (3) flip 0i signs  ->  T^ab (frame, contravariant)                 [raise with eta]
%   (4) changeTensorIndex(...,"covariant", metric) -> lower with g     [<-- coordinate g]
%   (5) contract with k = (1,nhat)/sqrt(2)
%
% Step (4) lowers FRAME indices with the COORDINATE metric.  The correct step is
% to lower with eta, which exactly undoes (3) and returns step (2).
%
%   SHIPPED   = as above.
%   FRAME     = contract step-(2) tensor T_ab with k^a = (1,nhat)/sqrt(2).   [correct]
%   COORD     = contract coordinate T_mn with k^m normalised so g_mn k^m k^n = 0.
%
% FRAME and COORD are the same scalar sampled over different direction sets, so
% agreement between them is the check that FRAME is right.
spaceScale = str2double(getenv('WF_SCALE'));
vlist      = str2num(getenv('WF_VLIST'));
NANG       = 100;
doCoord    = ~strcmp(getenv('WF_NOCOORD'),'1');

R1 = 10; Rbuff = 0; R2 = 20; cartoonThickness = 5;
gridSize = ceil([1, 2*(R2+10)*spaceScale, 2*(R2+10)*spaceScale, cartoonThickness]);
m = R2/(2*G)*c^2*(1/3);
sigma = 0; smoothFactor = 4000;
gridScaling = [1/(1000*c), 1/spaceScale, 1/spaceScale, 1/spaceScale];
worldCenter = [(cartoonThickness+1)/2, (2*(R2+10)*spaceScale+1)/2, ...
               (2*(R2+10)*spaceScale+1)/2, (cartoonThickness+1)/2].*gridScaling;

printf('SCALE %g   dx = %.3f m   %d null directions\n', spaceScale, 1/spaceScale, NANG);
Met = metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff, ...
                                  sigma, smoothFactor, 1.0, 1, gridScaling);
base_gtx = Met.tensor{1,2};

% Even directions on the sphere, matching generateUniformField('nulllike').
nvec = generateUniformField("nulllike", NANG, 1, 0);   % 4 x NANG, already /sqrt(2)

sl = @(A) A(1, 4:end-3, 4:end-3, 3);

printf('\n  %-8s %14s %14s %14s %10s\n', 'vWarp','SHIPPED','FRAME','COORD','FRAME/SHIP');
for v = vlist
  Met.tensor{1,2} = base_gtx * v;
  Met.tensor{2,1} = Met.tensor{1,2};

  Tcoord = getEnergyTensor(Met, 0);
  Tfrup  = doFrameTransfer(Met, Tcoord, "Eulerian", 0);   % T^ab, frame

  % ---- SHIPPED -------------------------------------------------------------
  shipped = getEnergyConditions(Tcoord, Met, "Null", NANG, 1, 0, 0);
  s_ship  = min(reshape(sl(shipped),[],1));

  % ---- FRAME: lower step-(3) with eta (undo the sign flip) ------------------
  Tf = Tfrup.tensor;
  for i = 2:4
    Tf{1,i} = -Tf{1,i};    Tf{i,1} = -Tf{i,1};
  end
  s_frame = Inf;
  for ii = 1:NANG
    acc = zeros(size(Tf{1,1}));
    for mu = 1:4
      for nu = 1:4
        acc = acc + Tf{mu,nu} * nvec(mu,ii) * nvec(nu,ii);
      end
    end
    s_frame = min(s_frame, min(reshape(sl(acc),[],1)));
  end

  % ---- COORD: coordinate T_mn with k made null against g --------------------
  Tc = changeTensorIndex(Tcoord, "covariant", Met).tensor;
  g  = changeTensorIndex(Met, "covariant").tensor;
  s_coord = NaN;
  if doCoord
  s_coord = Inf;
  for ii = 1:NANG
    n = nvec(2:4,ii) / norm(nvec(2:4,ii));      % unit spatial direction
    % k = (kt, n).  Solve g_mn k^m k^n = 0 for kt:
    %   g_tt kt^2 + 2 kt (g_ti n^i) + g_ij n^i n^j = 0
    A = g{1,1};
    B = g{1,2}*n(1) + g{1,3}*n(2) + g{1,4}*n(3);
    C = zeros(size(A));
    for a = 1:3
      for b = 1:3
        C = C + g{a+1,b+1} * n(a) * n(b);
      end
    end
    disc = max(B.^2 - A.*C, 0);
    kt = (-B - sqrt(disc)) ./ A;                % future-directed root (A<0)
    k = {kt, n(1)*ones(size(A)), n(2)*ones(size(A)), n(3)*ones(size(A))};
    nrm = sqrt(kt.^2 + 1);                      % match generateUniformField scaling
    acc = zeros(size(A));
    for mu = 1:4
      for nu = 1:4
        acc = acc + Tc{mu,nu} .* k{mu} .* k{nu} ./ (nrm.^2);
      end
    end
    s_coord = min(s_coord, min(reshape(sl(acc),[],1)));
  end
  end

  printf('  %-8.4f %14.5e %14.5e %14.5e %10.4f\n', ...
         v, s_ship, s_frame, s_coord, s_frame/s_ship);
  fflush(stdout);
end
