# split the combined shuffled file into train, test, validation

with open('data/europarl/europarl-en-corr3-shuffled.txt', 'r', encoding="utf-16") as myfile:
    X = myfile.readlines()
with open('data/europarl/europarl-sl-corr3-shuffled.txt', 'r', encoding="utf-16") as myfile2:
    y = myfile2.readlines()

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.000205, random_state=1)


#  GENERAL CORPORA
# EN
with open('data/assistant_data/TC3-train.en','w', encoding="utf8") as target:
    for line in X_train:
        target.write(line)

with open('data/assistant_data/TC3-val.en','w', encoding="utf8") as target2:
    for line in X_val:
        target2.write(line)

# SL
with open('data/assistant_data/TC3-train.sl','w', encoding="utf8") as target4:
    for line in y_train:
        target4.write(line)

with open('data/assistant_data/TC3-val.sl','w', encoding="utf8") as target5:
    for line in y_val:
        target5.write(line)


# SPECIALIZED CORPORA

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