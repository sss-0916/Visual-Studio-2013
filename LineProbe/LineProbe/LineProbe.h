#pragma once

#include <vector>

// ��ϣͰ�н��
template<class T>
struct HashBucketNode{
	T _data;
	HashBucketNode<T>* _next;

	// ���캯��
	HashBucketNode(const T& data)
		: _next(nullptr)
		, _data(data)
	{}
};

// ��ϣͰ
template<class T, class HashFunc = DefHashFunc<T>>
class HashBucket{
	typedef HashBucketNode<T> Node;
public:
	// ���캯��
	HashBucket(size_t capacity = 10)
		: _size(0)
	{
		_ht.resize(GetNextPrime(capacity), NULL)
	}

	// ��ϣͰ��Ԫ�ز����ظ�
	Node** Insert(const T& data){
		// ����Ԫ������Ͱ��
		size_t bucketNo = HashFunc(data);
		// �ж�Ԫ���Ƿ���Ͱ��
		Node* cur = _ht[bucketNo];
		while (cur != nullptr){
			if (cur->_data == data){
				return cur;
			}
			cur = cur->_next;
		}

		// ����Ԫ��
		cur = new Node(data);
		// ͷ��
		cur->_next = _ht[bucketNo];
		_ht[bucketNo] = cur;
		++_size;

		return cur;
	}

	// ɾ��Ͱ��Ԫ�أ�����ɾ��Ԫ�ص���һ�����
	Node** Erase(const T& data){
		// ����Ͱ��
		size_t bucketNo = HashFunc(data);
		Node* cur = _ht[bucketNo];
		Node* prev = nullptr, ret = nullptr;
		while (cur != nullptr){
			if (cur->_data == data){
				// ��Ͱ�е�һ��Ԫ��
				if (cur == _ht[bucketNo]){
					_ht[bucketNo] = cur->_next;
				}
				// ���ǵ�һ��Ԫ��
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
	// ��ЧԪ������
	size_t _size;
};