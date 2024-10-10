%{
#include <stdio.h>
int yylex(void);
void yyerror(char* s);
char st[100];
int top = 0;
%}
%token NUMBER NL
%left '+' '-'
%left '*' '/'
%%
S : E {printf("\n"); return 0;}
;
E : E '+' T {st[top++] = '+'; printf("%c", st[--top]);}
    | E '-' T {st[top++] = '-'; printf("%c", st[--top]);}
    | T
;
T : T '*' F {st[top++] = '*'; printf("%c", st[--top]);}
    | T '/' F {st[top++] = '/'; printf("%c", st[--top]);}
    | F
;
F : '(' E ')' 
    |'-' F {st[top++] = '-'; printf("%c", st[--top]);}
    | NUMBER {printf("%d", yylval);}
;
%%
int main(){
printf("\nEnter the Expression: ");
yyparse();
return 0;
}
void yyerror(char *s){
printf("\nInvalid Expression\n");
}
