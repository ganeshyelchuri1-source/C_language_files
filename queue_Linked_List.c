#include<stdio.h>
#include<stdlib.h>
#define max 5
struct node {
    int data;
    struct node *next;
};
struct node *nn=NULL,*rear=NULL,*front=NULL;
int num;
void enqueue(){
    struct node *nn=NULL;
    nn=(struct node*)malloc(sizeof(struct node));
    printf("enter a number ");
    scanf("%d",&num);
    nn->data=num;
nn->next=NULL;
if(rear==NULL){
    front=rear=nn;
}
else{
    rear->next=nn;
    rear=rear->next;
}
printf("inserted sucessfully!");
}
void dequeue(){
    if(front==NULL){
        printf("you reached the bottom of the bucket");
    }
    else
    printf("%d removed sucessfully",front->data);
    struct node *temp=front;
    front=front->next;
    free(temp);
}
void peek(){
    printf("%d is near to the front",front->data);

}
void is_empty(){
    if(front==NULL){
        printf("is empty");
    }
    else{
        printf("it is not empty");
    }
}
void is_full(){
    if(rear==NULL){
        printf("overflow due to the memory problem");
    }
    if(rear==max-1){
        printf("size problem");
    }
}
void printing(){
    struct node *temp=front;
    while(temp!=NULL){
        printf("-%d-",temp->data);
        temp=temp->next;
    }
}
int main() {
    int choice;
    do{
        printf("1.enqueue\n 2.dequeue\n 3.peek\n 4.is-full\n 5.is- empty\n 6.printing\n7.exit\n");
        printf("enter your choice");
        scanf("%d",&choice);
        switch(choice){
            case 1: enqueue(); break;
            case 2: dequeue(); break;
            case 3: peek(); break;
            case 4: is_full(); break;
            case 5: is_empty(); break;
            case 6: printing(); break;
            case 7: printf("enter 7 to exit"); break;
            default: printf("please choose another one");
        }
    }while(choice !=7);
}