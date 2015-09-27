#!/usr/bin/python

import sys, os
from subprocess import call

def get_current_folder_size(folder): 	# recursion
	total_size = os.path.getsize(folder)
	for item in os.listdir(folder):
		itempath = os.path.join(folder, item)
		if os.path.isfile(itempath):
			total_size += os.path.getsize(itempath)
		elif os.path.isdir(itempath):
			total_size += get_current_folder_size(itempath)
	return total_size

file_size = get_current_folder_size("~/Dropbox/.dropbox.cache")

if(file_size > 1024**3): # 1G cache size limit
	call('rm -r ~/Dropbox/.dropbox.cache', shell=True)
else:
	print "No need to clean cache"