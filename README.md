# Shared Transcript Corpus 🧰

A simple Python tool for extracting the words shared across multiple transcript files.

This project compares two or more `.txt` transcripts, identifies the words that appear in **all** of them, and prints those shared words as a small common-word corpus.

## Features ⚙️

- reads multiple transcript files
- normalizes text to lowercase
- removes punctuation through simple tokenization
- extracts shared words across all transcripts
- prints results in alphabetical order
- works with plain `.txt` files
- uses only Python standard library modules

## Project structure

```text
shared-transcript-corpus/
├── shared_words_corpus.py
├── transcript_a.txt
├── transcript_b.txt
├── README.md
└── RUNNING_ANALYSES.md

```

## Requirements
- Python 3
- No external libraries needed


## How it works 📚

- The script reads each transcript file and converts its words into a Python set.
- Then it computes the intersection of those sets, meaning it keeps only the words that appear in every transcript.

For example:
```
Transcript 1: apple banana orange

Transcript 2: banana orange grape

Shared words:

banana

orange

```

## How to run 💻
- Open a terminal inside the project folder and run:

```
python3 shared_words_corpus.py transcript_a.txt transcript_b.txt
```

You can also run it on more than two transcripts:

```
python3 shared_words_corpus.py transcript1.txt transcript2.txt transcript3.txt
```

## Example output

Using the included sample transcripts, the script produced:

```
Shared words (11 total):
common
it
shared
should
some
the
this
tool
transcript
unique
words
```

## Included sample files 📂

This repository includes two small sample transcripts for pilot testing:

- transcript_a.txt

- transcript_b.txt

These were added so users can test the script immediately before using their own transcript files.

## Notes 🗒️

- matching is case-insensitive
  
- punctuation is ignored
  
- the script keeps all words, including common words like the, it, and this
  
- this is a simple baseline version and can be extended later

  
## Possible future improvements

Some useful future extensions could include:

- stopword removal
  
- frequency counts
  
- exporting results to .txt or .csv
  
- counting words shared by most transcripts instead of all

- a graphical interface


## This tool can be useful for:

- transcript comparison

- pilot corpus creation

- lexical overlap analysis

- identifying repeated vocabulary across speech samples

- simple preprocessing before more advanced linguistic analysis



