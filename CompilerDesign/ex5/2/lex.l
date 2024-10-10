%{
#include "y.tab.h"
extern int yylval;
%}

%%

"01" { return START; }
"10" { return END; }
"0" { return ZERO; }
"1" { return ONE; }

%%

int yywrap() {
    return 1;
}
