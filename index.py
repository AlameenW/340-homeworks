with open ("INPUT/Student.csv","r") as file:
    file.readline()
    StdRec = dict(map(lambda line: (line.split(',')[0], line.split(',')[1:]), file.read().strip().split('\n')))
    print(StdRec)
