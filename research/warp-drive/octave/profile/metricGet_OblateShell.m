function [Metric] = metricGet_OblateShell(gridSize,worldCenter,m,R1,R2,Rbuff, ...
                                          sigma,smoothFactor,vWarp,doWarp, ...
                                          gridScaling,ecc)
% Oblate warp shell: the wall is thickened in the EQUATORIAL BELT, the region
% measured to carry the binding load, and left alone at the poles, which carry
% a third of it.  The direction of motion is +x, so the belt is (y,z).
%
%   R2eff(alpha) = R2 (1 + ecc sin^2 alpha),   sin^2 alpha = (y^2+z^2)/r^2
%   u            = R1 + (r-R1)(R2-R1)/(R2eff-R1)      shell coordinate
%
% and the spherical radial functions A, B, S are evaluated at u.  ecc = 0
% reproduces the sphere exactly.
%
% THIS IS NOT A SOLUTION of the Einstein equations -- it is a metric handed to
% the solver so the energy conditions can be TESTED on it.  The control is the
% vWarp = 0 run: if the deformation alone violates, the test is confounded.
  if nargin < 12, ecc = 0.0; end
  Metric.type="metric"; Metric.name="Oblate Warp Shell"; Metric.scaling=gridScaling;
  Metric.coords="cartesian"; Metric.index="covariant"; Metric.date=date;

  worldSize = sqrt((gridSize(2)*gridScaling(2)-worldCenter(2))^2 + ...
                   (gridSize(3)*gridScaling(3)-worldCenter(3))^2 + ...
                   (gridSize(4)*gridScaling(4)-worldCenter(4))^2);
  rsample = linspace(0, worldSize*1.2, 10^5);
  rho = zeros(1,numel(rsample)) + m/(4/3*pi*(R2^3-R1^3)).*(rsample>R1 & rsample<R2);
  [~, maxR] = min(diff(rho>0)); maxR = rsample(maxR);
  M = cumtrapz(rsample, 4*pi.*rho.*rsample.^2);
  P = tovShaped(rsample, rho, M);
  rho = smooth(smooth(smooth(smooth(rho,1.79*smoothFactor),1.79*smoothFactor), ...
                      1.79*smoothFactor),1.79*smoothFactor)';
  P   = smooth(smooth(smooth(smooth(P,smoothFactor),smoothFactor), ...
                      smoothFactor),smoothFactor)';
  M = cumtrapz(rsample, 4*pi.*rho.*rsample.^2); M(M<0)=max(M);
  Metric.params.rho=rho; Metric.params.P=P; Metric.params.M=M; Metric.params.rVec=rsample;

  S = compactSigmoid(rsample,R1,R2,sigma,Rbuff);
  S = smooth(smooth(S,smoothFactor),smoothFactor);
  B = (1-2*G.*M./rsample/c^2).^(-1); B(1)=1;
  a = alphaNumericSolver(M,P,maxR,rsample);
  A = -exp(2.*a);

  Metric.tensor = cell(4);
  for mu=1:4, for nu=1:4, Metric.tensor{mu,nu}=zeros(gridSize); end, end
  ShiftMatrix = zeros(gridSize);
  for i=1:gridSize(2)
   for j=1:gridSize(3)
    for k=1:gridSize(4)
      x = i*gridScaling(2)-worldCenter(2);
      y = j*gridScaling(3)-worldCenter(3);
      z = k*gridScaling(4)-worldCenter(4);
      r = sqrt(x^2+y^2+z^2);
      theta = atan2(sqrt(x^2+y^2),z); phi = atan2(y,x);
      if r > 0, s2 = (y^2+z^2)/r^2; else s2 = 0; end
      R2e = R2*(1 + ecc*s2);
      if r > R1
        u = R1 + (r-R1)*(R2-R1)/(R2e-R1);
      else
        u = r;
      end
      [~, mi] = min(abs(rsample-u));
      if rsample(mi) > u, mi = mi-1; end
      if mi < 1, mi = 1; end
      mi = mi + (u-rsample(mi))/(rsample(mi+1)-rsample(mi));
      g11 = legendreRadialInterp(A,mi); g22 = legendreRadialInterp(B,mi);
      [c11,c22,c23,c24,c33,c34,c44] = sph2cartDiag(theta,phi,g11,g22);
      Metric.tensor{1,1}(1,i,j,k)=c11; Metric.tensor{2,2}(1,i,j,k)=c22;
      Metric.tensor{2,3}(1,i,j,k)=c23; Metric.tensor{3,2}(1,i,j,k)=c23;
      Metric.tensor{2,4}(1,i,j,k)=c24; Metric.tensor{4,2}(1,i,j,k)=c24;
      Metric.tensor{3,3}(1,i,j,k)=c33; Metric.tensor{3,4}(1,i,j,k)=c34;
      Metric.tensor{4,3}(1,i,j,k)=c34; Metric.tensor{4,4}(1,i,j,k)=c44;
      ShiftMatrix(1,i,j,k) = legendreRadialInterp(S,mi);
    end
   end
  end
  if doWarp
    Metric.tensor{1,2} = -ShiftMatrix*vWarp;
    Metric.tensor{2,1} = Metric.tensor{1,2};
  end
end
