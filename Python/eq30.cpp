#include <iostream>
#include <vector>

using namespace std;

vector<int> parent;

int find(int x) {
    if(parent[x] == x)
        return x;
    return parent[x] = find(parent[x]);
}

void union_set(int x, int y) {
    int px = find(x);
    int py = find(y);
    if(px != py)
        parent[px] = py;
}

int main() {
    int N, M;
    cin >> N >> M;
    parent.resize(N);
    for(int i = 0; i < N; i++)
        parent[i] = i;
    for(int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        union_set(u, v);
    }
    int components = 0;
    for(int i = 0; i < N; i++)
        if(parent[i] == i)
            components++;
    cout << components - 1 << endl;
    return 0;
}
