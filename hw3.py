import argparse
import re
import Bio.Data.IUPACData as bdi
from Bio import SeqIO
from Bio.Seq import Seq
from itertools import product


# переводит символы неоднозначности во все возможные варианты посл-ти по IUPAC AMBIGIOUS CODE
def extend_ambiguous_seq(seq):
   amb_dict = bdi.ambiguous_dna_values
   return list(map("".join, product(*map(amb_dict.get, seq))))


# преобразует обратный праймер (переворачивает и по пр комплементарности заменяет символы)
def reverse_modifier(rev_list):
    list_mod = []
    for primer in rev_list:
        primer = Seq(primer)
        mod = primer.reverse_complement()
        list_mod.append(str(mod))
    return list_mod


# создание всех возможных паттернов для поиска при помощи регулярных выражений
def create_re_primer(forw_list, rev_list):
    list_primers_comb = []
    forw_list = [primer + '.+' for primer in forw_list]
    total = product(forw_list, rev_list)
    for el in total:
        list_primers_comb.append(''.join(map(str, el)))
    return list_primers_comb


#  поиск ампликонов в референсном геноме
def amplicon_search(fasta_f, primers):
    fasta_f = SeqIO.parse(fasta_f, 'fasta')
    search_res = []
    for feature in fasta_f:
        for primer in primers:
            reference = re.compile(primer)
            result = re.findall(reference, str(feature.seq))
            if result:
                # print(f'{feature.name} primer: {primer}  seqs:{result}')
                res = f'{feature.name}, {primer}, {result}'
                search_res.append(res)
    if not search_res:
        print('Ампликоны не найдены')
    return search_res


# запись в файл результата поиска
def write_csv(orf_results):
    with open('hw3_output.csv', 'w', newline='') as file:
       file.write('Name,Primer,Sequence')   # заголовки столбцов финальной таблицы
       file.write('\n')
       for i in orf_results:
           file.write(i)
           file.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str, help="Location of seqs in .fasta")  # ввод пути до файла
    parser.add_argument("--forward", type=str, help="Forward degenerate primer")  # ввод прямого праймера
    parser.add_argument("--reverse", type=str, help="Reverse degenerate primer")  # ввод обратного праймера
    args = parser.parse_args()

    try:
        forward = args.forward
        list_forward = extend_ambiguous_seq(forward)
    except TypeError:
        forward = input('Введите прямой праймер:').upper()
        list_forward = extend_ambiguous_seq(forward)

    try:
        reverse = args.reverse
        list_pre_reverse = extend_ambiguous_seq(reverse)
    except TypeError:
        reverse = input('Введите обртный праймер:').upper()
        list_pre_reverse = extend_ambiguous_seq(reverse)

    list_reverse = reverse_modifier(list_pre_reverse)
    list_primers = create_re_primer(list_forward, list_reverse)

    try:   # при отсутствии аргумента с расположением файла
        fasta = args.fasta

    except AttributeError:
        fasta = input('Введите путь до файла:')

    try:
        list_results = amplicon_search(fasta, list_primers)
    except FileNotFoundError:
        list_results = amplicon_search(open(input('Введите корректный путь до файла:')), list_primers)

    write_csv(list_results)

# python3 hw3.py --fasta ./test_data/try.fasta --forward CGCGBGCGCGCGCVCACW --reverse VACGCNAATGCAAA



