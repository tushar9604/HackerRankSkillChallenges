#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a;
    int b;
    cin >> a >> b;
    //printf("%d\n%d",a,b);
    
    for(int i = a;i < b+1;i++) {
        if (i == 1) {
            printf("one\n");
        }
        else if (i == 2) {
            printf("two\n");
        }
        else if (i == 3) {
            printf("three\n");
        }
        else if (i == 4) {
            printf("four\n");
        }
        else if (i == 5) {
            printf("five\n");
        }
        else if (i == 6) {
            printf("six\n");
        }
        else if (i == 7) {
            printf("seven\n");
        }
        else if (i == 8) {
            printf("eight\n");
        }
        else if (i == 9) {
            printf("nine\n");
        }
        else {
            if (i % 2 == 1) {
                printf("odd\n");
            }
            else {
                printf("even\n");
            }
        }
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b;
    string c[]={"","one","two","three","four","five","six","seven","eight","nine"};
    cin>>a>>b;
    for(int i=a;i<=b;i++)
        cout<<((i<=9)?c[i]:((i%2==0)?"even":"odd"))<<endl;
}