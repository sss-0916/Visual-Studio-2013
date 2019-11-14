#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
	int openLock(vector<string>& deadends, string target) {
		// 将死亡数字放入HashSet
		unordered_set<string> deadNum(deadends.begin(), deadends.end());

		// 死亡数字是"0000"
		if (deadNum.find("0000") != deadNum.end()){
			return -1;
		}

		queue<string> q;
		q.push("0000");

		// 保存拨动的次数
		int step = 0;

		while (!q.empty()){
			// 转一次得到的可能性的数量
			int qsz = q.size();

			while (qsz--){
				string cur = q.front();
				q.pop();

				for (size_t i = 0; i < cur.size(); ++i){
					string temp1 = cur;
					string temp2 = cur;

					// 向上拨
					temp1[i] = temp1[i] == '0' ? '9' : temp1[i] - 1;
					// 向下拨
					temp2[i] = temp2[i] == '9' ? '0' : temp2[i] + 1;

					if (temp1 == target || temp2 == target){
						return step + 1;
					}

					// 拨到死亡数字
					if (deadNum.find(temp1) != deadNum.end()
						|| deadNum.find(temp2) != deadNum.end()){
						return -1;
					}

					q.push(temp1);
					q.push(temp2);
				}
			}

			++step;
		}

		return step;
	}
};

int main(){

	vector<string> vs;
	vs.push_back("0201");
	vs.push_back("0101");
	vs.push_back("0102");
	vs.push_back("1212");
	vs.push_back("2002");

	string target = "0202";

	Solution sol;
	int ret = sol.openLock(vs, target);

	cout << ret << endl;
	
	system("pause");
	return 0;
}