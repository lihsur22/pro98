def swapFileData():
    file1 = input("Enter File Name : ")
    file2 = input("Enter File Name : ")
    with open(file1,'r') as a:
        data_1 = a.read()
    with open(file2,'r') as a:
        data_2 = a.read()
    with open(file1,'w') as a:
        for line in data_2:
            a.write(line)
    with open(file2,'w') as a:
        for line in data_1:
            a.write(line)
            
swapFileData()