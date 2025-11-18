"""
Preview a question written for Learning Mall in the Aitken format
=================================================================
"""

import re
import sys

import matplotlib.pyplot as plt


LATEX = {
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 20,
    "text.latex.preamble": r'\usepackage{amsfonts,amssymb,setspace}'
}

plt.rcParams.update(LATEX)


def parse_file(file_name):
    with open(file_name) as f:
        data = f.read()
    pairs = re.split('(ANSWER: [A-Z])', data, flags=re.IGNORECASE)
    return [(q + a).strip() for q, a in zip(pairs[::2], pairs[1::2])]


def render(text):
    text = text.replace("$$", "$")
    plt.clf()
    plt.axis("off")
    plt.text(0, 0.5, text, ha='left', linespacing=2)
    plt.show(block=False)


if __name__ == "__main__":

    file_name = sys.argv[1]
    problem_number = 0

    while True:
        quiz = parse_file(file_name)

        entered = input(
            f"Problem number of {len(quiz)} [empty to refresh; n for next]: ")

        if entered == "n":
            problem_number += 1
        elif entered:
            problem_number = int(entered)

        problem = quiz[problem_number]
        render(problem)
