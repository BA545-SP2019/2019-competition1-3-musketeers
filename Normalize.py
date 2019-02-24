def minmax_scale(df):
    '''takes in numpy ndarray and returns a normalized dataset through sklearn's min_max scaler.
    returns a fully transformed pandas dataframe.'''
    
    from sklearn import preprocessing
    import numpy as np
    import pandas as pd
    scaler = preprocessing.MinMaxScaler()
    dataset_minmax = scaler.fit_transform(df)
    
    return dataset_minmax