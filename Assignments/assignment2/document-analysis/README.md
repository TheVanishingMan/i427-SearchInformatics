### Assignment 2, Part 1: Document Analysis

#####Part 1:

Some things can be calculated almost exactly: number of letters, vowels, two-letter combinations.  Where possible, I tried to calculate things exactly.

Other calculations could be a matter of opinion, and where the interpretations were gray, I stuck with approximations: number of words, sentences, and syllables.

Consider a few examples:

  * How many syllables are in the word "cruellest?" (cru-lest or cru-el-lest)
  * How many syllables are in the word "Starnbergersee" or the word "deutsch?" (should we consider even non-English words for this assignment)
  * How many sentences does "T.S. Eliot grew up in St. Louis, Missouri." contain? (do we break on periods, length, or punctuation-uppercase combinations?)
  * How do we interpret the difficulty of comprehending "The old man the boat." (The old [noun] man [verb] the boat)

We make approximations because language is greatly open to interpretation and changes all the time.  Computer translation found its beginnings during the cold war, but is still mostly considered an unsolved problem.  Statistical models for frequency or relational models for patterns in the data are both most effective if we assume we live in a closed-world. However, assuming a closed world is fundamentally backwards for what language is.

I started by implementing the simplest suggestions provided in the instructions, hoping this could be a baseline for which I could evaluate further methods against.  100% accuracy without hard-coding every syllable-count in every word of every language.  If the simple rules can achieve 80-95% accuracy on average I'll be fairly happy.  Frankly I want to do well on this assignment, but I'm not predicting drug interactions or probability of lung cancer here: I don't expect a few percentage points to be the difference between life and death.

After that I made a few small adjustments: making sure I removed all non-letters before counting letters, counting sentences when the pattern '. H' appeared (punctuation + capital letter combinations).