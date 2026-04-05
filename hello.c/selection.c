#include<stdio.h>
int main() {
    int arr[10]={1,2,3,4,5,9,8,7,6,9};
    int i=0,j=0;
    int min,temp;
    for(i=0;i<10;i++){
       min=i;
       for(j=i+1;j<10;j++){
        if(arr[min]>arr[j]){
            min=j;
        }
        temp=arr[min];
        arr[min]=arr[j];
        arr[j]=temp;
       }
    }
    for(i=0;i<10;i++)
    printf("%d  ",arr[i]);
}