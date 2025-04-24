import csv
import os
from typing import List, Dict

def write_to_csv(papers: List[Dict], filename: str) -> None:
    if not papers:
        print("No papers found with non-academic authors.")
        return

    file_exists = os.path.isfile(filename)
    write_header = not file_exists

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=papers[0].keys())
        if write_header:
            writer.writeheader()
        writer.writerows(papers)