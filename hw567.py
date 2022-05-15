import argparse
import csv
from Bio import SeqIO


# функция выбора из файла только ДНК-последовательностей
def dna_read(seqs):
    only_dna_dict = {}
    dna_name = []
    dna_seqs = []
    dna_alph = set("ATGCN")
    for feature in seqs:
        leftover = set(str(feature.seq)) - dna_alph
        if leftover == set() or leftover == set('N'):
            dna_name.append(feature.name)
            dna_seqs.append(feature.seq)

    for j in range(len(dna_name)):
        only_dna_dict[dna_name[j]] = str(dna_seqs[j])

    if not only_dna_dict:
        print("Файл не содержит последовательностей ДНК")

    return only_dna_dict


# функция записи словаря с ДНК посл-ми в fasta-файл
def write_fasta(dict_dna):
    with open('hw5_DNA_seq.tab', 'w', newline='') as file:
       w = csv.writer(file, delimiter='\t')
       w.writerows(dict_dna.items())
       file.flush()


# функция поиска ORF в последовательностях из файла
def orf_search(seqs, min_length):
    data = []
    for feature in seqs:   # для каждой последовательности в файле
        for strand, nuc in [(+1, feature.seq), (-1, feature.seq.reverse_complement())]:   # прямая и обратная цепи
            for frame in range(3):   # для каждой рамки считывания
                for pro in nuc[frame:].translate(table=1).split("*"):   # транслируется ам-к посл-ть по стандартной табл
                        if len(pro) >= min_length and pro[0] == 'M':  # если посл-ти удовлетворяют усл. длины и опр. ORF
                            print(f'{feature.name} \t strand:{strand} \t frame:{frame} \t length:{len(pro)} \t seq:{pro}')  # вывод на экран
                            a = f'{feature.name}, {strand}, {frame}, {len(pro)}, {pro}'  # строка для записи в файл
                            data.append(a)
    if not data:
        print("ORF не найдены")
    return data   # список строк с результатами поиска ORF


# функция записи в файл результата поиска ORF
def write_csv(orf):
    with open('hw5_ORF.csv', 'w', newline='') as file:
       file.write('Name,Strand,Frame, Length, Amino acid sequence')   # заголовки столбцов финальной таблицы
       file.write('\n')
       for i in orf:
           file.write(i)
           file.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str, help="Locaion of fasta-file")   # ввод пути до файла
    parser.add_argument("--min_len", type=int, help="Min length of ORF am.ac sequence")  # ввод min длины ORF
    args = parser.parse_args()

    try:   # при отсутствии аргумента с расположением файла
        fasta = SeqIO.parse(args.fasta, 'fasta')

    except AttributeError:
        fasta = SeqIO.parse(input('Введите путь  до файла:'), 'fasta')

    except FileNotFoundError:
        fasta = SeqIO.parse(input('Введите корректный путь  до файла:'), 'fasta')

# выбираем только ДНК последовательности и  записываем в отдельный fasta-файл
    dna_dict = dna_read(fasta)
    write_fasta(dna_dict)
    SeqIO.convert('hw5_DNA_seq.tab', 'tab', 'hw5_DNA_output.fasta', 'fasta')
    fasta_dna = SeqIO.parse('hw5_DNA_output.fasta', 'fasta')

# поиск ORF
    try:
        min_len = args.min_len
        list_orf = orf_search(fasta_dna, min_len)

    except TypeError:
        min_len = int(input('Введите минимальную длину: '))
        list_orf = orf_search(fasta_dna, min_len)

# записываем результаты в файл
    write_csv(list_orf)





