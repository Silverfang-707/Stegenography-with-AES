#include<iostream>
using namespace std;
#include<random>
#include<ctime>
#include<string.h>
#include<limits.h>
#include<vector>

void lcs_length(string x, string y, vector<vector<int> >&c, vector<vector<char> > &b)
{
    int m,n,i,j;
    m = x.length();
    n = y.length();
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(x[i-1]==y[j-1])
            {
                c[i][j] = c[i-1][j-1] + 1;
                b[i][j] = 'd';
            }
            else if(c[i-1][j]>=c[i][j-1])
            {
                c[i][j] = c[i-1][j];
                b[i][j] = 'u';
            }
            else
            {
                c[i][j] = c[i][j-1];
                b[i][j] = 'd';
            }
        }
    }
}

void print_LCS(vector<vector<char> > &b, string x,int i, int j)
{
    if((i==0)||(j==0))
        return ;
    if(b[i][j]=='d')
    {
        print_LCS(b,x,i-1,j-1);
        cout<<x[i-1];
    }
    else if(b[i][j]=='u')
    {
        print_LCS(b,x,i-1,j);
    }
    else
        print_LCS(b,x,i,j-1);
}

string randomString(int length){
	const string CHARS = "abcdefghijklmnopqrstuvwxyz";
	random_device random_device;
	mt19937 generator(random_device());
	uniform_int_distribution<> distribution(0, CHARS.size() - 1);
	string random_string;
	for(int i = 0; i<length; i++){
		random_string += CHARS[distribution(generator)];
	}
	return random_string;
}

int main()
{
    string x,y;
    int xlen,ylen,i,j;
    cout<<"Enter the length of first string: ";
    cin>>xlen;
    cout<<"Enter the length of second String: ";
    cin>>ylen;
    x=randomString(xlen);
    y=randomString(ylen);
    cout<<"\nGenerated First String: "<<x<<endl;
    cout<<"Generated Second String: "<<y<<endl<<endl;
    vector<vector<int> > c(x.length()+1,vector<int>(y.length()+1,0));
    vector<vector<char> > b(x.length()+1,vector<char>(y.length()+1,' '));
    clock_t tStart = clock();
    lcs_length(x,y,c,b);
    double time=(double)(clock() - tStart)/CLOCKS_PER_SEC;
    for(i=0;i<x.length()+1;i++)
    {
        for(j=0;j<y.length()+1;j++)
            cout<<c[i][j]<<" ";
        cout<<endl;
    }
    for(i=0;i<x.length()+1;i++)
    {
        for(j=0;j<y.length()+1;j++)
            cout<<b[i][j]<<" ";
        cout<<endl;
    }
    cout<<"\nLCS: ";
    print_LCS(b,x,x.length(),y.length()-1);
    cout<<"\nTime taken: "<<time<<endl;
}
