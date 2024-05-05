#!/usr/bin/env python

"""
La liste de mots vient de :
https://github.com/chrplr/openlexicon/blob/master/datasets-info/Liste-de-mots-francais-Gutenberg/README-liste-francais-Gutenberg.md
"""

import random
import unicodedata
from collections import defaultdict

words = []

with open("liste.de.mots.francais.frgut.txt", "r") as f:
    for line in f:
        word = line.strip()
        # The next line to avoid accented letters to count as two characters.
        # It appears that unicode allows for instance an é to be encoded as an accent followed by an e
        # Source: https://stackoverflow.com/questions/54638285/single-accented-characters-with-str-len-x-2
        word = unicodedata.normalize("NFC", word)
        if len(word) == 8:
            words.append(word)


def denorm(word):
    return "".join(sorted(word))


# A table where the keys are the denormalized letters and values are a list of words that denormalize to the key
lookup = defaultdict(list)
for word in words:
    lookup[denorm(word)].append(word)

# A second pass to keep only anagrams and to sort
with_anagrams_sorted = {k: v for k, v in sorted(lookup.items()) if len(v) > 1}

# Just show a few
sample = dict(random.sample(list(with_anagrams_sorted.items()), 300))

for k, v in sample.items():
    print(k, v)
