#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

void selectionSort(vector<int> &elements, int n) {
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (elements[j] < elements[minIndex]) {
                minIndex = j;
            }
        }
        swap(elements[i], elements[minIndex]);
    }
}

void insertionSort(vector<int> &elements, int n) {  
    for(int j=1;j<n;j++)
    {
        int key = elements[j];
        int i = j-1;
        while((i>=0)&&(elements[i]>key))
        {
            elements[i+1] = elements[i];
            i = i-1;
        }
        elements[i+1] = key;
    }
}

void bestCase(int n){
    vector<int> elements;
    for(int i = 0; i < n; i++){
        elements.push_back(i);
    }
    clock_t tStart = clock();    
    selectionSort(elements, n);
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for BestCase in Selection Sort: "<<time1<<endl;
    tStart = clock();
    insertionSort(elements, n);
    time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for BestCase in Insertion Sort: "<<time1<<endl;
    printf("\n");
}

void averageCase(int n){
    vector<int> elements;
    for(int i = 0; i < n; i++){
        elements.push_back(rand());
    }
    clock_t tStart = clock();    
    selectionSort(elements, n);
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for AverageCase in Selection Sort: "<<time1<<endl;
    tStart = clock();
    insertionSort(elements, n);
    time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for AverageCase in Insertion Sort: "<<time1<<endl;
    printf("\n");
}

void worstCase(int n){
    vector<int> elements;
    for(int i = n; i > 0; i--){
        elements.push_back(i);
    }
    clock_t tStart = clock();    
    selectionSort(elements, n);
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for WorstCase in Selection Sort: "<<time1<<endl;
    tStart = clock();
    insertionSort(elements, n);
    time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for WorstCase in Insertion Sort: "<<time1<<endl;
    printf("\n");
}

int main(){
    int n;
    printf("--------Insertion Sort vs Selection Sort--------\n");
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    printf("\n");
    bestCase(n);
    averageCase(n);
    worstCase(n);    
}