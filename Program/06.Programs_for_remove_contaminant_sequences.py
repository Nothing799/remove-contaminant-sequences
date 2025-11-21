#!/usr/bin/env python

import sys
import os
from subprocess import *

if len(sys.argv) != 6:
    print('Usage: {0} invertebrates_hits.m6.txt non_invertebrates_hits.m6.txt gene.gff genome.fa output'.format(sys.argv[0]))
    raise SystemExit

script_dir = os.path.dirname(os.path.realpath(__file__))
#print('***',script_dir,'***')
find_tophit_py = script_dir + "\\01.find_tophit.py"
classify_genes_py = script_dir + "\\02.classify_genes.py"
gene2scaffold_infor_py = script_dir + "\\03.gene2scaffold.infor.py"
contaminate_gene_py = script_dir + "\\04.contaminate_gene.py"
#print('***',classify_genes_py,'***')
assert os.path.exists(find_tophit_py),"01.find_tophit.py executable not found"
assert os.path.exists(classify_genes_py),"02.classify_genes.py executable not found"
assert os.path.exists(gene2scaffold_infor_py),"03.gene2scaffold.infor.py executable not found"
assert os.path.exists(contaminate_gene_py),"04.contaminate_gene.py executable not found"
#print('***',sys.argv[3],'***')
invertebrates_hits = sys.argv[1]
non_invertebrates_hits = sys.argv[2]
gene_gff = sys.argv[3]
genome = sys.argv[4]
output_dir = sys.argv[5]

invertebrates_hits_tophit = output_dir + "\\01.invertebrates_hits.tophit.txt"
non_invertebrates_hits_tophit = output_dir + "\\01.non_invertebrates_hits.tophit.txt"
integrated_tophit = output_dir + "\\01.integrated_tophit.txt"

cmd = '{0} "{1}" "{2}" "{3}" "{4}" "{5}"'.format(find_tophit_py, invertebrates_hits, non_invertebrates_hits,invertebrates_hits_tophit,non_invertebrates_hits_tophit,integrated_tophit)
#print('***',cmd,'***')
print('Find blast hit ...')
Popen(cmd, shell = True, stdout = PIPE).communicate()

gene_group_1 = output_dir + "\\02.GeneGroup1.id"
gene_group_2 = output_dir + "\\02.GeneGroup2.id"
gene_group_3 = output_dir + "\\02.GeneGroup3.id"

cmd = '{0} "{1}" "{2}" "{3}" "{4}"'.format(classify_genes_py, integrated_tophit,gene_group_1,gene_group_2,gene_group_3)
#print('***',cmd,'***')
print('Identify genes in three groups ...')
Popen(cmd, shell = True, stdout = PIPE).communicate()

gene2scaffold_infor_result = output_dir + "\\03.gene2scaffold.infor.result.txt"

cmd = '{0} "{1}" "{2}" "{3}" "{4}" "{5}"'.format(gene2scaffold_infor_py, gene_gff, gene_group_1, gene_group_2, gene_group_3, gene2scaffold_infor_result)
print('Identify genes in three groups ...')
Popen(cmd, shell = True, stdout = PIPE).communicate()

contaminate_gene_delete = output_dir + "\\04.contaminate_gene.delete.txt"
contaminate_gene_check = output_dir + "\\04.contaminate_gene.check.txt"

cmd = '{0} "{1}" "{2}" "{3}"'.format(contaminate_gene_py, gene2scaffold_infor_result, contaminate_gene_delete, contaminate_gene_check)
print('Identify genes in three groups ...')
Popen(cmd, shell = True, stdout = PIPE).communicate()
'''
DdB_genome_contaminate_resultt = output_dir + "\05.DdB_genome_contaminate_result.txt"
DdB_genome_result = output_dir + "\05.DdB_genome_result.txt"

cmd = '{0} "{1}" "{2}" "{3}"'.format(filter.py, gene2scaffold_infor_result, contaminate_gene_delete, contaminate_gene_check)
print('Identify genes in three groups ...')
Popen(cmd, shell = True, stdout = PIPE).communicate()
'''
print('End of programs.')


