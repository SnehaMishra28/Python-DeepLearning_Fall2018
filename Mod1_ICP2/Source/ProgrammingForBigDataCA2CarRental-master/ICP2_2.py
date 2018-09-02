# Get the User file in read mode
inputFile = open("input.txt", "r")
# Get the 1st character of the file
firstChar = inputFile.read(1)
data = inputFile.read()
# If the 1st character is not available, then file is empty
if not firstChar:
    print("The file is empty!")
else:
    # Get the words of in opened file (separated by space)
    words = data.split(" ")
    # Get the sentences of the opened file (separated by new line)
    sentences = data.split("\n")
    # setting the variable to hold line numbers in the file
    lineNumber = 1
    # looping through each sentences of the file
    for x in sentences:
        wordsInSentence = 0
        charInSentence = 0
        # looping through each characters of the selected sentence
        for i in x:
            charInSentence += 1
        # looping through each words of the selected sentence (separated by space)
        for y in x.split(" "):
            wordsInSentence += 1
        # print the sentence - words and character count
        print(x, " - ", wordsInSentence, ",", charInSentence)
        # Increment th eline number before the next sentence in th eloop
        lineNumber += 1
# Close the opened file
inputFile.close()