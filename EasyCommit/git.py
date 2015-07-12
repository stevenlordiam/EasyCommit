import sys, os
from subprocess import call

path = sys.argv[1]
message = sys.argv[2:]

os.chdir("/Users/liuwenyue/Dropbox/github/"+path)
# change to directory to your git directory

call('git add -A', shell=True)
call("git commit -m \""+ " ".join(message)+"\"", shell=True)

call('git push origin master', shell=True)