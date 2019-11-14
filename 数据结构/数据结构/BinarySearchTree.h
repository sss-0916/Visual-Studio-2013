#pragma once

template<class K, class V>
struct BSTreeNode{
	pair<K, V> _kv;
	BSTreeNode<K, V>* _left;
	BSTreeNode<K, V>* _right;

	BSTreeNode(const pair<K, V>& kv)
		: _left(nullptr)
		, _right(nullptr)
		, _kv(kv)
	{}
};

template<class K, class V>
class BSTree{
	typedef BSTreeNode<K, V> Node;

public:
	BSTree()
		: _root(nullptr)
	{}

private:
	Node* _root;
};