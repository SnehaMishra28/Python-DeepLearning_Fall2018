fname = input("Input you 1st name: ")
lname = input("Enter your last name:")
print("Entered name is - " + fname+" "+lname)

print(''.join(reversed(lname + ' ' + fname)))