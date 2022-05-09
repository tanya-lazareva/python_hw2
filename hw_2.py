from Bio import SeqIO
from prettytable import PrettyTable

file = SeqIO.parse(input('Введите имя файла: '), 'fasta')

print('Выберите тип последовательностей в файле:\n 1-ДНК\n 2-РНК\n 3-протеин: ')
seq_type = int(input(''))

alphabet_DNA = ['A', 'T', 'G', 'C']
alphabet_RNA = ['A', 'U', 'G', 'C']
alphabet_protein = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N',
                    'Q', 'Y', 'C', 'K', 'R', 'H', 'D', 'E']

list_name = []   # список названий последовтельностей
list_len = []   # список длин последовтельностей
list_stat = []   # список словарей всех последовательностей

for feature in file:
    list_name.append(feature.name)
    list_len.append(len(feature.seq))
    count_list = {}
    for i in range(len(feature.seq)):
        if seq_type == 1:
            for k in range(len(alphabet_DNA)):
                count_list[alphabet_DNA[k]] = feature.seq.count(alphabet_DNA[k])
        if seq_type == 2:
            for k in range(len(alphabet_RNA)):
                count_list[alphabet_RNA[k]] = feature.seq.count(alphabet_RNA[k])
        if seq_type == 3:
            for k in range(len(alphabet_protein)):
                count_list[alphabet_protein[k]] = feature.seq.count(alphabet_protein[k])
    list_stat.append(count_list)

final_table = PrettyTable()   # итоговая таблица
final_table.add_column("Name", list_name)
final_table.add_column("Sequence length", list_len)
final_table.add_column("Statistics", list_stat)
final_table._max_width = {"Statistics": 45}
final_table.align = "l"

print(final_table)
final_table = final_table.get_string()

with open('hw2_final_table.txt', 'w') as results:
    results.write(final_table)
