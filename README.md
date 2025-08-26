# japanese-parse

This is a pet project to simultaneously tackle NLP programming challenges and 
improve my knowledge of the Japanese language.
japanese-parse is (currently) a segmentation project for text in the Japanese language.
This language presents a unique NLP challenge as word boundaries are not as explicit as English.

###Philosophy
To segment a language that has no 'words' like English or other languages in the latin script,
we must decide what constitutes a word.

Currently operating on the idea that a "word" in japanese consists of an 'idea' and an inflection particle.
This can be compared to languages with grammatical case endings, so particles in Japanese are part of a 'word's morphemes.


# Status 8/25/2025
Jupyter notebook - segments and translates kanji-based words.
Todo: Add particle analysis, sentence-ending verb extraction.
Long-term: Encode words and sentences using a tokenizer like BERT.
