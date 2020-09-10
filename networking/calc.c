#include <stdio.h>  // print and read functions

float calculator (char op, float a, float b){
    switch (op) {
        case '+':
            return a + b;

        case '-':
            return a - b;
            
        default:
            printf("Wrong operator");
            return 0;
    }
}
int main() {
    float a, b;
    char op;
    
    printf("Enter an arithmetic expression (e.g. 5 * 4):");
    scanf("%f %c %f", &a, &op, &b);
    printf("\n%f %c %f = %f\n", a, op, b, calculator(op, a, b));
    
    return 0;
}
