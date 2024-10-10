#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<ctime>
#include<time.h>
int matrix_chain_mul(int i, int j, vector<int> &p)
{
    int min_cost = INT_MAX,k,left_cost,right_cost,total_cost;    
    if(i==j)
        return 0;
    for(k=i;k<j;k++)
    {       
        left_cost = matrix_chain_mul(i,k,p);
        right_cost = matrix_chain_mul(k+1,j,p);
        total_cost = left_cost + right_cost + p[i-1] * p[k] * p[j];
        if(total_cost<min_cost)
        {
            min_cost = total_cost;
            
        }
    }
    return min_cost;
}

int main()
{
    srand(time(0));
    int n;
    vector<int> p;
    cout<<"Enter the number of elements: ";
    cin>>n;
    for(int z=0;z<n;z++){
        p.push_back(rand());
    }
    clock_t start = clock();
    int ans = matrix_chain_mul(1,n-1,p);
    double time=(double)(clock() - start)/CLOCKS_PER_SEC;
    cout<<"Minimum cost: "<<ans<<endl;
    cout<<"Time Taken is: "<<time<<endl;
}
