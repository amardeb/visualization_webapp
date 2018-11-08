import csv

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    my_list = list(readCSV)
    data=[]
    for row in my_list:
        data.append(row[0])
    data.pop(0)
    print(data)
   
