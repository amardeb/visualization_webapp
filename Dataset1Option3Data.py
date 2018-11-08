
from DataTemplate import *

class Dataset1Option3Data(DataTemplate):

    def getData(self, my_list):
        X=[]
        Y=[]
        for element in my_list:
            X.append(element[5])
            print(X)
            Y.append(element[12])
        X.pop(0)
        Y.pop(0)
        print(X)
        unique=[]
        number=[]
        for element in X:
            if element not in unique:
                unique.append(element)
        for element in unique:
            cnt=0
            cnt1=0
            for temp in range(len(X)):
                if element == X[temp]:
                    cnt1 = cnt1 +1
                    cnt = cnt + float(Y[temp])
            number.append(cnt/cnt1)
        dic = {'element':unique, 'number':number}
        print(dic)
        return dic


