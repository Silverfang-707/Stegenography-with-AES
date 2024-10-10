%{
#include <stdio.h>
#include <stdlib.h>
int yylex(void);
void yyerror(char* s);
%}
%token NUM
%left '+' '-'
%left '*' '/'
%%
S : E {printf("\n");}
E : E '+' T {printf("+");}
    | E '-' T {printf("-");}
    | T
;
T : T '*' F {printf("*");}
    | T '/' F {printf("/");}
    | F
;
F : '(' E ')' 
    |'-' F {printf("-");}
    | NUM {printf("%d", yylval);}
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
