# Spell Checker using Wagner-Fischer's Algorithm

## Libraries used

- nltk
- numpy

## Libraries used

This spell checker uses a set of 'all' words in the english language. This data is acquired from nltk.

The dataset is used for two things:

1. Verify if a given word is in it; i.e.: is spelled correctly.
2. Find suggestions for a misspelled word.

Finding suggestions is done using Wagner-Fischer's algorithm to compute the edit distance between 2 strings. Those strings which's edit distance is >4 are suggested as correct spellings.
