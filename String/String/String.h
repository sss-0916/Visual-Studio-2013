#pragma once

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string.h>
#include <assert.h>

namespace Sss{
	class string{
	public:
		typedef char* iterator;
		typedef const char* const_iterator;

		iterator begin(){
			return _str;
		}

		iterator end(){
			return _str + _size;
		}

		const_iterator begin() const{
			return _str;
		}

		const_iterator end() const{
			return _str + _size;
		}

	public:
		string(const char* str = "")
			: _str(nullptr)
			, _capacity(0)
		{
			_size = strlen(str);
			reserve(_size);
			strcpy(_str, str);
		}

		~string(){
			if (_str){
				delete[] _str;
				_size = 0;
				_capacity = 0;
			}
		}

		string(const string& s)
			: _str(nullptr)
			, _size(0)
			, _capacity(0)
		{
			// 如果s中有'\0'会出问题吗？
			string temp(s.c_str());
			swap(temp);
		}

		string& operator=(string s){
			swap(s);

			return *this;
		}

	public:
		string& operator+=(char ch);

		string& operator+=(const char* str);

		string operator+(char ch) const;

		string operator+(const char* str) const;

		char& operator[](size_t pos);

		const char& operator[](size_t pos) const;

	public:
		bool operator>(const string& s) const;

		bool operator==(const string& s) const;

		bool operator>=(const string& s) const;

		bool operator<(const string& s) const;

		bool operator<=(const string& s) const;

		bool operator!=(const string& s) const;

	public:
		string& insert(size_t pos, char ch);

		string& insert(size_t pos, const char* str);

		string& push_back(char ch);

		string& append(const char* str);

		string& erase(size_t pos, size_t len = _npos);

		size_t find(char ch, size_t pos = 0) const;

		size_t find(const char* str, size_t pos = 0) const;

	public:
		void reserve(size_t capacity);

		void resize(size_t size, char ch);

		size_t capacity() const{
			return _capacity;
		}

		size_t size() const{
			return _size;
		}

	public:
		char* c_str() const{
			return _str;
		}

		void swap(string& s){
			std::swap(_str, s._str);
			std::swap(_size, s._size);
			std::swap(_capacity, s._capacity);
		}

	private:
		char* _str;
		size_t _size;
		size_t _capacity;
		static size_t _npos;
	};

	// 此处定义_npos会报错，重复定义，为什么？不能在头文件中定义静态成员变量吗？
	//size_t string::_npos = -1;

}

void stringTest();