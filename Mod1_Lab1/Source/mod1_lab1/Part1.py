# Ask user Input String
str = input('Enter String here - ')

# Removing spaces from input string and
# converting string to lower case as D not equal to d
# which will give incorrect output
new_str = str.replace(" ", "").lower()
length1 = len(new_str)

# defining a dictionary to hold for character from string
freq_dict1 = {}

# Buliding the dictionary  with count from User input string
for i in range(0, length1):
    c = new_str[i]
    val = freq_dict1.get(c)
    if val is not None:
        freq_dict1[c] = val + 1
    else:
        freq_dict1[c] = 1

# looping through dictionary and printing first non repeating element.
for c in new_str:
    if freq_dict1[c] == 1:
        print('The first non repeating character in User str is: ', c)
        break