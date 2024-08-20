import statistics
from tabulate import tabulate
import numpy as np
import pandas as pd
import math

file = [r"C:\Users\vaths\OneDrive\Desktop\DADT\Python Scripts\CE4_Homework_297751233\CIS_500_S24_CE2_MonthlyMeanTemperatureCNY.txt"]

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

def Testing_hypothesis(l1,l2,s1):
    print(s1 + 'for each year during the period 2006 – 2022 in CNY')
    lists = list(zip(l1, l2))
    data_list = [list(row) for row in zip(*lists)]
    print(tabulate(data_list, tablefmt='grid'))
    print('Populate the Table below assuming α = 0.01 (weaker) and α = 0.05 (stronger requirement)')
    new_l1 = [int(x) for x in l1[1:len(l1)]]
    new_l2 = [float(x) for x in l2[1:len(l1)]]
    new_l1=(pd.Series(new_l1)).to_numpy()
    new_l2=(pd.Series(new_l2)).to_numpy()
    l1_mean = np.mean(new_l1)
    l2_mean = np.mean(new_l2)
    slope = np.sum((new_l1-l1_mean)*(new_l2-l2_mean))/np.sum((new_l1-l1_mean)*(new_l1-l1_mean))
    intercept = (l2_mean)-(slope*(l1_mean))
    prediction_mean = round(slope * int(2100) + intercept,3)
    mean = statistics.mean(new_l2)
    standarddeviation = statistics.pstdev(new_l2)
    l1 = ['Mean of ' + s1 + 'in 2100 (prediction from CE3, part a)','Mean of ' + s1 + '2006 - 2022','St. Dev. of ' + s1 + '2006 - 2022']
    l2 = [prediction_mean,mean,standarddeviation]
    data_list = list(zip(l1,l2))
    print(tabulate(data_list,headers=[],tablefmt='grid'))
    l1 = ['Testing requirement','Hypothesis H0 testing limit Max monthly temperature','Hypothesis Ho (accepted or rejected)','Global warming is evident (Yes or No)']
    k=[0.01,0.05]
    k1 = mean + (2.33*standarddeviation)
    k2 = mean + (1.645*standarddeviation)
    l2 = [k[0],k1,'Accepted H0' if k1>prediction_mean else 'Rejected H0','No' if k1>prediction_mean else 'Yes']
    l3 = [k[1],k2,'Accepted H0' if k2>prediction_mean else 'Rejected H0','No' if k2>prediction_mean else 'Yes']
    data_list = list(zip(l1,l2,l3))
    print(tabulate(data_list,headers=[],tablefmt='grid'))
    k=[]
    k.append(s1 + 'during 2006-2022 confirms' + l1[3])
    k.append(l2[3])
    k.append(l3[3])
    return k
data = extraction()
final = []

print ('The maximum monthly temperature data analysis and testing hypothesis during the period 2006 – 2022 in CNY ')
l=Testing_hypothesis(list(reversed(data[0])),list(reversed(data[1])),'Max Montly Temperature')
final.append(l)
print ('**************************************************************************************************')

print ('The minimum monthly temperature data analysis and testing hypothesis during the period 2006 – 2022 in CNY ')
l=Testing_hypothesis(list(reversed(data[0])),list(reversed(data[2])),'Min Montly Temperature')
final.append(l)
print ('**************************************************************************************************')

print ('The average monthly temperature data analysis and testing hypothesis during the period 2006 – 2022 in CNY ')
l=Testing_hypothesis(list(reversed(data[0])),list(reversed(data[3])),'Avg Montly Temperature')
final.append(l)
print ('**************************************************************************************************')

print ('The median monthly temperature data analysis and testing hypothesis during the period 2006 – 2022 in CNY ')
l=Testing_hypothesis(list(reversed(data[0])),list(reversed(data[4])),'Median Montly Temperature')
final.append(l)
print ('**************************************************************************************************')

print('Global warming prediction summary')
l1=[]
l2=[]
l3=[]
for i in range(0,len(final)):
    l1.append(final[i][0])
    l2.append(final[i][1])
    l3.append(final[i][2])
data_list = list(zip(l1,l2,l3))
print(tabulate(data_list, headers=["Global warming prediction weaker and stronger significance level requirements ", "α = 0.01", "α = 0.05"], tablefmt="grid"))