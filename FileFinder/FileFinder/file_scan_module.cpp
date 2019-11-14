#include "file_scan_module.h"

void FileScanModule::listDir(const std::string& path, 
		std::vector<std::string>& subfiles,
		std::vector<std::string>& subdirs){
	_finddata_t file;

	// Ҫ������Ŀ¼
	std::string path_ = path + "\\*.*";

	intptr_t handle = _findfirst(path_.c_str(), &file);
	if (handle == -1){
		cout << "_findfirst error" << endl;
		return;
	}

	do {
		// �ж��Ƿ�ΪĿ¼�ļ�
		if (file.attrib & _A_SUBDIR){
			// �ж��Ƿ�Ϊ.��..
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

	// ��������
	_findclose(handle);
}

void FileScanModule::fileScan(const std::string& path){
	std::vector<std::string> subfiles;
	std::vector<std::string> subdirs;

	std::string sql;

	listDir(path, subfiles, subdirs);

	// ����Ŀ¼�µ��ļ�
	std::set<std::string> localset;
	localset.insert(subfiles.begin(), subfiles.end());
	localset.insert(subdirs.begin(), subdirs.end());

	// ���ݿ��е��ļ�
	std::set < std::string> dbset;
	_dm.GetDocs(path, dbset);

	auto localit = localset.begin();
	auto dbit = dbset.begin();
	while (localit != localset.end() && dbit != dbset.end()){
		// �����У����ݿ���û��
		if (*localit < *dbit){
			_dm.InsertTab(path, *localit);

			++localit;
		}
		// ���ݿ��У�����û��
		else if (*localit > *dbit){
			_dm.DeleteTab(path, *dbit);

			++dbit;
		}
		// ����
		else{
			++localit;
			++dbit;
		}
	}

	// �����У����ݿ�û��
	while (localit != localset.end()){
		_dm.InsertTab(path, *localit);

		++localit;
	}

	// ����û�У����ݿ���
	while (dbit != dbset.end()){
		_dm.DeleteTab(path, *dbit);

		++dbit;
	}

	// �ݹ����
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

	// �ļ���ӡ
	//cout << "files: " << subfiles.size() << endl;
	//for (const auto& e : subfiles){
	//	cout << e << endl;
	//}

	//cout << endl;

	// Ŀ¼��ӡ
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