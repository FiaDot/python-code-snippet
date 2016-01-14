#!/usr/bin/python
# -*- coding: utf-8 -*-

# visual studio EUC-KR 로 저장된 소스 파일을 UTF-8로 변환
# iconv -f EUC-KR -t UTF-8 filepath > filepath

__author__ = "LEE GUNHO"
__email__ ="fiadot@gmail.com"


import os
import sys
import shutil
import codecs
import io


def findInFiles():		
	for dirname, dirnames, filenames in os.walk('.'):
	    for subdirname in dirnames:
	        name = os.path.join(dirname, subdirname)
	    for filename in filenames:
	        convFile(os.path.join(dirname, filename))
	       	
def convFile(filepath):
	if not filepath.lower().endswith(('.h', '.cpp', '.c')):
		return
	
	print(filepath)

	with codecs.open(filepath, "r",encoding='euc-kr') as r:
		data = r.readlines()

	with codecs.open(filepath, "wb", encoding="utf-8") as w:
		w.writelines(data)

	pass


def main():
	findInFiles()


if __name__ == '__main__':
    main()




