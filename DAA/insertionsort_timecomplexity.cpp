#include<iostream>
#include<vector>
#include<ctime>
using namespace std;

void averageCase(int n)
{
    vector<int> elements;
    int key,i,j;
    for(i=0;i<n;i++)
    {
        elements.push_back(rand());
    }
	clock_t tStart = clock();    
    for(j=1;j<n;j++)
    {
        key = elements[j];
        i = j-1;
        while((i>=0)&&(elements[i]>key))
        {
            elements[i+1] = elements[i];
            i = i-1;
        }
        elements[i+1] = key;
    }
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for AverageCase: "<<time1<<endl;
}

void bestCase(int n)
{
    vector<int> elements;
    int key,i,j;
    for(i=0;i<n;i++)
    {
        elements.push_back(i);
    }
	clock_t tStart = clock();    
    for(j=1;j<n;j++)
    {
        key = elements[j];
        i = j-1;
        while((i>=0)&&(elements[i]>key))
        {
            elements[i+1] = elements[i];
            i = i-1;
        }
        elements[i+1] = key;
    }
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
    cout<<"Time taken for BestCase: "<<time1<<endl;
}

void worstCase(int n)
{
    vector<int> elements;
    int key,i,j;
    for(j=n;j>=0;--j)
    {
        elements.push_back(j);
    }
	clock_t tStart = clock();    
    for(j=1;j<n;j++)
    {
        key = elements[j];
        i = j-1;
        while((i>=0)&&(elements[i]>key))
        {
            elements[i+1] = elements[i];
            i = i-1;
        }
        elements[i+1] = key;
    }
    double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for WorstCase: "<<time1<<endl;
}

int main()
{
    int n;
    cout<<"Enter the number of elements: ";
    cin>>n;
    bestCase(n);
    worstCase(n);
    averageCase(n);
}