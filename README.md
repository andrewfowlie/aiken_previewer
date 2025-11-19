# Aiken Previewer

Preview questions written in the [Aiken file](https://docs.moodle.org/501/en/Aiken_format) format on e.g. Moodle platforms. You get a preview with math rendered using latex.

## Usage

```bash
python3 aiken_previewer.py aiken_example.txt
```
This should give you a prompt where you can enter a question number to preview. You can edit your file (e.g. `aiken_example.txt`) and press enter and the preview will reload.

## Requirements

This requires Python and `matplotlib` for rendering, as well as working `LaTeX` installation, and perhaps some other tools; see <https://matplotlib.org/stable/users/explain/text/usetex.html>. If you've ever used `LaTeX` labels in matplotlib, this should work already.
