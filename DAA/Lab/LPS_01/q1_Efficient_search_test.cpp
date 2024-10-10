#include <iostream>
#include <stdio.h>
#include <vector>
#include <ctime>
using namespace std;

int findPositionBinary(vector<int> &numbers, int k) {
    int low = 0;
    int high = numbers.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (numbers[mid] == k) {
            return mid + 1;
        } else if (numbers[mid] < k) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int findPositionLinear(vector<int>& numbers, int k) {
    int position = 0;
    for (int num : numbers) {
        position++;
        if (num == k) {
            return position;
        }
    }
    return -1;
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

void numPush(vector<int> &numbers, int num){
    int ele;
    for(int i = 0; i < num;i++){
        cout <<"Enter a Number: ";
        cin >> ele;
        numbers.push_back(ele);
    }
}

int main() {
    int elenum,k;
    vector<int> numbers;
    cout <<"Enter the number of elements: ";
    cin >> elenum;
    numPush(numbers, elenum);
    cout <<"Enter the element to be found: ";
    cin >> k;
    cout <<"\n";
    insertionSort(numbers, elenum);
    
    //Binary Search
    clock_t tStart = clock();
    int position = findPositionBinary(numbers, k);
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;

    //Linear Search
    tStart = clock();
    position = findPositionLinear(numbers, k);
    double time2=(double)(clock() - tStart)/CLOCKS_PER_SEC;

    cout <<"Position of the Element: "<<position<<endl;
    cout <<"\n";

	cout<<"Time taken for Linear Search: "<<time2<<endl;
    cout<<"Time taken for Binary Search: "<<time1<<endl;
    cout <<"\n";

    return 0;
}
