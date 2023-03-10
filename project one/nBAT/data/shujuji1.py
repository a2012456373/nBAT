

import csv
import re
def seq2kmer0(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(0, len(seq) + 1 - k, 3)]
    kmers = " ".join(kmer)
    return kmers
def seq2kmer1(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(1, len(seq) + 1 - k, 3)]
    kmers = " ".join(kmer)
    return kmers
def seq2kmer2(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(2, len(seq) + 1 - k, 3)]
    kmers = " ".join(kmer)
    return kmers
def seq2kmer3(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(3, len(seq) + 1 - k, 6)]
    kmers = " ".join(kmer)
    return kmers
def seq2kmer4(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(4, len(seq) + 1 - k, 6)]
    kmers = " ".join(kmer)
    return kmers
def seq2kmer5(seq, k):
    """
    Convert original sequence to kmers

    Arguments:
    seq -- str, original sequence.
    k -- int, kmer of length k specified.

    Returns:
    kmers -- str, kmers separated by space

    """
    # kmer = [seq[x:x + k] for x in range(len(seq) + 1 - k)]
    kmer = [seq[x:x + k] for x in range(5, len(seq) + 1 - k, 6)]
    kmers = " ".join(kmer)
    return kmers
# ????????????
# with open(r"H:\parser-main\data\biio\positive.txt", 'r') as f:

with open(r"H:\project one\nBAT\case_study\case_study_seq.fa", 'r') as f:
    # ??????????????????
    lines = f.read()
# ???????????????????????????????????????
# gene_sequences = re.findall(r'>SPENT\d+\n([A-Z]+)', data)
# ?????????">"??????
#lines = [line for line in lines if ">" not in line]

data_list = lines.split("\n")

# ???????????????">"??????
gene_sequences = [line for line in data_list if not line.startswith(">")]

#gene_sequences = re.findall(r'>Lncipedia\d+\n([A-Z]+)', data)
# ?????????????????????CSV??????
with open(r"H:\parser-main\data\biio\positive2.csv", 'w', newline='') as f:
    # ??????CSV?????????
    writer = csv.writer(f)
    # ???????????????
    writer.writerow(['source','target'])
    #writer.writerow(['source',  'target'])
    # ????????????????????????
    sum=0
    y = 0
    ke=0
    for gene_sequence in gene_sequences:
        #print('1',len(gene_sequence))
        #sum+=len(gene_sequence)
        # ?????????????????????6-kmer??????
        k = 3
        #gene_sequence=list(gene_sequence)
        kmer_string0 = seq2kmer0(gene_sequence, k)
        kmer_string1 = seq2kmer1(gene_sequence, k)
        kmer_string2 = seq2kmer2(gene_sequence, k)
        # kmer_string3 = seq2kmer3(gene_sequence, k)
        # kmer_string4 = seq2kmer4(gene_sequence, k)
        # kmer_string5 = seq2kmer5(gene_sequence, k)

        x = kmer_string0.split(' ')
        #print('2',len(x))

        #rint(kmer_string)
        if len(x)>=2000:
            ke+=1
        sum += len(x)*3
        y += 3
        if y>21519:
            break
        # # ??????kmer????????????CSV??????
        #writer.writerow([kmer_string0, kmer_string1, kmer_string2,1])
        writer.writerow([kmer_string0, 0])
        writer.writerow([kmer_string1, 0])
        writer.writerow([kmer_string2, 0])
        # writer.writerow([kmer_string3, 0])
        # writer.writerow([kmer_string4, 0])
        # writer.writerow([kmer_string5, 0])
        #gene_sequence = " ".join(gene_sequence)

        #writer.writerow([gene_sequence, 1])
    print(ke/3)
    print(y)
    print(sum / y)