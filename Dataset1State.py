

from DatasetState import *
import csv

class Dataset1State(DatasetState):

    def getCSVData(self):
        csvfile = open('dataset1.csv')
        readCSV = csv.reader(csvfile, delimiter=',')
        my_list = list(readCSV)
        return my_list
