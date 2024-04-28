#!/usr/bin/env python

"""
La liste de mots vient de :
https://github.com/chrplr/openlexicon/blob/master/datasets-info/Liste-de-mots-francais-Gutenberg/README-liste-francais-Gutenberg.md
"""

import random
import unicodedata
from collections import defaultdict

import rich


def denorm(word):
    return "".join(sorted(word))


words = []

with open("liste.de.mots.francais.frgut.txt", "r") as f:
    for line in f:
        word = line.strip()
        # Next line to avoid the length of accented character to appear as 2.
        # https://stackoverflow.com/questions/54638285/single-accented-characters-with-str-len-x-2
        # So it's proper unicode to represent for instance an é as an accent followed by an e
        # surprised by this, it explains a lot of problems I've seen elsewhere.
        word = unicodedata.normalize("NFC", word)
        words.append(word)


eight_letter_words = [word for word in words if len(word) == 8]

# A table where the keys are the denormalized letters and values are a list of words that denormalize to the key
lookup = defaultdict(list)
for word in eight_letter_words:
    lookup[denorm(word)].append(word)

# A second pass to keep only anagrams and to sort
with_anagrams_sorted = {k: v for k, v in sorted(lookup.items()) if len(v) > 1}

sample = dict(random.sample(with_anagrams_sorted.items(), 300))

rich.print(with_anagrams_sorted)
