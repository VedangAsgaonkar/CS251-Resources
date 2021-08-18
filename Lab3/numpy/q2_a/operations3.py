import numpy as np
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
#reference: https://stackoverflow.com/questions/11604653/add-command-line-arguments-with-flags-in-python3/11604777
parser.add_argument("-p" , "--path" , help="path")
args=parser.parse_args() 
df = pd.read_csv(args.path, header=None)
mat = df.to_numpy()
#reference: https://numpy.org/doc/stable/reference/generated/numpy.sort.html
print(np.sort(mat,0))
print(np.sort(mat))
#reference: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html
print(np.sort(mat.flatten('C')))
