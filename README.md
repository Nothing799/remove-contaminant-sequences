## Before running the programs, please decompress the gzip files (in 'example', i.e., 'gene.gff.gz', 'invertebrates_hits.m6.txt.gz', 'non_invertebrates_hits.m6.txt.gz').
## remove-contaminant-sequences, under Windows system
1. The python script 'Programs_for_remove_contaminant_sequences.Windows.py' is used for remove contaminant sequences.
Running:
python Programs_for_remove_contaminant_sequences.Windows.py <invertebrates_hits.m6.txt> <non_invertebrates_hits.m6.txt> <gene.gff> <output dir>

2. Example:
python D:\Program\Programs_for_remove_contaminant_sequences.Windows.py invertebrates_hits.m6.txt non_invertebrates_hits.m6.txt gene.gff D:\Program\example

## remove-contaminant-sequences, under Linux system
# step 1 
python 01.find_tophit.py invertebrates_hits.m6.txt non_invertebrates_hits.m6.txt 01.invertebrates_hits.tophit.txt 01.non_invertebrates_hits.tophit.txt 01.integrated_tophit.txt

# step 2
python 02.classify_genes.py 01.integrated_tophit.txt 02.GeneGroup1.id 02.GeneGroup2.id 02.GeneGroup3.id

# step 3
python 03.gene2scaffold.infor.py gene.gff 02.GeneGroup1.id 02.GeneGroup2.id 02.GeneGroup3.id 03.gene2scaffold.infor.result.txt

# step 4
python 04.contaminate_gene.py 03.gene2scaffold.infor.result.txt 04.scaffold.delete.txt 04.scaffold.check.txt
