import numpy as np 
import pandas as pd
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
parser = argparse.ArgumentParser()
parser.add_argument("--path")
parser.add_argument("--output")
args = parser.parse_args()
df = pd.read_csv(args.path , header = None , dtype = 'float64')
#print(df)
df =df - df.mean()
mat = df.to_numpy()
mat = mat.astype('float64')
#print(mat.dtype)
np.set_printoptions(precision = 8)
covariance = np.cov(mat.T)
eigval , eigvec = np.linalg.eig(covariance)
sort_index = np.flip(np.argsort(eigval))
eigval = eigval[sort_index]
eigvec = eigvec[sort_index]
print(eigval)
#print(eigvec)
eig_values = eigval[0:2]
eig_vectors= (eigvec.T[0:2]).T
#print(eig_vectors)
transformed = df.dot(eig_vectors)
#print(transformed.shape)
df = pd.DataFrame(transformed)
df.to_csv(args.output+'output.csv' , header = None , index = None)
plt.scatter(df[0],df[1])
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.savefig(args.output+'out.png')
