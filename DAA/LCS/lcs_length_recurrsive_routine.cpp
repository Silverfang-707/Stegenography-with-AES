#include<iostream>
using namespace std;
#include<limits.h>
#include<string.h>
#include<vector>
#include<random>
#include<ctime>

int lcs_length(string x, string y, int x_index,int y_index)
{
    
    	int m,n,i,j,l1,l2;
    	m = x.length();
    	n = y.length();
    	if((x_index>=m)||(y_index>=n))
        	return 0;
    	if(x[x_index]==y[y_index])
    	{        
        	return lcs_length(x,y,x_index+1,y_index+1)+1;
    	}
    	else
    	{
        	l1 = lcs_length(x,y,x_index,y_index+1);
        	l2 = lcs_length(x,y,x_index+1,y_index);
        	return l1>l2? l1: l2;

    	}
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
	int xlen,ylen;
	cout<<"Enter the length of first string: ";
	cin>>xlen;
	cout<<"Enter the length of second String: ";
	cin>>ylen;
	string x,y;
	x=randomString(xlen);
	y=randomString(ylen);
	cout<<"\nGenerated First String: "<<x<<endl;
	cout<<"Generated Second String: "<<y<<endl;
	clock_t tStart = clock();
	cout<<"\nLCS Length: "<<lcs_length(x,y,0,0);
	double time=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"\nTime taken: "<<time<<endl; 
}
