class Upperpr:

    def __init__(self):
        self.str =''

    def get_string(self):
        self.str = input("enter the string")


    def print_string(self):
        print(self.str.upper())
str = Upperpr()
str.get_string()
str.print_string()













#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.