import pandas as pd
import re

#By James C. Hu

def blastn_adeno_out(infile):
    input_column_names = ['qseqid', 'sseqid', 'evalue', 'bitscore', 'pident', 'nident', 'qcovs', 'length', 'mismatch', 'qlen', 'slen']

    df = pd.read_csv(infile, sep='\t', names=input_column_names).copy()

    output_column_names = ['Seq_ID', 'Total_reads', 'HAdV_A18', 'HAdV_B3', 'HAdV_C5', 'HAdV_D8', 'HAdV_E4', 'HAdV_F40', 'HAdV_G52']

    df_HAdV_A18 = df[df['sseqid'] == 'GU191019.1_HAdV_A18']
    df_HAdV_B3 = df[df['sseqid'] == 'DQ086466.1_HAdV_B3']
    df_HAdV_C5 = df[df['sseqid'] == 'AC_000008.1_HAdV_C5']
    df_HAdV_D8 = df[df['sseqid'] == 'AB448767.1_HAdV_D8']
    df_HAdV_E4 = df[df['sseqid'] == 'AY487947.1_HAdV_E4']
    df_HAdV_F40 = df[df['sseqid'] == 'L19443.1_HAdV_F40']
    df_HAdV_G52 = df[df['sseqid'] == 'DQ923122.2_HAdV_G52']

    seq_id = re.split(r'(\d+)', infile)[0] + re.split(r'(\d+)', infile)[1]

    mapped_total = len(df)
    mapped_hadv_a = len(df_HAdV_A18)
    mapped_hadv_b = len(df_HAdV_B3)
    mapped_hadv_c = len(df_HAdV_C5)
    mapped_hadv_d = len(df_HAdV_D8)
    mapped_hadv_e = len(df_HAdV_E4)
    mapped_hadv_f = len(df_HAdV_F40)
    mapped_hadv_g = len(df_HAdV_G52)

    return [seq_id, mapped_total, mapped_hadv_a, mapped_hadv_b, mapped_hadv_c, mapped_hadv_d, mapped_hadv_e, mapped_hadv_f, mapped_hadv_g]
