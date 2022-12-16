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
        fprintf(yyout,"%s", lettre);
    }
}
<C>. {BEGIN 0;}
. ;


%%
int yywrap(){}
int main(int argc,char* argv[]){
    yyin = fopen(argv[1],"r");
    yyout = fopen(argv[2],"w");
    yylex();
    fclose(yyin);
    fclose(yyout);
    return 0;
}

