#include<stdio.h>
#define max 5
int arr[max];
int j=0,i=0,temp,front=0,rear=-1;
    void enqueue(){
        int element;
        if(front ==-1 && rear==-1){
            front++;

        }
        rear++;
        printf("enter a number");
        scanf("%d",&element);
        arr[rear]=element;
    }
    void dequeue(){
        if(front==-1 || front>rear){
            printf("it is not possible");
        }

        printf("%d removed sucessfully!",arr[front]);
        front++;
    }
    void peek(){
        printf("%d is there at rear position",arr[front]);
    }
    void is_empty(){
        if(rear==-1 && front==-1 || front>rear){
            printf("  queue is empty");
        }
        else{
            printf("queue is not empty");
        }
    }
    void is_full(){
        if(rear==max-1){
            printf("queue is full");
        }
        else{
            printf("it is not full");
        }
    }
    void printing(){

        int index=0;

        for(index=front;index<=rear;index++){
            printf("%d ",arr[index]);
        }}
            
     int main() {   
int choice;

do{
    printf("1.enqueue\n 2.dequeue \n 3.peek \n 4.is empty\n 5.is full\n 6.printing \n 7.exit\n");
    printf("enter a choice");
        scanf("%d",&choice);
        switch(choice){
        
        case 1:
        enqueue();break;
        case 2:
        dequeue();break;
        case 3:
        peek();break;
        case 4:
        is_empty();break;
        case 5:
        is_full();break;
        case 6:
        printing();break;
        case 7:
        printf("exiting");
        default:
        printf("enter another one ");
    }
}while(choice!=7);


}