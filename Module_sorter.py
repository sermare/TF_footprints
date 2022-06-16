import pandas as pd
import numpy as np
import os 
import glob

cur_dir = os.getcwd()
entries = os.listdir(cur_dir)

print("Found %s entries in %s" % (len(entries), cur_dir))
print('-' * 10)

path = "./"
extension_csv = 'csv'
extension_txt = 'txt'
os.chdir(path)
result = glob.glob('*.{}'.format(extension_csv))

modules = pd.read_csv(result[0])
modules = modules.sort_values(by = ['chr','start'])

tmp_modules = modules[modules.chr == 'chr1']
tmp_modules = tmp_modules.reset_index()

result_2 = glob.glob('*.{}'.format(extension_txt))

footprint = pd.read_csv(result_2[0], "\t")
footprint = footprint.sort_values(by ="Chr")

tmp_tf_footprints = footprint[footprint.Chr == 'chr1']
tmp_tf_footprints = tmp_tf_footprints.reset_index()

def closest(list1, list2, k):
    return(list1[np.abs(list1 - list2[k]).argmin()])

for i, y in enumerate(tmp_tf_footprints['tf_c1']):
    x1 = closest(tmp_modules['start'], tmp_tf_footprints['tf_c1'], i)
    x2 = tmp_modules[tmp_modules['start'] == x1]['end'].iloc[-1]

    if (x1 < y < x2):
        tmp_tf_footprints['Unnamed: 9'][i] = tmp_modules[tmp_modules['start'] == x1]['Module'].iloc[-1]
    
print('fucking done')