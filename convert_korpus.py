import re
import os


# Europarl
europarl_en = 'data/europarl/europarl-v7.en.txt'
f_en = open(europarl_en, "r", encoding="utf8")
f_new_en = open("data/europarl/europarl-en-corr.txt", "x", encoding="utf8")

for line in f_en.readlines():
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    f_new_en.write(s)

f_en.close()
f_new_en.close()

europarl_sl = 'data/europarl/europarl-v7.sl.txt'
f_sl = open(europarl_sl, "r", encoding="utf8")
f_new_sl = open("data/europarl/europarl-sl-corr.txt", "x", encoding="utf8")

for line in f_sl.readlines():
    s = line
    s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    if '\n' not in s:
        s = s+'\n'
    f_new_sl.write(s)

f_sl.close()
f_new_sl.close()


# AGS

for filename in os.listdir('data/AC_AGS/AGS_text'):
    file = 'data/AC_AGS/AGS_text/'+filename
    f = open(file, "r", encoding="utf8")
    f_new = open("data/AC_AGS/AGS_text/"+filename.replace(".txt", "")+"_corr.txt", "x", encoding="utf8")

    for line in f.readlines():
        s = line
        s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
        s = re.sub('\s{2,}', ' ', s)
        if '\n' not in s:
            s = s+'\n'
        f_new.write(s)

    f.close()
    f_new.close()

# AC

for filename in os.listdir('data/AC_AGS/AC_summary_text'):
    file = 'data/AC_AGS/AC_summary_text/'+filename
    f = open(file, "r", encoding="utf8")
    f_new = open("data/AC_AGS/AC_summary_text/"+filename.replace(".txt", "")+"_corr.txt", "x", encoding="utf8")

    for line in f.readlines():
        s = line
        s = re.sub('([\"\*\'.,!?_$/={}@€+])', r' \1 ', s)
        s = re.sub('\s{2,}', ' ', s)
        if '\n' not in s:
            s = s+'\n'
        f_new.write(s)

    f.close()
    f_new.close()


# test string
# s = "European* Agency \"for\" \'Reco=nst/ruct+ion\' (vote) 25. $3-4 {The} pr@otec_tion an€d welfare "







