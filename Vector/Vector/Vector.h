#pragma once

#include <iostream>
#include <string.h>
#include <assert.h>

template<class T>
class Vector{
public:
	typedef T* iterator;
	typedef const T* const_iterator;

	Vector()
		: _start(nullptr)
		, _finish(nullptr)
		, _endofstorage(nullptr)
	{}

	Vector(const Vector<T>& v)
		: _start(nullptr)
		, _finish(nullptr)
		, _endofstorage(nullptr)
	{
		Reserve(v.Size());

		for (size_t i = 0; i < v.Size(); ++i){
			PushBack(v[i]);
		}
	}

	Vector<T>& operator=(Vector<T> v){
		swap(v);

		return *this;
	}

	~Vector(){
		if (_start){
			delete[] _start;

			_start = nullptr;
			_finish = nullptr;
			_endofstorage = nullptr;
		}
	}

public:
	iterator begin(){
		return _start;
	}

	iterator end(){
		return _finish;
	}

	const_iterator begin() const{
		return _start;
	}

	const_iterator end() const{
		return _finish;
	}

public:
	void Reserve(size_t n, const T& val = T());

	void Resize(size_t n, const T& val = T());

public:
	void PushBack(const T& x);

	void PopBack();

	void Insert(iterator pos, const T& x);

	void Erase(iterator pos);

public:
	T& operator[](size_t pos){
		assert(pos < Size());

		return _start[pos];
	}

	const T& operator[](size_t pos) const{
		assert(pos < Size());

		return _start[pos];
	}

public:
	size_t Size() const{
		return _finish - _start;
	}

	size_t Capacity() const{
		return _endofstorage - _start;
	}

	void swap(Vector<T>& v){
		std::swap(_start, v._start);
		std::swap(_finish, v._finish);
		std::swap(_endofstorage, v._endofstorage);
	}

private:
	T* _start;
	T* _finish;
	T* _endofstorage;
};

void vectorTest();