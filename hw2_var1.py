from Bio import SeqIO
import argparse
from prettytable import PrettyTable


def stat_count(seqs, seqs_type):
    alphabet_DNA = ['A', 'T', 'G', 'C']
    alphabet_RNA = ['A', 'U', 'G', 'C']
    alphabet_protein = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N',
                        'Q', 'Y', 'C', 'K', 'R', 'H', 'D', 'E']

    # запись названия, подсчет и запись длины и статистики использования символов
    list_name = []  # список названий последовтельностей
    list_len = []  # список длин последовтельностей
    list_stat = []  # список словарей всех последовательностей

    for feature in seqs:
        list_name.append(feature.name)
        list_len.append(len(feature.seq))
        count_list = {}
        for i in range(len(feature.seq)):  # подсчет статистики в зависимости от типа последовательности
            if seqs_type == "DNA":
                for k in range(len(alphabet_DNA)):
                    count_list[alphabet_DNA[k]] = feature.seq.count(alphabet_DNA[k])
            if seqs_type == "RNA":
                for k in range(len(alphabet_RNA)):
                    count_list[alphabet_RNA[k]] = feature.seq.count(alphabet_RNA[k])
            if seqs_type == "PROTEIN":
                for k in range(len(alphabet_protein)):
                    count_list[alphabet_protein[k]] = feature.seq.count(alphabet_protein[k])
        list_stat.append(count_list)
    if len(count_list) == 0:
      print('Ошибка ввода типа последовательности')

    # запись в колонки таблицы
    final_table = PrettyTable()  # итоговая таблица
    final_table.add_column("Name", list_name)
    final_table.add_column("Sequence length", list_len)
    final_table.add_column("Statistics", list_stat)
    final_table._max_width = {"Statistics": 45}  # выбор ширины
    final_table.align = "l"  # выравнивание по левому краю


    final_table = final_table.get_string()  # перевод в стр для построчной записи
    with open('hw2_output.txt', 'w') as results:
        results.write(final_table)

    return final_table


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str, help="Location of DNA seqs in .fasta")   # ввод пути до файла
    parser.add_argument("--type", type=str, help="Type of seqs in file: DNA, RNA or PROTEIN")
    args = parser.parse_args()

    try:   # при отсутствии аргумента с расположением файла
        fasta = SeqIO.parse(args.fasta, 'fasta')
    except AttributeError:
        fasta = SeqIO.parse(input('Введите путь  до файла:'), 'fasta')

    try:   # некорректный ввод типа последовательности
        type_seqs = args.type.upper()
    except AttributeError:
        type_seqs = input('Введите тип последовательности DNA, RNA или PROTEIN:')

    statistics = stat_count(fasta, type_seqs)
    print(statistics)
