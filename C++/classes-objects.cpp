#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

class Student {
	private:
		int scores[5];
		int sum;
		
	public:
		Student() : sum(0) {}
		int calculateTotalScore() {return sum;}
		void input() {
			for(int i=0;i<5;i++) {
				cin >> scores[i];	
				sum += scores[i];
			}
		}
};

int main() {
	int n; // number of students
	cin >> n;
	Student *s = new Student[n]; // an array of n students
	
	for (int i = 0; i < n; i++) {
		s[i].input();
	}
	
	// calculate kristen's score
	int kristen_score = s[0].calculateTotalScore();
	
	// determine how many students scored higher than kristen
	int count = 0;
	for (int i = 1; i < n; i++) {
		int total = s[i].calculateTotalScore();
		if (total > kristen_score) {
			count++;
		}
	}
	
	// print result
	cout << count;
	
	return 0;
}

//It's the syntax for initializing members of the class and it is valid when using constructors. It is called initializer list and it follows the geneal syntax:

//class_name(type1 arg1, type2 arg2, type3 arg3): member1(arg1), member2(arg2), member3(arg3){}

//Instead of assignation:

//class_name(type1 arg1, type2 arg2, type3 arg3){member1 = arg1; member2 = arg2; member3 = arg3}
