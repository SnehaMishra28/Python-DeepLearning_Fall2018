sentence = input("Enter your sentence here - ")
length = len(sentence)
numbers = 0
letters = 0
space = 0
random = 0
for i in sentence:
    if i.isalpha():
        letters += 1
    elif i.isnumeric():
        numbers += 1
    elif i.isspace():
        space += 1
    else:
        random +=1
print("Letters in sentence are - ",letters)
print("Numbers in sentence are - ",numbers)
print("Spaces in sentence are - ",space)
print("Random variables in sentence are - ",random)