//Pràctica 2: Modelització del tractament d'ablació cardíaca IVS
//Euler explicit

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

//Dades
#define cv (3686)
#define rho (1081)
#define kappa (0.56)
#define sigma (0.472)
#define V  (40*pow(2,-0.5))
#define d  (0.02)
#define T0  ((pow(V,2)*sigma)/kappa)
#define t0 (pow(d,2)*(cv*rho)/kappa)
#define z0 (d)
#define Nz 100


double znorm(double z);
double Tnorm(double T);
double tnorm(double t);
double F(double dt,double dz, double Tj1, double Tj2, double Tj3);



int main(){
    //Discretitzacions i nombre d'intervals
    double dz=(znorm(0.02)/Nz);
    double dt=(0.49*pow(dz,2));
    int Nt=(0.025/dt)+1;
    int z1=znorm(0.0075)/dz+1; //Mirarem un pas més per assegurar que mirem tota la regio sana i no ens deixem un tros
    int z2=znorm(0.0125)/dz; //Aqui al contrari ja que volem mirar un pas mes enrere per assegurar revisar tota la regio sana

    

    //el primer es la posició(j) el segon es el temps(i)
    double T[Nz+1][Nt+1];

    for (int j = 0; j < Nz+1; j++)
    {
        T[j][0]=Tnorm(309.65);
    }

    for (int i = 0; i < Nt+1; i++)
    {
        T[0][i]=Tnorm(309.65);
        T[Nz][i]=Tnorm(309.65);
    }
    
    int a=0;
    int b=0;
    for (int i = 0; i < Nt; i++)
    {
        for (int j = 1; j < Nz; j++)
        {
            T[j][i+1]=F(dt,dz,T[j+1][i],T[j][i],T[j-1][i]);
            
        }

            for (int j = z1; j <z2 ; j++)
        {
            if (T[j][i+1]>Tnorm(50+273.15))
            {
                a++;
                break;
            }     
            if (T[j][i+1]>Tnorm(80+273.15))
            {
                printf("S'han superat 80 ºC al temps: %.2lf ""\n", dt*i*t0);
                b=1;
                break;
            }     
        }
        for (int j = 0; j <z1 ; j++)
        {
            if (T[j][i+1]>Tnorm(50+273.15))
            {
                printf("S'ha arribat a 50 ºC a la regió sana al temps: %.2lf s""\n", dt*i*t0);
                b=1;
                break;
            }            
        }
                
        for (int j = z2; j <Nz ; j++)
        {
            if (T[j][i+1]>Tnorm(50+273.15))
            {
                printf("S'ha arribat a 50 ºC a la regió sana al temps: %.2lf s""\n", dt*i*t0);
                b=1;
                break;
            }            
        }

        if (b==1)
        {
            break;
        }
          
    }
    printf("la zona afectada ha estat a 50 ºC %.2lf segons", a*dt*t0);
    return 0;
}


double znorm(double z){
    double znorm=z/z0;
    return znorm;
}
double Tnorm(double T){
    double Tnorm=T/T0;
    return Tnorm;
}
double tnorm(double t){
    double tnorm=t/t0;
    return tnorm;
}

double F(double dt,double dz, double Tj1, double Tj2, double Tj3){
    return dt/pow(dz,2)*(Tj1-2*Tj2+Tj3)+dt+Tj2;
}

