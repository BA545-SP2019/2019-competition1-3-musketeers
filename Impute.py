def impute_mean(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a numpy ndarray for use in sklearn preprocessing'''
    
    import pandas as pd
    
    data = df.apply(lambda x: x.fillna(x.mean()),axis=0)
    data = data.values
   
    return data



def impute_median(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a numpy ndarray for use in sklearn preprocessing'''
    
    import pandas as pd
    
    data = df.apply(lambda x: x.fillna(x.median()),axis=0)
    data = data.values
   
    return data