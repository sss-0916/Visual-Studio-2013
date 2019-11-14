#pragma once

// �������������
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

// ����������
template<class K, class V>
class BSTree{
	typedef BSTreeNode<K, V> Node;

public:
	BSTree()
		: _root(nullptr)
	{}

	~BSTree(){
		// �������������ͷ�
		_release(_root);
	}

	// ���������������
	void inorder(){
		_inorder(_root);

		cout << endl;
	}

	// �����������Ĳ���
	Node* find(const K& key){
		return _find(key);
	}

	// �����������Ĳ���
	bool insert(const pair<K, V>& kv){
		return _insert(kv);
	}

	// ������������ɾ��
	bool remove(const K& key){
		return _remove(key);
	}

private:
	// �ͷ�
	void _release(Node* root){
		// �����ǿ�
		if (root){
			// �������Һ���
			Node* left = root->_left;
			Node* right = root->_right;

			// �ͷŸ�
			delete root;

			// �����ǿգ��ͷ�����
			if (left){
				_release(left);
			}

			// �����ǿգ��ͷ�����
			if (right){
				_release(right);
			}
		}
	}

	// �������
	void _inorder(Node* root){
		// �ݹ����
		if (root == nullptr){
			return;
		}

		_inorder(root->_left);
		cout << root->_kv.first << " ";
		_inorder(root->_right);
	}

	// ����
	Node* _find(const K& key){
		Node* cur = _root;

		while (cur != nullptr){
			// �ȸ�����ȥ��������
			if (key > cur->_kv.first){
				cur = cur->_right;
			}
			// �ȸ����С��ȥ��������
			else if (key < cur->_kv.first){
				cur = cur->_left;
			}
			// ���
			else{
				break;
			}
		}

		return cur;
	}

	// ����
	bool _insert(const pair<K, V>& kv){
		// ��Ϊ��
		if (_root == nullptr){
			_root = new Node(kv);

			return true;
		}
		// ����Ϊ��
		else{
			Node* cur = _root;
			// ���游�ڵ�
			Node* parent = nullptr;

			while (cur != nullptr){
				parent = cur;

				// �ȸ�����ȥ������
				if (kv.first > cur->_kv.first){
					cur = cur->_right;
				}
				// �ȸ����С��ȥ������
				else if (kv.first < cur->_kv.first){
					cur = cur->_left;
				}
				// �͸����һ�����Ѵ��ڣ�����ʧ��
				else{
					return false;
				}
			}

			// �²�����
			cur = new Node(kv);

			// ��˫�׽��󣬲��뵽����
			if (kv.first > parent->_kv.first){
				parent->_right = cur;
			}
			// ��˫�׽��С�����뵽����
			else{
				parent->_left = cur;
			}

			return true;
		}
	}

	// ɾ��
	bool _remove(const K& key){
		Node* cur = _root;
		// ���游���
		Node* parent = nullptr;

		while (cur != nullptr){
			// �ȸ�����������
			if (key > cur->_kv.first){
				parent = cur;
				cur = cur->_right;
			}
			// �ȸ����С��������
			else if (key < cur->_kv.first){
				parent = cur;
				cur = cur->_left;
			}
			// �ҵ���
			else{
				// �ýڵ�����Ϊ��
				if (cur->_left == nullptr){
					// �ýڵ�Ϊ�����
					if (parent == nullptr){
						_root = cur->_right;
					}
					else{
						// �ýڵ��ڸ���������
						if (cur->_kv.first > parent->_kv.first){
							parent->_right = cur->_right;
						}
						// �ýڵ��ڸ���������
						else{
							parent->_left = cur->_right;
						}
					}
				}
				// �ýڵ�����Ϊ��
				else if (cur->_right == nullptr){
					// �ýڵ�Ϊ�����
					if (parent == nullptr){
						_root = cur->_left;
					}

					// �ýڵ��ڸ���������
					if (cur->_kv.first > parent->_kv.first){
						parent->_right = cur->_left;
					}
					// �ýڵ��ڸ���������
					else{
						parent->_left = cur->_right;
					}
				}
				// �ýڵ�����������Ϊ��
				else{
					// ������Ѱ��������
					Node* replace = cur->_right;
					// ����������ĸ����
					Node* rparent = cur;

					// Ѱ�������㣬�������е���Сֵ
					while (replace->_left){
						rparent = replace;
						replace = replace->_left;
					}

					cur->_kv = replace->_kv;
					cur = replace;

					// �ж�replace�Ƿ�������
					// replace������
					if (rparent->_left == replace){
						// �����������������������ĸ���������
						rparent->_left = replace->_right;
					}
					// replaceû������
					else{
						// �����������������������ĸ���������
						rparent->_right = replace->_right;
					}
				}

				// ɾ��������
				delete cur;

				return true;
			}
		}
		return false;
	}

private:
	Node* _root;
};