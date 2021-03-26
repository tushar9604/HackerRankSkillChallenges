#include <iostream>
#include <string>
using namespace std;

int main(){
    string a,b,c;
    char tmp;
    cin >> a >> b;
    c = a + b;
    printf("%d %d\n",a.size(),b.size());
    cout << c << endl;
    tmp = a[0];
    a[0] = b[0];
    b[0] = tmp;
    cout << a << " " << b << endl;
    
    return 0;
}