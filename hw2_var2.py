from Bio import SeqIO
import argparse
from collections import Counter


def stat_count(seqs):
    print('%20s %20s %100s' % ('Name', 'Length', 'Symbol Statistics'))
    for feature in seqs:
        print('%20s %20s %100s' % (feature.name, len(feature.seq), str(dict(Counter(feature.seq)))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str, help="Location of seqs in .fasta")   # ввод пути до файла
    args = parser.parse_args()

    try:   # при отсутствии аргумента с расположением файла
        fasta = SeqIO.parse(args.fasta, 'fasta')
    except AttributeError:
        fasta = SeqIO.parse(input('Введите путь  до файла:'), 'fasta')

    stat_count(fasta)

