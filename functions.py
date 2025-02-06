#Built-in functions / Standard library functions

y = max(67, 43, 89, 27,38)
print("The maximum value is", y)

x = min(67, 43, 89, 27,38)
print("The minimum value is", x)

def name():
      print("Eliphaz")

name() #Calling a function

def multiply():
    x=3
    y=4
    print(x*y)
multiply()

#Parameter and argument
def add(a, b):
   print(a+b)
add(6, 8)

def employee(name, age, position, salary):
    print(name, age, position, salary)

employee("Mark", "52", "CEO", 2000000)
employee("John", "45", "Chairman of the Board", 1800000)
employee("Lillian", "37", "Managing Director", 1700000)
employee("Mary", "40", "HR", 1200000)


print("    ")
# A program that displays details of five students
# Use a user-defined function with the parameters and argument
#Include fullname, age, course and gender


def student(fullname, age, course, gender):
    print(fullname, age, course, gender)

student("Mark Walker", "17", "Cyber Security","male")
student("Mary Bailey", "18", "Full stack","female")
student("Johanna Seymour", "17", "Data Science","female")
student("Henry VIII", "19", "Android Programming","male")
student("Thomas More", "16", "MIT","male")






