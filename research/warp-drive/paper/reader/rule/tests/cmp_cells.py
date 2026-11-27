# per-field max |G_a - G_b| and max |G_b| for two cells of equal shape, each given as a G text file (f a b k X)
# or as the Gref array of a pilot-input file (tests/pilotin.cpp, 'FILE:Gref'); values are 2^-320 X
import sys, struct
def load(spec):
    if ':' in spec:
        fn, name = spec.split(':'); b = open(fn, 'rb').read(); pos = 8 + 12
        while pos < len(b):
            nl = b.index(b'\n', pos); nm = b[pos:nl].decode(); pos = nl + 1; n = struct.unpack_from('<Q', b, pos)[0]; pos += 8
            if nm == name:
                out = []
                for i in range(n):
                    w = struct.unpack_from('<6Q', b, pos + 48 * i); x = sum(w[j] << (64 * j) for j in range(6)); out.append(x - (1 << 384) if x >> 383 else x)
                return out
            pos += 48 * n
        raise KeyError(name)
    return [int(l.split()[4]) for l in open(spec)]
A, Bv = load(sys.argv[1]), load(sys.argv[2]); NN = len(A) // 5; assert len(A) == len(Bv)
names = 'R m n W s'.split(); worst = 0
for f in range(5):
    d = max(abs(A[f * NN + i] - Bv[f * NN + i]) for i in range(NN)) / 2.0 ** 320
    g = max(abs(Bv[f * NN + i]) for i in range(NN)) / 2.0 ** 320
    print('%s: max|difference| %.2e, max|G| %.2e, relative %.2e' % (names[f], d, g, d / g if g else 0)); worst = max(worst, d)
print('largest absolute difference %.2e; values equal: %d of %d' % (worst, sum(a == b for a, b in zip(A, Bv)), len(A)))
