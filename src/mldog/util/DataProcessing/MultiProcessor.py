
from mldog.util.DataProcessing.ProcessableInterface import ProcessableInterface


class MultiProcessor(ProcessableInterface):
    def __init__(self,processableList):
        self.processableList = processableList
    def process(self, data):
        for processable in self.processableList:
            data = processable.process(data)
        return data