#include <iostream>
#include <stdlib.h>

class Base1{
public:
	virtual void func1(){
		std::cout << "Base1::func1()" << std::endl;
	}

	virtual void func2(){
		std::cout << "Base1::func2()" << std::endl;
	}

private:
	int _b1;
};

class Base2{
public:
	virtual void func1(){
		std::cout << "Base2::func1()" << std::endl;
	}

	virtual void func2(){
		std::cout << "Base2::func2()" << std::endl;
	}

private:
	int _b2;
};

class Derive : public Base1, public Base2{
public:
	virtual void func1(){
		std::cout << "Derive::func1()" << std::endl;
	}

	virtual void func3(){
		std::cout << "Derive::func3()" << std::endl;
	}

private:
	int _d;
};

typedef void(*VFPTR)();

void vfptrDisplay(VFPTR v[]){
	std::cout << "虚表地址: " << v << std::endl;

	for (int i = 0; v[i] != nullptr; ++i){
		printf("第%d个虚函数地址: 0X%x, ->", i, v[i]);
		VFPTR f = v[i];
		f();
	}

	std::cout << std::endl;
}

int main(){
	Derive d;

	VFPTR* vd1 = (VFPTR*)(*(int*)&d);
	vfptrDisplay(vd1);

	VFPTR* vd2 = (VFPTR*)(*(int*)((char*)&d + sizeof(Base1)));
	vfptrDisplay(vd2);

	system("pause");
	return 0;
}