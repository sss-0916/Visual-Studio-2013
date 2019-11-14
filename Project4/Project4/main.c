#include <iostream>
#include <string>
using namespace std;

int main(){
	string s;
	cin >> s;
	cout << s << endl;
	for (size_t i = 0; i < s.size(); ++i){
		cout << s[i] << " ";
	}
	cout << endl;
	
	return 0;
}