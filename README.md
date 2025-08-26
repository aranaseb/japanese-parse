# japanese-parse

This is a pet project to simultaneously tackle NLP programming challenges and 
improve my knowledge of the Japanese language.

japanese-parse is (currently) a segmentation project for text in the Japanese language.
This language presents a unique NLP challenge as word boundaries are not as explicit as English.

# Philosophy

To segment a language that has no 'words' like English or other languages in the latin script, we must decide what constitutes a word.

Currently operating on the idea that a "word" in japanese consists of an 'idea' and an inflection particle.
This can be compared to languages with grammatical case endings, so particles in Japanese are part of a 'word's morphemes.

The current algorithm uses hiragana/non-hiragana character boundaries to separate 'words'.
There is also a special case where my translation dataset does not find a direct translation for the kanji alone,
so it considers the following hiragana one character at a time. This is common in adjectives and verbs especially.

On the current dataset, Elementary Japanese sentences, this is working well.
However real Japanese text has much more complex 'word' boundaries that exceed my proficiency in the language.
I have observed adjacent kanji/kanji pairs of 'words', hiragana-only 'words' (like ある、する), and even full on particle dropping.
I have not even considered potential 'morphemes' within kanji 'words' themselves, like "駅" + "弁" = "駅弁".
And of course this could extend to the radicals of Han Chinese characters. This kind of "morphology" is far beyond my amateur command of Japanese.

I'll also acknowledge another concession in this philosophy, which is particles attatched to subphrases. My algorithm will incorrectly assign the particle to the closest preceding 'content word'.
For example: 今日は暑いなと思った parses to [今日:は, 暑い:なと, 思った:], forgoing a true syntax parse in favor of isolating 今日、暑い、思った.
Here, な and と modify the whole subphrase 今日は暑い, not just 暑い.
This may be a large barrier for true particle analysis as determining what particle modifies which subphrase would require full syntax tree level-wise analysis.

For now, I use this tool to extract kanji from easy-to-parse sentences and translate them so I can examine the raw syntax of a Japanese sentence with the 'content words' translated to my native language.

# Status 8/25/2025

Jupyter notebook - segments and translates kanji-based words.

Todo: Add sentence-ending verb extraction.

Long-term: Encode words and sentences using someone's BERT tokenizer for japanese (I am not smart or fluent enough to write that!)
