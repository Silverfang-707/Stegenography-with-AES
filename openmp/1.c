#include <stdio.h>
#include <omp.h>
#include <math.h>

#define NUM_THREADS 10
#define NUM_STUDENTS 2000

int main() {
    double marks[NUM_STUDENTS];
    double mean = 0.0, stddev = 0.0;

    // Initialize marks array here...

    omp_set_num_threads(NUM_THREADS);

    // Compute mean
    #pragma omp parallel for reduction(+:mean)
    for (int i = 0; i < NUM_STUDENTS; i++) {
        mean += marks[i];
    }
    mean /= NUM_STUDENTS;

    // Compute standard deviation
    #pragma omp parallel for reduction(+:stddev)
    for (int i = 0; i < NUM_STUDENTS; i++) {
        stddev += (marks[i] - mean) * (marks[i] - mean);
    }
    stddev = sqrt(stddev / NUM_STUDENTS);

    printf("Mean: %.2f, Standard Deviation: %.2f\n", mean, stddev);

    return 0;
}
