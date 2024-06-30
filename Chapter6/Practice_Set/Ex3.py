'''3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''


str=input("Enter comment:")

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

flag=False
for i in spam_keywords:
    if i.lower() in str.lower():
        print("Spam")
        flag=True
        break

if flag==False:
    print("Not Spam")