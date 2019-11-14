#pragma once

// ������ɫ
enum Color{
	RED, BLACK
};

// ��������
template<class K, class V>
struct RBTreeNode{

	RBTreeNode(const pair<K, V>& kv, Color color = RED)
		: _parent(nullptr)
		, _left(nullptr)
		, _right(nullptr)
		, _kv(kv)
		, _color(color)
	{}

	// ����˫��
	RBTreeNode<K, V>* _parent;
	// ��������
	RBTreeNode<K, V>* _left;
	// �����Һ���
	RBTreeNode<K, V>* _right;
	pair<K, V> _kv;
	// ������ɫ
	Color _color;

};

template<clas K, class V>
class RBTree{
	typedef RBTreeNode<K, V> Node;

public:
	RBTree()
		: _root(nullptr)
	{}

	// ������Ĳ���
	bool insert(const pair<K, V>& kv){
		// ����
		if (_root == nullptr){
			_root = new Node(kv);

			return true;
		}

		// ����Ϊ��
		Node* cur = _root;
		// ����˫��
		Node* parent = nullptr;

		while (cur != nullptr){
			parent = cur;

			// �ȵ�ǰ����ȥ������
			if (kv.first > cur->_kv.first){
				cur = cur->_right;
			}
			// �ȵ�ǰ���С��ȥ������
			else if (kv.first < cur->_kv.first){
				cur = cur->_left;
			}
			// ��ȣ��Ѿ����ڣ�����ʧ��
			else{
				return false;
			}
		}

		// ��㴴��
		cur = new Node(kv);

		// �´����Ľ��ָ����˫�׽��
		cur->_parent = parent;

		// ��˫�״���˫�׵�����
		if (kv.first > parent->_kv.first){
			parent->_right = cur;
		}
		// ��˫��С����˫�׵�����
		else{
			parent->_left = cur;
		}

		// ����Ϊ��ɫ��Υ�����򣬲���Ҫ����
		// ���״��ڲ���Ϊ��ɫ
		while (parent && parent->_color == RED){
			// �游���
			Node* grandparent = parent->_parent;
			// ����������游����
			if (parent == grandparent->_left){
				// ������
				Node* uncle = grandparent->_right;

				// ���һ�����������Ϊ��
				if (uncle != nullptr && uncle->_color == RED){
					// ���׺�����Ϳ�ɺڣ��游Ϳ�ɺ�
					parent->_color = BLACK;
					uncle->_color = BLACK;
					grandparent->_color = RED;

					// �游����cur���������ϵ���
					cur = grandparent;
					parent = parent->_parent;
				}
				// �����/�������岻���ڻ��ߴ�����Ϊ��
				else{
					// �ȴ�����������������ת��Ϊ�����
					if (cur = parent->_right){
						// ����
						leftRotate(parent);

						// ����parent��cur
						swap(parent, cur);
					}

					// ����������岻���ڻ��ߴ�����Ϊ��
					// �ҵ���
					rightRotate(grandparent);

					parent->_color = BLACK;
					grandparent->_color = RED;

					break;
				}
			}
			// �������游����
			else{
				// ���������游������
				Node* uncle = grandparent->_left;

				// ���һ�����������Ϊ��
				if (uncle != nullptr && uncle->_color == RED){
					// ���ף�����Ϳ�ɺ�ɫ���游Ϳ�ɺ�ɫ
					parent->_color = BLACK;
					uncle->_color = BLACK;
					grandparent->_color = RED;

					// ���游����cur���������ϵ���
					cur = grandparent;
					parent = cur->_parent;
				}
				// �����/�������岻����/���������Ϊ��
				else{
					// �ȴ�����������������ת��Ϊ�����
					if (cur = parent->_left){
						// �ҵ���
						rightRotate(parent);

						// ����parent��cur
						swap(parent, cur);
					}

					// ����������岻����/���������Ϊ��
					leftRotate(grandparent);

					// ����Ϳ�ڣ��游Ϳ��
					parent->_color = BLACK;
					grandparent->_color = RED;

					break;
				}
			}
		}

		// ���ڵ�Ϳ��
		_root->_color = BLACK;

		return true;
	}

