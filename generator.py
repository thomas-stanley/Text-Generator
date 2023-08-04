from nltk.tokenize import WhitespaceTokenizer
from nltk.util import trigrams
from random import choices
from random import choice
from re import match

tk = WhitespaceTokenizer()
file = input()
with open(file, 'r', encoding="utf-8") as f:
    text = f.read()
    tokens = tk.tokenize(text)

text_trigrams = list(trigrams(tokens))

info_dict = {}
for item in text_trigrams:
    head = f"{item[0]} {item[1]}"
    if head in info_dict:
        if item[-1] in info_dict[head]:
            info_dict[head][item[-1]] += 1
        else:
            info_dict[head][item[-1]] = 1
    else:
        info_dict[head] = {item[-1]: 1}

punctuation = [".", "!", "?"]
printed = 0
while printed < 10:
    flag = True
    start_word = choice(list(info_dict.keys()))
    while not match(r'^[A-Z].*[^.?!]$', list(start_word.split())[0]):
        start_word = choice(list(info_dict.keys()))
    full_text = start_word
    counter = 1
    while flag:
        continuing_word = choices(list(info_dict[start_word].keys()), list(info_dict[start_word].values()), k=1)[0]
        if counter < 5:
            if continuing_word[-1] in punctuation:
                break
        full_text += " " + continuing_word
        split_head = list(start_word.split())
        start_word = f"{split_head[1]} {continuing_word}"
        counter += 1
        if continuing_word[-1] in punctuation:
            print(full_text)
            flag = False
            printed += 1
