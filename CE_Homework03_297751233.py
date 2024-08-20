import statistics
from tabulate import tabulate
import numpy as np
import pandas as pd
import math

file = [r"C:\Users\vaths\OneDrive\Desktop\DADT\Python Scripts\CE3_Homework_297751233\CIS_500_S24_CE3_MonthlyMeanTemperatureCNY.txt"]

def extraction():
    with open(file[0], 'r') as x:
        y = x.readlines()
        l = []
        years = []
        data = []
        for y in y[1:]:
            k = y.strip().split('\t')
            l.append(k)
        maximum = []
        minimum = []
        average = []
        median = []
        for i in range(1,len(l)):
            years.append(l[i][0])
            maximum.append(max(l[i][1:len(l[i])]))
            minimum.append(min(l[i][1:len(l[i])]))
            s=0
            k=l[i]
            p=[]
            for j in range(1,len(k)):
                s=s+float(k[j])
                p.append(float(k[j]))
            average.append(round(s/(len(k)-1),3))
            median.append(round(statistics.median(p),3))
    years.append('Year')
    maximum.append('Max monthly temperature in F')
    minimum.append('Min monthly temperature in F')
    average.append('Average monthly temperature in F')
    median.append('Median monthly temperature in F')
    data.append(years)
    data.append(maximum)
    data.append(minimum)
    data.append(average)
    data.append(median)
    return data

def statistics_calculate(l1,l2,s1,s2):
    lists = list(zip(l1, l2))
    data_list = [list(row) for row in zip(*lists)]
    print(tabulate(data_list, tablefmt='grid'))
    new_l1 = [int(x) for x in l1[1:len(l1)]]
    new_l2 = [float(x) for x in l2[1:len(l1)]]
    new_l1=(pd.Series(new_l1)).to_numpy()
    new_l2=(pd.Series(new_l2)).to_numpy()
    l1_mean = np.mean(new_l1)
    l2_mean = np.mean(new_l2)
    slope = np.sum((new_l1-l1_mean)*(new_l2-l2_mean))/np.sum((new_l1-l1_mean)*(new_l1-l1_mean))
    intercept = (l2_mean)-(slope*(l1_mean))
    print('The slope and intercept are as below : ')
    print(slope)
    print(intercept)
    l3=[]
    l3.append(s1+'regression line')
    for i in range(0,len(new_l1)):
        l3.append(round(slope*new_l1[i]+intercept,3))
    print('The linear regression line ' + s1 + 'f(Year) and write your result in the form ' + s2) 
    lists = list(zip(l1, l3))
    data_list = [list(row) for row in zip(*lists)]
    print(tabulate(data_list, tablefmt='grid'))
    l1 = ['Year','2010','2020','2100']
    l2 = [s1+'(prediction in F)']
    for i in range(1,len(l1)):
        l2.append(round(slope*float(l1[i])+intercept,3))
    print('The satisfactory accuracy of the regression line predict the ' + s1 + 'in the year 2100 by extrapolating your regression line ')
    lists = list(zip(l1, l2))
    data_list = [list(row) for row in zip(*lists)]
    print(tabulate(data_list, tablefmt='grid'))
    k=[]
    k.append(s1+ 'regression line')
    k.append(slope)
    k.append(intercept)
    k.append(l1)
    k.append(l2)
    return k

data = extraction()
final = []
final_list=[]

print ('The maximum monthly temperature during the period 2006 – 2022 in CNY ')
l=statistics_calculate(list(reversed(data[0])),list(reversed(data[1])),'Max_Montly_Temperature','Tmax = Amax  Year + Bmax')
final.append(l[0])
final.append('Tmax = ' + str(l[1]) + ' * Year  ' + str(l[2]))
final.append(l[3])
final.append(l[4])
final_list.append(final)
print ('**************************************************************************************************')

final = []
print ('The minimum monthly temperature during the period 2006 – 2022 in CNY ')
l=statistics_calculate(list(reversed(data[0])),list(reversed(data[2])),'Min_Montly_Temperature','Tmin = Amin  Year + Bmin')
final.append(l[0])
final.append('Tmin = ' + str(l[1]) + ' * Year  ' + str(l[2]))
final.append(l[3])
final.append(l[4])
final_list.append(final)
print ('**************************************************************************************************')

final = []
print ('The average monthly temperature during the period 2006 – 2022 in CNY ')
l=statistics_calculate(list(reversed(data[0])),list(reversed(data[3])),'Avg_Montly_Temperature','Tavg = Aavg  Year + Bavg')
final.append(l[0])
final.append('Tavg = ' + str(l[1]) + ' * Year  ' + str(l[2]))
final.append(l[3])
final.append(l[4])
final_list.append(final)
print ('**************************************************************************************************')

final = []
print ('The median monthly temperature during the period 2006 – 2022 in CNY ')
l=statistics_calculate(list(reversed(data[0])),list(reversed(data[4])),'Median_Montly_Temperature','Tmedian = Amedian  Year + Bmedian')
final.append(l[0])
final.append('Tmedian = ' + str(l[1]) + ' * Year  ' + str(l[2]))
final.append(l[3])
final.append(l[4])
final_list.append(final)
print ('**************************************************************************************************')

print('Final Table')
print('Regression Lines')
l1=[]
l2=[]
l3=[]
for i in range(0,len(final_list)):
    l1.append(final_list[i][0])
    l2.append(final_list[i][1])
    l3.append(final_list[i][3])
data = list(zip(l1, l2))
print(tabulate(data, headers=["Years", "2006-2022"], tablefmt="grid"))
print('Temperature prediction in CNY in the Year 2100')
print(tabulate(l3, headers=["Year", "2010", "2020", "2100"], tablefmt="grid"))
