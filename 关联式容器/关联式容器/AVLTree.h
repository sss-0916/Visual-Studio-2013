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

	// ƽ������
	int _bf;
	pair<K, V> _kv;
	// �ýڵ�˫��
	AVLTreeNode<K, V>* _parent;
	// �ýڵ�����
	AVLTreeNode<K, V>* _left;
	// �ýڵ��Һ���
	AVLTreeNode<K, V>* _right;
};

// AVL��
template<class K, class V>
class AVLTree{
	typedef AVLTreeNode<K, V> Node;

public:
	AVLTree()
		: _root(nullptr)
	{}

	// ����
	bool insert(const pair<K, V>& kv){
		// ������ֱ�Ӳ���
		if (_root == nullptr){
			_root = new Node(kv);
			_root->bf = 0;

			return true;
		}

		// ���游ָ��
		Node* parent = nullptr;
		Node* cur = _root;
		while (cur != nullptr){
			// ���ڸ��ڵ㣬������
			if (kv.first > cur->_kv.first){
				parent = cur;
				cur = cur->_right;
			}
			// С�ڸ��ڵ㣬������
			else if (kv.first < cur->_kv.first){
				parent = cur;
				cur = cur->_left;
			}
			// �Ѿ����ڣ�����ʧ��
			else{
				return false;
			}
		}

		// �ҵ�����λ��
		cur = new Node(kv);
		// �²������parent�󣬲��뵽parent����
		if (kv.first > parent->_kv.first){
			parent->_right = cur;
			cur->_parent = parent;
		}
		// �²������parentС�����뵽parent����
		else{
			parent->_left = cur;
			cur->_parent = parent;
		}

		// ����ƽ������
		while (parent){
			// �²�����parent��������ƽ�����Ӽ�1
			if (cur == parent->_right){
				++parent->_bf;
			}
			// �²�����parent��������ƽ�����Ӽ�1
			else{
				--parent->_bf;
			}

			// ƽ������Ϊ0���߶���Ӱ��
			if (parent->_bf == 0){
				break;
			}
			// ƽ������Ϊ1���߶ȱ��ˣ����ϸ���
			else if (abs(parent->_bf) == 1){
				cur = parent;
				parent = parent->_parent;
			}
			// ƽ�����Ӿ���ֵΪ2����ƽ�⣬��ת����
			else if (abs(parent->_bf) == 2){
				// ƽ������Ϊ2���������
				if (parent->_bf == 2){
					// ��ǰΪ1���½ڵ�����ڽϸ����������Ҳ࣬����
					if (cur->_bf == 1){
						leftRotate(parent);
					}
					// ��ǰΪ-1���½ڵ�����ڽϸ�����������࣬������
					else if (cur->_bf == -1){
						rightLeftRotate(parent);
					}
				}
				// ƽ������Ϊ-2���������
				else if (parent->_bf == -2){
					// ��ǰΪ-1���½ڵ�����ڽϸ�����������࣬�ҵ���
					if (cur->_bf == -1){
						rightRotate(parent);
					}
					// ��ǰΪ1���½ڵ�����ڽϸ����������Ҳ࣬���ҵ���
					else if (cur->_bf == 1){
						rightLeftRotate(parent);
					}
				}

				break;
			}
			// ƽ������Ϊ����ֵ������
			else{
				assert(false);
			}
		}
	}

	// �������
	void inorder(){
		_inOrder(_root);
		cout << endl;
	}

private:
	// �������ĸ߶�
	int _height(Node* root){
		if (root == nullptr){
			return 0;
		}

		if (root->_left == nullptr && root->_right == nullptr){
			return 1;
		}

		// �����߶�
		int left_height = _height(root->_left) + 1;
		// �����߶�
		int right_height = _height(root->_right) + 1;

		// ���������и߶ȵ����ֵΪ������ĸ߶�
		return left_height > right_height ? left_height : right_height;
	}

	// �Ƿ�ƽ��
	bool _isBalance(Node* root){
		// ������ƽ���
		if (root == nullptr){
			return true;
		}

		// ����ƽ������
		int left_height = _height(root->_left);
		int right_height = _height(root->_right);
		int bf = right_height - left_height;

		// �������ƽ�����Ӻ�root��ƽ�����Ӳ�ͬ
		// ����ƽ�����Ӿ���ֵ����1����ƽ��
		if (bf != root->_bf || abs(bf) > 1){
			return false;
		}

		// root�������������Ƿ�ƽ��
		return _isBalance(root->_left) && _isBalance(root->_right);
	}

