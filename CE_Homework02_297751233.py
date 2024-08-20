import statistics
from tabulate import tabulate
import re
import math

files = [
    r"C:\Users\vaths\OneDrive\Desktop\DADT\Python Scripts\CE2_Homework_297751233\CIS_500_S24_CE2_MeanTemperature.txt",
    r"C:\Users\vaths\OneDrive\Desktop\DADT\Python Scripts\CE2_Homework_297751233\CIS_500_S24_CE2_Rainfall.txt",
    r"C:\Users\vaths\OneDrive\Desktop\DADT\Python Scripts\CE2_Homework_297751233\CIS_500_S24_CE2_Snowfall.txt"
]

def stats(f,fno):
    with open(f,'r') as x:
        y = x.readlines()
        l = []
        for y in y[1:]:
            k = y.strip().split('\t')
            l.append(k)
        p1 = list(zip(*l))
        k=[]
        month = []
        for i in range(1,len(p1)):
            v = p1[i]
            r=[]
            p=[]
            month.append(v[0])
            for j in range(1,len(v)):
                r.append(float(v[j]))
            p.append(max(r))
            p.append(min(r))
            p.append(statistics.median(r))
            p.append(sum(r)/(len(v)-1))
            p.append(statistics.stdev(r))
            k.append(p)
        z = list(zip(*k))
        datalist = [list(t) for t in z]
        c = ['Max','Min','Med','Avg','StDev']
        data_list = [[c] + i for c, i in zip(c, datalist)]
        y=[]
        if fno==1:
            y.append(max(data_list[0][1:]))
            y.append(min(data_list[1][1:]))
        else:
            y.append(sum(data_list[0][1:]))
            y.append(sum(data_list[1][1:]))
        y.append(statistics.median(data_list[2][1:]))
        y.append(sum(data_list[3][1:])/(len(data_list[3])-1))
        y.append(statistics.stdev(data_list[4][1:]))
        for i in range(0,len(data_list)):
            data_list[i].append(y[i])
        headers = ['Data','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Year']
        return (tabulate(data_list, headers=headers))

def correlation1(f1,f2):
    with open(f1,'r') as x:
        y = x.readlines()
        l = []
        for y in y[1:]:
            k = y.strip().split('\t')
            l.append(k)
        p1 = list(zip(*l))
    with open(f2,'r') as x:
        y = x.readlines()
        l = []
        for y in y[1:]:
            k = y.strip().split('\t')
            l.append(k)
        p2 = list(zip(*l))
    t1=[]
    t2=[]
    for i in range(1,len(p1)):
        v1 = p1[i]
        v2 = p2[i]
        r1=[]
        r2=[]
        for j in range(1,len(v1)):
            r1.append(float(v1[j]))
            r2.append(float(v2[j]))
        t1.append(sum(r1)/(len(r1))) 
        t2.append(sum(r2)/(len(r2)))
    x1=sum(t2)
    x2=sum(t1)
    x3=0
    x4=0
    x5=0
    n=len(t1)
    for i in range(0,len(t1)):
        x3=x3+t1[i]*t2[i]
        x4=x4+t2[i]*t2[i]
        x5=x5+t1[i]*t1[i]
    c=((n*x3)-(x1*x2))/math.sqrt((n*x4-(x1*x1))*(n*x5-(x2*x2)))
    print(c)
    if c==0:
        print('No correlation')
    elif c>0:
        print('Positive Correlation')
    else:
        print('Negative Correlation')

print('The maximum, average, minimum, median, and standard deviation of the reported monthly temperature means for each month and for the year during the period 2006 – 2022')
print(stats(files[0],1))

print('\n The maximum, average, minimum, median, and standard deviation of the reported monthly rainfall (measured in inches) for each month and total for the years during the period 2006 – 2022')
print(stats(files[1],2))

print('\n The maximum, average, minimum, median, and standard deviation of the reported monthly snowfall (measured in inches) for each month and total for the years during the period 2006 – 2022')
print(stats(files[2],3))

print('\n The average data from the tables in the parts a and b, determine correlation between monthly rainfall and monthly mean temperature is \n')
correlation1(files[0],files[1])

print('\n The average data from the tables in the parts a and c, determine correlation between monthly mean snowfall and monthly mean temperature is \n')
correlation1(files[0],files[2])

print('\n')



        


    


