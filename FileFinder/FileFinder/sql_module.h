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

	// �����ݿ�
	void Open(const std::string& path);

	// �ر����ݿ�
	void Close();

	// ִ��SQL���
	void ExecSql(const std::string& sql);

	// ��ȡ������Ϣ
	void getTable(const std::string& sql,
		int& row, int& col, char**& ret);

	SqlModule(const SqlModule&) = delete;

	SqlModule& operator=(const SqlModule&) = delete;

private:
	// ���ݿ����
	sqlite3* _db;
};

// RAII�Զ��ͷ�sqlite_get_table���ٵ��ڴ�
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

	// ��ȡ���ݿ��еı��������set��
	void GetDocs(const std::string path, 
		std::set<std::string>& docs);

	// ���в�������
	void InsertTab(const std::string path, 
		const std::string& doc);

	// ����ɾ������
	void DeleteTab(const std::string path, 
		const std::string& doc);

	// ����
	void SearchTab(const std::string& key, 
		std::vector<std::pair<std::string, std::string>>& doc_paths);

	// �ؼ����з�
	static void SplitResult(const std::string& str, const std::string& key,
		std::string& prefix, std::string& key_word, std::string& suffix);

private:
	// ��ʼ���������ݿ⣬����
	void Init();

private:
	SqlModule _sm;
};

// ʹ��������ɫ��ʾ�ı�
static void ColourPrintf(const char* str){
	// 0-�� 1-�� 2-�� 3-ǳ�� 4-�� 5-�� 6-�� 7-�� 8-�� 9-���� 10-����
	// 11-��ǳ�� 12-���� 13-���� 14-���� 15-����
	//��ɫ��ǰ��ɫ + ����ɫ*0x10 
	//���磺���Ǻ�ɫ������ɫ�ǰ�ɫ���� ��ɫ + ���� = 4 + 15*0x10 
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