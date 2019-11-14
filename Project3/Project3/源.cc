// 通过当前位置找到相邻的位置
static int nextP[4][2] = {
		{ -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }
};

class Solution {
public:
	// 被围绕区域
	void DFS(vector<vector<char>>& board, int x, int y, int row, int col){
		// 标记没有别'x'围绕的'o'为'#'
		board[x][y] = '#';

		// 下一个位置坐标
		int newX = 0;
		int newY = 0;

		// 上下左右找
		for (int i = 0; i < 4; ++i){
			int newX = x + nextP[i][0];
			int newY = y + nextP[i][1];

			// 越界
			if (newX >= row || newX < 0 || newY >= col || newY < 0){
				continue;
			}

			// 周围有'o'，进行递归遍历
			if (board[newX][newY] == 'o'){
				DFS(board, newX, newY, row, col);
			}
		}
	}

	void solve(vector<vector<char>>& board) {
		if (board.empty()){
			return;
		}

		// 获取行列
		int row = board.size();
		int col = board[0].size();

		// 第一列和最后一列
		for (int i = 0; i < row; ++i){
			if (board[i][0] == 'o'){
				DFS(board, i, 0, row, col);
			}

			if (board[i][col - 1] == 'o'){
				DFS(board, i, row - 1, row, col);
			}
		}

		// 第一行和最后一行
		for (int i = 0; i < col; ++i){
			if (board[0][i] == 'o'){
				DFS(board, 0, i, row, col);
			}

			if (board[row - 1][i] == 'o'){
				DFS(board, col - 1, i, row, col);
			}
		}

		// 将'o'改为'x'，将标记'#'改为'o'
		for (int i = 0; i < row; ++i){
			for (int j = 0; j < col; ++j){
				if (board[i][j] == 'o'){
					board[i][j] == 'x';
				}

				if (board[i][j] == '#'){
					board[i][j] = 'o';
				}
			}
		}
	}
};