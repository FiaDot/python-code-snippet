#!/usr/bin/python
# -*- coding: utf-8 -*-
# CSV 파일에 대한 SQL 변환 툴

# Input [ mapping file, csv file ] -> output [sql]

import sys
import os


def is_exist_map_file(map_file_name):
  if os.path.isdir(map_file_name):
    print("Exist!")
    return True
  else:
    print("Not exist!")
    return False


def build_map_file(map_file_name):
  map_file = open(map_file_name, 'w')
  map_file.write('test')
  map_file.close()


def build_output_sql_file(sql_file_name):
  sql_file = open(sql_file_name, 'w')
  sql_file.write('sql')
  sql_file.close()




print(sys.argv)

# 입력 받기!
# name = input("Input:")
# print(name)


csv_file_name = 'SkillTable.csv'
file_name = csv_file_name.rsplit('.', 1)[0]

map_file_name = file_name + '.map'

print("only file_name=" + file_name)
print("map_file_name=" + map_file_name)

if is_exist_map_file(map_file_name): 
  build_output_sql_file(sql_file_name)
else:
  build_map_file(map_file_name)





'''
import csv
with open(csv_file_name, newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
       print(', '.join(row))


txtfile = open("file", "r")
print(txtfile.read(1))
print(txtfile.readline())
print(txtfile.readline(5))
txtfile.close()
'''

# input("Press any key:")
