#include<iostream>
using namespace std;
#include<vector>
#include <ctime> 
#include<limits.h>
#include<math.h>
#include<time.h>
void mergesenti(vector<int> &elements, int left, int mid, int right)
{
	vector<int> left_Sub_Array, right_Sub_Array;
	int no_Left_Sub,no_Right_Sub,i,index_Left_SA,index_Right_SA,index_Full_Array;
	// Find number of elements in left subarray
	no_Left_Sub = mid-left+1;
	// Find number of elements in right subarray
	no_Right_Sub = right-mid;
	//make a copy of left sub array in a temporary array
	for(i=0;i<no_Left_Sub;i++)
		left_Sub_Array.push_back(elements[left+i]);
	left_Sub_Array.push_back(INT_MAX);
	//make a copy of right sub array into another temporary array
	for(i=0;i<no_Right_Sub;i++)
		right_Sub_Array.push_back(elements[mid+i+1]);
	right_Sub_Array.push_back(INT_MAX);
	// Position the indices for the three arrays rightly
	index_Left_SA=0;
	index_Right_SA=0;
	
	// When there are elements to be comapred in both the arrays
	for(index_Full_Array=left;index_Full_Array<=right;index_Full_Array++)
	{
		// if element in left sub array is less than element in right sub array
		if(left_Sub_Array[index_Left_SA] < right_Sub_Array[index_Right_SA])
		{
			// copy the element from left sub array into orginal array and increment indices
			elements[index_Full_Array] = left_Sub_Array[index_Left_SA];
			index_Left_SA++;
		}
		//otherwise
		else
		{
			// copy the element from right sub array into orginal array and increment indices
			elements[index_Full_Array] = right_Sub_Array[index_Right_SA];
			index_Right_SA++;
		}
	}
}

void mergesortsenti(vector<int> &elements, int left, int right)
{
	int mid;
	// When there is only one element in the array
	if(left==right)
		return;
	// Find mid of the array
	mid = (left+right)/2;
	// call mergesort for left subarray
	mergesortsenti(elements,left,mid);
	// call mergesort for right subarray
	mergesortsenti(elements,mid+1,right);
	// merge the sorted left and right subarray
	mergesenti(elements,left,mid,right);
}

void mergenosenti(vector<int> &elements, int left , int mid , int right)
{
	int i,j,k;
	int n1 = mid - left + 1;
	int n2 = right - mid;
	
	vector<int> left_array, right_array;

	for (i = 0; i < n1; ++i)
		left_array.push_back(elements[left + i]); //copy from index_low to index_mid

	for (j = 0; j < n2; ++j)
		right_array.push_back(elements[mid + 1 + j ]);  //copy from index_mid+1 to index_high
			

	for(k = left , i=j=0; k <= right; ++k )
	{
		if(i == n1)
			elements.push_back(right_array[j++]);
		
		else if(j == n2)
			elements.push_back(left_array[i++]);

		else if(left_array[i] <= right_array[j])
			elements.push_back(left_array[i++]);

		else elements.push_back(right_array[j++]);
	}


}

void mergesortnosenti(vector<int> &elements , int left, int right)
{
	int mid;

	if(left < right)
	{
		mid=(right + left) / 2 ;
		
		mergesortnosenti(elements , left , mid);
		mergesortnosenti(elements , mid + 1 , right);
		mergenosenti(elements , left , mid , right);
	}
}

void averagecasesenti(int n)
{
	vector<int> elements;
	for(int i=0;i<n;i++)
	{
		elements.push_back(rand());
	}
	clock_t tStart = clock();
	mergesortsenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for average case with sentinels is: "<<time1<<endl;
}

void bestcasesenti(int n)
{
	vector<int> elements;
	for(int i=0;i<n;i++)
	{
		elements.push_back(i);
	}
	clock_t tStart = clock();
	mergesortsenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for best case with sentinels is: "<<time1<<endl;
}

void worstcasesenti(int n)
{	
	vector<int> elements;
	for(int i=n;i>0;i--)
	{
		elements.push_back(i);
	}
	clock_t tStart = clock();
	mergesortsenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for worst case with sentinels is: "<<time1<<endl;
}

void averagecasenosenti(int n)
{
	vector<int> elements;
	for(int i=0;i<n;i++)
	{
		elements.push_back(rand());
	}
	clock_t tStart = clock();
	mergesortnosenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for average case with no sentinels is: "<<time1<<endl;
}

void bestcasenosenti(int n)
{
	vector<int> elements;
	for(int i=0;i<n;i++)
	{
		elements.push_back(i);
	}
	clock_t tStart = clock();
	mergesortnosenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for best case with no sentinels is: "<<time1<<endl;
}

void worstcasenosenti(int n)
{	
	vector<int> elements;
	for(int i=n;i>0;i--)
	{
		elements.push_back(i);
	}
	clock_t tStart = clock();
	mergesortnosenti(elements, 0, n-1);
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout<<"Time taken for worst case with no sentinels is: "<<time1<<endl;
}
int main()
{
	srand(time(0));
	int n;
	cout<<"Enter the Number of elements: ";
	cin>>n;
	printf("\nWith Sentinels:-\n");
	averagecasesenti(n);
	bestcasesenti(n);
	worstcasesenti(n);
	printf("\n");
	printf("With no Sentinels:-\n");
	averagecasenosenti(n);
	bestcasenosenti(n);
	worstcasenosenti(n);
}