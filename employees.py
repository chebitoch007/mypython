from functions import employee


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.salary = position
        self.position = salary

        def details(self):
            print(self.name,"is the", self.position,"and earns", self.salary)

        employee1=Employee("John","CEO","450000")
        print(employee1.name, employee1.position, employee1.salary)

        employee2=Employee("Jane","HR","350000")
        print(employee2.name, employee2.position, employee2.salary)

        employee3=Employee("Eunice","Accountant","300000")
        print(employee3.name, employee3.position, employee3.salary)





