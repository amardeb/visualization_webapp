
from DataTemplate import *
import operator

class Dataset2Option1Data(DataTemplate):

    def getData(self, my_list):
        X=[]
        Y=[]
        for element in my_list:
            X.append(element[2])


        X.pop(0)
        unique=[]
        number=[]
        for element in X:
            if element not in unique:
                unique.append(element)

        for element in unique:
            cnt=0
            i=1
            print(element)
            for temp in X:
                if element == temp:
                    temp2 = my_list[i]
                    j=7
                    while(j < 31):
                        if(temp2[j]==''):
                            j = j + 1
                            continue
                        cnt = cnt + int(temp2[j])
                        j = j + 1

                i = i + 1


            number.append(cnt)
        tempNumber = sorted(number, reverse=True)
        newNumber = tempNumber[:5]
        newUnique=[]
        for element in newNumber:
            i=0
            for temp in number:
                if temp == element:
                    newUnique.append(unique[i])
            i=i+1
        dic = {'element':newUnique, 'number':newNumber}
        return dic


