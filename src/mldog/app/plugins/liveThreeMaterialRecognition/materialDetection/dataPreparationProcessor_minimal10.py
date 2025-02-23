from numpy import ndarray
import pandas
import pandas as pd    
from pandas import DataFrame            
import glob
from tsfresh.feature_extraction import extract_features
import numpy as np

from mldog.util.DataProcessing.ProcessableInterface import ProcessableInterface
from tsfresh.feature_extraction import extract_features, MinimalFCParameters


class DataPreparationProcessor_minimal10(ProcessableInterface):
    def __init__(self):
        self.feature_names = ["Voltage__sum_values",
                              "Audio__length",
                              "Current__median",
                              "Voltage__minimum",
                              "Current__mean",
                              "Voltage__mean",
                              "Voltage__root_mean_square",
                              "Audio__mean",
                              "Audio__variance",
                              "Audio__standard_deviation"]

    def feature_extraction_mini(self,df: DataFrame):
        df["id"] = 0
        df.rename(columns={0:"Audio",1:"Voltage",2:"Current"},inplace=True)
        extraction_settings = MinimalFCParameters()
        extracted_features = extract_features(df, column_id = 'id',  default_fc_parameters=extraction_settings)
        extracted_features = extracted_features[self.feature_names]
        return extracted_features


    def process(self,data):
        extracted = self.feature_extraction_mini(pd.DataFrame(data))
        print(extracted)
        return extracted#just a quick fix #TODO