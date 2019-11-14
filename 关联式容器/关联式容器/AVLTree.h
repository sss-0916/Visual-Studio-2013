#pragma once

template<class K, class V>
struct AVLTreeNode{

	AVLTreeNode(const pair<K, V>& kv)
		: _bf(0)
		, _kv(kv)
		, _parent(nullptr)
		, _left(nullptr)
		, _right(nullptr)
	{}

	// 平衡因子
	int _bf;
	pair<K, V> _kv;
	// 该节点双亲
	AVLTreeNode<K, V>* _parent;
	// 该节点左孩子
	AVLTreeNode<K, V>* _left;
	// 该节点右孩子
	AVLTreeNode<K, V>* _right;
};

// AVL树
template<class K, class V>
class AVLTree{
	typedef AVLTreeNode<K, V> Node;

public:
	AVLTree()
		: _root(nullptr)
	{}

	// 插入
	bool insert(const pair<K, V>& kv){
		// 空树，直接插入
		if (_root == nullptr){
			_root = new Node(kv);
			_root->bf = 0;

			return true;
		}

		// 保存父指针
		Node* parent = nullptr;
		Node* cur = _root;
		while (cur != nullptr){
			// 大于根节点，右树找
			if (kv.first > cur->_kv.first){
				parent = cur;
				cur = cur->_right;
			}
			// 小于根节点，左树找
			else if (kv.first < cur->_kv.first){
				parent = cur;
				cur = cur->_left;
			}
			// 已经存在，插入失败
			else{
				return false;
			}
		}

		// 找到插入位置
		cur = new Node(kv);
		// 新插入结点比parent大，插入到parent右树
		if (kv.first > parent->_kv.first){
			parent->_right = cur;
			cur->_parent = parent;
		}
		// 新插入结点比parent小，插入到parent左树
		else{
			parent->_left = cur;
			cur->_parent = parent;
		}

		// 调整平衡因子
		while (parent){
			// 新插入在parent的右树，平衡因子加1
			if (cur == parent->_right){
				++parent->_bf;
			}
			// 新插入在parent的左树，平衡因子减1
			else{
				--parent->_bf;
			}

			// 平衡因子为0，高度无影响
			if (parent->_bf == 0){
				break;
			}
			// 平衡因子为1，高度变了，向上更新
			else if (abs(parent->_bf) == 1){
				cur = parent;
				parent = parent->_parent;
			}
			// 平衡因子绝对值为2，不平衡，旋转调整
			else if (abs(parent->_bf) == 2){
				// 平衡因子为2，右树变高
				if (parent->_bf == 2){
					// 当前为1，新节点插入在较高右子树的右侧，左单旋
					if (cur->_bf == 1){
						leftRotate(parent);
					}
					// 当前为-1，新节点插入在较高右子树的左侧，右左单旋
					else if (cur->_bf == -1){
						rightLeftRotate(parent);
					}
				}
				// 平衡因子为-2，左树变高
				else if (parent->_bf == -2){
					// 当前为-1，新节点插入在较高左子树的左侧，右单旋
					if (cur->_bf == -1){
						rightRotate(parent);
					}
					// 当前为1，新节点插入在较高左子树的右侧，左右单旋
					else if (cur->_bf == 1){
						rightLeftRotate(parent);
					}
				}

				break;
			}
			// 平衡因子为其他值，出错
			else{
				assert(false);
			}
		}
	}

	// 中序遍历
	void inorder(){
		_inOrder(_root);
		cout << endl;
	}

private:
	// 计算树的高度
	int _height(Node* root){
		if (root == nullptr){
			return 0;
		}

		if (root->_left == nullptr && root->_right == nullptr){
			return 1;
		}

		// 左树高度
		int left_height = _height(root->_left) + 1;
		// 右树高度
		int right_height = _height(root->_right) + 1;

		// 左树右树中高度的最大值为这棵树的高度
		return left_height > right_height ? left_height : right_height;
	}

	// 是否平衡
	bool _isBalance(Node* root){
		// 空树是平衡的
		if (root == nullptr){
			return true;
		}

		// 计算平衡因子
		int left_height = _height(root->_left);
		int right_height = _height(root->_right);
		int bf = right_height - left_height;

		// 计算出的平衡因子和root的平衡因子不同
		// 或者平衡因子绝对值超过1，不平衡
		if (bf != root->_bf || abs(bf) > 1){
			return false;
		}

		// root的左树和右树是否平衡
		return _isBalance(root->_left) && _isBalance(root->_right);
	}

