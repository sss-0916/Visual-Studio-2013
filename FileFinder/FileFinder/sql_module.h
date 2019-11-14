#pragma once

#include <sqlite3.h>
#include <string>
#include <set>
#include <vector>
#include <windows.h>

#pragma comment(lib, "sqlite3.lib")

class SqlModule{
public:
	SqlModule()
		: _db(nullptr)
	{}

	~SqlModule(){
		Close();
	}

	// 打开数据库
	void Open(const std::string& path);

	// 关闭数据库
	void Close();

	// 执行SQL语句
	void ExecSql(const std::string& sql);

	// 获取表中信息
	void getTable(const std::string& sql,
		int& row, int& col, char**& ret);

	SqlModule(const SqlModule&) = delete;

	SqlModule& operator=(const SqlModule&) = delete;

private:
	// 数据库对象
	sqlite3* _db;
};

// RAII自动释放sqlite_get_table开辟的内存
class AutoGetDocs{
public:
	AutoGetDocs(char** tab)
		: _tab(tab)
	{}

	~AutoGetDocs(){
		sqlite3_free_table(_tab);
	}

private:
	AutoGetDocs(const AutoGetDocs&) = delete;

	AutoGetDocs& operator=(const AutoGetDocs&) = delete;

private:
	char** _tab;
};

class DataModule{
public:
	DataModule(){
		_sm.Open("document.db");

		Init();
	}

	// 获取数据库中的表，将其放入set中
	void GetDocs(const std::string path, 
		std::set<std::string>& docs);

	// 表中插入数据
	void InsertTab(const std::string path, 
		const std::string& doc);

	// 表中删除数据
	void DeleteTab(const std::string path, 
		const std::string& doc);

	// 搜索
	void SearchTab(const std::string& key, 
		std::vector<std::pair<std::string, std::string>>& doc_paths);

	// 关键字切分
	static void SplitResult(const std::string& str, const std::string& key,
		std::string& prefix, std::string& key_word, std::string& suffix);

private:
	// 初始化，打开数据库，建表
	void Init();

private:
	SqlModule _sm;
};

// 使用特殊颜色显示文本
static void ColourPrintf(const char* str){
	// 0-黑 1-蓝 2-绿 3-浅绿 4-红 5-紫 6-黄 7-白 8-灰 9-淡蓝 10-淡绿
	// 11-淡浅绿 12-淡红 13-淡紫 14-淡黄 15-亮白
	//颜色：前景色 + 背景色*0x10 
	//例如：字是红色，背景色是白色，即 红色 + 亮白 = 4 + 15*0x10 
	WORD color = 4 + 15 * 0x10;
	WORD colorOld;
	HANDLE handle = ::GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_SCREEN_BUFFER_INFO csbi;
	GetConsoleScreenBufferInfo(handle, &csbi);
	colorOld = csbi.wAttributes;
	SetConsoleTextAttribute(handle, color);
	printf("%s", str);
	SetConsoleTextAttribute(handle, colorOld);
}