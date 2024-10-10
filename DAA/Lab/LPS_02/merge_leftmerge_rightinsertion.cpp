#include <iostream>
#include <vector>
#include <time.h>
#include <ctime>
using namespace std;

void insertionSort(vector<int>& arr, int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1);
    vector<int> R(n2);

    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }

    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        insertionSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

void bestCase(int n){
    vector<int> elements;
    for(int i=0; i<n; i++){
        elements.push_back(i);
    }
    clock_t start = clock();
    mergeSort(elements, 0, n - 1);
    double time = (double)(clock()-start)/CLOCKS_PER_SEC;
    cout<<"Time taken for Best Case: "<<time<<endl;
}

void averageCase(int n){
    vector<int> elements;
    for(int i=0; i<n; i++){
        elements.push_back(rand());
    }
    clock_t start = clock();
    mergeSort(elements, 0, n - 1);
    double time = (double)(clock()-start)/CLOCKS_PER_SEC;
    cout<<"Time taken for Average Case: "<<time<<endl;
}

void worstCase(int n){
    vector<int> elements;
    for(int i=n; i>0; i--){
        elements.push_back(i);
    }
    clock_t start = clock();
    mergeSort(elements, 0, n - 1);
    double time = (double)(clock()-start)/CLOCKS_PER_SEC;
    cout<<"Time taken for Worst Case: "<<time<<endl;
}

int main() {
    srand(time(0));
    vector<int> elements;
    int n;
    cout<<"Enter the number of elements: ";
    cin >> n;
    bestCase(n);
    averageCase(n);
    worstCase(n);
    return 0;
}
