#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 64  // Grid size
#define IX(i, j) ((i) + (N + 2) * (j))

typedef struct {
    float *u, *v;       // Velocity
    float *u_prev, *v_prev;
    float *dens, *dens_prev; // Density
} Fluid;

void add_source(int N, float *x, float *s, float dt) {
    for (int i = 0; i < (N + 2) * (N + 2); i++) x[i] += dt * s[i];
}

void diffuse(int N, int b, float *x, float *x0, float diff, float dt) {
    float a = dt * diff * N * N;
    for (int k = 0; k < 20; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                x[IX(i, j)] = (x0[IX(i, j)] + a * (x[IX(i - 1, j)] + x[IX(i + 1, j)] + x[IX(i, j - 1)] + x[IX(i, j + 1)])) / (1 + 4 * a);
            }
        }
    }
}

void advect(int N, int b, float *d, float *d0, float *u, float *v, float dt) {
    int i0, j0, i1, j1;
    float x, y, s0, t0, s1, t1, dt0;

    dt0 = dt * N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            x = i - dt0 * u[IX(i, j)];
            y = j - dt0 * v[IX(i, j)];

            if (x < 0.5) x = 0.5;
            if (x > N + 0.5) x = N + 0.5;
            i0 = (int) x;
            i1 = i0 + 1;

            if (y < 0.5) y = 0.5;
            if (y > N + 0.5) y = N + 0.5;
            j0 = (int) y;
            j1 = j0 + 1;

            s1 = x - i0;
            s0 = 1 - s1;
            t1 = y - j0;
            t0 = 1 - t1;

            d[IX(i, j)] = s0 * (t0 * d0[IX(i0, j0)] + t1 * d0[IX(i0, j1)]) +
                          s1 * (t0 * d0[IX(i1, j0)] + t1 * d0[IX(i1, j1)]);
        }
    }
}

void project(int N, float *u, float *v, float *p, float *div) {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            div[IX(i, j)] = -0.5f * (u[IX(i + 1, j)] - u[IX(i - 1, j)] + v[IX(i, j + 1)] - v[IX(i, j - 1)]) / N;
            p[IX(i, j)] = 0;
        }
    }

    for (int k = 0; k < 20; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                p[IX(i, j)] = (div[IX(i, j)] + p[IX(i - 1, j)] + p[IX(i + 1, j)] + p[IX(i, j - 1)] + p[IX(i, j + 1)]) / 4;
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            u[IX(i, j)] -= 0.5f * N * (p[IX(i + 1, j)] - p[IX(i - 1, j)]);
            v[IX(i, j)] -= 0.5f * N * (p[IX(i, j + 1)] - p[IX(i, j - 1)]);
        }
    }
}

void step(Fluid *fluid, float visc, float diff, float dt) {
    add_source(N, fluid->u, fluid->u_prev, dt);
    add_source(N, fluid->v, fluid->v_prev, dt);
    add_source(N, fluid->dens, fluid->dens_prev, dt);

    float *temp;

    temp = fluid->u_prev;
    fluid->u_prev = fluid->u;
    fluid->u = temp;

    temp = fluid->v_prev;
    fluid->v_prev = fluid->v;
    fluid->v = temp;

    diffuse(N, 1, fluid->u, fluid->u_prev, visc, dt);
    diffuse(N, 2, fluid->v, fluid->v_prev, visc, dt);

    project(N, fluid->u, fluid->v, fluid->u_prev, fluid->v_prev);

    temp = fluid->u_prev;
    fluid->u_prev = fluid->u;
    fluid->u = temp;

    temp = fluid->v_prev;
    fluid->v_prev = fluid->v;
    fluid->v = temp;

    advect(N, 1, fluid->u, fluid->u_prev, fluid->u_prev, fluid->v_prev, dt);
    advect(N, 2, fluid->v, fluid->v_prev, fluid->u_prev, fluid->v_prev, dt);

    project(N, fluid->u, fluid->v, fluid->u_prev, fluid->v_prev);

    temp = fluid->dens_prev;
    fluid->dens_prev = fluid->dens;
    fluid->dens = temp;

    diffuse(N, 0, fluid->dens, fluid->dens_prev, diff, dt);
    advect(N, 0, fluid->dens, fluid->dens_prev, fluid->u, fluid->v, dt);
}

void clear_data(Fluid *fluid) {
    for (int i = 0; i < (N + 2) * (N + 2); i++) {
        fluid->u[i] = fluid->v[i] = fluid->u_prev[i] = fluid->v_prev[i] = 0.0f;
        fluid->dens[i] = fluid->dens_prev[i] = 0.0f;
    }
}

Fluid* create_fluid() {
    Fluid *fluid = (Fluid*) malloc(sizeof(Fluid));
    fluid->u = (float*) malloc((N + 2) * (N + 2) * sizeof(float));
    fluid->v = (float*) malloc((N + 2) * (N + 2) * sizeof(float));
    fluid->u_prev = (float*) malloc((N + 2) * (N + 2) * sizeof(float));
    fluid->v_prev = (float*) malloc((N + 2) * (N + 2) * sizeof(float));
    fluid->dens = (float*) malloc((N + 2) * (N + 2) * sizeof(float));
    fluid->dens_prev = (float*) malloc((N + 2) * (N + 2) * sizeof(float));

    clear_data(fluid);

    return fluid;
}

void free_fluid(Fluid *fluid) {
    free(fluid->u);
    free(fluid->v);
    free(fluid->u_prev);
    free(fluid->v_prev);
    free(fluid->dens);
    free(fluid->dens_prev);
    free(fluid);
}

int main() {
    Fluid *fluid = create_fluid();

    // Simulation parameters
    float dt = 0.1f;
    float diff = 0.0f;
    float visc = 0.0f;

    // Add some initial density
    for (int i = 20; i <= 40; i++) {
        for (int j = 20; j <= 40; j++) {
            fluid->dens[IX(i, j)] = 100.0f;
        }
    }

    for (int frame = 0; frame < 100; frame++) {
        step(fluid, visc, diff, dt);

        // Print density for debugging
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                printf("%.1f ", fluid->dens[IX(i, j)]);
            }
            printf("\n");
        }
        printf("\n");
    }

    free_fluid(fluid);
    return 0;
}
