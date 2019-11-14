#include "file_scan_module.h"

void FileScanModule::listDir(const std::string& path, 
		std::vector<std::string>& subfiles,
		std::vector<std::string>& subdirs){
	_finddata_t file;

	// 要遍历的目录
	std::string path_ = path + "\\*.*";

	intptr_t handle = _findfirst(path_.c_str(), &file);
	if (handle == -1){
		cout << "_findfirst error" << endl;
		return;
	}

	do {
		// 判断是否为目录文件
		if (file.attrib & _A_SUBDIR){
			// 判断是否为.或..
			if ((strcmp(file.name, ".") != 0) && 
				(strcmp(file.name, "..") != 0)){
				//subdirs.push_back(path + "\\" + file.name);
				subdirs.push_back(file.name);
			}
		}
		else{
			//subfiles.push_back(path + "\\" + file.name);
			subfiles.push_back(file.name);
		}
	} while (_findnext(handle, &file) == 0);

	// 结束搜索
	_findclose(handle);
}

void FileScanModule::fileScan(const std::string& path){
	std::vector<std::string> subfiles;
	std::vector<std::string> subdirs;

	std::string sql;

	listDir(path, subfiles, subdirs);

	// 本地目录下的文件
	std::set<std::string> localset;
	localset.insert(subfiles.begin(), subfiles.end());
	localset.insert(subdirs.begin(), subdirs.end());

	// 数据库中的文件
	std::set < std::string> dbset;
	_dm.GetDocs(path, dbset);

	auto localit = localset.begin();
	auto dbit = dbset.begin();
	while (localit != localset.end() && dbit != dbset.end()){
		// 本地有，数据库中没有
		if (*localit < *dbit){
			_dm.InsertTab(path, *localit);

			++localit;
		}
		// 数据库有，本地没有
		else if (*localit > *dbit){
			_dm.DeleteTab(path, *dbit);

			++dbit;
		}
		// 都有
		else{
			++localit;
			++dbit;
		}
	}

	// 本地有，数据库没有
	while (localit != localset.end()){
		_dm.InsertTab(path, *localit);

		++localit;
	}

	// 本地没有，数据库有
	while (dbit != dbset.end()){
		_dm.DeleteTab(path, *dbit);

		++dbit;
	}

	// 递归遍历
	//for (const auto& e : subdirs){
	for (size_t i = 0; i < subdirs.size(); ++i){
		std::string subpath = path;
		subpath += "\\";
		subpath += subdirs[i];
		//subpath += e;
		//listDir(subpath, subfiles, subdirs);
		fileScan(subpath);
		//fileScan(subpath);
		//listDir(e, subfiles, subdirs);
		//listDir(subdirs[i], subfiles, subdirs);
		//cout << subdirs[i] << endl;
		//cout << e << endl;
	}

	// 文件打印
	//cout << "files: " << subfiles.size() << endl;
	//for (const auto& e : subfiles){
	//	cout << e << endl;
	//}

	//cout << endl;

	// 目录打印
	//cout << "dirs: " << subdirs.size() << endl;
	//for (const auto& e : subdirs){
	//	cout << e << endl;
	//}

	//std::set<std::string>::iterator sit = localset.begin();
	//while (sit != localset.end()){
	//	cout << *sit << endl;

	//	++sit;
	//}
	//cout << endl;
}