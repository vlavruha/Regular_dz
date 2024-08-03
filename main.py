from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from collections import defaultdict

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
    #Task 1
pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?([доб.]*)?\s*(\d+)*\)?"
pattern_repl = r'+7(\2)\3-\4-\5 \6\7'

new_list = []
res_list = []

for i, item in enumerate(contacts_list):
    fio = " ".join(item[:3]).split()
    # print(fio)
    while len(fio) < 3:
        fio += ['']
    new_list.append(fio + item[3:7])

    #Task 2
    new_list[i][5] = re.sub(pattern, pattern_repl, item[5]).strip()
# pprint(new_list)

    #Task 3

data = defaultdict(list)
for info in new_list:
    key = tuple(info[:2])
    for item in info:
        if item not in data[key]:
            data[key].append(item)

final_list = list(data.values())

# pprint(final_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_list)
