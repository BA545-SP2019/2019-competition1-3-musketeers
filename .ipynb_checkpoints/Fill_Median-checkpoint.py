import pandas as pd

def F_Median(x):
    for col in x.columns[x]:
    x[col] = x[col].fillna(x[col].median()):
        
        