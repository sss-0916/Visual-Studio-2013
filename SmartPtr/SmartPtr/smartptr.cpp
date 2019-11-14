#include <iostream>
#include <stdlib.h>
using namespace std;

template<class T>
class SmartPtr{
public:
	SmartPtr(T* ptr)
		: _ptr(ptr)
	{}

	~SmartPtr(){
		delete _ptr;
	}

	T& operator*(){
		return *_ptr;
	}

	T* operator->(){
		return _ptr;
	}

private:
	T* _ptr;
};

int main(){
	
	system("pause");
	return 0;
}

// sp2 = sp1
shared_ptr<T>& operator=(const shared_ptr<T>& sp){
	if (this != &sp){
		if (--(*pcnt) == 0){
			delete _ptr;
			delete _pcnt;
		}

		_ptr = s1._ptr;
		_pcnt = s1._pcnt;
		++(*_pcnt);
	}

	return *this;
}