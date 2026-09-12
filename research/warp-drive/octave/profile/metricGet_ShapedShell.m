function [Metric] = metricGet_ShapedShell(gridSize,worldCenter,m,R1,R2,Rbuff, ...
                                          sigma,smoothFactor,vWarp,doWarp, ...
                                          gridScaling,delta)
% Warp shell with a SHAPED radial density, otherwise following the same
% construction as Warp Factory's metricGet_WarpShellComoving (Helmerich & Fuchs,
% MIT) and calling its utilities sph2cartDiag, legendreRadialInterp,
% alphaNumericSolver and compactSigmoid.  The one physical change is the density:
%
%   rho(t) ~ delta + (1-delta) |cos(pi t)| ,   t = (r-R1)/(R2-R1)
%
% delta = 1 reproduces the uniform shell; delta = 0 puts the mass exactly where
% the momentum flux is, since f ~ |S''| ~ |cos(pi t)| for a raised-cosine shift.
% The pointwise constraint is |f|/rho, so matching the two equalises it.
  if nargin < 12, delta = 1.0; end

  Metric.type = "metric";  Metric.name = "Shaped Warp Shell";
  Metric.scaling = gridScaling;  Metric.coords = "cartesian";
  Metric.index = "covariant";  Metric.date = date;

  worldSize = sqrt((gridSize(2)*gridScaling(2)-worldCenter(2))^2 + ...
                   (gridSize(3)*gridScaling(3)-worldCenter(3))^2 + ...
                   (gridSize(4)*gridScaling(4)-worldCenter(4))^2);
  rsample = linspace(0, worldSize*1.2, 10^5);

  % shaped density, normalised to the requested total mass
  t = (rsample - R1)/(R2 - R1);
  % delta >= 0 : blend uniform with |cos(pi t)|  (symmetric, both edges)
  % delta <  0 : inner-weighted power law (1-t)^|delta|, which is what the
  %              measured ratio profile actually asks for -- the flux peaks at
  %              the INNER edge while smoothing pushes the density peak outward.
  if delta >= 0
    shp = delta + (1-delta)*abs(cos(pi*t));
  else
    shp = max(1-t, 0) .^ abs(delta);
  end
  shape = shp .* (rsample > R1 & rsample < R2);
  norm  = trapz(rsample, 4*pi*shape.*rsample.^2);
  rho   = m * shape / norm;
  Metric.params.rho = rho;

  [~, maxR] = min(diff(rho > 0));  maxR = rsample(maxR);
  M = cumtrapz(rsample, 4*pi.*rho.*rsample.^2);
  P = tovShaped(rsample, rho, M);
  Metric.params.P = P;

  rho = smooth(smooth(smooth(smooth(rho,1.79*smoothFactor),1.79*smoothFactor), ...
                      1.79*smoothFactor),1.79*smoothFactor)';
  P   = smooth(smooth(smooth(smooth(P,smoothFactor),smoothFactor), ...
                      smoothFactor),smoothFactor)';
  M = cumtrapz(rsample, 4*pi.*rho.*rsample.^2);  M(M<0) = max(M);
  Metric.params.M = M;  Metric.params.rVec = rsample;

  shiftRadialVector = compactSigmoid(rsample,R1,R2,sigma,Rbuff);
  shiftRadialVector = smooth(smooth(shiftRadialVector,smoothFactor),smoothFactor);

  B = (1-2*G.*M./rsample/c^2).^(-1);  B(1) = 1;
  a = alphaNumericSolver(M,P,maxR,rsample);
  A = -exp(2.*a);

  Metric.tensor = cell(4);
  for mu = 1:4, for nu = 1:4, Metric.tensor{mu,nu} = zeros(gridSize); end, end
  ShiftMatrix = zeros(gridSize);
  for i = 1:gridSize(2)
    for j = 1:gridSize(3)
      for k = 1:gridSize(4)
        x = i*gridScaling(2)-worldCenter(2);
        y = j*gridScaling(3)-worldCenter(3);
        z = k*gridScaling(4)-worldCenter(4);
        r = sqrt(x^2+y^2+z^2);
        theta = atan2(sqrt(x^2+y^2),z);  phi = atan2(y,x);
        [~, minIdx] = min(abs(rsample-r));
        if rsample(minIdx) > r, minIdx = minIdx - 1; end
        minIdx = minIdx + (r-rsample(minIdx))/(rsample(minIdx+1)-rsample(minIdx));
        g11 = legendreRadialInterp(A,minIdx);  g22 = legendreRadialInterp(B,minIdx);
        [c11,c22,c23,c24,c33,c34,c44] = sph2cartDiag(theta,phi,g11,g22);
        Metric.tensor{1,1}(1,i,j,k)=c11;  Metric.tensor{2,2}(1,i,j,k)=c22;
        Metric.tensor{2,3}(1,i,j,k)=c23;  Metric.tensor{3,2}(1,i,j,k)=c23;
        Metric.tensor{2,4}(1,i,j,k)=c24;  Metric.tensor{4,2}(1,i,j,k)=c24;
        Metric.tensor{3,3}(1,i,j,k)=c33;  Metric.tensor{3,4}(1,i,j,k)=c34;
        Metric.tensor{4,3}(1,i,j,k)=c34;  Metric.tensor{4,4}(1,i,j,k)=c44;
        ShiftMatrix(1,i,j,k) = legendreRadialInterp(shiftRadialVector,minIdx);
      end
    end
  end
  if doWarp
    Metric.tensor{1,2} = -ShiftMatrix*vWarp;
    Metric.tensor{2,1} = Metric.tensor{1,2};
  end
end
