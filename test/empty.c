#include <stdio.h>
#include <stdlib.h>

int* solution(int N, int K, int* seat, int* out_n) {
    int* reserved = (int*)calloc(N + 1, sizeof(int));
    int* result = (int*)malloc(N * sizeof(int)); // Allocate memory based on maximum possible seats
    *out_n = 0; // Initialize out_n to 0

    int next_seat = 1;

    for (int i = 0; i < K; i++) {
        if (seat[i] == 0) {
            // Find the next available seat
            while (reserved[next_seat]) {
                next_seat++;
            }
            reserved[next_seat] = 1;
            result[*out_n] = next_seat;
            (*out_n)++; // Increment out_n when a seat is assigned
            // Update next_seat to the next available seat
            next_seat++;
        } else {
            // Free the reserved seat
            reserved[seat[i]] = 0;
            result[*out_n] = seat[i];
            (*out_n)++; // Increment out_n when a seat is assigned
            // Update next_seat only if the canceled seat is before it
            if (seat[i] < next_seat) {
                next_seat = seat[i];
            }
        }
    }

    free(reserved);
    return result;
}

int main() {
    int out_n;
    int N;
    scanf("%d", &N);
    int K;
    scanf("%d", &K);
    int i_seat;
    int *seat = (int *)malloc(sizeof(int)*K);
    for(i_seat = 0; i_seat < K; i_seat++)
        scanf("%d", &seat[i_seat]);

    int* out = solution(N, K, seat, &out_n);
    printf("%d", out[0]);
    for(int i_out = 1; i_out < out_n; i_out++)
        printf(" %d", out[i_out]);

    free(seat);
    free(out);
    return 0;
}
