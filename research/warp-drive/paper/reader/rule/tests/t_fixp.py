import sys, math
B = 320; bad = 0; n = 0
for line in sys.stdin:
    t = line.split(); a, b, N, k = int(t[0]), int(t[1]), int(t[2]), int(t[3])
    ab, bd, q, dq, sh, s, d, mi, sq = t[4], int(t[5]), t[6], int(t[7]), int(t[8]), int(t[9]), int(t[10]), int(t[11]), int(t[12])
    m = int(t[13]); xs = [int(v) for v in t[14:14 + 2 * m]]; dt = int(t[14 + 2 * m])
    ok = int(ab) == (a * b) >> B and (q == 'Z' or int(q) == (a << B) // bd) and dq == a // N and sh == a >> k
    ok = ok and s == a + b and d == a - b and abs(mi) == abs(a) * N and sq == math.isqrt(abs(a) << B)
    ok = ok and dt == sum(xs[2 * i] * xs[2 * i + 1] for i in range(m)) >> B
    n += 1; bad += not ok
print('cases', n, 'disagreements', bad)
