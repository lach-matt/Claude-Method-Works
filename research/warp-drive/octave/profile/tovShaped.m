function P = tovShaped(r, rho, M)
% Numerically integrate the Tolman-Oppenheimer-Volkoff equation inward from the
% outer edge with P = 0 there, for an ARBITRARY radial mass-density profile.
%
% Warp Factory's TOVconstDensity is the interior-Schwarzschild closed form for a
% UNIFORM SPHERE and cannot represent a shaped shell.  This is the general case:
%   dP/dr = -G (rho + P/c^2)(M + 4 pi r^3 P/c^2) / ( r^2 (1 - 2GM/(c^2 r)) )
% Heun (2nd-order) stepping inward on the supplied radial sample.
  P = zeros(size(r));
  n = numel(r);
  f = @(rr, MM, rr_rho, PP) -G*(rr_rho + PP/c^2).*(MM + 4*pi*rr.^3.*PP/c^2) ...
                             ./ ( rr.^2 .* (1 - 2*G*MM./(c^2*rr)) );
  % find the outermost index where rho > 0; integrate inward from there
  idx = find(rho > 0, 1, 'last');
  if isempty(idx), return; end
  for i = idx:-1:2
    h  = r(i) - r(i-1);                       % positive
    k1 = f(r(i),   M(i),   rho(i),   P(i));
    Pp = P(i) - h*k1;                          % predictor, stepping inward
    k2 = f(r(i-1), M(i-1), rho(i-1), Pp);
    P(i-1) = P(i) - h*(k1 + k2)/2;
    if ~isfinite(P(i-1)), P(i-1) = P(i); end
  end
  P(rho <= 0 & r < r(idx)) = 0;                % vacuum interior
  P(r >= r(idx)) = 0;                          % vacuum exterior
  P(P < 0) = 0;
end
