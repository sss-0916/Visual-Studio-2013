#include "String.h"

void Func(String&& s){
	// ����ת��
	String copy(std::forward<String>(s));
}

int main(){
	String str("hello, world!");

	// ������ֵ����
	Func(std::move(str));

	return 0;
}