#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main()
{
	map<int, int> duplicate;
	vector<int> a, b;
	int x,y;
	int sum = 0;
	int score = 0;
	int times = 0;

	ifstream inputFile("twoLists.txt");

	while (inputFile >> x >> y){
		a.push_back(x);
		b.push_back(y);
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	for (int i = 0; i < 1000; ++i)
	{
		times = count(b.begin(), b.end(), a[i]);
		score = times * a[i];

		sum += score;
	}



	cout << sum << endl;


	return 0;
};