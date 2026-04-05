#include<stdio.h>
int main() {
    int i=0,j=0;
    int n,min=0,temp;
    printf("enter a number");
    scanf("%d",&n);
    int arr[n];
    printf("start entering your  details");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        printf("%d",arr[i]);
    }
    for(i=0;i<n;i++){
        min=arr[i];
        for(j=0;j<n;j++){
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }

}