int main(void){
    int a,b,c;
    int result1,result2,result3,result4;
    scanf("%d %d %d",&a,&b,&c);
    result1=(a+b)%c;
    result2=((a%c)+(b%c))%c;
    result3=(a*b)%c;
    result4=((a%c)*(b%c))%c;
    printf("%d\n",result1);
    printf("%d\n",result2);
    printf("%d\n",result3);
    printf("%d\n",result4);
}
