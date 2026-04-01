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
        for(j=0;j<n;j++){
            if(arr[j]>arr[j+1]){
                min=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=min;
            }
        }
    }
    printf("the ascending order of the entered array is:-");
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}
// #include<stdio.h>
// int main() {
//     int min=0;
//     int arr[]={1,22333,3555,40,5};
//     int j=0,i=0;
//     for(i=0;i<5;i++){
//         min=i;
//         for(j=0;j<5-i;j++){
//             if(arr[j]>arr[j+1]){
//                 min=arr[j];
//                 arr[j]=arr[j+1];
//                 arr[j+1]=min;
//             }
//         }
//     }
//     for(i=0;i<5;i++){
//         printf("%d ",arr[i]);
//     }
    
// }