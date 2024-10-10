%{
#include "y.tab.h"
extern int yylval;
%}

%%
[01] {yylval = atoi(yytext); return NUMBER;}
[.] {return DOT;}
[\t]+ ;
[\n] {return NL;}
. {return yytext[0];}
%%

int yywrap(){
    return 1;
}