##!/usr/bin/env python

import sys
import os
from subprocess import *

if len(sys.argv) != 6:
    print('Usage: {0} invertebrates_hits.m6.txt non_invertebrates_hits.m6.txt 01.invertebrates_hits.tophit.txt 01.non_invertebrates_hits.tophit.txt 01.integrated_tophit.txt'.format(sys.argv[0]))
    raise SystemExit

invertebrates_hits = sys.argv[1]
non_invertebrates_hits = sys.argv[2]
invertebrates_hits_tophit = sys.argv[3]
non_invertebrates_hits_tophit = sys.argv[4]
integrated_tophit = sys.argv[5]

def find_blast_tophit(f) :#（1）
    infor={}
    e_value={}
    result = ''
    for line in f.readlines() :#读取所有行并放入列表 可以不用readline()
        line = line.replace('\n','')
        line_list = line.split('\t')#直接操作
        line_list[10] = float(line_list[10])
        tag = infor.get(line_list[0],'not_found')
        if(tag == 'not_found') :
            infor[line_list[0]] = line_list
            e_value[line_list[0]] = line_list[10]
        else :
            if(line_list[10] < e_value[line_list[0]]) :#(2)
                e_value[line_list[0]] = line_list[10]
                infor[line_list[0]] = line_list
    for i in infor.values() :
        i[10] = str(i[10])
        line = '\t'.join(i)#文件写入内容必须是字符串
        result += line
        result += '\n'
    return result       

file1 = open(invertebrates_hits, "r")#("04.txt", "r")
file2 = open(non_invertebrates_hits, "r")#句柄

file = open(invertebrates_hits_tophit,'w')
file.write(find_blast_tophit(file1))
file.close()

file = open(non_invertebrates_hits_tophit,'w')
file.write(find_blast_tophit(file2))
file.close()

file1.close()
file2.close()

ans = {}
result = 'Query\tinvertebrates-Sbjct\tE-value\tvertebrates-Sbjct\tE-value\t\n'
file1_1 = open(invertebrates_hits_tophit, "r")
file2_1 = open(non_invertebrates_hits_tophit, "r")#句柄
for line in file1_1.readlines() :
        line = line.replace('\n','')
        line_list = line.split('\t')
        ans[line_list[0]] = line_list[0] + "\t" + line_list[1] + "\t" + line_list[10] + "\t--\t--"

for line in file2_1.readlines() :
        line = line.replace('\n','')
        line_list = line.split('\t')
        tag = ans.get(line_list[0],'not_found')
        if(tag == 'not_found') :#(4)
            ans[line_list[0]] = line_list[0] + "\t--\t--\t" + line_list[1] + "\t" + line_list[10]
        else :
            ans[line_list[0]] = ans[line_list[0]].rstrip("--\t")
            ans[line_list[0]] = ans[line_list[0]] + "\t"  + line_list[1] + "\t" + line_list[10]#(5)
            #extend接受一个可迭代对象作为参数
            #并将可迭代对象的每个元素追加到列表的末尾
            #append会将整个列表作为1个元素放进去

file1_1.close()
file2_1.close()
for i in ans.values() :
    #line = '\t'.join(i)#文件写入内容必须是字符串
    result += i
    result += '\n'
file3 = open(integrated_tophit,'w')
file3.write(result)
file3.close()
