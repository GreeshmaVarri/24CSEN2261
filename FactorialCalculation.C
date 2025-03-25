#cHATGPT AI
#include <stdio.h>
#include <stdlib.h>

// Function to calculate the factorial of a number
unsigned long long factorial(int n) {
    if (n < 0) {
        fprintf(stderr, "Error: Factorial is not defined for negative numbers.\n");
        exit(1); // Exit with an error if the input is negative
    }

    unsigned long long result = 1; // Initialize the result to 1 (base case for multiplication)

    for (int i = 1; i <= n; i++) {
        result *= i; // Multiply result by the current number
    }

    return result; // Return the calculated factorial
}

int main() {
    int num;

    // Prompt user for input
    printf("Enter a non-negative integer: ");
    if (scanf("%d", &num) != 1) {
        fprintf(stderr, "Invalid input. Please enter an integer.\n");
        return 1; // Exit with an error if the input is not valid
    }

    // Calculate and display the factorial
    unsigned long long result = factorial(num);
    printf("The factorial of %d is %llu\n", num, result);

    return 0; // Indicate successful program termination
}
