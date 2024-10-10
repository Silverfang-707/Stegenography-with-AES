%{
#include<stdio.h>
#include<stdlib.h>
int yylex(void);
void yyerror(char *);
int count = 0;
%}

%token A B NL

%%

stmt: S NL
{
    if(count == 0)
        printf("valid string\n");
    else
        printf("invalid string\n");
    exit(0);
}
;

S: A { count++; } S B B { count--; } | ;

%%

void yyerror(char *msg) {
    printf("invalid string\n");
    exit(0);
}

int main() {
    printf("\nenter the string: ");
    yyparse();
    return 0;
}
