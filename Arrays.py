
courses = ["MIT", "Cyber security", "Data Science"]
print(courses)

#Accessing an element
print(courses[2])

#Looping through an array
for a in courses:
    print("Course is",a)

#Adding a new element into an array
courses.append("Laravel")
print(courses)

#Deleting an element from an array
courses.remove("Data Science")
print(courses)


