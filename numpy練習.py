import numpy as np

populationData = np.genfromtxt('peopleCounting.csv', dtype='int',
                            skip_header=1, delimiter=',', encoding='utf-8')
for row in populationData:
    for i in range(1,10):
        if int(row[1]) == i:
            sumData = row[3]+ row[4]
            print(str(row[0])+"年", str(row[1])+"月", '國小(含)之前的人數：', sumData)
            print('{}年{}月國小(含)之前的人數：{}'.format(row[0], row[1], sumData))