
#include<stdio.h>
#include<stdlib.h>
struct node {
    
    int data;
    struct node *prev;
    struct node *next;
};
struct node* createdoublelinkedlist(){
    struct node *head=NULL,*temp=NULL,*nn=NULL;
    int i=1;
    while(i==1){
        nn=(struct node*)malloc(sizeof(struct node));
    printf("enter a number");
    scanf("%d",&nn->data);
    nn->next=NULL;
    if(head==NULL){
        nn->prev=NULL;
        head=temp=nn;
    }
    else{
        temp->next=nn;
        nn->prev=temp;
        temp=temp->next;
    }
    printf("enter 1 to continue and 0 to stop");
    scanf("%d",&i);
}
return head;
}
void display(struct node *head){
    struct node *temp=head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("null");
}
struct node* addatfirst(struct node *head){
struct node* temp=head,*nn=NULL;
nn=(struct node*)malloc(sizeof(struct node));
printf("enter a num to add at first");
scanf("%d",&nn->data);
nn->prev=NULL;
nn->next=temp;
temp=nn;
return temp;
}
struct node* removeatfirst(struct node *head){
    struct node *temp=head,*nn=NULL;
    head=head->next;
    free(temp);
    return head;
}
void removeatlast(struct node *head){
    struct node *temp=head;
while(temp->next!=NULL){
  
    temp=temp->next;
    }
    
    temp->prev->next=NULL;
    free(temp);
}
void addatlast(struct node *head){
    struct node *temp=head,*nn=NULL;
    nn=(struct node*)malloc(sizeof(struct node));
    printf("enter a element to add at last");
    scanf("%d",&nn->data);
    nn->next=NULL;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=nn;
    nn->prev=temp->next;
}
void insertatposition(struct node *head){
    struct node *temp=head,*nn;
    int p;
    printf("enter a element  position");
    scanf("%d",&p);
    for(int i=1;i<p-1;i++){
        temp=temp->next;
    }
    nn=(struct node*)malloc(sizeof(struct node));
    printf("enter a element");
    scanf("%d",&nn->data);
    nn->prev=temp;
   
nn->next=temp->next;
 temp->next=nn;
}
void removeatposition(struct node *head){
    struct node *temp=head;
    int p;
    printf("enter a position");
    scanf("%d",&p);
    for(int i=1;i<p;i++){
        temp=temp->next;
    }
     temp->next->prev=temp->prev;
    temp->prev->next=temp->next;
    free(temp);
}
struct node* reverse(struct node *head){
    struct node *temp=head,*c=NULL;
    
    while(temp!=NULL){
        c=temp->prev;
        temp->prev=temp->next;
        temp->next=c;
      temp=temp->prev;
    }
    head=c->prev;
    return head;
}

int main() {
struct node *head=createdoublelinkedlist();
// display(head);
// head=addatfirst(head);
// display(head);
// head=removeatfirst(head);
// display(head);
// removeatlast(head);
// display(head);
// addatlast(head);
// display(head);
// insertatposition(head);
// display(head);
// removeatposition(head);
// display(head);
head=reverse(head);
display(head);
}