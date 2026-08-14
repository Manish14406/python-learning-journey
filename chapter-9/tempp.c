#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define MAX 20

void create(int arr[], int *n)
{
    printf("Enter the number of elements to enter\n");
    scanf("%d",n);
    printf("Enter the array elements\n");
    for(int i=0;i<*n;i++)
    {
        scanf("%d",&arr[i]);

    }

}
void insert(int arr[], int *n)
{
    int pos,value;
    printf("Insertion\n");
    printf("Enter position to be inserted\n");
    scanf("%d",&pos);
    printf("Enter the value to be inserted\n");
    scanf("%d",&value);

    for(int i = *n-1;i>=pos;i--)
    {
        arr[i+1]=arr[i];
    }
    arr[pos] = value;
}

void display(int arr[], int n)
{
    printf("The array elements are\n");
    for(int i =0;i<n;i++){
        printf("%d\n",arr[i]);
    }
}
int main()
{
    int n;
 int arr[MAX];
 while(1)
 {
    printf("Create:1\nInsert:2\nDisplay:3\nExit:4\n");
    int choice;
    printf("Enter your choice\n");
    scanf("%d",&choice);
    switch(choice)
    {
        case 1:
        create(arr,&n);
        break;
        case 2:
        insert(arr,&n);
        break;
        case 3:
        display(arr,n);
        break;
        case 4:
        exit(0);
        
    }
 }
 return 0;
}

void deleteElement(int arr[], int *n);
