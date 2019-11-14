#pragma once

#include <deque>

template<class T, class Container = deque<T>>
class Queue{
public:
	void Push(const T& x){
		_con.push_back(x);
	}

	void Pop(){
		_con.pop_front();
	}

	size_t Size() const{
		return _con.size();
	}

	bool Empty() const {
		return _con.empty();
	}

	const T& Front() const{
		return _con.front();
	}

	const T& Back() const{
		return _con.back();
	}

private:
	Container _con;
};