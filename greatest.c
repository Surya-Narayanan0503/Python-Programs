#include<stdio.h>
int main()
{
int m,n,o;
scanf("%d %d %d",&m,&n,&o);
if(m>n && m>o){
		printf("%d",m);
	}
	
	else if(m<n && o<n){
			printf("%d",n);
		}
	else{
			printf("%d",o);
		}
}
