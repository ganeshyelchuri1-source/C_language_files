#include<stdio.h>
#include<ctype.h>
#include<string.h>
#define max 9
int j=0,i=0,top=-1;
char infix[100],postfix[100],stack[max];
void push(char element){
    top++;
    stack[top]=element;
}
char pop(){
    char element=stack[top];
    top--;
    return element;
}
int precedence(char num){
    if(num=='^')
    return 3;
    else if(num=='*'||num=='/'|| num=='%')
    return 2;
    else if (num=='+'|| num=='-')
    return 1;
    else 
    return 0;
}
int main(){
    printf("enter the string");
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
        else{
            while(top!=-1 && precedence(stack[top])>=precedence(infix[i])){
                postfix[j]=pop();
                j++;
            }
            push(infix[i]);
        }
        i++;
    }
    while(top>-1){
        postfix[j]=pop();
        j++;
    }
    postfix[j]='\0';
    printf("%s",postfix);
}