
import pandas as pd

class DataInvestigator:

    #constructor
    def __init__(self, df):
        self.df = df

    #returns most frequent value in the column, none if error
    def baseline(self, col):
        try:
            column = self.df.iloc[:,col]
            mostFreq = column.mode().iloc[0]
            return mostFreq
        except Exception:
            return None

    #returns correlation between two columns, none if error
    def corr(self, col1, col2):
        try:
            column1 = self.df.iloc[:,col1]
            column2 = self.df.iloc[:,col2]
            return column1.corr(column2)
        except Exception:
            return None

    #same as baseline
    def zeroR(self, col):
        try:
            return self.baseline(col)
        except Exception:
            return None



df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)

print(di.baseline(1))   #53
print(di.zeroR(1))      #53
print(di.corr(0, 1))    #some value
print(di.baseline(99))  #none, no column 99