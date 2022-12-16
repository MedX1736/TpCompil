%{

%}

%%

a+|b+|c+|d+|e+|f+|g+|h+|i+|j+|k+|l+|m+|n+|o+|p+|q+|r+|s+|t+|u+|v+|w+|x+|y+|z+|A+|B+|C+|D+|E+|F+|G+|H+|I+|J+|K+|L+|M+|N+|O+|P+|Q+|R+|S+|T+|U+|V+|W+|X+|Y+|Z+ {fprintf(yyout,"%s%d", &yytext[yyleng-1], yyleng); } 
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