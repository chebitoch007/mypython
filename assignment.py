# 1. A program to check whether a year is a leap year or not
year = int(input("Enter year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year".format(year))
else:
    print(year,"is not a leap year".format(year))

# 2. A program to check whether a letter is a consonant or a vowel



# 3. A program to check whether a letter input by the user is a consonant or a vowel
letter = input("Enter a character: ")

if(letter=='A' or letter=='a' or letter=='E' or letter =='e' or letter=='I'
 or letter=='i' or letter=='O' or letter=='o' or letter=='U' or letter=='u'):
    print(letter, "is a Vowel")
else:
    print(letter, "is a Consonant")

