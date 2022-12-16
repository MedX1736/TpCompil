%{

%}

%%

a+|b+|c+|d+|e+|f+|g+|h+|i+|j+|k+|l+|m+|n+|o+|p+|q+|r+|s+|t+|u+|v+|w+|x+|y+|z+|A+|B+|C+|D+|E+|F+|G+|H+|I+|J+|K+|L+|M+|N+|O+|P+|Q+|R+|S+|T+|U+|V+|W+|X+|Y+|Z+ {printf("%s%d", &yytext[yyleng-1], yyleng); } 
. ;

%%

int yywrap(){}
int main(int argc,char* argv[]){
    yy_scan_string(argv[1]);
    yylex();
    return 0;
}