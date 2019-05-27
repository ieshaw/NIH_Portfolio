import pandas as pd

class noptimal:

    def __init__(self, data_df):
        '''
        input data_df: pandas dataframe with columns 
            ['disease', 'year', 'funding', 'rate']
            where 'rate' could be the number of YLL or DALY
        '''
        self.data_df = data_df.copy(deep=True)
        self.diseases = self.data_df['disease'].unique()
        self.disease_map = {}
        i = 1
        self.rate_returns_df = pd.DataFrame(0,index=self.data_df['year'].unique().tolist(),
                                            columns=[str(i) for i in range(1,len(self.diseases)+1)])
        #TODO: Error chack have data for each year for each disease
        self.funding_returns_df = self.rate_returns_df.copy(deep=True)
        for disease in self.diseases:
            self.disease_map[disease] = i
            dis_df = self.data_df.loc[self.data_df['disease'] == disease].copy(deep=True)
            self.rate_returns_df[str(i)] = dis_df['rate'].values
            self.funding_returns_df[str(i)] = dis_df['funding'].values
            i += 1

    #TODO: Turn df's into returns df's

    def find_lag(self):
        diseases = self.data_df['disease'].unique()
        corr_dict = {}
        for disease in diseases:
            corr_dict[disease] = 0
            dis_df = self.data_df.loc[self.data_df['disease'] == disease].copy(deep=True)
            for i in range(1,dis_df['year'].nunique()):
                curr_corr = dis_df['funding'].corr(dis_df['rate'])
            print(dis_df)


    def __del__(self):
        pass
