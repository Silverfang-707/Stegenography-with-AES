%{
#include "y.tab.h"
%}

%%
aba.*               { return START_WITH_ABA; }
.*bb                { return END_WITH_BB; }
.                   { return INVALID; }
%%

int yywrap() {
    return 1;
}
