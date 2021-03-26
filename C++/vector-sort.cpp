#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	vector<int> v; 
	int n;
	cin >> n;
	int tmp;
	for(int i=0;i<n;i++){
		cin >> tmp;
		v.push_back(tmp);
	}
	sort(v.begin(),v.end());
	for(int i=0;i<n;i++){
		cout << v[i] << " 
	}
	return 0;
}	