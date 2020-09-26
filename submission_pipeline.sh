#!/usr/bin/env bash

pip install -e .

python ./src/translation_preprocessing.py $1 $2

# CLIN27 translation tool
git clone https://github.com/eriktks/clin2017st.git
cd clin2017st
make
bin/tokenize < ../data/positive_stripped.txt > pos.tok
bin/tokenize < ../data/negative.txt > neg.tok
bin/translate -l lexicon.txt < pos.tok > ../data/pos.translated.tok
bin/translate -l lexicon.txt < neg.tok > ../data/neg.translated.tok
cd ..

python ./src/generate_POS_sequences.py

cat ./data/parsed/positive_pos_coarse.txt ./data/parsed/negative_pos_coarse.txt > ./data/parsed/all_pos_coarse.txt
ratvec train -s " " -f ./data/parsed/all_pos_coarse.txt  -r ./data/CGN/POS_coarse_sequences3000.txt  -d ./output/2-spectrum/3000 --sim p_spectrum --n-ngram 2 &
ratvec evaluate_clin30 -d ./output/2-spectrum/3000 -n 100 &
