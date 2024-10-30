f = open('Student.csv')
stdRec = dict(map(lambda line: (line.strip().split(',')[0],line.split(',')[1:]), f.read().strip().split('\n')))
f.seek(0)
header = f.readline().strip().split(',')
data = f.read().strip().split('\n')
f.close()
token = input('Enter a student number to search: ')
for index in range(len(data)):
    if data[index].startswith(token):
        result = data[index]
        print(data[index])
f2 = open(f'{token}.csv','w')
f2.writelines(header)
f2.writelines(result)
f2.close()
f2 = open(f'{token}.csv','w')
f2.read()