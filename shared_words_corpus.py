"""
shared_words_corpus.py
----------------------

This script reads multiple transcript files and identifies the set of
words that are common to all transcripts. It can be useful for
generating a corpus of shared vocabulary across different audio
transcripts or text documents.

Usage:
    python shared_words_corpus.py transcript1.txt transcript2.txt ...

The script will output the list of shared words to the console. By
default it treats words case-insensitively and strips punctuation
characters so that "Word", "word," and "word." are considered the same
token. If a transcript contains no words in common with the others, an
empty set will be reported.

Example::

    # Given two transcripts with overlapping vocabulary
    python shared_words_corpus.py lesson1.txt lesson2.txt
    Shared words (3 total):
    - algorithm
    - data
    - structure

The script can easily be adapted or extended to exclude stop words or
perform more sophisticated linguistic processing, but it keeps things
simple by default per the user's request.
"""

import argparse
import re
from pathlib import Path
from typing import Iterable, Set, Optional


def extract_words(text: str) -> Set[str]:
    """Extract a set of normalized words from the given text.

    Words are normalized by converting to lowercase and stripping
    punctuation. This function uses a simple regular expression to split
    on non-alphanumeric characters, which works well for plain text
    transcripts. It does not attempt to handle contractions or other
    tokenization quirks.

    Args:
        text: The raw text of a transcript.

    Returns:
        A set of unique words present in the text.
    """
    # Split on any sequence of characters that is not a letter or digit.
    tokens = re.split(r"[^\w]+", text.lower())
    # Filter out empty strings resulting from multiple separators.
    return {t for t in tokens if t}


def compute_shared_words(transcripts: Iterable[Path]) -> Set[str]:
    """Compute the intersection of word sets across multiple transcript files.

    Args:
        transcripts: An iterable of file paths pointing to transcript files.

    Returns:
        A set containing the words that appear in every transcript.

    Raises:
        FileNotFoundError: If any of the specified transcript files do not exist.
        ValueError: If fewer than two transcripts are provided.
    """
    transcript_paths = list(transcripts)
    if len(transcript_paths) < 2:
        raise ValueError(
            "At least two transcripts are required to compute shared words."
        )

    # Initialize the shared words set with words from the first transcript.
    shared_words = None  # type: Optional[Set[str]] 

    for path in transcript_paths:
        if not path.exists():
            raise FileNotFoundError(f"Transcript file not found: {path}")
        text = path.read_text(encoding="utf-8")
        words_in_file = extract_words(text)
        if shared_words is None:
            shared_words = words_in_file
        else:
            shared_words &= words_in_file
        # If at any point the intersection becomes empty, no need to
        # continue processing other files because there can be no shared
        # words left.
        if not shared_words:
            break

    return shared_words if shared_words is not None else set()


def main(argv: Optional[Iterable[str]] = None) -> None:
    """Entry point for the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate a corpus of words shared across multiple transcripts."
    )
    parser.add_argument(
        "transcripts",
        metavar="TRANSCRIPT",
        type=Path,
        nargs="+",
        help="Paths to transcript text files (at least two).",
    )
    args = parser.parse_args(args=argv)

    try:
        common_words = compute_shared_words(args.transcripts)
    except Exception as e:
        parser.error(str(e))
        return

    # Output results
    count = len(common_words)
    print(f"Shared words ({count} total):")
    for word in sorted(common_words):
        print(word)


if __name__ == "__main__":
    main()