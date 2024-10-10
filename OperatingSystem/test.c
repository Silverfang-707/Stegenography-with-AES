#include <stdio.h>
void findwaitingtime(int processes[], int n, int bt[], int wt[]){
    wt[0]=0;
    for(int i=0; i<n; i++){
        wt[i]=bt[i-1] + wt[i-1];
    }
}

void findturnaroundtime(int processes[], int n, int bt[], int wt[], int tat[]){
    for (int i=0; i<n; i++){
        tat[i]=bt[i] + wt[i];
    }
}

void findavgtime(int processes[], int n, int bt[]){
    int wt[10], tat[10], total_wt=0, total_tat=0;
    findwaitingtime(processes, n, bt, wt);
    findturnaroundtime(processes, n, bt, wt, tat);
    printf("Processes   Bursttime   Waitingtime turnaroundtime");
    for(int i=0;i<n;i++){
        total_wt+=wt[i];
        total_tat+=tat[i];
        printf("    %d",(i+1));
        printf("        %d",bt[i]);
        printf("        %d",wt[i]);
        printf("        %d\n",tat[i]);
    }
    int s=(float)total_wt/(float)n;
    int t=(float)total_tat/(float)n;
    printf("Average waiting time = %d",s);
    printf("\n");
    printf("Average turn around time = %d",t);
}

int main(){
    int n,temp;
    int processes[n],burst_time[10];
    printf("Enter the number of processes");
    scanf("%d",&n);
    for(int i=1; i<n; i++){
        processes[i-1]=i;
    }
    for(int i=0; i<n; i++){
        scanf("Enter the burst time: %d",&temp);
        burst_time[i]=temp;
    }
    findavgtime(processes,n,burst_time);
    return 0;
}