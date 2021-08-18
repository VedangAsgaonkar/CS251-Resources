import argparse
import scipy.integrate as integrate


parser = argparse.ArgumentParser()
parser.add_argument("list",type = float,action = 'append',nargs = '+')
args = parser.parse_args()
print(args.list)
limits = args.list[0]
print(integrate.tplquad(lambda x,y,z:(x*y*z)**2 ,*limits)[0])
