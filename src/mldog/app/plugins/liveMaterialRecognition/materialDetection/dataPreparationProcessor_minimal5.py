from numpy import ndarray
import pandas
import pandas as pd    
from pandas import DataFrame            
import glob
from tsfresh.feature_extraction import extract_features
import numpy as np

from mldog.util.DataProcessing.ProcessableInterface import ProcessableInterface



class DataPreparationProcessor5(ProcessableInterface):
    def feature_extraction_mini_numpy(self,dataframe:pd.DataFrame):
        """
        The feature_extraction_mini_numpy function gives the same results as applying minimalFCParameters in tsfresh.extract_features
        And select_features methode. 

        Recommandation: use this method becouse it is faster 

        parameter:
        - Dataframe 

       Return: 
        five Features as a dataframe 
        """
    
        dataframe.rename(columns={0:"Audio",1:"Voltage",2:"Current"},inplace=True)
    
        median_Voltage = []
        Current__sum_values = []
        Audio__standard_deviation = []
        Audio__root_mean_square	= []
        median_Current = []

        median_Voltage.append(np.median(dataframe["Voltage"]))
        Current__sum_values.append(np.sum(dataframe["Current"]))
        Audio__standard_deviation.append(np.std(dataframe["Audio"]))
        Audio__root_mean_square	.append(np.sqrt(np.mean(dataframe['Audio']**2)))
        median_Current.append(np.median(dataframe["Current"]))

        data = {'Voltage__median': median_Voltage, 
                'Current__sum_values': Current__sum_values, 
                'Audio__standard_deviation': Audio__standard_deviation,
                'Audio__root_mean_square': Audio__root_mean_square,
                'Current__median': median_Current}

        df = pd.DataFrame(data)
        return df 

    def process(self,data):
        return self.feature_extraction_mini_numpy(pandas.DataFrame(data)) #just a quick fix #TODO


