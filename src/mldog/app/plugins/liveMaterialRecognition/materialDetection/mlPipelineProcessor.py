from pathlib import Path
from numpy import ndarray
import pickle

from mldog.util.DataProcessing.ProcessableInterface import ProcessableInterface



class MlPipelineProcessor(ProcessableInterface):
    def __init__(self,pathInMaterialDetection):
        try:
            # Lade ML-Algorithmus:
            file_path = Path(__file__).parent / pathInMaterialDetection
            with open(file_path, 'rb') as grid_search_file:
                self.loaded_Predictor = pickle.load(grid_search_file)
            grid_search_file.close()

        except FileNotFoundError:
            print("Fehler: pickle model nicht auffindbar.")
            return None
        except pickle.PickleError as pe:
            print(f"Fehler beim laden des pickle Models: {pe}")
            return None  
        except Exception as e:
            print(f"Ein unerwarteter Fehler: {e}")
            return None  

    def process(self,data) -> ndarray:
       return self.loaded_Predictor.predict_proba(data)