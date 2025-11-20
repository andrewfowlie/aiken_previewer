# Aiken Tools

Tools for using questions written in the [Aiken file](https://docs.moodle.org/501/en/Aiken_format) format on e.g. Moodle platforms. 

## Usage

```bash
python3 aiken_previewer.py aiken_example.txt  # preview with math rendered using latex
python3 aiken_search.py "whatever you want" aiken_example.txt  # show only questions matching a search string
python3 aiken_clean.py aiken_example.txt  # remove duplicated questions and malformatted questions (e.g. questions for which the question is empty)
```
## Requirements

This requires Python. For previewing, we require `matplotlib` for rendering as well as a working `LaTeX` installation, and perhaps some other tools; see <https://matplotlib.org/stable/users/explain/text/usetex.html>. If you've ever used `LaTeX` labels in matplotlib, this should work already.
