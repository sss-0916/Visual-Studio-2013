#include "String.h"

void Func(String&& s){
	// 完美转发
	String copy(std::forward<String>(s));
}

int main(){
	String str("hello, world!");

	// 传递右值引用
	Func(std::move(str));

	return 0;
}