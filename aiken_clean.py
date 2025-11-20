"""
Remove duplicated and malformatted Aiken questions
=================================================
"""

import re
import sys


def parse_file(file_name):
    with open(file_name) as f:
        data = f.read()
    pairs = re.split('(ANSWER: [A-Z])', data)
    return [(q + a).strip() for q, a in zip(pairs[::2], pairs[1::2])]


def non_empty_question(problem):
    question = problem.split("A)", 1)[0]
    return bool(question)


if __name__ == "__main__":

    file_names = sys.argv[1:]

    questions = [parse_file(file_name) for file_name in file_names]
    questions = sum(questions, [])

    unique = set(questions)
    complete = [u for u in unique if non_empty_question(u)]

    for c in complete:
        print(c)
