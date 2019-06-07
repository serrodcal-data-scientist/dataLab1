import numpy as np
import pandas as pd
from scipy.io import arff
import matplotlib.pyplot as plt

def pretty_print(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)

if __name__ == '__main__':

    # Load data as numpy array from ARFF file using scipy library
    data, meta = arff.loadarff('autos.arff')

    # Shape is (205, 0), so there are 205 tuples
    # Load data into a Pandas' DataFrame, using range function to generate column index, meta for naming columns and data for the information
    df = pd.DataFrame(data=data, index=range(len(data)), columns=meta)

    print(df.head())

    # TODO: Check any error in datas before?

    # Since make column is actually a categorical column I'm going to convert it to several columns.
    #df = pd.pivot_table(df, columns='make', index=['autos'], values='make') # This doesn't work, fuck

    # Convert make colum from binary to str
    #df['make'] = df['make'].astype('str') # This also doesn't work, fuck
