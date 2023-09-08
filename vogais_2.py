def vogais(x):
    vogal =['a','e','i','o','u']
    if x in vogal:
        return True
    else:
        return False
x=input()
x=x.lower()
resultado=vogais(x)
print(resultado)
