#include<stdio.h>
#include<stdlib.h>
#define max 5
int stack[max];
int top=-1;
int i=0;
void push(){
    if(top==max-1){
        printf("stack overflow");
    }
    else{
    int element;
    printf("enter a value to store");
    scanf("%d",&element);
    top++;
    stack[top]=element;
    }
}
void pop() {
    if(top==-1){
        printf("stack underflow");
    }
    else{
        printf("%d removed sucessfully",stack[top]); 
        top--;
    }
}
void peek(){
    printf("%d removed sucessfully",stack[top]);
}
void is_empty() {
    if (top==-1){
        printf("stack is empty");
    }
    else{
        printf("stack is not empty");
    }
}
void is_full() {
    if(top==max-1){
        printf("stack is full");
    }
    else{
        printf("stack is not full");
    }
}
void count(){
    int count=0;
    for(i=top;i>-1;i--){
        count++;
    }
    printf("%d",count);
}
void printing_elements(){
    for(i=top;i>-1;i--){
        printf("%d",stack[top]);
    }
}
void is_present(){
    int key;
    printf("enter a number to find");
    scanf("%d",&key);
    for(i=top;i>-1;i--){
        if(key==stack[top]){
            printf("element is present");

        }
        else{
            continue;
        }
    }
}
int main() {
    int choice;
    do{
        printf("1.push\n2.pop\n 3.peek\n 4.is empty\n 5.is full\n 6.count\n 7.print elements \n 8.is_present");
            printf("enter a choice");
    scanf("%d",&choice);
    switch(choice){
            case 1:
            push();
            break;
            case 2:
            pop();
            break;
            case 3:
            peek();
            break;
            case 4:
            is_empty();
            break;
            case 5:
            is_full();
            break;
            case 6:
            count();
            break;
            case 7:
            printing_elements();
            break;
            case 8:
            is_present();
            break;
            case 9:
            return 1;
            default :
            printf("print another");
    printf("enter a choice");
    scanf("%d",&choice);
        }

    }while(choice!=8);
}