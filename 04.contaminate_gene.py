##!/usr/bin/env python

import sys
import os
from subprocess import *

if len(sys.argv) != 4:
    print('Usage: {0} 03.gene2scaffold.infor.result.txt 04.contaminate_gene.delete.txt 04.contaminate_gene.check.txt'.format(sys.argv[0]))
    raise SystemExit

gene2scaffold_infor = sys.argv[1]
contaminate_gene_delete = sys.argv[2]
contaminate_gene_check = sys.argv[3]

import os

infor = {}
infor12 = {}
infor3 = {}
result1 = 'scaffold\tn\tgeneID\n'
result2 = 'seqID\n'

with open(gene2scaffold_infor, 'r') as infile :
    next(infile)#跳过标题行
    for line in infile :
        line = line.strip()
        line_list = line.split('\t')
        tag = infor.get(line_list[1],'not_found')
        if(tag == 'not_found') :
            infor12[line_list[1]] = [0]#1+2,geneID,0,[0],'0'
            infor[line_list[1]] = 1
        else :
            infor[line_list[1]] += 1
        if(line_list[0] == line_list[2] or line_list[0] == line_list[3]) :
            infor12[line_list[1]][0] += 1
            infor12[line_list[1]].append(line_list[0])
        tag = infor3.get(line_list[1],'not_found')
        if(tag == 'not_found') :
            infor3[line_list[1]] = [0]
        if(line_list[0] == line_list[4]) :
            infor3[line_list[1]][0] += 1
            infor3[line_list[1]].append(line_list[4])
            
for i in infor.keys() :
    if(infor12[i][0]/infor[i] >= 0.5) :
        result1 += i + '\t' + str(infor[i]) + '\t' + ','.join(infor12[i][1:])+ '\n'
    elif(infor12[i][0]/infor[i] < 0.5 and (infor12[i][0] +infor3[i][0])/infor[i] >=0.5) :
        result2 += i + '\n'

with open(contaminate_gene_delete, 'w') as outfile1,open(contaminate_gene_check, 'w') as outfile2 :
    outfile1.write(result1)
    outfile2.write(result2)
            
