def SwapFileData():
    file1 = input("Enter name of first file :  ")
    file2 = input("Enter name of second file :  ")
    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        data_a.write(data_b)

    with open(file2, 'w') as b:
        data_b.write(data_a)

SwapFileData()
    
    
