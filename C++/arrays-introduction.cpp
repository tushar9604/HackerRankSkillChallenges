#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[n];
	for (i = 0; i < n; i++) {
		cin >> arr[i]
	}
	while (cout << arr[--n] << " " && n);
	return 0;
}

#include <iostream>
int main() {
    int N,i=0;
    std::cin>>N;
    int *A = new int[N];
    while(std::cin>>A[i++]);
    while(std::cout<<A[--N]<<' ' && N);
    delete[] A;
    return 0;
}