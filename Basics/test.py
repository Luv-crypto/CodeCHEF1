def myfunc(word):
    new_word = []
    for x in range (len(word)):
        if x%2==0:
            new_word.append(word[x].lower())
        else:
            new_word.append(word[x].upper())
        return '.join(new_word)'
myfunc("bot")     

