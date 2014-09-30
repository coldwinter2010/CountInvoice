# -*- coding: cp936 -*-
#检查最大可能凑的发票
import os
def getMax(rawdatalist,target):
    datalist=rawdatalist[:]
    if len(datalist)==0:
        return [0]
    if len(datalist)==1:
        if datalist[0]>target:
            return [0]
        else:
            return [datalist[0],datalist[0]]
    #大于1
    lastData=datalist.pop()
    if lastData>target:
        tmp=getMax(datalist,target)
        return tmp
    else:
        tmp1=getMax(datalist,target)
        tmp11=tmp1[0]
        tmp2=getMax(datalist,target-lastData);
        tmp22=lastData+tmp2[0]
        if tmp11>tmp22:
            return tmp1
        else:
            tmp2[0]=tmp22
            tmp2.insert(1,lastData)
            return tmp2
print '请输入要凑的最大额度'
tar=int(raw_input())
print '目标是:',tar
print '请输入现有的发票钱数，用空格隔开'
src=raw_input()
data=[]
max=0
srcList=src.split(' ')
for i in srcList:
    data.append(float(i))
out=getMax(data,tar)
print '凑出来：',out
