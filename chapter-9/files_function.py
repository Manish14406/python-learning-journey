# f = open("files.txt")

# data = f.readlines()
# print(data,type(data))
# f.close()

# f = open("files.txt")

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# line5 = f.readline()
# print(line5=="")


f = open("files.txt")
line=f.readline()

while(line != ""):
    print(line)
    line=f.readline()
f.close()