#include<iostream>
#include<vector>
#include<ctime>
using namespace std;
int main()
{
    vector<int> elements;
    int key,i,j,n,ele,sea;
    int count=0;
    cout<<"Enter number of elements: ";
    cin>>n;
    cout<<"Enter the element to be found: ";
    cin>>sea;
    for(i=0;i<n;i++)
	{
	cin>>ele;
	elements.push_back(ele);
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
    for(i=0;i<n;i++){
    	if(elements[i]==sea){
    		break;
    	}
    	else{
    		count+=1;
    	}
    }
double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for Ascending Order: "<<time1<<endl;
	cout<<"Index of the given element is: "<<count<<endl;
	for(i=0;i<n;i++){
		cout<<elements[i]<<" ";
	}
}
