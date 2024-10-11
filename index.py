with open ("INPUT/Student.csv","r") as file:
    file.readline()
    StdRec = dict(map(lambda line: (line.split(',')[0], line.split(',')[1:]), file.read().strip().split('\n')))
    print(StdRec)
    file.seek(0)
    header = tuple(file.readline().strip().split(','))
    print(header)
    data = file.read().strip().split('\n')
    print(data)

    token = input('Enter a student number:')
    for entry in data:
        if entry.startswith(token):
            result = entry
            print(result)

    f = open(f'RESULT/{token}.csv','w')
    f.writelines(header)
    f.write('\n')
    f.writelines(result)
    f = open(f'RESULT/{token}.csv','r')
    print(f.read())
    f.close()

