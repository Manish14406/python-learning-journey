#include<stdio.h>
#include<stdlib.h>
#define MAX 20

void create(int arr[], int *n)
{
    printf("Enter the size of the array\n");
    scanf("%d",n);
    printf("Enter the elements into the array\n");
    for(int i = 0;i<*n;i++)
    {
        scanf("%d",&arr[i]);
    }


}
void insert(int arr[], int *n)
{
     int value,pos;
     printf("Enter the position to be inserted: \n");
     scanf("%d",&pos);
     printf("Enter the value to be inserted: \n");
     scanf("%d",&value);

     for(int i = *n+1;i>=pos;i--)
     {
        arr[i] = arr[i-1];
     }
     arr[pos] = value;
     (*n)++;
}
void display(int arr[], int n)
{
    printf("Displaying the array elements\n");
    for( int i = 0;i<n;i++)
    {
        printf("%d\n",arr[i]);
    }
}

int main()
{
    int n,arr[MAX];
    int choice;
    while(1){
        printf("1:Create\n2:Insert\n3:Display\n4:exit\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
               create(arr,&n);
                 break;
            case 2:
               insert(arr,&n);
            case 3:
               display(arr,n);
            case 4:
               exit(0);

        }
    }
    return 0;
}
// void deleteElement(int arr[], int *n)
