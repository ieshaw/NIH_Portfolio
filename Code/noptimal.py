import pandas as pd

class noptimal:

    def __init__(self, data_df):
        '''
        input data_df: pandas dataframe with columns 
            ['disease', 'year', 'funding', 'rate']
            where 'val' could be the number of YLL or DALY
        '''
        self.data_df = data_df.copy(deep=True)
        
    def find_lag(self):
        print("Finding lag")


    def __del__(self):
        pass
