def read_file(file_name):
    file = open(file_name, "r")

    table = file.readlines()
    for i in range(len(table)):
        table[i] = table[i].replace("\n", "")
        temp = table[i].split(" ")
        table[i] = [float(temp[0]), float(temp[1]), 1]
    
    return table