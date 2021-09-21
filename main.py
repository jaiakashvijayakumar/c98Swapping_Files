def swapfile():
    file_Name1 = input("Enter the file name : ")
    file_Name2 = input("Enter the file name : ")

    with open(file_Name1, "r") as a:
        file_Name1_data = a.read()

    with open(file_Name2 , "r") as b:
        file_Name2_data = b.read()    

    with open(file_Name1, "w") as a:
        a.write(file_Name2_data)

    with open(file_Name2, "w") as b:
        b.write(file_Name1_data)       

swapfile()        