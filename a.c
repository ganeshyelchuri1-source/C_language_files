// SINGLE LINKED list
#include<stdio.h>
#include<stdlib.h>
struct node {
int data;
struct node* next;
};
struct node* create_list(){
struct node *nn=NULL,*temp=NULL,*head=NULL;
int i=1;
    while(i==1){
    nn=(struct node*)malloc(sizeof(struct node));
    
    printf("enter a number to store");
scanf("%d",&nn->data);
nn->next=NULL;
if (head==NULL){
    head=temp=nn;
}
else
{temp->next=nn;
    temp=temp->next;
    
}
printf("enter 1 to continue and 0 t0 stop");
scanf("%d",&i);
}
return head;
}
int counting(struct node* head){
   struct node* temp=head;
   int count=0;
   if (temp==NULL){
    printf("no elements are present in the list");
   }
   while(temp!=NULL){
    count++;

    temp=temp->next;
}

return count;}
void display(struct node* head){
   struct node* temp=head;
   if (temp==NULL){
    printf("no elements are present in the list");
   }
   while(temp!=NULL){
    printf("%d->",temp->data);
    temp=temp->next;
}
printf("NULL");
}
struct node* insert_at_first(struct node* head){
    struct node* temp=head;
    temp=(struct node*)malloc(sizeof(struct node));
    printf("enter a value");
    scanf("%d",&temp->data);
    temp->next=head;
    head=temp;
return head;
}
struct node* delete_at_first(struct node *head){

struct node *temp=NULL;
temp=head;
head=head->next;
free(temp);
return head;}
void insert_at_last(struct node *head){
   struct node *temp=head;
struct node *nn=(struct node*)malloc(sizeof(struct node));
printf("enter a value to insert at last");
scanf("%d",&nn->data);
nn->next=NULL;
while(temp->next!=NULL){
    temp=temp->next;
}
temp->next=nn;
}
void delete_at_last(struct node *head){
    struct node* temp=head,*prev=NULL;
    while(temp->next!=NULL){
        prev=temp;// to print 1
        // /at first we should present at temp 
        //while to add any thing at last we should present at temp next
        // and while changing at first at head store head adress because head value gets changed
    temp=temp->next;
    }
    prev->next=NULL;
    free(temp);

}
void insert_at_position(struct node* head){
    struct node* temp=head;
int p,num;

printf("enter a element to add at specific position");
scanf("%d",&p);
struct node* nn=(struct node*)malloc(sizeof(struct node));
printf("enter a number to add");
scanf("%d",&nn->data);
for(int i=1;i<p-1;i++){
    temp=temp->next;
}
nn->next= temp->next;
temp->next=nn;

}
void remove_at_position(struct node* head){
    struct node* temp=head,*nn=NULL;
int p;
    printf("enter a place value to remove ");
    scanf("%d",&p);
    for(int i=1;i<p;i++){
        nn=temp;
        temp=temp->next;
    }


nn->next=temp->next;

    free(nn);
}
struct node* reversell(struct node *head){
struct node *temp=head,*c=head,*n=NULL,*p=NULL;
while(temp!=NULL){
    n=c->next;
    c->next=p;
    p=c;
    c=n;

}
return p;
}

int main() {
struct node* head=create_list();

printf("count=%d",counting(head));
display(head);
head=insert_at_first(head);
display(head);
head=delete_at_first(head);
display(head);
insert_at_last(head);
display(head);
delete_at_last(head);
display(head);
insert_at_position(head);
display(head);
remove_at_position(head);
display(head);
head=reversell(head);
display(head);
}
// DOUBLE LINKED LIST

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
void backward_display(struct node *head){
    struct node *temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    while(temp!=head){
        printf("%d ",temp->data);
        temp=temp->prev;
    }
    printf("%d",temp->data);
}
int main() {
struct node *head=createdoublelinkedlist();
display(head);
head=addatfirst(head);
display(head);
head=removeatfirst(head);
display(head);
removeatlast(head);
display(head);
addatlast(head);
display(head);
insertatposition(head);
display(head);
removeatposition(head);
display(head);
head=reverse(head);
display(head);
backward_display(head);

}