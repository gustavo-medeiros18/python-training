#* Variable declaration example. Python is a dynamically typed language, so
#* you don't need to declare the type of a variable when you create one.
#* Python automatically assigns data types to variables based on the value
#* assigned to it.

number = 10
print(number)

#* Python automatically puts a space between the string and the value
print('The value of number is', number)

#* You can also use the + operator to concatenate strings and variables.
#* However, you need to convert the variable into a string using the str()
#* function. Because the + operator only works with strings.
print('The value of number is ' + str(number))

salary = 20.10
firstName = 'Gustavo'
isProgrammer = True

#* Two ways to concatenate strings and variables
print(firstName + ' earns ' + str(salary) + ' and is a programmer? ' + str(isProgrammer))
print(firstName, 'earns', salary, 'and is a programmer?', isProgrammer)
