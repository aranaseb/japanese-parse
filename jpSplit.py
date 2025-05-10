# program to 'split' japanese sentences into words
import collections
import pandas as pd
import random
import re

def isHiragana(c) -> bool:
    return u'\u3040' <= c <= u'\u309F'

def normalize(sentence: str) -> str:
    sentence = re.sub("。", '', sentence)
    sentence = re.sub("、", '', sentence)
    sentence = re.sub("（", '', sentence)
    sentence = re.sub("）", '', sentence)
    sentence = re.sub("・", '', sentence)
    sentence = re.sub("『", '', sentence)  # removes anything in brackets
    sentence = re.sub("』", '', sentence)  # removes anything in brackets
    sentence = re.sub("\n", '', sentence)  # removes anything in brackets
    return sentence

def split(sentence: str):
    sentence = normalize(sentence)
    backwards = sentence[::-1]

    words = collections.deque()
    inflections = collections.deque()

    i = 0
    while i < len(backwards):
        inflection = ""
        while i < len(backwards) and isHiragana(backwards[i]):
            inflection = backwards[i] + inflection  # populate inflection with hiragana
            i += 1
        inflections.insert(0,inflection)

        word = ""
        while i < len(backwards) and not isHiragana(backwards[i]):
            word = backwards[i] + word  # populate word with non-hiragana
            i += 1
        words.insert(0,word)

    df = pd.DataFrame(list(zip(words, inflections)), columns=['Word', 'Inflection'], index=range(1,len(words) + 1))
    print(df)

def main():
    path = "/Users/Thano/wiki-jp/wiki"
    wiki_df = pd.read_pickle(path)
    wiki_df.head()

    random.seed(123)
    articleNum = random.randint(0, len(wiki_df))
    series = wiki_df.text
    text = series[articleNum]
    sentences = text.split("。")
    sentence = sentences[random.randint(0, len(sentences) - 1)]
    print("\nSentence: ", re.sub("\n", "", sentence))
    print()
    split(sentence)
main()
