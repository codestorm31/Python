'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word twinkle.
'''

with open("poems.txt") as f:
    content=f.readline()
    if("Twinkle" in content):
        print("Found Twinkle")
    else:
        print("Not Found")