	// �������
	Node* getRoot(){
		return _root;
	}

	// �ǲ��Ǻ����
	bool _isRBTree(Node* root, size_t cnt, size_t black_cnt){
		// �ߵ�һ��·���ľ�ͷ
		if (root == nullptr){
			// �жϺ�ɫ������Ƿ���ͬ
			if (cnt != black_cnt){
				cout << "Υ�������ģ�ÿ��·���к�ɫ���ĸ���������ͬ��" << endl;

				return false;
			}

			return true;
		}

		// ͳ�Ƶ�ǰ·����ɫ�������
		if (root->_color == BLACK){
			++cnt;
		}

		// ��⵱ǰ�������˫�׽���Ƿ��Ǻ�ɫ
		Node* parent = root->_parent;
		if (parent != nullptr && parent->_color == RED && root->_color == RED){
			cout << "Υ����������û������һ��ĺ�ɫ��㣡" << endl;

			return false;
		}

		return _isRBTree(root->_left, cnt, black_cnt) &&
			_isRBTree(root->_right, cnt, black_cnt);
	}

	// �ǲ��Ǻ����
	bool isRBTree(){
		Node* root = getRoot();

		// �����Ǻ����
		if (root == nullptr){
			return true;
		}

		// �����ڵ��Ƿ�Ϊ��ɫ
		if (root->_color == BLACK){
			cout << "Υ�����ʶ�����������Ϊ��ɫ��" << endl;

			return false;
		}

		// ��ȡ����һ��·���ĺڽ������������ѡ������·��
		size_t black_cnt = 0;
		Node* cur = root;
		while (cur != nullptr){
			if (cur->_color == BLACK){
				++black_cnt;
			}

			cur = cur->_left;
		}

		// ����Ƿ��������������ʣ�cnt������¼·���к�ɫ��������
		size_t cnt = 0;

		return _isRBTree(root, cnt, black_cnt);
	}

private:
	// ���ڵ�
	Node* _root;
};

// �ǲ��Ǻ����
bool _isRBTree(Node* root, size_t cnt, size_t black_cnt){
	// �ߵ�һ��·���ľ�ͷ
	if (root == nullptr){
		// �жϺ�ɫ������Ƿ���ͬ
		if (cnt != black_cnt){
			cout << "Υ�������ģ�ÿ��·���к�ɫ���ĸ���������ͬ��" << endl;

			return false;
		}

		return true;
	}

	// ͳ�Ƶ�ǰ·����ɫ�������
	if (root->_color == BLACK){
		++cnt;
	}

	// ��⵱ǰ�������˫�׽���Ƿ��Ǻ�ɫ
	Node* parent = root->_parent;
	if (parent != nullptr && parent->_color == RED && root->_color == RED){
		cout << "Υ����������û������һ��ĺ�ɫ��㣡" << endl;

		return false;
	}

	return _isRBTree(root->_left, cnt, black_cnt) &&
		_isRBTree(root->_right, cnt, black_cnt);
}

// �ǲ��Ǻ����
bool isRBTree(){
	Node* root = getRoot();

	// �����Ǻ����
	if (root == nullptr){
		return true;
	}

	// �����ڵ��Ƿ�Ϊ��ɫ
	if (root->_color == BLACK){
		cout << "Υ�����ʶ�����������Ϊ��ɫ��" << endl;

		return false;
	}

	// ��ȡ����һ��·���ĺڽ������������ѡ������·��
	size_t black_cnt = 0;
	Node* cur = root;
	while (cur != nullptr){
		if (cur->_color == BLACK){
			++black_cnt;
		}

		cur = cur->_left;
	}

	// ����Ƿ��������������ʣ�cnt������¼·���к�ɫ��������
	size_t cnt = 0;

	return _isRBTree(root, cnt, black_cnt);
}