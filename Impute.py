def impute_mean(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a pandas dataframe'''
    
    import pandas as pd
    
    data = df.apply(lambda x: x.fillna(x.mean()),axis=0)
    
   
    return data



def impute_median(df):
    '''Takes in a pandas dataframe and imputes a column's mean value into missing values.
    Returns a pandas dataframe for use in sklearn preprocessing'''
    
    import pandas as pd
    
    data = df.apply(lambda x: x.fillna(x.median()),axis=0)
   
    return data


def impute_knn(df, k_num):
    '''impute missing values using a KNN implementation.
    Using the Impyute library, use a KNN model to impute into missing values. 
    Input a pandas dataframe of the Competition 1 dataset, along with the desired number of neighbors to consider.
    Outputs a non-null pandas dataframe
    .'''
    
    import pandas as pd
    import  impyute.imputation
    data = df.values
    data = impyute.imputation.cs.fast_knn(df, k=k_num)
    data = pd.DataFrame(data)
    
    return data