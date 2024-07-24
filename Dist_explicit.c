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
    double dt=(0.25*pow(dz,2));
    int Nt=(0.025/dt)+1;

    //el primer es la posició(j) el segon es el temps(i)
    double T[Nz+1][Nt+1];
    //CC i CI
    for (int j = 0; j < Nz+1; j++)
    {
        T[j][0]=Tnorm(309.65);
    }

    for (int i = 0; i < Nt+1; i++)
    {
        T[0][i]=Tnorm(309.65);
        T[Nz][i]=Tnorm(309.65);
    }
    

    for (int i = 0; i < Nt; i++)
    {
        for (int j = 1; j < Nz; j++)
        {
            T[j][i+1]=F(dt,dz,T[j+1][i],T[j][i],T[j-1][i]);
        }
        
    }
    
    FILE* output; //generem un fitxer que direm output 
    //(perquè es guardi el fitxer s'ha de canviar la direcció d'on vols que te'l guardi, sino sortirà un error)
    
     output=fopen("CARPETA\\T_explicit(0.25).txt","w"); // w de write
        fprintf(output,"%.18lf   ",0); //posem aquest 0 per a poder posar una columna amb el valor de la posició
    for (int i = 0; i < Nt+1; i++){
        fprintf(output,"%.18lf    ", dt*i); //guardem els temps en la primera fila 
   
    }
    fprintf(output, "\n");

    for (int j = 0; j < Nz+1; j++){
        fprintf(output,"%.18lf   ",dz*j);//guardem la posició
        for (int i = 0; i < Nt+1; i++)
        {
            fprintf(output,"%.18lf    ",T[j][i]);//gaurdem les T
        }
        fprintf(output, "\n");
    }     
    
    fclose(output);

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
