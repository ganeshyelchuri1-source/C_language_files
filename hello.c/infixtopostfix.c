#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define max 100
char stack[max];
int top=-1;
int i=0;
int j=0;
// char postfix[];
int preferance(char num){
    if (num=='*'||num=='%'||num=='/')
    return 3;
    else if(num=='+'||num=='-')
    return 2;
    else
    return 0;
}
char pop(){
    char name=stack[top];
    printf("%d",stack[top]);
    top--;
    return name;
}
void push(char element){
    top++;
    stack[top]=element;
}
int main() {
    char infix[1000];
    char postfix[1000];
printf("enter the infix expression");
scanf("%s",&infix);
for(i=0;i!='\0';i++){
    if(isalnum(infix[i])){
        postfix[j]=infix[i];j++;
    }
    else if(infix[i]=='(')
    push(infix[i]);
    else if(infix[i]==')'){
        while(stack[i]=='('){
            postfix[j]=pop();
            j+=1;
        }
        pop();
    }
    else(top!=-1 && preferance(stack[top])>=preferance(infix[i])){
        push(infix[i]);
    j++;
    }
    push(infix[i]);
}
printf(postfix);
}