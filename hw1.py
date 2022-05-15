import argparse


def read_fasta(fasta_file):
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('>'):   # возвращает имя последовательности
            print(line)
        else:
            print(line)   # возвращает саму последовательность


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str, help="Locaion of DNA seqs in .fasta")   # ввод пути до файла
    args = parser.parse_args()
    fasta = open(args.fasta, 'r')
    read_fasta(fasta)
