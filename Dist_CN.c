//Pràctica 2: Modelització del tractament d'ablació cardíaca IVS
//Euler implicit Gauss-Seidel

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


int main(){
    //Discretitzacions i nombre d'intervals
    //La longitud 
    double dz=(znorm(0.02)/Nz);
    double dt=(0.5*pow(dz,1));
    double gamma=dt/pow(dz,2);
    int Nt=(0.025/dt)+1; 
    double a;
    


    //el primer es la posició(j) el segon es el temps(i)
    double T[Nz+1][Nt+1];
    
    // omplim la matriu de temperatures amb les CC i CI
    for (int j = 0; j < Nz+1; j++)
    {
        T[j][0]=Tnorm(309.65);
    }

    for (int i = 0; i < Nt+1; i++)
    {
        T[0][i]=Tnorm(309.65);
        T[Nz][i]=Tnorm(309.65);
    }
    
    
    for (int i = 1; i < Nt+1; i++) //El temps el comencem a 1 perquè per t=0 ja tenim la CI omplerta
    {   
        int iter=0;
        for (int j = 1; j < Nz; j++) //Les posicions comencem a 1 i aqcabem a NZ-1 perque ja ho tenim omplert amb les CC
        {
            T[j][i]=T[j][i-1];  //imposem ansatz a t1 on diem que per totes les posicions la T valgui el que valia al temps anterior
        }
     
        do
        {   
            iter++;
            a=T[Nz-1][i]; //agafem la T a un punt en concret i quan fem l'operació de GS comparem amb el que hem trobat
            for (int j = 1; j < Nz; j++)
            {   
                T[j][i]=(1/(1+gamma))*(T[j][i-1]*(1-gamma)+dt+(gamma/2)*(T[j-1][i-1]+T[j+1][i-1]+T[j-1][i]+T[j+1][i]));
            }
        } while (iter<1500 && fabs(T[Nz-1][i]-a)>0.0000000000000001);//amb més precissió el nombre d'iteracions és el mateix
        
        printf("%d  ""%lf   ""%lf   \n", iter,  a,T[Nz-1][i]);//imprimeix el nombre d'iteracions que ha fet i els valors que comparem 
    }
    
    FILE* output; //generem un fitxer que direm output 
    //(perquè es guardi el fitxer s'ha de canviar la direcció d'on vols que te'l guardi, sino sortirà un error)
    
    output=fopen("CARPETA\\T_CN(0.5).txt","w"); // w de write
        fprintf(output,"%.18lf   ",0); //posem aquest 0 per a poder posar una columna amb el valor de la posició
    for (int i = 0; i < Nt+1; i++){
        fprintf(output,"%.18lf    ", dt*i);
   
    }
    fprintf(output, "\n");

    for (int j = 0; j < Nz+1; j++){
        fprintf(output,"%.18lf   ",dz*j);
        for (int i = 0; i < Nt+1; i++)
        {
            fprintf(output,"%.18lf    ",T[j][i]);
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

