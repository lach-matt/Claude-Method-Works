/* shoot_x.c -- session 18, T7b. Two-sided INHOMOGENEOUS Numerov on the log mesh x = ln r,
   y'' = q(x) y + s(x),  y = r^{-1/2} P.  Outward from i=0 to m+1, inward from i=ie down to m.
   Homogeneous (h) and particular (p) branches for each side; the caller matches y[m], y[m+1].
   f = 1 - h^2 q/12 (as shoot.c);  Numerov: f[i+1] y[i+1] = (12-10 f[i]) y[i] - f[i-1] y[i-1] + h^2 (s[i+1]+10 s[i]+s[i-1])/12.
   No rescaling: starts are chosen by the caller so nothing overflows (see t7b_hf.py). */
void shoot_x(int n, double h, const double *f, const double *s, int m, int ie, double y0, double y1,
             double *yoh, double *yop, double *yih, double *yip)
{
    int i; double h2 = h*h/12.0;
    for (i = 0; i < n; i++) { yoh[i]=0; yop[i]=0; yih[i]=0; yip[i]=0; }
    yoh[0] = y0; yoh[1] = y1;                       /* outward homogeneous, regular start */
    yop[0] = 0.0; yop[1] = 0.0;                     /* outward particular */
    for (i = 1; i <= m; i++) {
        yoh[i+1] = ((12-10*f[i])*yoh[i] - f[i-1]*yoh[i-1]) / f[i+1];
        yop[i+1] = ((12-10*f[i])*yop[i] - f[i-1]*yop[i-1] + h2*(s[i+1]+10*s[i]+s[i-1])) / f[i+1];
    }
    if (ie > n-1) ie = n-1;
    yih[ie] = 1e-30; yih[ie-1] = 1e-30 * (1.0 + h*3.0);   /* decaying inward: grows as we go in; caller picks ie */
    /* particular inward: adiabatic start y ~ -s/q  (q>0 out there) */
    { double q0 = 12.0*(1.0-f[ie])/(h*h), q1 = 12.0*(1.0-f[ie-1])/(h*h);
      yip[ie]   = (q0 > 1e-12) ? -s[ie]/q0 : 0.0;
      yip[ie-1] = (q1 > 1e-12) ? -s[ie-1]/q1 : 0.0; }
    for (i = ie-1; i > m; i--) {
        yih[i-1] = ((12-10*f[i])*yih[i] - f[i+1]*yih[i+1]) / f[i-1];
        yip[i-1] = ((12-10*f[i])*yip[i] - f[i+1]*yip[i+1] + h2*(s[i+1]+10*s[i]+s[i-1])) / f[i-1];
    }
}
