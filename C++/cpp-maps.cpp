#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int n,type,mark;
    
    cin >> n;
    map<string, int> clas;
    string name;
    
    for(int i=0;i<n;i++)
    {
        cin >> type;
		cin >> name;
        
        if (type == 1)
        {
			cin >> mark;
			clas[name] += mark;
        }
		else if (type == 2)
		{
			clas.erase(name);
		}
		
		else 
		{
			cout << clas[name] << endl;
		}
			
    }
    
    return 0;
}
