#include<stdio.h>
#include<stdlib.h>
struct node {
    int data;
    struct node *next;
};
struct node *top=NULL;
void push() {
    struct node *nn=(struct node*)malloc(sizeof(struct node));
    int n;
    printf("enter a number");
    scanf("%d",&n);
    nn->data=n;
    nn->next=top;
    top=nn;
}
void pop(){
    struct node *temp=top;
    printf("%d deleted sucessfully",top->data);

    top=top->next;
    free(temp);
}
void peek() {
    printf("%d is there at last",top->data);
}
void printing(){
    while(top!=NULL){
        printf("%d-> ",top->data);
        top=top->next;
    }}
void counting(){
    struct node *temp=top;
    int count=0;
    while(temp!=NULL){
        count++;
    
    temp=temp->next;}
    printf("%d are there",count);
}
void pre_abs(){
    int key;
    struct node *temp=top;
    printf("Enter a number");
    scanf("%d",&key);
    while(temp!=NULL){
        if(temp->data==key){
            printf("element is there");
            return;
        }
        temp=temp->next;
    }
}
int main() {
    int choice=0;
    do{
    printf("1.push\n 2.pop \n3.peek\n4.printing\n 5.counting \n6.pre_abs\n 7.to exit");
    printf("enter your selection");
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
        printing();
        break;
        case 5:
        counting();
        break;
        case 6:
        pre_abs();
        break;
        case 7:
        printf("exiting");
        return 1;
        default:
        printf("invalid ");
    }

    }while(choice!=7);

}