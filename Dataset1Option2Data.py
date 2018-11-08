
from DataTemplate import *

class Dataset1Option2Data(DataTemplate):

    def getData(self, my_list):
        X=[]
        for element in my_list:
            X.append(element[5])
        X.pop(0)
        unique=[]
        number=[]
        for element in X:
            if element not in unique:
                unique.append(element)
        for element in unique:
            cnt=0
            for temp in X:
                if element == temp:
                    cnt = cnt + 1
            number.append(cnt)

        dic = {'element':unique, 'number':number}
        return dic


