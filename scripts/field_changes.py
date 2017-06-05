"""
Given a csv file in format:

    old,new
    SRO Full Name,SRO Nickname

changes fieldnames in datamap csv file
"""

import csv
import codecs


def get_amending_fields() -> list:
    with codecs.open(
            '../finance_changes.csv', 'r', errors='ignore') as amendment_file:
        a_reader = csv.reader(amendment_file)
        return [(item[1], item[0]) for item in a_reader]


amending_fields = get_amending_fields()

with open('../new-dm.csv', 'w', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    with codecs.open('../datamap-returns-to-master-WITH_HEADER_FORSQLITE.csv', 'r+', errors='ignore') as f:
        reader = csv.reader(f)
        for line in reader:
            # TODO need to test for membership of a tuple within a list here
            if line[0] in amending_fields:
                writer.writerow(
                    [amending_fields[amending_fields.index(line[0])], line[1], line[2]])
            else:
                writer.writerow(
                    [line[0], line[1], line[2]])