	void _inorder(Node* root){
		_inorder(root->_left);
		cout << root->_kv.first << " ";
		_inorder(root->_right);
	}

	// 右单旋
	void rightRotate(Node* parent){
		// 20结点的左树10
		Node* subL = parent->_left;
		// 20结点的左树的右树b
		Node* subLR = parent->_left->_right;

		// 将b挂到20结点的左树
		parent->_left = subLR;

		// 如果b不为空，将b的双亲结点指向20结点
		if (subLR){
			subLR->_parent = parent;
		}

		// 将20结点挂到10结点的右树
		subL->_right = parent;

		// pp保存20结点的双亲结点
		Node* pp = parent->_parent;
		// 将20结点的双亲结点改为10结点
		parent->_parent = subL;

		// 如果20结点是根节点
		if (pp == nullptr){
			// 10结点设为根节点
			_root = subL;
			_root->_parent = nullptr;
		}
		// 20结点不是根节点
		else{
			// 20结点是其双亲结点的左子树
			if (pp->_left == parent){
				pp->_left = subL;
			}
			// 20结点是其双亲结点的右子树
			else{
				pp->_right = subL;
			}

			// 10结点的双亲结点改为20结点的双亲结点
			subL->_parent = pp;
		}

		// 旋转完成后，平衡因子更新为0
		parent->_bf = subL->_bf = 0;
	}

	// 左单旋
	void leftRotate(Node* parent){
		// 10结点的右树20
		Node* subR = parent->_right;
		// 10结点的右树的左树b
		Node* subRL = parent->_right->_left;

		// 将b设置为10结点的右树
		parent->_right = subRL;

		// 如果b非空，将b的父亲设置为10结点
		if (subRL){
			subRL->_parent = parent;
		}

		// 保存10结点的父结点
		Node* pp = parent->_parent;

		// 将10结点的父结点设置为结点20
		parent->_parent = subR;

		// 将10结点设置为结点20的左树
		subR->_left = parent;

		// 10结点是根节点
		if (parent == _root){
			// 20结点设为根节点
			_root = subR;
			_root->_parent = nullptr;
		}
		// 10结点不是根结点
		else{
			// 10结点是其父结点的左树
			if (parent == pp->_left){
				pp->_left = subR;
				subR->_parent = pp;
			}
			// 10结点是其父结点的右树
			else{
				pp->_right = subR;
				subR->_parent = pp;
			}
		}

		// 调整平衡因子
		parent->_bf = subR->_bf = 0;
	}

	// 左右双旋
	void leftRightRotate(Node* parent){
		// 保存20结点的平衡因子，旋转完成后
		// 根据该平衡因子对其他平衡因子进行调整
		int bf = parent->_left->_right->_bf;

		// 对10结点所在子树进行左单旋
		leftRotate(parent->_left);

		// 对30结点所在树进行右单旋
		rightRotate(parent);

		// 插入后20结点平衡因子为1
		// 说明新插入结点在20结点的右树，说明20结点左树高度较低
		// 左右旋之后，20结点的左树成为10结点的右树
		// 从而10结点的平衡因子为-1
		if (bf == 1){
			parent->_left->_bf = -1;
		}
		// 插入后20结点平衡因子为-1
		// 说明新插入结点在20结点的左树
		// 20结点的右树高度较低
		// 左右旋之后，20结点的右树成为30结点的左树
		// 从而30结点的平衡因子为1
		else if (bf == -1){
			parent->_bf = 1;
		}
	}

	// 右左旋
	void rightLeftRotate(Node* parent){
		// 首先保存插入之后20结点的平衡因子
		int bf = parent->_right->_left->_bf;

		// 进行右单旋
		rightRotate(parent->_right);

		// 进行左单旋
		leftRotate(parent);

		// 新节点插入在c
		// b的高度较低为h-1
		// 双旋之后，b会成为10结点的右树
		// 因此10结点的平衡因子为-1
		if (bf == 1){
			parent->_bf = -1;
		}
		// 新节点插入在b
		// c的高度较低为h-1
		// 双旋之后，c会成为30结点的左树
		// 因此30结点的平衡因子为1
		else if (bf == -1){
			parent->_right->_bf = 1;
		}
	}

private:
	Node* _root;
};