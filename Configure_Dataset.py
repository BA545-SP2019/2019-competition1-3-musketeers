def configure(filename):
    '''formats the competition one dataset in order to be used for multiple pipelines
    
        input: file, an excel file of the competition one dataset
        
        returns: a pandas dataframe with the following changes:
            - replace all '-' with np.nan
            - drops missing values in the IPO Pricing columns
            - drop ticker and company name
            - calculates the target variables
            - calculates control varibles and drops columns used to calc control variables
            - converts textual characteristics columns to ratio columns, as mentioned in the hints
            - fills in missing values in 'I3' with researched values, and converts column I3 into new column called "Bins", which is the industry of the correspontding SIC code
            - one hot encodes the Bins column, and drops the Bins column'''
    
    #import proper libraries
    import numpy as np
    import pandas as pd
    
    # create an initial data frame from data supplied to us
    df  = pd.read_excel(filename, header=0)
    
    
    #drop missing values in IPO pricing columns and name/ticker info
    df = df.replace('-', np.NaN)
    df = df.dropna(subset=['P(IPO)', 'P(H)', 'P(L)', 'P(1Day)'], axis = 0)
    df = df.drop(['I1','I2'], axis = 1)
    # calculate target variables Y1 & Y2
    # first, calculate intermediate values and use as columns to dataframe
    df['p_mid'] = (df['P(H)'] + df['P(L)']) / 2
    
    df["Y1"] = np.where(df['P(IPO)'] < df['p_mid'], 1, 0)
    df['Y2'] = np.where(df['P(IPO)'] < df['P(1Day)'], 1, 0)
    
    #convert 'T1' : 'T5' into ratios, as suggested in the hints
    df['%_long_sentences'] = df['T4'] / df['T1']
    df['%_long_words'] = df['T5'] / df['T2']
    df['%_positive_words'] = df['S1'] / df['T2']
    df['%_negative_words'] = df['S2'] / df['T2']
    df['%_uncertain_words'] = df['S3'] / df['T2']
    
    #calculate control variables
    df["C3'"] = np.where(df['C3'] > 0, 1, 0)
    df["C5'"] = df['C5'] / df['C6']
    
    #to calculate C6' need intermediate calculation, will call it df['fraction']
    df['fraction'] = (df['P(IPO)'] - df['p_mid']) / df['p_mid'] * 100
    df["C6'"] = np.where(df["P(IPO)"] > df['p_mid'], df['fraction'], 0)  
    

    #correct column I3
    df.I3 = df.I3.astype(str)
    #fill in missing values with researched values
    df.iloc[170, 0] = '6794'
    df.iloc[183, 0] = '6794'
    df.iloc[483, 0] = '3663'
    df.iloc[599, 0] = '5063'
    df.iloc[239, 0] = '8742'
    df.iloc[214, 0] = '7389'
    
    #convert I3 into Bins column, and one-hot encode the bins
    #first, converti I3 to numeric
    df['I3'] = df['I3'].astype(float)
    
    #define bins with SIC codes
    bins =[0,999,1499,1799,1999,3999,4999,5199,5999,6799,8999,9729,9999]
    #names
    group_names=["Agriculture Forestry and Fishing","Mining","Construction","not used","Manufacturing","Transportation Communications, Electric, Gas and Sanitary service","Wholesale Trade","Retail Trade","Finance, Insurance and Real Estate","Services","Public Administration","Nonclassifiable"]
    df["Bins"] = pd.cut(df["I3"],bins,labels= group_names)
    
    # bin further to reduce number of classes to 5
    df['Bins'] = df['Bins'].replace(['Mining', 'Construction', 'Manufacturing'], 'Manufacturing')
    df['Bins'] = df['Bins'].replace(['Wholesale Trade', 'Retail Trade'], 'Trade')
    df['Bins'] = df['Bins'].replace(["Transportation Communications, Electric, Gas and Sanitary service", "Services","Public Administration"], 'Public Services')           
    df['Bins'] = df['Bins'].replace("Agriculture Forestry and Fishing", 'Agriculture')
    df['Bins'] = df['Bins'].replace('Finance, Insurance and Real Estate', 'Finance/Insurance Services')

    #One-hot encode 'Bins'
    df = df.join(pd.get_dummies(df['Bins'], prefix = 'one_hot'))
    
    #drop any remaining unnecessary columns
    configured_df = df.drop(labels = ['Bins', 'p_mid', 'I3', 'P(IPO)', 'P(H)', 'P(L)', 'P(1Day)', 'fraction', 'C3', 'C5', 'C6', 'T1', 'T2', 'T3', 'T4', 'T5', 'S1', 'S2', 'S3'], axis = 1)
    
    return configured_df