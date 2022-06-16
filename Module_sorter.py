import pandas as pd
import numpy as np
import os 
import glob
import time

start = time.time()

cur_dir = os.getcwd()
entries = os.listdir(cur_dir)

print("Found %s entries in %s" % (len(entries), cur_dir))
print('-' * 10)

## Load the files

path = "./"
extension_csv = 'csv'
extension_txt = 'txt'
os.chdir(path)
result = glob.glob('*.{}'.format(extension_csv))

modules = pd.read_csv(result[0])
modules = modules.sort_values(by = ['chr','start'])

## Result_2 file will be changing but I will done that later (a lot of files will be inputted)

result_2 = glob.glob('*.{}'.format(extension_txt))

footprint = pd.read_csv(result_2[0], "\t")
footprint = footprint.sort_values(by ="Chr")

def closest(list1, list2, k):
    return(list1[np.abs(list1 - list2[k]).argmin()])


### Loading the chromosomes

chromosomes = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15',
       'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21',
       'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9',
       'chrX', 'chrY']  

for chromosome in chromosomes:

    tmp_modules = modules[modules.chr == chromosome]
    tmp_modules = tmp_modules.reset_index()

    tmp_tf_footprints = footprint[footprint.Chr == chromosome]
    tmp_tf_footprints = tmp_tf_footprints.reset_index()

    for i, y in enumerate(tmp_tf_footprints['tf_c1']):
        x1 = closest(tmp_modules['start'], tmp_tf_footprints['tf_c1'], i)
        x2 = tmp_modules[tmp_modules['start'] == x1]['end'].iloc[-1]

        if (x1 < y < x2):
            pass
           # tmp_tf_footprints['Unnamed: 9'][i] = tmp_modules[tmp_modules['start'] == x1]['Module'].iloc[-1]
    
    print('fucking done with', chromosome)


### Time it for fun
end = time.time()
print(end - start)