
# EVALUATION
from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.chrf_score import corpus_chrf
from nltk.translate.gleu_score import corpus_gleu
from nltk.translate.meteor_score import meteor_score
from nltk.translate.nist_score import corpus_nist
from nltk.translate.ribes_score import corpus_ribes
import statistics

# ASSISTANT DATA

# EN SL
with open('data/assistant_data/translation/en_sl/10k/output-en_sl10k-corr.txt', 'r', encoding="utf8") as myfile:
    output0 = myfile.readlines()

output = [x.split(' ') for x in output0]

with open('data/assistant_data/asistent_testset-corr.sl', 'r', encoding="utf8") as myfile2:
    slo_testset0 = myfile2.readlines()
slo_testset = [x.split(' ') for x in slo_testset0]
slo_testset2 = [[x] for x in slo_testset]

print("EN-SL")
print("BLEU: ", corpus_bleu(slo_testset2, output))
print("CHRF: ", corpus_chrf(slo_testset, output))
print("GLEU: ", corpus_gleu(slo_testset2, output))
print("NIST: ", corpus_nist(slo_testset2, output))
try:
    print("RIBES: ", corpus_ribes(slo_testset2, output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE

meteor_scores = []
for i in range(len(slo_testset)):
    meteor_scores.append(meteor_score([slo_testset0[i]], output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.051330726152354234
# CHRF:  0.2357208402675213
# GLEU:  0.08137303482138836
# NIST:  1.9600814066389685
# RIBES: Error with RIBES division by zero
# METEOR:  0.24559112309731732

# SL EN
with open('data/assistant_data/translation/sl_en/10k/output-sl_en10k-corr.txt', 'r', encoding="utf8") as myfile3:
    en_output0 = myfile3.readlines()

en_output = [x.split(' ') for x in en_output0]

with open('data/assistant_data/asistent_testset-corr.en', 'r', encoding="utf8") as myfile4:
    en_testset0 = myfile4.readlines()
en_testset = [x.split(' ') for x in en_testset0]
en_testset2 = [[x] for x in en_testset]

print("SL-EN")
print("BLEU: ", corpus_bleu(en_testset2, en_output))
print("CHRF: ", corpus_chrf(en_testset, en_output))
print("GLEU: ", corpus_gleu(en_testset2, en_output))
print("NIST: ", corpus_nist(en_testset2, en_output))
try:
    print("RIBES: ", corpus_ribes(en_testset2, en_output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(en_testset)):
    meteor_scores.append(meteor_score([en_testset0[i]], en_output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.05361978033233083
# CHRF:  0.24929311263385426
# GLEU:  0.08150863461206216
# NIST:  1.9861340052006444
# RIBES: Error with RIBES division by zero
# METEOR:  0.2546687046790273

# SPECIALISED DATA

# EN SL
with open('data/special/translation/en_sl/15k/output-en_sl_specialized_model.txt', 'r', encoding="utf8") as myfile:
    output0 = myfile.readlines()

output = [x.split(' ') for x in output0]

with open('data/special/special-corr-test.sl', 'r', encoding="utf8") as myfile2:
    slo_testset0 = myfile2.readlines()
slo_testset = [x.split(' ') for x in slo_testset0]
slo_testset2 = [[x] for x in slo_testset]

print("EN-SL Special data, special model")
print("BLEU: ", corpus_bleu(slo_testset2, output))
print("CHRF: ", corpus_chrf(slo_testset, output))
print("GLEU: ", corpus_gleu(slo_testset2, output))
print("NIST: ", corpus_nist(slo_testset2, output))
try:
    print("RIBES: ", corpus_ribes(slo_testset2, output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(slo_testset)):
    meteor_scores.append(meteor_score([slo_testset0[i]], output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.2198951196578901
# CHRF:  0.39340467628950954
# GLEU:  0.20611685099442636
# NIST:  4.931799025732957
# RIBES: Error with RIBES division by zero
# METEOR:  0.409657973908508

# SL EN
with open('data/special/translation/sl_en/15k/output-sl_en_specialized.txt', 'r', encoding="utf8") as myfile3:
    en_output0 = myfile3.readlines()

en_output = [x.split(' ') for x in en_output0]

with open('data/special/special-corr-test.en', 'r', encoding="utf8") as myfile4:
    en_testset0 = myfile4.readlines()
en_testset = [x.split(' ') for x in en_testset0]
en_testset2 = [[x] for x in en_testset]

print("SL-EN Special data, special model")
print("BLEU: ", corpus_bleu(en_testset2, en_output))
print("CHRF: ", corpus_chrf(en_testset, en_output))
print("GLEU: ", corpus_gleu(en_testset2, en_output))
print("NIST: ", corpus_nist(en_testset2, en_output))
try:
    print("RIBES: ", corpus_ribes(en_testset2, en_output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(en_testset)):
    meteor_scores.append(meteor_score([en_testset0[i]], en_output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.2873617688389729
# CHRF:  0.4816203078065288
# GLEU:  0.2887775933731843
# NIST:  6.546765681185366
# RIBES: Error with RIBES division by zero
# METEOR:  0.517152829012708


# SPECIALISED DATA, General model

# EN SL
with open('data/special/translation/en_sl/15k/output-en_sl-general_model.txt', 'r', encoding="utf8") as myfile:
    output0 = myfile.readlines()

output = [x.split(' ') for x in output0]

with open('data/special/special-corr-test.sl', 'r', encoding="utf8") as myfile2:
    slo_testset0 = myfile2.readlines()
slo_testset = [x.split(' ') for x in slo_testset0]
slo_testset2 = [[x] for x in slo_testset]

print("EN-SL Special data, General model")
print("BLEU: ", corpus_bleu(slo_testset2, output))
print("CHRF: ", corpus_chrf(slo_testset, output))
print("GLEU: ", corpus_gleu(slo_testset2, output))
print("NIST: ", corpus_nist(slo_testset2, output))
try:
    print("RIBES: ", corpus_ribes(slo_testset2, output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(slo_testset)):
    meteor_scores.append(meteor_score([slo_testset0[i]], output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.04217453624347013
# CHRF:  0.18935211213292338
# GLEU:  0.06255520719076693
# NIST:  1.5254853132429693
# RIBES: Error with RIBES division by zero
# METEOR:  0.21134677650991632

# SL EN
with open('data/special/translation/sl_en/15k/output-sl_en_general.txt', 'r', encoding="utf8") as myfile3:
    en_output0 = myfile3.readlines()

en_output = [x.split(' ') for x in en_output0]

with open('data/special/special-corr-test.en', 'r', encoding="utf8") as myfile4:
    en_testset0 = myfile4.readlines()
en_testset = [x.split(' ') for x in en_testset0]
en_testset2 = [[x] for x in en_testset]

print("SL-EN Special data, General model")
print("BLEU: ", corpus_bleu(en_testset2, en_output))
print("CHRF: ", corpus_chrf(en_testset, en_output))
print("GLEU: ", corpus_gleu(en_testset2, en_output))
print("NIST: ", corpus_nist(en_testset2, en_output))
try:
    print("RIBES: ", corpus_ribes(en_testset2, en_output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(en_testset)):
    meteor_scores.append(meteor_score([en_testset0[i]], en_output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.03258947162289811
# CHRF:  0.18003877957561928
# GLEU:  0.050288711198377536
# NIST:  1.2350933239500113
# RIBES: Error with RIBES division by zero
# METEOR:  0.18999680812604094





# SPECIALISED DATA, General and specialised model, only en_sl
#

# General model 100k, special data
with open('data/special/translation/en_sl/output-en_sl100k-corr.txt', 'r', encoding="utf8") as myfile:
    output0 = myfile.readlines()

output = [x.split(' ') for x in output0]

with open('data/special/special-corr-test.sl', 'r', encoding="utf8") as myfile2:
    slo_testset0 = myfile2.readlines()
slo_testset = [x.split(' ') for x in slo_testset0]
slo_testset2 = [[x] for x in slo_testset]

print("EN-SL Special data, General model 100k, vocab 50k")
print("BLEU: ", corpus_bleu(slo_testset2, output))
print("CHRF: ", corpus_chrf(slo_testset, output))
print("GLEU: ", corpus_gleu(slo_testset2, output))
print("NIST: ", corpus_nist(slo_testset2, output))
try:
    print("RIBES: ", corpus_ribes(slo_testset2, output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(slo_testset)):
    meteor_scores.append(meteor_score([slo_testset0[i]], output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.17564465631708243
# CHRF:  0.35934562201847237
# GLEU:  0.19687343690509074
# NIST:  4.517113259772697
# RIBES: Error with RIBES division by zero
# METEOR:  0.38298733381991457

# Specialised model 130k, special data
with open('data/special/translation/en_sl/output-en_sl130k-corr.txt', 'r', encoding="utf8") as myfile3:
    en_output0 = myfile3.readlines()

en_output = [x.split(' ') for x in en_output0]

with open('data/special/special-corr-test.sl', 'r', encoding="utf8") as myfile4:
    en_testset0 = myfile4.readlines()
en_testset = [x.split(' ') for x in en_testset0]
en_testset2 = [[x] for x in en_testset]

print("EN-SL Special data, Special model 130k, 50k vocab")
print("BLEU: ", corpus_bleu(en_testset2, en_output))
print("CHRF: ", corpus_chrf(en_testset, en_output))
print("GLEU: ", corpus_gleu(en_testset2, en_output))
print("NIST: ", corpus_nist(en_testset2, en_output))
try:
    print("RIBES: ", corpus_ribes(en_testset2, en_output))
except Exception as err:
    print("Error with RIBES", err)

# AVG METEOR SCORE
meteor_scores = []
for i in range(len(en_testset)):
    meteor_scores.append(meteor_score([en_testset0[i]], en_output0[i]))

print("METEOR: ", statistics.mean(meteor_scores))

# BLEU:  0.24220801130477004
# CHRF:  0.4194497275062216
# GLEU:  0.257127266747395
# NIST:  5.606371857492066
# RIBES: Error with RIBES division by zero
# METEOR:  0.4454680595010666
