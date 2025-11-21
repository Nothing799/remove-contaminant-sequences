#过滤污染的scaffold
import os
fasta = "DdB_genome.fa"#fasta = input("fa")
ID = "05.filter_ID.txt"#ID = input("ID")
result1 = "DdB_genome_non_contaminate_result.txt"#result1 = input("result")
result2 = "DdB_genome_contaminate_result.txt"#result2 = input("result")
content = []
index = 1
tag = ''
outfile1 = open(result1,'w')
outfile2 = open(result2,'w')
with open(ID,'r') as IDfile :
    next(IDfile)
    for line in IDfile :
        content.append(line)#没有对ID文件和fasta文件进行strip(),因为一行只有一个元素，所以直接比较 可以省去strip和'\n'
with open(fasta,'r') as infile :
    for line in infile :
        if(index%2 != 0) :
            if(line[1:] not in content) :
                outfile1.write(line)
            else :
                outfile2.write(line)
                tag = 'contaminate'
        else :
            if(tag != 'contaminate') :
                outfile1.write(line)
            else :
                outfile2.write(line)
                tag = ''
        '''if(index%2 != 0) :
            if(line[1:] not in content) :
                outfile1.write(line)
            else :
                outfile2.write(line)'''
        index += 1
            
outfile1.close()
outfile2.close()
