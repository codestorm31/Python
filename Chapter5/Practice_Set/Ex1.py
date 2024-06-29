'''1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!'''

dict = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "आप कैसे हैं?": "How are you?",
    "मैं ठीक हूं": "I'm fine",
    "कल मिलते हैं": "See you tomorrow",
    "किताब": "Book",
    "पानी": "Water",
    "सूरज": "Sun",
    "चांद": "Moon"
}

while True:
    inp=input("Enter Hindi Word (or Exit): ")
    if(inp.lower()=="exit"):
        print("Exited!")
        break
    if inp in dict:
        print("In English:",dict[inp])
    else:
        print("Sorry Not found")