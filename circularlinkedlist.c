#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
};
struct node* createlist(){
    
    struct node *temp=NULL,*nn=NULL,*head=NULL;
    int i=1;
    while(i==1){
    nn=(struct node*)malloc(sizeof(struct node));
    printf("enter the data");
    scanf("%d",&nn->data);
    nn->next=head;
    if(head==NULL){
    temp=head=nn;
    }
    else{
    temp->next=nn;
    temp=temp->next;
    }
    printf("enter 1 to continue and 0 to stop");
    scanf("%d",&i);}
    // nn->next=head;}
    return head;
}
void display(struct node *head){
    struct node *temp=head;
    printf("%d,",temp->data);
    temp=temp->next;
    while(temp!=head){
    printf("%d,",temp->data);
    temp=temp->next;
    }
    
}
int count_of_elements(struct node *head){
    struct node *temp=head;
    int count=1;
    temp=temp->next;
    while(temp!=head){
        count++;
    temp=temp->next;
    }
    return count;
}
struct node* insert_at_first(struct node *head){
    struct node *temp=head;
   struct node *nn=(struct node*)malloc(sizeof(struct node));
    printf("enter a value");
    scanf("%d",&nn->data);
    nn->next=temp;
    while(temp->next!=head){
        temp=temp->next;
    }
   temp->next=nn;
   head=nn;   
return head;
}

struct node* delete_at_first(struct node *head){

struct node *temp=head,*c=head,*prev=NULL;
temp=temp->next;
    while(temp->next!=head){
        prev=temp;
        temp=temp->next;
    }
   prev->next=head;
   free(temp);
  
// free(c);
return head;
}
void insert_at_position(struct node *head){
    struct node *temp=head;
    int p;
    printf("enter position value");
    scanf("%d",&p);
    for(int i=1;i<p-1;i++){
        temp=temp->next;
    }
    struct node *nn=(struct node*)malloc(sizeof(struct node));
    printf("enter the data");
    scanf("%d",&nn->data);
    nn->next=temp->next;
    temp->next=nn;
}
void delete_at_position(struct node *head){
    struct node *temp=head,*prev=NULL;
    int p;
    printf("enter the position data");
    scanf("%d",&p);
    for(int i=1;i<p;i++){
        prev=temp;
        temp=temp->next;
    }
    prev->next=temp->next;
    free(temp);

}
void insert_at_last(struct node *head){
    struct node *temp=head;
    temp=temp->next;
    while(temp->next!=head){
        temp=temp->next;
    }
    struct node *nn=(struct node*)malloc(sizeof(struct node));
    printf("enter the data to add at last");
    scanf("%d",&nn->data);
    temp->next=nn;
    nn->next=head;
}
void remove_at_last(struct node *head){
    struct node *temp=head,*prev=NULL;
    temp=temp->next;
    while(temp->next!=head){
        prev=temp;
        temp=temp->next;
    }
prev->next=head;
free(temp);

}
// struct node* reverse_the_ll(struct node *head){
//     struct node *temp=head,*dup=NULL,*n=NULL,*p=NULL;
//     dup=temp;
//     temp=temp->next;
//     temp->next=dup;
//     while(temp->next!=head){
//     n=temp->next;
//     temp->next=p;
//     p=temp;
//     temp=n;
//     }
//     head=p;
// return temp;
// }
int search_operaration(struct node *head){
    struct node *temp=head;
    int num,count=0;
    printf("enter a number a find");
    scanf("%d",&num);
    if(temp->data==num){
        count=1;
        exit(1);
    }
    else {
        temp=temp->next;
        while(temp->next!=head){
        if(temp->data==num)  {
            count=1;
            break;
        }    
        temp=temp->next;      
        }
    }
    return count;
}
int main() {
struct node *head=createlist();
display(head);
// head=insert_at_first(head);
// display(head);
// printf("\n");
// head=delete_at_first(head);
// display(head);
// insert_at_position(head);
// display(head);
// delete_at_position(head);
// display(head);
// insert_at_last(head);
// display(head);
// printf("\n");
// remove_at_last(head);
// display(head);
// printf("\n");
// head=reverse_the_ll(head);
// display(head);
int elements=count_of_elements(head);
printf("no.of elements are:%d",elements);

int count=search_operaration(head);
if(count==1){
    printf("element is founded in the linked list");
}
else
    printf("element is not there in the linked list");
}