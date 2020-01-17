# RatVec approach for the CLIN30 shared task on small data for predicting perfect doubling



You can reproduce our submitted results by executing the provided bash script following the format specified in the shared task instructions:
```bash
bash submission_pipeline.sh positive stripped.csv negative.csv
```

However, the whole pipeline may take a while since it involves the installation of several third-party tools. You can also use the provided preprocessed data and execute just the three last lines of the script:
```bash
pip install -e .
ratvec train -s " " -f ./data/parsed/all_pos_coarse.txt  -r ./data/CGN/POS_coarse_sequences3000.txt  -d ./output/2-spectrum/3000 --sim p_spectrum --n-ngram 2 
ratvec evaluate_clin30 -d ./output/2-spectrum/3000 -n 100 
```
We recommend to execute the scripts on a [LaMachine](https://proycon.github.io/LaMachine) environment to ease the installation of the necessary components.
