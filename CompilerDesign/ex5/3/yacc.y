%{
#include <stdio.h>

void yyerror(const char *s);
%}

%token START_WITH_ABA
%token END_WITH_BB
%token INVALID

%%

start: valid_string     { printf("Valid\n"); }
     | INVALID          { printf("Invalid\n"); }
     ;

valid_string: START_WITH_ABA
            | END_WITH_BB
            ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}
