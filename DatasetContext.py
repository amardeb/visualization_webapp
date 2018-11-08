
class DatasetContext:

    def __init__(self, state):
        self._state = state

    def getState(self, state):
        self._state = state

    def getCSVData(self):
        my_list = self._state.getCSVData()
        return my_list
