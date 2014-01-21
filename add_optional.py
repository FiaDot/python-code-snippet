#!/usr/bin/python
# -*- coding: utf-8 -*-
# *dao.java 에 대해 @Select 다음 줄에 @Options(flushCache=true) 추가
# TODO : import org.apache.ibatis.annotations.Options; 없으면 추가 하는 것도 필요.

import os
import sys
import shutil

def check_file_name(filepath):
    if not filepath.endswith("Dao.java"):
        return ""
    print(filepath)        


    backup_file_name = filepath.rsplit('.', 1)[0] + '.bak'
    shutil.copy(filepath, backup_file_name)

    output_data = []
    with open(filepath, "r") as f:        
        data = f.readlines()
        
        for line in data:
            try:
                output_data.append(line)
                
                if "@Select" in line:                    
                    add_line = "\t@Options(flushCache=true)\n"
                    output_data.append(add_line)
            except ValueError:
                pass

 
    with open(filepath, "w") as f:
        f.writelines(output_data)
        

   
for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        name = os.path.join(dirname, subdirname)
    for filename in filenames:
        output = check_file_name(os.path.join(dirname, filename))
        if "" != output:
            print(output)
