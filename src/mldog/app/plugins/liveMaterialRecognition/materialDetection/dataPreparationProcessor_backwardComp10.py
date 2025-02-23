from numpy import ndarray
import pandas
import pandas as pd    
from pandas import DataFrame            
import glob
from tsfresh.feature_extraction import extract_features
import numpy as np

from mldog.util.DataProcessing.ProcessableInterface import ProcessableInterface



class DataPreparationProcessor10(ProcessableInterface):
   
    def feature_extraction_Comprehensiver(self,df: DataFrame, d: dict):

        """
        extrahiert die features , hilfsfunktion
        """
        extracted_features = extract_features(df, column_id = 'id',default_fc_parameters= d)
        return extracted_features
    


    def feature_extraction_comprehensiver_Backward(self, dataframe: pd.DataFrame):
        """
        Features are extracted with tsfesh (comprehensiver) and selekted with Backward Elimination
        """

        dataframe.rename(columns={0:"Audio",1:"Voltage",2:"Current"},inplace=True)
        dataframe["id"] = 0
        print(dataframe)

        dictionary_kombination = {}
        dictionary_kombination.update({
        "fourier_entropy": [{"bins": x} for x in [3]],
        "permutation_entropy": [{"tau": 1, "dimension": x} for x in [ 6,7]], 
        "quantile": [{"q": q} for q in [0.1]],
        "mean_n_absolute_max": [{"number_of_maxima": 7 }],
        "lempel_ziv_complexity": [{"bins": x} for x in [ 3, 5, 10, 100]],
        "cid_ce": [{"normalize": False}]
        })

        featur = self.feature_extraction_Comprehensiver(dataframe, dictionary_kombination)

        gewünschte_Features= ["Audio__cid_ce__normalize_False","Voltage__quantile__q_0.1","Current__lempel_ziv_complexity__bins_3",
                              "Current__lempel_ziv_complexity__bins_5","Current__lempel_ziv_complexity__bins_10",
                              "Current__lempel_ziv_complexity__bins_100","Current__fourier_entropy__bins_3","Current__permutation_entropy__dimension_6__tau_1",
                              "Current__permutation_entropy__dimension_7__tau_1","Current__mean_n_absolute_max__number_of_maxima_7"]

        return  featur[gewünschte_Features]

    def process(self,data):
        return self.feature_extraction_comprehensiver_Backward(pandas.DataFrame(data)) #just a quick fix #TODO
