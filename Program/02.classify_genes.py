##!/usr/bin/env python

import sys
import os
from subprocess import *

if len(sys.argv) != 5:
    print('Usage: {0} 01.integrated_tophit.txt 02.GeneGroup1.id 02.GeneGroup2.id 02.GeneGroup3.id'.format(sys.argv[0]))
    raise SystemExit

integrated_tophit = sys.argv[1]
GeneGroup1 = sys.argv[2]
GeneGroup2 = sys.argv[3]
GeneGroup3 = sys.argv[4]

import os#文件操作
ans1 = ''
ans2 = ''
ans3 = ''
outfile1 = open (GeneGroup1, 'w')
outfile2 = open (GeneGroup2, 'w')
outfile3 = open (GeneGroup3, 'w')
with open(integrated_tophit, 'r') as infile :
    next(infile)#跳过标题行
    for line in infile :
        line = line.strip()
        line_list = line.split('\t')
        if(line_list[2] != '--' and line_list[4] != '--' and line_list[2] != '0.0') :
            t = float(line_list[4])/float(line_list[2])
            if(t < 1e-50) :
                outfile1.write(line_list[0][4:] + '\n')#ans1 = ans1 + line_list[0] + '\n'直接写入，不然会超时
            else :
                outfile3.write(line_list[0][4:] + '\n')
        elif(line_list[2] == '--' and line_list[4] != '--') :
            outfile2.write(line_list[0][4:] + '\n')#ans2 += ans2 + line_list[0] + '\n'
        else :
            outfile3.write(line_list[0][4:] + '\n')#ans3 += ans3 + line_list[0] + '\n'
outfile1.close()
outfile2.close()
outfile3.close()

