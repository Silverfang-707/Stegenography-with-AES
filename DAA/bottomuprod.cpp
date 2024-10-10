#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<time.h>
#include<ctime>
int maximum(int a, int b)
{    
    if(a>b)
        return a;
    return b;
}
int bottom_up_cut_rod(vector<int> &p, int length)
{    
    vector<int> r(100,0);
    int i,q,j;
    r[0] = 0;
    for (j=1;j<=length;j++)
    {
        q = INT_MIN;
        for(i=1;i<=j;i++)
        {
            q = maximum(q,p[i-1]+r[j-i]);
        }
        r[j] = q;
    }
    return r[length];
}

int main()
{
    srand(time(0));
    vector<int> p;
    int i,n,max_profit;
    cout<<"Enter the number of elements: ";
    cin>>n;
    for(i=0;i<n;i++)
    {
        p.push_back(rand());
    }
    clock_t tStart = clock();
    max_profit = bottom_up_cut_rod(p,n);
    double time=(double)(clock() - tStart)/CLOCKS_PER_SEC;
    cout<<"Max Profit: "<<max_profit<<endl;
    cout<<"Time Taken is: "<<time<<endl;
}