def impute_bin_mean(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a pandas dataframe'''
    
    import pandas as pd
    
    
    data = df.fillna(df.groupby(["one_hot_Manufacturing","one_hot_Other","one_hot_Public Services"]).transform('mean'))
    
   
    return data


def impute_bin_median(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a pandas dataframe for use in sklearn preprocessing'''
    
    import pandas as pd
    
    data = df.fillna(df.groupby(["one_hot_Manufacturing","one_hot_Other","one_hot_Public Services"]).transform('median'))
   
    return data