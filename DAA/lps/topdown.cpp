#include <iostream>
#include <vector>
#include <climits>
using namespace std;

void printMatrix(vector<vector<int>> &matrix) {
    for (int i = 1; i < matrix.size(); i++) {
        for (int j = i + 1; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int MatrixChainOrder(vector<int> &p, int i, int j, vector<vector<int>> &m, vector<vector<int>> &s) {
    if (m[i][j] < INT_MAX) {
        return m[i][j];
    }

    if (i == j) {
        m[i][j] = 0;
    } else {
        for (int k = i; k < j; k++) {
            int q = MatrixChainOrder(p, i, k, m, s) + MatrixChainOrder(p, k + 1, j, m, s) + p[i - 1] * p[k] * p[j];
            if (q < m[i][j]) {
                m[i][j] = q;
                s[i][j] = k;
            }
        }
    }
    return m[i][j];
}

int main() {
    int n;
    cin >> n;

    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    vector<vector<int>> m(n, vector<int>(n, INT_MAX));
    vector<vector<int>> s(n, vector<int>(n));

    int minCost = MatrixChainOrder(p, 1, n - 1, m, s);

    cout << "M table:" << endl;
    printMatrix(m);

    cout << "S table:" << endl;
    printMatrix(s);

    cout << "Minimum cost: " << minCost << endl;

    return 0;
}
