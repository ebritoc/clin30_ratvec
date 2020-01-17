# -*- coding: utf-8 -*-

import modin.pandas as pd
import sys

sys.argv[1]
df_stripped = pd.read_csv(sys.argv[1])
df_neg = pd.read_csv(sys.argv[2])
neg_text_list = list(df_neg["context"])
stripped_text_list = list(df_stripped["context"]) 

with open("../data/positive_stripped.txt", "w") as f:    
        f.write("\n".join(stripped_text_list)+'\n')
        
with open("../data/negative.txt", "w") as f:    
        f.write("\n".join(neg_text_list)+'\n')

