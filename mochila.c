#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int knapsack(int values[] , int weights[], int items, int capacity){
    if (items == 0 || capacity == 0){
        return 0;
    }

    if (weights[items - 1] > capacity){
        return knapsack(values, weights, items - 1, capacity);
    }

    int a = values[items-1] + knapsack(values, weights, items-1, capacity-weights[items-1]);
    int b = knapsack(values, weights, items-1, capacity);
    return __max(a, b);
}

int knapsack_memo(int values[], int weights[], int items, int capacity){
    int i, w;
    int v;
    int K[items+1][capacity+1];

    for (i = 0; i <= items; i++){
        for (w = 0; w <= capacity; w++){
            v++;
            if (i == 0 || w == 0){
                K[i][w] = 0;
            }
            else if (weights[i-1] <= w){
                K[i][w] = __max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w]);
            }
            else{
                K[i][w] = K[i-1][w];
            }
        }
    }
    // show real size of bytes the matrix in memory
    // printf("Size of matrix: %d", sizeof(K));
    printf("v: %d", v);

    return K[items][capacity];
}

int* read_values(FILE* ptr, int* size){

    int* values = malloc(sizeof(int));
    int i = 0;
    while(!feof(ptr)){
        fscanf(ptr, "%d", &values[i]);
        i++;
        values = realloc(values, sizeof(int)*(i+1));
    }
    *size = i-1;
    return values;
}


void main(int argc, char *argv[]){

    FILE* ptr_capacity;
    int items = 0;
    int capacity = 0;

    ptr_capacity = fopen("test//capacity.txt", "r");
    fscanf(ptr_capacity, "%d", &capacity);

    printf("\nCapacity: %d", capacity);



    FILE* ptr_values;
    ptr_values = fopen("test//values.txt", "r");
    int* values = read_values(ptr_values, &items);

    printf("\nItems: %d", items);

   
    // printf("\nValues: ");
    // for(int i = 0; i < items; i++){
    //     printf("%d ", values[i]);
    // }



    FILE* ptr_weights;
    ptr_weights = fopen("test//weights.txt", "r");
    int* weights = read_values(ptr_weights, &items);
    
    // printf("\nWeights: ");
    // for(int i = 0; i < items; i++){
    //     printf("%d ", weights[i]);
    // }




    // int values[] = {68, 62, 39, 20, 74, 63, 20, 100, 49, 74};
    // int weights[] = {83, 49, 70, 16, 19, 28, 71, 49, 23, 56};
    // int capacity = 100;
    // int items = sizeof(values)/sizeof(values[0]);




    clock_t start, end;
    double time_spent;

    // start = clock();
    // printf("\nC knapsack: %d", knapsack(values, weights, items, capacity));    
    // end = clock();
    // time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    // printf("\nTime spent: %f", time_spent);

    start = clock();
    printf("\nchegou aqui");
    printf("\nC knapsack memo: %d", knapsack_memo(values, weights, items, capacity));    
    printf("\nchegou aqui1");
    end = clock();
    time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime spent: %f", time_spent);


}

