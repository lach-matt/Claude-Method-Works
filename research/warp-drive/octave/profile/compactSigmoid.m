function f = compactSigmoid(r, R1, R2, sigma, Rbuff)
% RAISED-COSINE shift profile, overriding Warp Factory's compactSigmoid.
% Same contract: 1 inside R1+Rbuff, 0 outside R2-Rbuff, C^1 at both joins.
%   S(t) = (1 + cos(pi t))/2,  t = (r-a)/(b-a)
% Peak curvature is exactly pi^2/2 / d^2, against 9.841/d^2 for the original
% and a bang-bang bound of 4/d^2.  sigma is accepted and ignored: this profile
% has no sharpness parameter, which is the point.
  a = R1 + Rbuff; b = R2 - Rbuff;
  t = (r - a) ./ (b - a);
  f = 0.5*(1 + cos(pi*t));
  f(r <= a) = 1;
  f(r >= b) = 0;
  if any(isinf(f(:))) || any(~isreal(f(:)))
    error('raised-cosine profile returned non-numeric values');
  end
end
