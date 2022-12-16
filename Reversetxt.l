%{
char lettre[5];
char chiffre[5];
int i, j;
%}

%start C 

%%
[a-zA-Z] {strcpy(lettre, yytext) ;
BEGIN C;}

<C>[1-9]([0-9])* {
    j= atoi(yytext);
    for (i=0; i<j; i++){
        printf("%s", lettre);
    }
}
<C>. {BEGIN 0;}
. ;


%%
int yywrap(){}
int main(int argc,char* argv[]){
    yy_scan_string(argv[1]);
    yylex();
    return 0;
}

