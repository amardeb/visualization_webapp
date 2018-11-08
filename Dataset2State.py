
from DatasetState import *
import csv

class Dataset2State(DatasetState):

    def getCSVData(self):
        csvfile = open('dataset2.csv')
        readCSV = csv.reader(csvfile, delimiter=',')
        my_list = list(readCSV)
        return my_list
