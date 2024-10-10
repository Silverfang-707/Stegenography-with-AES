#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <SDL2/SDL.h>

const int N = 64;  // Grid size
const int WINDOW_SIZE = 512;

#define IX(i, j) ((i) + (N + 2) * (j))

__global__ void add_source(int size, float *x, float *s, float dt) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < size) {
        x[i] += dt * s[i];
    }
}

__global__ void diffuse(int size, int b, float *x, float *x0, float diff, float dt) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < size) {
        float a = dt * diff * N * N;
        x[IX(i % N, i / N)] = (x0[IX(i % N, i / N)] + a * (x[IX((i % N) - 1, i / N)] + x[IX((i % N) + 1, i / N)] + x[IX(i % N, (i / N) - 1)] + x[IX(i % N, (i / N) + 1)])) / (1 + 4 * a);
    }
}

__global__ void advect(int size, int b, float *d, float *d0, float *u, float *v, float dt) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < size) {
        float dt0 = dt * N;
        float x = (i % N) - dt0 * u[IX((i % N), (i / N))];
        float y = (i / N) - dt0 * v[IX((i % N), (i / N))];
        if (x < 0.5f) x = 0.5f;
        if (x > N + 0.5f) x = N + 0.5f;
        int i0 = (int)x;
        int i1 = i0 + 1;
        if (y < 0.5f) y = 0.5f;
        if (y > N + 0.5f) y = N + 0.5f;
        int j0 = (int)y;
        int j1 = j0 + 1;
        float s1 = x - i0;
        float s0 = 1 - s1;
        float t1 = y - j0;
        float t0 = 1 - t1;
        d[IX(i % N, i / N)] = s0 * (t0 * d0[IX(i0, j0)] + t1 * d0[IX(i0, j1)]) + s1 * (t0 * d0[IX(i1, j0)] + t1 * d0[IX(i1, j1)]);
    }
}

__global__ void project(int size, float *u, float *v, float *p, float *div) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < size) {
        div[IX(i % N, i / N)] = -0.5f * (u[IX((i % N) + 1, i / N)] - u[IX((i % N) - 1, i / N)] + v[IX(i % N, (i / N) + 1)] - v[IX(i % N, (i / N) - 1)]) / N;
        p[IX(i % N, i / N)] = 0;
    }
}

void step(float *u, float *v, float *u_prev, float *v_prev, float *dens, float *dens_prev, float visc, float diff, float dt) {
    int size = (N + 2) * (N + 2);
    add_source<<<(size + 255) / 256, 256>>>(size, u, u_prev, dt);
    add_source<<<(size + 255) / 256, 256>>>(size, v, v_prev, dt);
    add_source<<<(size + 255) / 256, 256>>>(size, dens, dens_prev, dt);

    diffuse<<<(size + 255) / 256, 256>>>(size, 1, u, u_prev, visc, dt);
    diffuse<<<(size + 255) / 256, 256>>>(size, 2, v, v_prev, visc, dt);
    project<<<(size + 255) / 256, 256>>>(size, u, v, u_prev, v_prev);

    advect<<<(size + 255) / 256, 256>>>(size, 1, u, u_prev, u_prev, v_prev, dt);
    advect<<<(size + 255) / 256, 256>>>(size, 2, v, v_prev, u_prev, v_prev, dt);
    project<<<(size + 255) / 256, 256>>>(size, u, v, u_prev, v_prev);

    diffuse<<<(size + 255) / 256, 256>>>(size, 0, dens, dens_prev, diff, dt);
    advect<<<(size + 255) / 256, 256>>>(size, 0, dens, dens_prev, u, v, dt);
}

int main() {
    int size = (N + 2) * (N + 2) * sizeof(float);

    float *u, *v, *u_prev, *v_prev, *dens, *dens_prev;
    cudaMallocManaged(&u, size);
    cudaMallocManaged(&v, size);
    cudaMallocManaged(&u_prev, size);
    cudaMallocManaged(&v_prev, size);
    cudaMallocManaged(&dens, size);
    cudaMallocManaged(&dens_prev, size);

    memset(u, 0, size);
    memset(v, 0, size);
    memset(u_prev, 0, size);
    memset(v_prev, 0, size);
    memset(dens, 0, size);
    memset(dens_prev, 0, size);

    // Simulation parameters
    float dt = 0.1f;
    float diff = 0.0f;
    float visc = 0.0f;

    // Add some initial density
    for (int i = 20; i <= 40; i++) {
        for (int j = 20; j <= 40; j++) {
            dens[IX(i, j)] = 100.0f;
        }
    }

    // Initialize SDL
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("Fluid Simulation",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WINDOW_SIZE,
                                          WINDOW_SIZE,
                                          SDL_WINDOW_SHOWN);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    SDL_Texture *texture = SDL_CreateTexture(renderer,
                                             SDL_PIXELFORMAT_RGBA8888,
                                             SDL_TEXTUREACCESS_STREAMING,
                                             WINDOW_SIZE,
                                             WINDOW_SIZE);

    for (int frame = 0; frame < 100; frame++) {
        step(u, v, u_prev, v_prev, dens, dens_prev, visc, diff, dt);

        // Update SDL texture
        uint32_t *pixels = new uint32_t[WINDOW_SIZE * WINDOW_SIZE];
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                float density = dens[IX(x, y)];
                uint8_t color = (density > 0) ? (uint8_t)fminf(255, density) : 0;
                pixels[y * N + x] = SDL_MapRGBA(SDL_PIXELFORMAT_RGBA8888, color, 0, 0, 255);
            }
        }
        SDL_UpdateTexture(texture, NULL, pixels, WINDOW_SIZE * sizeof(uint32_t));
        delete[] pixels;

        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        SDL_RenderPresent(renderer);

        // Handle events
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                goto end;
            }
        }
        SDL_Delay(100); // Delay to control frame rate
    }

end:
    // Cleanup
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    cudaFree(u);
    cudaFree(v);
    cudaFree(u_prev);
    cudaFree(v_prev);
    cudaFree(dens);
    cudaFree(dens_prev);

    return 0;
}
