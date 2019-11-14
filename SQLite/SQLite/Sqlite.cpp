#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>

#pragma comment(lib,"sqlite3.lib")

int main()
{
	sqlite3 *db;
	char *zErrMsg = 0;
	const char* data = "Callback function called";

	// 连接数据库
	sqlite3_open("lab330.db", &db);

	// SQL语句，创建表
	char* create_tb = "create table student ("\
		"id int unsigned primary key,"\
		"name varchar(20) not null,"\
		"hometown varchar(128) not null"\
		");";

	// 创建表
	sqlite3_exec(db, create_tb, nullptr, nullptr, &zErrMsg);

	// SQL语句，插入表
	char* insert_tab = "insert into student values"\
		"(1, 'Fan', 'ShanDong'),"\
		"(2, 'Lin', 'HeBei'),"\
		"(3, 'Niu', 'JiangSu');";

	// 插入数据
	sqlite3_exec(db, insert_tab, nullptr, nullptr, &zErrMsg);

	// SQL语句，更新表
	char* update_tab = "update student set name = 'F' where name = 'Fan';"\
		"update student set name = 'L' where name = 'Lin';"\
		"update student set name = 'N' where name = 'Niu';";

	// 更新数据
	sqlite3_exec(db, update_tab, nullptr, nullptr, &zErrMsg);

	// SQL语句，删除数据
	char* delete_tab = "delete from student where name = 'L';"\
		"delete from student where name = 'N';";

	// 删除数据
	sqlite3_exec(db, delete_tab, nullptr, nullptr, &zErrMsg);

	// SQL语句，查询
	char* select_tab = "select * from student;";

	char** result = nullptr;
	int row, col;
	sqlite3_get_table(db, select_tab, &result, &row, &col, nullptr);

	// 结果打印
	for (int i = 0; i <= row; ++i){
		printf("%s\t", result[i * col + 0]);
		printf("%s\t", result[i * col + 1]);
		printf("%s\n", result[i * col + 2]);
	}

	// 空间释放
	sqlite3_free_table(result);

	// 关闭数据库
	sqlite3_close(db);

	system("pause");
	return 0;
}