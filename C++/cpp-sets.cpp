#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
        
    int n,q,x;
    set<int> s;
    
    cin >> n;
    
    for(int i=0;i<n;i++)
    {
        cin >> q >> x;
        
        switch (q) {
            case 1:
                s.insert(x);
                break;
            case 2:
                s.erase(x);
                break;
            case 3:
                cout << (s.find(x) == s.end() ? "No" : "Yes") << endl;
                break;            
        }
    }
        
    return 0;
}
