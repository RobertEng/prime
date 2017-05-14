#include<stdio.h>
#include<omp.h>
main(){
    int id;
    #pragma omp parallel
    {
        id = omp_get_thread_num();
        printf("Greetings from process %d!/n", id);
    }
}