#pragma once

// 结点的颜色
enum Color{
	RED, BLACK
};

// 红黑树结点
template<class K, class V>
struct RBTreeNode{

	RBTreeNode(const pair<K, V>& kv, Color color = RED)
		: _parent(nullptr)
		, _left(nullptr)
		, _right(nullptr)
		, _kv(kv)
		, _color(color)
	{}

	// 结点的双亲
	RBTreeNode<K, V>* _parent;
	// 结点的左孩子
	RBTreeNode<K, V>* _left;
	// 结点的右孩子
	RBTreeNode<K, V>* _right;
	pair<K, V> _kv;
	// 结点的颜色
	Color _color;

};

template<clas K, class V>
class RBTree{
	typedef RBTreeNode<K, V> Node;

public:
	RBTree()
		: _root(nullptr)
	{}

	// 红黑树的插入
	bool insert(const pair<K, V>& kv){
		// 空树
		if (_root == nullptr){
			_root = new Node(kv);

			return true;
		}

		// 树不为空
		Node* cur = _root;
		// 保存双亲
		Node* parent = nullptr;

		while (cur != nullptr){
			parent = cur;

			// 比当前结点大，去右树找
			if (kv.first > cur->_kv.first){
				cur = cur->_right;
			}
			// 比当前结点小，去左树找
			else if (kv.first < cur->_kv.first){
				cur = cur->_left;
			}
			// 相等，已经存在，插入失败
			else{
				return false;
			}
		}

		// 结点创建
		cur = new Node(kv);

		// 新创建的结点指向其双亲结点
		cur->_parent = parent;

		// 比双亲大，在双亲的右树
		if (kv.first > parent->_kv.first){
			parent->_right = cur;
		}
		// 比双亲小，在双亲的左树
		else{
			parent->_left = cur;
		}

		// 父亲为黑色不违反规则，不需要调整
		// 父亲存在并且为红色
		while (parent && parent->_color == RED){
			// 祖父结点
			Node* grandparent = parent->_parent;
			// 如果父亲是祖父的左
			if (parent == grandparent->_left){
				// 叔叔结点
				Node* uncle = grandparent->_right;

				// 情况一：叔叔存在且为红
				if (uncle != nullptr && uncle->_color == RED){
					// 父亲和叔叔涂成黑，祖父涂成红
					parent->_color = BLACK;
					uncle->_color = BLACK;
					grandparent->_color = RED;

					// 祖父赋给cur，继续向上调整
					cur = grandparent;
					parent = parent->_parent;
				}
				// 情况二/三：叔叔不存在或者存在且为黑
				else{
					// 先处理情况三，将情况三转化为情况二
					if (cur = parent->_right){
						// 左单旋
						leftRotate(parent);

						// 交换parent和cur
						swap(parent, cur);
					}

					// 情况二：叔叔不存在或者存在且为黑
					// 右单旋
					rightRotate(grandparent);

					parent->_color = BLACK;
					grandparent->_color = RED;

					break;
				}
			}
			// 父亲是祖父的右
			else{
				// 叔叔结点是祖父结点的左
				Node* uncle = grandparent->_left;

				// 情况一：叔叔存在且为红
				if (uncle != nullptr && uncle->_color == RED){
					// 父亲，叔叔涂成黑色，祖父涂成红色
					parent->_color = BLACK;
					uncle->_color = BLACK;
					grandparent->_color = RED;

					// 将祖父赋给cur，继续向上调整
					cur = grandparent;
					parent = cur->_parent;
				}
				// 情况二/三：叔叔不存在/叔叔存在且为黑
				else{
					// 先处理情况三，将情况三转化为情况二
					if (cur = parent->_left){
						// 右单旋
						rightRotate(parent);

						// 交换parent和cur
						swap(parent, cur);
					}

					// 情况二：叔叔不存在/叔叔存在且为黑
					leftRotate(grandparent);

					// 父亲涂黑，祖父涂红
					parent->_color = BLACK;
					grandparent->_color = RED;

					break;
				}
			}
		}

		// 根节点涂黑
		_root->_color = BLACK;

		return true;
	}

	// 获得树根
	Node* getRoot(){
		return _root;
	}

	// 是不是红黑树
	bool _isRBTree(Node* root, size_t cnt, size_t black_cnt){
		// 走到一条路径的尽头
		if (root == nullptr){
			// 判断黑色结点数是否相同
			if (cnt != black_cnt){
				cout << "违反性质四：每条路径中黑色结点的个数必须相同！" << endl;

				return false;
			}

			return true;
		}

		// 统计当前路径黑色结点数量
		if (root->_color == BLACK){
			++cnt;
		}

		// 检测当前结点与其双亲结点是否都是红色
		Node* parent = root->_parent;
		if (parent != nullptr && parent->_color == RED && root->_color == RED){
			cout << "违反性质三：没有连在一起的红色结点！" << endl;

			return false;
		}

		return _isRBTree(root->_left, cnt, black_cnt) &&
			_isRBTree(root->_right, cnt, black_cnt);
	}

	// 是不是红黑树
	bool isRBTree(){
		Node* root = getRoot();

		// 空树是红黑树
		if (root == nullptr){
			return true;
		}

		// 检测根节点是否为黑色
		if (root->_color == BLACK){
			cout << "违反性质二：根结点必须为黑色！" << endl;

			return false;
		}

		// 获取任意一条路径的黑结点数量，这里选择最左路径
		size_t black_cnt = 0;
		Node* cur = root;
		while (cur != nullptr){
			if (cur->_color == BLACK){
				++black_cnt;
			}

			cur = cur->_left;
		}

		// 检测是否满足红黑树的性质，cnt用来记录路径中黑色结点的数量
		size_t cnt = 0;

		return _isRBTree(root, cnt, black_cnt);
	}

private:
	// 根节点
	Node* _root;
};

// 是不是红黑树
bool _isRBTree(Node* root, size_t cnt, size_t black_cnt){
	// 走到一条路径的尽头
	if (root == nullptr){
		// 判断黑色结点数是否相同
		if (cnt != black_cnt){
			cout << "违反性质四：每条路径中黑色结点的个数必须相同！" << endl;

			return false;
		}

		return true;
	}

	// 统计当前路径黑色结点数量
	if (root->_color == BLACK){
		++cnt;
	}

	// 检测当前结点与其双亲结点是否都是红色
	Node* parent = root->_parent;
	if (parent != nullptr && parent->_color == RED && root->_color == RED){
		cout << "违反性质三：没有连在一起的红色结点！" << endl;

		return false;
	}

	return _isRBTree(root->_left, cnt, black_cnt) &&
		_isRBTree(root->_right, cnt, black_cnt);
}

// 是不是红黑树
bool isRBTree(){
	Node* root = getRoot();

	// 空树是红黑树
	if (root == nullptr){
		return true;
	}

	// 检测根节点是否为黑色
	if (root->_color == BLACK){
		cout << "违反性质二：根结点必须为黑色！" << endl;

		return false;
	}

	// 获取任意一条路径的黑结点数量，这里选择最左路径
	size_t black_cnt = 0;
	Node* cur = root;
	while (cur != nullptr){
		if (cur->_color == BLACK){
			++black_cnt;
		}

		cur = cur->_left;
	}

	// 检测是否满足红黑树的性质，cnt用来记录路径中黑色结点的数量
	size_t cnt = 0;

	return _isRBTree(root, cnt, black_cnt);
}