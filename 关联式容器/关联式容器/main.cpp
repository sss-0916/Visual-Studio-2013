#include <iostream>
#include <stdlib.h>
using namespace std;
#include "BinarySearchTree.h"
#include "AVLTree.h"
#include "RBTree.h"

void testBSTree(){
	BSTree<int, int> bst;

	bst.insert(make_pair(1, 1));
	bst.insert(make_pair(2, 2));
	bst.insert(make_pair(3, 3));
	bst.insert(make_pair(4, 4));

	bst.inorder();

	bst.remove(4);
	bst.inorder();
}

int main(){

	testBSTree();

	system("pause");
	return 0;
}