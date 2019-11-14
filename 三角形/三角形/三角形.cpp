#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

int main(){
	vector<int> v;
	int num;

	while (cin >> num){
		v.push_back(num);
	}

	for (int i = 0; i < v.size(); i += 3){
		if (v[0] + v[1] > v[2] &&
			v[0] + v[2] > v[1] &&
			v[1] + v[2] > v[0]){
			cout << "Yes" << endl;
		}
		else{
			cout << "No" << endl;
		}
	}

	system("pause");
	return 0;
}