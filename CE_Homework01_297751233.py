files = [
    r"C:\Users\vaths\OneDrive\Desktop\CIS_500_S24_CE1_DiseaseTrueIncidence.txt",
    r"C:\Users\vaths\OneDrive\Desktop\CIS_500_S24_CE1_FalsePositive.txt ",
    r"C:\Users\vaths\OneDrive\Desktop\CIS_500_S24_CE1_TruePositive.txt"
]
Pcount = []
Ncount = []
Totalcount = []

for i in range(0,len(files)):
    x1=files[i]
    with open(x1, 'r') as x2:
        j = x2.read()
        Pcount.append(j.count('P'))
        Ncount.append(j.count('N'))
        Totalcount.append(j.count('P')+j.count('N'))
print('No of cows that are healthy : ' , Ncount[0])  
print('No of cows that are infected : ' , Pcount[0])  
print('Total no of cows : ',Totalcount[0])
print('No of cows that are healthy is negative : ' , Ncount[1]) 
print('No of cows that are healthy is positive : ' , Pcount[1])
print('Total no of cows : ',Totalcount[1])
print('No of cows that are infected is negative : ' , Ncount[2])
print('No of cows that are infected is positive : ' , Pcount[2]) 
print('Total no of cows : ',Totalcount[2],'\n')

print('Question a\n')
a = Pcount[0]/Totalcount[0]
print('The incidence of the infected cows in Syracuse greater area ' , a ,'\n')

print('Question b\n')
b = Pcount[2]/Totalcount[2]
print('The probability that a cow will be tested positive if it is really infected ' , b ,'\n')

print('Question c\n')
c = Pcount[1]/Totalcount[1]
print('The probability that a cow will be tested positive if it is really healthy ' , c , '\n')

print('Question d\n')
d = b*a/(b*a+c*(1-a))
print('The probability that a cow has the mad cow disease given a positive test ' , d , '\n')

print('Question e\n')
e = (1-b)*a/(a*(1-b)+(1-c)*(1-a))
print('The probability of a cow has the mad cow disease given NOT tested ' , e , '\n')