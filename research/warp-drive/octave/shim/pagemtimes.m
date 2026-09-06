function C = pagemtimes(varargin)
% Octave shim for MATLAB R2020b pagemtimes: page-wise matrix multiply over the
% leading two dimensions, broadcasting over all trailing dimensions.
% Supports pagemtimes(A,B) and pagemtimes(A,opA,B,opB) with 'none'/'transpose'.
  if nargin == 2
    A = varargin{1}; opA = 'none'; B = varargin{2}; opB = 'none';
  elseif nargin == 4
    A = varargin{1}; opA = varargin{2}; B = varargin{3}; opB = varargin{4};
  else
    error('pagemtimes shim: expected 2 or 4 arguments');
  end
  sA = size(A); sB = size(B);
  tail = sA(3:end);
  N = prod(tail);
  A = reshape(A, sA(1), sA(2), N);
  B = reshape(B, sB(1), sB(2), N);
  if strcmpi(opA, 'transpose') || strcmpi(opA, 'ctranspose')
    A = permute(A, [2 1 3]);
  end
  if strcmpi(opB, 'transpose') || strcmpi(opB, 'ctranspose')
    B = permute(B, [2 1 3]);
  end
  m = size(A,1); k = size(A,2); n = size(B,2);
  if size(B,1) ~= k
    error('pagemtimes shim: inner dimensions disagree (%d vs %d)', k, size(B,1));
  end
  C = zeros(m, n, N, class(A));
  for i = 1:m
    for j = 1:n
      acc = zeros(1, 1, N, class(A));
      for kk = 1:k
        acc = acc + A(i,kk,:) .* B(kk,j,:);
      end
      C(i,j,:) = acc;
    end
  end
  C = reshape(C, [m, n, tail]);
end
