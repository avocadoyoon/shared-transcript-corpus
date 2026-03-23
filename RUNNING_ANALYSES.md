# Running Analyses

This file explains how to run the shared-word extraction analysis and what the output means.

## Purpose

The analysis identifies the words that are shared across multiple transcript files.

In this project, the script compares transcript text files and returns the vocabulary that appears in every file provided.

## Input files

The sample analysis uses these two files:

- `transcript_a.txt`
- `transcript_b.txt`

You can replace them with your own `.txt` transcript files later.

## Command used

Run the analysis from the terminal with:

```bash
python3 shared_words_corpus.py transcript_a.txt transcript_b.txt
```

## What this command does

This command tells Python to:

- execute the script ```shared_words_corpus.py```

- open the files ```transcript_a.txt``` and ```transcript_b.txt```

- extract words from both transcripts

- compare the word sets

- print the words shared across both transcripts

  
## Output from the pilot test

The pilot test on the included sample transcripts produced:

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

## Interpretation of the output

This means those 11 words appeared in both transcript files.

The script only keeps words that occur in every transcript provided.

So:

- if a word appears in both files, it is included

- if a word appears in only one file, it is excluded

## Important note about the sample output

The word ```unique``` appears in the shared-word list because it was written in both sample transcripts.

So although the sentence described some words as “unique,” the literal word unique itself appeared in both texts and was therefore correctly included in the overlap.



## How to run the analysis on your own transcripts

Replace the sample file names with your own files:

```
python3 shared_words_corpus.py my_transcript_1.txt my_transcript_2.txt
```

Or with more than two transcripts:

```
python3 shared_words_corpus.py t1.txt t2.txt t3.txt t4.txt
```

## Expected behavior with multiple transcripts

- When you provide more transcripts, the script becomes stricter.

- A word will only be included if it appears in all files.

For example:

- if a word appears in 3 out of 4 transcripts, it will not be included

- if a word appears in all 4 transcripts, it will be included

## Current preprocessing behavior

The script currently performs simple preprocessing:

- converts text to lowercase

- splits text into words

- ignores punctuation

- keeps all remaining words


This analysis can help with:

- finding lexical overlap across transcripts

- creating a shared vocabulary list

- preparing a small common-word corpus

- piloting transcript comparison workflows

- building a baseline before more advanced NLP steps


## Suggested next steps

- Possible next analyses or improvements include:

- removing stopwords

- exporting the output to a file

- counting frequency of shared words

- comparing partial overlap across transcripts

- visualizing overlap size across files
