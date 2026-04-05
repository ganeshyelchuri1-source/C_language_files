#include<stdio.h>
#include<ctype.h>
#define max 100
char infix[100];
char postfix[100];
int i=0,j=0;
int top=-1;
char stack[max];
void push(char element){
    if(top==max-1){
        printf("there is no space");
    }
    else{
    top++;
    stack[top]=element;}
    
}
char pop(){
    if(top==-1){
        printf("there is no space");
    }
    else{
    char element=stack[top];
    top--;
    return element;}
}
int precedence( char element){
    if(element=='^'){
        return 3;
    }
    else if(element=='+' || element=='-'){
        return 1;
    }
    else if(element=='*' || element=='/'|| element=='%')
    return 2;
else{
    return 0;
}
}
int main() {
    printf("enter a expression");
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
                    postfix[j]==pop();
                    j++;
                }
                pop();
            }
        
        else {
            if(top!=-1 && precedence(stack[top])>=precedence(infix[i])){
                postfix[j]=pop();
                j++;
            }
            else{
                push(infix[i]);
            }
        }
        i++;

    }
    while(top!=-1){
        postfix[j]=pop();
        j++;
    }
    postfix[j]='\0';
    printf("%s",postfix);
}