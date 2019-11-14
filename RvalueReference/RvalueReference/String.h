#pragma once

#define _CRT_SECURE_NO_WARNINGS

#include <string.h>
#include <iostream>

// String类
class String{
public:
	// 构造函数
	String(const char* str = "")
		: _str(new char[strlen(str) + 1])
	{
		strcpy(_str, str);
	}

	// 析构函数
	~String(){
		if (_str){
			delete[] _str;
		}
	}

	// 拷贝构造函数
	String(const String& s)
		: _str(new char[strlen(s._str) + 1])
	{
		std::cout << "String(const String& s)" << std::endl;

		strcpy(_str, s._str);
	}

	// 移动构造函数
	String(String&& s){
		std::cout << "String(String&& s)" << std::endl;

		_str = s._str;
		s._str = nullptr;
	}

	// 赋值运算符重载函数
	String& operator=(const String& s){
		std::cout << "String& operator=(const String& s)" << std::endl;

		if (this != &s){
			char* temp = new char[strlen(s._str) + 1];
			strcpy(temp, s._str);
			delete[] _str;
			_str = temp;
		}

		return *this;
	}

	// 移动赋值函数
	String& operator=(String&& s){
		std::cout << "String& operator=(String&& s)" << std::endl;

		// 将传入对象的资源和当前对象的资源交换
		std::swap(_str, s._str);

		return *this;
	}

	// +=运算符重载
	String& operator+=(const String& s){
		/*
		*	...
		*/

		return *this;
	}

	// +运算符重载
	String operator+(const String& s){
		String ret(*this);
		/*
		*	...
		*/

		return ret;
	}

private:
	char* _str;
};