def minmax_scale(df):
    '''takes in pandas dataframe and returns a normalized dataset through sklearn's min_max scaler.
    Returns a fully transformed pandas dataframe.'''
    
    from sklearn import preprocessing
    import numpy as np
    import pandas as pd
    
    #create a numpy ndarray for use in sklearn
    df = df.values
    scaler = preprocessing.MinMaxScaler()
    dataset_minmax = scaler.fit_transform(df)
    dataset_minmax = pd.DataFrame(dataset_minmax)
    return dataset_minmax



def z_score(df):
    '''transorm a pandas dataframe using a z-score transformation
    returns a pandas dataframe'''
    
    from sklearn import preprocessing
    data = df.values
    scaler = preprocessing.StandardScaler()
    
    data_scaled = scaler.fit_transform(data)
    
    df = pd.DataFrame(data_scaled)
    
    return df