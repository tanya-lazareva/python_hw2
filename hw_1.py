def read_fasta(fasta_file):
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('>'):
            print(line)
        else:
            print(line)


with open(input('Введите имя файла:')) as fasta_file:
    read_fasta(fasta_file)
