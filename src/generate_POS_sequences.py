# -*- coding: utf-8 -*-

import frog
import re


with open("./data/pos.translated.tok", "r") as f_in:
    pos_trans_list = [l for l in f_in]
with open("./data/neg.translated.tok", "r") as f_in:
    neg_trans_list = [l for l in f_in]



frog = frog.Frog(frog.FrogOptions(parser=False, ner=False, tok=False))
p = re.compile('(ADJ|BW|LID|N|SPEC|TSW|TW|VG|VNW|VZ|WW|LET)\((.*)\)')

def parse_pos(pos):
    m = p.match(pos)    
    coarse = m.group(1)
    fine = m.group(2)
    return coarse, fine.split(",")

X_pos = [
    [parse_pos(t["pos"])[0] for t in frog.process(sent)]
    
    for sent in pos_trans_list
]
X_neg = [
    [parse_pos(t["pos"])[0] for t in frog.process(sent)]
    
    for sent in neg_trans_list
]

with open("./data/parsed/positive_pos_coarse.txt", "w") as f:
    for s in X_pos:
        f.write(" ".join(s)+'\n')
with open("./data/parsed/negative_pos_coarse.txt", "w") as f:
    for s in X_neg:
        f.write(" ".join(s)+'\n')
