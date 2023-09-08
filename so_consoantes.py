def letra(x):
    cons=['z','x','c','v','b','n','m','s','d','f','g','h','j','k','l','ç','q','w','r','t','y','p']
    if x in cons:
        return True
    else:
        return False
x=input()
x=x.lower()
x=letra(x)
print(x)
