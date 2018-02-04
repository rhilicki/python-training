import os
import random
path1 = os.getcwd()
print(path1)

somenum = random.random()
# print somenum

# print(random.choice([1,2,3,4]))

S = 'shubbery'
L = list(S)
# print(dir(S))
# print L[11]  

f = open('data.txt', 'w')
f.write('Oi dude where are thou\n')
f.write('again')
f.close()

f = open('data.txt', 'r')
text = f.read()
# print(text)

print text.split()[-4]
print text.split()[-3]
print text.split()[-2]
print text.split()[-1]
print text.split()[0]
print text.split()[1]
print text.split()[2]
print text.split()[3]


E = {'cto': {'name': 'Bob', 'age': 40}}
print E['cto']['age']