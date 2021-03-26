#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	
	int n;
	cin >> n;
	
	vector<int> v;
	int temp;
	
	for(int i=0;i<n;i++)
	{
		cin >> temp;
		v.push_back(temp);
	}
	
	int pos;
	cin >> pos;
	
	v.erase(v.begin()+(pos-1));
	
	int start,end;
	cin >> start >> end;
	
	v.erase(v.begin()+(start-1),v.begin()+(end-1));
	
	int size=v.size();
	
	cout << size << endl;
	
	for (int j=0;j<size;j++)
	{
		cout<<v[j]<< " ";
	}
	
	return 0;
}