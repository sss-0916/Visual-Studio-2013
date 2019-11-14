#include <iostream>
#include <stdlib.h>

void third(){
	throw e;
}

void second(){
	third();
}

void first(){
	second();
}

int main(){

	first();
	
	system("pause");
	return 0;
}