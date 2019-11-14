#define _CRT_SECURE_NO_WARNINGS

#include "sql_module.h"
#include "file_scan_module.h"
#include <iostream>
#include <vector>

using std::cout;
using std::endl;

void SqlModule::Open(const std::string& path){
	sqlite3_open(path.c_str(), &_db);
	//int ret = sqlite3_open(path.c_str(), &_db);
	//if (ret){
	//	fprintf(stderr, "Can't open database: %s\n", 
	//		sqlite3_errmsg(_db));
	//	exit(0);
	//}
	//else{
	//	fprintf(stderr, "Opened database successfully\n");
	//}
}

void SqlModule::Close(){
	sqlite3_close(_db);
}

void SqlModule::ExecSql(const std::string& sql){
	//char* zErrMsg = nullptr;

	int ret = sqlite3_exec(_db, sql.c_str(), 
		nullptr, nullptr, nullptr);

	//int ret = sqlite3_exec(_db, sql.c_str(), 
	//	nullptr, nullptr, &zErrMsg);
	//if (ret != SQLITE_OK){
	//	fprintf(stderr, "SQL error: %s\n", zErrMsg);
	//	sqlite3_free(zErrMsg);
	//}
	//else{
	//	fprintf(stdout, "Table created successfully\n");
	//}
}

void SqlModule::getTable(const std::string& sql,
	int& row, int& col, char**& ret){

	//char* zErrMsg;
	// 表的查询
	sqlite3_get_table(_db, sql.c_str(), &ret, 
		&row, &col, nullptr);
	//cout << "hehe" << endl;
	//std::cout << zErrMsg << endl;
	//cout << "hehe" << endl;

	//int ret = sqlite3_exec(_db, sql.c_str(), 
	//	row, col, &zErrMsg);
}

void DataModule::Init(){
	//Open("document.db");

	std::string sql = "create table doc("\
		"id integer primary key autoincrement,"\
		"path_name text,"\
		"file_name text,"\
		"file_pinyin text,"\
		"file_initial text"\
		");";

	_sm.ExecSql(sql);
}

void DataModule::GetDocs(const std::string path, 
	std::set<std::string>& docs){
	char sql[256] = { 0 };

	// 表中查找
	sprintf(sql, "select file_name from doc "\
		"where path_name = '%s';", path.c_str());

	char** ret = nullptr;
	int row = 0;
	int col = 0;

	// 查表
	_sm.getTable(sql, row, col, ret);

	// 资源托管
	AutoGetDocs agd(ret);

	// 跳过第一行，第一行为表头
	for (int i = 1; i <= row; ++i){
		docs.insert(ret[i * col + 0]);
		//docs.insert(ret[i * col + 1]);
	}

	// 资源释放
	//sqlite3_free_table(ret);
}

void DataModule::InsertTab(const std::string path, 
	const std::string& doc){
	char sql[256] = { 0 };

	// 拼音
	std::string pinyin = ChineseConvertPinYinAllSpell(doc);

	// 首字母
	std::string initial = ChineseConvertPinYinInitials(doc);

	// 表中插入数据
	sprintf(sql, "insert into doc("\
		"path_name, file_name, file_pinyin, file_initial"\
		") values('%s', '%s', '%s', '%s');",
		path.c_str(), doc.c_str(), pinyin.c_str(), initial.c_str());

	_sm.ExecSql(sql);
}

void DataModule::DeleteTab(const std::string path, 
	const std::string& doc){
	char sql[256] = { 0 };

	// 表中删除数据
	sprintf(sql, "delete from doc where"\
		" path_name = '%s' and file_name = '%s';",
		path.c_str(), doc.c_str());

	_sm.ExecSql(sql);

	std::string subpath = path;
	subpath += "\\";
	subpath += doc;

	// 若目录被删除，则删除目录下的所有文件
	sprintf(sql, "delete from doc where path_name = '%s';",
		subpath.c_str());

	_sm.ExecSql(sql);
}

void DataModule::SearchTab(const std::string& key,
	std::vector<std::pair<std::string, std::string>>& doc_paths){
	char sql[256];

	std::string key_pinyin = ChineseConvertPinYinAllSpell(key);
	std::string key_initial = ChineseConvertPinYinInitials(key);

	// 模糊匹配
	sprintf(sql, "select file_name, path_name from doc "\
		"where file_pinyin like '%%%s%%' or file_initial like '%%%s%%'", 
		key_pinyin.c_str(), key_initial.c_str());

	char** ret = nullptr;
	int row = 0;
	int col = 0;

	// 获得结果
	_sm.getTable(sql, row, col, ret);

	// 将结果放入vector
	for (int i = 1; i <= row; ++i){
		doc_paths.push_back(std::make_pair(ret[i * col + 0],
			ret[i * col + 1]));
	}
}

void DataModule::SplitResult(const std::string& str, const std::string& key,
	std::string& prefix, std::string& key_word, std::string& suffix){

	// key为源串中的关键字
	{
		size_t pos = str.find(key);
		if (pos != std::string::npos){
			prefix = str.substr(0, pos);
			key_word = str.substr(pos, key.size());
			suffix = str.substr(pos + key.size(), std::string::npos);

			return;
		}
	}

	// key关键字拼音
	{
		// 字符串和关键字转拼音
		std::string str_pinyin = ChineseConvertPinYinAllSpell(str);
		std::string key_pinyin = ChineseConvertPinYinAllSpell(key);

		size_t pos = str_pinyin.find(key_pinyin);
		if (pos != std::string::npos){
			char chinese[3] = { 0 };

			size_t end = pos + key_pinyin.size();
			size_t pinyin_i = 0;
			size_t str_i = 0;
			size_t key_start = 0;

			while (pinyin_i < end){
				if (pinyin_i == pos){
					key_start = str_i;
				}

				if (str[str_i] >= 0 && str[str_i] <= 127){
					++str_i;
					++pinyin_i;
				}
				else{
					chinese[0] = str[str_i];
					chinese[1] = str[str_i + 1];

					std::string word = ChineseConvertPinYinAllSpell(chinese);
					pinyin_i += word.size();
					str_i += 2;
				}
			}

			prefix = str.substr(0, key_start);
			key_word = str.substr(key_start, str_i - key_start);
			suffix = str.substr(str_i, std::string::npos);

			return;
		}
	}

	// key为关键字首字母
	{
		// 字符串和关键字转首字母
		std::string str_initial = ChineseConvertPinYinInitials(str);
		std::string key_initial = ChineseConvertPinYinInitials(key);

		size_t pos = str_initial.find(key_initial);
		if (pos != std::string::npos){
			size_t end = pos + key_initial.size();
			size_t str_i = 0;
			size_t initial_i = 0;
			size_t key_start = 0;

			while (initial_i < end){
				if (initial_i == pos){
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

			return;
		}
	}

	prefix = str;
	return;
}