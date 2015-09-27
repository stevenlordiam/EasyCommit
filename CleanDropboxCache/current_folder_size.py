#!/usr/bin/python

import os

def get_current_folder_size(folder): 	# recursion
	total_size = os.path.getsize(folder)
	for item in os.listdir(folder):
		itempath = os.path.join(folder, item)
		if os.path.isfile(itempath):
			total_size += os.path.getsize(itempath)
		elif os.path.isdir(itempath):
			total_size += get_current_folder_size(itempath)
	return total_size

file_size = get_current_folder_size(".")

if(file_size > 0 and file_size < 1024):
	print "Size: " + "%.2lf" % (file_size) + " B"
elif(file_size > 1024 and file_size < 1024*1024):
	print "Size: " + "%.2lf" % (file_size/1024.0) + " K"
elif(file_size > 1024*1024 and file_size < 1024*1024*1024):
	print "Size: " + "%.2lf" % (file_size/1024.0/1024.0) + " M"
elif(file_size > 1024*1024*1024 and file_size < 1024*1024*1024*1024):
	print "Size: " + "%.2lf" % (file_size/1024.0/1024.0/1024.0) + " G"