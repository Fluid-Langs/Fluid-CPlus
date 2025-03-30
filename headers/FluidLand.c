#ifndef FLUIDLAND_C
#define FLUIDLAND_C

#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Added for string manipulation functions
#include <math.h>   // Added for mathematical functions

#ifdef __cplusplus
#   include <iostream>
#   include <string>
#endif // __cplusplus

// define common keywords
#define func r() void r()
#define import r #include <r>
#define xif (r) if (r)
#define Return r return r;
#define def r() class r()
#define main() int main()
#define ifn r #ifdef r
#define Nill NULL
#define let r = x int r = x
#define cosin r const r
#define loop r while (r)
#define print r printf("%s", r)
#define true 1
#define false 0

// Utility functions
#define max(a, b) ((a) > (b) ? (a) : (b)) // Function to get maximum of two values
#define min(a, b) ((a) < (b) ? (a) : (b)) // Function to get minimum of two values
#define swap(a, b) { typeof(a) temp = a; a = b; b = temp; } // Function to swap two values
#define strlen_custom(s) (sizeof(s) / sizeof(s[0]) - 1) // Custom string length function

// Additional utility functions
#define square(x) ((x) * (x)) // Function to calculate square of a number
#define cube(x) ((x) * (x) * (x)) // Function to calculate cube of a number
#define clamp(x, min, max) (x < min ? min : (x > max ? max : x)) // Clamp a value between min and max
#define abs_value(x) ((x) < 0 ? -(x) : (x)) // Absolute value function
#define pow_custom(base, exp) (pow((base), (exp))) // Power function
#define factorial(n) (n <= 1 ? 1 : (n) * factorial((n) - 1)) // Factorial function

// String manipulation
#define strcpy_custom(dest, src) strncpy(dest, src, sizeof(dest)) // Custom string copy
#define strcat_custom(dest, src) strncat(dest, src, sizeof(dest) - strlen(dest) - 1) // Custom string concatenate
#define strcmp_custom(s1, s2) strcmp(s1, s2) // Custom string compare
#define strrev_custom(s) strrev(s) // Custom string reverse (requires implementation)

// Memory management
#define allocate(size) malloc(size) // Memory allocation
#define deallocate(ptr) free(ptr) // Memory deallocation

// Debugging
#define debug(msg) printf("DEBUG: %s\n", msg) // Debugging macro
#define assert(condition) if (!(condition)) { printf("Assertion failed: %s\n", #condition); exit(1); } // Assertion macro

// Random number generation
#define random_int(min, max) (rand() % ((max) - (min) + 1) + (min)) // Random integer between min and max

// Array utilities
#define array_length(arr) (sizeof(arr) / sizeof(arr[0])) // Get length of an array
#define array_fill(arr, value, size) for (int i = 0; i < size; i++) arr[i] = value // Fill array with a value

// Type definitions
typedef struct { int x; int y; } Point; // Define a Point structure
typedef struct { float real; float imag; } Complex; // Define a Complex number structure

// Mathematical constants
#define PI 3.14159265358979323846 // Define PI constant
#define E 2.71828182845904523536 // Define Euler's number

// String constants
#define EMPTY_STRING "" // Define an empty string

// Built-in functions
#define print_array(arr, size) { \
    for (int i = 0; i < size; i++) { \
        printf("%d ", arr[i]); \
    } \
    printf("\n"); \
} // Print elements of an array

#define sum_array(arr, size) ({ \
    int sum = 0; \
    for (int i = 0; i < size; i++) { \
        sum += arr[i]; \
    } \
    sum; \
}) // Sum elements of an array

#define find_max_in_array(arr, size) ({ \
    int max_val = arr[0]; \
    for (int i = 1; i < size; i++) { \
        if (arr[i] > max_val) { \
            max_val = arr[i]; \
        } \
    } \
    max_val; \
}) // Find maximum value in an array

#define find_min_in_array(arr, size) ({ \
    int min_val = arr[0]; \
    for (int i = 1; i < size; i++) { \
        if (arr[i] < min_val) { \
            min_val = arr[i]; \
        } \
    } \
    min_val; \
}) // Find minimum value in an array

#define reverse_string(s) { \
    int len = strlen(s); \
    for (int i = 0; i < len / 2; i++) { \
        char temp = s[i]; \
        s[i] = s[len - i - 1]; \
        s[len - i - 1] = temp; \
    } \
} // Reverse a string in place

// Command-line functions
#define get_command_line_arg(argc, argv, index) (index < argc ? argv[index] : NULL) // Get command line argument
#define print_command_line_args(argc, argv) { \
    for (int i = 0; i < argc; i++) { \
        printf("Argument %d: %s\n", i, argv[i]); \
    } \
} // Print all command line arguments

#define read_input(prompt, buffer, size) { \
    printf("%s", prompt); \
    fgets(buffer, size, stdin); \
    buffer[strcspn(buffer, "\n")] = 0; /* Remove newline character */ \
} // Read input from the user

#define clear_screen() printf("\033[H\033[J") // Clear the console screen

#endif // FLUIDLAND_C