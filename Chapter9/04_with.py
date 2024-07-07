# f=open("new.txt")
# print(f.read())
# f.close()

# Same can be written by with statement like this:

with open("new.txt") as f:
    print(f.read())
# YOU DONT HAVE TO EXPLICITLY CLOSE THE FILE
