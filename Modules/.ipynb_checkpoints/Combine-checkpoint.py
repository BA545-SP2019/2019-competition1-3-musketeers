def combine(array, y1, y2):
    '''reconvert a transformed ndarray back into a pandas dataframe, 
    and recombine the dataframe with its Y1 and Y2 columns'''
    
    import numpy as np
    import pandas as pd
    
    data = pd.DataFrame(array)
    data = data.join([y1, y2])
    return data