import numpy as np
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
#reference: https://stackoverflow.com/questions/11604653/add-command-line-arguments-with-flags-in-python3/11604777
parser.add_argument("-p" , "--path" , help="path")
args=parser.parse_args()
df = pd.read_csv(args.path, header=None)
mat = df.to_numpy()
l = mat.flatten("C")
l = np.sort(l)
#reference: https://www.kite.com/python/answers/how-to-count-frequency-of-unique-values-in-a-numpy-array-in-python
(elems, cnt)= np.unique(l,return_counts=True)
print(elems)
print(cnt)
print(elems[-2])
