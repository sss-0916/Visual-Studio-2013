#pragma once

#include <vector>

// 哈希桶中结点
template<class T>
struct HashBucketNode{
	T _data;
	HashBucketNode<T>* _next;

	// 构造函数
	HashBucketNode(const T& data)
		: _next(nullptr)
		, _data(data)
	{}
};

// 哈希桶
template<class T, class HashFunc = DefHashFunc<T>>
class HashBucket{
	typedef HashBucketNode<T> Node;
public:
	// 构造函数
	HashBucket(size_t capacity = 10)
		: _size(0)
	{
		_ht.resize(GetNextPrime(capacity), NULL)
	}

	// 哈希桶中元素不能重复
	Node** Insert(const T& data){
		// 计算元素所在桶号
		size_t bucketNo = HashFunc(data);
		// 判断元素是否在桶中
		Node* cur = _ht[bucketNo];
		while (cur != nullptr){
			if (cur->_data == data){
				return cur;
			}
			cur = cur->_next;
		}

		// 插入元素
		cur = new Node(data);
		// 头插
		cur->_next = _ht[bucketNo];
		_ht[bucketNo] = cur;
		++_size;

		return cur;
	}

	// 删除桶中元素，返回删除元素的下一个结点
	Node** Erase(const T& data){
		// 计算桶号
		size_t bucketNo = HashFunc(data);
		Node* cur = _ht[bucketNo];
		Node* prev = nullptr, ret = nullptr;
		while (cur != nullptr){
			if (cur->_data == data){
				// 是桶中第一个元素
				if (cur == _ht[bucketNo]){
					_ht[bucketNo] = cur->_next;
				}
				// 不是第一个元素
				else{
					prev->_next = cur->_next;
				}

				ret = cur->_next;
				delete cur;
				--_size;

				return ret;
			}
		}

		return nullptr;
	}

private:
	vector<Node**> _ht;
	// 有效元素数量
	size_t _size;
};