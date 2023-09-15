import random

outfile = open('numbers.txt', 'w')

for x in range(100):
    outfile.write(str(random.randint(1,11)) + '\n')
outfile.close()
print('done')


mylist = []
infile = open('numbers.txt', 'r')

for y in range(100):
    mylist.append(int(infile.readline()))
infile.close()
print(mylist)