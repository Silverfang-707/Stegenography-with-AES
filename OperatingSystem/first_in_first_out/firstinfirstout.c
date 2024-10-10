#include <stdio.h>

int firstinfirstout(int frames)  
{   
    int incomingStream[frames];
    for(int i=0;i<frames;i++){
	printf("Enter the Reference string one by one: ");
	scanf("%d",&incomingStream[i]);
    }	
    int pageFaults = 0;  
    int m, n, s, pages;   
    pages = sizeof(incomingStream)/sizeof(incomingStream[0]);   
    printf(" Incoming \t Frame 1 \t Frame 2 \t Frame 3 ");  
    int temp[ frames ];  
    for(m = 0; m < frames; m++)  
    {  
        temp[m] = -1;  
    }  
    for(m = 0; m < pages; m++)  
    {  
        s = 0;   
        for(n = 0; n < frames; n++)  
        {  
            if(incomingStream[m] == temp[n])  
            {  
                s++;  
                pageFaults--;  
            }  
        }  
        pageFaults++;  
        if((pageFaults <= frames) && (s == 0))  
        {  
            temp[m] = incomingStream[m];  
        }  
        else if(s == 0)  
        {  
            temp[(pageFaults - 1) % frames] = incomingStream[m];  
        }  
        printf("\n");  
        printf("%d\t\t\t",incomingStream[m]);  
        for(n = 0; n < frames; n++)  
        {  
            if(temp[n] != -1)  
                printf(" %d\t\t\t", temp[n]);  
            else  
                printf(" - \t\t\t");  
        }  
    }  
    printf("\nTotal Page Faults:\t%d\n", pageFaults);  
    return 0;  
}

int main(){
	int frame;
	printf("Enter the number of frames: ");
	scanf("%d",&frame);
	firstinfirstout(frame);
}
