#include "Vector.h"

template<class T>
void Vector<T>::Reserve(size_t n, const T& val = T()){
	if (n > Capacity()){
		size_t size = Size();

		T* temp = new T[n];

		if (_start){
			for (size_t i = 0; i < size; ++i){
				temp[i] = _start[i];
			}
		}

		delete[] _start;

		_start = temp;
		_finish = _start + size;
		_endofstorage = _start + n;
	}
}

template<class T>
void Vector<T>::Resize(size_t n, const T& val = T()){
	if (n <= Size()){
		_finish = _start + n;
	}
	else{
		Reserve(n);

		while (_finish != _start + n){
			*_finish = val;
			++_finish;
		}
	}
}

template<class T>
void Vector<T>::PushBack(const T& x){
	if (_finish == _endofstorage){
		size_t capacity = Capacity() == 0 ? 4 : Capacity() * 2;
		Reserve(capacity);
	}

	*_finish = x;
	++_finish;
}

template<class T>
void Vector<T>::PopBack(){
	if (_finish > _start){
		--_finish;
	}
}

template<class T>
void Vector<T>::Insert(iterator pos, const T& x){
	assert(pos < _finish);

	if (_finish == _endofstorage){
		size_t offset = pos - _start;
		size_t capacity = Capacity() == 0 ? 4 : Capacity() * 2;

		Reserve(capacity);
		pos = _start + offset;
	}

	iterator end = _finish - 1;
	while (end >= pos){
		*(end + 1) = *end;
		--end;
	}

	*pos = x;
	++_finish;
}

// 使用iterator返回值会出错，原因暂时不详
template<class T>
void Vector<T>::Erase(iterator pos){
	assert(pos < _finish);

	iterator it = pos;
	while (it < _finish - 1){
		*it = *(it + 1);
		++it;
	}

	--_finish;

	return pos;
}

void vectorTest(){
	Vector<int> v;

	v.PushBack(1);
	v.PushBack(2);
	v.PushBack(3);
	v.PushBack(4);
	v.Insert(v.begin() + 1, 8);

	for (size_t i = 0; i < v.Size(); ++i){
		std::cout << v[i] << std::endl;
	}

}