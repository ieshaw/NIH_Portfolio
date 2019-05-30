import pandas as pd

class noptimal:

    def __init__(self, data_df, isFundingStationary=False, isRateStationary=False):
        '''
        input data_df: pandas dataframe with columns 
            ['disease', 'year', 'funding', 'rate']
            where 'rate' could be the number of YLL or DALY
        '''
        self.data_df = data_df.copy(deep=True)
        self.diseases = self.data_df['disease'].unique().tolist()
        self.years = self.data_df['year'].unique().tolist()
        self.rate_returns_df = pd.DataFrame(0,index= self.years,
                                            columns=[str(i) for i in range(len(self.diseases))])
        #Error chack have data for each year for each disease
        year_counts = self.data_df['year'].value_counts()
        if max(year_counts) != min(year_counts):
            raise ValueError('''
                    Not all years appear for each disease.
                    ''')
        self.funding_returns_df = self.rate_returns_df.copy(deep=True)
        #Hash map (python dict) diseases in case names have spaces or bad characters
        i = 0
        self.disease_map = {}
        for disease in self.diseases:
            self.disease_map[disease] = i
            dis_df = self.data_df.loc[self.data_df['disease'] == disease].copy(deep=True)
            self.rate_returns_df[str(i)] = dis_df['rate'].values
            self.funding_returns_df[str(i)] = dis_df['funding'].values
            i += 1
        if not isFundingStationary:
            self.funding_returns_df = self.funding_returns_df.pct_change()
            self.funding_returns_df.dropna(inplace=True)
        if not isRateStationary:
            self.rate_returns_df = self.rate_returns_df.pct_change()
            self.rate_returns_df.dropna(inplace=True)

    def find_lag(self):
        diseases = self.data_df['disease'].unique()
        self.lag_dict = {}
        for disease in diseases:
            self.lag_dict[disease] = {"corr": 0, "lag": 0}
            dis_df = self.data_df.loc[self.data_df['disease'] == disease].copy(deep=True)
            for lag in range(dis_df['year'].nunique() - 1):
                curr_corr = dis_df['funding'].corr(dis_df['rate'])
                if abs(curr_corr) > abs(self.lag_dict[disease]["corr"]):
                    self.lag_dict[disease]["corr"] = curr_corr
                    self.lag_dict[disease]["lag"] = lag
                dis_df['rate'] = dis_df['rate'].shift(-1)
                dis_df.dropna(inplace=True)

    def lag_adjust_rate_df(self):
        self.find_lag()
        for disease_hash in self.rate_returns_df.columns:
            disease = self.diseases[int(disease_hash)]
            lag = self.lag_dict[disease]["lag"]
            if lag < 0:
                raise ValueError('''
                        A lag of {} years for the rate of {} 
                        has a correlation of {} with funding.
                        This implies funding increases disease frequency.
                        Cannot find rate correlation between diseases if 
                        lag correlation coefficient is negative.
                        '''.format(lag,disease,self.lag_dict[disease]["lag"]))
            self.rate_returns_df[disease_hash] = self.rate_returns_df[disease_hash].shift(int(-1*lag))
        self.rate_returns_df.dropna(inplace=True)

    def __del__(self):
        pass
