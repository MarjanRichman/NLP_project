# randomize the file lines

import random

rand_array = []
with open("data/combined_corpora-en.txt", 'r', encoding="utf-16") as source:
    data_en = []
    for line in source:
        temp_rand = random.random()
        rand_array.append(temp_rand)
        data_en.append((temp_rand, line))
    # data_en = [ (temp_rand, line) for line in source ]
data_en.sort(key=lambda tup:tup[0])
with open('data/combined_corpora-en-shuffled.txt', 'w', encoding="utf-16") as target:
    for _, line in data_en:
        target.write( line )

data_en = []
with open("data/combined_corpora-sl.txt", 'r', encoding="utf-16") as source2:
    data_sl = []
    for iterator, line in enumerate(source2):
        data_sl.append((rand_array[iterator], line))
    # data_sl = [ (rand_array[iterator], line) for line in source2 ]

data_sl.sort(key=lambda tup:tup[0])
with open('data/combined_corpora-sl-shuffled.txt','w', encoding="utf-16") as target2:
    for _, line in data_sl:
        target2.write( line )