# combine files

filenames = ['data/special/ECDC.en', 'data/special/EMEA.en']
with open('data/special/special.en', 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)

filenames = ['data/special/ECDC.sl', 'data/special/EMEA.sl']
with open('data/special/special.sl', 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)