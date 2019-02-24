def skew_transform_square(data):
    '''input a pandas dataframe of competition one dataset and returns a transformed dataset based on values of skewness for each column.
    For a single column: 
        if the value of skew is between [-.5, .5], no transformation takes place.
        if the value of skew is less than -0.5, perform a square transformation.
        if the value of skew is greater than .5, perform a square root transformation.
        '''
    import pandas as pd
    import numpy as np
    
    
    dataskew = data.skew()
    pair = dict(zip(dataskew.index, dataskew.values))
    
    for key, val in pair.items():
        if val < -.5:
            data[key] = np.square(data[key])
        if val > .5:
            data[key] = np.sqrt(data[key])
    
            
    return data
    

def skew_transform_log(data):
    '''input a pandas dataframe of competition one dataset and returns a transformed dataset based on values of skewness for each column.
    For a single column: 
        if the value of skew is between [-.5, .5], no transformation takes place.
        if the value of skew is less than -0.5, perform an e^x transformation.
        if the value of skew is greater than .5, perform a log transformation.
        '''
    
    import pandas as pd
    import numpy as np
    
    data = data + .000000001
    
    dataskew = data.skew()
    pair = dict(zip(dataskew.index, dataskew.values))
    
    for key, val in pair.items():
        if val < -.5:
            data[key] = np.exp(data[key])
        if val > .5:
            data[key] = np.log(data[key])
            
    return data
    
                               