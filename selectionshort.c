#include<stdio.h>
int main() {
    int i=0,j=0,n;
    printf("enter a size of the array");
    scanf("%d",&n);
    int arr[n];
    int min=0,temp=0;
    printf("start enterint your elements");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        min=i;
        for(j=i;j<n;j++){
            if(arr[min]>arr[j]){
                min=j;
            }
        }
        temp=arr[min];
        arr[min]=arr[i];
        arr[i]=temp;
    }
    for(i=0;i<n;i++)
    printf("%d  ",arr[i]);
}