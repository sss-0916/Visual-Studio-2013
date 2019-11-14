#define _CRT_SECURE_NO_WARNINGS

#include "file_scan_module.h"
#include "sql_module.h"
#include <thread>
#include <stdlib.h>

using std::cout;
using std::endl;

void fileScanTest(){
	FileScanModule fsm;

	while (1){
		fsm.fileScan("C:\\Users\\Administrator\\Desktop\\CSDN");

		// 线程休眠3s
		std::this_thread::sleep_for(std::chrono::seconds(3));
	}
	//fsm.fileScan("C:\\Users\\Administrator\\Desktop\\奖学金");
}

void sqlModuleTest(){
	//DataModule dm;

	SqlModule sm;

	sm.Open("document.db");

	std::string sql = "create table doc("\
		"id integer primary key autoincrement,"\
		"path_name text,"\
		"file_name text"\
		");";

	sm.ExecSql(sql);

	char sql_str[256];
	sprintf(sql_str, "insert into doc(path_name, file_name) "\
		"values('%s', '%s');", "hehe", "haha");
	//std::string insert_sql = "insert into doc"\
	//  "(path_name, file_name) values(hehe, haha);";

	//cout << sql_str << endl;
	sm.ExecSql(sql_str);

	sprintf(sql_str, "select path_name, "\
		"file_name from doc;");

	//cout << sql_str << endl;

	char** ret = nullptr;
	int row, col;
	sm.getTable(sql_str, row, col, ret);

	cout << row << endl;
	cout << col << endl;

	for (int i = 1; i < row; ++i){
		cout << ret[i * col] << "\t";
		cout << i << "\t";
		cout << ret[i * col + 1] << endl;
	}

	//sm.Init();

	sm.Close();
}

void searchTest(){
	DataModule dm;

	// 关键字
	std::string key;
	// 搜索结果
	std::vector<std::pair<std::string, std::string>> result;

	cout << "========================================="\
			"========================================="\
			"===========" << endl;

	while (1){
		cout << "请输入要搜索的关键字：";

		std::cin >> key;

		result.clear();

		dm.SearchTab(key, result);

		printf("%-50s %-50s\n", "文件", "目录");

		// 输出搜索结果
		for (const auto& e : result){
			//cout << e.first << " " << e.second << endl;
			//printf("%-50s", e.first.c_str());
			std::string prefix, key_word, suffix;
			dm.SplitResult(e.first, key, prefix, key_word, suffix);
			//printf("%-50s %-50s\n", "文件", "目录");
			cout << prefix;
			ColourPrintf(key_word.c_str());
			cout << suffix;
			for (size_t i = e.first.size(); i <= 50; ++i){
				cout << " ";
			}

			printf("%-50s\n", e.second.c_str());
		}

		cout << "========================================="\
				"========================================="\
				"===========" << endl;
	}
}

void chineseToPinyinTest(){
	std::string s = "拣尽寒枝不肯栖，寂寞沙洲冷。";

	cout << ChineseConvertPinYinAllSpell(s) << endl;
	cout << ChineseConvertPinYinInitials(s) << endl;
}

void highLightTest(){
	std::string str = "我是张蒙蒙你是谁啊？";
	//ColourPrintf(str.c_str());

#if 0
	// 输入关键字是中文
	{
		std::string key = "张蒙蒙";

		std::string prefix, suffix, key_word;

		size_t pos = str.find(key.c_str());
		if (pos != std::string::npos){

			prefix = str.substr(0, pos);
			key_word = str.substr(pos, pos + key.size() - pos);
			suffix = str.substr(pos + key.size(), std::string::npos);

			//cout << suffix << endl;
			cout << prefix;
			ColourPrintf(key_word.c_str());
			cout << suffix << endl;
		}
	}
#endif

#if 0
	// 输入关键字是拼音
	{
		std::string key = "zhangmengmeng";
		std::string prefix, key_word, suffix;

		// 将源串转为拼音
		std::string str_pinyin = ChineseConvertPinYinAllSpell(str);
		std::string key_pinyin = ChineseConvertPinYinAllSpell(key);

		//cout << key_pinyin << endl;
		//cout << str_pinyin << endl;

		size_t pos = str_pinyin.find(key_pinyin);
		//cout << pos << endl;
		if (pos != std::string::npos){
			char chinese[3] = { 0 };

			size_t start = pos;
			size_t end = pos + key_pinyin.size();
			size_t pinyin_i = 0;
			size_t str_i = 0;
			size_t key_start = 0;
			//size_t key_end = 0;

			while (pinyin_i < end){
				if (pinyin_i == start){
					//prefix = str.substr(0, str_i);
					key_start = str_i;
				}

				// 判断是否为ascii
				if (str[str_i] >= 0 && str[str_i] <= 127){
					++str_i;
					++pinyin_i;
				}
				else{
					chinese[0] = str[str_i];
					chinese[1] = str[str_i + 1];

					// 将单个汉字转为拼音
					std::string word = ChineseConvertPinYinAllSpell(chinese);

					pinyin_i += word.size();
					str_i += 2;
					//++str_i;
				}
			}

			prefix = str.substr(0, key_start);
			key_word = str.substr(key_start, str_i - key_start);
			suffix = str.substr(str_i, std::string::npos);

			cout << prefix << endl;
			cout << key_word << endl;
			cout << suffix << endl;
		}
	}
#endif

	{
		std::string key = "zmm";
		std::string prefix, key_word, suffix;

		// 将源串转为首字母
		std::string str_initial = ChineseConvertPinYinInitials(str);
		std::string key_initial = ChineseConvertPinYinInitials(key);

		size_t pos = str_initial.find(key_initial);
		if (pos != std::string::npos){
			size_t start = pos;
			size_t end = pos + key_initial.size();
			size_t str_i = 0;
			size_t initial_i = 0;
			size_t key_start = 0;

			while (initial_i < end){
				if (initial_i == start){
					key_start = str_i;
				}

				if (str[str_i] >= 0 && str[str_i] <= 127){
					++str_i;
					++initial_i;
				}
				else{
					str_i += 2;
					++initial_i;
				}
			}

			prefix = str.substr(0, key_start);
			key_word = str.substr(key_start, str_i - key_start);
			suffix = str.substr(str_i, std::string::npos);

			cout << prefix;
			ColourPrintf(key_word.c_str());
			cout << suffix << endl;
		}
	}
}

void fileFinderTest(){
	std::thread t1(fileScanTest);
	t1.detach();

	searchTest();
}

int main(){

	//fileFinderTest();

	//fileScanTest();

	//fileScanTest();

	//sqlModuleTest();

	searchTest();

	//chineseToPinyinTest();

	//highLightTest();
	
	system("pause");
	return 0;
}