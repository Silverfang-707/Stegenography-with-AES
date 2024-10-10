%{
#include <stdio.h>
extern int yylex();
void yyerror(const char *s);
%}

%token START END ZERO ONE

%%

input: START middle END
    { printf("Accepted\n"); }
    ;

middle: /* empty */
    | middle ZERO
    | middle ONE
    ;

%%

void yyerror(const char *s) {
    printf("Not accepted\n");
}

int main() {
    yyparse();
    return 0;
}
