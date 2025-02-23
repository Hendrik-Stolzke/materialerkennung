import time
import numpy as np
import pickle
from mldog.app.plugins.liveMaterialRecognition.materialDetection.dataPreparationProcessor_backwardComp10 import DataPreparationProcessor10
from mldog.app.plugins.liveMaterialRecognition.materialDetection.dataPreparationProcessor_minimal5 import DataPreparationProcessor5
from mldog.app.plugins.liveMaterialRecognition.materialDetection.mlPipelineProcessor import MlPipelineProcessor
from mldog.util.DataProcessing.MultiProcessor import MultiProcessor



from ..model.task import Task
from ...util.drill.drill_procedure_detector import DrillProcedureDetector


class MaterialRecognitionTask(Task):
    """
    Simple task class for classifying material.
    """
    loaded_ML_Pipeline = None
    
    def __init__(self, ttl_max = 80, window_size = 48000, active_power = 50):
        """
        Construct a new task instance.

        Parameters
        ----------
        name : str
            The name of the task.
        """
        super().__init__('Material Recognition Task')
        self.processor = MultiProcessor([DataPreparationProcessor10(),MlPipelineProcessor("./second_pickleModel/bestModel.pkl")])
        
        self.detector = DrillProcedureDetector(ttl_max=ttl_max, window_size=window_size, active_power=active_power)
        self.start = False


    def reset(self) -> None:
        """
        Reset internal buffer to start a new detection from scratch.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        self.detector.reset()

        self.mlPipe = mlPipelineProcessor()

        


    def process(self, data: np.ndarray) -> None:
        """
        Process new measurement data.

        Measurement data is received in chunks (sequential data portions).
        This method is automatically called by the task thread for each incoming data chunk during an active measurement.
        Any complex / time consuming calculations on measurement data should be performed within this method.

        Parameters
        ----------
        data: ndarray
            The next chunk of measurement data to process.

        Returns
        -------
        None
        """

        # forward steam data to detector instance
        drill_data = self.detector.update(data)

        if self.detector.start_detected:
            if(not self.start):
                print("start")
                self.publishResult(("start",0))
                self.start = True

        # check for successful drill procedure detection and publish it accordingly
        if drill_data is not None:
            print("stop")
            self.publishResult(("analysis",0))
            timeBefore = time.time()
            res = [self.performPipeline(drill_data),0]
            res[1] = time.time()-timeBefore
            self.publishResult(("result", res))  
            self.power = False
            self.start = False


    def performPipeline(self,data: np.ndarray):
        
        return(self.processor.process(data))
                      
