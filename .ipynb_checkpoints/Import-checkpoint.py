import pandas as pd

def data_import(file):
    data= pd.read_excel(file, header=0)
    return data