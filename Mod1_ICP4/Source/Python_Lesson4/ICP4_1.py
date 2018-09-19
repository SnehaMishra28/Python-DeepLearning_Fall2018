# Lab 4 Employee Class Define and Use Case
class Employee:
    emp_count = 0  # Class Attribute Data Member

    def __init__(self, nam, fam, sal, dep):
        self.name = nam
        self.family = fam
        self.salary = sal
        self.department = dep                # Data Attribute
        Employee.emp_count += 1

    def getempcount(self):
        return self.__class__.emp_count

    def getname(self):
        return self.name

    def getsalary(self):
        return self.salary

    def getfamily(self):
        return self.family

    def getdep(self):
        return self.department


# Inherting the base class Employee
class FullEmployee(Employee):

    def __init__(self, nam, fam, sal, dep, bon):
        Employee.__init__(self, nam, fam, sal, dep)  # Call base class constructor
        self.bonus = bon

    def getbonus(self):
        return self.bonus



def avgsalary(staff):
    result = 0
    for e in staff:
        result += e.getsalary()
        print(result)
    avg1 = result/e.getempcount()
    print(avg1)
    print(e.getempcount())
    return avg1


emp1 = Employee('Razu', 'B', 30000, 'IT')
emp2 = Employee('Swati', 'A', 30000, 'HR')

boss = FullEmployee('Adam', 'M', 30000, 'CEO', 50000)


# Definig list to hold all employees for iterating and calling there function
staffs = []

# Appending the objects in the list
staffs.append(emp1)
staffs.append(emp2)


for f in staffs:
    print('Employee Name : ', f.getname(), 'Employee Salary : ', f.getsalary(), 'Employee Bonus : ', f.getdep(),
          'The employee Count is:', f.getempcount())


print(boss.getname(), boss.getsalary(), boss.getbonus())
print()
print('The average salary of Employeess', avgsalary(staffs))