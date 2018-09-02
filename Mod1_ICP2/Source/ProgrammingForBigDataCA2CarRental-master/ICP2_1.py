# Ask User's input
valuesInput = input("Input some number : ")
# define list 'a' to append 1st and last values of list
a=[]
# define list 'l' to collect the user input elements in list
l = []
# iterate through the user input elements to append in list 'l'
for i in valuesInput.split(","):
    l.append(i)
# Get the 1st and last value in th elist
a.append(l[0])
a.append(l[-1])
# Print out the elements of list 'a'
print(a)
# Convert the list 'a' to tuple
t = tuple(a)
# Print out the elements of tuple 't'
print(t)