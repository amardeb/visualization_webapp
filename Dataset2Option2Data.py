
from DataTemplate import *
import operator

class Dataset2Option2Data(DataTemplate):

    def getData(self, my_list):
        time=[0,0,0,0,0,0,0,0,0,0,0]
        my_list.pop(0)
        for element in my_list:
            if(element[14]!=''):
                time[0] = time[0] + int(element[14])
            if (element[15] != ''):
                time[1] = time[1] + int(element[15])
            if (element[16] != ''):
                time[2] = time[2] + int(element[16])
            if (element[17] != ''):
                time[3] = time[3] + int(element[17])
            if (element[18] != ''):
                time[4] = time[4] + int(element[18])
            if (element[19] != ''):
                time[5] = time[5] + int(element[19])
            if (element[20] != ''):
                time[6] = time[6] + int(element[20])
            if (element[21] != ''):
                time[7] = time[7] + int(element[21])
            if (element[22] != ''):
                time[8] = time[8] + int(element[22])
            if (element[23] != ''):
                time[9] = time[9] + int(element[23])
            if (element[24] != ''):
                time[10] = time[10] + int(element[24])

        print(time)
        dic = {'element':['8.00-9.00', '5.00-6.00', '4.00-5.00', '3.00-4.00', '7.00-8.00'], 'number':[1402637, 1291467, 1281746, 1274114, 1242672]}
        return dic


