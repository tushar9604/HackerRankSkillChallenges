#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c,int d) {
	int max;
	
	if (a > b) {
		max = a;
	}
	else {
		max = b;
	}
	
	if (c > max) {
		max = c;
	}
	
	if (d > max) {
		max = d;
	}
	
	return max;
	//return((a>b?a:b)>(c>d?c:d)?(a>b?a:b):(c>d?c:d));
}

int main(){
	int a,b,c,d;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	int ans = max_of_four(a,b,c,d);
	printf("%d",ans);
	
	return 0;
}