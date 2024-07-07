f=open("new.txt")

# lines=f.readlines()

# line1=f.readline()
# print(line1, type(line1))

line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()