#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>

#pragma comment(lib,"sqlite3.lib")

int main()
{
	sqlite3 *db;
	char *zErrMsg = 0;
	const char* data = "Callback function called";

	// �������ݿ�
	sqlite3_open("lab330.db", &db);

	// SQL��䣬������
	char* create_tb = "create table student ("\
		"id int unsigned primary key,"\
		"name varchar(20) not null,"\
		"hometown varchar(128) not null"\
		");";

	// ������
	sqlite3_exec(db, create_tb, nullptr, nullptr, &zErrMsg);

	// SQL��䣬�����
	char* insert_tab = "insert into student values"\
		"(1, 'Fan', 'ShanDong'),"\
		"(2, 'Lin', 'HeBei'),"\
		"(3, 'Niu', 'JiangSu');";

	// ��������
	sqlite3_exec(db, insert_tab, nullptr, nullptr, &zErrMsg);

	// SQL��䣬���±�
	char* update_tab = "update student set name = 'F' where name = 'Fan';"\
		"update student set name = 'L' where name = 'Lin';"\
		"update student set name = 'N' where name = 'Niu';";

	// ��������
	sqlite3_exec(db, update_tab, nullptr, nullptr, &zErrMsg);

	// SQL��䣬ɾ������
	char* delete_tab = "delete from student where name = 'L';"\
		"delete from student where name = 'N';";

	// ɾ������
	sqlite3_exec(db, delete_tab, nullptr, nullptr, &zErrMsg);

	// SQL��䣬��ѯ
	char* select_tab = "select * from student;";

	char** result = nullptr;
	int row, col;
	sqlite3_get_table(db, select_tab, &result, &row, &col, nullptr);

	// �����ӡ
	for (int i = 0; i <= row; ++i){
		printf("%s\t", result[i * col + 0]);
		printf("%s\t", result[i * col + 1]);
		printf("%s\n", result[i * col + 2]);
	}

	// �ռ��ͷ�
	sqlite3_free_table(result);

	// �ر����ݿ�
	sqlite3_close(db);

	system("pause");
	return 0;
}