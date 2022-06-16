import pandas as pd
import numpy as np
import os 

cur_dir = os.getcwd()
entries = os.listdir(cur_dir)

print("Found %s entries in %s" % (len(entries), cur_dir))
print('-' * 10)
for entry in entries:
    print(entry)