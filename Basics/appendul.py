def myfunc(word):
    new_word = []
    for x in range (len(word)):
        if x%2==0:
            new_word.append(word[x].upper())
        else:
            new_word.append(word[x].lower())
    return ''.join(new_word)      
print(myfunc("rhombicosidodecahedron"))     

