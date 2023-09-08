def variavel(x):
    n=['0','1','2','3','4','5','6','7','8','9']
    if x.isalpha() or x in n:
        return True
    else:
        return False


x=input()
x=x.lower()
resultado=variavel(x)
print(resultado)
