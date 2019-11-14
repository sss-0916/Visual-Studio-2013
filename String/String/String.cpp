#include "String.h"

void Sss::string::reserve(size_t capacity){
	if (capacity == 0 || capacity > _capacity){
		if (capacity % 8 == 0){
			capacity += 8;
		}
		else{
			capacity = (capacity / 8 + 1) * 8;
		}

		char* temp = new char[capacity];

		if (_str){
			strcpy(temp, _str);
		}

		delete[] _str;

		_str = temp;
		_capacity = capacity - 1;
	}
}

void Sss::string::resize(size_t size, char ch = '\0'){
	if (size <= _size){
		_size = size;
		_str[_size] = '\0';
	}
	else{
		reserve(size);

		for (size_t i = _size; i < size; ++i){
			_str[i] = ch;
		}

		_str[size] = '\0';
	}
}

Sss::string& Sss::string::insert(size_t pos, char ch){
	assert(pos <= _size);

	if (_size == _capacity){
		reserve(_capacity * 2);
	}

	for (int i = (int)_size; i >= (int)pos; --i){
		_str[i + 1] = _str[i];
	}

	_str[pos] = ch;
	++_size;

	return *this;
}

Sss::string& Sss::string::insert(size_t pos, const char* str){
	assert(pos <= _size);

	int len = strlen(str);

	while (_size + len >= _capacity){
		reserve(_capacity * 2);
	}

	for (int i = (int)_size; i >= (int)pos; --i){
		_str[i + len] = _str[i];
	}

	for (int i = pos, j = 0; j < (int)len; ++i){
		_str[i] = str[j++];
	}

	_size += len;

	return *this;
}

Sss::string& Sss::string::push_back(char ch){
	insert(_size, ch);

	return *this;
}

Sss::string& Sss::string::append(const char* str){
	insert(_size, str);

	return *this;
}

Sss::string& Sss::string::erase(size_t pos, size_t len){
	if (pos >= _size){
		return *this;
	}

	for (size_t i = pos, j = 0; j < len && i < _size - 2; ++i){
		_str[i] = _str[i + 1];
	}

	--_size;
	_str[_size] = '\0';

	return *this;
}

size_t Sss::string::find(char ch, size_t pos) const{
	assert(pos < _size);

	for (int i = pos; i < (int)_size; ++i){
		if (_str[i] == ch){
			return (size_t)i;
		}
	}

	return -1;
}

size_t Sss::string::find(const char* str, size_t pos) const{
	assert(pos < _size);

	char* temp = strstr(_str + pos, str);

	return temp - _str;
}

Sss::string& Sss::string::operator+=(char ch){
	insert(_size, ch);

	return *this;
}

Sss::string& Sss::string::operator+=(const char* str){
	insert(_size, str);

	return *this;
}

Sss::string Sss::string::operator+(char ch) const{
	string temp(*this);

	temp += ch;

	return temp;
}

Sss::string Sss::string::operator+(const char* str) const{
	string temp(*this);

	temp += str;

	return temp;
}

char& Sss::string::operator[](size_t pos){
	assert(pos < _size);

	return *(_str + pos);
}

const char& Sss::string::operator[](size_t pos) const{
	assert(pos < _size);

	return *(_str + pos);
}

bool Sss::string::operator>(const string& s) const{
	int ret = strcmp((*this).c_str(), s.c_str());

	if (ret <= 0){
		return false;
	}

	return true;
}

bool Sss::string::operator==(const string& s) const{
	int ret = strcmp((*this).c_str(), s.c_str());

	if (!ret){
		return true;
	}

	return false;
}

bool Sss::string::operator>=(const string& s) const{
	return (*this) > s || (*this) == s;
}

bool Sss::string::operator<(const string& s) const{
	return !((*this) >= s);
}

bool Sss::string::operator<=(const string& s) const{
	return !((*this) > s);
}

bool Sss::string::operator!=(const string& s) const{
	return !((*this) == s);
}

size_t Sss::string::_npos = -1;

void stringTest(){

	Sss::string s1("helloa");
	Sss::string s2("hello");

	if (s1 > s2){
		std::cout << "hehe" << std::endl;
	}
}