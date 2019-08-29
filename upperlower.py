def count(str):
    lowercase = 0
    uppercase = 0
    for c in str:
        if str.isupper:
            uppercase += 1
            print(uppercase)
        elif str.islower:
            lowercase += 1
            print(lowercase)
        else:
            pass
count('BrillerSys')