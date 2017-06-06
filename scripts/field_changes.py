"""
Given a csv file in format:

    old,new
    SRO Full Name,SRO Nickname

changes fieldnames in datamap csv file
"""

import csv


def get_amending_fields() -> list:
    with open('finance_changes.csv', 'r') as amendment_file:
        a_reader = csv.reader(amendment_file)
        return [(item[1], item[0]) for item in a_reader]


if __name__ == "__main__":

    amending_fields = get_amending_fields()

    with open('new-dm.csv', 'w', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        with open(
            '../datamap.csv', 'r+', encoding='latin1') as f:
            reader = csv.reader(f)
            for line in reader:

                # get the number of items in the dm line
                indices = list(range(len(line)))

                # if the key dm is in the list of fields to be changed...
                if line[0] in [a_item[1] for a_item in amending_fields]:
                    # put the new key on its own in a list
                    w_row = [[item[0] for item in amending_fields if
                              item[1] == line[0]][0]]

                    # if we have more items in the dm line...
                    if len(indices) > 1:
                        # make a list of the remaining dm line items
                        remaining_dm_items = [line[x] for x in indices[1:]]
                        w_row = w_row + remaining_dm_items
                    writer.writerow(w_row)
                else:
                    w_row = [line[i] for i in indices]
                    writer.writerow(w_row)
