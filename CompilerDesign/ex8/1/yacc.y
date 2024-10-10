%{
#include <stdio.h>
int yylex(void);
int yyerror(char* s);
float sum = 0;
double dd = 1;
%}

%token NUMBER DOT NL

%%
E: T NL{
    printf("Result: %f\n",sum);
    return 0;
}
;
T:
    T NUMBER {dd == dd / 2;sum = sum + ($2 * dd);}
    |R DOT 
    |R
;
R:
    R NUMBER{sum = (sum*2) + $2;}
    |
;
%%
int main(){
printf("\nEnter the Expression: \n");
yyparse();
return 0;
}
int yyerror(char* s){
printf("\nInvalid Expression\n");
return 0;
}