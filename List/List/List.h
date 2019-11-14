#pragma once

template<class T>
class ListNode{
public:
	ListNode<T>* _next;
	ListNode<T>* _prev;
	T _data;

public:
	ListNode(const T& x = T())
		: _next(nullptr)
		, _prev(nullptr)
		, _data(x)
	{}
};

template<class T, class Ref, class Ptr>
class Iterator{
public:
	typedef ListNode<T> Node;
	typedef Iterator<T, Ref, Ptr> Self;
	Node* _node;

	Iterator(Node* node)
		: _node(node)
	{}

	Ref operator*(){
		return _node->_data;
	}

	Ptr operator->(){
		return &_node->_data;
	}

	Self& operator++(){
		_node = _node->_next;

		return *this;
	}

	Self operator++(int){
		Self temp(*this);

		_node = _node->_next;

		return temp;
	}

	Self& operator--(){
		_node = _node->_prev;

		return *this;
	}

	bool operator!=(const Self& it){
		return _node != it->_node;
	}
};

template<class T>
class List{
	typedef ListNode<T> Node;

public:
	typedef Iterator<T, T&, T*> iterator;
	typedef Iterator<T, const T&, const T*> const_iterator;

	List()
		: _head(new Node)
	{
		_head->_next = _head;
		_head->_prev = _head;
	}

	iterator begin(){
		return _head->_next;
	}

	iterator end(){
		return _head->_prev;
	}

	const_iterator begin() const{
		return _head->_next;
	}

	const_iterator end() const{
		return _head->_prev;
	}

	void PushBack(const T& x){
		Node* temp = new Node(x);

		temp->_next = _head;
		temp->_prev = _head->_prev;
		_head->_prev->_next = temp;
		_head->_prev = temp;
	}

private:
	Node* _head;
};