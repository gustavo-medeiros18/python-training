#* input() function is used to receive data from standard input device.
#* default input device is keyboard. It always returns the string that
#* has been read.
input()

#* It is possible to pass a string to the input() function. This string
#* will be used as a prompt to the user.
name = input("Enter your name: ")
print("Hello", name)