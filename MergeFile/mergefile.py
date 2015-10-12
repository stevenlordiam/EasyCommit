# -*- coding: utf-8 -*- 

import os
root = './pic'
a=os.walk(root)
for x in a:
    if len(x[-1])>0 and '.jpg' in x[-1][0]: 
        pre=os.path.basename(x[0])
        for j in x[-1]:
            os.rename(x[0]+'/'+j, root+'/'+pre+'_'+j)
