# Defining List for Python Class
Python = ['Sneha', 'Suyash', 'Gutlu', 'Bubba', 'Raju', 'Plam', 'Aditya']

# Defining List for Web Application
WebApp = ['Gutlu', 'Swati', 'Aditya', 'Plam']

# List to hold number of students who are attending Python but not Web Application
pythonNotWebApp = []

# Logic to fill new list
for p in Python:
    if p not in WebApp:
        pythonNotWebApp.append(p)

# Driver Program
if __name__ == "__main__":
    print('The student who are attending Python and not WebApplication Class are: ', pythonNotWebApp)