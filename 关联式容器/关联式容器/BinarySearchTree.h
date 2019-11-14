#pragma once

// 二叉搜索树结点
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

// 二叉搜索树
template<class K, class V>
class BSTree{
	typedef BSTreeNode<K, V> Node;

public:
	BSTree()
		: _root(nullptr)
	{}

	~BSTree(){
		// 二叉搜索树的释放
		_release(_root);
	}

	// 二叉树的中序遍历
	void inorder(){
		_inorder(_root);

		cout << endl;
	}

	// 二叉搜索树的查找
	Node* find(const K& key){
		return _find(key);
	}

	// 二叉搜索树的插入
	bool insert(const pair<K, V>& kv){
		return _insert(kv);
	}

	// 二叉搜索树的删除
	bool remove(const K& key){
		return _remove(key);
	}

private:
	// 释放
	void _release(Node* root){
		// 该树非空
		if (root){
			// 保存左右孩子
			Node* left = root->_left;
			Node* right = root->_right;

			// 释放根
			delete root;

			// 左树非空，释放左树
			if (left){
				_release(left);
			}

			// 右树非空，释放右树
			if (right){
				_release(right);
			}
		}
	}

	// 中序遍历
	void _inorder(Node* root){
		// 递归出口
		if (root == nullptr){
			return;
		}

		_inorder(root->_left);
		cout << root->_kv.first << " ";
		_inorder(root->_right);
	}

	// 查找
	Node* _find(const K& key){
		Node* cur = _root;

		while (cur != nullptr){
			// 比根结点大，去右子树找
			if (key > cur->_kv.first){
				cur = cur->_right;
			}
			// 比根结点小，去左子树找
			else if (key < cur->_kv.first){
				cur = cur->_left;
			}
			// 相等
			else{
				break;
			}
		}

		return cur;
	}

	// 插入
	bool _insert(const pair<K, V>& kv){
		// 树为空
		if (_root == nullptr){
			_root = new Node(kv);

			return true;
		}
		// 树不为空
		else{
			Node* cur = _root;
			// 保存父节点
			Node* parent = nullptr;

			while (cur != nullptr){
				parent = cur;

				// 比根结点大，去右子树
				if (kv.first > cur->_kv.first){
					cur = cur->_right;
				}
				// 比根结点小，去左子树
				else if (kv.first < cur->_kv.first){
					cur = cur->_left;
				}
				// 和根结点一样，已存在，插入失败
				else{
					return false;
				}
			}

			// 新插入结点
			cur = new Node(kv);

			// 比双亲结点大，插入到右树
			if (kv.first > parent->_kv.first){
				parent->_right = cur;
			}
			// 比双亲结点小，插入到左树
			else{
				parent->_left = cur;
			}

			return true;
		}
	}

	// 删除
	bool _remove(const K& key){
		Node* cur = _root;
		// 保存父结点
		Node* parent = nullptr;

		while (cur != nullptr){
			// 比根结点大，右树找
			if (key > cur->_kv.first){
				parent = cur;
				cur = cur->_right;
			}
			// 比根结点小，左树找
			else if (key < cur->_kv.first){
				parent = cur;
				cur = cur->_left;
			}
			// 找到了
			else{
				// 该节点左树为空
				if (cur->_left == nullptr){
					// 该节点为根结点
					if (parent == nullptr){
						_root = cur->_right;
					}
					else{
						// 该节点在父结点的右树
						if (cur->_kv.first > parent->_kv.first){
							parent->_right = cur->_right;
						}
						// 该节点在父结点的左树
						else{
							parent->_left = cur->_right;
						}
					}
				}
				// 该节点右树为空
				else if (cur->_right == nullptr){
					// 该节点为根结点
					if (parent == nullptr){
						_root = cur->_left;
					}

					// 该节点在父结点的右树
					if (cur->_kv.first > parent->_kv.first){
						parent->_right = cur->_left;
					}
					// 该节点在父结点的右树
					else{
						parent->_left = cur->_right;
					}
				}
				// 该节点左右树都不为空
				else{
					// 右树中寻找替代结点
					Node* replace = cur->_right;
					// 保存替代结点的父结点
					Node* rparent = cur;

					// 寻找最左结点，即右树中的最小值
					while (replace->_left){
						rparent = replace;
						replace = replace->_left;
					}

					cur->_kv = replace->_kv;
					cur = replace;

					// 判断replace是否有左树
					// replace有左树
					if (rparent->_left == replace){
						// 将替代结点的右树连到替代结点的父结点的左树
						rparent->_left = replace->_right;
					}
					// replace没有左树
					else{
						// 将替代结点的右树连到替代结点的父结点的右树
						rparent->_right = replace->_right;
					}
				}

				// 删除替代结点
				delete cur;

				return true;
			}
		}
		return false;
	}

private:
	Node* _root;
};