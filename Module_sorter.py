import pandas as pd
import numpy as np
import os 
import glob
import time

pd.options.mode.chained_assignment = None  # default='warn'

def closest(list1, list2, k):
    return(list1[np.abs(list1 - list2[k]).argmin()])

def get_values(files):

    for file in files:
        ### Loading the chromosomes
        start = time.time()
        print('working on ', file)

        footprint = pd.read_csv(file, "\t")
        footprint = footprint.sort_values(by ="Chr")

        # print(footprint.head())
        # print(file)
        # print(file[:4])

        chromosomes = ['chr1', 'chrY', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15',
            'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21',
            'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9',
            'chrX']  

        #Where the magic happens

        for chromosome in chromosomes[:]:

            try:
                tmp_modules = modules[modules.chr == chromosome]
                tmp_modules = tmp_modules.reset_index()

                tmp_tf_footprints = footprint[footprint.Chr == chromosome]
                tmp_tf_footprints = tmp_tf_footprints.reset_index()

                tmp_tf_footprints['strand'] = str(file[:6])
                
                for i, y in enumerate(tmp_tf_footprints['tf_c1']):
                    x1 = closest(tmp_modules['start'], tmp_tf_footprints['tf_c1'], i)
                    x2 = tmp_modules[tmp_modules['start'] == x1]['end'].iloc[-1]

                    if (x1 < y < x2):
                        tmp_tf_footprints['Unnamed: 9'][i] = tmp_modules[tmp_modules['start'] == x1]['Peak'].iloc[-1]
                        tmp_tf_footprints['num'][i] = tmp_modules[tmp_modules['start'] == x1]['Module'].iloc[-1]

                if chromosome == 'chr1':
                    out_csv = tmp_tf_footprints
                else:
                    out_csv = pd.concat([out_csv, tmp_tf_footprints])
            except:
                pass

        out_csv.to_csv(file[:6] + '_output.tsv')

        ### Time it for fun
        end = time.time()
        print(end - start)

cur_dir = os.getcwd()
entries = os.listdir(cur_dir)


#print("Found %s entries in %s" % (len(entries), cur_dir)) 
#print('-' * 10)

path = "./"
extension_csv = 'csv'
extension_txt = 'txt'
os.chdir(path)
result = glob.glob('*.{}'.format(extension_csv))

modules = pd.read_csv(result[0])
modules = modules.sort_values(by = ['chr','start'])

## Type of files load
print("How do you want to load filess?: A/M")
loader = input("")

if(loader == 'A'):
# Automatically Load the filess
    # Result_2 files will be changing but I will done that later (a lot of filess will be inputted)
    result_2 = glob.glob('*.{}'.format(extension_txt))
    #print(result_2)
    get_values(result_2)
elif(loader == 'M'):
    result_2 = [input()]
    get_values(result_2)
else:
    print('bye bye')