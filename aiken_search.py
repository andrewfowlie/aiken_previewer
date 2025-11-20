"""
Search Aiken questions
======================
"""

import re
import sys


def parse_file(file_name):
    with open(file_name) as f:
        data = f.read()
    pairs = re.split('(ANSWER: [A-Z])', data)
    return [(q + a).strip() for q, a in zip(pairs[::2], pairs[1::2])]


def search(file_name, pattern):
    quiz = parse_file(file_name)
    return [p for p in quiz if pattern.lower() in p.lower()]


if __name__ == "__main__":

    pattern = sys.argv[1]
    file_names = sys.argv[2:]

    for file_name in file_names:
        hits = search(file_name, pattern)
        for h in hits:
            print(h)
