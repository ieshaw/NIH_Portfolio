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

        def test_missing_year(self):
            a_list = [['A', 2010, 1, 1],
                       ['A', 2011, 2, 1], 
                       ['A', 2012, 3, 2],
                       ['A', 2013, 4, 3],
                       ['A', 2015, 5, 4]]
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
            daly_df = pd.DataFrame(entries, index=None, columns=df_cols)
            with self.assertRaises(ValueError) as cm:
                noptimal(daly_df)

        def test_make_funding_stationary(self):
            self.assertEqual(self.test_noptimal.funding_returns_df.at[2011,"0"],1)
            self.assertEqual(self.test_noptimal.funding_returns_df.at[2012,"1"],0.5)

        def test_make_rate_stationary(self):
            self.assertEqual(self.test_noptimal.rate_returns_df.at[2011,"0"],0)
            self.assertEqual(self.test_noptimal.rate_returns_df.at[2013,"1"],1)

        def test_find_lag(self):
            self.test_noptimal.find_lag()
            self.assertEqual(self.test_noptimal.lag_dict["A"]["lag"], 1)
            self.assertEqual(self.test_noptimal.lag_dict["B"]["lag"], 2)

        def test_lag_adjust_rate_df(self):
            self.test_noptimal.lag_adjust_rate_df()
            shape = self.test_noptimal.rate_returns_df.shape
            self.assertEqual(shape[0], 2)            
            self.assertEqual(shape[1], 2)            
        
        #TODO: Make This Test
        def test_lag_adjust_rate_df_negative_corr(self):
            pass

        #TODO: Try the lag adjust rate df function on our date


if __name__ == '__main__':
        unittest.main()
