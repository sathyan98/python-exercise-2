class rectangle:

    def __init__(self):
        self.l = ''
        self.w = ''
        self.result = ''

    def length(self):
        self.l = input("enter the length")

    def width(self):
        self.w = input("enter the width")

    def calc(self):
        self.result = self.l *(self.w)
        print(int(self.result))


rec = rectangle()
rec.length()
rec.width()
rec.calc()

# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
#self.w shows as string