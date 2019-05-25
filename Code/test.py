import pandas as pd

import unittest

from noptimal import noptimal

class Test_noptimal_class(unittest.TestCase):

        def setUp(self):
            self.daly_df = pd.DataFrame({1:1})
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
