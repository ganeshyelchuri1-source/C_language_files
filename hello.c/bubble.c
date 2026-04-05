#include<stdio.h>
int main() {
    int arr[10]={1,2,3,4,5,9,8,7,6,9};
    int i=0,j=0;
    int min,temp;
    for(i=0;i<10-1;i++){
       min=i;
       for(j=i;j<10-1;j++){
        if(arr[j]>arr[j+1]){
            temp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
        }
       }
    }
    for(i=0;i<10;i++)
    printf("%d  ",arr[i]);
}