function yy = smooth(y, span)
% Octave shim for MATLAB Curve Fitting Toolbox smooth(y, span), 'moving' method.
% Moving average over an odd span, with symmetrically shrinking windows at the ends.
  if nargin < 2, span = 5; end
  span = floor(span);
  if mod(span,2) == 0, span = span - 1; end
  if span < 1, span = 1; end
  y = y(:); n = numel(y); yy = zeros(n,1);
  h = (span-1)/2;
  for i = 1:n
    w = min([h, i-1, n-i]);          % symmetric shrink at the ends
    yy(i) = mean(y(i-w:i+w));
  end
  if span == 1, yy = y; end
end
