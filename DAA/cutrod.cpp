#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<ctime>
#include<time.h>

int maximum(int a, int b)
{    
    if(a>b)
        return a;
    return b;
}

int cut_rod(vector<int> p, int length)
{    
    int i;
    int q=INT_MIN;
    if(length==0)
        return 0;
    for(i=1;i<=length;i++)
    {
        q = maximum(q,p[i-1]+cut_rod(p,length-i));
    }
    return q;
}

int main()
{
    srand(time(0));
    vector<int> p;
    int i,n,max_profit;
    cout<<"Enter the number of cuts: ";
    cin>>n;
    for(i=0;i<n;i++)
    {
        p.push_back(rand());
    }
    clock_t tStart = clock();
    max_profit = cut_rod(p,n);
    double time=(double)(clock() - tStart)/CLOCKS_PER_SEC;
    cout<<"Max profit: "<<max_profit<<endl;
    cout<<"Time taken: "<<time<<endl;
}