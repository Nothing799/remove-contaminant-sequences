##!/usr/bin/env python

import sys
import os
from subprocess import *
import re

if len(sys.argv) != 6:
    print('Usage: {0} gene.gff 02.GeneGroup1.id 02.GeneGroup2.id 02.GeneGroup3.id 03.gene2scaffold.infor.result.txt'.format(sys.argv[0]))
    raise SystemExit

DdB_gene_file = sys.argv[1]
id1_file = sys.argv[2]
id2_file = sys.argv[3]
id3_file = sys.argv[4]
gene2scaffold_infor = sys.argv[5]

result = "GeneID\tSeqID\tGeneGroup1\tGeneGroup2\tGeneGroup3\n"
ID1 = []
ID2 = []
ID3 = []

with open(id1_file, 'r') as id1 ,open(id2_file, 'r') as id2 ,open(id3_file, 'r') as id3 :
    for line in id1 :
        line = line.strip()
        ID1.append(line)
    for line in id2 :
        line = line.strip()
        ID2.append(line)
    for line in id3 :
        line = line.strip()
        ID3.append(line)

with open(DdB_gene_file, 'r') as infile :
    for line in infile :
        line = line.strip()  
        line_list = line.split('\t')
        if(line_list[2] == 'gene') :
            t = re.split(r':|;',line_list[8])
            result += t[1] + '\t' + line_list[0] + '\t'
            if(t[1] in ID1) :
                result += t[1] + '\t'
            else :
                result += '--\t'
            if(t[1] in ID2) :
                result += t[1] + '\t'
            else :
                result += '--\t'
            if(t[1] in ID3) :
                result += t[1]
            else :
                result += '--'
            result += '\n'

with open(gene2scaffold_infor, 'w') as outfile:
    outfile.write(result)
