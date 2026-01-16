class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, employee_id=None, name=None, age=None, salary=None):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, new_id):
        self.__employee_id = new_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object destroyed")


class Manager(Employee):
    def __init__(self, employee_id=None, name=None, age=None, salary=None, department=None):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, employee_id=None, name=None, age=None, salary=None, programming_language=None):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


person = None
employee = None
manager = None
developer = None

print("--- Python OOP Project: Employee Management System ---")

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)
            print(f"Person created with name: {name} and age: {age}.")

        case 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(emp_id, name, age, salary)
            print("Employee created successfully")

        case 3:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager = Manager(emp_id, name, age, salary, dept)
            print("Manager created successfully")

        case 4:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            developer = Developer(emp_id, name, age, salary, lang)
            print("Developer created successfully")

        case 5:
            found = False

            if person:
                print("\nPerson Details:")
                person.display()
                found = True
            else:
                print("\nPerson: No record found")

            if employee:
                print("\nEmployee Details:")
                employee.display()
                found = True
            else:
                print("\nEmployee: No record found")

            if manager:
                print("\nManager Details:")
                manager.display()
                found = True
            else:
                print("\nManager: No record found")

            if developer:
                print("\nDeveloper Details:")
                developer.display()
                found = True
            else:
                print("\nDeveloper: No record found")

            if not found:
                print("\nNo records available.")

            print("\nSubclass Checks:")
            print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
            print("Is Developer subclass of Employee?", issubclass(Developer, Employee))

        case 6:
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

        case _:
            print("Invalid choice. Try again.")
