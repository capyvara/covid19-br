import argparse
import datetime
import json
from collections import Counter
from itertools import groupby

import rows
from tqdm import tqdm

from epiweeks import Week, Year

cities = rows.import_from_csv("data/populacao-estimada-2019.csv")

def convert_file(filename):
    table = rows.import_from_csv(filename)
    row_key = lambda row: (row.date, row.state)
    table = sorted(table, key=row_key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    parser.add_argument("output_filename")
    args = parser.parse_args()

    writer = rows.utils.CsvLazyDictWriter(args.output_filename)
    for row in tqdm(convert_file(args.input_filename)):
        writer.writerow(row)
