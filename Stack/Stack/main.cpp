#include "Stack.h"
#include <stdlib.h>
#include <iostream>

int main(){

	Stack<int, std::deque<int>> s;

	s.Push(1);
	s.Push(2);
	s.Push(3);
	s.Push(4);

	while (!s.Empty()){
		std::cout << s.Top() << std::endl;
		s.Pop();
	}
	
	system("pause");
	return 0;
}