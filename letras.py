def letras(x):
    vogal=['a','e','i','o','u']
    consoante=['z','x','c','v','b','n','m','s','d','f','g','h','j','k','l','ç','q','w','r','t','y','p']
    if x in vogal or consoante:
        return True
    else:
        return False
x=input()
x=x.lower()
resultado=letras(x)
print(resultado)
