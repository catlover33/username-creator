#template = {year of enrolment}{first name}.{surname}@gmail.com
address = ("@gmail.com")

year = input("What year will you be enrolling in the school?\n> ")
first_name = input("What is your first name?\n> ")
surname = input("What is your surname?\n> ")

print("Your new E-Mail address is " + year[2: 4] + first_name + "." + surname + address)