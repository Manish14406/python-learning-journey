#include<stdio.h>

typedef struct{
    int pid,Priority,wt,bt,tat;
}Process;

int main()
{
    int avgwt=0;
    int avgtat=0;
   int n;
    printf("enter no of process\n");
    scanf("%d",&n);

    Process p[n],temp;

    for( int i=0;i<n;i++)
    {
        p[i].pid=i+1;
        printf("Process : %d\n",i+1);
        printf("Enter bt\n");
        scanf("%d",&p[i].bt);
        printf("Enter priority\n");
        scanf("%d",&p[i].Priority);
    }

    for(int i =0;i<n-1;i++)
    {
        for(int j = i+1;j<n;j++)
        {
            if(p[i].Priority > p[j].Priority){
            temp = p[i];
            p[i] = p[j];
            p[j] = temp;
        }
    }
    }

    p[0].wt = 0;
    p[0].tat = p[0].bt;

    for(int i=1;i<n;i++)
    {
        p[i].wt = p[i-1].wt + p[i-1].bt;
        p[i].tat = p[i].wt + p[i].bt;
    }

   printf("\nPid\tpri\tbt\twt\ttat\n");

   for(int i =0;i<n;i++)
   {
    printf("P%d\t%d\t%d\t%d\t%d\n",p[i].pid,p[i].Priority,p[i].bt,p[i].wt,p[i].tat);
    avgwt+=p[i].wt;
    avgtat+=p[i].tat;
   }
   printf("\nAvg waiting time %f",avgwt/n);
   printf("\nAverage turn around time %f",avgtat/n);

   return 0;

}

#include<stdio.h.>
typedef struct 
{
    int pid,bt,wt,tat;
}Process;

int main()
{
    int avgwt=0,avgtat=0;
    int n;

    printf("Enter no of processe\n");
    scanf("%d",&n);
    Process p[n],temp;

    for(int i =0;i<n;i++){
        p[i].pid = i+1;
        printf("Process %d\n");
        printf("Enter Bt: ");
        scanf("%d",&p[i].bt);
    }
   
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(p[i].bt > p[j].bt)
            {
               temp = p[i];
               p[i]=p[j];
               p[j] = temp;
            }
        }
    }



    p[0].wt = 0;
    for(int i=1;i<n;i++)
    {
       p[i].wt = p[i-1].bt + p[i-1].wt;
    }

    for(int i =0;i<n;i++){
        p[i].tat = p[i].bt + p[i].wt;
    }

    printf("\nPid\tBT\tWt\tTat\n");

    for(int i=0;i<n;i++)
    {
        printf("P%d\t%d\t%d\t%d\n",p[i].pid,p[i].bt,p[i].wt,p[i].tat);
        avgwt +=p[i].wt;
        avgtat+=p[i].tat;
    }

    printf("\n avg-wt %d",avgwt/n);
    printf("\n avg-tat %d",avgtat/n);
    


return 0;


}