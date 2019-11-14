#pragma once

#define _CRT_SECURE_NO_WARNINGS

#include <string.h>
#include <iostream>

// String��
class String{
public:
	// ���캯��
	String(const char* str = "")
		: _str(new char[strlen(str) + 1])
	{
		strcpy(_str, str);
	}

	// ��������
	~String(){
		if (_str){
			delete[] _str;
		}
	}

	// �������캯��
	String(const String& s)
		: _str(new char[strlen(s._str) + 1])
	{
		std::cout << "String(const String& s)" << std::endl;

		strcpy(_str, s._str);
	}

	// �ƶ����캯��
	String(String&& s){
		std::cout << "String(String&& s)" << std::endl;

		_str = s._str;
		s._str = nullptr;
	}

	// ��ֵ��������غ���
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

	// �ƶ���ֵ����
	String& operator=(String&& s){
		std::cout << "String& operator=(String&& s)" << std::endl;

		// ������������Դ�͵�ǰ�������Դ����
		std::swap(_str, s._str);

		return *this;
	}

	// +=���������
	String& operator+=(const String& s){
		/*
		*	...
		*/

		return *this;
	}

	// +���������
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