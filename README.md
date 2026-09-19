CSCI 6032 Machine Learning
Homework 2
https://github.com/jntettey-ux/csci6032-hw2-jntettey-ux.git
Windows 11  

## Text statistics

Run the command-line program with a UTF-8 text file:

```bash
python3 src/text_stats.py sample.txt
```

The program prints JSON containing the number of `lines`, `words`, and
`characters`. Run the tests with Python's built-in unittest framework:

```bash
python3 -m unittest discover
```

To include the most frequent words, pass `--top N`. The output adds a `top`
array whose entries contain the normalized `word` and its `count`. Words are
matched case-insensitively and ties are ordered alphabetically:

```bash
python3 src/text_stats.py --top 5 sample.txt
```