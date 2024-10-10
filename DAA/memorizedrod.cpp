#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<time.h>
#include<ctime>

int memoized_cut_rod_aux(vector<int> &p, int length,vector<int> &r);
int maximum(int a, int b)
{    
    if(a>b)
        return a;
    return b;
}
int memoized_cut_rod(vector<int> &p, int length)
{    
    vector<int> r(100,0);
    int i;
    for(i=0;i<100;i++)
        r[i] = INT_MIN;
    return memoized_cut_rod_aux(p,length,r);    
}
int memoized_cut_rod_aux(vector<int> &p, int length,vector<int> &r)
{
    int q;
    if(r[length]>=0)
        return(r[length]);
    if(length==0)
        return 0;
    q = INT_MIN;
    for(int i=1;i<=length;i++)
        q = maximum(q,p[i-1]+memoized_cut_rod_aux(p,length-i,r));
    r[length] = q;
    return q;
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
    max_profit = memoized_cut_rod(p,n);
    double time=(double)(clock() - tStart)/CLOCKS_PER_SEC;
    cout<<"Max profit: "<<max_profit<<endl;
    cout<<"Time taken: "<<time<<endl;
}