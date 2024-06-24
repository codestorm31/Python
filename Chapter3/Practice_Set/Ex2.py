'''
2. Write a program to fill in a letter template given below with name and date.
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

from datetime import date

Name=input("Enter name:")
date=str(date.today())

letter='''
    Dear <|Name|>,
    You are selected!
    <|Date|>    
'''

print(letter.replace("<|Name|>",Name).replace("<|Date|>",date))
