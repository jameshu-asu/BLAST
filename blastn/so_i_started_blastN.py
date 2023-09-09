import os
import subprocess
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')

seq_list = [i for i in df['Seq_ID']]

os.chdir('fastas')

custom_fasta_list = [file for seq in seq_list for file in os.listdir() if seq in file]
# all_fasta_list = [file for file in os.listdir() if file.endswith('.fasta')]


os.chdir('../')

fasta_command_list1 = [command for i in np.array_split([i for i in custom_fasta_list], 5)[0] if (command := ['blastn', '-db', 'HAdV_db', '-query', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/fastas/{i}', '-evalue', '1e-3', '-num_threads', '32', '-max_target_seqs', '1', '-max_hsps', '1', '-outfmt', '6 qseqid sseqid evalue bitscore pident nident qcovs length mismatch qlen slen', '-out', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/output/{i.split("_")[0]}_blastn_output'])]
fasta_command_list2 = [command for i in np.array_split([i for i in custom_fasta_list], 5)[1] if (command := ['blastn', '-db', 'HAdV_db', '-query', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/fastas/{i}', '-evalue', '1e-3', '-num_threads', '32', '-max_target_seqs', '1', '-max_hsps', '1', '-outfmt', '6 qseqid sseqid evalue bitscore pident nident qcovs length mismatch qlen slen', '-out', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/output/{i.split("_")[0]}_blastn_output'])]
fasta_command_list3 = [command for i in np.array_split([i for i in custom_fasta_list], 5)[2] if (command := ['blastn', '-db', 'HAdV_db', '-query', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/fastas/{i}', '-evalue', '1e-3', '-num_threads', '32', '-max_target_seqs', '1', '-max_hsps', '1', '-outfmt', '6 qseqid sseqid evalue bitscore pident nident qcovs length mismatch qlen slen', '-out', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/output/{i.split("_")[0]}_blastn_output'])]
fasta_command_list4 = [command for i in np.array_split([i for i in custom_fasta_list], 5)[3] if (command := ['blastn', '-db', 'HAdV_db', '-query', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/fastas/{i}', '-evalue', '1e-3', '-num_threads', '32', '-max_target_seqs', '1', '-max_hsps', '1', '-outfmt', '6 qseqid sseqid evalue bitscore pident nident qcovs length mismatch qlen slen', '-out', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/output/{i.split("_")[0]}_blastn_output'])]
fasta_command_list5 = [command for i in np.array_split([i for i in custom_fasta_list], 5)[4] if (command := ['blastn', '-db', 'HAdV_db', '-query', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/fastas/{i}', '-evalue', '1e-3', '-num_threads', '32', '-max_target_seqs', '1', '-max_hsps', '1', '-outfmt', '6 qseqid sseqid evalue bitscore pident nident qcovs length mismatch qlen slen', '-out', f'/mnt/storage/wastewater_analysis/HAdV_fastaFiles/output/{i.split("_")[0]}_blastn_output'])]

procs1 = [subprocess.Popen(i) for i in fasta_command_list1]
procs2 = [subprocess.Popen(i) for i in fasta_command_list2]
procs3 = [subprocess.Popen(i) for i in fasta_command_list3]
procs4 = [subprocess.Popen(i) for i in fasta_command_list4]
procs5 = [subprocess.Popen(i) for i in fasta_command_list5]

for p in procs1:
    p.wait()
for p in procs2:
    p.wait()
for p in procs3:
    p.wait()
for p in procs4:
    p.wait()
for p in procs5:
    p.wait()
