%{
#include "y.tab.h"
extern int yylval;
%}

%%
"0"    { yylval = 0; return A; }
"1"    { yylval = 1; return B; }
\n     { return NL; }
.      { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
