days = ['monday','tuesday','wednesday','thursday','friday']


with open('test', "w") as wrfile:
    for i in days:
        wrfile.write(i)
cont = open('test')
print(cont.read())