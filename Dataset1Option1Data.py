
from DataTemplate import *

class Dataset1Option1Data(DataTemplate):

    def getData(self, my_list):
        X=[]
        for element in my_list:
            X.append(element[0])
        X.pop(0)
        print (X)
        a=0
        b=0
        for element in X:
            if element == 'MITx':
                a=a+1
            else:
                b=b+1
        varsity = ['MITx', 'HarvardX']
        number = [a, b]
        dic = {'element':varsity, 'number':number}

        return dic

