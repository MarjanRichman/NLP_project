import re
import os

# # SPECIAL
# europarl_en = 'data/special/special.en'
# f_en = open(europarl_en, "r", encoding="utf8")
# deletion_flag = []
# for iterator, line in enumerate(f_en.readlines()):
#     if line == '\n':
#         deletion_flag.append(iterator)
#
# europarl_sl = 'data/special/special.sl'
# f_sl = open(europarl_sl, "r", encoding="utf8")
#
# for iterator, line in enumerate(f_sl.readlines()):
#     if line == '\n':
#         deletion_flag.append(iterator)
# f_en.close()
# f_sl.close()
# f_en = open(europarl_en, "r", encoding="utf8")
#
# f_new_en = open("data/special/special-corr.en", "x", encoding="utf8")
# for iterator, line in enumerate(f_en.readlines()):
#     s = line
#     s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#     s = re.sub('\s{2,}', ' ', s)
#     if '\n' not in s:
#         s = s+'\n'
#     if iterator not in deletion_flag:
#         f_new_en.write(s)
#
# f_en.close()
# f_new_en.close()
#
# f_sl = open(europarl_sl, "r", encoding="utf8")
# f_new_sl = open("data/special/special-corr.sl", "x", encoding="utf8")
# for iterator, line in enumerate(f_sl.readlines()):
#     s = line
#     s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#     s = re.sub('\s{2,}', ' ', s)
#     if '\n' not in s:
#         s = s+'\n'
#     if iterator not in deletion_flag:
#         f_new_sl.write(s)
#
# f_sl.close()
# f_new_sl.close()


# # Europarl
# europarl_en = 'data/europarl/europarl-v7.en.txt'
# f_en = open(europarl_en, "r", encoding="utf8")
# deletion_flag = []
# for iterator, line in enumerate(f_en.readlines()):
#     if line == '\n':
#         deletion_flag.append(iterator)
#
# europarl_sl = 'data/europarl/europarl-v7.sl.txt'
# f_sl = open(europarl_sl, "r", encoding="utf8")
#
# for iterator, line in enumerate(f_sl.readlines()):
#     if line == '\n':
#         deletion_flag.append(iterator)
# f_en.close()
# f_sl.close()
# f_en = open(europarl_en, "r", encoding="utf8")
#
# f_new_en = open("data/europarl/europarl-en-corr3.txt", "x", encoding="utf-16")
# for iterator, line in enumerate(f_en.readlines()):
#     s = line
#     s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#     s = re.sub('\s{2,}', ' ', s)
#     if '\n' not in s:
#         s = s+'\n'
#     if iterator not in deletion_flag:
#         f_new_en.write(s)
#
# f_en.close()
# f_new_en.close()
#
# f_sl = open(europarl_sl, "r", encoding="utf8")
# f_new_sl = open("data/europarl/europarl-sl-corr3.txt", "x", encoding="utf-16")
# for iterator, line in enumerate(f_sl.readlines()):
#     s = line
#     s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#     s = re.sub('\s{2,}', ' ', s)
#     if '\n' not in s:
#         s = s+'\n'
#     if iterator not in deletion_flag:
#         f_new_sl.write(s)
#
# f_sl.close()
# f_new_sl.close()
#
#
# # AGS
#
# for filename in os.listdir('data/AC_AGS/AGS_text'):
#     file = 'data/AC_AGS/AGS_text/'+filename
#     f = open(file, "r", encoding="utf8")
#     f_new = open("data/AC_AGS/AGS_text/"+filename.replace(".txt", "")+"_corr.txt", "x", encoding="utf8")
#
#     for line in f.readlines():
#         s = line
#         s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#         s = re.sub('\s{2,}', ' ', s)
#         if '\n' not in s:
#             s = s+'\n'
#         f_new.write(s)
#
#     f.close()
#     f_new.close()
#
# # AC
#
# for filename in os.listdir('data/AC_AGS/AC_summary_text'):
#     file = 'data/AC_AGS/AC_summary_text/'+filename
#     f = open(file, "r", encoding="utf8")
#     f_new = open("data/AC_AGS/AC_summary_text/"+filename.replace(".txt", "")+"_corr.txt", "x", encoding="utf8")
#
#     for line in f.readlines():
#         s = line
#         s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
#         s = re.sub('\s{2,}', ' ', s)
#         if '\n' not in s:
#             s = s+'\n'
#         f_new.write(s)
#
#     f.close()
#     f_new.close()


# randomize the file lines

