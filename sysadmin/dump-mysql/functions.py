# -*- coding: UTF-8 -*-
import os

def create_log(file_name,content):
    if file_name!='' and content!='':
        f_log=open(file_name,"a+")
        f_log.write(content)
        f_log.close()
    else:
        print 'file name or content is empty !!!'
        
def del_file(file_name):
    if os.path.isfile(file_name):
	try:
	    os.remove(file_name)
	except:
	    pass

def check_file_size(path_file):
    size_file = 0
    if path_file!='':
        if os.path.isfile(path_file):
            
            size_file = os.path.getsize(path_file)
        else:
            print 'Path file is not a file : ',path_file
    else:
        print 'Path file is empty : ',path_file

    return size_file 
