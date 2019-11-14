#include "Queue.h"
#include <iostream>
#include <stdlib.h>

int main(){
	Queue<int, std::deque<int>> q;

	q.Push(1);
	q.Push(2);
	q.Push(3);
	q.Push(4);
	q.Push(5);

	while (!q.Empty()){
		std::cout << q.Front() << std::endl;
		q.Pop();
	}
	
	system("pause");
	return 0;
}