def impute(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a numpy ndarray for use in sklearn preprocessing'''
   
    data = df.apply(lambda x: x.fillna(x.mean()),axis=0)
    data = data.values
   
    return data