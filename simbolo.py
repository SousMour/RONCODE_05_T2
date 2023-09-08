def simbolo(x):
    if x.isalpha() or x.isdecimal():
        return False
    else:
        return True
x=input()
a=simbolo(x)
print(a)
