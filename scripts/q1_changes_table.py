import csv

def get_old_keys() -> tuple:
    """Return tuple of old key, new key."""
    with open('finance_changes.csv', 'r') as f:
        changes_reader = csv.DictReader(f)
        return [(item['Current'], item['New']) for item in changes_reader]

def match_new_key_to_old_cellref() -> tuple:
    print("{:<120} {:<30}".format("New Key", "Old Cellref"))
    print("{:-<120}".format("---"))
    with open('../archive/datamap-returns-to-master', 'r') as f:
        reader = csv.reader(f)
        pairs = get_old_keys()
        for p in pairs:
            for k in reader:
                if k[0] == p[0]:
                    print("{:<120} {:<30}".format(p[1], k[2]))
                    break

match_new_key_to_old_cellref()
