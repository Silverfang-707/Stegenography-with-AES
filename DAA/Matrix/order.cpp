#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<ctime>
#include<time.h>

void matrix_chain_order(vector<int> p, vector<vector<int> >& m, vector<vector<int> >& s)
{
    int n,l,i,j,k,q;
    n = p.size()-1;
    for(l=2;l<=n;l++)
    {
        for(i=1;i<=n-l+1;i++)
        {
            j = i+l-1;
            m[i-1][j-1] = INT_MAX;
            for(k=i;k<=j-1;k++)
            {
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j];
                if(q<m[i-1][j-1])
                {
                    m[i-1][j-1] = q;
                    s[i-1][j-1] = k;
                }
            }
        }
    }
}

void print_Optimal_Parens(vector<vector<int> >& s, int i, int j)
{
    if(i==j)
        cout<<"A"<<i;
    else
    {
        cout<<"(";
        print_Optimal_Parens(s,i,s[i-1][j-1]);
        print_Optimal_Parens(s,s[i-1][j-1]+1,j);
        cout<<")";
    }
}

int main()
{
    srand(time(0));
    int n,i,j;
    cout<<"Enter the number of elements: ";
    cin>>n;
    vector<int> p(n);
    for(i=0;i<n;i++)
        p[i]=rand();
    vector<vector<int> > m(n-1,vector<int>(n-1,0));
    vector<vector<int> > s(n-1,vector<int>(n-1,0));
    clock_t start = clock();
    matrix_chain_order(p,m,s);
    double time=(double)(clock() - start)/CLOCKS_PER_SEC;
    cout<<"'M' table is "<<endl;
    for(i=0;i<n-2;i++)
    {
        for(j=1;j<n-1;j++)
            cout<<m[i][j]<<" ";
        cout<<endl;
    }
    cout<<"\n'S' table is "<<endl;
    for(i=0;i<n-2;i++)
    {
        for(j=0;j<n-1;j++)
            cout<<s[i][j]<<" ";
        cout<<endl;
    }
    
    cout<<"\nMinimum cost is "<<m[0][n-2]<<endl<<"\n";
    print_Optimal_Parens(s,1,n-1);
    cout<<"\nTime taken: "<<time<<endl;
}#include<iostream>
using namespace std;
#include<vector>
#include<limits.h>
#include<ctime>
#include<time.h>

void matrix_chain_order(vector<int> p, vector<vector<int> >& m, vector<vector<int> >& s)
{
    int n,l,i,j,k,q;
    n = p.size()-1;
    for(l=2;l<=n;l++)
    {
        for(i=1;i<=n-l+1;i++)
        {
            j = i+l-1;
            m[i-1][j-1] = INT_MAX;
            for(k=i;k<=j-1;k++)
            {
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j];
                if(q<m[i-1][j-1])
                {
                    m[i-1][j-1] = q;
                    s[i-1][j-1] = k;
                }
            }
        }
    }
}

void print_Optimal_Parens(vector<vector<int> >& s, int i, int j)
{
    if(i==j)
        cout<<"A"<<i;
    else
    {
        cout<<"(";
        print_Optimal_Parens(s,i,s[i-1][j-1]);
        print_Optimal_Parens(s,s[i-1][j-1]+1,j);
        cout<<")";
    }
}

int main()
{
    srand(time(0));
    int n,i,j;
    cout<<"Enter the number of elements: ";
    cin>>n;
    vector<int> p(n);
    for(i=0;i<n;i++)
        p[i]=rand();
    vector<vector<int> > m(n-1,vector<int>(n-1,0));
    vector<vector<int> > s(n-1,vector<int>(n-1,0));
    clock_t start = clock();
    matrix_chain_order(p,m,s);
    double time=(double)(clock() - start)/CLOCKS_PER_SEC;
    cout<<"'M' table is "<<endl;
    for(i=0;i<n-2;i++)
    {
        for(j=1;j<n-1;j++)
            cout<<m[i][j]<<" ";
        cout<<endl;
    }
    cout<<"\n'S' table is "<<endl;
    for(i=0;i<n-2;i++)
    {
        for(j=0;j<n-1;j++)
            cout<<s[i][j]<<" ";
        cout<<endl;
    }
    
    cout<<"\nMinimum cost is "<<m[0][n-2]<<endl<<"\n";
    print_Optimal_Parens(s,1,n-1);
    cout<<"\nTime taken: "<<time<<endl;
}