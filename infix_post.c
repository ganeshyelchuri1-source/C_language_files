#include<stdio.h>
#include<ctype.h>
#define max 30
int i=0,j=0;
char stack[max];
int top=-1;
char infix[100];
char postfix[100];
void push(char element){

        top++;
        stack[top]=element;

    }
char pop() {
    char element=stack[top];
    top--;
    return element;
}
int precedence(char element){
    if (element=='^')
    return 3;
    else if (element=='*'|| element=='/'||element=='%')
    return 2;
    else if(element=='+'|| element=='-')
    return 1;
    else
    return 0;
}
int main(){
    printf("enter infix expression");
    scanf("%s",infix);
    while(infix[i]!='\0'){
        if(isalnum(infix[i])){
            postfix[j]=infix[i];
            j++;
        }
        else if(infix[i]=='('){
            push(infix[i]);
        }
        else if(infix[i]==')'){
            while(stack[top]!='('){
                postfix[j]=pop();
                j++;
            }
            pop();
        }
        else {
            while(top!=-1 && precedence(stack[top])>=precedence(infix[i])){
        postfix[j]=pop();
        j++;
            }
            push(infix[i]);
            
        }

        
    }
    while(top!=-1){
            postfix[j]=pop();
            j++;
        }
    postfix[j]='\0';
    printf("%s",postfix);
}
