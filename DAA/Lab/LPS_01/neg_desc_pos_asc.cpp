#include <iostream>
#include <vector>
using namespace std;

void insertionSortAsc(vector<int> &elements, int n) {  
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

void insertionSortDesc(vector<int> &elements, int n) {  
    for(int j=1;j<n;j++)
    {
        int key = elements[j];
        int i = j-1;
        while((i>=0)&&(elements[i]<key))
        {
            elements[i+1] = elements[i];
            i = i-1;
        }
        elements[i+1] = key;
    }
}

void arrangeNumbers(vector<int> &numbers) {
    vector<int> negatives;
    vector<int> positives;

    // Separate negative and positive numbers (including zero)
    for (int num : numbers) {
        if (num < 0)
            negatives.push_back(num);
        else
            positives.push_back(num);
    }

    // Sort negative numbers in descending order
    insertionSortDesc(negatives, negatives.size());

    // Sort positive numbers in ascending order
    insertionSortAsc(positives, positives.size());

    // Concatenate the negative numbers, zero, and positive numbers
    numbers.clear();
    numbers.insert(numbers.end(), negatives.begin(), negatives.end());
    numbers.insert(numbers.end(), positives.begin(), positives.end());
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
    vector<int> numbers;
    int n;
    cout <<"Enter the number of elements: ";
    cin >> n;
    numPush(numbers, n);
    arrangeNumbers(numbers);

    // Print the arranged sequence
    cout <<"Arranged sequence: "<< endl;
    for (int num : numbers)
        cout << num << " ";
    cout << endl;

    return 0;
}
