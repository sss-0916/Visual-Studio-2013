#pragma once

#include <deque>

template<class T, class Container = std::deque<T>>
class Stack{
public:
	void Push(const T& x){
		_con.push_back(x);
	}

	void Pop(){
		_con.pop_back();
	}

	size_t Size() const{
		return _con.size();
	}

	bool Empty() const{
		return _con.empty();
	}

	T& Top(){
		return _con.back();
	}

	const T& Top() const{
		return _con.back();
	}

private:
	Container _con;
};