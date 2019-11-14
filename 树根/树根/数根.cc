#include <iostream>
#include <stdlib.h>

int numberRoot(int n){
	int ret = 0;

	while (n){
		ret += n % 10;
		n /= 10;
	}

	if (ret / 10){
		return numberRoot(ret);
	}
	return ret;
}

int main(){
	int n;

	while (std::cin >> n){
		std::cout << numberRoot(n) << std::endl;
	}
	
	system("pause");
	return 0;
}