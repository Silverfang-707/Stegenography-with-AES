#include<bits/stdc++.h>
using namespace std;
int n;
int p[1000];
int m[1000][1000];
int s[1000][1000];
void print(int i,int j)
{
    if(i==j)
    {
        cout<<"A"<<i;
        return;
    }
    cout<<"(";
    print(i,s[i][j]);
    cout<<")";
    cout<<"(";
    print(s[i][j]+1,j);
    cout<<")";
}
void matrixChainOrder()
{
    for(int i=1;i<=n;i++)
        m[i][i]=0;
    for(int l=2;l<=n;l++)
    {
        for(int i=1;i<=n-l+1;i++)
        {
            int j=i+l-1;
            m[i][j]=INT_MIN;
            for(int k=i;k<j;k++)
            {
                int q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j];
                if(q>m[i][j])
                {
                    m[i][j]=q;
                    s[i][j]=k;
                }
            }
        }
    }
}
int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>p[i];
    matrixChainOrder();
    for(int i=1;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
            cout<<m[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    for(int i=1;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
            cout<<s[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    cout<<"Maximum cost is"<<endl<<m[1][n-1]<<endl<<endl;
    cout<<"Parenthesization of matrices is"<<endl;
    print(1,n-1);
}
