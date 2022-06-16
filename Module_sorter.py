import pandas as pd
import numpy as np
import os 

cur_dir = os.getcwd()
entries = os.listdir(cur_dir)

print("Found %s entries in %s" % (len(entries), cur_dir))
print('-' * 10)

[print(entry) if '.py' in entry in entries]

# footprint = pd.read_csv()


# TF_footprints = pd.read_csv('P503_5.ATAC.peaks.TF.info.txt', "\t")
# TF_footprints = TF_footprints.sort_values(by ="Chr")