	void _inorder(Node* root){
		_inorder(root->_left);
		cout << root->_kv.first << " ";
		_inorder(root->_right);
	}

	// �ҵ���
	void rightRotate(Node* parent){
		// 20��������10
		Node* subL = parent->_left;
		// 20��������������b
		Node* subLR = parent->_left->_right;

		// ��b�ҵ�20��������
		parent->_left = subLR;

		// ���b��Ϊ�գ���b��˫�׽��ָ��20���
		if (subLR){
			subLR->_parent = parent;
		}

		// ��20���ҵ�10��������
		subL->_right = parent;

		// pp����20����˫�׽��
		Node* pp = parent->_parent;
		// ��20����˫�׽���Ϊ10���
		parent->_parent = subL;

		// ���20����Ǹ��ڵ�
		if (pp == nullptr){
			// 10�����Ϊ���ڵ�
			_root = subL;
			_root->_parent = nullptr;
		}
		// 20��㲻�Ǹ��ڵ�
		else{
			// 20�������˫�׽���������
			if (pp->_left == parent){
				pp->_left = subL;
			}
			// 20�������˫�׽���������
			else{
				pp->_right = subL;
			}

			// 10����˫�׽���Ϊ20����˫�׽��
			subL->_parent = pp;
		}

		// ��ת��ɺ�ƽ�����Ӹ���Ϊ0
		parent->_bf = subL->_bf = 0;
	}

	// ����
	void leftRotate(Node* parent){
		// 10��������20
		Node* subR = parent->_right;
		// 10��������������b
		Node* subRL = parent->_right->_left;

		// ��b����Ϊ10��������
		parent->_right = subRL;

		// ���b�ǿգ���b�ĸ�������Ϊ10���
		if (subRL){
			subRL->_parent = parent;
		}

		// ����10���ĸ����
		Node* pp = parent->_parent;

		// ��10���ĸ��������Ϊ���20
		parent->_parent = subR;

		// ��10�������Ϊ���20������
		subR->_left = parent;

		// 10����Ǹ��ڵ�
		if (parent == _root){
			// 20�����Ϊ���ڵ�
			_root = subR;
			_root->_parent = nullptr;
		}
		// 10��㲻�Ǹ����
		else{
			// 10������丸��������
			if (parent == pp->_left){
				pp->_left = subR;
				subR->_parent = pp;
			}
			// 10������丸��������
			else{
				pp->_right = subR;
				subR->_parent = pp;
			}
		}

		// ����ƽ������
		parent->_bf = subR->_bf = 0;
	}

	// ����˫��
	void leftRightRotate(Node* parent){
		// ����20����ƽ�����ӣ���ת��ɺ�
		// ���ݸ�ƽ�����Ӷ�����ƽ�����ӽ��е���
		int bf = parent->_left->_right->_bf;

		// ��10�������������������
		leftRotate(parent->_left);

		// ��30��������������ҵ���
		rightRotate(parent);

		// �����20���ƽ������Ϊ1
		// ˵���²�������20����������˵��20��������߶Ƚϵ�
		// ������֮��20����������Ϊ10��������
		// �Ӷ�10����ƽ������Ϊ-1
		if (bf == 1){
			parent->_left->_bf = -1;
		}
		// �����20���ƽ������Ϊ-1
		// ˵���²�������20��������
		// 20���������߶Ƚϵ�
		// ������֮��20����������Ϊ30��������
		// �Ӷ�30����ƽ������Ϊ1
		else if (bf == -1){
			parent->_bf = 1;
		}
	}

	// ������
	void rightLeftRotate(Node* parent){
		// ���ȱ������֮��20����ƽ������
		int bf = parent->_right->_left->_bf;

		// �����ҵ���
		rightRotate(parent->_right);

		// ��������
		leftRotate(parent);

		// �½ڵ������c
		// b�ĸ߶Ƚϵ�Ϊh-1
		// ˫��֮��b���Ϊ10��������
		// ���10����ƽ������Ϊ-1
		if (bf == 1){
			parent->_bf = -1;
		}
		// �½ڵ������b
		// c�ĸ߶Ƚϵ�Ϊh-1
		// ˫��֮��c���Ϊ30��������
		// ���30����ƽ������Ϊ1
		else if (bf == -1){
			parent->_right->_bf = 1;
		}
	}

private:
	Node* _root;
};