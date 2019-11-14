#include <iostream>
#include <stdlib.h>
#include <map>
#include <set>
using namespace std;

int main(){

	multiset<int> m;
	m.insert(1);
	m.insert(1);
	m.insert(2);
	m.insert(2);
	m.insert(3);
	m.insert(3);

	multiset<int>::iterator mit = m.begin();
	while (mit != m.end()){
		cout << *mit << " ";
		++mit;
	}
	cout << endl;

	m.erase(1);

	mit = m.begin();
	while (mit != m.end()){
		cout << *mit << " ";
		++mit;
	}
	cout << endl;
	
	system("pause");
	return 0;
}