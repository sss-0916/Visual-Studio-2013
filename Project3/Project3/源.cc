// ͨ����ǰλ���ҵ����ڵ�λ��
static int nextP[4][2] = {
		{ -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }
};

class Solution {
public:
	// ��Χ������
	void DFS(vector<vector<char>>& board, int x, int y, int row, int col){
		// ���û�б�'x'Χ�Ƶ�'o'Ϊ'#'
		board[x][y] = '#';

		// ��һ��λ������
		int newX = 0;
		int newY = 0;

		// ����������
		for (int i = 0; i < 4; ++i){
			int newX = x + nextP[i][0];
			int newY = y + nextP[i][1];

			// Խ��
			if (newX >= row || newX < 0 || newY >= col || newY < 0){
				continue;
			}

			// ��Χ��'o'�����еݹ����
			if (board[newX][newY] == 'o'){
				DFS(board, newX, newY, row, col);
			}
		}
	}

	void solve(vector<vector<char>>& board) {
		if (board.empty()){
			return;
		}

		// ��ȡ����
		int row = board.size();
		int col = board[0].size();

		// ��һ�к����һ��
		for (int i = 0; i < row; ++i){
			if (board[i][0] == 'o'){
				DFS(board, i, 0, row, col);
			}

			if (board[i][col - 1] == 'o'){
				DFS(board, i, row - 1, row, col);
			}
		}

		// ��һ�к����һ��
		for (int i = 0; i < col; ++i){
			if (board[0][i] == 'o'){
				DFS(board, 0, i, row, col);
			}

			if (board[row - 1][i] == 'o'){
				DFS(board, col - 1, i, row, col);
			}
		}

		// ��'o'��Ϊ'x'�������'#'��Ϊ'o'
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