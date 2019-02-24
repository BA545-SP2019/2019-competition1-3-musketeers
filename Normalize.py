def minmax_scale(df):
    '''takes in pandas dataframe and returns a normalized dataset through sklearn's min_max scaler.
    Returns a fully transformed pandas dataframe.'''
    
    from sklearn import preprocessing
    import numpy as np
    import pandas as pd
    
    #create a numpy ndarray for use in sklearn
    df = data.values
    scaler = preprocessing.MinMaxScaler()
    dataset_minmax = scaler.fit_transform(df)
    
    return dataset_minmax