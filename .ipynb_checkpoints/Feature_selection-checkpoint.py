def pca_selection(df, n_component=True, var=False):
    '''Apply PCA to a dataset and return the transformed dataset as a pandas dataframe.
    You can choose whether you want to specify a number of components to keep,
    or how much variance you want to be explained, resulting in a number of features that
    explains that much variance. Uses remaining standard settings of sklearn's PCA() object.
    
    Inputs: df, a non-null, (recommended standardized) pandas dataframe you would like to apply PCA to.
            n_component; an optional argument specifying how many resulting components you want.
            var; an optional argument specifying how much variance you want the resulting dataframe to explain
            
             
    For instance, if you want to have 2 resulting components, you would call "pca_selector(df, n_component = 2)" 
    
    If you want have a dataframe of 95% variance explained, you would call "pca_selector(df, var=0.95)"
    '''
    
    from sklearn.decomposition import PCA
    import pandas as pd
   
    if n_component:
        pca = PCA(n_components = n_component)
    if var:
        pca = PCA(var)
        
    principalcomponents = pca.fit_transform(df)
    principalDF = pd.DataFrame(principalcomponents)
    
    return principalDF


def RFE(df, number, y):
    '''run the Recursive Feature Elimination to a pandas dataframe.
    Return a pandas dataframe with the user-specified number of top features as calculated by the RFE algorithm, modeled by a simple Logistic Regression.
    Need to specify which target variable, y1 or y2, you would like the RFE to model after."
    '''
    import pandas as pd
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression
    
    model = LogisticRegression()
    rfe = RFE(model, number)
    
    fit = rfe.fit_transform(df, y)
    fit = pd.DataFrame(fit)
    
    
    return fit
    return fit.n_features_
    return fit.support_
    return fit.ranking_