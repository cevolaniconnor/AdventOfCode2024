#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	vector<int> a, b;
	int x,y;
	int sum = 0;
	int diff;

	ifstream inputFile("twoLists.txt");

	while (inputFile >> x >> y){
		a.push_back(x);
		b.push_back(y);
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	for (int i = 0; i < 1000; i++){
		diff = a[i] - b[i];

		sum += abs(diff);
	}

	cout << sum << endl;


	return 0;
};