# -*- coding: utf-8 -*- 

import os
root = './pic'
a=os.walk(root)
for x in a:
    if len(x[-1])>0 and '.jpg' in x[-1][0]:  #分离出最后一级目录名，如Australia  
        pre=os.path.basename(x[0])
        for j in x[-1]:
            #将Australia/1.jpg生成新的文件名Australia_1.jpg
            #再将win7walls/Australia/1.jpg移动到
              #win7walls/Australia_1.jpg，注意没有使用
              #shutil.move，因为它是基于复制的，同盘的移动文件
              #效率很低，而os.rename对于同盘文件的移动相当快
              #其实它就是更改了一下文件属性
            os.rename(x[0]+'/'+j, root+'/'+pre+'_'+j)

# http://blog.csdn.net/thy38/article/details/4496810