# import random
#
# rand_array = []
# with open("data/combined_corpora-en.txt", 'r', encoding="utf-16") as source:
#     data_en = []
#     for line in source:
#         temp_rand = random.random()
#         rand_array.append(temp_rand)
#         data_en.append((temp_rand, line))
#     # data_en = [ (temp_rand, line) for line in source ]
# data_en.sort(key=lambda tup:tup[0])
# with open('data/combined_corpora-en-shuffled.txt', 'w', encoding="utf-16") as target:
#     for _, line in data_en:
#         target.write( line )
#
# data_en = []
# with open("data/combined_corpora-sl.txt", 'r', encoding="utf-16") as source2:
#     data_sl = []
#     for iterator, line in enumerate(source2):
#         data_sl.append((rand_array[iterator], line))
#     # data_sl = [ (rand_array[iterator], line) for line in source2 ]
#
# data_sl.sort(key=lambda tup:tup[0])
# with open('data/combined_corpora-sl-shuffled.txt','w', encoding="utf-16") as target2:
#     for _, line in data_sl:
#         target2.write( line )



# # combine files
#
# filenames = ['data/special/ECDC.en', 'data/special/EMEA.en']
# with open('data/special/special.en', 'w', encoding="utf-8") as outfile:
#     for fname in filenames:
#         with open(fname, encoding="utf-8") as infile:
#             for line in infile:
#                 outfile.write(line)
#
# filenames = ['data/special/ECDC.sl', 'data/special/EMEA.sl']
# with open('data/special/special.sl', 'w', encoding="utf-8") as outfile:
#     for fname in filenames:
#         with open(fname, encoding="utf-8") as infile:
#             for line in infile:
#                 outfile.write(line)

# split the combined shuffled file into train, test, validation

# with open('data/europarl/europarl-en-corr3-shuffled.txt', 'r', encoding="utf-16") as myfile:
#     X = myfile.readlines()
# with open('data/europarl/europarl-sl-corr3-shuffled.txt', 'r', encoding="utf-16") as myfile2:
#     y = myfile2.readlines()

# from sklearn.model_selection import train_test_split
# X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.000205, random_state=1)
#
#
# #  GENERAL CORPORA
# # EN
# with open('data/assistant_data/TC3-train.en','w', encoding="utf8") as target:
#     for line in X_train:
#         target.write(line)
#
# with open('data/assistant_data/TC3-val.en','w', encoding="utf8") as target2:
#     for line in X_val:
#         target2.write(line)
#
# # SL
# with open('data/assistant_data/TC3-train.sl','w', encoding="utf8") as target4:
#     for line in y_train:
#         target4.write(line)
#
# with open('data/assistant_data/TC3-val.sl','w', encoding="utf8") as target5:
#     for line in y_val:
#         target5.write(line)


# SPECIALIZED CORPORA
from sklearn.model_selection import train_test_split
with open('data/special/special-corr.en', 'r', encoding="utf8") as myfile:
    X = myfile.readlines()
with open('data/special/special-corr.sl', 'r', encoding="utf8") as myfile2:
    y = myfile2.readlines()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0059, random_state=1)  # 0.0059 * 340742 = 2010

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.015, random_state=1) # 0,015 * 338732 = 5080 validation
# EN
with open('data/special/special-corr-train.en','w', encoding="utf8") as target:
    for line in X_train:
        target.write(line)

with open('data/special/special-corr-test.en','w', encoding="utf8") as target2:
    for line in X_test:
        target2.write(line)

with open('data/special/special-corr-val.en','w', encoding="utf8") as target3:
    for line in X_val:
        target3.write(line)

# SL
with open('data/special/special-corr-train.sl','w', encoding="utf8") as target4:
    for line in y_train:
        target4.write(line)

with open('data/special/special-corr-test.sl','w', encoding="utf8") as target5:
    for line in y_test:
        target5.write(line)

with open('data/special/special-corr-val.sl','w', encoding="utf8") as target6:
    for line in y_val:
        target6.write(line)

# useful info
#
# # test string
# # s = "European* Agency \"for\" \'Reco=nst/ruct+ion\' (vote) 25. $3-4 {The} pr@otec_tion an€d welfare "
#
# # preprocess the data
# "onmt_preprocess -train_src data/europarl/europarl-en-corr-train.txt -train_tgt " \
# "data/europarl/europarl-sl-corr-train.txt -valid_src data/europarl/europarl-en-corr-val.txt -valid_tgt" \
# "data/europarl/europarl-sl-corr-val.txt -save_data data/europarl/result"
#
# onmt_preprocess -train_src data/src-train.txt -train_tgt
# data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt
# data/tgt-val.txt -save_data data/demo
#
# "onmt_train -data data/europarl/result -save_model en_slo-model"