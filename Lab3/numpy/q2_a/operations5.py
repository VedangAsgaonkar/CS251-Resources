import numpy as np
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
#reference: https://stackoverflow.com/questions/11604653/add-command-line-arguments-with-flags-in-python3/11604777
parser.add_argument("-p" , "--path" , help="path")
parser.add_argument("-n","--num",help="number")
args=parser.parse_args()
num = int(args.num1)
df = pd.read_csv(args.path, header=None)
mat = df.to_numpy()
mat = np.pad(mat,num)
print(mat)