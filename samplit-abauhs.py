import argparse
import pandas as pd
import numpy as np

#get the filename from the command line
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

#read file and sample 1% of the data
df = pd.read_csv(args.filename)
df_s = df[np.random.random(len(df)) < 0.01]

#print
print(df_s.to_string())

# python samplit-abauhs.py nobel-prize-laureates.csv

#Im getting lost

