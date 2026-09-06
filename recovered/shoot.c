#include <math.h>
/* identical arithmetic to rad._shoot: y[0]=1e-30, y[1]=y0*exp((l+.5)h); Numerov; node count; rescale */
int shoot(const double *q, int n, double h, int l, double *ylast){
    double *f=(double*)malloc(n*sizeof(double)); int i,nodes=0;
    double y0=1e-30, y1=y0*exp((l+0.5)*h), y2;
    for(i=0;i<n;i++) f[i]=1.0-h*h*q[i]/12.0;
    for(i=1;i<n-1;i++){
        y2=((12.0-10.0*f[i])*y1-f[i-1]*y0)/f[i+1];
        if(((y2<0)!=(y1<0)) && y1!=0.0) nodes++;
        if(fabs(y2)>1e100){y1/=1e100;y2/=1e100;}
        y0=y1;y1=y2;
    }
    *ylast=y1; free(f); return nodes;
}