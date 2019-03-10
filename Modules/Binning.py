def apply_day_bins(col):
    #bin the days column into equal height bins
    
    q1 = data['C1'].describe()['25%']
    q2 = data['C1'].describe()['50%']
    q3 = data['C1'].describe()['75%']
    
    
    if col <= q1:
        return(1)
    if col > q1 and col <=q2: 
        return(2)
    if col > q2 and col <= q3:
        return(3)
    else:
        return(4)
    
def apply_day_bins1(df, col):
    #bin the days column into equal height bins
    
    q1 = df[col].describe()['25%']
    q2 = df[col].describe()['50%']
    q3 = df[col].describe()['75%']
    
    
    if col <= q1:
        return(1)
    if col > q1 and col <=q2: 
        return(2)
    if col > q2 and col <= q3:
        return(3)
    else:
        return(4)
    
    df[col] = df[col]