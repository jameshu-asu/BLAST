import pandas as pd
import os
import csv
from Adeno_helper import *

#By James C. Hu

pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

'''
1.  qseqid      query or source (gene) sequence id
2.  sseqid      subject or target (reference genome) sequence id
3.  evalue      expect value (the number of expected hits of similar quality(score) that could be found just by chance)
                e.g. "E-value of 10 means that up to 10 hits can be expected to be found just by chance, given the same size of a random database"
                Smaller E-Value = better the match.
4.  bitscore    bit score (the required size of a sequence database in which the current match could be found just by chance. Bit-score is log base 2 scaled and normalized raw-score.)
                e.g. "Each incrase by one doubles the required database size (2^bit-score)"
5.  pident      percentage of identical positions
6.  nident      Number of identical matches
7.  qcovs       Query Coverage Per Subject
8.  length      alignment length (sequence overlap)
9.  mismatch    number of mismatches
10. qlen        Query sequence length
11. slen        Subject sequence length

Source : https://www.metagenomics.wiki/tools/blast/blastn-output-format-6
'''


df_out = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5, 6, 7, 8])

file_list = [file for file in os.listdir() if file.endswith('output')]

for file in file_list:
    df_in = pd.DataFrame(blastn_adeno_out(file)).T
    df_out = pd.concat([df_out, df_in])

df_out = df_out.rename(columns={0: 'Seq_ID', 1: 'Total_mapped_reads', 2: 'HAdV_A18', 3: 'HAdV_B3', 4: 'HAdV_C5', 5: 'HAdV_D8', 6: 'HAdV_E4', 7: 'HAdV_F40', 8: 'HAdV_G52'}).set_index('Seq_ID')

df_out.to_csv('HAdV_output_230103_230424.csv')
