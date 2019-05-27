import pandas as pd

import unittest

from noptimal import noptimal

class Test_noptimal_class(unittest.TestCase):

        def setUp(self):
            a_list = [['A', 2010, 1, 1],
                       ['A', 2011, 2, 1], 
                       ['A', 2012, 3, 2],
                       ['A', 2013, 4, 3],
                       ['A', 2014, 5, 4]]
            b_list = [['B', 2010, 1, 1],
                       ['B', 2011, 2, 1], 
                       ['B', 2012, 3, 1],
                       ['B', 2013, 4, 2],
                       ['B', 2014, 5, 3]]
            entry_lists = [a_list, b_list]
            entries = []
            for entry_list in entry_lists:
                entries.extend(entry_list)
            df_cols = ['disease', 'year', 'funding', 'rate']
            self.daly_df = pd.DataFrame(entries, index=None, columns=df_cols)
            self.test_noptimal = noptimal(self.daly_df)

        '''
        def setUp(self):
            filename = "Data/nih_gbd_data.csv"
            self.data_df = pd.read_csv(filename)
            self.daly_df = (self.data_df.loc[
                (self.data_df['measure_name'] == 'DALYs (Disability-Adjusted Life Years)') 
                & (self.data_df['metric_name'] == 'Rate')]).copy()
            self.daly_df.drop(['measure_name','metric_name'], axis=1,inplace=True)
            self.daly_df.rename({'val':'rate'}, axis=1,inplace=True)
            self.test_noptimal = noptimal(self.daly_df)
        '''

        def test_find_lag(self):
            self.test_noptimal.find_lag()

        


if __name__ == '__main__':
        unittest.main()
