#include<stdio.h>
#include<ctype.h>
#define max 100
int j=0,i=0,top=-1;
char stack[max];
char postfix[1000],infix[1000];
void push(char element){
    top++;
    stack[top]=element; 
}
char pop(){
    char element;
    element=stack[top];
    top--;
    return element;
}
int precedence(char element){
    if(element=='^'){
        return 3;
    }
    else if(element=='*'|| element=='%'|| element=='/'){
        return 2; 
    }
    else if(element=='+'|| element=='-'){
        return 1;
    }
    else{
        return 0;
    }
}
int main() {
    printf("enter a number");
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
            while(top>-1 && stack[top]!='('){
                postfix[j]=pop();
                j++;
            }

            pop();}
        
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
return 0;
}