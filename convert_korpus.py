import re
import os
import nltk

# Separates the special characters from words, deletes all empty sentences and their translations

# ASSISTANT TEST DATA
europarl_en = 'data/assistant_data/asistent_testset.en'
f_en = open(europarl_en, "r", encoding="utf8")
deletion_flag = []
for iterator, line in enumerate(f_en.readlines()):
    if line == '\n':
        deletion_flag.append(iterator)

europarl_sl = 'data/assistant_data/asistent_testset.sl'
f_sl = open(europarl_sl, "r", encoding="utf8")

for iterator, line in enumerate(f_sl.readlines()):
    if line == '\n':
        deletion_flag.append(iterator)
f_en.close()
f_sl.close()
f_en = open(europarl_en, "r", encoding="utf8")

f_new_en = open("data/assistant_data/asistent_testset-corr.en", "x", encoding="utf8")
for iterator, line in enumerate(f_en.readlines()):
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    if iterator not in deletion_flag:
        f_new_en.write(s)

f_en.close()
f_new_en.close()

f_sl = open(europarl_sl, "r", encoding="utf8")
f_new_sl = open("data/assistant_data/asistent_testset-corr.sl", "x", encoding="utf8")
for iterator, line in enumerate(f_sl.readlines()):
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    if iterator not in deletion_flag:
        f_new_sl.write(s)

f_sl.close()
f_new_sl.close()


# SPECIALISED CORPUS DATA
europarl_en = 'data/special/special.en'
f_en = open(europarl_en, "r", encoding="utf8")
deletion_flag = []
for iterator, line in enumerate(f_en.readlines()):
    if line == '\n':
        deletion_flag.append(iterator)

europarl_sl = 'data/special/special.sl'
f_sl = open(europarl_sl, "r", encoding="utf8")

for iterator, line in enumerate(f_sl.readlines()):
    if line == '\n':
        deletion_flag.append(iterator)
f_en.close()
f_sl.close()
f_en = open(europarl_en, "r", encoding="utf8")

f_new_en = open("data/special/special-corr.en", "x", encoding="utf8")
for iterator, line in enumerate(f_en.readlines()):
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    if iterator not in deletion_flag:
        f_new_en.write(s)

f_en.close()
f_new_en.close()

f_sl = open(europarl_sl, "r", encoding="utf8")
f_new_sl = open("data/special/special-corr.sl", "x", encoding="utf8")
for iterator, line in enumerate(f_sl.readlines()):
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    if iterator not in deletion_flag:
        f_new_sl.write(s)

f_sl.close()
f_new_sl.close()