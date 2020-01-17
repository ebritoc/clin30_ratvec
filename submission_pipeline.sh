#!/usr/bin/env bash

pip install -e .

python translation_preprocessing $1 $2

# CLIN27 translation tool
git clone https://github.com/eriktks/clin2017st.git
cd clin2017st
make
bin/tokenize < clin30/positive_stripped.txt > pos.tok
bin/tokenize < clin30/negative.txt > neg.tok
bin/translate -l lexicon.txt < pos.tok > pos.translated.tok
bin/translate -l lexicon.txt < neg.tok > neg.translated.tok
cd ..

python generate_POS_sequences.py

cat ./data/parsed/positive_pos_coarse.txt ./data/parsed/positive_neg_coarse.txt > ./data/parsed/all_pos_coarse.txt
ratvec train -s " " -f ./data/parsed/all_pos_coarse.txt  -r ./data/CGN/POS_coarse_sequences3000.txt  -d ./output/2-spectrum/3000 --sim p_spectrum --n-ngram 2 &
ratvec evaluate_clin30 -d ./output/2-spectrum/3000 -n 100 &