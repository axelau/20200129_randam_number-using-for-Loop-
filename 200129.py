import random

Biglists = []
count = 1


for loop in range(40):
    list = []
    for x in range(4):
        list.append(random.randint(0,9))
    #print(list)
    Biglists.append(list)
    count += 1

x = 1
total = len(Biglists)
print('totol:', 'total')
for loop in Biglists:
	print('The', x, 'nunber is',loop)
	x +=1


with open('200129.txt', 'w') as f:
	for s in Biglists:
		f.write(str(s[0])+str(s[1])+str(s[2])+str(s[3])+'\n')